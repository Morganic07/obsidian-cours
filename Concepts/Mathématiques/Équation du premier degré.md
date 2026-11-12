---
type: concept
tags: [year4]
aliases: [équation linéaire à une inconnue, équation ax+b=0, linear equation in one variable, équation du 1er degré]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp2/2.4.c|2.4.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une équation du premier degré à une inconnue $x$ est une équation qui peut s'écrire $ax + b = 0$, où $a$ et $b$ sont des réels donnés et $a \neq 0$. Elle a une unique solution :

$$ax + b = 0 \iff x = -\frac{b}{a}$$

On l'obtient en soustrayant $b$ aux deux membres puis en divisant par $a$, opérations qui conservent l'équivalence. Résoudre l'équation revient à chercher où s'annule la [[Fonction affine|fonction affine]] $f(x) = ax + b$, c'est-à-dire l'abscisse du point où sa droite coupe l'axe des abscisses.

Si $a = 0$, l'équation n'est plus du premier degré et devient $b = 0$ : aucune solution si $b \neq 0$, une infinité (tout réel) si $b = 0$. Un programme qui résout $ax + b = 0$ doit traiter ce cas à part pour ne pas diviser par zéro ([[Raisonnement par disjonction des cas]], [[Validation des entrées]]).

```c
if (a != 0)
    printf("x = %f\n", -b / a);
else if (b == 0)
    printf("tout réel est solution\n");
else
    printf("pas de solution\n");
```

Vérifier une solution approchée par `a*x + b == 0` en `float` échoue souvent, $-b/a$ n'étant pas exactement représentable ([[Comparaison de nombres flottants]]). L'équation du premier degré est le cas le plus simple des [[Système linéaire|systèmes linéaires]] ; au degré suivant vient l'[[Équation du second degré|équation du second degré]] $ax^2 + bx + c = 0$.

## Dans le cours

- [[tp2]] : le programme 2.4 lit les coefficients `a` et `b`, demande la solution à l'utilisatrice et vérifie `a*x+b==0` ; avec des `float`, la réponse `-0.333333` à $3x + 1 = 0$ est déclarée fausse.

Voir aussi : [[Fonction affine]], [[Équation du second degré]], [[Polynôme]].
