---
type: concept
tags: [year2]
aliases: [swap, swap area, swap partition, partition swap, swap space, espace d'échange, swapfile, swap file, fichier d'échange]
matieres: [Operating System]
sources: ["[[3 - OS|OS - chp 3]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]", "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"]
maj: 2026-11-08
---

Espace du disque que Linux utilise quand la RAM est pleine : une mémoire virtuelle qui étend la [[Mémoire vive]], mais plus lente, donc pas utilisée pour les données souvent consultées. C'est une partition nécessaire à l'installation d'Ubuntu. `free -h` affiche la RAM et le swap.

**Compléments (hors du cours)** :

- **Fichier plutôt que partition** : le swap peut être un simple fichier du système de fichiers. Depuis la version 17.04, [[Ubuntu]] crée par défaut un fichier d'échange (`/swapfile`, ou `/swap.img` selon l'installeur) au lieu d'une partition : il est plus simple à créer, agrandir ou supprimer, sans repartitionner le disque.
- **Hibernation** : mettre la machine en veille prolongée recopie le contenu de la RAM dans le swap avant l'arrêt, puis le relit au redémarrage ; le swap doit alors être au moins aussi grand que la RAM occupée.
- `swapon --show` liste les espaces d'échange actifs (partition ou fichier, taille, quantité utilisée).
- Le mécanisme général qui permet de placer une partie de la mémoire d'un processus sur le disque est la [[Mémoire virtuelle]].

Notion parente : [[Partitions Linux]]. Voir aussi : [[Commande free]], [[Mémoire virtuelle]].

Résumés : [[3 - OS]], [[4 - OS]]
