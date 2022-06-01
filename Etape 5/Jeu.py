from ast import Break
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
	pioche=Joueur.pioche(joueurCourant(jeu))
	nombrePlanchettes = Pioche.nombrePlanchettes(pioche)
	global GameStart
	GameStart=True
	endGame=False
	Decalage=choisisDecalage(jeu, Planchette)
	planchetteAPoser = selectionnePlanchette(jeu)
	desequilibre=False
	
	
	#sinon la partie peut commencer ou continuer
	while nombrePlanchettes!=0 and desequilibre==False and endGame!=True:
		# Dialogue.saisisEntier(selectionnePlanchette(jeu))
		Dialogue.saisisEntier("selectionnes une Planchette")
		Pioche.retire(pioche,Planchette.numero(planchetteAPoser))
		print("hello")	
		if planchetteAPoser==None: #si aucune planchette n'est désignée
			endGame=True #fin du jeu
			print("Jeu terminé")
			
		else:
			if GameStart:
				Pile.empileEtCalcule(pile(jeu),planchetteAPoser,0) #le decalage est nul car c'est la première
				majVues(jeu)
				passeJoueurSuivant(jeu)
				GameStart=False #car la première planchette est posée
				print(GameStart)
			else:
				#milieu de partie
				passeJoueurSuivant(jeu)
				if Decalage==None:
					endGame=True
					print("Jeu terminé")

				else:
					Pile.empileEtCalcule(pile(jeu),planchetteAPoser,Decalage)
					for empilement in pile(jeu):
						if Empilement.desequilibre(empilement):
							desequilibre=True
					majVues(jeu)
			
			print(nombrePlanchettes)
			break
	if desequilibre==True:
		print("Tu tombeeeees")
		Dialogue.afficheMessage(joueurCourant(jeu),"à perdu")

	else:
		
		if nombrePlanchettes==0:
			Dialogue.afficheMessage("Égalité!")
			print("je suis là")

#J'AI MIS DE LA MERDE DANS MES DIALOGUES."....."
def selectionnePlanchette(jeu):
	numero=0 #initialisé à 0
	#tant que la valeur entrée par le joueur est différente d'un nom de planchette de la pioche
	while Pioche.contient(Joueur.pioche(joueurCourant(jeu)),numero)!= True:
		#on lui demande re ressaisir un numero
		numero = Dialogue.saisisEntier("numero planchette voulue")
		#s'il ne met rien
		if numero==None:
			return None
	
	return Exemplaires.planchette(Joueur.pioche(joueurCourant(jeu))[Pioche.recherche(Joueur.pioche(joueurCourant(jeu)), numero)])
	
def choisisDecalage(jeu, planchetteAPoser):
	# if Fenetre.quitte(jeu):
	# 	return None
	# if GameStart==False:
	# 	return None
	# else:
	# 	planchetteAPoser=Dialogue.saisisEntier(jeu)
	# 	if planchetteAPoser<= Pile.sommet(pile):
	# 		pass
	# 	else:
	# 			return planchetteAPoser


	decalage = 0	#initialisation de la variable qui contiendra la valeur de décalage choisi sur 0
	if Pile.estVide(pile(jeu)) :
		pass
	else :
		marge = Planchette.marge(Empilement.planchette(Pile.sommet(pile(jeu))))
		longueur_dessous = Planchette.longueur(Empilement.planchette(Pile.sommet(pile(jeu))))
		longueur_dessus = Planchette.longueur(planchetteAPoser)
		
		while ((longueur_dessous/2 - marge) - longueur_dessus/2) < decalage < ((marge - longueur_dessous/2) + longueur_dessus/2) or abs(decalage) > ((longueur_dessous + longueur_dessus)/2)  :
			# decalage = Dialogue.saisisFlottant(Joueur.nom(joueurCourant(jeu)))
			decalage = Dialogue.saisisFlottant("yo")
			if decalage == None : break
			if ((longueur_dessous/2 - marge) - longueur_dessus/2) < decalage < ((marge - longueur_dessous/2) + longueur_dessus/2) :
				Dialogue.afficheMessage("Le décalage choisi est trop petit.\nLa planchette ne peut reposer que sur une marge.")
			elif abs(decalage) >= ((longueur_dessous + longueur_dessus)/2) :
				Dialogue.afficheMessage("Le décalage choisi est trop grand.\nLa planchette doit reposer sur la planchette précédente.")
	return decalage
