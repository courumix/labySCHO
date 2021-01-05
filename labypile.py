def pile():
    return []

def vide(p):
    return p==[]

def empiler(p,x):
    p.append(x)

def depiler(p):
    assert not vide(p), "Pile vide"
    return p.pop()

def taille(p):
    return len(p)

def sommet(p):
    sommet=taille(p)-1
    return p[sommet]