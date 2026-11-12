---
type: concept
tags: [year4]
aliases: [jump table, table de branchement, branch table]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.10.c|3.10.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une table de sauts (*jump table*) est un [[Tableau (programmation)|tableau]] d'adresses de code, indexé par une valeur entière. Pour exécuter la branche qui correspond à la valeur `v`, le programme lit l'adresse rangée en case `v` et y saute directement, au lieu de comparer `v` aux cas un par un. Le choix se fait ainsi en temps constant, $O(1)$, quel que soit le nombre de cas ([[Complexité algorithmique]]).

Les [[Compilateur|compilateurs]] s'en servent pour traduire un `switch` ([[Structure conditionnelle]]) quand les valeurs des `case` sont nombreuses et proches les unes des autres : la table a une case par valeur entre le plus petit et le plus grand `case`, les trous renvoyant au `default`. Avant de lire la table, le code vérifie que la valeur est dans l'intervalle couvert. Quand les valeurs sont rares et dispersées (`case 1`, `case 1000`, `case 50000`), la table serait trop grande : le compilateur produit alors une suite de comparaisons, ou une [[Recherche dichotomique|recherche dichotomique]] sur les valeurs triées. C'est une raison pour laquelle les étiquettes `case` doivent être des [[Expression constante|expressions constantes]] entières, connues à la compilation.

En [[Langage d'assemblage|assembleur]] x86-64, cela donne un saut indirect du type `jmp *table(,%rax,8)` ; on l'observe avec `gcc -S -O2` ou sur un explorateur de compilateur en ligne. En [[Langage C|C]], on peut écrire soi-même l'équivalent avec un tableau de pointeurs de fonctions :

```c
void nord(void), sud(void), est(void);
void (*actions[])(void) = { nord, sud, est };
if (choix >= 0 && choix < 3)
    actions[choix]();          // appel direct, sans comparer les cas
```

Le même principe sert aux tables de vecteurs d'[[Interruption|interruptions]] du processeur et aux tables de méthodes virtuelles du C++.

## Dans le cours

- [[tp3]] : le `switch` du programme 3.10 (cas 1, 2 et 3, valeurs consécutives) se prête à cette traduction ; la fiche l'explique comme complément.

Voir aussi : [[Structure conditionnelle]], [[Instructions break et continue]], [[Code machine]], [[Compteur de programme]].
