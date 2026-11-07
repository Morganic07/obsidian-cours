---
type: concept
tags: [year3]
aliases: [Open Shortest Path First]
matieres: [Computer Network]
sources: ["[[3 - Dynamic Routing|Chp3 - Dynamic Routing]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : OSPF (Open Shortest Path First) est un protocole de [[Routage dynamique|routage dynamique]] à état de liens, utilisé à l'intérieur d'un [[Système autonome|système autonome]]. Chaque routeur diffuse l'état de ses liens à tous les autres, si bien que tous construisent la même carte du réseau ; chacun calcule ensuite les plus courts chemins avec l'algorithme de Dijkstra, selon un coût lié à la bande passante des liens. Il converge vite, gère le [[VLSM]] et découpe les grands réseaux en zones (*areas*).

## Dans le cours

Nommé dans le cours sans définition : OSPF y est cité comme exemple d'IGP, utilisé à l'intérieur d'un [[Système autonome]]. Le chapitre ne le détaille pas.

Notion parente : [[Routage dynamique]]. Voir aussi : [[EIGRP]].

Résumés : [[3 - Dynamic Routing]]
