# NumPy

NumPy is a core library for scientific computing in Python
- Data Science, Machine Learning, Deep Learning
- scikit-learn, matplotlib, pandas, ....

NumPy code is written in C Programming Language, it boosts the performance of the multidimensional array while doing the mathematical operations with arrays.

## Installation
Install [NumPy](https://pypi.org/project/numpy/) using [pipenv](https://pypi.org/project/pipenv/) or [pip](https://pypi.org/project/pip/).

```
pipenv install numpy

OR

pip install numpy
```

**Import `NumPy` and check the version of recently installed python library or package**
```
import numpy as np

print(np.__version__)
```

**Create an array and analyse it's shape, data type, dimension, size of array, byte size**
```
num = np.array([1, 2, 3])

print(num)

print(num.shape)

print(num.dtype)

print(num.ndim)

print(num.size)

print(num.itemsize)
```

The [main.py](/NumPy/main.py) file includes all the examples:



---
[Back](/README.md)