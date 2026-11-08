---
type: concept
tags: [year4]
aliases: [planar graph, formule d'Euler, théorème de Kuratowski, théorème des quatre couleurs, four color theorem]
sources: ["[[1 - Undirected graph|Chp 1 - Undirected graph]]"]
maj: 2026-11-08
---

Graphe que l'on peut dessiner sans croisement d'arêtes. Tout [[Sous-graphe|sous-graphe]] et tout graphe [[Isomorphisme de graphes|isomorphe]] d'un graphe planaire sont planaires.

## Compléments (hors du cours)

**Faces** : un dessin planaire découpe le plan en régions appelées faces, dont une seule, la face extérieure, est non bornée.

**Formule d'Euler** : pour un graphe planaire [[Graphe connexe|connexe]] dessiné sans croisement, avec $n$ sommets, $m$ arêtes et $f$ faces (face extérieure comprise) :

$$n - m + f = 2$$

Exemple : le cube a 8 sommets, 12 arêtes et 6 faces, $8 - 12 + 6 = 2$ ; un arbre a $n - 1$ arêtes et une seule face, $n - (n-1) + 1 = 2$.

**Corollaire** : un [[Graphe simple|graphe simple]] planaire à $n \ge 3$ sommets a au plus $3n - 6$ arêtes (chaque face est bordée par au moins 3 arêtes et chaque arête borde au plus 2 faces, donc $3f \le 2m$). S'il n'a aucun triangle, la borne devient $m \le 2n - 4$. Un graphe planaire est donc toujours creux.

**Deux graphes non planaires** :

- $K_5$, le [[Graphe complet|graphe complet]] à 5 sommets : $10$ arêtes, alors que $3 \times 5 - 6 = 9$ ;
- $K_{3,3}$, le [[Graphe biparti|graphe biparti]] complet à 3 + 3 sommets (problème des trois maisons à relier chacune à trois usines, eau, gaz, électricité, sans croisement) : sans triangle, $9$ arêtes alors que $2 \times 6 - 4 = 8$.

**Théorème de Kuratowski** (1930) : un graphe est planaire si et seulement s'il ne contient aucun sous-graphe qui soit une subdivision de $K_5$ ou de $K_{3,3}$ (une subdivision remplace des arêtes par des chaînes).

**Théorème des quatre couleurs** (Appel et Haken, 1976) : les sommets de tout graphe planaire peuvent être coloriés avec au plus quatre couleurs de sorte que deux sommets adjacents aient des couleurs différentes ; de façon équivalente, toute carte géographique se colorie avec quatre couleurs sans que deux pays voisins partagent la même. C'est le premier grand théorème dont la preuve repose sur une vérification par ordinateur d'un grand nombre de cas.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Sous-graphe]], [[Isomorphisme de graphes]], [[Graphe complet]], [[Graphe biparti]], [[Graphe connexe]], [[Graphe simple]].

Résumés : [[1 - Undirected graph]]
