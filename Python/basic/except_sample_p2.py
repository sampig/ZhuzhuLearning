#!/usr/bin/env python2.7


def exe_finally():
    try:
        print "try 1."
        return
        print "try 2."
    except:
        print "except"
    finally:
        print "finally 1"


def raise_exept():
    try:
        raise NameError("A name error")
    finally:
        print "finally 2"


exe_finally()
try:
    raise_exept()
except:
    print "Error"
