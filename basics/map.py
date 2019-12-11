def double(n):
    return (n+n)
nums = [int(x) for x in input('Enter nums to double ').split()]
res = map(double,nums)
print('Doubled list ',list(res))

