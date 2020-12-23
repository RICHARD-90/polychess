# Alpha-beta

'''
α la valeur du meilleur choix pour A (initial : −∞)
β la valeur du meilleur choix pour B (initial : +∞)
'''
class Joueur:
	'''
	Enregistrer des joueurs 
	'''
	pass

# mes joueurs:
A = Joueur()
B = Joueur()

# paramettre 
profondeur = 5
coups = 80 

# l'etat est donné par le polychess 
class Etat:
	pass
etat = Etat()
#fonction min_Max
def min_Max(joueur, profondeur, etat): 
	pass

# retourne un booleen qui dit si c'est la fin ou pas 
def fin(etat): 
	'''
	correspond au cas ou la profondeur est nulle ou l'etat est un noeud racine
	'''
	pass
# meilleur coup pour le joueur A
a = min_Max(A, profondeur, etat) 
# meilleur coup pour le joueur B
b = min_Max(B, profondeur, etat)  

def successeur(etat, objectif):
	pass

# alpha_beta pour le joueur A
def alpha_beta_A(etat, a, b):
	# si c'est deja la fin on retourne l'etat
	if fin(etat) : return eval(etat)
	# on initialise la valeur a −∞ 
	# v = -10000000000
	v = -80
	for s in successeur(etat, maxi):
		v = max(v,alpha_beta_B(s,a,b))
		if v >= b : return v
		a = max(v,a)
	return v

# alpha_beta pour le joueur B
def alpha_beta_B(etat, a, b):
	# si c'est deja la fin on retourne l'etat
	if fin(etat) : return eval(etat)
	# on initialise la valeur a +∞
	# v = 10000000000
	v = 80 
	for s in successeur(etat, mini):
		v = min(v,alpha_beta_A(s,a,b))
		if v <= a: return v
		b = min(v,b)
	return v