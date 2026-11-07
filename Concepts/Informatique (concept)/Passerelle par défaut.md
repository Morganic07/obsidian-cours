---
type: concept
tags: [year3]
aliases: [default gateway, gateway of last resort]
sources: ["[[4 - VLAN ／ IVR Commands (résumé)|Chp4 - VLAN ／ IVR Commands]]", "[[2 - Static Routing (résumé)|Chp2 - Static Routing]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : la passerelle par défaut (*default gateway*) d'un hôte est l'adresse IP du [[Routeur|routeur]] de son réseau local auquel il envoie tous les paquets destinés à un autre réseau ; elle doit appartenir au même sous-réseau que l'hôte. Sur un routeur, la notion correspondante est la route par défaut (`0.0.0.0/0`), utilisée quand aucune route plus précise ne correspond à la destination ; Cisco IOS l'appelle *gateway of last resort*.

## Dans le cours

Nommée dans le cours sans définition propre :

- dans le routage inter-VLAN, l'adresse IP de la [[Sous-interface]] d'un VLAN est annotée « this is default gateway IP » : elle sert de passerelle aux hôtes du VLAN ;
- la sortie de `show ip route` affiche « Gateway of last resort is not set » en l'absence de route par défaut.

Voir aussi : [[Routage statique]].

Résumés : [[4 - VLAN ／ IVR Commands (résumé)]], [[2 - Static Routing (résumé)]]
