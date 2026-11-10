---
type: concept
tags: [year4]
aliases: [orchestrateur, orchestrateur de conteneurs, Docker Swarm, container orchestration]
sources: ["[[Raw/Year 4/SHS/Prise de note SHS.docx|Prise de note SHS.docx]]"]
maj: 2026-11-10
---

**Définition (complément, hors du cours)** : l'orchestration de conteneurs est la gestion automatisée d'un grand nombre de [[Conteneur (informatique)|conteneurs]] répartis sur plusieurs machines : placement sur les serveurs, redémarrage en cas de panne, mise à l'échelle selon la charge, réseau et mises à jour progressives. Un conteneur isolé se lance à la main ; des milliers de conteneurs, en production, demandent un orchestrateur. Les principaux ont été [[Kubernetes]] (Google, 2014), Docker Swarm (outil de Docker, intégré au moteur Docker en 2016) et Apache Mesos ; Kubernetes s'est imposé, au point que Docker l'a lui-même intégré à ses produits en 2017.

## Dans le cours

Dans [[6 - design libre]], un groupe d'étudiants raconte que Docker a sorti son propre orchestrateur, Docker Swarm, sous [[Licence Apache|licence Apache 2.0]], puis que Kubernetes, construit par Google, l'a délogé du marché. Le groupe en tire que la valeur d'un commun peu protégé est captée par ceux qui contrôlent l'infrastructure.

Voir aussi : [[Conteneur (informatique)]], [[Kubernetes]], [[Cloud computing]].

Résumés : [[6 - design libre]]
