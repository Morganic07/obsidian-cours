---
type: concept
aliases: [portée d'une variable, portée des variables, scope d'une variable, erreur de scope]
matieres: [Java]
sources: ["[[Chp1 - Intro Java]]"]
maj: 2026-11-05
---

La portée d'une variable est la région du code où l'on peut l'utiliser, en écriture comme en lecture. Les régions sont en général délimitées par des paires d'accolades `{ ... }`.

Dans une même portée, tous les noms de variables doivent être uniques.

**Erreur classique** : une variable déclarée dans le bloc d'un `do { ... }` n'existe plus en dehors de ce bloc, donc elle ne peut pas servir dans la condition `while (x < 10)` qui suit. Erreur de compilation.

Liens : [[Transtypage]]

Résumé : [[Chp1 - Intro Java (résumé)]]
