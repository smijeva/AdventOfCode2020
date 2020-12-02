"""
The day 2 task is to verify whether password matches given constraints.
I used this task to practice regular expressions for a bit (with named groups) and some list comprehension again.
"""

import re


def part1():
    file = open('input2.txt')
    passwords = [re.search('^(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>.): (?P<pass>.+)$', line)
                 for line in file]
    passwords_validity = [int(p['min'])
                          <= sum([c == p['char'] for c in p['pass']])
                          <= int(p['max'])
                          for p in passwords]
    print(sum(passwords_validity))


def part2():
    file = open('input2.txt')
    passwords = [re.search('^(?P<first>[0-9]+)-(?P<second>[0-9]+) (?P<char>.): (?P<pass>.+)$', line)
                 for line in file]
    passwords_validity = [(p['pass'][int(p['first'])-1] == p['char'])
                          ^ (p['pass'][int(p['second'])-1] == p['char'])
                          for p in passwords]
    print(sum(passwords_validity))


part1()
