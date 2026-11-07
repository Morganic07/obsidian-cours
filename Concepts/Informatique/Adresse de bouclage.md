---
type: concept
tags:
  - year2
  - year3
aliases:
  - Interface de bouclage
  - loopback
  - loopback interface
  - localhost
  - 127.0.0.1
  - boucle locale
  - loopback address
  - adresse de loopback
  - 127.0.0.0/8
matieres:
  - Operating System
  - Computer Network
sources:
  - "[[3 - TP3|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
  - "[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]"
maj: 2026-11-07
---

**En Operating System** : `lo` est une interface réseau virtuelle qui permet à l'ordinateur de s'envoyer des données à lui-même via le réseau, sans passer par le matériel réseau physique ; elle sert à tester. L'entrée `127.0.0.1 localhost` du [[Fichier hosts|fichier /etc/hosts]] doit être conservée.

**En Computer Network** : la plage 127.0.0.0 à 127.255.255.255 est réservée dans la classe A et sert à tester la pile réseau du poste local. Elle reste toujours joignable, même si l'interface n'est reliée à aucun réseau. La classe A utile va donc de 0 à 126, et une adresse réservée ne s'attribue pas à un hôte.

Notion parente : [[Interface réseau]]. Voir aussi : [[Commande ping]], [[Adressage IPv4 et CIDR]].

Résumés : [[3 - TP3]], [[2 - IP Addressing]]
