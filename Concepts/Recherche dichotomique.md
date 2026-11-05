---
type: concept
aliases: [dichotomie, recherche par dichotomie, approche par dichotomie, binary search]
matieres: [Algo]
sources: ["[[Chp1 - récursivité et complexité]]"]
maj: 2026-11-05
---

Recherche d'une valeur dans un tableau **trié**. On prend l'élément du milieu : s'il convient, c'est fini. Sinon, on cherche dans la moitié gauche si le milieu est plus grand que la valeur, dans la moitié droite sinon. On répète jusqu'à trouver la valeur ou à obtenir un intervalle vide (valeur absente, le cours renvoie $-1$).

Le cours donne une version itérative (`while gauche <= droite`) et une version récursive (`rechercheDichoRec(tab, debut, fin, valeur)`).

**Complexité de la version récursive** : la séparation coûte $\Theta(1)$ (calcul du milieu), la reconstruction rien. Un seul sous-problème de taille moitié : $T(n) = T(n/2) + \Theta(1)$, avec $a = 1$, $b = 2$, $k = 0$. On est dans le cas $a = b^k$, donc $O(\log_2 n)$. Voir [[Calcul de complexité et théorème de résolution]].

Liens : [[Récursivité]], [[Calcul de complexité et théorème de résolution]]

Résumé : [[Chp1 - récursivité et complexité (résumé)]]
