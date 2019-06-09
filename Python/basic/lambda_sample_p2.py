#!/usr/bin/env python2.7


f = lambda x: 2 * x
g = lambda x: x > 10

print(f(5))
print(g(5))
print(g(25))

list = [1, 2, 3, 4, 5]
squaredList = map(lambda x: x * x, list)
print(squaredList)

filterList = filter(lambda x: x % 2 == 0, list)
print(filterList)

reduceList = reduce(lambda x, y: x + y, list)
print(reduceList)


def my_lambda_func(p):
    return lambda p1, p2: (p1 + p2) * p


f = my_lambda_func(5)
print(f(2, 3))

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
