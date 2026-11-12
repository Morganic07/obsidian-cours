---
type: concept
tags: [year3, year4]
aliases: [Dijkstra, Dijkstra's algorithm, Dijkstra algorithm, SPF, Shortest Path First]
sources: ["[[Raw/Year 3/Computer Network/Chp3 : Dynamic Routing.docx|Chp3 - Dynamic Routing]]", "[[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]]", "[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - dijkstra]]) : algorithme qui résout le problème du [[Plus court chemin|plus court chemin]] sur un graphe orienté ou non, valué positivement : à partir d'un sommet d'origine, il construit progressivement un sous-graphe, une arborescence qui donne le plus court chemin de l'origine à chaque autre sommet, en stockant pour chaque sommet sa distance (poids cumulé) et son parent. À chaque étape, il traite le sommet de poids le plus faible pas encore traité.

**Compléments (hors du cours)** : algorithme de calcul des plus courts chemins depuis une source $s$ dans un [[Graphe pondéré|graphe pondéré]] dont tous les poids sont positifs ou nuls, conçu par Edsger W. Dijkstra en 1956 et publié en 1959.

**Principe** : on pose $d(s) = 0$ et $d(v) = +\infty$ pour les autres sommets. À chaque étape, on choisit parmi les sommets non encore traités celui, $u$, de plus petite distance provisoire ; sa distance est alors définitive. On relâche ensuite ses arêtes sortantes :
$$d(v) \leftarrow \min\big(d(v),\ d(u) + w(u,v)\big),$$
en notant $u$ comme prédécesseur de $v$ quand la distance baisse. On s'arrête quand tous les sommets accessibles sont traités. Les prédécesseurs forment un arbre des plus courts chemins enraciné en $s$.

C'est un [[Algorithme glouton|algorithme glouton]] : le choix du sommet le plus proche n'est jamais remis en cause, ce qui n'est juste que si aucun poids n'est négatif (un arc négatif découvert plus tard pourrait raccourcir un chemin déjà fixé).

**Complexité** : $O(|V|^2)$ avec un simple tableau des distances (adapté aux graphes denses) ; $O\big((|V| + |E|)\log|V|\big)$ avec un tas binaire (file de priorité).

**Poids négatifs** : il ne fonctionne pas ; utiliser l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]], plus lent ($O(|V| \cdot |E|)$). Sans poids (ou à poids tous égaux), un parcours en largeur suffit.

**En réseau** : dans un protocole à état de liens ([[OSPF]], IS-IS), chaque routeur reçoit l'état des liens de tous les routeurs de sa zone, donc la carte complète ; il lance Dijkstra (appelé SPF, *Shortest Path First*) en se prenant pour source, avec le coût des liens comme poids, et remplit sa table de routage à partir de l'arbre obtenu.

## Dans le cours

Computer Network et le chapitre 4 de Graph theory ne le nomment pas. Il apparaît dans les compléments de [[3 - Dynamic Routing]] (calcul de l'arbre des plus courts chemins par chaque routeur à état de liens) et, en une phrase, dans [[4 - oriented graphs]] de Graph theory : le parcours en largeur donne les plus courts chemins en nombre d'arcs, mais pour des arcs pondérés positifs il faut Dijkstra. Le chapitre lui-même ne le présente pas.

Les suppléments du chapitre 4 de Graph theory le détaillent : [[4 - dijkstra]] (diaporama CY Tech) donne le principe, un exemple déroulé en tables étape par étape jusqu'à l'arborescence finale, et deux exercices ; [[4 - bellman ford]] le situe dans le tableau des cas (arcs de poids positifs, source unique) et l'oppose à Bellman-Ford pour le routage (fonctionnement global contre local).

Voir aussi : [[Algorithme de Bellman-Ford]], [[Algorithme A étoile]], [[Arbre des plus courts chemins]], [[Relâchement d'un arc]], [[Routage à état de liens]], [[OSPF]], [[Routage dynamique]], [[Graphe pondéré]], [[Chemin (graphe)]], [[Algorithme glouton]], [[Arbre couvrant minimal]], [[ARMAC]].

Résumés : [[3 - Dynamic Routing]], [[4 - oriented graphs]], [[4 - dijkstra]], [[4 - bellman ford]]
