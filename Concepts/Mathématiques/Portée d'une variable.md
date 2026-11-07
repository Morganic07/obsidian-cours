---
type: concept
tags: [year1, year3]
aliases: [portée d'une variable, portée des variables, scope d'une variable, erreur de scope, variable locale, variables locales, variable globale, variables globales]
matieres: [Java, Algo Maths]
sources: ["[[Chp1 - Intro Java (résumé)|Chp1 - Intro Java]]", "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

La portée d'une variable est la région du code où l'on peut l'utiliser, en écriture comme en lecture. Les régions sont en général délimitées par des paires d'accolades `{ ... }`.

Dans une même portée, tous les noms de variables doivent être uniques.

**Erreur classique** : une variable déclarée dans le bloc d'un `do { ... }` n'existe plus en dehors de ce bloc, donc elle ne peut pas servir dans la condition `while (x < 10)` qui suit. Erreur de compilation ([[Boucle (programmation)]]).

**En algo de 1re année** : une **variable locale** est déclarée dans une fonction ou une procédure et n'est visible que par elle ; une **variable globale** est visible dans tout le programme. Trois exemples font prévoir l'affichage : modifier un paramètre n'affecte pas l'argument ([[Passage de paramètres]]), modifier une globale si. L'examen de novembre 2022 porte sur la portée ([[AlgoID1 (résumé)]], [[Contrôles (résumé)]]).

Notion parente : [[Fonction et procédure]].

Liens : [[Transtypage]]

Résumés : [[Chp1 - Intro Java (résumé)]], [[AlgoID1 (résumé)]], [[Contrôles (résumé)]]
