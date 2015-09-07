#!/usr/bin/python
#: Title        : class9.py
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Class number 10
#:                - creating our first dictionary (phone guide)
#:                - using a dictionary to keep random values 
#: Version      : 1.0

# defining a new dictionary 
phone_guide = dict()
phone_guide = {'john':706123456, 'peter':704123321, 'random_fellow':123456789}

# functions
def showdictionary(dictionary):
    for key, value in dictionary.items():
        print key, value


# phone guide
while True:
    print "\nEnter what do you want to do"
    option = raw_input("(e) exits, (a) adds a number, (s) shows the guide, (d) is to delete a number: ")
    if option == 'e':
        print "exititing the program, thank you for running it"
        break
    elif option == "a":
        name = raw_input("enter the name: ")
        number = raw_input("enter the phone number: ")
        
        # adding a new item to the dictionary
        phone_guide[name] = number
        
    elif option == "s":
        showdictionary(phone_guide)
    elif option == "d":
        delete = raw_input("enter which name you want to delete: ")
        
        # catch the error in case the item does not exists
        try:
            # deleting a specific item from the dictionary
            del phone_guide[delete]
            
        except:
            print "Name does not exist"
    else:
        print "error, please try again!!"


# functions
def star():
    for i in range(5):
        t.forward(50)
        t.right(144)  
        
def pattern():
    for i in range(50):
        t.forward(100)
        t.left(123)

# importing color_lib
from colors_lib import *

# new dictionary
positions = dict()

import random as r

# dictionary will contain color as key and a random "y position" as a value 
for i in color_list:
    x = i
    y = r.randint(-500,500)
    positions[x] = y

# print out the dictionary
showdictionary(positions)

# turtle
import turtle as t

# tracer function turns turtle animation on/off and set delay for update drawings
t.tracer(4, 10)

t.showturtle()
t.bgcolor("black")
count = 0

# looping through the dictionary
for key, value in positions.items():
    t.up()
    # x will be random
    x = r.randint(-650,650) 
    
    # go to a random x, y position
    t.goto(x, value)
    
    # color is the key of the dictionary
    t.color(key)
    
    # counting times to add into title
    count = count + 1
    
    t.down()
    
    t.title("x="+str(x)+" y="+str(value)+ " total=" +str(count))
    
    # filling with color
    t.begin_fill()
    
    star()

    # ending filling
    t.end_fill()
    #pattern()
    
t.done()
