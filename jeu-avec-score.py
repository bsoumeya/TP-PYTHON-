# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import random

N = 20 # Nombre d'allumettes
print("Un ensemble de {} allumettes sont disposées devant vous.".format(N))
print("A chaque étape, vous pouvez retirer entre 1 et 4 allumettes")
print("Le joueur qui prend le dernier bâton a perdu. Vous jouez contre l'ordinateur et vous jouez en premier.")
print("")

val = 0
filename "score.txt"
score = 0

while(N >= 1):
    print("Allumettes disponibles: " + " | " * N)

    # Tour du joueur
    nb_allumettes_joueur = -1
    while(not nb_allumettes_joueur in range(1,5)):
        nb_allumettes_joueur = int(input("Combien d'allumettes souhaitez vous retirer ? (entre 1 et 4) : "))
    N = N - nb_allumettes_joueur
    if(N < 0):
       print("Vous avez perdu !")
       break;
    elif(N == 1):
        print("Vous avez gagné !")
        break;
    
    print("Tour de l'ordinateur, allumettes disponibles: " + " | " * N)
    # Tour de l'ordinateur
    # On essaye de prendre autant d'allumettes que nécessaire pour en laisser
    # un multiple de 6
    nb_allumettes_ordinateur = 0
    if(N <= 5):
        nb_allumettes_ordinateur = N - 1
        print("Vous avez perdu. L'ordinateur prends {} allumettes.".format(nb_allumettes_ordinateur))
        print("Vous prenez donc forcément la dernière")
        break
    else:
        nb_allumettes_ordinateur = N % 6
        if(nb_allumettes_ordinateur == 0):
            nb_allumettes_ordinateur = random.randint(1, 4)
        print("L'ordinateur prends {} allumettes.".format(nb_allumettes_ordinateur))
    N -= nb_allumettes_ordinateur
	
	score = score + 1
	
	file = open(filename, "w")
	scoreLu = []
	for val in file.read().split():
		if score > val
		scoreLu.append(int(score))
	file.close()