Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #OPERATORS
>>> #OPERATORS: Arithmetic, Assignment, Relational, Logical, Unary Operator
>>> 
>>> # Arithmetic Operators are:
>>> 
>>> x = 2
>>> y = 3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x/y
0.6666666666666666
>>> 
>>> # Assignment Operators are:
>>> 
>>> x = 2
>>> 
>>> x = x+2
>>> x
4
>>> x+=2
>>> x
6
>>> # x = x+2 is the same to x+=2
>>> 
>>> x*=3
>>> x
18
>>> 
>>> a,b = 5,6
>>> a
5
>>> b
6
# I can assign two variables in one line

# UNARY Operators are:

# Binary = 2, Unary = 1

n = 7
n
7
-n
-7
n
7
n = -n
n
-7

#Relational Operators are:

a < b
True
a > b
False

a==b
False

#Single = means assogning, double == means compering
# a is 5 and b is 6 so a==b a isn't the same to b that's why False

a = 6
a==b
True

a <= b
True
a >= b
True
a != b
False
# != means not equal
# it's False because a is equal to b, both are 6

b = 7
a != b
True

#Logical Operators are:

a = 5
b = 4

a < 8 and b < 5
True

a < 8 and b < 2
False

# TRUTH TABLE : True will be only when both are True
# in AND  both must to be True to get True
# in OR   if one conditional is true the outcome will be True

a < 8 or b < 2
True

# Not

x = True
x
True
not x
False

# By using not, I can reverse the operation

x
True
x = not x
x
False
