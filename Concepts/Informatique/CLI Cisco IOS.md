---
type: concept
tags:
  - year3
aliases:
  - IOS
  - Cisco IOS
  - modes de la CLI
  - mode privilégié
  - mode utilisateur
  - configuration globale
  - running-config
  - startup-config
  - Packet Tracer
  - show running-config
  - write memory
  - show startup-config
  - configure terminal
  - Internetwork Operating System
  - NVRAM
  - show ip interface brief
  - copy running-config startup-config
  - erase startup-config
matieres:
  - Computer Network
sources:
  - "[[1 - Computer Networks|chp1 - Computer Networks]]"
  - "[[7 - Cisco|Formation CISCO Packet Tracer]]"
  - "[[Raw/Year 3/Computer Network/chp1 : Computer Networks.docx|chp1 - Computer Networks]]"
  - "[[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]]"
maj: 2026-11-08
---

**Définition** (d'après [[1 - Computer Networks]]) : IOS est le système d'exploitation des routeurs (2911) et des switchs (2960) Cisco, piloté en ligne de commande (CLI).

**Trois modes**
- Utilisateur : invite `>`, commandes très limitées comme `show`.
- Privilégié : invite `#`, atteint par `enable`. Permet aussi de sauvegarder, effacer, redémarrer.
- Configuration globale : invite `(config)#`, atteinte par `configure terminal` depuis le mode privilégié. On ne saute pas du mode utilisateur à la configuration globale. `exit` remonte d'un niveau.

**Deux mémoires**
- `running-config` : en RAM, perdue au redémarrage, c'est là qu'on configure. `show running-config`.
- `startup-config` : chargée au démarrage. `write memory` y copie la configuration courante, `show startup-config` l'affiche.

Une [[Interface réseau|interface]] `FastEthernet0/1` se lit slot/port. Les interfaces d'un routeur sont désactivées par défaut : `no shutdown` les active.

## Compléments (hors du cours)

**Nom et mémoires** : IOS signifie *Internetwork Operating System*. Un équipement Cisco a quatre mémoires :

| Mémoire | Contenu | Volatile |
|---|---|---|
| ROM | programme de démarrage (bootstrap, test POST) | non |
| Flash | image du système IOS | non |
| NVRAM | `startup-config` | non |
| RAM | `running-config`, tables de routage et ARP | oui |

- `copy running-config startup-config` équivaut à `write memory` (abrégé `wr`).
- Retour à la configuration d'usine : `erase startup-config` puis `reload` (redémarrage sans configuration enregistrée).

**Sous-modes de configuration**, atteints depuis `(config)#` :

| Commande | Invite |
|---|---|
| `interface g0/0` | `(config-if)#` |
| `line console 0`, `line vty 0 4` | `(config-line)#` |
| `router ospf 1` | `(config-router)#` |
| `vlan 10` | `(config-vlan)#` |

`exit` remonte d'un niveau ; `end` ou Ctrl+Z revient directement au mode privilégié. `do show …` exécute un `show` sans quitter la configuration (`do show ip interface brief`).

**Aides à la saisie**
- `?` : aide contextuelle (commandes possibles, ou suite d'une commande : `show ?`).
- Tab : complète le mot commencé.
- Abréviations acceptées tant qu'elles ne sont pas ambiguës : `conf t`, `sh run`, `g0/1`.
- Préfixe `no` : annule une commande (`no shutdown`, `no ip route …`).

**Configuration de base d'un équipement**

```
enable
configure terminal
hostname R1
enable secret <mot de passe>          ! mot de passe du mode privilégié, stocké haché
interface g0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
end
copy running-config startup-config
```

**Vérifier les interfaces** : `show ip interface brief` donne pour chaque interface son adresse et deux états, *Status* (couche physique) et *Protocol* (couche liaison). Une interface jamais activée affiche « administratively down » jusqu'au `no shutdown`. Les préfixes de nom indiquent le débit : `Fa` (FastEthernet) = 100 Mbit/s, `Gi` (GigabitEthernet) = 1 Gbit/s.

**Packet Tracer** : simulateur de réseaux de la Cisco Networking Academy. En mode *Realtime* le réseau fonctionne normalement ; en mode *Simulation*, on suit les paquets pas à pas et on inspecte leur contenu couche par couche.

Liens : [[Routage statique]], [[VLAN]], [[Interface réseau]], [[Commande ping]]

Résumés : [[1 - Computer Networks]], [[7 - Cisco]]
