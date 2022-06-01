import Dialogue
import Empilement
import Exemplaires
import Fenetre
import Joueur
import Pile
import Pioche
import Planchette
import VuePioche
import VuePile


# Etape 5.1

def cree():
	#retourne une liste représentant le jeu dans son état initial
	return [Fenetre.cree(1000,600), Pile.cree(), Joueur.cree(1), Joueur.cree(2), {'indiceJoueur':0}]

def fenetre(jeu):
	#retourne la fenêtre principale de l’application
	# return jeu[0]
	return Fenetre.tk(jeu)

def pile(jeu):
	#retour la pile de planchettes du jeu
	return jeu[1]

def joueurs(jeu):
	#retourne la liste des joueurs
	return [Joueur.nom(jeu[2]),Joueur.nom(jeu[3])]

def indiceJoueur(jeu):
	#retourne l’indice du joueur courant (0 ou 1)
	return jeu[4]['indiceJoueur']

def joueurCourant(jeu):
	#retourne le joueur courant du jeu
	#si son indice est de 0, alors c'est le Joueur1 qui est entrain de jouer
	if jeu[4]['indiceJoueur']==0:
		return jeu[2]
	#sinon c'est le Joueur2
	else:
		return jeu[3]

def passeJoueurSuivant(jeu):
	#passe au joueur suivant
	#si le Joueur1 joue, on passe au Joueur2 et inversement
	if indiceJoueur(jeu)==0:
		jeu[4]['indiceJoueur']=1
	else:
		jeu[4]['indiceJoueur']=0



# Etape 5.2

def joue(jeu):
	majVues(jeu) #on appelle la fonction
	activite(jeu)
	Fenetre.bouclePrincipale(fenetre(jeu))
	
	

def majVues(jeu):
	#initialise et affiche le jeu
	#on clean la fenêtre
	Fenetre.effaceGraphiques(fenetre(jeu))
	#on dessine la fenêtre avec ce qui va dedans
	VuePile.dessine(fenetre(jeu), pile(jeu))

	#on affiche les pioches des deux joueurs
	VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurCourant(jeu)), True)
	VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurCourant(jeu)), False)


# Etape 5.3

def activite(jeu):
	
	#on initialise les variables
	Pioche=Joueur.pioche(joueurCourant(jeu))
	global GameStart
	GameStart=True
	
	Decalage=choisisDecalage(jeu, Planchette)
	print("Hello")
	planchetteAPoser = selectionnePlanchette(jeu)
	Desequilibre=False
	
	nombrePlanchette=Pioche.nombrePlanchettes(Joueur.pioche(joueurCourant(jeu)))
	#doit sélectionner une planchette
	
	if planchetteAPoser == None :
		print("Jeu terminé") #s'il n'y a pas de planchette à poser, c'est fini

	#sinon la partie peut commencer ou continuer
	

	while nombrePlanchette!=0 and Empilement.desequilibre==False and planchetteAPoser!=None:
		Dialogue.afficheMessage("Sélectionnez une planchette",selectionnePlanchette(jeu))
		if planchetteAPoser==None:
			print("Jeu terminé")
		else:
			Pioche.retire(Pioche,Planchette.numero(planchetteAPoser))
			if GameStart:
				Pile.empileEtCalcule(pile(jeu),planchetteAPoser,0) #le decalage est nul car c'est la première
				majVues(jeu)
				passeJoueurSuivant(jeu)
				GameStart=False #car la première planchette est posée
			else:
				#milieu de partie
				passeJoueurSuivant(jeu)
				if Decalage==None:
					print("Jeu terminé")
				else:
					Pile.empileEtCalcule(pile(jeu),planchetteAPoser,Decalage)
					for empilement in pile(jeu):
						if Empilement.desequilibre(empilement):
							Desequilibre = True
				majVues(jeu)
	if Desequilibre==True:
		Dialogue.afficheMessage(Joueur.nom(joueurCourant(jeu)),+"a gagné!")
	else:
		if nombrePlanchette==0:
			Dialogue.afficheMessage("Égalité!")


def selectionnePlanchette(jeu):
	numero=0 #initialisé à 0
	#tant que la valeur entrée par le joueur est différente d'un nom de planchette de la pioche
	while Pioche.contient(Joueur.pioche(joueurCourant(jeu)),numero)!= True:
		#on lui demande re ressaisir un numero
		numero = Dialogue.saisisEntier(Joueur.nom(joueurCourant(jeu)) + ', entrez un numéro de planchette valide.')
		#s'il ne met rien
		if numero==None:
			return None
	
def choisisDecalage(jeu, planchetteAPoser):
	# if Fenetre.quitte(jeu):
	# 	return None
	if GameStart==False:
		return None
	else:
		planchetteAPoser=Dialogue.saisisEntier(jeu)
		if planchetteAPoser<= Pile.sommet(pile):
			pass




		
		else:
			return planchetteAPoser
