## Profil NACA - MGA 802

### But: 
Ce programme vous permet de tracer un profil NACA symétrique du type: NACA00XX avec XX correspondant à l'épaisseur maximale du profil


### Structure du programme:
- 2 fonctions pour créer les tableaux numpy des coordonnées des profils extrados et intrados avec les données suivantes:

  - Transformée de Glauert pour la distribution non uniforme: xc = 1/2 * (1 − cos θ) 
  - Equation de paramétrage: yt = 5t(0.2969√xc − 0.1260 xc − 0.3516 xc^2 + 0.2843 xc^3− 0.1036 xc^4)

- 1 fonction pour le tracé du graphique à l'aide de Matplotlib
- 1 fonction principale qui appelle les 3 autres fonctions et renvoit l'épaisseur maximale et sa position ainsi que le graphique


### Utilisation:
#### Entrées:
Le programme demande 4 entrées à l'utilisateur, il suffit de suivre les instructions de la console:
- Nom du profil NACA
- Longueur corde (en mètres)
- Nombres de points (pour la précision du tracé)
- Type de distribution: linéaire ou non uniforme

#### Sortie:
L'utilisateur obtient:
- l'épaisseur maximale du profil renseigné
- La position de l'épaisseur maximale sur la corde en % corde
- Le tracé du profil, les unités des axes sont en % corde
