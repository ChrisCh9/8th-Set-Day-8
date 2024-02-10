#Write the numbers as shown below (1 2 3),starting at the bottom of the number one. 

import turtle

turtle.shape("turtle")

for i in range(0,3): 
    #for i in range(0,3):
        turtle.left(60)
        turtle.forward(50)
        turtle.right(150)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)

        #turtle.right(60)
        #turtle.forward(100)


turtle.exitonclick()