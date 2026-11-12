---
type: concept
tags: [year4]
aliases: [fonctions affines, affine function, coefficient directeur, ordonnée à l'origine]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp2/2.5.c|2.5.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une fonction affine est une [[Application (mathématiques)|fonction]] de $\mathbb{R}$ dans $\mathbb{R}$ de la forme

$$f(x) = ax + b$$

où $a$ est le **coefficient directeur** (la pente) et $b$ l'**ordonnée à l'origine** ($b = f(0)$). Son [[Graphe d'une fonction|graphe]] est une droite non verticale.

Propriétés :

- l'accroissement est proportionnel à celui de la variable : $f(x_2) - f(x_1) = a\,(x_2 - x_1)$, d'où $a = \dfrac{f(x_2) - f(x_1)}{x_2 - x_1}$ pour deux points distincts ;
- $f$ est croissante si $a > 0$, décroissante si $a < 0$, constante si $a = 0$ ([[Application monotone]]) ; sa [[Dérivabilité|dérivée]] vaut $a$ partout ;
- si $a \neq 0$, elle s'annule en un seul point, $x = -b/a$ ([[Équation du premier degré]]), et c'est une [[Bijection|bijection]] de réciproque $y \mapsto (y - b)/a$, elle aussi affine.

Cas particuliers : $b = 0$ donne une fonction **linéaire** $f(x) = ax$, qui traduit une situation de proportionnalité ; $a = 0$ une fonction constante. Le [[Développement limité|développement limité]] à l'ordre 1 approche une fonction dérivable par une fonction affine, sa [[Tangente à une courbe|tangente]]. En statistique, la régression linéaire cherche la fonction affine la plus proche d'un nuage de points ([[Moindres carrés]]).

## Dans le cours

- [[tp2]] : le programme 2.5 lit un réel `x` et affiche $f(x) = 3x + 4$ ; le fichier d'origine ne compilait pas, la chaîne de format de `scanf` étant coupée par un retour à la ligne.

Voir aussi : [[Équation du premier degré]], [[Transformation linéaire]], [[Polynôme]].
