---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp5 .docx|chp5 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp5 .docx|chp5 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 5, [[Changement de base]].
La [[Matrice|matrice]] qui représente une [[Transformation linéaire|application linéaire]] est construite avec une [[Base (algèbre linéaire)|base]] de départ et une base d'arrivée. Une autre base donne une autre matrice.

## Matrice de passage

Soit $E$ un espace vectoriel de dimension $n$, et $B = \{e_1, \dots, e_n\}$, $B' = \{e'_1, \dots, e'_n\}$ deux bases. On exprime les vecteurs de $B'$ en fonction de ceux de $B$ :
$$\begin{aligned} e'_1 &= p_{11} e_1 + p_{21} e_2 + \dots + p_{n1} e_n \\ e'_2 &= p_{12} e_1 + \dots + p_{n2} e_n \\ &\ \ \vdots \\ e'_n &= p_{1n} e_1 + \dots + p_{nn} e_n \end{aligned}$$

La **matrice de passage** de $B$ à $B'$, notée $P_{B \to B'}$, est la matrice dont les colonnes sont les coefficients des $e'_i$ dans $B$ : $P = (p_{ij})$.

Exemple : dans $\mathbb{R}^2$, $B = (e_1, e_2)$ la base canonique et $B' = (e'_1, e'_2)$ avec $e'_1 = e_1 + e_2$ et $e'_2 = -e_1 + e_2$. On écrit en colonnes les coordonnées des nouveaux vecteurs dans l'ancienne base : $P_{B \to B'} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. [[Complément hors du cours|ⓘ]]

Une matrice de passage est toujours [[Matrice inversible|inversible]] : ses colonnes forment une base, donc son [[Déterminant|déterminant]] est non nul (voir la fin du chapitre). C'est aussi la matrice de l'application identité $\mathrm{Id}_E$ écrite de la base $B'$ (au départ) vers la base $B$ (à l'arrivée). [[Complément hors du cours|ⓘ]]

**Théorème** : $P_{B \to B'} \cdot P_{B' \to B''} = P_{B \to B''}$.

Avec $B'' = B$, on obtient $P_{B \to B'} \cdot P_{B' \to B} = P_{B \to B} = I_n$ : c'est pourquoi l'inverse de $P_{B \to B'}$ est $P_{B' \to B}$, comme l'écrit la section suivante. [[Complément hors du cours|ⓘ]]

## Action d'un changement de base sur les composantes d'un vecteur

**Théorème** : si $X$ et $X'$ sont les colonnes de coordonnées d'un même vecteur dans $B$ et $B'$, alors $X = PX'$ et les nouvelles coordonnées sont $X' = P^{-1} \cdot X$. [[Erreurs du cours#^e-5-algebre-lineaire|✎]]

- $P = P_{B \to B'}$ et $P^{-1} = P_{B' \to B}$.

Pourquoi $X = PX'$ : si $x = \sum_j x'_j e'_j$ et $e'_j = \sum_i p_{ij} e_i$, alors $x = \sum_i \big(\sum_j p_{ij} x'_j\big) e_i$, donc la $i$-ième coordonnée de $x$ dans $B$ est $\sum_j p_{ij} x'_j$, soit $X = PX'$. Le sens surprend : $P$ exprime les nouveaux vecteurs dans l'ancienne base, mais elle donne les **anciennes** coordonnées à partir des **nouvelles**. Avec l'exemple ci-dessus, le vecteur de coordonnées $X' = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ dans $B'$ (c'est $e'_1$) a pour coordonnées $X = PX' = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ dans $B$. [[Complément hors du cours|ⓘ]]

## Action d'un changement de base sur la matrice d'une application linéaire

**Théorème** :
$$A' = P^{-1} \cdot A \cdot P$$

- $A$ est la [[Matrice d'une application linéaire|matrice de $f$]] dans la base $B$ ; [[Erreurs du cours#^e-5-algebre-lineaire|✎]]
- $A'$ est la matrice de $f$ dans la base $B'$ ; [[Erreurs du cours#^e-5-algebre-lineaire|✎]]
- $P$ est la matrice de passage de $B$ à $B'$ (« nouveaux vecteurs en fonction des anciens ») ;
- $P^{-1}$ est la matrice de passage de $B'$ à $B$.

Démonstration en une ligne : soit $y = f(x)$, de coordonnées $X, Y$ dans $B$ et $X', Y'$ dans $B'$. Dans $B$, $Y = AX$ ; on remplace $X = PX'$ et $Y = PY'$, d'où $PY' = APX'$, puis $Y' = P^{-1}APX'$. Or $Y' = A'X'$ pour tout $X'$, donc $A' = P^{-1}AP$. Ici $f$ va de $E$ dans $E$ (un **endomorphisme**) et la même base sert au départ et à l'arrivée. [[Complément hors du cours|ⓘ]]

Pour $f : E \to F$ entre deux espaces différents, avec $P$ la matrice de passage dans $E$ et $Q$ celle dans $F$, la formule devient $A' = Q^{-1} A P$. [[Complément hors du cours|ⓘ]]

Deux matrices carrées $A$ et $A'$ liées par $A' = P^{-1}AP$ avec $P$ inversible sont dites [[Matrices semblables|semblables]] : elles représentent le même endomorphisme dans deux bases. Elles ont donc le même déterminant ($\det A' = \det P^{-1} \det A \det P = \det A$), la même [[Trace d'une matrice|trace]], le même [[Rang d'une matrice|rang]] et les mêmes [[Valeur propre|valeurs propres]]. Tout l'intérêt du changement de base est de choisir une base où la matrice est la plus simple possible, idéalement diagonale : c'est la [[Diagonalisation|diagonalisation]], vue au chapitre suivant sur les valeurs propres ([[7 - Algèbre linéaire|chp7]]). [[Complément hors du cours|ⓘ]]

## Déterminant et familles libres

Le chapitre se termine par des résultats sur le [[Déterminant|déterminant]], repris dans [[6 - Algèbre linéaire|chp6]] :

- **Règle de calcul** : si l'on échange deux colonnes adjacentes, le déterminant change de signe.
- Cela vaut pour l'échange de deux colonnes quelconques, adjacentes ou non : un tel échange s'obtient par un nombre impair d'échanges adjacents. Multiplier une colonne par $\lambda$ multiplie le déterminant par $\lambda$. [[Complément hors du cours|ⓘ]]
- **Théorème** : soit $A = (c_1, \dots, c_n)$ (colonnes). $\det A \neq 0 \iff (c_1, \dots, c_n)$ est une base. Autrement dit, le déterminant est non nul si et seulement si les vecteurs colonnes forment une [[Indépendance linéaire|famille libre]].
- **Méthode** : pour démontrer qu'une famille de vecteurs est libre, on calcule le déterminant de la matrice formée de ses vecteurs colonnes. Vecteurs libres : $\det A \neq 0$ ; vecteurs liés : $\det A = 0$.
- Tous ces théorèmes valent aussi pour les **lignes** (souligné dans le cours).
- Un déterminant reste inchangé si l'on ajoute à une colonne (ou une ligne) une [[Combinaison linéaire|combinaison linéaire]] des autres (souligné dans le cours).
