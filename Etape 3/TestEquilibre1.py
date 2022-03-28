import Pile
import Planchette

pile = Pile.cree()
p181 = Planchette.cree(10, 1)

Pile.empileEtCalcule(pile, p181, 0)
for n in range(5):
	Pile.empileEtCalcule(pile, p181, 2)

print(Pile.versChaine(pile))
