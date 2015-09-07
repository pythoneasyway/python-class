#!/usr/bin/python
#: Title        : class1.py
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Class number 1 
#: 		  - defining variables
#:		  - functions: upper(), lower(), str()
#: Options      : none
#: Version      : 1.0

# 1. The first line of this code indicates what interpreter will be used, follow by a description header
# 2. All lines which are comments starts with a '#'
# 3. Comments are ommited during execution

# DEFINE VARIABLES
name = "john"
age = 9
grade = 3

# upper function, change a string into upercase
city = "New York City".upper()
country = "USA"
population = 300000000

# print out the variables
# str() transform a integer into a string
# '+' operator concatenates strings
print name + " is age "+ str(age) + " and is from", city 

# add 5 to age
# this could also be written like:
# age += 5
age = age + 5

print "In five years " + name.upper() + " is going to be " + str(age) + " and the grade will be ", str(grade + 5)

# lower(), changes a string into lowercase
print city + " is part of the " + country.lower() 
print "Where live "+ str(population) + " people"


