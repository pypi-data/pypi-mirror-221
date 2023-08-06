# `kioss`
**Keep I/O Simple and Stupid**

[![Actions Status](https://github.com/bonnal-enzo/kioss/workflows/test/badge.svg)](https://github.com/bonnal-enzo/kioss/actions) [![Actions Status](https://github.com/bonnal-enzo/kioss/workflows/PyPI/badge.svg)](https://github.com/bonnal-enzo/kioss/actions)

## Install

`python -m pip install kioss`

## Overview

```python
from kioss import Pipe

words_count: int = (
    Pipe(open("...", "r"))
    .map(str.split)
    .explode()
    .map(lambda _: 1)
    .reduce(int.__add__)
)
```

## Features
- `.slow` a pipe to limit the iteration's speed over it to a given `freq`
- `.catch` any pipe's error to treat it after iteration
- `.batch` pipe's elements and yield them as lists of a given max size or spanning over a given max period.
- `.map` over pipe's elements uing multiple threads
- `.merge` several pipes to form a new one that yields elements using multiple threads
- `.log` a pipe's iteration status
- `.list` a pipe to collect its output into a list having an optional max size
- `reduce` a pipe
- `filter` a pipe


## Setup

```bash
python -m venv .venv
source ./.venv/bin/activate
python -m unittest
python -m black kioss/* test/* 
```
