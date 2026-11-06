---
type: concept
tags: [year2]
aliases: [hauteur d'un nœud, profondeur d'un nœud, niveau d'un nœud]
sources: ["[[raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres]]", "[[raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID]]", "[[raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL]]", "[[AVL momo]]", "[[qui dit quoi AVL]]"]
maj: 2026-11-06
---

Profondeur maximale des nœuds, autrement dit longueur maximale d'une branche en nombre d'arêtes. Dans les chapitres 3 et 4, elle vaut 0 pour un arbre à un seul nœud et $-1$ pour l'arbre vide.

En récursif : $h=1+\max(h_g,h_d)$. Pour un arbre binaire à $n$ nœuds : $h+1 \le n \le 2^{h+1}-1$.

Notion parente : [[Vocabulaire des arbres]]. Voir aussi : [[Arbre binaire]], [[Arbre AVL]].

## À vérifier

Désaccord de convention entre les sources :

- [[raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL]] pose $h(\text{NIL})=0$ (une feuille a donc une hauteur de 1), alors que [[raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres]] et [[raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID]] donnent $-1$ pour l'arbre vide ;
- le code de [[AVL momo]] et de [[qui dit quoi AVL]] renvoie 0 pour l'arbre vide ;
- [[qui dit quoi AVL]] définit la hauteur comme la distance à la racine, ce qui correspond à la profondeur.

Résumés : [[Chapitre3-Arbres (résumé)]], [[Chapitre4-Preing2ID (résumé)]], [[ARBRE AVL (résumé)]], [[AVL momo (résumé)]], [[qui dit quoi AVL (résumé)]]
