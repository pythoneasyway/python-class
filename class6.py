#!/usr/bin/python
#: Title        : class6.py
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Class number 6
#:                - loops: for and while
#:		  - breaking loops: brake
#:                - lists functions: append(), remove(), sort()
#: Version      : 1.0

for i in range(1,10):
    print "John ", i

# my current weight and height
my_weight = 53
my_height = 127

# using for to calculate "possible" weight :)
for i in range(9,35):
     my_weight = my_weight + 2.5
     print "my weight when i am ", i, " is going to be", my_weight, "pounds"

# using for to calculate "possible" height :)
for i in range(9,21):
    my_height = my_height + 5
    print "my height when i am ", i, " i am going to be", my_height/30.48, " feet tall"
   
# create a list called ingredients, which contains the items needed for a party
ingredients = ["pizza", "balloons", "cake", "people", "electronics", "chips", "goodie bags"]

# printing the items
for f in ingredients:
    print "for my party I need",f
    
# append() add items to a list
ingredients.append("confetti")
ingredients.append("food")
ingredients.append("books")

# prints an empty line
print 
for i in ingredients:
	print "my updated ingredients for the party are", i

# remove() deletes the given item from the list
ingredients.remove("books")

print 
for i in ingredients:
	print "my last ingredients for the party are", i

# sort() sort the list, in this case alphabetically
ingredients.sort()

print 
for i in ingredients:
	print "my sorted ingredients for the party are", i


# create a list contries
countries = ["USA","India" ,"Turkey", "Canada", "Belgium", "Costa Rica", "England", "Austria", "Czech Republic"]

# sort the countries
countries.sort()
print 
for i in countries:
	print "I have been in these countries", i

# adding a new country 
countries.append("Switzerland")

# reverse () reverse the order of the items :)
countries.reverse()
print "My reverse list is "
for i in countries:
	print "I have been in these countries", i

#########################
# MY FIRST GUESSING GAME
#########################
print
print "MY FIRST GUESSING GAME"
import random as r
# generates a random number between 1 and 999
number = r.randint(1,1000)

# generates a random number between 1 and 10
ticket = r.randint(1,11)
n = 0

# A while loop statement in Python programming language repeatedly 
# executes a statement as long as a given condition is true.
while True:
	# the string is transformed into integer right after is entered
	value = int(raw_input("enter a number between 1 and 1000=> "))
	if value > number:
		print "number too big"
	elif value < number:
		print "number too small"
	else:
		print "number found, it was =>", number 
		# when the number is found, we must 
		# break the cycle in order to get out the loop!!
		break
	print "try number", n, "try again!"
	n = n + 1  

if n < 6:
	print "YOU WIN A TICKET TO", countries[ticket]
else:
	print "TO MANY TRIES, NO TICKET THIS TIME, YOU LOSEEEEE!!"
