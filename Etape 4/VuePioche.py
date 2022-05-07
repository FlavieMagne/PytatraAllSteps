from tkinter import *

import Exemplaires
import Planchette
import Pioche
import Fenetre
import VuePlanchette

def dessine(fenetre, pioche, gauche):
	if gauche==True:
		#pioche à gauche
		Fenetre.toile(fenetre).create_text(30,400,text=Exemplaires.versChaine(pioche[0]))
		Fenetre.toile(fenetre).create_text(30,420,text=Exemplaires.versChaine(pioche[1]))
		Fenetre.toile(fenetre).create_text(30,440,text=Exemplaires.versChaine(pioche[2]))
		Fenetre.toile(fenetre).create_text(30,460,text=Exemplaires.versChaine(pioche[3]))
		Fenetre.toile(fenetre).create_text(30,480,text=Exemplaires.versChaine(pioche[4]))
		Fenetre.toile(fenetre).create_text(30,500,text=Exemplaires.versChaine(pioche[5]))
		Fenetre.toile(fenetre).create_text(30,520,text=Exemplaires.versChaine(pioche[6]))
		Fenetre.toile(fenetre).create_text(30,540,text=Exemplaires.versChaine(pioche[7]))
		Fenetre.toile(fenetre).create_text(30,560,text=Exemplaires.versChaine(pioche[8]))
	
	else:
		#pioche à droite
		#970 correspond aux x et 410 indenté de 20 aux y
		Fenetre.toile(fenetre).create_text(970,400,text=Exemplaires.versChaine(pioche[0]))
		Fenetre.toile(fenetre).create_text(970,420,text=Exemplaires.versChaine(pioche[1]))
		Fenetre.toile(fenetre).create_text(970,440,text=Exemplaires.versChaine(pioche[2]))
		Fenetre.toile(fenetre).create_text(970,460,text=Exemplaires.versChaine(pioche[3]))
		Fenetre.toile(fenetre).create_text(970,480,text=Exemplaires.versChaine(pioche[4]))
		Fenetre.toile(fenetre).create_text(970,500,text=Exemplaires.versChaine(pioche[5]))
		Fenetre.toile(fenetre).create_text(970,520,text=Exemplaires.versChaine(pioche[6]))
		Fenetre.toile(fenetre).create_text(970,540,text=Exemplaires.versChaine(pioche[7]))
		Fenetre.toile(fenetre).create_text(970,560,text=Exemplaires.versChaine(pioche[8]))
	
	y0=400
	for exemplaire in pioche:
		if gauche:
		#on place les planchettes (fenêtre de 1000 pixels de large)
			x0=1000-940
		else:
			x0=1000-200
		
		#on récupère la fonction dessine de VuePlanchette
		#on passe en condition exemplaire[0] pour acceder seulement au tuple de l'exemplaire
		#car il est défini de tel sorte: [(...;...),int]
		VuePlanchette.dessine(fenetre,exemplaire[0],x0,y0) 
		#on indente de 20 les ordonnées
		y0=y0+20
		