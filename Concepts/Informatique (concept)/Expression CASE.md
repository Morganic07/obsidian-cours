---
type: concept
tags: [year3]
aliases: [CASE WHEN, instruction CASE]
sources: ["[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : en [[Langage SQL|SQL]], l'expression `CASE` renvoie une valeur choisie selon des conditions, à la manière d'un « si… alors… sinon » : `CASE WHEN condition1 THEN valeur1 WHEN condition2 THEN valeur2 ELSE valeur_par_défaut END`. Elle s'utilise partout où une valeur est attendue (`SELECT`, `ORDER BY`, à l'intérieur d'une [[Fonction d'agrégation|fonction d'agrégation]]) ; par exemple `SUM(CASE WHEN … THEN 1 ELSE 0 END)` compte les lignes qui vérifient une condition. Sans `ELSE`, elle renvoie `NULL` quand aucune condition n'est vraie.

## Dans le cours

Nommée sans définition dans le rapport du projet étudiant Ligue Football, qui l'utilise pour compter les victoires par équipe.

Notion parente : [[Langage SQL]]. Voir aussi : [[Fonction d'agrégation]].

Résumés (rapprochement, complément hors du cours) : [[2 - opérateurs et SQL (résumé)]]
