import Vecteur

def cree(x, y):
    dictcoord={
        "abscisse":x,
        "ordonnee":y,
    }
    return dictcoord

def x(point, valeur=None):
    if (valeur != None):
        point['abscisse']=valeur
    return point['abscisse']

def y(point, valeur=None):
    if (valeur != None):
        point['ordonnee']=valeur
    return point['ordonnee']

def vecteur(point):
    return (Vecteur.cree(point['abscisse'], point['ordonnee']))

def deplace(point, deplacement):
    point["abscisse"]=point["abscisse"]+deplacement[0]
    point["ordonnee"]=point["ordonnee"]+deplacement[1]
    pass