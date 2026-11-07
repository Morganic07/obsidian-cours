---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]], dans [[Computer Network (index)]] : notes de prise en main de Cisco Packet Tracer (matériel utilisé, modes de la ligne de commande IOS, mémoires de configuration) et d'un tutoriel vidéo sur `ping`. Note très courte, sans image, écrite par l'étudiante (« recap cours du prof », avec un « je crois » sur le sens d'IOS).

## Récapitulatif du cours

Le même texte figure au début de [[1 - Computer Networks (résumé)|chp1 - Computer Networks]]. Voir [[CLI Cisco IOS]].

### Matériel utilisé

- [[Routeur|Routeurs]] : **Cisco 2911**.
- Commutateurs (*switches*) : **Cisco 2960**.

### Les trois modes de la CLI IOS

Le système d'exploitation de Cisco est **IOS** (*Internetwork Operating System*, développé avec un « je crois » dans la note). Sa CLI a trois modes :

| Mode | Invite | Rôle |
|---|---|---|
| *User mode* | `>` | commandes très restreintes (`show`) |
| *Privilege mode* | `#` | en plus : sauvegarder, effacer, redémarrer la configuration et les appareils |
| *Global Configuration mode* | `(config)#` | toutes les commandes de configuration, **sauf** les commandes `show` |

En cliquant sur un PC ou un commutateur dans Packet Tracer, on accède à sa CLI.

- Passer en mode privilégié : `> enable`
- Passer en configuration globale : `# configure terminal`
- On **ne peut pas** sauter du mode utilisateur au mode de configuration globale : toujours passer par le mode privilégié.
- Revenir au mode précédent : `exit`
- Certaines commandes d'un mode ne sont pas utilisables dans les autres modes, même « supérieurs ».

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
| *startup-config* | mémoire non volatile (complément : la note ne le précise pas) | chargée dans la RAM (comme *running-config*) au démarrage | `show startup-config` |

- Sauvegarder la configuration : `write memory`.
- Tout cela se fait en mode privilégié.

### Nommage des interfaces

Une interface s'affiche par exemple `FastEthernet0/1` : le `0/1` signifie **slot/port** (voir [[Interface réseau]]).

## Tutoriel vidéo : `ping` entre deux PC

Dans Packet Tracer, ouvrir le PC, puis **Desktop > Command Prompt**, et lancer :

```
ping <IP de l'ordinateur à joindre>
```

Voir [[Commande ping]].

## Adressage IP et masques de sous-réseau

Le titre existe, la section est vide. Le sujet est traité dans [[2 - IP Addressing (résumé)]].

## Points à vérifier dans le cours

1. **Contenu manquant** : la partie sur l'adressage IP et les masques n'a pas de texte.
2. **Doublon** : le récapitulatif est identique à celui de [[1 - Computer Networks (résumé)|chp1 - Computer Networks]]. Rien de nouveau n'est à y chercher.
3. **« startup Config : fait monter les running config dans la RAM »** : formulation de l'étudiante. Au démarrage, c'est la *startup-config* qui est copiée dans la RAM pour devenir la *running-config*.
4. **« Global Config mode permet de run all configurations commands sauf les show commands »** : vrai pour les commandes `show` saisies telles quelles ; IOS permet de les lancer depuis ce mode avec le préfixe `do` (complément, hors cours).
