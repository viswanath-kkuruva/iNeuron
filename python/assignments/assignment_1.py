#!/usr/bin/env python
# coding: utf-8

"""
Task 1.1 : Install Jupyter notebook and run the first program and share the screenshot of the output.
"""
link = "https://github.com/viswanath-kkuruva/iNeuron/blob/master/python/assignments/Task_1.1_jupyter_notebook_execution_screenshot.png"

"""
Task 1.2 : Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.
"""
output = []
start = 2000
end = 3200
for num in range(start, end+1):
    if num % 7 == 0 and num % 5 != 0:
        output.append(str(num))
result = ','.join(output)
print(result)

"""
Task 1.3 : Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.
"""
first_name = input('Please input your first name : ')
last_name = input('Please input your last name : ')
result = '{} {}'.format(first_name[::-1], last_name[::-1])
print(result)

"""
Task 1.4 : Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
"""
import math

diameter = 12
radius = diameter / 2

volume = (4/3) * math.pi * (radius ** 3)
print(volume)

"""
Task 2.1 : Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
"""
sequence = input('Please input numbers sequence seperated by comma : ')
lst = sequence.split(',')
print(lst)

"""
Task 2.2 : Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
max_stars = 5
for i in range(max_stars*2):
    output = ''
    stars = i
    if i > max_stars:
        stars = max_stars - (i -max_stars)
    for j in range(stars):
        output += '* '
    print(output)

"""
Task 2.3 : Write a Python program to reverse a word after accepting the input from the user.
Input word: AcadGild
Output: dilGdacA
"""
word = input('Please input word to be reversed : ')
print(word[::-1])

"""
Task 2.4 : 
Write a Python Program to print the given string in the format specified in the sample output.

WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens

Sample Output:
WE, THE PEOPLE OF INDIA,
      having solemnly resolved to constitute India into a SOVEREIGN, !
             SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
             and to secure to all its citizens
"""

output = """WE, THE PEOPLE OF INDIA,
      having solemnly resolved to constitute India into a SOVEREIGN, !
             SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
              and to secure to all its citizens
"""
print(output)

output = """WE, THE PEOPLE OF INDIA,
      having solemnly resolved to constitute India into a SOVEREIGN, """ + "!" + """
             SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
              and to secure to all its citizens
"""
print(output)

output = """WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, !\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t and to secure to all its citizens
"""
print(output)