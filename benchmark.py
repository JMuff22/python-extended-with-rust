import numpy as np
from rust_ext import axpy
import timeit
import sys

a=42
try:
    n = int(sys.argv[1])
except:
    n = 1000

x = np.random.rand(n)
y = np.random.rand(n)

def rumpy_bench():
    return axpy(a,x,y)

def numpy_bench():
    return a*x + y

c = np.zeros(n)

def python_bench():
    for i in range(n):
        c[i] = a * x[i] + y[i]
    return c

loops=1000
result1 = timeit.timeit(stmt='rumpy_bench()', globals=globals(), number=loops)
result2 = timeit.timeit(stmt='numpy_bench()', globals=globals(), number=loops)
result3 = timeit.timeit(stmt='python_bench()', globals=globals(), number=loops)
print("Rumpy: ", result1*1000, " ms")
print("Numpy: ", result2*1000, " ms")
print("Standard Python: ", result3*1000, " ms")