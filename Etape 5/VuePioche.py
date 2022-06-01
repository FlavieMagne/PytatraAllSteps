from tkinter import *

import Exemplaires
import Planchette
import Fenetre
import VuePlanchette

def dessine(fenetre, pioche, gauche):
	y=400
	if gauche==True:
		#pioche à gauche
		#[::-1] pour inverser le sens des écritures dans pioche
		print(f'len pioche: {len(pioche)}')
		for i in range(len(pioche)):
			Fenetre.toile(fenetre).create_text(30,y+i*20,text=Exemplaires.versChaine(pioche[i])[::-1])
	
	else:
		#pioche à droite
		#970 correspond aux x et 410 indenté de 20 aux y
		print(f'len pioche: {len(pioche)}')
		for i in range(len(pioche)):
			Fenetre.toile(fenetre).create_text(970, y+i*20 ,text=Exemplaires.versChaine(pioche[i])[::-1])
	
	y0=400
	for exemplaire in pioche:
		#on place les planchettes
		if gauche:
			x0=60 
			
		else:
			#140 est la taille de la planchette la plus longue
			#et on retire la planchette actuelle pour bien la placer et avoir un alignement à droite
			x0=800+140-VuePlanchette.pixels(Planchette.longueur(exemplaire[0]))
		
		#on récupère la fonction dessine de VuePlanchette
		#on passe en condition exemplaire[0] pour acceder seulement au tuple de l'exemplaire
		#car il est défini de tel sorte: [(...;...),int]
		VuePlanchette.dessine(fenetre,exemplaire[0],x0,y0) 
		#on indente de 20 les ordonnées
		y0=y0+20
		
