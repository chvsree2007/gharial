#!/bin/python3
def add(a,b):
    return(a+b)

a,b = input('Enter two numbers to ADD:').split(',')
out = add(int(a),int(b))
print('Sum of {} and {} is:'.format(a,b),out)

