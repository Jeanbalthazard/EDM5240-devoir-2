#coding: utf-8

import csv

fichier = "concordia1.csv"
f1 = open(fichier)

lignes = csv.reader(f1)
next(lignes)

for ligne in lignes:
# j'ai créé une boucle afin de trouver toutes les variables nécessaires à la structure de la phrase.
    if "M." in ligne[6]:
# j'ai imposé une condition selon laquelle si on trouvait l'expression « M. » dans la colonne 6 (celle des thèses), une variable était établie. 
        these = ("La maîtrise")
    elif "Ph." in ligne[6]: 
        these = ("Le doctorat")
# j'ai imposé une autre condition, si jamais la boucle ne rencontrait pas la première. Dans le deuxième cas, donc, si on trouvait l'expression « Ph. », une autre variable était établie.
    nom = (ligne[1]+ " " + ligne[0])
# Cette variable me permet d'avoir le nom complet de l'auteur avec un espace entre son prénom et son nom de famille
    titre = (ligne[2])
# Cette varaible me permet d'avoir le titre complet de la thèse en question. 
    lgtitre = (len(str.strip(ligne[2])))
# Cette variable avec la fonction « len » me permet d'avoir la longueur du titre. J'ai appliqué la fonction « strip » afin d'ôter les espaces inutiles juste avant les guillemets ouvrants et fermants.
    print("{} de {} compte tant de pages. Son titre est « {} » et contient {} caractères.".format(these, nom, titre, lgtitre))
# Tel que vu durant le premier cours sur Python, on peut utiliser la fonction « format » pour attribuer des variables à certaines parties d'une phrase. 

# Cette section, qui m'aurait permis d'ajouter le nombre de pages, est incomplète. Malgré plusieurs heures à essayer de trouver une solution, je n'ai pas été en mesure de créer le code approprié.

# dictio = { 
#     "1000" : "m",
#     "900" : "cm",
#     "500" : "d",
#     "400" : "cd",
#     "100" : "c", 
#     "90" : "xc",
#     "50" : "l",
#     "40" : "xl",
#     "10" : "x",
#     "9" : "ix",
#     "5" : "v",
#     "4" : "iv",
#     "1" : "i"
#     }
    

# for ligne in lignes:
#     x = dictio.values()
#     y = dictio.keys()
#     if ligne[5].startswith(x) == 
