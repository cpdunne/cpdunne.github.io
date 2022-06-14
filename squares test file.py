import turtle               # import the turtle module 
import math                 # import the math module

numsquares = int(input("Number of squares to draw: "))
numsquares -= 1

screen = turtle.Screen()    # open a turtle screen 
screen.bgcolor("yellow")    # set screen's background color

ted = turtle.Turtle()       # create a turtle; call it ted

sideLength = 300            #set length of first square's side to 300

for i in range(4):              # draw a square: do the following 4 times
     ted.forward(sideLength)    # draw a line 150 pixels long
     ted.left(90)               # turn left to be ready for next line

if numsquares > 0:
     ted.goto(sideLength / 2, 0)
     ted.left(45)
     sideLength = sideLength/ math.sqrt(2)
     ted.forward(sideLength)
     for i in range(3):              # draw a square: do the following 4 times
          ted.left(90)
          ted.forward(sideLength)    # draw a line 150 pixels long
     numsquares -= 1

while numsquares > 0:
          ted.penup()
          sideLength = sideLength/ math.sqrt(2)
          ted.goto(sideLength / 2, sideLength / 2)
          ted.pendown()
          ted.left(45)
          ted.forward(sideLength)
          for i in range(3):              # draw a square: do the following 4 times
               ted.left(90)
               ted.forward(sideLength)
          numsquares -= 1

     

screen.exitonclick()        # close screen when user clicks on it