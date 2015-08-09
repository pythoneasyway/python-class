#!/usr/bin/python
# pythoneasyway@gmail.com
# the olympic symbol

import turtle as t
t.showturtle()
t.speed(0)
t.circle(100)
# Pull the pen up – no drawing when moving.
t.up()
# go to the x, y position
t.goto(-150,0)
t.color("blue")
# Pull the pen down – drawing when moving.
t.down()
t.circle(100)
t.up()
t.goto(150, 0)
t.color("red")
t.circle(100)
t.down()
t.circle(100)
t.up()
t.goto(70,-80)
t.color("green")
t.down()
t.circle(100)
t.up()
t.goto(-70,-80)
t.color("yellow")
t.circle(100)
t.down()
t.circle(100)
t.title("Olympic symbol")
t.color("black")
t.up()
t.goto(0,-150)
# write() writes text with the font provide
# font=arian, size=30, style=normal
t.write("Olympics", font = ("arial", 30, "normal"))
t.done()
