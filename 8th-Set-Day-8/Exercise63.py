#Draw three squares in a row with a gap between each. Fill them using three different colours.  

import turtle

turtle.shape("turtle")

turtle.speed(1)
turtle.penup()
turtle.backward(200)
turtle.pendown()

for i in range(0,3): 
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
        
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()

turtle.exitonclick()

'''import turtle

turtle.shape("turtle")

for i in range(0,3): 
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
        
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()

turtle.exitonclick()'''