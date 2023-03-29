import turtle   #Outside_In
import turtle
import time
import random
 
print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    a = int(num_str)
 
angle = 180 - 180*(a-2)/a
 
turtle.up
 
x = 0
y = 0
turtle.setpos(x, y)
 
 
numshapes = 8
for x in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(a):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        print (turtle.pos())
        turtle.up()
        turtle.end_fill()
 
time.sleep(11)
turtle.bye()


