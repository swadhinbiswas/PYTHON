import turtle
my=turtle.Turtle()
my.speed(0)

def square(length,angle):
    for i in range(4):
        my.forward(length)
        my.right(angle)
        
    
for i in range(100):
    square(200,90)
    my.right(11)
        
    















