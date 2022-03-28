import Vecteur

v1 = Vecteur.cree(1, 2)
print("v1=" + str(v1))


print(Vecteur.x(v1))
print(Vecteur.y(v1))
print(Vecteur.norme(v1))

v2 = Vecteur.cree(3, 4)
print("v2=" + str(v2))

v3 = Vecteur.somme(v1, v2)
print("v3=" + str(v3))
