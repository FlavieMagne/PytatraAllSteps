import Vecteur
import Point

p = Point.cree(1, 2)
print("p=" + str(p))
print(Point.x(p))
print(Point.y(p))

Point.x(p, 3)
Point.y(p, 4)
print("p=" + str(p))
print(Point.vecteur(p))

v = Vecteur.cree(5, 6)
print("v=" + str(v))
Point.deplace(p, v)
print("p=" + str(p))
