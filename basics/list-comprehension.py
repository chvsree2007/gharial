#!/bin/python3
def add(a,b,c):
    return(a+b+c)
x,y,z = [int(a) for a in input('enter three values ').split()]
print('Entered values ',x,y,z)
out = add(x,y,z)
print('Sum is ',out)
