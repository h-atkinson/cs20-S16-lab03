#lab03.py for Hannah Atkinson and Brittany Wilson
#CS20, Spring 2016, Instructor: Phil Conrad
#Draw some initials using turtle graphics

import turtle
import math
import random

friend = turtle.Turtle()
friend.up()
friend.color("blue")

red = turtle.Turtle()
red.up()
red.color("red")

def drawH(Turtlefriend, width, height):
    """
    draw H with Turtlefriend, with a width and height
    """
    friend.down()
    friend.left(90)
    friend.forward(height)
    friend.backward(height / 2)
    friend.right(90)
    friend.forward(width)
    friend.left(90)
    friend.forward(height / 2)
    friend.backward(height)
    friend.up()
    
def drawA(Turtlefriend, height):
    """
    draw A with turtles, of height
    """
    width = ((height) * math.tan(.349))
    friend.down()
    friend.right(20)
    friend.forward(height)
    friend.right(140)
    friend.forward(height)
    friend.backward(height / 2)
    friend.right(110)
    friend.forward(width)
    friend.up()
    friend.setheading(0)

def drawB(Turtlered, width, height):
    """
    draw B with turtles, of width nd height
    """
    red.down()
    red.forward(width)
    red.circle((height / 4),180, 20)
    red.forward(width)
    red.backward(width)
    red.left(180)
    red.circle((height / 4),180, 20)
    red.forward(width)
    red.left(90)
    red.forward(height)
    red.up()

def drawW(Turtlered, width, height):
    """
    draw W with turtles of width and height
    """
    red.backward(height)
    red.left(30)
    red.down()
    red.forward(height)
    red.left(130)
    red.forward(height * .67)
    red.right(140)
    red.forward(height * .67)
    red.left(130)
    red.forward(height)
    red.up()
    red.setheading(0)
    
def go():
    """
    draws three sets of initials of randomly-generated heights and widths with turtles Friend and Red
    """
    startX = random.randint(-200, -100)
    startY = random.randint(100, 150)
    widtha = random.randint(30, 70)
    heighta = random.randint(40,90)
    friend.goto(startX, startY)
    drawH(friend, widtha, heighta)
    friend.goto((startX + widtha + 30), startY)
    drawA(friend, heighta)
    red.goto((startX + 60 + (2 * widtha)), startY)
    drawB(red, widtha, heighta)
    red.goto((startX + 90 + (3*widtha)), startY)
    drawW(red, widtha, heighta)
    startXb = random.randint(-200, -100)
    startYb = random.randint(-50, 00)
    widthb = random.randint(30,70)
    heightb = random.randint(40, 90)
    friend.goto(startXb, startYb)
    drawH(friend, widthb, heightb)
    friend.goto((startXb + widthb + 30), startYb)
    drawA(friend, heightb)
    red.goto((startXb + 60 + (2 * widthb)), startYb)
    drawB(red, widthb, heightb)
    red.goto((startXb + 90 + (3*widthb)), startYb)
    drawW(red, widthb, heightb)
    startXc = random.randint(-200, -100)
    startYc = random.randint(-200, -100)
    widthc = random.randint(30,70)
    heightc = random.randint(40,90)
    friend.goto(startXc, startYc)
    drawH(friend, widthc, heightc)
    friend.goto((startXc + widthc + 30), startYc)
    drawA(friend, heightc)
    red.goto((startXc + 60 + (2 * widthc)), startYc)
    drawB(red, widthc, heightc)
    red.goto((startXc + 90 + (3*widthc)), startYc)
    drawW(red, widthc, heightc)
