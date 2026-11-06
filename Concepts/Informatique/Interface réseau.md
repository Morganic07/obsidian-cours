---
type: concept
tags: [year2, year3]
aliases: [network interface, interfaces réseau, eth0, wlan0, interface Ethernet, "Interface d'un équipement réseau", FastEthernet, GigabitEthernet, interface gigabitEthernet, slot/port]
matieres: [Operating System, Computer Network]
sources: ["[[Cours TP3]]", "[[raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2)]]", "[[chp1 - Computer Networks]]", "[[Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-06
---

**Sous Linux** (Operating System) : `eth0` est une interface Ethernet (le numéro varie), `wlan0` une interface Wi-Fi, `lo` la boucle locale ([[Adresse de bouclage]]). Dans la sortie de [[Commande ifconfig|ifconfig]] : `inet` donne l'adresse IPv4, `netmask` le masque, `broadcast` l'adresse de diffusion, `inet6` l'adresse [[IPv6]], `RX`/`TX` les paquets reçus et envoyés, plus des drapeaux d'état. Le sujet montre une sortie à trois interfaces (eth0, wlan0, eth1).

**Sur un équipement Cisco** (Computer Network) : une interface se note par exemple `FastEthernet0/1`, où 0/1 signifie slot/port. On la sélectionne par `interface gigabitEthernet 0/1`, on lui donne une adresse avec `ip address <adresse> <masque>` et on l'active avec `no shutdown`, car les ports d'un [[Routeur]] sont désactivés par défaut.

Notion parente : [[CLI Cisco IOS]]. Voir aussi : [[Commande ip]], [[Netplan]], [[Sous-interface]].

## À vérifier

- La note [[chp1 - Computer Networks]] commente `interface gigabitEthernet 0/1` par « to enable the interface » : cette ligne sélectionne l'interface, c'est `no shutdown` qui l'active.

Résumés : [[Cours TP3 (résumé)]], [[TP3-Commands (2) (résumé)]], [[chp1 - Computer Networks (résumé)]], [[Chp4 - VLAN ／ IVR Commands (résumé)]]
