"""
echo Two too. | grep -i t[ow]o
Two too.

echo Two too. | grep -i t[aw]o
Two too.

echo Two too tao. | grep -i t[aw]o
Two too tao.
"""

"""
Using regular expressions in Python code:

import Python's built-in re module

use the findall method

method takes two parameters, a regular expression in quotes, and a string to search on

doesn't accept a list

pass in re.IGNORECASE as a third parameter to make a case-insensitive search

pass in re.MULTILINE as a third parameter to to look for matches on
all of the lines of a multi-line screen):
"""

import re

l = "Beautiful is better than ugly."
# l = "Beautiful beautiful gorgeous pretty cute"

# matches = re.findall("Beautiful", l)
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("If", zen, re.MULTILINE)

print(m)

string = "Two too."

s = re.findall("t[wo]o", string, re.IGNORECASE)

print(s)

line = "123?45 hello"

n = re.findall("\d", line, re.IGNORECASE)
# n = re.findall("[[:digit:]]", line, re.IGNORECASE)

print(n)

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

print(found)

for match in found:
    print(match)

# echo I love $ | grep \\$
# I think the first \ is escaping the second \ which is escaping the $

money = "I love $"

x = re.findall("\\$", money, re.IGNORECASE)

print(x)

# Resources

# https://regexr.com/
# https://www.tutorialspoint.com/python/python_reg_expressions.htm

# https://regexone.com/lesson/introduction_abcs
# https://www.regular-expressions.info/tutorial.html
# Mastering Regular Expressions by Jeffrey E.F. Friedl

# CHALLENGE 1

# g Dutch zen.txt

# CHALLENGE 2

# echo Arizona 479, 501, 870. California 209, 213, 650 | grep [[:digit:]]

# CHALLENGE 3

# echo The ghost that says boo haunts the loo | grep .oo

oo_matches = re.findall(".oo", "The ghost that says boo haunts the loo")

print(oo_matches)

# Character classes in grep may be different
# https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_03.html








