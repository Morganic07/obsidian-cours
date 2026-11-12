---
type: concept
tags: [year4]
aliases: [mention au baccalauréat, mention assez bien, mention bien, mention très bien]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.6.c|3.6.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en France, une mention qualifie le niveau atteint à un examen noté sur 20, selon la moyenne générale obtenue. Au baccalauréat :

| Moyenne $m$ sur 20 | Résultat |
|---|---|
| $m < 8$ | refusé |
| $8 \le m < 10$ | admis à passer les épreuves de rattrapage (second groupe) |
| $10 \le m < 12$ | admis, sans mention (« passable ») |
| $12 \le m < 14$ | mention assez bien |
| $14 \le m < 16$ | mention bien |
| $m \ge 16$ | mention très bien |

Les mentions ne sont attribuées qu'aux candidats admis dès le premier groupe d'épreuves, pas après le rattrapage. Depuis la session 2021, première du baccalauréat réformé, une moyenne d'au moins 18 vaut la mention très bien « avec les félicitations du jury » (ministère de l'Éducation nationale, bilan de la session 2021). Le même barème se retrouve pour le diplôme national du brevet et pour de nombreux diplômes de l'enseignement supérieur (licence, master).

En programmation, ce barème est l'exemple type d'une chaîne `if … else if … else` ([[Structure conditionnelle]]) : comme les conditions sont testées dans l'ordre, chaque branche peut se contenter de la borne supérieure, la borne inférieure étant garantie par l'échec des tests précédents. Les intervalles sont fermés à gauche et ouverts à droite (12 donne « assez bien », pas « passable ») : utiliser `<` et non `<=` évite une [[Erreur de décalage d'une unité|erreur de borne]]. Une moyenne hors de $[0, 20]$ doit être refusée avant ([[Validation des entrées]]).

## Dans le cours

- [[tp3]] : le programme 3.6 affiche la mention correspondant à une moyenne sur 20 avec une chaîne `else if` ; une moyenne hors de $[0, 20]$ n'y est pas traitée.

Voir aussi : [[Structure conditionnelle]], [[Validation des entrées]].
