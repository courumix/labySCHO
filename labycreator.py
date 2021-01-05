from numpy import random

def labycreator (x,y,proba0):
    test=False
    while not test:
        laby=random.rand(x,y)
        laby[laby>proba0]=1
        laby[laby<=proba0]=0
        test=True
    return laby