---
type: concept
tags:
  - year1
  - year2
  - year4
aliases:
  - dichotomie
  - recherche par dichotomie
  - approche par dichotomie
  - binary search
  - recherche_dichotomique
matieres:
  - Algo
  - Analyse Maths
  - Algo Maths
  - graph theory
sources:
  - "[[chp 1 - récursivité et complexité (résumé)|Chp1 - récursivité et complexité]]"
  - "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[chp 3 - complexité (résumé)|chp3 - complexité]]"
maj: 2026-11-06
---

Recherche d'une valeur dans un tableau **trié**. On prend l'élément du milieu : s'il convient, c'est fini. Sinon, on cherche dans la moitié gauche si le milieu est plus grand que la valeur, dans la moitié droite sinon. On répète jusqu'à trouver la valeur ou à obtenir un intervalle vide (valeur absente, le cours renvoie $-1$).

Le cours donne une version itérative (`while gauche <= droite`) et une version récursive (`rechercheDichoRec(tab, debut, fin, valeur)`).

**Complexité de la version récursive** : la séparation coûte $\Theta(1)$ (calcul du milieu), la reconstruction rien. Un seul sous-problème de taille moitié : $T(n) = T(n/2) + \Theta(1)$, avec $a = 1$, $b = 2$, $k = 0$. On est dans le cas $a = b^k$, donc $O(\log_2 n)$. Voir [[Calcul de complexité et théorème de résolution]].

**Graph theory** (chapitre complexité) : dans un tableau trié de $n = 2^k$ éléments, le nombre d'étapes vérifie $v_{2^k} \le 1 + v_{2^{k-1}}$, d'où $O(\log n)$ ; pour un $n$ quelconque, on l'encadre entre deux puissances de 2. À comparer avec la [[Recherche séquentielle]] ; la preuve passe par une [[Récurrence]].

**Première année** : la dichotomie sert aussi hors des tableaux. En analyse, la preuve du [[Théorème des valeurs intermédiaires]] procède par dichotomie (intervalle coupé en deux, suites adjacentes, précision $(b-a)/2^n$) ; en algorithmique, on calcule une puissance par dichotomie ([[Exponentiation rapide]]).

Notions parentes : [[Diviser pour régner]], [[Complexité algorithmique]]. Liens : [[Récursivité]], [[Calcul de complexité et théorème de résolution]]

## À vérifier

- Dans [[chp 3 - complexité (résumé)|chp3 - complexité]], la fonction `recherche_dic` renverrait 0 si la valeur est trouvée, et non sa position (relevé du résumé).

Résumés : [[chp 1 - récursivité et complexité (résumé)]], [[chp 3 - complexité (résumé)]], [[AnalyseID1 (résumé)]], [[AlgoID1 (résumé)]]
