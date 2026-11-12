---
type: concept
tags:
  - year4
aliases:
  - IEEE 754
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-12
---

Nommée dans le cours de C sans plus de détail : c'est la norme appliquée pour lire des octets comme un nombre à virgule (`float`), en séparant signe, exposant et mantisse. Le cours cite aussi l'unité de calcul en virgule flottante (FPU).

Notion parente : [[Type primitif]]. Voir aussi : [[Complément à deux]].

## Dans le cours

- [[tp2]] : le programme 2.4 vérifie la solution de $ax + b = 0$ par `a*x+b == 0` en `float` ; pour $3x + 1 = 0$, la réponse `-0.333333` est déclarée fausse, $1/3$ n'étant qu'approché en binaire ([[Comparaison de nombres flottants]]).
- [[tp6]] : $\pi$ écrit avec 20 décimales dans le calcul des volumes (6.3), alors qu'un `double` n'en garde que 15 à 17 chiffres significatifs ; le reste est arrondi.
- [[formation C++]] : 2,3 n'est représentable exactement ni en `double` (2,2999999999999998…) ni en `float` (2,2999999523…), 53 et 24 bits de mantisse (programme 1-variables).

Résumés : [[1 - basiques]]
