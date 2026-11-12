---
type: concept
tags: [year4]
aliases: [années bissextiles, leap year, 29 février]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.8.c|3.8.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une année bissextile compte 366 jours au lieu de 365, le jour ajouté étant le 29 février. Elle compense l'écart entre l'année civile de 365 jours et l'année tropique (le temps qui sépare deux équinoxes de printemps), d'environ 365,2422 jours : sans correction, le calendrier dériverait d'environ un quart de jour par an par rapport aux saisons.

Dans le [[Calendrier grégorien|calendrier grégorien]], la règle est la suivante : une année est bissextile si elle est divisible par 4 sans l'être par 100, ou si elle est divisible par 400. Ainsi 2024 et 2000 sont bissextiles, 1900 et 2026 ne le sont pas. Sur 400 ans, cela fait 97 années bissextiles, d'où une année moyenne de 365,2425 jours. Le calendrier julien, qu'il a remplacé, comptait une année bissextile tous les 4 ans sans exception (année moyenne de 365,25 jours).

En [[Langage C|C]], la règle s'écrit avec le reste de la [[Division euclidienne|division euclidienne]] (`%`) et les [[Opérateur logique|opérateurs logiques]] :

```c
int bissextile = (annee % 4 == 0 && annee % 100 != 0) || annee % 400 == 0;
```

`&&` étant prioritaire sur `||` ([[Associativité et ordre d'évaluation]]), les parenthèses sont facultatives, mais [[GCC]] conseille de les écrire (`-Wparentheses`). Le test peut aussi s'écrire avec des `if` imbriqués : divisible par 400, puis par 100, puis par 4 ([[Structure conditionnelle]]).

## Dans le cours

- [[tp3]] : le programme 3.8 lit une année et teste la règle avec `annee%4==0 && annee%100!=0 || annee%400==0`.

Voir aussi : [[Calendrier grégorien]], [[Divisibilité]], [[Norme ISO 8601]].
