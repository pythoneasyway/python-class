#!/usr/bin/python
#: Title        : 
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Lotto game
#: Options      : none
#: Version      : 1.0
import random as r
all_numbers = range(1,47)
my_numbers = list()
your_numbers = list()
total = 0
print "Let's play lotto!!"
print "Enter 6 numbers between 1 and 46, separates by comma"
your_numbers = raw_input("Number ").split(",")
print "Your numbers are: ", your_numbers
for i in range(1,7):
	number = r.choice(all_numbers)
	my_numbers.append(number)
	all_numbers.remove(number)
print "My Numbers are  : ", my_numbers
for i in your_numbers:
	total = total + my_numbers.count(i)
print "You got ", total, "Numbers!!!"
