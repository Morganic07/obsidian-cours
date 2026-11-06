---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides]] (101 diapositives, texte, « Analyse 1, premier semestre 2026-2027 »), dans [[Analyse Maths (matière)]]. Ce sont les diapositives corrigées du TD1 « Réels ». Elles reprennent les exercices de [[TD1-numbres-reels (résumé)]] et en ajoutent (partie entière, dénombrement d'entiers). Cours associé : [[Chap1-reels (résumé)]].

## Exercices et méthodes de résolution

| Ex. | Sujet | Méthode du corrigé |
|---|---|---|
| 1, 2 | Rationnels, décimaux, irrationnels ($1/3$, $1/15$, $1/25$, $1/125$, $0{,}\overline3$, $\sqrt2$) ; fractions de $3{,}\overline{14}$, $0{,}\overline9$, $3{,}1\overline{49}$ | Un nombre est rationnel si et seulement si son écriture décimale est finie ou périodique. Deux méthodes pour la fraction : multiplication par $10^k$ puis soustraction, ou série géométrique $\sum a^k = 1/(1-a)$ |
| 3 | $\ln 3 / \ln 2$ irrationnel | Absurde : $p\ln 2 = q\ln 3$ donne $2^p = 3^q$ |
| 4 | Rationnel plus irrationnel ; $\sqrt2 \notin \mathbb{Q}$ ; un irrationnel entre deux rationnels | Absurde avec la stabilité de $\mathbb{Q}$ par somme et produit ; $\sqrt 2$ par parité |
| 5 | Quantificateurs : majorant, minorant, borné et leurs négations | « $A$ non minoré » : $\forall m,\ \exists x \in A,\ x < m$ ; « non borné » : $\forall M, \forall m, \exists x \in A,\ x < m$ ou $x > M$ |
| 6 | $I = \{x \ne 0 : -2 < x + \frac{1}{2x} \le 2\}$, réunion de deux intervalles ; sup, inf, max, min | Résoudre l'inéquation avec tableau de signe |
| 7 | Bornes de $\{1 + 1/n\}$, $\{1/p - 1/q\}$, $\{x : x^2 < 2\}$ | $\{x^2 < 2\} = ]-\sqrt2, \sqrt2[$ : sup et inf valent $\pm\sqrt2$ mais ne sont pas atteints ; pour $1/p - 1/q$, fixer $q = 1$ puis $p = 1$ pour approcher les bornes |
| 8 | $0 < \frac{mn}{(m+n)^2} \le \frac14$ et bornes de l'ensemble | Inégalité $(m-n)^2 \ge 0$ ; la borne $1/4$ est atteinte en $m = n$ ; $0$ est la borne inférieure |
| 9 à 11 | $\sup A \le \inf B$ si $x \le y$ pour tout couple ; $\sup(-A) = -\inf A$ ; $\sup(A+B) = \sup A + \sup B$ ; produit $A \cdot B$ | Double inégalité, avec l'une des caractérisations du sup. Contre-exemple pour le produit : $A = [-3,-1]$, $B = [1,4]$ donne $\sup(AB) = -1 \ne -4 = \sup A \cdot \sup B$. Il faut des ensembles de positifs |
| 12, 13 | $\{1/n\}$ ; $\sup\{\lvert x-y\rvert\} = \sup A - \inf A$ | Majoration par $\sup A - \inf A$, puis approcher les bornes |
| 14, 15 | $\sup(A \cup B) = \max(\ldots)$, $\inf(A \cup B)$, $\sup(A \cap B) \le \min(\ldots)$ | Double inégalité |
| 16, 17 | $E$ est croissante ; $E(x) + E(y) \le E(x+y) \le E(x) + E(y) + 1$ | $E(x) = \max\{n \in \mathbb{Z} : n \le x\}$, d'où $x - 1 < E(x) \le x$ |
| 18 | Dénombrements d'entiers : entre 1 et $x$, pairs, multiples de 3, couples de $x + 2y = n$, façons de payer 10 euros avec des pièces de 10 et 20 centimes | $0 \le 2k \le x \iff 0 \le k \le x/2$ donne $E(x/2) + 1$ pairs ; $x + 2y = n$ a $E(n/2) + 1$ solutions ; réponse $51$ pour les pièces |
| 19 | $(5E(x)+2)(3E(x)+6) = 0$ ; $(2E(x)+1)^2 < 4$ | Raisonner sur l'entier $E(x)$, puis revenir à $x$ |
| 20 | Formule d'Hermite $\sum_{k=0}^{n-1} E(x + k/n) = E(nx)$ | Montrer que $f$ est de période $1/n$, la calculer sur $[0, 1/n[$ |
| 21 | Cauchy-Schwarz | Polynôme $\sum (a_k + b_k x)^2$ de signe constant |
| 22 | $x \le H \le G \le A \le y$ ; Bernoulli $(1+a)^n \ge 1 + na$ | Carrés ; récurrence sur $n$ |
| 23 | Nombre de chiffres de $n$ | $p = E(\log_{10} n)$ |

## Points à vérifier

- **Exercice 19, question 2** : le corrigé écrit $-1 \le E(x) \le 0 \iff -1 < x < 1$ et conclut $S_2 = ]-1;1[$. L'ensemble correct est $[-1, 1[$ : $E(x) = -1$ correspond à $x \in [-1, 0[$, et $x = -1$ est bien solution. La même erreur figure dans le corrigé du DS1 de 2021 : voir [[DS1-correction-2021 (résumé)]].
- **Exercice 3** : le corrigé conclut « contradiction » à $2^p = 3^q$ sans la justifier. Il faut dire que $p$ et $q$ sont des entiers strictement positifs (car $\ln 3/\ln 2 > 0$) et que $2^p$ est pair alors que $3^q$ est impair (complément).

## Liens

[[Borne supérieure]], [[Relation d'ordre]], [[Récurrence]], [[Produit scalaire]], [[Dénombrement]].
