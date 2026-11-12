---
type: concept
tags: [year4]
aliases: [crible d'Eratosthène, crible d'Eratosthene, sieve of Eratosthenes]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp5/5.6.c|5.6.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : le crible d'Ératosthène, attribué au savant grec Ératosthène (IIIe siècle av. J.-C.), est un [[Algorithme|algorithme]] qui donne tous les [[Nombre premier|nombres premiers]] inférieurs ou égaux à un entier $N$. Au lieu de tester chaque nombre séparément, il élimine les multiples :

1. on prend un [[Tableau (programmation)|tableau]] de $N + 1$ cases, toutes marquées « premier » sauf 0 et 1 ;
2. pour chaque entier $p \ge 2$ encore marqué, tant que $p^2 \le N$, on raye ses multiples $p^2, p^2 + p, p^2 + 2p, \dots$ ;
3. les cases restées marquées sont les nombres premiers.

On commence à $p^2$ parce que les multiples plus petits, $kp$ avec $k < p$, ont déjà été rayés par le facteur $k$ ; et on s'arrête à $\sqrt N$ parce qu'un nombre composé $n \le N$ a forcément un diviseur premier $\le \sqrt n$ ([[Racine carrée]]).

```c
#include <stdbool.h>
#define N 100
bool premier[N + 1];
for (int i = 2; i <= N; i++) premier[i] = true;
for (int p = 2; p * p <= N; p++)
    if (premier[p])
        for (int m = p * p; m <= N; m += p)
            premier[m] = false;
```

Sa [[Complexité algorithmique|complexité]] est en $O(N \log \log N)$ opérations, presque linéaire, pour $O(N)$ mémoire ; tester chaque nombre par divisions successives jusqu'à $\sqrt n$ coûte au total $O(N \sqrt N)$. Le crible est donc la bonne méthode pour **lister** les premiers jusqu'à $N$, et le test par divisions pour savoir si **un** nombre est premier. Pour de très grands $N$, la mémoire devient la limite, et l'on crible par segments.

## Dans le cours

- [[tp5]] : alternative au programme 5.6, qui liste les nombres premiers jusqu'à 100 en testant chaque nombre séparément avec un [[Drapeau (programmation)|drapeau]] `est_premier`.

Voir aussi : [[Nombre premier]], [[Divisibilité]], [[Boucle imbriquée]], [[Recherche exhaustive]].
