---
type: concept
tags: [year2]
aliases: [cache du CPU, CPU cache, cache L1, cache L2, cache L3, cache hit, cache miss, ligne de cache, cache line, principe de localité]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition** (d'après [[1 - OS]]) : mémoire très rapide située dans le CPU, qui stocke les données et instructions souvent utilisées. Avant de faire appel à la RAM, le CPU vérifie ses caches : si la donnée y est, il n'a pas besoin d'aller la chercher en RAM.

## Complément (hors du cours)

**Niveaux de cache.** Le cache est organisé en plusieurs niveaux, du plus petit et plus rapide au plus grand et plus lent :
- **L1** : propre à chaque [[Cœur de processeur|cœur]], quelques dizaines de kilo-octets, souvent séparé en cache d'instructions (L1i) et cache de données (L1d) ;
- **L2** : plus grand (de l'ordre de quelques centaines de kilo-octets à quelques mégaoctets), généralement propre à chaque cœur ;
- **L3** : le plus grand (plusieurs mégaoctets), partagé entre les cœurs.

Le CPU cherche d'abord en L1, puis en L2, puis en L3, et ne va en RAM qu'en dernier recours.

**Hit et miss.** Trouver la donnée dans le cache s'appelle un *cache hit* ; ne pas la trouver, un *cache miss*, qui oblige à aller la chercher au niveau suivant, beaucoup plus lent. La part des accès servis par le cache (taux de succès, *hit rate*) détermine le gain : avec un temps d'accès au cache $t_c$, à la mémoire $t_m$ et un taux de succès $h$, le temps d'accès moyen vaut
$$t_{\text{moyen}} = h \, t_c + (1 - h)\,(t_c + t_m) = t_c + (1 - h)\, t_m.$$

**Principe de localité.** Le cache est efficace parce que les programmes ne visitent pas la mémoire au hasard :
- **localité temporelle** : une donnée utilisée a de fortes chances d'être réutilisée bientôt (variable de boucle, instructions d'une boucle) ;
- **localité spatiale** : les adresses voisines d'une donnée utilisée ont de fortes chances d'être utilisées aussi (cases suivantes d'un tableau, instructions consécutives).

C'est pourquoi le cache ne charge pas des octets isolés mais des blocs entiers, les **lignes de cache** (*cache lines*, souvent 64 octets) : lire une case d'un tableau amène aussi ses voisines.

**Technologie.** Le cache est fait de **SRAM** (*Static RAM*), rapide mais chère et encombrante, alors que la [[Mémoire vive]] principale est en DRAM.

## Dans le cours

Le cours présente le cache du CPU dans la [[Hiérarchie de stockage]] : vitesse SSD ≪ vitesse RAM ≪ vitesse caches. Les niveaux, la localité et la SRAM sont des compléments de [[1 - OS]].

Notion parente : [[Hiérarchie de stockage]]. Voir aussi : [[Processeur]], [[Mémoire vive]], [[Registre du processeur]], [[Cœur de processeur]], [[Cycle mémoire]].

Résumés : [[1 - OS]]
