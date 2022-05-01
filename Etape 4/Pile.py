import Planchette
import Empilement

def cree():
	return [] #retourne une liste vide


def estVide(pile):
	estVide=not pile
	return estVide

def sommet(pile):
	if estVide(pile)==True:
		return None #renvoie None si la liste est vide
	else:
		return pile[-1] #si la liste n'est pas vide, renvoie l'empilement au sommet de la pile (au dernier élément de la liste)

def empile(pile, planchette, decalage):
	if estVide(pile)==True:
		pile.append(Empilement.cree(planchette,decalage)) #si la viste est vide, on lui ajoute une planchette
	else:
		pile.append(Empilement.cree(planchette,decalage+Empilement.centreGeometrique(sommet(pile)))) #si la liste n'est pas vide, on lui ajoute une planchette en prennantenn compte le centre geo de la planchette la plus au sommet


def versChaine(pile):

	piles=("-----------------------\n")
	for i in range(len(pile)-1,-1,-1): #pour lire les empilements du sommet au sol, car ils sont definis du sol au sommet dans la liste: pile
		#on cree une ligne par empilement et on récupère le fichier Empilement pour ne pas avoir a tout refaire
		piles+= str(Empilement.versChaine(pile[i]))+"\n"
	piles+=("^^^^^^^^^^^^^^^^^^^^^^^")
	return piles

def empileEtCalcule(pile, planchette, decalage):
	empile(pile, planchette, decalage)
	calculeCentresGravite(pile)
	calculeEquilibre(pile)

def calculeCentresGravite(pile):
	for i in range(len(pile)-1, 0, -1) : #on lit la liste à partir de la fin, jusquà l'élément 0, en incrémentant de 1 (-1 car sens inverse)
		#on récupère les éléments de notre tuple dans Empilement
		masse_dessus = pile[i][2]['masse'] #dans la liste pile, on se déplace dans tous les i (les planchettes) et on récupère l'élément 2 (la masse dans le tuple)
		longueur = pile[i-1][0][0]
		centre = pile[i-1][1]
		centreG_dessus = pile[i][2]['centreGravite']

		masse = longueur + masse_dessus #masse de l'empilement
		gi = (longueur*centre+masse_dessus*centreG_dessus)/masse #position du centre de gravité

		#on remplace les anciennes valeurs par les nouvelles
		pile[i-1][2]['masse'] = masse
		pile[i-1][2]['centreGravite'] = gi


def calculeEquilibre(pile):
	for i in range(len(pile)-1, 0, -1) : #on vérifie pour chaque empilement si il est en équilibre
		#on part tpujours du sommet jusqu'à 0 avec un pas de 1

		#on définit des variables pour que ce soit plus simple
		centreG_dessus = pile[i][2]['centreGravite'] #pour chaque empilement, on récupère le centreGravité, soit le 2 eme élément du tuple
		longueur = pile[i-1][0][0]
		centre = pile[i-1][1]

		if abs(centreG_dessus-centre)>longueur/2: #abs pour valeur absolue
			pile[i][2]['desequilibre']=True
		