# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""

FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]

# Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter
FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]
try:
    personnes = []
    i = 0
    while i < 8:
        valeur = int(input())
        personnes.append(valeur)
        i = i + 1
    
    i = 0
    invalide = False
    while i < 8:
        if personnes[i] < 0:
            invalide = True
        i = i + 1
    
    if invalide:
        print("Erreur - donnees invalides.")
    else:

# Calculer les intensites brutes (liste de 8 floats)
        intensites = []
        i = 0
        while i < 8:
            intensite = personnes[i] * FACTEURS[i]
            intensites.append(intensite)
            i = i + 1
# Calculer les niveaux normalises (liste de 8 entiers dans [0,10])
        maxI = intensites[0]
        i = 1
        while i < 8:
            if intensites[i] > maxI:
                maxI = intensites[i]
            i = i + 1

        niveaux = []
        if maxI == 0:
            i = 0
            while i < 8:
                niveaux.append(0)
                i = i + 1
        else:
            i = 0
            while i < 8:
                niveau = int((intensites[i] / maxI) * 10 + 0.5)
                niveaux.append(niveau)
                i = i + 1

# Afficher la grille (10 lignes) puis la ligne des labels
        ligne = 10
        while ligne >= 1:
            if ligne == 10:
                print("10 | ", end="")
            else:
                print(" " + str(ligne) + " | ", end="")
            
            col = 0
            while col < 8:
                if niveaux[col] >= ligne:
                    print("❚", end="")
                else:
                    print(".", end="")
                
                if col < 7:
                    print(" ", end="")
                else:
                    print()
                
                col = col + 1
            
            ligne = ligne - 1
        
        print("     A B C D E F G H")
        
except ValueError:
    print("Erreur - donnees invalides.")
