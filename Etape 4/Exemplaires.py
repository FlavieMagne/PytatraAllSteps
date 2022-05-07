import Planchette

def cree(planchette, nombre):
	#retourne une liste qui représente le nombre d’exemplaires d’une planchette
	return [planchette, nombre]

def planchette(exemplaires):
	#on retourne la planchette considérée par les exemplaires en question
	return exemplaires[0]

def nombre(exemplaires, valeur=None):
	#si la valeur est définie
	if valeur!=None:
		#valeur prend le nombre d'exemplaires
		exemplaires[1]=valeur
	return exemplaires[1]

def retireUn(exemplaires):
	#on retire un exemplaires
	exemplaires[1]=exemplaires[1]-1
	return exemplaires[1]

def versChaine(exemplaires):
	n=str(nombre(exemplaires)) #nombre exemplaires de la planchette
	p=str(Planchette.numero(planchette(exemplaires))) #planchette de numéro p
	nbr=n+"x"+p #on veut avoir le nombre x le numéro de la planchette
	return nbr
