#!/usr/bin/python
# pythoneasyway@gmail.com

# raw_input() read imput from the console and store it in the variable
dollars_per_day = raw_input("enter the dollars per day: ")
days = raw_input("enter the days per month: ")
months = raw_input("enter the number of months: ")

# calculating the total dolars per mont 
total = int(dollars_per_day) * int(days) * int(months) 
print "the total is", total

# the '*' character multiples strings
asterixes = '*'
print "Each * represents a dollar =>", asterixes * total

# range() creates a list with the respective range
print range(1, total + 1)

text = raw_input("please enter how fat you are: ")
print "you are ", text
text2 = raw_input("please enter a short history: ")
# len() count the number of characters in a string
print "your history has: ", len(text2), "letters"

# using python turtle graph
# we need to import the turtle first, any name could be given after after "as"
# using t for simplicity
import turtle as t

# speed 0 or over 10 is the fastest
t.speed(0)
# showing the turtle
t.showturtle()
# moving forward 200 pixels
t.forward(200)
# turning right 90 degrees
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
# setting color to blue
t.color("blue")
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.forward(200)
# moving backward 200 pixels
t.backward(200)
t.color("red")
t.forward(200)
t.right(90)
# turning left 180 degrees
t.left(180)
t.forward(200)
t.left(180)
t.right(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.right(90)
t.color("green")
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
# drawing a circle with radius 300 and so on
t.circle(300)
t.circle(100)
t.circle(200)
t.circle(50)
t.circle(25)
t.circle(6)
t.circle(3)
t.circle(1)
# turtle stops with done 
t.done()
