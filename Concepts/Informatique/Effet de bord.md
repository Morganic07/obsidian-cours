---
type: concept
tags: [year1, year3]
aliases: [side effect, side effects, effets de bord]
sources: ["[[Chp1 - Intro Java (résumé)|Chp1 - Intro Java]]", "[[AlgoID1 (résumé)]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une fonction ou une expression a un effet de bord quand, en plus de produire une valeur, elle modifie un état extérieur à elle : une [[Variable (programmation)|variable]] globale, un argument passé par référence, un objet mutable, un fichier, l'affichage. Par exemple, `i++` renvoie une valeur et modifie `i`. Quand une même expression contient plusieurs effets de bord, son résultat dépend de l'ordre d'évaluation de ses opérandes.

## Dans le cours

Nommé sans définition dans deux cours :

- **Algo Maths** (Year 1) : en Python, un argument est transmis par valeur, mais pour une valeur mutable c'est la référence qui est transmise ; l'appel peut alors créer des « effets secondaires (*side effects*) hors de la fonction » ([[AlgoID1 (résumé)]]).
- **Java** (Year 3) : [[Chp1 - Intro Java (résumé)|Chp1 - Intro Java]] mentionne les effets de bord (side effects) pour expliquer pourquoi l'ordre d'évaluation des opérandes compte.

Notion parente : [[Langage Java]]. Voir aussi : [[Associativité et ordre d'évaluation]], [[Opérateur d'incrémentation]].

Résumés : [[AlgoID1 (résumé)]], [[Chp1 - Intro Java (résumé)]]
