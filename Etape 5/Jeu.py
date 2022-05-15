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
	return jeu[0]

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
	if indiceJoueur(jeu) == 0:
		jeu[4]['indiceJoueur'] = 1
	else:
		jeu[4]['indiceJoueur'] = 0



# Etape 5.2

def joue(jeu):
	Fenetre.affiche(fenetre(jeu))

def majVues(jeu):
	#on clean la fenetre
	Fenetre.effaceGraphiques(fenetre(jeu))
	#on dessine la fenetre avec ce qui va dedans
	VuePile.dessine(fenetre(jeu), pile(jeu))
	
	for gauche in enumerate(joueurs(jeu)):
		#si gauche est vrai, on dessine la pioche à gauche
		#sinon, à droite
		if gauche==True:
			VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurs, gauche))
		elif gauche==False:
			VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurs, gauche))


# Etape 5.3

def activite(jeu):
	pass

def selectionnePlanchette(jeu):
	return None

def choisisDecalage(jeu, planchetteAPoser):
	return None
