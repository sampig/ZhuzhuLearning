#!/usr/bin/env python

import subprocess
from subprocess import Popen, PIPE


process = Popen(["cat", "subprocess_sample.py"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)

# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
subprocess.call(["ls", "-l"])

# subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
s = subprocess.check_output(["echo", "Hello zhuzhu!"])
print("s = " + str(s))


print("\n")
s = subprocess.check_output(["ping", "-c 1", "www.google.com"])
print("s = " + str(s))

s = subprocess.check_output(["ping", "-c 4", "google.com"])
output = s.decode("utf-8")
lines = output.split('\n')
for line in lines:
    print(line)


