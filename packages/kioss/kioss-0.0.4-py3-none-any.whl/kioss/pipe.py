import itertools
import logging
import time
import timeit
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from functools import reduce
from queue import Empty, Queue
from typing import Callable, Iterable, Iterator, List, TypeVar

import kioss.util as util

T = TypeVar("T")
R = TypeVar("R")


class Pipe(Iterator[T]):
    def __init__(self, iterator: Iterator[T]) -> None:
        self.iterator: Iterator[T] = iter(
            iterator
        )  # call iter in case it is an iterable that is passed

    def __next__(self) -> T:
        return next(self.iterator)

    def __iter__(self) -> T:
        return self

    def chain(self, *others: Iterable["Pipe[T]"]) -> "Pipe[T]":
        return Pipe[T](itertools.chain(self, *others))

    def merge(self, *others: Iterable["Pipe[T]"]) -> "Pipe[T]":
        return _ConcurrentlyMergingPipe[T]([self, *others])

    def map(
        self, func: Callable[[T], R], num_threads: int = 0, sidify: bool = False
    ) -> "Pipe[R]":
        if sidify:
            func = util.sidify(func)

        if num_threads <= 1:
            return Pipe[R](map(func, self))
        else:

            def iterable():
                executor = ThreadPoolExecutor(max_workers=num_threads)
                # non consumed map results block the worker that produced them, hence it makes it compatible with self.slow()
                yield from executor.map(func, self)
                executor.shutdown()

            return Pipe[R](iter(iterable()))

    def explode(self: Iterable[R]) -> "Pipe[R]":
        return _ExplodingPipe[R](self)

    def filter(self, predicate: Callable[[T], bool]) -> "Pipe[T]":
        return Pipe[T](filter(predicate, self))

    def batch(
        self, max_size: int = 100, max_window_seconds: float = float("inf")
    ) -> "Pipe[List[T]]":
        return _BatchingPipe[T](self, max_size, max_window_seconds)

    def slow(self, freq: int) -> "Pipe[T]":
        return Pipe[T](_SlowingIterator(self, freq))

    def head(self, n) -> "Pipe[T]":
        return Pipe[T](itertools.islice(self, n))

    def catch(self) -> "Pipe[T]":
        return _CatchingPipe[T](self)

    def log(self) -> "Pipe[T]":
        return _LoggingPipe[T](self)

    def reduce(self, f: Callable[[R, T], R], initial: R) -> R:
        return reduce(f, self, initial)

    def list(self, limit: int = float("inf")) -> List[T]:
        return [elem for i, elem in enumerate(self) if i < limit]

    def time(self) -> float:
        def iterate():
            for _ in self:
                pass

        return timeit.timeit(iterate, number=1)


class _ExplodingPipe(Pipe[R]):
    def __init__(self, iterator: Iterator[Iterable[R]]) -> None:
        super().__init__(iterator)
        self.current_iterator_elem = iter(super().__next__())

    def __next__(self) -> R:
        try:
            return next(self.current_iterator_elem)
        except StopIteration:
            self.current_iterator_elem = iter(super().__next__())
            return next(self)


class _CatchingPipe(Pipe[T]):
    def __next__(self) -> T:
        try:
            return super().__next__()
        except Exception as e:
            if isinstance(e, StopIteration):
                raise
            else:
                return e


class _LoggingPipe(Pipe[T]):
    def __init__(self, iterator: Iterator[T]) -> None:
        super().__init__(iterator)
        logging.getLogger().setLevel(logging.INFO)
        self.yields_count = 0
        self.errors_count = 0
        self.last_log_at_yields_count = 0
        self.start_time = time.time()

    def _log(self) -> None:
        logging.info(
            "%s elements have been yielded in elapsed time '%s', with %s errors produced.",
            self.yields_count,
            str(
                datetime.fromtimestamp(time.time())
                - datetime.fromtimestamp(self.start_time)
            ),
            self.errors_count,
        )

    def __next__(self) -> T:
        try:
            elem = super().__next__()
        except StopIteration:
            self._log()
            raise

        self.yields_count += 1
        if isinstance(elem, Exception):
            self.errors_count += 1

        if self.yields_count + self.errors_count >= 2 * self.last_log_at_yields_count:
            self._log()
            self.last_log_at_yields_count = self.yields_count + self.errors_count

        return elem


class _SlowingIterator(Pipe[T]):
    def __init__(self, iterator: Iterator[T], freq: int) -> None:
        super().__init__(iterator)
        self.freq = freq
        self.start = None
        self.yields_count = 0

    def __next__(self) -> T:
        if not self.start:
            self.start = time.time()
        while True:
            while self.yields_count > (time.time() - self.start) * self.freq:
                time.sleep(1 / self.freq)
            self.yields_count += 1
            return super().__next__()


class _BatchingPipe(Pipe[List[T]]):
    def __init__(
        self, iterator: Iterator[T], max_size: int, max_window_seconds: float
    ) -> None:
        super().__init__(iterator)
        self.max_size = max_size
        self.max_window_seconds = max_window_seconds

    def __next__(self) -> List[T]:
        start_time = time.time()
        batch = [next(self.iterator)]
        try:
            while (
                len(batch) < self.max_size
                and (time.time() - start_time) < self.max_window_seconds
            ):
                batch.append(next(self.iterator))
            return batch
        except StopIteration:
            if batch:
                return batch
            else:
                raise


class _ConcurrentlyMergingPipe(Pipe[T]):
    MAX_QUEUE_SIZE = 64
    MIN_SLEEP_TIME_MS = 0.005

    def __init__(self, iterators: List[Iterator[T]]) -> None:
        super().__init__(
            iter(_ConcurrentlyMergingPipe._concurrently_merging_iterable(iterators))
        )

    @staticmethod
    def _pull_in_queue(iterator: Iterator[T], queue: Queue) -> None:
        for elem in iterator:
            backoffed_sleep_time = _ConcurrentlyMergingPipe.MIN_SLEEP_TIME_MS
            while queue.qsize() > _ConcurrentlyMergingPipe.MAX_QUEUE_SIZE:
                time.sleep(backoffed_sleep_time)
                backoffed_sleep_time *= 2
            queue.put(elem)

    @staticmethod
    def _concurrently_merging_iterable(iterators: List[Iterator[T]]) -> Iterator[T]:
        queue = Queue()
        with ThreadPoolExecutor(max_workers=len(iterators)) as executor:
            futures = [
                executor.submit(
                    _ConcurrentlyMergingPipe._pull_in_queue, iterator, queue
                )
                for iterator in iterators
            ]
            while not queue.empty() or not all((future.done() for future in futures)):
                try:
                    yield queue.get(block=False)
                except Empty:
                    time.sleep(0.05)
