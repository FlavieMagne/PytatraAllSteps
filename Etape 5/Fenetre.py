from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Etape 2

Titre = 'Pytatra' #creation du titre

def cree(largeur, hauteur):
	fen = Tk()  #création variable fen contenant Tk
	fen.title(Titre) #attribution du titre 
	can = Canvas(fen, bg='dark grey',height=hauteur,width=largeur) #creation canvas
	can.pack()
	return (fen, can, largeur, hauteur) 

def toile(fenetre):
	return fenetre[1] #retourne le 2eme element du tuple

def largeur(fenetre):
	return fenetre[2] #retourne le 3eme element du tuple

def hauteur(fenetre):
	return fenetre[3] #retourne le 4eme element du tuple

def tk(fenetre):
	return fenetre[0] #retourne le 1er element du tuple (la fenetre)

def affiche(fenetre):
	tk(fenetre).mainloop() # démarrage du réceptionnaire d’événements

# Etape 5

TagGraphiques = 'graphique'
#bug dans le test, je pense qu'il faut appeler affiche et non bouclePrincipale
def effaceGraphiques(fenetre):
	#on ajoute un tag à tous les objects du canvas
	toile(fenetre).addtag_all(TagGraphiques)
	#on supprime les graphiques de la toile de la fenêtre
	toile(fenetre).delete(TagGraphiques)
		
def afficheMessage(fenetre, message):
	pass

def saisisTexte(fenetre, message):
	return None

def saisisEntier(fenetre, message):
	return None

def saisisFlottant(fenetre, message):
	return None
