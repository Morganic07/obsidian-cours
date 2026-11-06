---
type: source
tags: [year3]
sources: ["[[chp1 - Computer Networks]]"]
maj: 2026-11-05
---

Résumé de [[chp1 - Computer Networks]], dans [[Computer Network (matière)]]. Notes personnelles, en français et en anglais mêlés, des deux premiers cours Cisco. En cas d'écart, le cours fait foi.

## Contenu, dans l'ordre du cours

- **Matériel** : routeurs 2911, commutateurs (switch) 2960. Système d'exploitation : IOS.
- **Trois modes de la ligne de commande** (voir [[CLI Cisco IOS]]) : utilisateur (`>`), privilégié (`#`, atteint par `enable`), configuration globale (`(config)#`, atteinte par `configure terminal`). On ne passe pas du mode utilisateur à la configuration globale sans passer par le mode privilégié. `exit` revient en arrière.
- **À quoi servent les modes** : le mode utilisateur permet des commandes très limitées comme `show`. Le mode privilégié permet aussi de sauvegarder, effacer, redémarrer. La configuration globale permet les commandes de configuration.
- **Deux mémoires** : `running-config` en RAM (perdue au redémarrage, c'est là qu'on configure), `startup-config` (chargée au démarrage). `show running-config`, `write memory`, `show startup-config`, en mode privilégié. Une interface `FastEthernet0/1` se lit slot/port.
- **Routage statique** (deuxième cours, voir [[Routage statique]]) : `ip route <réseau> <masque> <sortie>`. Configuration des interfaces : `interface gigabitEthernet 0/1`, `ip address ...`, `no shutdown`, `exit`, puis la même chose sur l'interface 0/2.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Cette note n'a aucune image.

1. **« Internetwork Operating System, je crois »** : l'étudiant doute. C'est bien le sens de IOS (complément).
2. **« Global Config permet toutes les commandes de configuration sauf les show »** : sur IOS, `show` se lance depuis une configuration avec `do show ...`. Le cours dit que certaines commandes ne marchent pas dans les autres modes, ce qui reste vrai (complément).
3. **Étudiant : « je sais pas à quoi tout ça sert »** : `ip address` donne son adresse à l'interface et `no shutdown` l'active (une interface de routeur est désactivée par défaut, voir [[VLAN]]). Le commentaire « to enable the interface » placé à côté de `interface gigabitEthernet 0/1` est donc inexact : cette ligne sélectionne l'interface (complément).
4. **Adressage de l'exemple** : l'interface 0/2 reçoit `203.0.113.5/255.255.255.252`, alors que l'exemple de route cible 192.168.20.0 via `g0/2`. Ce n'est pas le même plan d'adressage que dans [[Chp2 - Static Routing]].
5. **Redondance** : les sections du mode de la ligne de commande sont répétées dans [[Formation CISCO Packet Tracer]].
