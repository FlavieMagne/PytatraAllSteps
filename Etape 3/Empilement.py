import Planchette

def cree(planchette, centre):
	# centreGeometrique=centre
	# masse=Planchette.longueur(planchette) #la masse est égale à la longueur de la planchette
	# desequilibre=False #la pile est à l'equilibre
	# centreGravite=centre
	return (planchette, centre, {'masse' : Planchette.longueur(planchette), 'centreGravite' : centre, 'desequilibre' : False})
def planchette(empilement):
	return empilement[0] #retourne la premiere valeur de la liste initialisée avec la fonction cree

def centreGeometrique(empilement): #en cm
	return empilement[1] #retourne la deuxieme valeur de la liste initialisée avec la fonction cree

def masse(empilement, valeur=None): #sans unite
	if valeur!=None:
		empilement[2]['masse']=valeur #si valeur est verifiee, elle remplace la valeur de la masse
	return empilement[2]['masse'] #on retourne cette valeur

def centreGravite(empilement, valeur=None):
	if valeur!=None:
		empilement[2]['centreGravite']=valeur
	return empilement[2]['centreGravite']

def desequilibre(empilement, valeur=None):
	if valeur!=None:
		empilement[2]['desequilibre']=valeur
	return empilement[2]['desequilibre']

def versChaine(empilement):
	n=str(Planchette.numero(planchette(empilement)))
	m=str(masse(empilement))
	c=str(centreGeometrique(empilement))
	g=str(centreGravite(empilement))
	chaine="n°="+n+" m="+m+" c="+c+" g="+g
	if empilement[2]['desequilibre']!=False: #la pile est en desequilibre
		chaine=chaine+"!"
	return chaine