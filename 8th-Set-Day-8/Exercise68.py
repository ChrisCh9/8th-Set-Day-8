#Draw a pattern that will change each time the program is run. Use the random function to pick the number of lines, the length of each line and the angle of each turn.

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