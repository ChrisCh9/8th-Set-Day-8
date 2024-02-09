#Draw three squares in a row with a gap between each. Fill them using three different colours.  

import turtle

turtle.shape("turtle")

for i in range(0,3): 
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)

turtle.exitonclick()