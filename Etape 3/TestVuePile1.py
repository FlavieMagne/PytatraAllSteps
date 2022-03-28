import Fenetre
import Pile
import Planchette
import VuePile

pile = Pile.cree()
p181 = Planchette.cree(10, 1)

Pile.empileEtCalcule(pile, p181, 0)
for n in range(5):
	Pile.empileEtCalcule(pile, p181, 2)

fenetre = Fenetre.cree(1000, 600)
VuePile.dessine(fenetre, pile)
Fenetre.affiche(fenetre)
