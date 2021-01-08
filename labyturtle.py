from turtle import *
from labycreator import *

laby=labycreator(10,10,0.2)

setup(1000,1000)
up()
speed(0)
goto(-340,250)

def murcarre (longueur):
    down()
    for i in range(4):
        lt(90)
        fd(longueur)
    lt(135)
    fd(1.414*longueur)
    rt(135)
    up()
    fd(longueur)
    rt(135)
    down()
    fd(1.414*longueur)
    up()
    lt(135)
    fd(longueur)
    
def limite (longueur):
    down()
    for i in range(4):
        fd(longueur)
        lt(90)
    
def start ():
    up()
    goto(-390,275)
    color('Red')
    down()
    circle(25,extent=None,steps=None)
    
def end (laby):
    up()
    lignes=len(laby)
    colonnes=len(laby[0])
    sortieX=lignes-1
    sortieY=colonnes-1
    goto(-390,300)
    setheading(0)
    fd(50*sortieX)
    rt(90)
    fd(50*sortieY + 25)
    color('Green')
    down()
    circle(25,extent=None,steps=None)

def labyturtle (laby):
    delay(0)
    ht()
    tracer(0,0)
    lignes=len(laby)
    colonnes=len(laby[0])
    for i in range (lignes):
        for j in range(colonnes):
            if laby[i][j] == 0:
                murcarre(50)
                fd(50)
            else:
                fd(50)
        up()
        bk(50*lignes)
        rt(90)
        fd(50)
        lt(90)
    goto(-390,300)
    rt(90)
    down()
    pensize(2)
    limite(lignes*50)
    start()
    end(laby)
    update()

###déplacement utilisateur###
#up()
#goto(-365,275)
#def move_forward():
#    setheading(90)
#    fd(50)
#
#def move_backward():
#    setheading(270)
#    fd(50)
#
#def turn_left():
#    setheading(180)
#    fd(50)
#
#def turn_right():
#    setheading(0)
#    fd(50)
#
#onkey(move_forward, 'Up')
#onkey(move_backward, 'Down')
#onkey(turn_left, 'Left')
#onkey(turn_right, 'Right')
#
#listen()
#done()
#
#mainloop()