## Defining a ftn without parameter

# def square():
#     x=4*2
#     print(x)

# square()

## Defining a ftn with parameter

# def square(x):
#     x_square=x**2
#     print(x_square)

# square(4)
# square(5)


## if you dnt wnat to print that value directly, instead return the sqaure value and assign it to a variable


# def square(x):
#     x_square=x**2
#     return x_square
# num = square(5)
# print(num)


## DocStrings
    # it decribes what your ftn does, serve as documentation
    # placed in the imediate line after the ftn header
    # in b/w triple double quotes """..... """


## MULTIPLE parameter and return values

from ast import arg
import re
from unittest import result


def raise_to_power(value_1,value_2):
    """raise value1 to the power of value2"""
    new_value= value_1**value_2
    return new_value

z= raise_to_power(4,3)
print(z)
raise_to_power(5,6)


## MULTIPLE return Values
    # for this we use TUPLE

def raise_to_both(value_1,value_2):
    """raise value1 to the power of value2 and viceversa"""
    new_value1= value_1**value_2
    new_value2= value_2**value_1
    new_tuple =(new_value1,new_value2)
    return new_tuple

print(raise_to_both(2,3))
# or
result =raise_to_both(2,3)
print(result)


## DEFAULT argument
    # lets say that you are writing a ftn that takes multiple parameters, and that there is often a common value for some of these paramters

def power(number,pow=1):
    new__value= number**pow
    return new__value

v=power(9)
c=power(9,2)
print(v)
print(c)


## FLEXIBLE arguments
    # if you aren't sure how many arguments a user will want to pass it
    # we use *args

def add_all(*args):
    sum_all=0
    for num in args:
        sum_all +=num
    return sum_all

print(add_all(2,3))

def mult_all(*args):
    mult_all=1
    for num in args:
        mult_all*=num
    return mult_all

print(mult_all(2,3,6))


## LAMBDA ftn
    # Its a quicker way to write ftns
    # after keyword lambda, we specify the names of arguments, then use colon: followed by the expression that specifies what we wish the ftn to return

#example
lambda x,y: x**y
raise_topow =lambda x,y: x**y

print(raise_topow(2,3))


## MAP
    # map takes two arguments(ftsn, seq)
    # map() applies theftn to all elements in the sequence

#example
nums= [4,5,6,7,8]
square_all=map(lambda num:num**2,nums)
print(list(square_all))
    #using list for readibility
#example
def myfunc(n):
  return len(n)

xx = map(myfunc, ('apple', 'banana', 'cherry'))

print(list(xx))




        