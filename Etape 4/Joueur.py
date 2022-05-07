import Pioche

def cree(numero):
	
	#on créer un tuple représentant un joueur par son numéro 
	#et sa pioche complète de 27 planchettes
	return (numero,Pioche.cree())

def numero(joueur):
	#on retourne le numéro du joueur
	return joueur[0]

def nom(joueur):
	#on définit son nom
	return "Joueur"+str(numero(joueur))

def pioche(joueur):
	#on retourne sa pioche
	return joueur[1]
