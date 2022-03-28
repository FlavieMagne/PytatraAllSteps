import Empilement
import Pile
import Planchette

pile = Pile.cree()

print("pile=" + str(pile))
print("estVide=" + str(Pile.estVide(pile)))
print("sommet=" + str(Pile.sommet(pile)))

p262 = Planchette.cree(10, 2)
p545 = Planchette.cree(14, 5)
Pile.empile(pile, p262, 0)
Pile.empile(pile, p262, 2)
Pile.empile(pile, p545, 3)

print("pile=" + str(pile))
print("estVide=" + str(Pile.estVide(pile)))
print("sommet=" + str(Pile.sommet(pile)))

print(Pile.versChaine(pile))
