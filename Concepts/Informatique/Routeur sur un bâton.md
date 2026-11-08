---
type: concept
tags: [year3]
aliases: [router-on-a-stick, router on a stick, ROAS]
sources: ["[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : montage de routage inter-VLAN dans lequel un [[Routeur|routeur]] est relié au [[Commutateur|commutateur]] par un seul lien physique configuré en *trunk* [[Encapsulation 802.1Q|802.1Q]], découpé côté routeur en une [[Sous-interface|sous-interface]] par [[VLAN]]. Chaque sous-interface reçoit l'étiquette de son VLAN et une adresse IP de son sous-réseau, qui sert de [[Passerelle par défaut|passerelle par défaut]] aux hôtes de ce VLAN :

```
Router(config)# interface g0/1
Router(config-if)# no shutdown
Router(config-if)# interface g0/1.10
Router(config-subif)# encapsulation dot1q 10
Router(config-subif)# ip address 192.168.10.254 255.255.255.0
```

et de même pour chaque VLAN ; côté commutateur, le port relié au routeur est mis en `switchport mode trunk`.

**Trajet d'un paquet** : un hôte du VLAN 10 qui écrit à un hôte du VLAN 20 envoie la trame à sa passerelle ; elle monte au routeur étiquetée VLAN 10, le routeur la route vers la sous-interface du VLAN 20 et la renvoie sur le même lien, étiquetée VLAN 20.

**Avantage** : un seul port de routeur, quel que soit le nombre de VLAN.

**Limite** : tout le trafic inter-VLAN passe deux fois sur ce lien (montée puis descente), dont le débit est partagé ; le lien et le routeur sont aussi un point de panne unique.

**Alternatives** : une interface physique du routeur par VLAN, reliée à un port *access* de chaque VLAN (simple, mais consomme autant de ports que de VLAN) ; ou un [[Commutateur de niveau 3|commutateur de niveau 3]] qui route lui-même entre ses VLAN par des SVI, solution courante en entreprise.

## Dans le cours

C'est la configuration IVR (*Inter-VLAN Routing*) de [[4 - VLAN ／ IVR Commands]] : routeur relié au commutateur par un lien *trunk*, sous-interfaces `gigabitEthernet 0/1.10`, `.20`, `.30` avec `encapsulation dot1q` ; le cours ne donne pas le nom du montage, qu'apportent les compléments de la fiche.

Voir aussi : [[VLAN]], [[Sous-interface]], [[Encapsulation 802.1Q]], [[Passerelle par défaut]], [[Commutateur de niveau 3]], [[Domaine de diffusion]].

Résumés : [[4 - VLAN ／ IVR Commands]]
