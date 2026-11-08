---
type: concept
tags: [year2]
aliases: [associative array, associative arrays, tableaux associatifs, tableau associatif AWK, map (structure de données)]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Cours TP5.docx|Cours TP5]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un tableau associatif (*associative array*, aussi appelé *map* ou dictionnaire) est une structure qui associe des **clés** quelconques (chaînes, nombres) à des **valeurs**, au lieu d'indices entiers consécutifs 0, 1, 2… comme un [[Tableau (programmation)|tableau]] classique. On y accède par la clé : `t["165"]`, `t["Paris"]`.

Il est en général implémenté par une [[Table de hachage]] : accès, insertion et recherche se font en temps moyen constant, $O(1)$, mais l'ordre des clés n'est pas garanti (il dépend du hachage, pas de l'ordre d'insertion).

## Dans le cours

En [[AWK]], **tout tableau est associatif**. Le TP5 compte les voitures par puissance dans `car.tsv` :

```bash
awk -F'\t' '{count[$4]++} END {for (power in count) print power, count[power]}' car.tsv
```

- `count[$4]++` utilise la valeur de la 4e colonne (la puissance) comme clé et incrémente le compteur associé ;
- une case absente vaut 0 (ou la chaîne vide) à sa première lecture, d'où l'absence d'initialisation ;
- `for (k in tab)` parcourt les clés dans un ordre **non spécifié**, ce qui explique que la sortie du TP ne soit pas triée ; pour la trier : `… | sort -n` ([[Commande sort]], [[Redirection et tube]]).

**Équivalents** (complément, hors du cours) : le [[Dictionnaire (Python)|dictionnaire Python]] (`d = {}`, `d[k] = d.get(k, 0) + 1`), et en Bash les tableaux déclarés par `declare -A tab`, puis `tab[cle]=valeur` et `${tab[cle]}`.

Voir aussi : [[AWK]], [[Tableau (programmation)]], [[Table de hachage]], [[Dictionnaire (Python)]].

Résumés : [[5 - TP5]]
