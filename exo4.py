# -*- coding: utf-8 -*-
# Exercice 04 - Verification d'une rampe d'accessibilite (gabarit)
"""
Objectif :
- DEMANDER : hauteur (cm, float) et longueur (m, float)
- Valider : hauteur >= 0 et longueur > 0
- Calculer :
    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle = atan(hauteur_m / longueur_m) en degres
- Verifier la conformite : pente <= 8.00

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT :
    Pente: PP.PP%
    Angle: AA.AA deg
    Conforme: OUI|NON
Si NON, afficher une 4e ligne :
    Depassement: DD.DD%

Prompts EXACTS :
1) "Entrez la hauteur a franchir (en centimetres) : "
2) "Entrez la longueur horizontale (en metres) : "
"""

# Importer math
import math
# Lire hauteur_cm et longueur_m
try:
    hauteur_cm = float(input("Entrez la hauteur a franchir (en centimetres) : "))
    longueur_m = float(input("Entrez la longueur horizontale (en metres) : "))
# Validation
    if hauteur_cm < 0 or longueur_m <= 0:
        print("Erreur - donnees invalides.")
    else:
# Calcul pente et angle
        hauteur_m = hauteur_cm / 100
        
        pente = (hauteur_m / longueur_m) * 100
        
        angle_rad = math.atan(hauteur_m / longueur_m)
        angle_deg = angle_rad * 180 / math.pi
# Affichage exact (+ ligne depassement si necessaire)
        print("Pente: " + "{:.2f}".format(pente) + "%")
        print("Angle: " + "{:.2f}".format(angle_deg) + " deg")
        
        if pente <= 8:
            print("Conforme: OUI")
        else:
            print("Conforme: NON")
            depassement = pente - 8
            print("Depassement: " + "{:.2f}".format(depassement) + "%")
            
except ValueError:
    print("Erreur - donnees invalides.")
