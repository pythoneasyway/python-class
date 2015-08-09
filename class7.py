#!/usr/bin/python
# pythoneasyway@gmail.com
# exercises with loops while and for

# choose a number lower than 12345678
while True:
    number = raw_input("enter a number: ")
    number = int(number)
    if number > 12345678:
        print "Number is too big"
    else:
        break

total = 0

# using for to print out 
# each number until reaches the limit
for i in range(1,number):
    print i

variable = 1
number = 1000

# using while loop to calculate 
# how much is the sum of all numbers between 1 and 1000
while variable < number:
    print variable
    variable = variable + 1
    total = total + variable

print "the total is ", total 


attempts_failed = 0

# using while to loop indefinitely until 
# the password is right
while True:
    password = raw_input("enter a password ==> ") 
    if password == "qwertzuiopasdfghjklyxcvbnm":
        print "password is correct"
        break
    else:
        print "Go to jail, the authorities have caught you"
	# we keep the failed attemts
	# if is bigger than 3 then you probably don't know the password :)
        attempts_failed =  attempts_failed + 1
        if attempts_failed > 3:
            print "you are arrested"
            break

while True:
    name = raw_input("enter a name ==>  ")
    print "the number of letters  in your name is ", len(name)
    # find() search for the given substring inside the main string
    # the funcion returns the position where was found, 
    # if is not found then return -1
    # in this case, it search for "z" inside the name
    if name.find("z") != -1:
        break
        
import turtle as t  
t.showturtle()     

# drawing with multiple turtles :)
t1 = t.Pen()
t2 = t.Pen()
t3 = t.Pen()
t4 = t.Pen()

# max speed for all turtles
t.speed(0)
t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)

t4.circle(200)
t2.right(90)
t2.circle(200)
t3.backward(100)
t4.forward(200)
t1.left(90)
t1.forward(200)
t3.color("red")
t2.color("blue")
t1.color("green")
t.color("yellow")
t2.circle(200)
t1.circle(200)
t3.right(90)
t3.circle(200)
t2.forward(200)
t.circle(100)
t2.circle(100)

import random as r
# create a list with colors
colors = ['red','blue','yellow','green','purple','black', "brown", "pink", "light blue", "tan"]
# drawing inside a loop
for i in range(1,20):
    # pensize() change the size of the pen 
    # in this case it will be a random number between 1 and 10
    t3.pensize(r.randint(1,10))
    # generates a random number between 100 and 400
    size = r.randint(100,400)
    # title of the window will be the size concatenated with the times of execution 
    t.title("Size:"+str(size)+" Times "+str(i))
    # creates a circle with so many steps as the current 'i' index 
    t3.circle(size, steps = i)
    # choice(), Return a random element from the non-empty sequence
    # in this case choose a color from the list colors randomly
    t3.color(r.choice(colors))
t.done()
