#!/bin/python3
import re
string = input('Enter a string ')
c = input('Enter a char to count ')
out = re.findall(c,string)
print('Total number of chars ',len(out))
print('Total number of chars ',string.count(c))

