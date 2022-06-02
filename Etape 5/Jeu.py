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

#supprime des 2 pioches
#se ferme parfois pour rien
	
	#on initialise les variables
	pioche=Joueur.pioche(joueurCourant(jeu))
	nombrePlanchettes = Pioche.nombrePlanchettes(pioche)
	global GameStart
	GameStart=True
	endGame=False
	desequilibre=False
	
	#sinon la partie peut commencer ou continuer
	while nombrePlanchettes!=0 and desequilibre==False and endGame!=True:
		planchetteAPoser = selectionnePlanchette(jeu)
		decalage=choisisDecalage(jeu, planchetteAPoser)
		Pioche.retire(pioche,Planchette.numero(planchetteAPoser))
		if planchetteAPoser==None: #si aucune planchette n'est désignée
			endGame=True #fin du jeu
			
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
				if decalage==None:
					endGame=True

				else:
					Pile.empileEtCalcule(pile(jeu),planchetteAPoser,decalage)
					for empilement in pile(jeu):
						if Empilement.desequilibre(empilement):
							desequilibre=True
					majVues(jeu)
			
			print(nombrePlanchettes)
		
	if desequilibre==True:
		Dialogue.afficheMessage("Tu as perdu !")
	else:
		if nombrePlanchettes==0:
			Dialogue.afficheMessage("Égalité !")


def selectionnePlanchette(jeu):
	numero=0 #initialisé à 0
	#tant que la valeur entrée par le joueur est différente d'un nom de planchette de la pioche
	print(Joueur.pioche(joueurCourant(jeu)), numero)
	while Pioche.contient(Joueur.pioche(joueurCourant(jeu)),numero)!= True:
		#on lui demande re ressaisir un numero
		numero = Dialogue.saisisEntier(Joueur.nom(joueurCourant(jeu)))
		if Pioche.contient(Joueur.pioche(joueurCourant(jeu)),numero)!=True:
			Dialogue.afficheMessage("La planchette choisie n'existe pas.")
		#s'il ferme
		if numero==None:
			return None

	numero = str(numero)
	marge = int(numero[0])
	longueur = int(numero[1]) + 2 * marge
	return Planchette.cree(longueur, marge)

def choisisDecalage(jeu, planchetteAPoser):
	decalage = 0	#initialisé à 0
	#s'il n'y a plus de planchette, on pass car il n'y aura evidemment pas de decalage
	if Pile.estVide(pile(jeu)) :
		pass
	#sinon on joue
	else :
		#on définit des variables pour simplifier les calculs
		marge = Planchette.marge(Empilement.planchette(Pile.sommet(pile(jeu))))
		longueurPLdessous = Planchette.longueur(Empilement.planchette(Pile.sommet(pile(jeu))))
		longueur_dessus = Planchette.longueur(planchetteAPoser)
		Calc1=longueurPLdessous/2 - marge - longueur_dessus/2
		Calc2=marge - longueurPLdessous/2 + longueur_dessus/2
		Calc3=longueurPLdessous + longueur_dessus/2
		
		#on fait quelques calculs:
		#on met abs pour la valeur absolue
		while Calc1<decalage<Calc2 or abs(decalage)>Calc3:
			decalage=Dialogue.saisisFlottant("Choisissez un déclage")
			#s'il n'y a pas de décalage, on ne fait rien
			if decalage==None: break
			#si le décalage est trop petit, c'est à dire si la planchette que l'on veut poser touche
			# #les 2 marges, on le dit 
			if Calc1 < decalage < Calc2:
				Dialogue.afficheMessage("Le décalage choisi est trop petit. La planchette ne doit reposer que sur une marge.")
			#Sinon, si le décalage est trop grand, on le dit, car la planchette
			#doit reposer sur celle d'en dessous
			elif abs(decalage)>=Calc3:
				Dialogue.afficheMessage("Le décalage choisi est trop grand.")
	return decalage
