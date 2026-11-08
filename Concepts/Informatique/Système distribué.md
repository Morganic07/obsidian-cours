---
type: concept
tags: [year2]
aliases: [distributed systems, distributed system, systèmes distribués, Network Operating System, Top of Rack, ToR switch, pair-à-pair, peer-to-peer, P2P]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition** (d'après [[1 - OS]]) : ensemble de systèmes séparés, éventuellement hétérogènes, reliés en réseau. Le Network Operating System fournit des fonctions entre les systèmes du réseau et donne l'illusion d'un seul système. Le cours montre un schéma de réseau de centre de données (core, aggregate et ToR switches).

## Complément (hors du cours)

**Lecture du schéma du cours.** Le réseau du centre de données est un arbre sur trois niveaux de [[Commutateur|commutateurs]] :
- **ToR** (*Top of Rack*) : en haut de chaque baie, il relie les serveurs de cette baie ;
- **aggregate** (agrégation) : regroupe plusieurs commutateurs ToR ;
- **core** (cœur de réseau) : relie les commutateurs d'agrégation entre eux et à l'extérieur (Internet).

Les liens sont doublés entre niveaux : si un commutateur ou un câble tombe, le trafic passe par l'autre chemin (tolérance aux pannes).

**Intérêts d'un système distribué** :
- **partage des ressources** : fichiers, imprimantes, puissance de calcul d'une machine utilisables depuis une autre ;
- **calcul plus rapide** : un travail découpé en morceaux traités en parallèle sur plusieurs machines ;
- **fiabilité** : la panne d'une machine n'arrête pas l'ensemble, les autres prennent le relais ;
- **communication** : échange de messages et de données entre utilisateurs et programmes de sites différents.

**Organisation.** Le plus souvent, les machines suivent le [[Modèle client-serveur]] : des serveurs fournissent un service à des clients. Dans la variante **pair-à-pair** (*peer-to-peer*, P2P), chaque machine est à la fois client et serveur, sans serveur central ; exemple : BitTorrent, où chaque participant télécharge des morceaux d'un fichier et en envoie à son tour aux autres.

## Dans le cours

Le cours définit le système distribué et montre le schéma du centre de données sans le commenter ; la lecture du schéma, les intérêts et le pair-à-pair sont des compléments de [[1 - OS]].

Notion parente : [[Environnement informatique]]. Voir aussi : [[Modèle client-serveur]], [[Système en grappe (cluster)]], [[Commutateur]], [[Cloud computing]].

Résumés : [[1 - OS]]
