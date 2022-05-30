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

def bouclePrincipale(fenetre):
	tk(fenetre).mainloop() # démarrage du réceptionnaire d’événements

# Etape 5

TagGraphiques = 'graphique'

def effaceGraphiques(fenetre):
	#on ajoute un tag à tous les objects du canvas
	# print(f"canvas: {toile(fenetre)}")
	toile(fenetre).addtag_all(TagGraphiques)
	#on supprime les graphiques de la toile de la fenêtre
	toile(fenetre).delete(TagGraphiques)
	

def quandOuverte(fenetre, fonction, argument):
	def fonctionInterne(e):
		# pour éviter les invocations ultérieures
		tk(fenetre).unbind('<Map>') 
		# invocation de la fonction principale
		fonction(argument)
	# liaison de l'évènement d'ouverture
	tk(fenetre).bind('<Map>', fonctionInterne)

def quitte(fenetre):
	tk(fenetre).quit()

def afficheMessage(message):
	showinfo("Pytatra", message)

def saisisEntier(message):
	return saisisNombre(message, True)

def saisisFlottant(message):
	return saisisNombre(message, False)

def saisisNombre(message, entier):
	saisie = None
	while (saisie == None):
		if (entier):
			saisie = askinteger("Pytatra", message)
		else:
			saisie = askfloat("Pytatra", message)
		if (saisie == None):
			reponse = askyesno("Pytatra", "Voulez-vous terminer le jeu ?")
			if (reponse):
				return None
	return saisie
