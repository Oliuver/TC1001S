#Juego Viborita por Jorge

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
ran = random.randint(0, 4)
ran2 = random.randint(0, 4)
a = ["black", "blue", "yellow", "green", "purple"]

def change(x, y):
    #esta funcion sirve pa cambiar la posicion de la serpiente
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    #esta funcion sirve para mover a la serpiente
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        #con esta funcion se choca y se pone roja la cabecita
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        #esta funcion cambia la posicion de la comida cuando se la come
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, a[ran2])#esta funcion crea a la serpiente

    square(food.x, food.y, 9, a[ran])#esta funcion dibuja el cuadradito
    update()#update
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()