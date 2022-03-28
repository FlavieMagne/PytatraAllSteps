
# Fonctions fournies
# Attention : les exceptions ne sont pas au programme !

def estEntier(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def estReel(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

# Exemple 1 (pas de contrôle sur la saisie)
def exemple1():
	print("Entrez un nombre")
	s = input()
	print("C'est une chaîne")

# Exemple 2.1 (contrôle sur la saisie, pas de feedback)
def exemple21():
	print("Entrez un nombre")
	s = input()
	if (estEntier(s)):
		print("C'est un entier")

# Exemple 2.2 (contrôle sur la saisie, feedback)
def exemple22():
	print("Entrez un nombre")
	s = input()
	if (estEntier(s)):
		print("C'est un entier")
	else:
		print("Ce n'est pas un entier")

# Exemple 2.3 (contrôle sur la saisie, feedback)
def exemple23():
	print("Entrez un nombre")
	s = input()
	if (estEntier(s)):
		print("C'est un entier")
	elif (estReel(s)):
		print("C'est un réel")
	else:
		print("Ce n'est pas un nombre")

# Exemple 3 (contrôle sur la saisie, feedback et demande itérative)
def exemple3():
	print("Entrez un nombre")
	s = input()
	while (not estEntier(s) and not estReel(s)):
		print("Ce n'est pas un nombre")
		print("Entrez un nouveau nombre")
		s = input()
	if (estEntier(s)):
		print("C'est un entier")
	else:
		print("C'est un réel")

# exemple1()
# exemple21()
# exemple22()
# exemple23()
exemple3()
