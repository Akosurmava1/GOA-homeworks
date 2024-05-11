from turtle import *


#we want to paint to house

# step 1: draw a square
width(6)
speed(10)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a square

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170, 170)
pendown()

color("brown")
begin_fill()
penup()
goto(30,140)
pendown()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
penup()
begin_fill()
goto(120,180)
pendown()
right(270)
forward(40)
right(270)
forward(40)
right(270)
forward(40)
right(270)
forward(40)
end_fill()
exitonclick()





