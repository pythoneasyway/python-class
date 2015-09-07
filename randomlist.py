#!/usr/bin/python
#: Title        : 
#: Date         : 
#: Author       : pythoneasyway@gmail.com
#: Description  : Random shapes
#: Options      : none
#: Version      : 1.0
import random as r
values = list()
sum = 0
for i in range(500):
	x = r.randint(-350,350)
	y = r.randint(-350,350)
	values.append([x,y])

# removing values
for i in range(0,250):
	values.remove(values[i])

from colors_lib import *

choices = [3,4,5,6,7,8,9,10]
import turtle as t
t.showturtle()
t.speed(0)
index = 0

for x, y in values:
	t.up()
	t.goto(x, y)
	t.down()
	t.write(index)
	t.color(color_list[index])
	t.circle(15, steps = r.choice(choices))
	t.title(i)
	index = index + 1
t.done()
