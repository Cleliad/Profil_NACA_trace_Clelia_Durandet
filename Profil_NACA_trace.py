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
    tableau_up = np.zeros((len(x_c), 2), float)
    for i in range(len(x_c)):
        y_t = 5*t*(0.2969*math.sqrt(x_c[i])-0.1260*x_c[i]-0.3516*x_c[i]**2
                   + 0.2843*(x_c[i])**3-0.1038*(x_c[i])**4)
        x_up = x_c[i]*c
        tableau_up[i] = [x_up, y_t*c]
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


def tracer_graphique(tableau_up, tableau_down, x_c, deux_derniers_chiffres, c):
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100

    x_extrados = [((tableau_up[i][0])/c)*100 for i in range(len(x_c))]
    y_extrados = [((tableau_up[i][1])/c)*100 for i in range(len(x_c))]

    x_intrados = [((tableau_down[i][0])/c)*100 for i in range(len(x_c))]
    y_intrados = [((tableau_down[i][1])/c)*100 for i in range(len(x_c))]

    plt.plot(x_extrados, y_extrados, color='blue', label='extrados', linestyle='dashed')
    plt.plot(x_intrados, y_intrados, color='magenta', label='intrados', linestyle='dashed')

    affichage = str(deux_derniers_chiffres)
    plt.xlabel('% corde')
    plt.ylabel('axe vertical y (% corde)')
    plt.title('Graphique du profil NACA00' + affichage)
    plt.grid()
    plt.legend()
    plt.show()
