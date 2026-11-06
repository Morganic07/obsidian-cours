---
type: source
tags: [year1]
sources: [".raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf"]
maj: 2026-11-06
---

Résumé du TD4 Applications, corrigé (PDF) (`.raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf`) (94 diapositives, algèbre, premier semestre 2023), dans [[Outil Maths (matière)]]. C'est le corrigé de [[TD4Applications (résumé)]] (les énoncés y sont listés). Cours : [[Chapitre4-Fonctions (1) (résumé)]], [[Injectivité et surjectivité]], [[Opérations sur les ensembles]]. Texte extrait en entier ; le résumé va par exercice, sans tout recopier.

## Résultats et méthodes par exercice

- **Ex. 1** (images et images réciproques de $\mathbb{R}_+$, $\mathbb{R}_-$, $\{-1\}$). Méthode : tracer le graphe, lire monotonie et image. $e^x$ : $f(\mathbb{R}_+) = [1, +\infty[$, $f(\mathbb{R}_-) = ]0,1]$, $f^{-1}(\mathbb{R}_-) = f^{-1}(\{-1\}) = \emptyset$. $\ln$ : $f^{-1}(\mathbb{R}_+) = [1,+\infty[$, $f^{-1}(\{-1\}) = \{e^{-1}\}$. $\cos$ : images dans $[-1,1]$, images réciproques en intervalles $+\, 2k\pi$.
- **Ex. 2** ($x^2$) : $f([-3,-1] \cup [-2,1]) = [0,9]$ égal à l'union des images ; $f([-3,-1] \cap [-2,1]) = [1,4]$, ici égal à l'intersection des images (cas particulier, la propriété générale est une simple inclusion) ; les images réciproques commutent avec union et intersection.
- **Ex. 3** ($\min(x^2, 3)$) : $f(\mathbb{R}) = [0,3]$, $f([2,+\infty[) = \{3\}$, $f^{-1}([0,1]) = [-1,1]$, $f^{-1}([4,+\infty[) = \emptyset$.
- **Ex. 4** : pour montrer qu'une application n'est pas injective, exhiber deux antécédents distincts ; pas surjective, exhiber un élément sans antécédent. $n \mapsto n+1$ : injective, non surjective sur $\mathbb{N}$ (0), bijective sur $\mathbb{Z}$. Homographie $\frac{x+1}{x-1}$ : injective, 1 sans antécédent. $(x,y) \mapsto (1, x-y, y)$ : injective, non surjective. $(x,y,z) \mapsto (x+y+z, x-y-z, x)$ : ni l'une ni l'autre (système incompatible si $a - c \neq c - b$). $(x,y) \mapsto (x+y, xy)$ : ni l'une ni l'autre (résoudre $t^2 - at + b = 0$ ; $(0,1)$ sans antécédent). $(x,y) \mapsto 2y$ : surjective, non injective. Le dernier cas ($xy - y^3$) est laissé au lecteur.
- **Ex. 5** : $1/x$ injective, non surjective sur $\mathbb{R}$, bijective de $\mathbb{R}^*$ sur $\mathbb{R}^*$ ; $\sin$ bijective de $[-\pi/2, \pi/2]$ sur $[-1,1]$ ; $x^2 + x$ bijective de $[-1/2, +\infty[$ sur $[-1/4, +\infty[$ (sommet de la parabole en $-1/2$). Composées : $\sin(1/x)$ définie sur $\mathbb{R}^*$ ; $1/\sin x$ définie sur $\mathbb{R} \setminus \pi\mathbb{Z}$.
- **Ex. 6** ($|1+x| + |1-x| - 2$) : paire, donc non injective ; trois expressions ($-2x-2$, $0$, $2x-2$) ; image $\mathbb{R}_+$ ; sur $[1,+\infty[$ vers $\mathbb{R}_+$ bijective, de réciproque $y \mapsto (y+2)/2$.
- **Ex. 7** : $f(n) = 2n$ injective, non surjective ; $g$ (moitié si pair) surjective, non injective ; $g \circ f = \mathrm{id}$, mais $f \circ g \neq \mathrm{id}$ ($n$ si pair, $2n$ si impair). Exemple type d'inverse à gauche sans être bijection.
- **Ex. 8** : $\sin(\pi x)$ surjective sur $[-1,1]$, non injective ; sa restriction à $]-1/2, 1/2[$ est bijective sur $]-1,1[$ (composée de deux bijections).
- **Ex. 9** ($\frac{3x+1}{x-2} = 3 + \frac{7}{x-2}$) : réciproque $y \mapsto \frac{2y+1}{y-3}$ de $\mathbb{R} \setminus \{3\}$ sur $\mathbb{R} \setminus \{2\}$.
- **Ex. 10** : « sa mère » est une application, ni injective ni surjective ; « sa sœur » n'en est pas une.
- **Ex. 11, 12** : preuves par double inclusion de $f(A \cup B) = f(A) \cup f(B)$, $f(A \cap B) \subset f(A) \cap f(B)$, de l'image réciproque avec $\cup$ et $\cap$, $f(A \cap f^{-1}(C)) = f(A) \cap C$, $A \subset f^{-1}(f(A))$, $f(f^{-1}(C)) = f(E) \cap C$ ; l'égalité $A = f^{-1}(f(A))$ pour tout $A$ caractérise l'injectivité (appliquer à un singleton) ; $f(f^{-1}(C)) = C$ pour tout $C$ caractérise la surjectivité.
- **Ex. 13** : quatre implications entre injectivité, surjectivité et composition. Dans $g \circ f$ : surjective $\Rightarrow$ $g$ surjective ; injective $\Rightarrow$ $f$ injective ; plus $g$ injective $\Rightarrow$ $f$ surjective ; plus $f$ surjective $\Rightarrow$ $g$ injective.
- **Ex. 14, 16** : appliquer l'exercice 13 à des composées bien choisies pour obtenir la bijectivité de chaque application.
- **Ex. 15** : $f$ bijective $\iff f(A^c) = f(A)^c$ pour tout $A$ (injectivité par la propriété appliquée à $\{x\}$, surjectivité avec $A = E$).
- **Ex. 17** : une surjection est simplifiable à droite ($g \circ f = h \circ f \Rightarrow g = h$).
- **Exercice supplémentaire** : vérité de huit propositions à quantificateurs sur $f : E \to F$ ; l'ordre $\forall \exists$ ou $\exists \forall$ change tout ($\forall x \exists y$ est la définition d'application, $\forall y \exists x$ la surjectivité, $\exists y \forall x$ une application constante).
- **Ex. 18** : fonctions indicatrices : $1_{A \setminus B} = 1_A - 1_A 1_B$, $1_{A \Delta B} = 1_A + 1_B - 2 \cdot 1_A 1_B$ ; $A \Delta (B \cap C) = (A \Delta B) \cap (A \Delta C) \iff A \cap (B \Delta C) = \emptyset$.
- **Ex. 19** ($z \mapsto z + 1/z$ sur $\mathbb{C}^*$) : non injective ($f(z) = f(1/z)$), surjective (équation $z^2 - az + 1 = 0$), image du cercle unité $[-2, 2]$ (car $f(e^{i\theta}) = 2\cos\theta$), image réciproque de $i\mathbb{R}$ égale à $i\mathbb{R}^*$ (voir ci-dessous).

## Méthodes à retenir

- Pour une image ou une image réciproque d'intervalle : tracer le graphe, puis découper selon la monotonie.
- Pour la bijectivité : résoudre $y = f(x)$ et vérifier qu'il y a une solution unique ; la solution est la réciproque.
- Pour une propriété de $f(A)$ ou $f^{-1}(C)$ : double inclusion en partant d'un élément.
- Pour les implications sur les composées : donner un nom à l'élément cherché et le construire avec $f(t)$ ou $g(y)$.

## Points à vérifier

- **Exercice 5, $f_2^{-1}(]-1,1[)$** : le corrigé donne $]-\pi/2, \pi/2[ + k\pi$. C'est faux : $\sin x \in ]-1,1[$ équivaut à $x \notin \pi/2 + \pi\mathbb{Z}$, soit $\mathbb{R} \setminus (\pi/2 + \pi\mathbb{Z})$ (complément).
- **Exercice 9, question 1** : le corrigé dit $f$ « décroissante » sur $\mathbb{R} \setminus \{2\}$, ce qui n'est vrai que sur chaque intervalle. Il écrit ensuite des bornes ouvertes pour $f([0,2[)$ et $f(]2,4])$ alors que $0$ et $4$ appartiennent aux intervalles : les images sont $]-\infty, -1/2]$ et $[13/2, +\infty[$ (complément).
- **Exercice 9, question 2** : les inégalités écrites pour $f^{-1}(]3,4])$ (« $3 \leq \ldots < 4$ ») ne correspondent pas à l'intervalle $]3,4]$ ; le résultat $[9, +\infty[$ est, lui, cohérent avec $]3,4]$ (complément). Les crochets de $f^{-1}([0,3[)$ sont illisibles dans le texte extrait : la bonne réponse est $]-\infty, -1/3]$.
- **Exercice 8, question 1** : « $\pi x$ est un antécédent de $y$ » doit se lire « $x/\pi$ » (coquille).
- **Exercice 19, question 3** : le raisonnement donne $\mathrm{Re}(z) = 0$ avec $z \neq 0$, donc $f^{-1}(i\mathbb{R}) = i\mathbb{R}^* $ et non $i\mathbb{R}$ (0 est exclu du départ) (complément).
- **Exercice 2, question 2** : une des égalités finales est écrite avec $]-\infty, 2[$ au lieu de $]-\infty, 2]$ (coquille).
