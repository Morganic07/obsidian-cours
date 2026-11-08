---
type: concept
tags: [year4]
aliases: [classe P, classe NP, P vs NP, P = NP, NP-complet, NP-complete, NP-difficile, NP-hard]
sources: ["[[Raw/Year 4/graph theory/chp3 - complexité .docx|chp3 - complexité]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : les classes P et NP sont des classes de complexité de la théorie de la complexité. Elles portent sur des **problèmes de décision** (dont la réponse est oui ou non), et non sur des algorithmes.

- **P** : problèmes résolus par un algorithme en temps polynomial, $O(n^k)$ pour un $k$ fixé, où $n$ est la taille de l'entrée.
- **NP** : problèmes dont une solution proposée (un **certificat**) se **vérifie** en temps polynomial. Tout problème de P est dans NP (on peut le résoudre, donc vérifier, en temps polynomial) : $P \subseteq NP$.
- **NP-complet** : problème qui est dans NP et auquel **tout** problème de NP se ramène par une réduction en temps polynomial. Un algorithme polynomial pour un seul problème NP-complet en donnerait un pour tout NP.
- **NP-difficile** : problème qui vérifie seulement la seconde condition (tout problème de NP s'y ramène), sans être forcément dans NP ; c'est le cas, par exemple, des versions d'optimisation des problèmes NP-complets.

Savoir si $P = NP$ est un problème ouvert : c'est l'un des sept **problèmes du millénaire** posés par le Clay Mathematics Institute en 2000.

Exemples de problèmes NP-complets, dans leur version de décision : le [[Problème du voyageur de commerce]] (existe-t-il une tournée de longueur au plus $L$ ?) et le [[Problème du sac à dos]] (peut-on atteindre une valeur au moins $V$ sans dépasser la capacité ?). On ne leur connaît aucun algorithme polynomial.

À distinguer des ordres de grandeur d'un algorithme (constant, linéaire, quadratique, exponentiel…) décrits dans [[Classe de complexité]].

## Dans le cours

Le cours ne les nomme pas. Elles apparaissent dans les compléments de [[3 - complexité]], à propos de la frontière entre algorithmes polynomiaux, jugés praticables, et exponentiels.

Voir aussi : [[Complexité algorithmique]], [[Classe de complexité]], [[Problème du voyageur de commerce]], [[Problème du sac à dos]].

Résumés : [[3 - complexité]]
