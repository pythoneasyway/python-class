#!/usr/bin/python
#: Title        : class9.py
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Class number 9
#:                - creating our own functions with def
#:                - using try and except to "catch" possible errors
#: Version      : 1.0

# Defining our first function
# It calculates the sum of two numbers and returns the result
def addition(a, b):
    c = a + b
    return c

# A function can also directly return the result
def addition2(a, b):
    return a + b

#print addition(10,20)
#print addition2(100,123456)

def subtraction(a, b):
    return a - b

#print subtraction(23, 17)

def multiplication(a, b):
    return a * b
#print multiplication(2, 74)

def division(a, b):
    return a / b
#print division(22,2)

# this code can be improved!! ;-)
while True:
    a = raw_input("please enter 1st number: ")
    b = raw_input("please enter 2nd number: ")
    try:
         a = int(a)
         b = int(b)        
    except:
         print "Only numbers are valid, please try again!!"
         exit()            

    if b == 0:
     print "Division: division by zero is not possible"
     print "multiplication: ", multiplication(a, b)
     print "subtraction: ", subtraction(a, b)
     print "addition: ", addition(a, b)
    else: 
     print "Division: ", division(a, b) 
     print "multiplication: ", multiplication(a, b)
     print "subtraction: ", subtraction(a, b)
     print "addition: ", addition(a, b)
     break
        

import turtle as t
t.showturtle()

# importing our own library color
from colors_lib import *

import random as r

x = list()
y = list()

# creating random coordinates (x,y) and adding them to the lists
for i in range(0, len(color_list)):
    x.append(r.randint(-650,650))
    y.append(r.randint(-350,350))

# defining a count for the loop
a = 0

# shapes
# 3 = triangle
# 4 = square
# 5 = pentagon
# 6 = hexagon

shape = [3, 4, 5, 6]

# we can use it to setrandom speeds!
speed = [0,1,2,3,4,5,6,7,8,9]

# black for the background
t.bgcolor("black")

# browsing the list, color by color
for i in color_list:
    # choosing a random speed 
    speedy = r.choice(speed) 
    
    # setting the previously choosed speed
    t.speed(speedy)

    # going to random (x, y) !!
    t.penup()
    t.goto(x[a],y[a])
    t.pendown()
    
    # increasing the counter
    a = a + 1
    
    # setting the color according to the index
    t.color(i)
    
    # drawing with circle, random size between 10-20
    # shape will be random too!! 
    t.circle(r.randint(10,20), steps = r.choice(shape))
    
    # title will contain color, current number inside loop and the speed
    t.title("Color:" +i+" "+ "Cycle Number: "+ str(a)+ " Speed: "+ str(speedy))
    
    # write the current index
    t.write(str(a))
    
t.done()
