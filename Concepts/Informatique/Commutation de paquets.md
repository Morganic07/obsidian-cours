---
type: concept
tags: [year4]
aliases: [packet switching, réseau à commutation de paquets]
sources: ["[[Raw/Year 4/histoire du design et interactions /chp2 cours.pdf|chp2 cours.pdf]]"]
maj: 2026-11-10
---

**Définition** (d'après [[2 - Histoire du design]]) : technique qui découpe les données en morceaux (des paquets) envoyés par des chemins multiples, de sorte qu'un réseau reste fonctionnel même si une partie est détruite. C'est l'« innovation majeure » d'[[ARPANET]], premier réseau à l'utiliser.

Fonctionnement (complément, hors du cours) : chaque paquet porte un en-tête avec l'adresse de destination ; les nœuds du réseau (aujourd'hui les [[Routeur|routeurs]]) le font suivre de proche en proche selon leur table de routage ([[Routage IP]]), et la machine destinataire remet les paquets dans l'ordre. Elle s'oppose à la **commutation de circuits** du téléphone classique, qui réserve une ligne de bout en bout pendant toute la communication, même dans les silences. Les liens sont ainsi partagés entre de nombreux échanges, ce qui convient au trafic informatique, fait de rafales courtes. L'idée a deux origines indépendantes : Paul Baran (RAND Corporation, 1960-1964), qui cherchait un réseau de télécommunication capable de survivre à une attaque nucléaire, et Donald Davies (laboratoire national de physique britannique, 1965), qui invente le mot *packet* ; Leonard Kleinrock en a étudié la théorie (files d'attente). [[Complément hors du cours|ⓘ]]

## Dans le cours

[[1 - Histoire du design]] : nommée dans le résumé des réseaux en fin de fiche, avec ARPANET ; le [[Réseau décentralisé|réseau décentralisé]] y est défini parmi les concepts essentiels.

[[2 - Histoire du design]] : fiche ARPANET (page 2). La survie à une destruction partielle motivait les travaux de Baran, mais ARPANET a été financé pour partager des ressources de calcul entre centres de recherche (voir [[Réseau décentralisé]]).

Voir aussi : [[ARPANET]], [[Suite des protocoles Internet]], [[Routage IP]], [[Modèle OSI]].

Résumés : [[1 - Histoire du design]] · [[2 - Histoire du design]]
