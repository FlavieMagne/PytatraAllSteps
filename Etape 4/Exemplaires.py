import Planchette

def cree(planchette, nombre):
	return [planchette, nombre] #retourne une liste contenant un type de planchette et le nombre

def planchette(exemplaires):
	return exemplaires[0]

def nombre(exemplaires, valeur=None):
	if valeur!=None:
		exemplaires[1]=valeur
	return exemplaires[1]

def retireUn(exemplaires):
	exemplaires[1]=exemplaires[1]-1
	return exemplaires[1]

def versChaine(exemplaires):
	n=str(nombre(exemplaires)) #nombre exemplaires de la planchette
	p=str(Planchette.numero(planchette(exemplaires))) #planchette de numéro p
	nbr=n+"x"+p #on veut avoir le nombre x le numéro de la planchette
	return nbr
