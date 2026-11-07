---
type: concept
tags: [year2]
aliases: [hauteur d'un nœud, profondeur d'un nœud, niveau d'un nœud]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]", "[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]", "[[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]", "[[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]]"]
maj: 2026-11-07
---

Profondeur maximale des nœuds, autrement dit longueur maximale d'une branche en nombre d'arêtes. Dans les chapitres 3 et 4, elle vaut 0 pour un arbre à un seul nœud et $-1$ pour l'arbre vide.

En récursif : $h=1+\max(h_g,h_d)$. Pour un arbre binaire à $n$ nœuds : $h+1 \le n \le 2^{h+1}-1$.

Notion parente : [[Vocabulaire des arbres]]. Voir aussi : [[Arbre binaire]], [[Arbre AVL]].

## Conventions selon les sources

Les sources ne prennent pas la même convention :

- ARBRE AVL ([[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]) pose $h(\text{NIL})=0$ (« 1 pour une feuille ; 0 si NIL »), alors que Chapitre3-Arbres ([[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]) donne 0 pour un arbre à un seul nœud et $-1$ pour l'arbre vide, et que Chapitre4-Preing2ID ([[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]) la définit comme la longueur maximale d'une branche en arêtes ;
- le code de [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]] et de [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]] compte 0 pour un sous-arbre absent (une feuille vaut 1), alors que leur texte annonce $-1$ ;
- [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]] définit la hauteur d'un nœud comme le nombre de branches qui le séparent de la racine, ce qui correspond à la profondeur.

Résumés : [[3 - Arbres]], [[4 - Arbres binaires]], [[6 - AVL]]
