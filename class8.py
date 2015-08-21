#!/usr/bin/python
# define 2 lists to work with
even_list = list()
odd_list = list()

# we'll use the numbers from 1 to 1000 
for i in range(1,1001):
    # % is modulo, which is here the remainder of the division of number by 2
    if i % 2 == 0:
        # add the even number to the list
        even_list.append(i)
    else:
        # add the odd number to the list
        odd_list.append(i)
print "the odd numbers are ", odd_list
print "the even numbers are ", even_list

# import everything from the file colors_lib
from colors_lib import *
# print out the color_list defined in the previous imported module
print color_list
# total of colors
print "the total of colors is", len(color_list)

import turtle as t
t.showturtle()
total = len(color_list)
index = 1
t.up()
t.goto(0,-350)
t.down()
for i in color_list:
    t.color(i)
    if index <100:
	# create first triangle
        t.circle(index, steps = 3)
    elif index<200:
	# create the square
        t.circle(index, steps = 4)
    elif index<250:
	# creae the pentagon
        t.circle(index, steps = 5)
    elif index<300:
	# create the hexagon
        t.circle(index, steps = 6)
    elif index<350:
	# last circle
        t.circle(index)
    else:
	# change the background
        t.bgcolor(i)
    # print in the title the color's name and the number of the color.
    t.title(i+" "+str(index))
    t.speed(0)
    index = index +1 
# finish
t.done()
