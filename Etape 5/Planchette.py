# Etape 2
Epaisseur = 1

def cree(longueur, marge):
	return (longueur, marge) #retourne un tuple avec longueur et marge de la planchette

def longueur(planchette):
	return planchette[0] #retourne la longueur totale de la planchette

def marge(planchette):
	return planchette[1] #retourne la longueur de la marge de la planchette

def numero(planchette):
	number = int(
		str(planchette[1])+str(planchette[0]-planchette[1]*2)+str(planchette[1])
	)
	return number #retourne le nombre de la planchette (LongueurMarge-LongueurZoneDePause-LongueurMarge)