---
type: concept
tags: [year4]
aliases: [suite de Lucas, nombre de Lucas, Lucas numbers]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp4/4.6.c|4.6.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : les nombres de Lucas, étudiés par le mathématicien français Édouard Lucas au XIXe siècle, forment la [[Suite numérique|suite]] définie par [[Récurrence|récurrence]] :

$$L_0 = 2, \quad L_1 = 1, \quad L_n = L_{n-1} + L_{n-2} \ (n \ge 2)$$

soit 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123… ; $L_{20} = 15\,127$. C'est la même récurrence que la [[Suite de Fibonacci|suite de Fibonacci]] ($F_0 = 0$, $F_1 = 1$), avec d'autres termes initiaux.

Propriétés :

- **formule explicite** : $L_n = \varphi^n + \psi^n$, où $\varphi = \frac{1 + \sqrt5}{2}$ est le [[Nombre d'or|nombre d'or]] et $\psi = \frac{1 - \sqrt5}{2}$ ; ce sont les racines de l'[[Équation caractéristique|équation caractéristique]] $r^2 = r + 1$. Comme $|\psi| < 1$, $L_n$ est l'entier le plus proche de $\varphi^n$ dès $n \ge 2$ ;
- le rapport $L_{n+1}/L_n$ tend vers $\varphi$, comme pour Fibonacci ;
- liens avec Fibonacci : $L_n = F_{n-1} + F_{n+1}$ et $F_{2n} = F_n L_n$ ;
- la croissance est exponentielle, en $\varphi^n \approx 1{,}618^n$ : $L_{45}$ dépasse déjà $2^{31} - 1$, la plus grande valeur d'un `int` de 32 bits ([[Dépassement d'entier]]).

Lucas s'en est servi pour ses tests de primalité, dont le test de Lucas-Lehmer des [[Nombre de Mersenne|nombres de Mersenne]].

**Calcul itératif.** Comme pour Fibonacci, on garde les deux derniers termes dans deux variables qu'on décale à chaque tour, en $O(n)$ ; la version récursive directe recalcule les mêmes termes et coûte un temps exponentiel ([[Récursivité]], [[Programmation dynamique]]).

```c
long a = 2, b = 1;                 // L0, L1
for (int i = 2; i <= 20; i++) {
    long c = a + b;                // L(i)
    a = b; b = c;                  // décalage
}
```

## Dans le cours

- [[tp4]] : le programme 4.6 affiche $L_0$ à $L_{20} = 15\,127$ avec deux variables qu'il décale à chaque tour.

Voir aussi : [[Suite de Fibonacci]], [[Nombre d'or]], [[Récurrence]].
