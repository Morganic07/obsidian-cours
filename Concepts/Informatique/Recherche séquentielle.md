---
type: concept
tags: [year4]
aliases: [sequential search]
sources: ["[[3 - complexité|chp3 - complexité]]"]
maj: 2026-11-12
---

Recherche d'un élément en parcourant le tableau élément par élément. Complexité : $O(n)$ au pire cas, $O(1)$ au meilleur, et $\frac{n+1}{2}$ comparaisons en moyenne.

Notion parente : [[Complexité algorithmique]]. Voir aussi : [[Recherche dichotomique]].

## Dans le cours

- [[tp7]] : la [[Recherche du minimum et du maximum|recherche du minimum et du maximum]] d'un tableau (7.2) se fait en un seul parcours séquentiel.
- [[td listes chaînées]] : `rechercherElement` parcourt la [[Liste chaînée|liste]] et renvoie l'adresse du premier chaînon portant la valeur, ou `NULL` si elle est absente, en $O(n)$.

Résumés : [[3 - complexité]]
