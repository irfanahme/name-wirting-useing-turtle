# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:48:01 2018

@author: Arya
"""
import turtle


def letter_A(turtle):
    turtle.left(90)
    turtle.forward(200 / 2)
    for i in range(3):
        turtle.forward(200 / 2)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.forward(200)

def letter_I(turtle1):
    turtle1.forward(100)
    turtle1.backward(100 / 2)   
    turtle1.left(90)
    turtle1.forward(200)
    turtle1.right(90)
    turtle1.backward(100 / 2)
    turtle1.forward(100)

we=turtle.Screen()
i=turtle.Turtle()
i.penup()
i.setposition(-100,0)


i.pendown()
letter_I(i)


i.penup()

i.setposition(100,0)
i.pendown()
letter_A(i)
i.hideturtle()
we.exitonclick()