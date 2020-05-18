from functools import reduce
from operator import add
def sum_array(arr):
    return reduce(add, arr, 0)

print(sum_array([1, 2, 3, 4]))
