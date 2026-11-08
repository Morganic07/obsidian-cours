---
type: concept
tags: [year2]
aliases: [DMA, Direct Memory Access, contrôleur DMA, cycle stealing]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition** (d'après [[1 - OS]]) : DMA = *Direct Memory Access* : mécanisme qui permet d'accéder à la RAM sans interrompre le CPU (schéma « Working of an I/O operation »).

## Mécanisme (complément, hors du cours)

Sans DMA, pour un gros transfert (lire un fichier de plusieurs mégaoctets), le CPU devrait copier lui-même chaque mot du buffer du [[Contrôleur de périphérique|contrôleur]] vers la RAM, et recevoir une [[Interruption]] à chaque petit morceau : il passerait son temps à déplacer des données.

Avec DMA :
1. le CPU programme le **contrôleur DMA** : adresse de départ en RAM, nombre d'octets à transférer, sens du transfert (lecture ou écriture) ;
2. le transfert du bloc entier se fait directement entre le buffer du périphérique et la RAM, par le [[Bus système]], pendant que le CPU fait autre chose ;
3. une **seule interruption** signale la fin du bloc, au lieu d'une par mot.

Le CPU et le contrôleur DMA se partagent le bus : quand le contrôleur l'utilise, le CPU peut être brièvement ralenti dans ses propres accès à la RAM (*cycle stealing*, « vol de cycles »). Il continue néanmoins de travailler, en particulier sur les données déjà présentes dans ses [[Mémoire cache|caches]].

## Dans le cours

Le cours nomme le DMA sur le schéma d'une opération d'entrée-sortie ; le déroulé du transfert est un complément de [[1 - OS]].

Notion parente : [[Opération d'entrée-sortie]]. Voir aussi : [[Mémoire vive]], [[Interruption]], [[Contrôleur de périphérique]], [[Bus système]].

Résumés : [[1 - OS]]
