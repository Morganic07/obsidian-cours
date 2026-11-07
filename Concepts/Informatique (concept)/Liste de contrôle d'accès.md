---
type: concept
tags: [year3]
aliases: [ACL, ACLs, Access Control List, access-list, wildcard mask, masque générique, ACE, refus implicite, implicit deny, ACL standard, ACL étendue, standard ACL, extended ACL, ip access-group, inbound, outbound]
matieres: [Computer Network]
sources: ["[[chp 6 - Access Control List (résumé)|chp6 - Access Control List]]", "[[chp 5 - NAT ／ PAT (résumé)|Chp5 - NAT ／ PAT]]"]
maj: 2026-11-06
---

Une ACL est un filtre de paquets : une séquence ordonnée d'ACE (Access Control Entries) qui indique au routeur de laisser passer (`permit`) ou de rejeter (`deny`) un trafic. Elle est écrite en configuration globale et ne prend effet qu'une fois appliquée à une interface, en entrée (`in`) ou en sortie (`out`). Le sens (*inbound*, *outbound*) se lit depuis le routeur.

- Le routeur lit les ACE de haut en bas et s'arrête à la première qui correspond.
- Un `deny` implicite termine toute ACL.
- Au plus une ACL par interface et par direction : une seconde remplace la première.
- **Standard** : filtre sur la source seule (numéros 1 à 99 et 1300 à 1999). **Étendue** : source, destination, ports. Chacune peut être numérotée ou nommée.
- Syntaxe : `access-list <n> {deny | permit} <ip> <wildcard>`, puis `ip access-group <n> {in | out}`.
- Une ACL standard se place près de la destination.

**Wildcard mask** : masque de sous-réseau inversé, obtenu en retranchant chaque octet à 255. Un 0 signifie « doit correspondre », un 1 « peu importe ». /24 donne 0.0.0.255, /28 donne 0.0.0.15, /32 donne 0.0.0.0. On le retrouve dans l'`access-list` d'un PAT : `access-list 1 permit 192.168.0.0 0.0.0.255` désigne le trafic à traduire ([[chp 5 - NAT ／ PAT (résumé)]]).

> [!warning] Écart dans le cours
> Dans la solution du TP, l'exigence 4 (PC1 vers 10.0.1.0/24) est placée sur « G0/2 en sortie ACL 10 ». 10.0.1.0/24 est derrière G0/1 (complément).

Voir aussi : [[NAT et PAT]], [[CLI Cisco IOS]], [[Numéro de port]]

Résumés : [[chp 6 - Access Control List (résumé)]], [[chp 5 - NAT ／ PAT (résumé)]]
