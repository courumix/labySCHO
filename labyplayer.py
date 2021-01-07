from labycreator import *
from labypile import *
from labyresolveur import *
from labyturtle import *

fonctionne=False
while fonctionne == False:
    laby=labycreator(15,15,0.5)
    T,solution=parcours(laby,[0,0],(14,14))
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

onkey(move_forward, 'Up')
onkey(move_backward, 'Down')
onkey(turn_left, 'Left')
onkey(turn_right, 'Right')

listen()
done()

mainloop()