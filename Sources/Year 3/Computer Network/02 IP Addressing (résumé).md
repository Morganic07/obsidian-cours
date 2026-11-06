---
type: source
sources: ["[[raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing]] (57 diapositives, en anglais, « IPv4 Addressing »), dans [[Year 3 - Computer Network]]. Les tableaux et schémas ont été lus sur les diapositives 14 à 16 et 23 à 24 ; le reste, par le texte. Le concept détaillé est [[Adressage IPv4 et CIDR]].

## Contenu, dans l'ordre du cours

- **Terminologie** : bit, octet (8 bits), adresse réseau (pour le routage vers un réseau distant), adresse de broadcast (envoi à tous les nœuds), adresse d'hôte.
- **Notation décimale pointée** : 32 bits en quatre octets séparés par des points. Rappel décimal-binaire avec une conversion de 255, 240, 224, 192, 160, 144, 128, 96, 64, 40 en 8 bits (par exemple 240 = 11110000, 40 = 00101000).
- **Adresse IPv4** : numéro de 32 bits, soit 4,3 milliards d'adresses ; l'IPv4 est la quatrième version du protocole. Une adresse donne l'adresse réseau et l'adresse d'hôte, séparées par le masque de sous-réseau (1 sur les bits réseau, 0 sur les bits hôte). Exemple : 192.168.10.4 avec 255.255.255.0.
- **Classes A à E** : A (premier octet 0 à 127, masque /8, $2^{24}$ adresses par réseau), B (128 à 191, /16, 65 536), C (192 à 223, /24, 256), D (224 à 239, multicast), E (240 à 255, recherche). La plage 127.0.0.0/8 est réservée au bouclage (loopback), qui reste joignable même sans réseau : la classe A utile va donc de 0 à 126.
- **Longueur de préfixe** : `10.224.64.19/8`, `172.224.32.6/16`, `192.168.1.4/24`. Masques par défaut : 255.0.0.0, 255.255.0.0, 255.255.255.0.
- **Adresses spéciales d'un réseau** : adresse réseau (partie hôte à 0) et broadcast (partie hôte à 1) ne s'attribuent pas ; première adresse utilisable juste après le réseau, dernière juste avant le broadcast. Schémas avec deux réseaux `192.168.1.0/24` et `192.168.2.0/24` reliés par un routeur.
- **Hôtes par réseau** : $2^n - 2$ avec $n$ bits hôte.
- **IANA et gaspillage** : l'IANA attribuait des réseaux selon la taille des entreprises ; une entreprise de 5000 hôtes recevait un réseau de classe B, d'où environ 60 000 adresses perdues.
- **CIDR** (IETF, 1993) : fin des préfixes imposés /8, /16, /24 ; découpage en sous-réseaux. Tableau pour `192.168.1.0` du /24 (254 hôtes) au /32, avec la table des masques de 255.255.255.0 (/24) à 255.255.255.255 (/32).
- **Quiz et exercices** : conversion binaire-décimal de 00111111 00111000 11100111 00010011 ; questions à choix sur l'adresse IP, le masque et les adresses non attribuables ; pour 43.109.23.12/8, 129.221.23.13/16 et 224.192.64.32/24, trouver adresse réseau, nombre d'hôtes, broadcast, première et dernière adresse utilisable ; découper `192.168.1.0/24` en quatre sous-réseaux selon des besoins en hôtes, et `192.168.255.0/24` en cinq sous-réseaux de même taille.

## Liens

Prérequis du [[Routage statique]] et du [[Routage dynamique]] ; le [[NAT et PAT]] traite les adresses privées ; [[CLI Cisco IOS]] pour configurer les adresses.

## Points à vérifier

1. **Plage de la classe A** : la diapositive 15 affiche « 0 à 127 » dans le tableau, et la ligne en rouge juste dessous corrige en « 0 à 126 ». Les adresses commençant par 0 sont aussi réservées (complément : usage courant, hors cours).
2. **Quiz 224.192.64.32/24** : cette adresse est de classe D (multicast), qui n'a pas de masque par défaut ni d'hôtes ; l'exercice utilise un /24 pour le calcul, ce qui sort de l'adressage classful.
3. **Ligne /31 du tableau CIDR** : $2^1 - 2 = 0$ hôte utilisable, alors qu'un /31 sert en pratique aux liaisons point à point (complément : hors cours).
