#program using map() function
import math
def fun(n) :
    return n * n
lst = [5, 10, 15, 20, 25]
m1 = map(math.radians, lst)
m2 = map(math.factorial, lst)
m3 = map(fun, lst)
print(list(m1)) # prints list of radians of all values in lst
print(list(m2)) # prints list of factorial of all values in lst
print(list(m3)) # prints list of squares of all values in lst

#program using filter() function
def fun(n) :
    if n % 5 == 0 :
        return True
    else :
        return False
lst1 = ['A', 'X', 'Y', '3', 'M', '4', 'D']
f1 = filter(str.isalpha, lst1)
print(list(f1)) # prints ['A', 'X', 'Y', 'M', 'D']

lst2 = [5, 10, 18, 27, 25]
f2 = filter(fun, lst2)
print(list(f2)) # prints [5, 10, 25]

#program using reduce() function
from functools import reduce
def getsum(x, y) :
    return x + y
def getprod(x, y) :
    return x * y
lst = [1, 2, 3, 4, 5]
s = reduce(getsum, lst)
p = reduce(getprod, lst)
print(s) # prints 15
print(p) # prints 120