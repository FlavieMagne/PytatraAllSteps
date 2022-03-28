import math

def cree(x, y):
    return (x, y)

def x(vecteur):
    return vecteur[0]

def y(vecteur):
    return vecteur[1]

# propriété calculée
def norme(vecteur):
    return math.sqrt(
        math.pow(vecteur[0], 2)+
        math.pow(vecteur[1], 2)
    )

def somme(vecteur1, vecteur2):
    return (
        vecteur1[0]+vecteur2[0],
        vecteur1[1]+vecteur2[1]
    )