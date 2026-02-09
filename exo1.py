# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# Lire le nom (str)
nom = input("Entrez votre nom complet : ")
# Lire les 4 valeurs (int)
matchs_football = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
duree_football = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
matchs_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
duree_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
# Valider les donnees (matchs >= 0, durees > 0)
if matchs_football < 0 or matchs_soccer < 0:
        print("Erreur - donnees invalides.")
elif duree_football <= 0 or duree_soccer <= 0:
    print("Erreur - donnees invalides.")
else:
# Calculer les minutes totales (football, soccer, total)
        total_minutes_football = matchs_football * duree_football
        total_minutes_soccer = matchs_soccer * duree_soccer
        total_minutes = total_minutes_football + total_minutes_soccer
        
# Convertir en heures/minutes et afficher exactement 4 lignes
        heures_football = total_minutes_football // 60
        minutes_football = total_minutes_football % 60
        
        heures_soccer = total_minutes_soccer // 60
        minutes_soccer = total_minutes_soccer % 60
        
        heures_total = total_minutes // 60
        minutes_total = total_minutes % 60

        
        print("Bonjour " + nom)
        print("Football (carabins): " + str(matchs_football) + " match(s), " + 
              str(heures_football) + "h" + str(minutes_football).zfill(2) + " de visionnage")
        print("Soccer (carabins): " + str(matchs_soccer) + " match(s), " + 
              str(heures_soccer) + "h" + str(minutes_soccer).zfill(2) + " de visionnage")
        print("Total: " + str(heures_total) + "h" + str(minutes_total).zfill(2))
