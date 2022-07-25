# WaTOR

README

# Programmation du Projet WATOR

Le Projet WaTOR est un programme qui permet de visualiser une simulation d'un ecosystème entre poisson et requins vivant dans un espace torique. 

## Pré-Requis 

-Python

## Démarrage

Exécutez le programme avec **VSCODE** , dans la partie initialisation vous pouvez choisir le nombre de requins et de poissons, le temps de reproduction,l'énergie des requins et des poissons ainsi que la taille de l'environnement.
Vous pouvez également choisir le nombre de tour que vous voulez faire.

## Problèmes

Pour faire jouer nos requins ou nos poissons on va parcourir notre grille et les faires bouger de ligne en ligne. Certaines créatures peuvent donc bouger plus d'une fois dans un tour de jeu. 
Les requins n'ont pas d'énergies limite à partir du moment ou ils mangent un poisson ils gagnent +2 d'énergie.
L'écosystème a tendance à pencher en faveur des requins.
Comme il était indiqué en cours il n'y avait pas la contrainte de faire bouger que les poissons et les requins c'est à dire qu'à chaque fois qu'on boucle dans la grille si un poisson ou un requin bouge vers le bas à la ligne suivante il va rejouer un tour,l'affichage est fait après un tour complet de la grille si un poisson à la case 0.0 est à la case 5.3 c'est normal.
Pour les requins qui se mangent entre eux vous pouvez tester une grille de 5x4 avec 0 poissons et 20 requins et un temps de reproduction supérieur à leur énergie E ils vont mourrir à tour = E

## Fabriqué avec

- **Visual Studio Code** - Editeur de code
- **Git** - Logiciel de gestion.
- **GitHub** - Site web et service de cloud pour stocker et gérer le code.
- **Python** - Langage de programmation interprété.

## Versions

Dernière version : 1.0

## Auteurs

- Jeffrey NGUYEN 
- Yi ZHANG
- Omar SAHBOUN


