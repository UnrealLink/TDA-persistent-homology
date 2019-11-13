# TDA-persistent-homology

Implementation of an algorithm computing the persistent homology of a filtration.

- *main.py* Fichier à exécuter.
- *simplex.py* Définit la classe Simplex avec un ordre permettant de trier
les simplexes d'une filtration en respectant la contrainte d'une face
arrivant toujours avant un simplexe dans lequel elle apparait.
- *complex.py* Définit la classe Complex qui génère une liste de simplexes
à partir du fichier d'une filtration.
- *column.py* Définit l'objet Column qui est une représentation creuse d'une
colonne (liste des indices non nuls) sur laquelle nous avons implémenté
l'addition sur Z/2Z.
- *matrix.py* Définit la classe Matrix sur laquelle nous avons implémenté
l'algorithme de réduction à l'aide d'un pivot de Gauss, ainsi que la gé-
nération d'un code barre à partir de la matrice réduite. Pour accélérer
la recherche de pivots lors de la réduction, nous gardons en mémoire
pour chaque ligne l'indice de la colonne contenant le pivot s'il y en a
un, et -1 sinon.
- *utils.py* Implémente une recherche dichotomique dans une liste triée.
- *plot.py* Permet d'afficher le code barre.
- *data/* Contient les filtrations (celles des sphères et des boules sont dans
balls).
- *results/* Contient les codes barres calculés. (le fichier .txt le contient
sous le format voulu, le fichier .pickle contient l'objet binaire python).
