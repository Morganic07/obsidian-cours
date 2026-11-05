---
type: concept
aliases: [IOS, Cisco IOS, modes de la CLI, mode privilégié, mode utilisateur, configuration globale, running-config, startup-config, Packet Tracer]
matieres: [Computer Network]
sources: ["[[chp1 - Computer Networks]]", "[[Formation CISCO Packet Tracer]]"]
maj: 2026-11-05
---

IOS est le système d'exploitation des routeurs (2911) et des switchs (2960) Cisco, piloté en ligne de commande (CLI).

**Trois modes**
- Utilisateur : invite `>`, commandes très limitées comme `show`.
- Privilégié : invite `#`, atteint par `enable`. Permet aussi de sauvegarder, effacer, redémarrer.
- Configuration globale : invite `(config)#`, atteinte par `configure terminal` depuis le mode privilégié. On ne saute pas du mode utilisateur à la configuration globale. `exit` remonte d'un niveau.

**Deux mémoires**
- `running-config` : en RAM, perdue au redémarrage, c'est là qu'on configure. `show running-config`.
- `startup-config` : chargée au démarrage. `write memory` y copie la configuration courante, `show startup-config` l'affiche.

Une interface `FastEthernet0/1` se lit slot/port. Les interfaces d'un routeur sont désactivées par défaut : `no shutdown` les active.

Liens : [[Routage statique]], [[VLAN]]

Résumés : [[chp1 - Computer Networks (résumé)]], [[Formation CISCO Packet Tracer (résumé)]]
