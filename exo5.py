# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# Lire n (int) et statut (str)
try:
    n = int(input("Entrez le nombre de billets necessaires : "))
    statut = input("Entrez le statut etudiant (O/N) : ")
# Validation (n >= 0 et statut dans {O, N})
    if n < 0 or (statut != "O" and statut != "N"):
        print("Erreur - donnees invalides.")
    else:
        
        prix_24 = 66.00
        prix_12 = 36.00
        prix_5 = 15.75
        prix_unit = 3.60
        
        if statut == "O":
            prix_24 = prix_24 * 0.88
            prix_12 = prix_12 * 0.88
            prix_5 = prix_5 * 0.88
# Chercher la meilleure combinaison (A, B, C, D)
        meilleur_cout = -1
        meilleur_total_billets = -1
        meilleur_unitaires = -1
        meilleur_24 = 0
        meilleur_12 = 0
        meilleur_5 = 0
        
# toutes les combinaisons possibles
        nb_24 = 0
        while nb_24 * 24 <= n + 24:
            nb_12 = 0
            while nb_24 * 24 + nb_12 * 12 <= n + 12:
                nb_5 = 0
                while nb_24 * 24 + nb_12 * 12 + nb_5 * 5 <= n + 5:
                    billets_forfaits = nb_24 * 24 + nb_12 * 12 + nb_5 * 5
                    
                    if billets_forfaits >= n:
                        nb_unit = 0
                    else:
                        nb_unit = n - billets_forfaits
                    
                    total_billets = billets_forfaits + nb_unit
                    cout_total = nb_24 * prix_24 + nb_12 * prix_12 + nb_5 * prix_5 + nb_unit * prix_unit
                    
# Vérifier si c'est la meilleure solution
                    if meilleur_cout == -1:
                        meilleur_cout = cout_total
                        meilleur_total_billets = total_billets
                        meilleur_unitaires = nb_unit
                        meilleur_24 = nb_24
                        meilleur_12 = nb_12
                        meilleur_5 = nb_5
                    else:
                        ameliore = False
                        if cout_total < meilleur_cout:
                            ameliore = True
                        elif cout_total == meilleur_cout:
                            if total_billets < meilleur_total_billets:
                                ameliore = True
                            elif total_billets == meilleur_total_billets:
                                if nb_unit < meilleur_unitaires:
                                    ameliore = True
                        
                        if ameliore:
                            meilleur_cout = cout_total
                            meilleur_total_billets = total_billets
                            meilleur_unitaires = nb_unit
                            meilleur_24 = nb_24
                            meilleur_12 = nb_12
                            meilleur_5 = nb_5
                    
                    nb_5 = nb_5 + 1
                nb_12 = nb_12 + 1
            nb_24 = nb_24 + 1
# Calculer et afficher le resultat exact (6 lignes)
        print("Forfaits de 24 billets - " + str(meilleur_24))
        print("Forfaits de 12 billets - " + str(meilleur_12))
        print("Forfaits de 5 billets - " + str(meilleur_5))
        print("Billets unitaires - " + str(meilleur_unitaires))
        print("Total billets - " + str(meilleur_total_billets))
        print("Prix total - " + "{:.2f}".format(meilleur_cout) + "$")
        
except ValueError:
    print("Erreur - donnees invalides.")
