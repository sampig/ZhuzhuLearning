#!/usr/bin/env python2.7


import os.path


def read_file():
    filename = ""
    if filename == "":
        filename = input("input file:")
    else:
        filename = "test.csv"
    if not os.path.isfile(filename):
        print "File does not exist."
        return
    print "read file:", filename
    with open(filename) as f:
        content = f.readlines()
    for line1 in content:
        print line1
        break
    print "Lines:", len(line1)
    with open(filename) as f:
        content2 = f.read().splitlines() # without "\n"
    for line2 in content2:
        print line2
        break
    print "Lines:", len(line2)


def write_file():
    filename = str(raw_input("output file:"))
    if not os.path.isfile(filename):
        print "Create a new file:", filename
        file = open(filename, "w")
    else:
        print "Append the existing file:", filename
        file = open(filename, "a")
    file.write("zhuzhu test.\n")
    file.close()


if __name__ == "__main__":
    read_file()
    write_file()
