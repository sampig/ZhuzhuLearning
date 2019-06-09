#!/usr/bin/env python2.7

import sys


sys.setrecursionlimit(50)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print factorial(30)
print factorial(3)
try:
    print factorial(50)
except Exception, e:
    print e


def add_up(num):
    if num == 1:
        return 1
    else:
        return num + add_up(num - 1)


print add_up(3)
try:
    print add_up(50)
except Exception, e:
    print e
