# ================================================================================================
# Auteur: Clélia Durandet
# Date: 31 mai 2024
# Profil NACA symétrique
# ================================================================================================

# IMPORTATION DES MODULES/LIBRAIRIES

import math
import matplotlib.pyplot as plt
import numpy as np
from math import *

# FONCTION 1: création des tableaux de valeurs extrados (up) et intrados (down)


def creer_tableau_profil_extrados(x_c, c, t):
    tableau_up = np.zeros((len(x_c), 2), float)  # création du tableau
    for i in range(len(x_c)):
        y_t = 5*t*(0.2969*math.sqrt(x_c[i])-0.1260*x_c[i]-0.3516*x_c[i]**2
                   + 0.2843*(x_c[i])**3-0.1038*(x_c[i])**4)
        x_up = x_c[i]*c
        tableau_up[i] = [x_up, y_t*c]  # ajout des tuples de coordonnées dans le tableau
    return tableau_up


def creer_tableau_profil_intrados(x_c, c, t):
    tableau_down = np.zeros((len(x_c), 2), float)
    for i in range(len(x_c)):
        y_t = 5*t*(0.2969*math.sqrt(x_c[i])-0.1260*x_c[i]-0.3516*x_c[i]**2
                   + 0.2843*(x_c[i])**3-0.1038*(x_c[i])**4)
        x_up = x_c[i]*c
        tableau_down[i] = [x_up, -y_t*c]
    return tableau_down


# FONCTION 2: tracé du profil NACA donné


def tracer_graphique(tableau_up, tableau_down, x_c, deux_derniers_chiffres, c, choix, index_position_corde):
    plt.rcParams['font.size'] = 12
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    x_extrados = [((tableau_up[i][0])/c)*100 for i in range(len(x_c))]
    y_extrados = [((tableau_up[i][1])/c)*100 for i in range(len(x_c))]

    x_intrados = [((tableau_down[i][0])/c)*100 for i in range(len(x_c))]
    y_intrados = [((tableau_down[i][1])/c)*100 for i in range(len(x_c))]

    x_epaisseur = np.ones((100, 1))*(index_position_corde/c)*100
    y_epaisseur = np.linspace(-100, 100, 100)

    plt.plot(x_extrados, y_extrados, color='blue', label='extrados', linestyle='dashed')
    plt.plot(x_intrados, y_intrados, color='magenta', label='intrados', linestyle='dashed')
    plt.plot(x_epaisseur, y_epaisseur, color='red', label='épaisseur maximale')

    affichage = str(deux_derniers_chiffres)  # pour écrire le nom du profil dans le titre du graphique
    plt.xlabel('% corde')
    plt.ylabel('axe vertical y (% corde)')
    plt.title('Graphique du profil NACA00' + affichage + ' ' + '(' + choix + ')')
    plt.axis((0., 100., -100., 100.))  # échelle des axes
    plt.grid()
    plt.legend()
    plt.show()


# FONCTION PRINCIPALE


def tracer_profil_naca():

    # Instructions et entrées utilisateur

    print('='*100, '\n', "Ce programme te permet de tracer un profil NACA symétrique (4 chiffres)\n", '='*100, '\n')
    while True:
        try:
            nom_profil = str(input("Nom du profil NACA sous le format 'NACA00XX':\n"))
            c = int(input('Quelle est la longueur de la corde (en mètres):\n'))
            nombre_points = int(input('Combien de points souhaites-tu pour le tracé: \n'))
            distribution = int(input('Quel type de distribution veux-tu: '
                                     'lineaire (tape 0) ou non uniforme (tape 1): \n'))

# Création du tableau de valeurs de x_c selon la distribution choisie

            if distribution == 1:  # non uniforme (transformée de Glauert)
                theta = np.linspace(0, pi, nombre_points)
                x_c = [0.5 * (1 - math.cos(angle)) for angle in theta]
                choix = 'non uniforme'
            else:  # linéaire
                x_c = np.linspace(0, 1, nombre_points)
                choix = 'linéaire'

            deux_derniers_chiffres = int(nom_profil[-2:])
            t = deux_derniers_chiffres / 100
            break
        except ValueError:
            print("Une des entrées est invalide. Veuillez essayer de nouveau.")

# Création des tableaux numpy des coordonnées des courbes extrados et intrados

    tableau_up = creer_tableau_profil_extrados(x_c, c, t)
    tableau_down = creer_tableau_profil_intrados(x_c, c, t)

# Affichage utilisateur
    print('=' * 35, 'Données', '=' * 35, '\n')
    print('Epaisseur maximale du profil: ', t, '\n')
    position_epaisseur_max = np.argmax(tableau_up[:, 1])
    index_position_corde = tableau_up[position_epaisseur_max, 0]
    print("Position de l'épaisseur maximale sur la corde:", (index_position_corde/c)*100, '% de la corde')
    print('=' * 80)

# Génération du tracé du profil complet à partir des tables de données

    tracer_graphique(tableau_up, tableau_down, x_c, deux_derniers_chiffres, c, choix, index_position_corde)


# Appel de la fonction principale

tracer_profil_naca()