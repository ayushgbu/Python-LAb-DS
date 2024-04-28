#built-in math functions
print (abs(-40))
print (pow(3,5))
print (min(10,20,5))
print (max(10,20,30,60.7,90))
print (divmod(17,4))
print (bin(5), hex(90), oct(44))
print (round(2.5445), round(2.5445,2))

#mathematical functions from math module
import math as m
x=1.5357
print (m.pi, m.e)
print (m.sqrt(x))
print (m.factorial(6))
print (m.fabs(x))
print (m.log10(x))
print (m.exp(x))
print (m.trunc(x))
print (m.floor(x))
print (m.ceil(x))
print (m.modf(x))