from turtle import Turtle
from random import randint

laura = Turtle()

laura.color('red')
laura.shape('turtle')

laura.penup()
laura.goto(-160, 100)
laura.pendown()

rik = Turtle()
lauren = Turtle()
Carrieanne = Turtle()

rik.color('green')
rik.shape('turtle')
rik.penup()
rik.goto(-160, 70)
rik.pendown()

Carrieanne.color('blue')
Carrieanne.shape('turtle')
Carrieanne.penup()
Carrieanne.goto(-160, 40)
Carrieanne.pendown()

lauren.color('purple')
lauren.shape('turtle')
lauren.penup()
lauren.goto(-160, 10)
lauren.pendown()

for movement in range(100):
    laura.forward(randint(1, 5))
    lauren.forward(randint(1, 5))
    rik.forward(randint(1, 5))
    Carrieanne.forward(randint(1, 5))

# ~~~python
input("Press Enter to close")
# ~~~