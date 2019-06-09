#!/usr/bin/env python2.7

import random


# Generate a pseudo-random number between 0 and 1.
print random.random()

# Pick a random number between 1 and 100.
print random.randint(1, 100)

# Generate a random floating point number between 1 and 10
print random.uniform(1, 10)

# shuffle a list
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(items)
print items

# pick random number from a list
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = random.sample(items, 1)
print x[0]
print x
y = random.sample(items, 4)
print y

languages = ["Python", "Java", "SQL", "C", "JavaScript"]
lang = random.sample(languages, 1)
print lang[0]
langs = random.sample(languages, 3)
print langs
