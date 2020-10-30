#!/bin/python3
# impotieren von Funktionen
import turtle
import random
# Turtle erstellen, Hindergrundfarben definieren
elsa = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colours = ["cyan", "red", "green","brown"]
#anfangs strich der flocke
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()
# definition der schneeflocke
def branch():
    a = 0
    while a < 3:
        b = 0
        while b < 3:
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
            b = b + 1   
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
        a = a + 1
    elsa.right(90)
    elsa.forward(90)
        
        
# bau der schnneflocke
c = 0
while c < 8:
    branch()
    elsa.left(45)
    elsa.color(random.choice(colours))
    c = c + 1

