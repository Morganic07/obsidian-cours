---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp5 .docx|chp5 (Algèbre)]]"
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp5 .docx|chp5 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 5, [[Changement de base]]. En cas d'écart, le cours fait foi.

La [[Matrice|matrice]] qui représente une [[Transformation linéaire|application linéaire]] est construite avec une [[Base (algèbre linéaire)|base]] de départ et une base d'arrivée. Une autre base donne une autre matrice.

## Matrice de passage

Soit $E$ un espace vectoriel de dimension $n$, et $B = \{e_1, \dots, e_n\}$, $B' = \{e'_1, \dots, e'_n\}$ deux bases. On exprime les vecteurs de $B'$ en fonction de ceux de $B$ :
$$\begin{aligned} e'_1 &= p_{11} e_1 + p_{21} e_2 + \dots + p_{n1} e_n \\ e'_2 &= p_{12} e_1 + \dots + p_{n2} e_n \\ &\ \ \vdots \\ e'_n &= p_{1n} e_1 + \dots + p_{nn} e_n \end{aligned}$$

La **matrice de passage** de $B$ à $B'$, notée $P_{B \to B'}$, est la matrice dont les colonnes sont les coefficients des $e'_i$ dans $B$ : $P = (p_{ij})$.

**Théorème** : $P_{B \to B'} \cdot P_{B' \to B''} = P_{B \to B''}$.

## Action d'un changement de base sur les composantes d'un vecteur

**Théorème** : le cours écrit « Si X = X = » (hypothèse vide à l'export) puis $X^{-1} = P^{-1} \cdot X$. Il s'agit des nouvelles coordonnées : si $X$ et $X'$ sont les colonnes de coordonnées d'un même vecteur dans $B$ et $B'$, alors $X = PX'$ et $X' = P^{-1} X$ (complément, voir Erreurs du cours).

- $P = P_{B \to B'}$ et $P^{-1} = P_{B' \to B}$.

## Action d'un changement de base sur la matrice d'une application linéaire

**Théorème** :
$$A' = P^{-1} \cdot A \cdot P$$

- $A$ est la [[Matrice d'une application linéaire|matrice de $f$]] dans la base $B$ ;
- $A'$ est la matrice de $f$ dans la base $B'$ ;
- $P$ est la matrice de passage de $B$ à $B'$ (« nouveaux vecteurs en fonction des anciens ») ;
- $P^{-1}$ est la matrice de passage de $B'$ à $B$.

## Déterminant et familles libres

Le chapitre se termine par des résultats sur le [[Déterminant|déterminant]], repris dans [[6 - Algèbre linéaire|chp6]] :

- **Règle de calcul** : si l'on échange deux colonnes adjacentes, le déterminant change de signe.
- **Théorème** : soit $A = (c_1, \dots, c_n)$ (colonnes). $\det A \neq 0 \iff (c_1, \dots, c_n)$ est une base. Autrement dit, le déterminant est non nul si et seulement si les vecteurs colonnes forment une [[Indépendance linéaire|famille libre]].
- **Méthode** : pour démontrer qu'une famille de vecteurs est libre, on calcule le déterminant de la matrice formée de ses vecteurs colonnes. Vecteurs libres : $\det A \neq 0$ ; vecteurs liés : $\det A = 0$.
- Tous ces théorèmes valent aussi pour les **lignes** (souligné dans le cours).
- Un déterminant reste inchangé si l'on ajoute à une colonne (ou une ligne) une [[Combinaison linéaire|combinaison linéaire]] des autres (souligné dans le cours).

## Erreurs du cours

- [[Raw/Year 1/Algèbre Linéaire/Cours /chp5 .docx|chp5 (Algèbre)]] écrit « $X^{-1} = P^{-1} \cdot X$ » ; il faut « $X' = P^{-1} \cdot X$ » (nouvelles coordonnées) : un vecteur colonne n'a pas d'inverse. L'hypothèse « Si X = X = » est vide dans l'export du document, comme dans [[4 - Algèbre linéaire|chp4]].
- Pour $A' = P^{-1} A P$, le cours écrit « A est la matrice de F dans la base B » et « A' est la matrice de E dans la base B' » ; il faut « matrice de $f$ » dans les deux cas (corrigé dans la liste de cette fiche).
