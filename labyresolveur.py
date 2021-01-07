from copy import deepcopy
from labypile import *
from labycreator import *

#laby=[[0,1,0,0,0,0],
#      [0,1,1,1,1,0],
#      [0,1,0,1,0,0],
#      [0,1,0,1,1,0],
#      [0,1,1,0,1,0],
#      [0,0,0,0,1,0]]
#
#laby=labycreator(10,10,0.2)
#
#lignes=len(laby)
#colonnes=len(laby[0])

#T=deepcopy(laby)
#T[3][2]="hello"
#e=(0,1)
#a,b=e[0],e[1]
#T[a][b]=8

#for ligne in laby:
#    print(ligne)
#print("------------------")
#for ligne in T:
#    print(ligne)
    
def voisins(T,v,laby):
    lignes=len(laby)
    colonnes=len(laby[0])
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
    T[v[0]][v[1]]=2
    recherche=True
    while recherche:
        vois=voisins(T,v,laby)
        if len(vois)==0:
            if len(p)==0:
                recherche=False
            else:
                v=depiler(p)
        else:
            empiler(p,v)
            v=vois[0]
            T[v[0]][v[1]]=2
            if v==sortie:
                empiler(p,v)
                recherche=False     
    return T,p
    