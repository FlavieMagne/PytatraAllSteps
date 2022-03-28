from sys import builtin_module_names
from tkinter import *

import Fenetre
import Planchette

Facteur = 10 # 1 cm = 10 pixels

def pixels(cm): #retourne le nombre de pixels correspondant au nombre de cm
	return (Facteur*cm)

def dessine(fenetre, planchette, x0, y0): # dessine la planchette à l’intérieur de la toile de la fenetre
	can=Fenetre.toile(fenetre)

	#on convertit les zones de pause et marge en pixels	
	planchette1=pixels(planchette[1])
	planchette0=pixels(planchette[0])

	#x0 et y0 sont deja en pixels
	x1=x0+planchette1
	x2=x1+planchette0-planchette1*2
	x3=x2+planchette1
	y1=y0+10

	can.create_rectangle(x0,y0,x1,y1,fill="grey") #cree un rectangle pour la marge de gauche
	can.create_rectangle(x1,y0,x2,y1,fill="pink") #cree un rectangle pour la zone de pause
	can.create_rectangle(x2,y0,x3,y1,fill="grey") #cree un rectangle pour la marge de droite
