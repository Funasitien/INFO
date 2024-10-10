# Import turtule object, functions and the random package.
import turtle
from turtle import *
import random

# Hide the turtle for a *fancy* design and make it faster beacause we can
hideturtle()
turtle.speed(0)

# Print a square, the base of the dice.
def square(x, y, length):

    # Go to the center of the screen
    turtle.up()
    turtle.goto(x, y)

    turtle.down()

    # Draw the square
    for i in range(4):
        forward(length)
        left(90)

# The function to draw the circles (the dots of the dice)
def cercle(x, y, r):
    turtle.up()
    turtle.goto((x, y))
    turtle.down()
    turtle.begin_fill()
    # The dot function allow us to make a cicrle at the center of te screen
    # Thing which is not possible with the circle() function
    turtle.dot(r*2, 'black')
    turtle.end_fill()


# The function to draw the dice
def dice(length, dots=1, nbs=1):
    
    # Set the dot's size value to an automatic one (if it was not set)
    # We cant do this in the function as it use a variable
    if dots == 1:
        dots = length/8

    # Then we generate the value of the global x ...
    gx = (nbs*length)/2
    y = -length/2

    for i in range(nbs):
        # ... to use it to know the X position of the dice
        x = -gx + (length * i)
        
        # Then we draw the square
        square(x, y, length)
    
        # We generate the value of the dice
        num = random.randint(1, 6)
        
        """
        #To debug, you can then change the value of num
        num = 6
        """
        
        # Instead of using if num = 1; if num = 2;..
        # I use some math expressions to create dots which are in common for severals dice faces
    
        # Create the center dot if the random num is odd
        if (num % 2) == 0:
            pass
        else:
            # Reminder : the cercle function use 3 arguments : x, y and size (or r)
            cercle(x+(length/2), 0, dots)
    
        # Create the first two dots at two opposite corners if the nuber is not one (so the dots for 2, 3, 4, 5 and 6)
        if num != 1:
        
            # All of these caculs are used to let the user customize the size of the square and of the dotes of the dice, while keeping a margin between the dots and the square.
            # These caculs are not this interesting, it's most a lot of debuging and just work with the square function above.
            cercle(x+length-dots*1.5, (length/2) -(dots*1.5) , dots)
            cercle(x+dots*1.5, -(length/2) +(dots*1.5) , dots)
    
        # If it's bigger that 3, we create the two mising dots at the two missing corners (for 4, 5 and 6)
        if num > 3:
        
            # Here it's the sames caculs than before but reverted and with somes tweaks
            cercle(x+length-dots*1.5, -(length/2) +(dots*1.5), dots)
            cercle(x+dots*1.5, (length/2) -(dots*1.5), dots)
    
        # As siw have two middle dots which are only use for this face, we create them separetly
        if num == 6:
            cercle(x+length-dots*1.5, 0, dots)
            cercle(x+dots*1.5, 0, dots)
    
    # And then it repeat to create the number of dice specified in the config
    # ...

# Then Finnaly we call the main function to generate the dice
# Create 20 dice with a square of 100px length and with dots with a size of 13
dice(200, 1, 16)
turtle.done()
# 100 Lines