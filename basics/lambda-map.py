#!/bin/python3
nums = [int(x) for x in input('Enter nums to double ').split()]
res = map(lambda x:x+x,nums)
print('Doubled list ',list(res))

