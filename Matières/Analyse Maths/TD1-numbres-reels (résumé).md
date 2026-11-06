---
type: source
tags: [year1]
sources: [".raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf"]
maj: 2026-11-06
---

Résumé de TD1-numbres-reels (`.raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf`) (4 pages, sans corrigé), dans [[Analyse Maths (matière)]]. TD sur les réels, en lien avec [[Chap1-reels (résumé)]]. Version 2020-2021.

## Thèmes et méthodes (19 exercices)

| Ex. | Thème | Méthode |
|---|---|---|
| 1, 2 | Rationnels et décimaux ; écriture fractionnaire de développements périodiques ($3{,}1414\ldots$, $0{,}999\ldots$, $3{,}1499\ldots$) | Multiplier par $10^k$ et soustraire. Piège : $0{,}999\ldots = 1$ |
| 3, 15 | Irrationalité de $\ln 3 / \ln 2$ et de $\sqrt2$ ; somme d'un rationnel et d'un irrationnel ; entre deux rationnels il y a un irrationnel | Raisonnement par l'absurde |
| 4, 5, 10 | Déterminer majorants, minorants, sup, inf, max, min : $\{x : -2 < x + 1/(2x) \le 2\}$, $\{1 + 1/n\}$, $\{x : x^2 < 2\}$, $\{1/n\}$, $\{1/n - 1/p\}$ | Écrire l'ensemble comme réunion d'intervalles, puis prouver sup et inf avec les deux conditions de caractérisation |
| 6 | Traduire en quantificateurs : majorant, majoré, non minoré, borné, non borné | Négation : $\forall$ devient $\exists$ |
| 7 | $\sup(-A) = -\inf A$ ; $\sup(A+B) = \sup A + \sup B$ ; produit $A\cdot B$ : l'égalité $\sup(AB) = \sup A \sup B$ est fausse en général | Il faut des éléments positifs pour le produit |
| 8 | $0 < mn/(m+n)^2 \le 1/4$, bornes de l'ensemble | Inégalité arithmético-géométrique, atteinte pour $m = n$ |
| 9 | $\sup\{\lvert x-y\rvert\} = \sup A - \inf A$ | Encadrer, puis choisir $x$ et $y$ proches des bornes |
| 11, 12 | Si $x \le y$ pour tout $x \in A$, $y \in B$, alors $\sup A \le \inf B$ ; sup et inf d'une réunion, d'une intersection, d'une inclusion | Majorant et plus petit majorant |
| 13, 14, 19 | Partie entière : croissance, $E(x)+E(y) \le E(x+y) \le E(x)+E(y)+1$, $E(x)+E(-x)$, $E(E(nx)/n) = E(x)$, formule d'Hermite $\sum_{k=0}^{n-1} E(x + k/n) = E(nx)$ | Encadrer $x = E(x) + \{x\}$ ; pour l'ex. 19, montrer que $f$ est de période $1/n$ puis nulle sur $[0, 1/n[$ |
| 16 | Écriture en base 10 : trouver $p$ en fonction de $n$ | Encadrement $10^p \le n < 10^{p+1}$, donc $p = E(\log_{10} n)$ |
| 17 | Moyennes $H \le G \le A$ ; inégalité de Bernoulli $(1+a)^n \ge 1+na$ | Carré $(\sqrt x - \sqrt y)^2 \ge 0$ ; récurrence |
| 18 | Cauchy-Schwarz pour des sommes | Polynôme $\sum (a_k + b_k x)^2 \ge 0$ de signe constant, discriminant négatif ou nul |

## À retenir

Pour prouver $\sup A = s$, vérifier deux choses : $s$ majore $A$, et tout réel $y < s$ n'est pas un majorant (voir [[Borne supérieure]]). Les exercices 7, 11 et 12 servent de lemmes pour la suite du cours.

## Liens

[[Borne supérieure]], [[Relation d'ordre]], [[Récurrence]], [[Produit scalaire]] (Cauchy-Schwarz), [[Chap1-reels (résumé)]].
