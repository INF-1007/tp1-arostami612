# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# Importer math
import math
# Lire les 4 valeurs
try:
    distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
    attente = float(input("Entrez le temps d'attente de la navette (en minutes) : "))
    temps_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
    controle = float(input("Entrez le temps de controle a l'entree (en minutes) : "))
# Validation
    if distance < 0 or attente < 0 or temps_metro < 0 or controle < 0:
        print("Erreur - donnees invalides.")
    else:
# Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
        temps_marche = distance * 60 / 5 + controle
        temps_navette = attente + distance * 60 / 18 + controle
        temps_metro_total = temps_metro + controle
        
        temps_marche = math.ceil(temps_marche)
        temps_navette = math.ceil(temps_navette)
        temps_metro_total = math.ceil(temps_metro_total)

# trouver temps min  
        temps_min = temps_marche
        if temps_navette < temps_min:
            temps_min = temps_navette
        if temps_metro_total < temps_min:
            temps_min = temps_metro_total
            
# compter combien de temps min       
        nb_min = 0
        if temps_marche == temps_min:
            nb_min = nb_min + 1
        if temps_navette == temps_min:
            nb_min = nb_min + 1
        if temps_metro_total == temps_min:
            nb_min = nb_min + 1
# Afficher la phrase exacte
        if nb_min == 1:
            if temps_marche == temps_min:
                print("Option la plus rapide : marcher.")
            elif temps_navette == temps_min:
                print("Option la plus rapide : navette.")
            else:
                print("Option la plus rapide : metro.")
        elif nb_min == 2:
            if temps_marche == temps_min and temps_navette == temps_min:
                print("Egalite : marcher et navette.")
            elif temps_marche == temps_min and temps_metro_total == temps_min:
                print("Egalite : marcher et metro.")
            else:
                print("Egalite : navette et metro.")
        else:
            print("Egalite : marcher, navette et metro.")
            
except ValueError:
    print("Erreur - donnees invalides.")
