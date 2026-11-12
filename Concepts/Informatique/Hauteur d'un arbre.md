---
type: concept
tags: [year2, year4]
aliases: [hauteur d'un nœud, profondeur d'un nœud, niveau d'un nœud]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]", "[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]", "[[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]", "[[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]]"]
maj: 2026-11-12
---

Profondeur maximale des nœuds, autrement dit longueur maximale d'une branche en nombre d'arêtes. Dans les chapitres 3 et 4, elle vaut 0 pour un arbre à un seul nœud et $-1$ pour l'arbre vide.

En récursif : $h=1+\max(h_g,h_d)$. Pour un arbre binaire à $n$ nœuds : $h+1 \le n \le 2^{h+1}-1$.

Notion parente : [[Vocabulaire des arbres]]. Voir aussi : [[Arbre binaire]], [[Arbre AVL]], [[Arbre équilibré]], [[Arbre dégénéré]].

## Hauteur et taille d'un arbre k-aire (graph theory)

Dans [[2 - tree revisions années précédentes]], la profondeur d'un nœud est la distance (nombre d'arcs) de la racine au nœud, et la hauteur la profondeur maximale. Pour un [[Arbre m-aire|arbre k-aire]] ($k \ge 2$) de taille $n \ge 1$ :
- pire cas (hauteur la plus grande, arbre [[Arbre dégénéré|dégénéré]]) : $h = n - 1$ ;
- meilleur cas (chaque niveau rempli avant le suivant) : $h = \lceil \log_k((k-1)n + 1) \rceil - 1$, soit $\lfloor \log_2 n \rfloor$ pour un arbre binaire.

La borne du meilleur cas vient de ce qu'un arbre de hauteur $h$ a au plus $1 + k + \dots + k^h = \frac{k^{h+1}-1}{k-1}$ nœuds (voir [[Suite géométrique]] et [[Logarithme]]) ; la formule a été refaite dans la fiche, qui la corrige.

## Conventions selon les sources

Les sources ne prennent pas la même convention :

- ARBRE AVL ([[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]) pose $h(\text{NIL})=0$ (« 1 pour une feuille ; 0 si NIL »), alors que Chapitre3-Arbres ([[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]) donne 0 pour un arbre à un seul nœud et $-1$ pour l'arbre vide, et que Chapitre4-Preing2ID ([[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]) la définit comme la longueur maximale d'une branche en arêtes ;
- le code de [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]] et de [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]] compte 0 pour un sous-arbre absent (une feuille vaut 1), alors que leur texte annonce $-1$ ;
- [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]] définit la hauteur d'un nœud comme le nombre de branches qui le séparent de la racine, ce qui correspond à la profondeur.

Résumés : [[3 - Arbres]], [[4 - Arbres binaires]], [[6 - AVL]], [[2 - tree revisions années précédentes]]
