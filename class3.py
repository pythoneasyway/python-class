#!/usr/bin/python
#: Title        : class3.py
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Class number 3
#:                - conditionals: if; elif; else
#:                - functions: replace(), range()
#: Version      : 1.0

text = raw_input("enter some text: ")
print text

# replace() a string with a new string
print text.replace("john", "rambo")

# a	 4
# e	 3
# i	 1
# o	 0
# u	 2
password = raw_input("enter a phrase for your password: ")
pass1 = password.replace("a", "4")
pass2 = pass1.replace("e", "3")
pass3 = pass2.replace("i", "1")
pass4 = pass3.replace("o", "0")

# replace space for nonspace
pass5 = pass4.replace(" ", "") 
final_pass = pass5.replace("u", "2")
print "Your secure password is: ", final_pass

money = raw_input("how much money do you have? ")

# int() return an integer object constructed from a number or string
# "if" is used for decision making
# If the condition is true, then do the indented statements. 
# If the condition is not true, then skip the indented statements.
if int(money) > 1000000:
    print "You are rich. Buy me a big screen TV"
    guest = raw_input("enter the number of guests you will put in a party: ")
    if int(guest)>100:
        print "you have a big party"
# "elif" if used for decision making
# If condition was not true in the if above, then compares again
    elif int(guest) > 30:
        print "you have a medium party"
# "else" if used for decision making, it is the last step to be compared
# If the condition in the elif was not true, then do the idented statments
    else:
        print "Invite more guests, the party is boring"
	# the following list represent the number of guests
	print range(0,int(guest))
else: 
    print "you are poor. I will give you 100 dollars"
