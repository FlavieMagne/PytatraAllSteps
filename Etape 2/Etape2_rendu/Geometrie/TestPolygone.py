import Point
import Polygone

p = Polygone.cree(1, 2, 3, 4, 'bleu', 2.5)
print("p=" + str(p))
print(Polygone.points(p))

Polygone.ajoute(p, 5, 6)
Polygone.couleur(p, 'vert')
Polygone.epaisseur(p, 3)
print("p=" + str(p))

for point in Polygone.points(p):
	print(Point.vecteur(point))