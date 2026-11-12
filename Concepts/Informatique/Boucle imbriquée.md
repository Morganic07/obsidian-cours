---
type: concept
tags: [year4]
aliases: [boucles imbriquées, nested loop, nested loops, double boucle]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp4/4.7.c|4.7.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une boucle imbriquée est une [[Boucle (programmation)|boucle]] placée dans le corps d'une autre boucle. Pour **chaque** tour de la boucle externe, la boucle interne s'exécute entièrement, du début à la fin.

```c
for (int i = 0; i < 3; i++)          // boucle externe : 3 tours
    for (int j = 0; j < 4; j++)      // boucle interne : 4 tours à chaque fois
        printf("(%d,%d) ", i, j);    // exécuté 3 × 4 = 12 fois
```

Le nombre total de tours est le **produit** des nombres de tours quand les bornes sont fixes ; quand la borne interne dépend du compteur externe (`for (j = 0; j <= i; j++)`), c'est une somme, ici $1 + 2 + \dots + n = \frac{n(n+1)}{2}$ ([[Somme des premiers entiers]]). Dans les deux cas, deux boucles sur $n$ éléments donnent une [[Complexité algorithmique|complexité]] en $O(n^2)$, trois en $O(n^3)$ : c'est souvent la partie coûteuse d'un programme.

Usages typiques : parcourir un tableau à deux dimensions ou une [[Matrice|matrice]] (lignes puis colonnes), comparer toutes les paires d'éléments ([[Tri par sélection]], [[Tri par insertion]]), tester tous les diviseurs de chaque nombre d'une liste ([[Nombre premier]], [[Nombre parfait]]), dessiner des motifs ([[Art ASCII]]).

Précautions :

- chaque boucle a son propre [[Compteur (programmation)|compteur]] (`i`, `j`) ; réutiliser `i` dans la boucle interne casse la boucle externe ;
- un [[Accumulateur (programmation)|accumulateur]] ou un [[Drapeau (programmation)|drapeau]] propre à la boucle interne doit être réinitialisé à chaque tour de la boucle externe, le plus sûr étant de le déclarer à l'intérieur ;
- `break` ne sort que de la boucle la plus intérieure ([[Instructions break et continue]]).

## Dans le cours

- [[tp4]] : les programmes 4.7 à 4.9 dessinent des motifs d'étoiles, la boucle externe parcourant les lignes et la boucle interne les colonnes.
- [[tp5]] : la liste des nombres premiers et celle des nombres parfaits testent les diviseurs de chaque nombre dans une boucle interne ; le drapeau `est_premier` doit être remis à 1 pour chaque nouveau nombre.

Voir aussi : [[Boucle (programmation)]], [[Complexité algorithmique]], [[Invariant de boucle]].
