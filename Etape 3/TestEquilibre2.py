import Pile
import Planchette

pile = Pile.cree()

p262 = Planchette.cree(10, 2)
p464 = Planchette.cree(14, 4)

Pile.empileEtCalcule(pile, p464, 0)
for n in range(2):
	Pile.empileEtCalcule(pile, p262, 3)
	Pile.empileEtCalcule(pile, p464, 2)
for n in range(2):
	Pile.empileEtCalcule(pile, p262, 3)
	Pile.empileEtCalcule(pile, p464, -2)
for n in range(2):
	Pile.empileEtCalcule(pile, p262, -3)
	Pile.empileEtCalcule(pile, p464, -3)

print(Pile.versChaine(pile))
