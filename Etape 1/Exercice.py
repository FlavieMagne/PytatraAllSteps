import random

def mystere():
	b = False
	c = 0
	i = random.randint(0, 100)
	print(i)
	while(not b):
		print("Entrez un nombre :")
		s = input()
		while (not s.isdigit()):
			print("Ce n'est pas un entier, recommencez")
			s = input()
		j = int(s)
		if (j > i):
			print("Trop grand !")
		elif (j < i):
			print("Trop petit !")
		else:
			b = True
		c += 1
	print("Score = " + str(c))

mystere()