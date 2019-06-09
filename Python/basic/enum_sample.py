#!/usr/bin/env python


# An old way to create enums:
def enum(**enums):
    return type("Enum", (), enums)


Numbers = enum(ONE=1,TWO=2, THREE=3, FOUR=4, FIVE=5, SIX=6)
print(type(Numbers))
print(Numbers.ONE)
print(Numbers.FIVE)


# In Python2.7,
# from aenum import Enum


# In Python3.5+
# from enum import Enum
