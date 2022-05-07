import Fenetre
import Planchette
import VuePlanchette

print(VuePlanchette.Facteur)
print(VuePlanchette.pixels(1))
print(VuePlanchette.pixels(12))
print()

f = Fenetre.cree(1000, 600)
epaisseur = VuePlanchette.pixels(Planchette.Epaisseur)

x0 = 10 #pixels
y0 = 10
for i in range(3):
	longueur = 10 + (2 * i)
	for j in range(3):
		marge = 1 + i + j
		print("")           #by myself
		for k in range(2):
			p = Planchette.cree(longueur, marge)
			print(Planchette.numero(p))
			VuePlanchette.dessine(f, p, x0, y0)
			y0 += epaisseur

Fenetre.affiche(f)
