---
type: concept
tags: [year2]
aliases: [container, conteneur Docker, conteneurisation, containerization]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un conteneur isole une application, avec ses bibliothèques et ses dépendances, dans un environnement à part sur le même système.

- À la différence d'une [[Machine virtuelle|machine virtuelle]], il n'embarque pas son propre OS : il **partage le [[Noyau|noyau]] de l'hôte**. Sous Linux, l'isolement repose sur deux mécanismes du noyau : les [[Espace de noms (namespace)|espaces de noms]] (*namespaces*), qui donnent au conteneur sa propre vue des processus, du réseau et des fichiers, et les *cgroups*, qui limitent ses ressources (CPU, mémoire).
- Avantages : démarrage en quelques secondes, faible encombrement, même comportement d'une machine à l'autre (l'image du conteneur contient tout ce dont l'application a besoin).
- Limite : il ne fait tourner qu'un système compatible avec le noyau hôte (des conteneurs Linux sur un noyau Linux) ; l'isolement est aussi moins fort que celui d'une VM, puisque le noyau est commun.
- Exemple d'outil : Docker ; les conteneurs sont très utilisés en [[Cloud computing]].

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[1 - OS]], comme alternative plus légère à la machine virtuelle.

Voir aussi : [[Machine virtuelle]], [[Noyau]], [[Espace de noms (namespace)]], [[Cloud computing]].

Résumés : [[1 - OS]]
