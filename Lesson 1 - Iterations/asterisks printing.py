'''
CopyRight 2022
@author Yuyang Chen
All rights reserved. 
'''

'''
Question 1 (For loop):
Print a striangle made of asterisks('*') separated by spaces. The triangle shouuld consist of n rows, where n is a given positive integer, 
and consecutive rows should contain 1,2,...,n asterisks. For example, for n=4 the triangle should appear as follows:

*
* *
* * *
* * * *
'''

n = 4
for i in range(1, n+1):
    a = '*'
    b = '*' + ' '
    print(b*(i-1) + a)


'''
Question 2 (For loop):
Print a triangle made of asterisks (‘*’) separated by spaces and consisting of n rows again, but this time upside down, and make it symmetrical. 
Consecutive rows should contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1) spaces. 
For example, for n = 4 the triangle should appear as follows:

* * * * * * *
  * * * * *
    * * *
      *
'''


n = 20
for i in range(n,0,-1):
    a = (n-i)*' '
    b = i*('*'+' ')
    print(a+b)
