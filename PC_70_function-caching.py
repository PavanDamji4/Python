# This is 70th code of this python course
# This code demonstrates the use of function caching

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fun(n):
    time.sleep(5)
    return n

print(fun(3))
print(fun(5))
print(fun(10))
print(fun(34))
print(fun(3))
print(fun(5))
print(fun(10))
print(fun(34))

