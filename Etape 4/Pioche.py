import Exemplaires
import Planchette

def cree():
	pioche = []
	for i in range(3) :
		for j in range(1, 4) :
			planchette = Planchette.cree(10+2*i, i+j)
			pioche.append(Exemplaires.cree(planchette, i+j))
	return pioche

def nombrePlanchettes(pioche):
	#on initialise une variable
	nombre=0
	#on cree une boucle qui récupère chaque exemplaires du jeu
	for i in pioche:
		nombre+=Exemplaires.nombre(i)
	return nombre

def versChaine(pioche):
	#on s'aide de notre travail dans Exemplaires
	#boucle qui récupère les nombres d'exemplaires et leurs numéros
	contenuPioche=""
	for planchette in pioche:
		contenuPioche+=Exemplaires.versChaine(planchette)+" "
	return 	contenuPioche

def recherche(pioche, numero):
	indice=-1
	for i in range(0,len(pioche)):
		#si le numéro recherché existe
		planchette=pioche[i] #recupere la planchette courante
		numero_planchette = int(Planchette.numero(Exemplaires.planchette(planchette))) #on recupere le numero
		if numero_planchette==numero and Exemplaires.nombre(planchette)>0: #si le numero de la planchette courante correspond au numero recherhce
			#on retourne ce numéro
			indice=i #on retourne son index
			break		
	return indice

def contient(pioche, numero):
	if recherche(pioche,numero)!=None:
		return True
	else:
		return False

def retire(pioche, numero):
	# on definit une variable qui va contenir la planchette correspondant au numéro passé en paramètre
	planchette_a_trouver=None
	# on parcourt la pioche pour trouver la planchette correspondant au numéro donné
	for i in range(0, len(pioche)):
		planchette=pioche[i] #recupere la planchette courante
		numero_planchette = int(Planchette.numero(Exemplaires.planchette(planchette))) # on recupère son numéro
		if numero_planchette==numero: # si le numéro de la planchette courante est égal au numéro donné...
			planchette_a_trouver=planchette # on stocke la planchette courante dans la variable définie au dessus

	#si la planchette demandée est présente dans la pioche...
	if contient(pioche,numero)==True:
		#on retire l'exemplaire demandé de la pioche
		Exemplaires.retireUn(pioche[recherche(pioche,numero)])
		# si la planchette est dans la pioche...
		if planchette_a_trouver is not None:
			# et si le nombre d’exemplaires après retrait atteint 0...
			if Exemplaires.nombre(planchette_a_trouver)==0:
				# alors on supprime l'élément recherché de la liste
				del(pioche[pioche.index(planchette_a_trouver)])
	else:
		#sinon aucune action n'est effectuée
		pass
