import Point

def cree(x1, y1, x2, y2, couleur, epaisseur):
    return (
        (
            [Point.cree(x1, y1), Point.cree(x2, y2)],
            [couleur],
            [epaisseur]
        )
    )

def points(polygone):
    return polygone[0] 

def couleur(polygone, valeur=None):
    if valeur!=None:
        buffer = polygone
        buffer[1][0]=valeur
        polygone=buffer
    return polygone[1]

def epaisseur(polygone, valeur=None):
    if valeur!=None:
        buffer = polygone
        buffer[2][0]=valeur
        polygone=buffer
    return polygone[2]

def ajoute(polygone, x, y):
    buffer = polygone
    buffer[0].append(Point.cree(x, y))
    polygone=buffer