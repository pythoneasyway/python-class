#!/usr/bin/python
#: Title        : class5.py
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Class number 5 
#:                - using strings, string slicing, string comparision
#:                - functions: randint(). turtle functions: title()
#:		  - random numbers
#: Version      : 1.0

b = "buy me a big screen TV"
p = "You are poor. Get a better job."

salary = raw_input("enter your salary ")
if int(salary) > 100000:
    # [] access the respective the content of the given position
    # b[0]='b'
    # b[1]='u'
    # b[2]='y'
    print b[0],b[1],b[2]
    # b[0:4]="buy"
    print b[0:4]
else:
    # p[8:12]="poor"
    print p[8:12]

name = raw_input("please enter your name: ")
if name == "john":
    print "you are fron new york"
elif name == "mike":
    print "You are from toronto"
else:
	print "you come from qwertzuiop :-)"

# importing random, in order to use some random numbers
import random as r

nums = raw_input("enter a range of numbers between 1 and your range: ")

# For loops are traditionally used when you have a piece of code which you want to repeat n number of times
# print 10 random numbers with their index
for i in range(1,11):
    #randint() returns a random number between the given range
    print "Number", i, r.randint(1,int(nums))

# using turtle to print some circles with loop
# and drawing text in the x,y axis
import turtle as t
t.showturtle()
t.speed(0)
for i in range(1,10):
    t.circle(i)
    # title() changes the title for the window
    t.title(i)

t.up()
t.goto(-100,0)
t.color("blue")
t.down()
for i in range(1,10):
    t.circle(i)
    t.title(i)
for i in range(1,400,10):
    t.goto(0,i)
    t.write("mike")
for i in range(1,400,30):
    t.goto(i,0)
    t.color("green")
    t.write("john")
for i in range(1,-400,-20):
    t.goto(i,0)
    t.color("red")
    t.write("NYC")
for i in range(1,-400,-10):
    t.color("yellow")
    t.goto(0,i)
    t.write("USA")
t.done()
