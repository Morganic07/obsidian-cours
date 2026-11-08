---
type: concept
tags: [year4]
aliases: [Eulerian graph, cycle eulérien, chaîne eulérienne, Eulerian cycle, Eulerian path, ponts de Königsberg]
sources: ["[[Raw/Year 4/graph theory/Chp 1 - Undirected graph.docx|Chp 1 - Undirected graph]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une **chaîne eulérienne** est une [[Chaîne (graphe)|chaîne]] qui passe exactement une fois par chaque arête du graphe ; un **cycle eulérien** est une chaîne eulérienne fermée (elle revient à son point de départ). Un graphe qui possède un cycle eulérien est dit **eulérien**.

**Théorème d'Euler** (1736, preuve complète par Hierholzer en 1873) : soit $G$ un graphe non orienté [[Graphe connexe|connexe]] ayant au moins une arête.

- $G$ est eulérien si et seulement si tous ses sommets sont de [[Degré d'un sommet|degré]] pair ;
- $G$ possède une chaîne eulérienne non fermée si et seulement s'il a exactement deux sommets de degré impair ; ces deux sommets sont alors les extrémités de la chaîne.

Idée de la condition nécessaire : chaque passage par un sommet intermédiaire utilise une arête pour entrer et une pour sortir, donc consomme 2 dans son degré. Le cas « exactement un sommet de degré impair » est impossible, d'après le [[Lemme des poignées de main]].

**Graphe orienté** : un graphe orienté fortement connexe possède un circuit eulérien si et seulement si $d^+(v) = d^-(v)$ pour tout sommet $v$.

**Les sept ponts de Königsberg** : la ville (aujourd'hui Kaliningrad) avait quatre quartiers reliés par sept ponts ; peut-on se promener en traversant chaque pont une seule fois ? En modélisant les quartiers par des sommets et les ponts par des arêtes (un multigraphe), on obtient quatre sommets de degrés 3, 3, 3 et 5 : quatre sommets de degré impair, donc ni cycle ni chaîne eulérienne. L'article d'Euler sur ce problème est considéré comme l'acte de naissance de la théorie des graphes.

Exemple courant : dessiner une figure « sans lever le crayon et sans repasser sur un trait » revient à chercher une chaîne eulérienne.

**À ne pas confondre** avec un graphe **hamiltonien**, qui possède un [[Cycle (graphe)|cycle]] passant exactement une fois par chaque *sommet*. Autant le caractère eulérien se teste en temps linéaire par un simple calcul de degrés, autant décider si un graphe est hamiltonien est un problème NP-complet ; le [[Problème du voyageur de commerce]] en est la version pondérée.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[1 - Undirected graph]], à partir des notions de degré et de chaîne.

Voir aussi : [[Degré d'un sommet]], [[Lemme des poignées de main]], [[Cycle (graphe)]], [[Chaîne (graphe)]], [[Graphe connexe]], [[Graphe non orienté]].

Résumés : [[1 - Undirected graph]]
