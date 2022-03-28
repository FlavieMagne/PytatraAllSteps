import Planchette
import Empilement

def cree():
	return [] #retourne une liste vide


def estVide(pile):
	if pile!=None:
		pile=True #retourne vrai si la liste est vide
	else:
		pile=False #faux sinon
	return pile

def sommet(pile):
	if estVide(pile):
		return None #renvoie None si la liste est vide
	else:
		return pile[-1] #si la liste n'est pas vide, renvoie l'empilement au sommet de la pile (au dernier élément de la liste)

def empile(pile, planchette, decalage):
	if estVide(pile):
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
	#masse calculée du sommet au sol
	for i in range(len(pile)-2,-1,-1):

		Masse=Empilement.masse(pile[i])
		MasseSommet=Empilement.masse(pile[i+1]) #masse de l'empilement au sommet
		longueur=Planchette.longueur(Empilement.planchette(pile[i])) #longueur planchette a la base de la pile
		centre = Empilement.centreGeometrique(pile[i])
		centreGrav_dessus = Empilement.centreGravite(pile[i+1])

		mi=longueur+Masse
		# gi=(longueur*centre+MasseSommet*centreGrav_dessus)/mi
		gi=(longueur*centre+MasseSommet*centreGrav_dessus)/mi	

		pile[i][2][1]=mi
		pile[i][1][2]=gi 


		# if MasseSommet==longueur:
		# 	# Masse=Empilement.masse(pile[i])
		# 	mi=longueur+MasseSommet
		# 	gi=(longueur*centre+MasseSommet*centreGrav_dessus)/MasseSommet
		# else:
		
		# 	mi=longueur+MasseSommet
		# 	# gi=(longueur*centre+MasseSommet*centreGrav_dessus)/mi
		# 	gi=(longueur*centre+MasseSommet*centreGrav_dessus)/mi

		# 	#centre=somme des décalages de ts les centres geometriques?
			
		# 	#on remplace les valeurs précédentes par les nouvelles:
		# pile[i][2]=mi
		# pile[i][1]=gi 


def calculeEquilibre(pile):
	pass