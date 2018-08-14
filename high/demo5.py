# reduce(function, sequence, initial)
from functools import reduce

list_x = [1, 2, 3, 4, 5, 6]

r = reduce(lambda x, y: x + y, list_x, 100)
print(r)
