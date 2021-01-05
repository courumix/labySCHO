from copy import deepcopy
from labypile import *

laby=[[0,1,0,0,0,0],
      [0,1,1,1,1,0],
      [0,1,0,1,0,0],
      [0,1,0,1,1,0],
      [0,1,1,0,1,0],
      [0,0,0,0,1,0]]

lignes=len(laby)
colonnes=len(laby[0])

T=deepcopy(laby)
T[3][2]="hello"
e=(0,1)
a,b=e[0],e[1]
T[a][b]=8

for ligne in laby:
    print(ligne)
print("------------------")
for ligne in T:
    print(ligne)
    
def voisins(T,v):
    V=[]
    i,j=v[0],v[1]
    for a in (-1,1):
        if 0<=i+a<lignes:
            if T[i+a][j]==1:
                V.append((i+a,j))
        if 0<=j+a<colonnes:
            if T[i][j+a]==1:
                V.append((i,j+a))
    return V

def parcours(laby,entree,sortie):
    T=deepcopy(laby)
    p=pile()
    v=entree
    T[entree[0]][entree[1]]=-1
    return T