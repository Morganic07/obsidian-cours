---
type: concept
tags: [year4]
aliases: [élévation à la puissance, calcul d'une puissance, exponentiation naïve]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp6/6.1.c|6.1.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : l'exponentiation est l'opération qui, à une base $a$ et à un exposant $n$, associe la [[Puissance (mathématiques)|puissance]] $a^n$. Pour un exposant entier naturel, c'est une multiplication répétée, $a^n = a \times \dots \times a$ ($n$ facteurs), avec $a^0 = 1$ ; elle s'étend aux exposants négatifs ($a^{-n} = 1/a^n$ pour $a \neq 0$), puis rationnels et réels. Contrairement à l'addition et à la multiplication, elle n'est ni commutative ($2^3 = 8$ mais $3^2 = 9$) ni associative ($2^{(3^2)} = 512$ mais $(2^3)^2 = 64$) ; par convention, $a^{b^c}$ se lit $a^{(b^c)}$.

**Calcul en programmation.** La méthode naïve multiplie $n$ fois un [[Accumulateur (programmation)|accumulateur]] initialisé à 1, élément neutre de la multiplication :

```c
int puissance(int valeur, int exposant) {
    int resultat = 1;
    for (int i = 0; i < exposant; i++)
        resultat *= valeur;     // invariant : resultat = valeur^i
    return resultat;
}
```

Elle fait $n$ multiplications, donc une [[Complexité algorithmique|complexité]] en $O(n)$. L'[[Exponentiation rapide|exponentiation rapide]] utilise $a^{2k} = (a^k)^2$ et n'en fait qu'environ $2\log_2 n$ : $O(\log n)$. Deux pièges :

- le résultat croît très vite et sort de la capacité du type ([[Dépassement d'entier]]) : $2^{31}$ ne tient déjà plus dans un `int` de 32 bits ;
- l'ordre des arguments compte : `puissance(e, v)` calcule $e^v$, pas $v^e$.

La [[Bibliothèque standard du C|bibliothèque standard du C]] fournit `double pow(double x, double y)` dans `<math.h>` ([[Bibliothèque cmath]] en C++), qui accepte des exposants réels mais travaille en [[Nombre à virgule flottante|flottants]] : pour des entiers, une boucle ou l'exponentiation rapide évite les arrondis. Le C n'a pas d'opérateur de puissance : `^` y est le OU exclusif bit à bit ([[Opérateur bit à bit]]), et `2 ^ 3` vaut 1. [[Langage Python|Python]] écrit `2 ** 3`.

## Dans le cours

- [[tp6]] : la fonction `puissance(valeur, exposant)` du programme 6.1 calcule la puissance par une boucle de multiplications ; l'appel d'origine `puissance(e,v)` inversait base et exposant (2 puis 10 donnaient 1024 au lieu de 100).
- [[tp4]] : le programme 4.5 fait le même calcul directement dans `main` ([[Puissance (mathématiques)]]).

Voir aussi : [[Puissance (mathématiques)]], [[Exponentiation rapide]], [[Échelle logarithmique]].
