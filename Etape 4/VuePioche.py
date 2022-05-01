from tkinter import *

import Exemplaires
import Planchette
import Pioche
import Fenetre
import VuePlanchette

def dessine(fenetre, pioche, gauche):
	if gauche==True:
		#pioche à gauche
		Fenetre.toile(fenetre).create_text(50,200,text=Pioche.versChaine(pioche))
	else:
		#pioche à droite
		Fenetre.toile(fenetre).create_text(950,200,text=Pioche.versChaine(pioche))
	for exemplaire in pioche:
		planchette=Exemplaires.planchette(exemplaire)
		Fenetre.toile(fenetre).create_text(50,300,text=Exemplaires.versChaine(exemplaire))
		# Exemplaires.versChaine(exemplaire)
		return planchette