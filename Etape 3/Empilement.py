import Planchette

def cree(planchette, centre):
	centreGeometrique=centre
	masse=Planchette.longueur(planchette) #la masse est égale à la longueur de la planchette
	desequilibre=False #la pile est à l'equilibre
	centreGravite=centre
	return [planchette, centreGeometrique, masse, centreGravite, desequilibre] #on cree une liste

def planchette(empilement):
	return empilement[0] #retourne la premiere valeur de la liste initialisée avec la fonction cree

def centreGeometrique(empilement): #en cm
	return empilement[1] #retourne la deuxieme valeur de la liste initialisée avec la fonction cree

def masse(empilement, valeur=None): #sans unite
	if valeur!=None:
		empilement[2]=valeur #si valeur est verifiee, elle remplace la valeur de la masse
	return empilement[2] #on retourne cette valeur

def centreGravite(empilement, valeur=None):
	if valeur!=None:
		empilement[3]=valeur
	return empilement[3]

def desequilibre(empilement, valeur=None):
	if valeur!=None:
		empilement[4]=valeur
	return empilement[4]

def versChaine(empilement):
	n=str(Planchette.numero(planchette(empilement)))
	m=str(masse(empilement))
	c=str(centreGeometrique(empilement))
	g=str(centreGravite(empilement))
	chaine="n°="+n+"m="+m+"c="+c+"g="+g
	if empilement[4]!=False: #la pile est en desequilibre
		chaine=chaine+"!"
	return chaine
