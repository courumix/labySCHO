from labycreator import *
from labypile import *
from labyresolveur import *
from labyturtle import *

player = Turtle()
player.up()
player.setpos(-365,275)

fonctionne=False
x=15
y=15
ratio0=0.2
entree=(0,0)


while fonctionne == False:
    laby=labycreator(x,y,ratio0) 
    laby[entree]=1
    sortie=(len(laby)-1,len(laby[0])-1)
    T,solution=parcours(laby,entree,sortie)
    print(solution)
    print(T)
    if len(solution) != 0:
        fonctionne=True

labyturtle(laby)


###déplacement utilisateur###
up()
goto(-365,275)
def move_forward():
    setheading(90)
    fd(50)

def move_backward():
    setheading(270)
    fd(50)

def turn_left():
    setheading(180)
    fd(50)

def turn_right():
    setheading(0)
    fd(50)

player.screen.onkey(move_forward, 'Up')
player.screen.onkey(move_backward, 'Down')
player.screen.onkey(turn_left, 'Left')
player.screen.onkey(turn_right, 'Right')

player.screen.listen()


mainloop()