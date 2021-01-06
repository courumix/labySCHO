from turtle import *

laby=[[0,1,0,0,0,0],
      [0,1,1,1,1,0],
      [0,1,0,1,0,0],
      [0,1,0,1,1,0],
      [0,1,1,0,1,0],
      [0,0,0,0,1,0]]

setup(800,800)
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
    

def labyturtle (laby):
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
    ht()
        
            

labyturtle(laby)

mainloop()