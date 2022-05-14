"""
Integrantes:
    Fernando de Jesús Mendivil Terminel - A00232280
    Randy Oliver Ortega Cota - A00232304
    Juan Pablo Capobianco Ramos - A01252252
    Jorge Leopoldo Jiménez Velásquez - A01253696
    
Aportes innovadores:
    Paredes que se cierran (idea de oliver)
    Decoración a la comida (idea de jorge)
    Comida envenenada (idea de fer)
    Color diferente por cada 2 comidas (idea de Juan Pablo)
"""

from turtle import *
from random import randrange
from cv2 import rectangle
from freegames import square, vector, line
import random

food = vector(0, 0)
amoebas = vector(10, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
ran = random.randint(0, 4)
ran2 = random.randint(0, 4)
a = ["gray", "blue", "yellow", "green", "purple", "red", "pink", "#e1e1e1", "#00ffff", "#FFD700"]
foodcolors = ["green", "red", "yellow", "purple", "brown"] # colores de comidas mas comunes

foodCounter = 0

def change(x, y):
    #esta funcion sirve para cambiar la posicion de la serpiente
    aim.x = x
    aim.y = y
    #se dibujan los limites jugables en cada entrada de movimiento
    limites(len(snake))

def inside(head, size):
    #return -200 < head.x < 190 and -200 < head.y < 190
    return (-200+size*2) < head.x < (190-size*2) and (-200+size*2) < head.y < (190-size*2)

def limites(size):
    pencolor("black")
    line(-200+size*2, -200+size*2, 190-size*2, -200+size*2)
    line(-200+size*2, 190-size*2, 190-size*2, 190-size*2)
    line(-200+size*2, -200+size*2, -200+size*2, 190-size*2)
    line(190-size*2, -200+size*2, 190-size*2, 190-size*2)

def move():
    #esta funcion sirve para mover a la serpiente
    head = snake[-1].copy()
    head.move(aim)
    
    if not inside(head, len(snake)) or head in snake:
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
        amoebas.x = randrange(-15, 15) * 10
        amoebas.y = randrange(-15, 15) * 10

    elif head == amoebas: 
        #aqui se le quita tamaño a la vibora si come amoebas (fer)
        print('Snake:', len(snake))
        amoebas.x = randrange(-15, 15) * 10
        amoebas.y = randrange(-15, 15) * 10
        snake.pop(0)
        snake.pop(0)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #Esto cambia el color de la serpiente
        if (len(snake) < 20):
            color = a[len(snake) // 2]
        else:
            color = a[9]
        square(body.x, body.y, 9, color)#esta funcion crea a la serpiente

    if (len(snake) < 25):
        square(food.x, food.y, 9, foodcolors[len(snake) // 5])#esta funcion dibuja el cuadradito
    else:
        square(food.x, food.y, 9, foodcolors[4])
    square(amoebas.x, amoebas.y, 9, "gray")#esta funcion dibuja las amoebas (fer)
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