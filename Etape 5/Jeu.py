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
	Fenetre.bouclePrincipale(fenetre(jeu))
	
	activite(jeu)

def majVues(jeu):
	#on clean la fenêtre
	Fenetre.effaceGraphiques(fenetre(jeu))
	#on dessine la fenêtre avec ce qui va dedans
	VuePile.dessine(fenetre(jeu), pile(jeu))

	#on affiche les pioches des deux joueurs
	VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurCourant(jeu)), True)
	VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurCourant(jeu)), False)


# Etape 5.3

def activite(jeu):
	Fenetre.quitte(fenetre(jeu))
	joueurCourant(jeu)

	if (Pioche.cree(jeu)!=0 and Empilement.desequilibre(jeu,False))==True:
		print("Sélectionnez une planchette",selectionnePlanchette(jeu))
		if selectionnePlanchette(jeu)!=None:
			pass
		else:
			print("Voulez-vous débuter une partie?", None)
			
	else:
		pass

	
# choisisDecalage(jeu, planchetteAPoser)

def selectionnePlanchette(jeu):
	dialogue=Dialogue.saisisNombre(jeu);
	if Fenetre.quitte(jeu):
		return None
	else:
		for dialogue in jeu:
			Dialogue.saisisFlottant(dialogue)
			Dialogue.saisisEntier(dialogue)
	
		return Dialogue.afficheMessage(jeu)

def choisisDecalage(jeu, planchetteAPoser):
	if Fenetre.quitte(jeu):
		return None
	else:
		planchetteAPoser=Dialogue.saisisEntier(jeu)
		if planchetteAPoser<= Pile.sommet(pile):
			pass




		
		else:
			return planchetteAPoser
