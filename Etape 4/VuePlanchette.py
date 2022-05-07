from sys import builtin_module_names
from tkinter import *

import Fenetre
import Planchette

Facteur = 10 # 1 cm = 10 pixels

def pixels(cm): #retourne le nombre de pixels correspondant au nombre de cm
	return (Facteur*cm)

def dessine(fenetre, planchette, x0, y0): # dessine la planchette à l’intérieur de la toile de la fenetre
	can=Fenetre.toile(fenetre)
	#on convertit les longueurs et marges en pixels	
	marge=pixels(planchette[1])
	longueur=pixels(planchette[0])
	
	#x0 et y0 sont deja en pixels
	x1=x0+marge
	x2=x1+longueur-marge*2
	x3=x2+marge
	y1=y0+10

	#on dessine les planchettes
	can.create_rectangle(x0,y0,x1,y1,fill="grey") #cree un rectangle pour la marge de gauche
	can.create_rectangle(x1,y0,x2,y1,fill="pink") #cree un rectangle pour la zone de pause
	can.create_rectangle(x2,y0,x3,y1,fill="grey") #cree un rectangle pour la marge de droite
