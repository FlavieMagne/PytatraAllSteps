from tkinter import *

import Planchette
import Empilement
import Fenetre
import VuePlanchette

	
#on créer one fonction dessine_croix car nous en auront besoin pour la dessiner plus tard
def dessine_croix(fenetre, color, x, y) :
	taille = VuePlanchette.pixels(0.3)*Planchette.Epaisseur #0.3 est la taille de la croix
	Fenetre.toile(fenetre).create_line(x-taille, y-taille, x+taille, y+taille, fill = color, width = 2)
	Fenetre.toile(fenetre).create_line(x-taille, y+taille, x+taille, y-taille, fill = color, width = 2)
	#on trace deux lignes pour former une croix
def dessine(fenetre, pile):
	#canvas
	hauteur=Fenetre.hauteur(fenetre)
	largeur=Fenetre.largeur(fenetre)

	for i in range(len(pile)):
		#on définit les variables
		planchette = Empilement.planchette(pile[i])
		centre=Empilement.centreGeometrique(pile[i])
		longueur = Planchette.longueur(planchette)

		#on place la planchette (coin en bas à gauche)
		x0=largeur/2 + VuePlanchette.pixels(centre-longueur/2)#au milieu des abscisses
		#on divise la largeur par 2 pour être au milieu de la fenêtre
		#on convertit en pixels et on recipère le centre de la planchette du bas de l'empilement 
		#et on divise sa longueur par 2 car la définition de la planchette prend en compte le coin sup gauche
		y0=hauteur-40-VuePlanchette.pixels((i+1)*Planchette.Epaisseur)  #planchette pas posée sur le sol, mais à 40 pixels du sol
		#y0 tient compte de l'épaisseur de la planchette de dessous, pour se poser dessus
		
		#on affiche les planchettes
		VuePlanchette.dessine(fenetre, planchette, x0 , y0)

		# coordonnées de la croix
		x = Fenetre.largeur(fenetre)/2 + VuePlanchette.pixels(Empilement.centreGravite(pile[i]))
		#largeur fenetre /2 pour avoir le centre
		# et on ajoute le centre de gravité de la planchette
		y = Fenetre.hauteur(fenetre)-40-VuePlanchette.pixels((i+0.5)*Planchette.Epaisseur)
		#on prend la hauteur -40 pixels (comme précédemment) puis on soustrait le nbr de planchettes précédentes multipliée par l'épaisseur
		#le facteur 0.5 sert à ajuster la place de la croix

		#si la pile est en équilibre, on place une croix verte, sinon, elle est rouge
		if not Empilement.desequilibre(pile[i]):
			dessine_croix(fenetre, 'green', x, y)
		else:
			dessine_croix(fenetre, 'red', x, y)
		