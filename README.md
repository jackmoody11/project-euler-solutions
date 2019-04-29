# Project Euler

This repo hosts my personal solutions to Project Euler questions and is intended to help with ideas **after** writing your own solutions.

## The Process
---------------
1. Solve the problem on your own
2. Check if you got it right on the [Project Euler website](https://projecteuler.net)
3. See if my solutions give you any ideas on how to optimize
4. If you found a better way, send a pull request!


Note: My solutions are by **no** means optimized. They are a work in progress.

## Testing
----------
You can test any of the Python solutions. I would appreciate any help with testing in Java and/or C as well. To test all Python solutions, while in the python directory you can run

```sh
python3 tests.py
```

The output will look something like this:
```
Problem 001:       0 ms
Problem 002:       0 ms
Problem 003:     108 ms
Problem 004:     296 ms
Problem 005:       0 ms
...
Problem 071:       0 ms
Problem 073:    4131 ms
Total computation time: 85898 ms
67 problems solved
```

If you would like to only run specific tests, you can do so by running something like
```sh
# Separate each problem number with a space (no zero padding)
python3 tests.py 2 3 5 7
```

which will output

```
Problem 002:       0 ms
Problem 003:     111 ms
Problem 005:       0 ms
Problem 007:      13 ms
Total computation time: 134 ms
4 problems solved
```

If you would like to graph the execution times of the problems tested, you can add the `-g` or `--graph` argument.

```sh
# -g and --graph are equivalent
python3 tests.py 1 2 3 4 5 6 7 8 9 10 -g
```

![Tests with graph](/tests_graph.png)

In order to ensure the functions in utils are working as expected (without creating an official testing folder), doctests have been added to the docstrings. Adding the `--doctest` option when running tests.py will run a verbose doctest on utils.py.

### Progress
![My Project Euler Badge](https://projecteuler.net/profile/jackmoody11.png)


| Problem # | Python | C | Java |
| ------ | ------ | - | ---- |
| 001 | [Solution](/python/p001.py) - [Alternate Solution](/python/p001_alt.py)  | [Solution](/c/p001.c) | [Solution](/java/p001.java) |
| 002 | [Solution](/python/p002.py) | [Solution](/c/p002.c) | [Solution](/java/p002.java) |
| 003 | [Solution](/python/p003.py) | [Solution](/c/p003.c) | [Solution](/java/p003.java) |
| 004 | [Solution](/python/p004.py) | [Solution](/c/p004.c) | [Solution](/java/p004.java) |
| 005 | [Solution](/python/p005.py) | [Solution](/c/p005.c) | X |
| 006 | [Solution](/python/p006.py) | [Solution](/c/p006.c) | X |
| 007 | [Solution](/python/p007.py) | [Solution](/c/p007.c) | X |
| 008 | [Solution](/python/p008.py) | [Solution](/c/p008.c) | X |
| 009 | [Solution](/python/p009.py) | [Solution](/c/p009.c) | X |
| 010 | [Solution](/python/p010.py) | [Solution](/c/p010.c) | X |
| 011 | [Solution](/python/p011.py) | X | X |
| 012 | [Solution](/python/p012.py) | [Solution](/c/p012.c) | X |
| 013 | [Solution](/python/p013.py) | X | X |
| 014 | [Solution](/python/p014.py) | [Solution](/c/p014.c) | X |
| 015 | [Solution](/python/p015.py) | [Solution](/c/p015.c) | X |
| 016 | [Solution](/python/p016.py) | X | X |
| 017 | [Solution](/python/p017.py) | X | X |
| 018 | [Solution](/python/p018.py) | X | X |
| 019 | [Solution](/python/p019.py) - [Alternate Solution](/python/p019_alt.py) | X | X |
| 020 | [Solution](/python/p020.py) | X | X |
| 021 | [Solution](/python/p021.py) | X | X |
| 022 | [Solution](/python/p022.py) | X | X |
| 023 | [Solution](/python/p023.py) | X | X |
| 024 | [Solution](/python/p024.py) | X | X |
| 025 | [Solution](/python/p025.py) | X | X |
| 026 | [Solution](/python/p026.py) | X | X |
| 027 | [Solution](/python/p027.py) | X | X |
| 028 | [Solution](/python/p028.py) | X | X |
| 029 | [Solution](/python/p029.py) | X | X |
| 030 | [Solution](/python/p030.py) | X | X |
| 031 | [Solution](/python/p031.py) | X | X |
| 032 | [Solution](/python/p032.py) | X | X |
| 033 | [Solution](/python/p033.py) | X | X |
| 034 | [Solution](/python/p034.py) | X | X |
| 035 | [Solution](/python/p035.py) | X | X |
| 036 | [Solution](/python/p036.py) | X | X |
| 037 | [Solution](/python/p037.py) | X | X |
| 038 | [Solution](/python/p038.py) | X | X |
| 039 | [Solution](/python/p039.py) | [Solution](/c/p039.c) | X |
| 040 | [Solution](/python/p040.py) | X | X |
| 041 | [Solution](/python/p041.py) | X | X |
| 042 | [Solution](/python/p042.py) | X | X |
| 043 | [Solution](/python/p043.py) | X | X |
| 044 | [Solution](/python/p044.py) | X | X |
| 045 | [Solution](/python/p045.py) | X | X |
| 046 | [Solution](/python/p046.py) | X | X |
| 047 | [Solution](/python/p047.py) | X | X |
| 048 | [Solution](/python/p048.py) | X | X |
| 049 | [Solution](/python/p049.py) | X | X |
| 050 | [Solution](/python/p050.py) | X | X |
| 051 | X | X | X |
| 052 | [Solution](/python/p052.py) | X | X |
| 053 | [Solution](/python/p053.py) | X | X |
| 054 | [Solution](/python/p054.py) | X | X |
| 055 | [Solution](/python/p055.py) | X | X |
| 056 | [Solution](/python/p056.py) | X | X |
| 057 | [Solution](/python/p057.py) | X | X |
| 058 | [Solution](/python/p058.py) | X | X |
| 059 | [Solution](/python/p059.py) | X | X |
| 060 | X | X | X |
| 061 | X | X | X |
| 062 | [Solution](/python/p062.py) | X | X |
| 063 | [Solution](/python/p063.py) | X | X |
| 064 | X | X | X |
| 065 | [Solution](/python/p065.py) | X | X |
| 066 | X | X | X |
| 067 | [Solution](/python/p067.py) | X | X |
| 068 | [Solution](/python/p068.py) | X | X |
| 069 | [Solution](/python/p069.py) | X | X |
| 070 | [Solution](/python/p070.py) | X | X |
| 071 | [Solution](/python/p071.py) | X | X |
| 072 | [Solution](/python/p072.py) | X | X |
| 073 | [Solution](/python/p073.py) | X | X |
| 074 | [Solution](/python/p074.py) | X | X |
| ... | X | X | X |
| 080 | [Solution](/python/p080.py) | X | X |
| ... | X | X | X |
| 097 | [Solution](/python/p097.py) | X | X |
