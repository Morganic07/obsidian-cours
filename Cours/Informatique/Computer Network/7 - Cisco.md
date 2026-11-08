---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : notes de prise en main de Cisco Packet Tracer (matériel utilisé, modes de la ligne de commande IOS, mémoires de configuration) et d'un tutoriel vidéo sur `ping`. Note très courte, sans image, écrite par l'étudiante (« recap cours du prof », avec un « je crois » sur le sens d'IOS).

## Récapitulatif du cours

Le même texte figure au début de [[1 - Computer Networks|chp1 - Computer Networks]]. Voir [[CLI Cisco IOS]].

**Packet Tracer** est un simulateur de réseau gratuit distribué par Cisco dans le cadre de sa *Networking Academy* : on y place des équipements, on les relie par des câbles et on les configure comme de vrais appareils, avec une CLI IOS simulée. Son mode **Simulation** montre le trajet des paquets pas à pas, protocole par protocole, ce qui aide à comprendre ARP, ICMP ou les ACL. Il ne reproduit qu'une partie des commandes d'IOS. [[Complément hors du cours|ⓘ]]

### Matériel utilisé

- [[Routeur|Routeurs]] : **Cisco 2911**.
- Commutateurs (*switches*) : **Cisco 2960**.

Les deux n'opèrent pas au même niveau : le [[Routeur|routeur]] relie des réseaux IP différents et choisit la route d'un paquet selon l'adresse IP de destination (couche 3) ; le [[Commutateur|commutateur]] relie les appareils d'un même réseau local et achemine les trames selon l'adresse MAC (couche 2). [[Complément hors du cours|ⓘ]]

### Les trois modes de la CLI IOS

Le système d'exploitation de Cisco est **IOS** (*Internetwork Operating System*, développé avec un « je crois » dans la note). Sa CLI a trois modes :

| Mode | Invite | Rôle |
|---|---|---|
| *User mode* | `>` | commandes très restreintes (`show`) |
| *Privilege mode* | `#` | en plus : sauvegarder, effacer, redémarrer la configuration et les appareils |
| *Global Configuration mode* | `(config)#` | toutes les commandes de configuration, **sauf** les commandes `show` |

Le développement de la note est le bon : IOS signifie bien *Internetwork Operating System*. Rien à voir avec iOS d'Apple (Apple utilise ce nom sous licence de Cisco). [[Complément hors du cours|ⓘ]]

En cliquant sur un PC ou un commutateur dans Packet Tracer, on accède à sa CLI.

- Passer en mode privilégié : `> enable`
- Passer en configuration globale : `# configure terminal`
- On **ne peut pas** sauter du mode utilisateur au mode de configuration globale : toujours passer par le mode privilégié.
- Revenir au mode précédent : `exit`
- Certaines commandes d'un mode ne sont pas utilisables dans les autres modes, même « supérieurs ».

Depuis la configuration globale, on entre dans des **sous-modes** pour configurer un élément précis ; l'invite indique où l'on se trouve : [[Complément hors du cours|ⓘ]]

| Commande (depuis `(config)#`) | Invite | Ce qu'on configure |
|---|---|---|
| `interface g0/0` | `(config-if)#` | une [[Interface réseau\|interface]] : adresse IP, activation, ACL |
| `line console 0` / `line vty 0 4` | `(config-line)#` | l'accès par le port console ou à distance (Telnet, SSH) |
| `router rip`, `router ospf 1` | `(config-router)#` | un protocole de routage dynamique |
| `vlan 10` (commutateur) | `(config-vlan)#` | un [[VLAN]] |

- `exit` remonte d'un seul niveau ; `end` (ou Ctrl+Z) revient directement au mode privilégié. [[Complément hors du cours|ⓘ]]
- Les commandes `show` ne passent pas en configuration, mais on peut les préfixer de `do` : `Router(config)# do show running-config`. [[Complément hors du cours|ⓘ]]
- Les commandes s'abrègent tant qu'il n'y a pas d'ambiguïté (`en` pour `enable`, `conf t` pour `configure terminal`, `sh run` pour `show running-config`) ; Tab complète un mot, `?` liste les commandes ou options possibles à cet endroit. [[Complément hors du cours|ⓘ]]
- Préfixer une commande de `no` l'annule : `no shutdown` active une interface (éteinte par défaut sur un routeur), `no ip address` retire l'adresse. [[Complément hors du cours|ⓘ]]

Configuration de base d'un routeur, en exemple : [[Complément hors du cours|ⓘ]]

```
Router(config)# hostname R1
R1(config)# enable secret <mot de passe>
R1(config)# interface g0/0
R1(config-if)# ip address 192.168.1.254 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# end
R1# write memory
```

`hostname` change le nom affiché dans l'invite ; `enable secret` protège l'accès au mode privilégié par un mot de passe stocké chiffré (haché). [[Complément hors du cours|ⓘ]]

```
Router> enable
Router# configure terminal
Router(config)# exit
Router#
```

### Les deux mémoires de configuration

| Mémoire | Emplacement | Rôle | Commande d'affichage |
|---|---|---|---|
| *running-config* | [[Mémoire vive\|RAM]], effacée au redémarrage | c'est là qu'on crée les configurations, avant de les sauvegarder dans la *startup-config* | `show running-config` |
| *startup-config* | mémoire non volatile (complément : la note ne le précise pas) | copiée dans la RAM au démarrage, où elle devient la *running-config* [[Erreurs du cours#^e-7-cisco\|✎]] | `show startup-config` |

- Sauvegarder la configuration : `write memory`.
- Tout cela se fait en mode privilégié.

La mémoire non volatile qui garde la *startup-config* s'appelle la **NVRAM** (voir [[Mémoire volatile et non volatile]]). Le système IOS lui-même est stocké à part, en mémoire flash. [[Complément hors du cours|ⓘ]]

`copy running-config startup-config` fait la même chose que `write memory` et c'est la forme la plus répandue. Sans cette sauvegarde, toute la configuration est perdue au redémarrage. `erase startup-config` puis `reload` remettent l'appareil à sa configuration d'usine. [[Complément hors du cours|ⓘ]]

### Nommage des interfaces

Une interface s'affiche par exemple `FastEthernet0/1` : le `0/1` signifie **slot/port** (voir [[Interface réseau]]).

Le nom donne aussi le débit : `FastEthernet` (`Fa`) = 100 Mbit/s, `GigabitEthernet` (`Gi`, `g`) = 1 Gbit/s. Le Cisco 2911 a trois interfaces `GigabitEthernet0/0` à `0/2`, celles qu'on retrouve dans les topologies du cours (`G0/0`, `G0/1`, `G0/2`). `show ip interface brief` résume l'état (*up/down*) et l'adresse IP de chaque interface. [[Complément hors du cours|ⓘ]]

## Tutoriel vidéo : `ping` entre deux PC

Dans Packet Tracer, ouvrir le PC, puis **Desktop > Command Prompt**, et lancer :

```
ping <IP de l'ordinateur à joindre>
```

Voir [[Commande ping]].

`ping` envoie des messages [[ICMP]] *echo request* et attend des *echo reply* ; il affiche le temps aller-retour de chaque réponse. Une réponse prouve que les deux machines se joignent dans les deux sens ; une absence de réponse ne dit pas où est la panne (adresse, passerelle, câble, ACL ou pare-feu qui bloque ICMP). [[Complément hors du cours|ⓘ]]

Dans Packet Tracer, il est courant que le **premier** paquet d'un premier `ping` soit perdu (*Request timed out*) puis que les suivants passent : le PC doit d'abord trouver l'adresse MAC du destinataire ou de sa passerelle par le [[Protocole ARP|protocole ARP]], et la première requête expire pendant ce temps. Ce n'est pas une panne. [[Complément hors du cours|ⓘ]]

Pour qu'un PC joigne un réseau différent du sien, il lui faut une **passerelle par défaut** (*Default Gateway*, dans Desktop > IP Configuration) : l'adresse de l'interface du routeur sur son réseau. `tracert <IP>` (sur un PC Windows ou Packet Tracer) liste les routeurs traversés. [[Complément hors du cours|ⓘ]]

## Adressage IP et masques de sous-réseau

Le titre existe, la section est vide. Le sujet est traité dans [[2 - IP Addressing]].
