---
type: concept
tags: [year3]
aliases: [ACL, ACLs, Access Control List, access-list, wildcard mask, masque générique, ACE, refus implicite, implicit deny, ACL standard, ACL étendue, standard ACL, extended ACL, ip access-group, inbound, outbound, ACL nommée, named ACL, ip access-list, show access-lists]
matieres: [Computer Network]
sources: ["[[6 - Access Control List|chp6 - Access Control List]]", "[[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]]", "[[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]]"]
maj: 2026-11-08
---

Une ACL est un filtre de paquets : une séquence ordonnée d'ACE (Access Control Entries) qui indique au routeur de laisser passer (`permit`) ou de rejeter (`deny`) un trafic. Elle est écrite en configuration globale et ne prend effet qu'une fois appliquée à une interface, en entrée (`in`) ou en sortie (`out`). Le sens (*inbound*, *outbound*) se lit depuis le routeur.

- Le routeur lit les ACE de haut en bas et s'arrête à la première qui correspond.
- Un `deny` implicite termine toute ACL.
- Au plus une ACL par interface et par direction : une seconde remplace la première.
- **Standard** : filtre sur la source seule (numéros 1 à 99 et 1300 à 1999). **Étendue** : source, destination, ports. Chacune peut être numérotée ou nommée.
- Syntaxe : `access-list <n> {deny | permit} <ip> <wildcard>`, puis `ip access-group <n> {in | out}`.
- Une ACL standard se place près de la destination.

**Wildcard mask** : masque de sous-réseau inversé, obtenu en retranchant chaque octet à 255. Un 0 signifie « doit correspondre », un 1 « peu importe ». /24 donne 0.0.0.255, /28 donne 0.0.0.15, /32 donne 0.0.0.0. On le retrouve dans l'`access-list` d'un PAT : `access-list 1 permit 192.168.0.0 0.0.0.255` désigne le trafic à traduire ([[5 - NAT ／ PAT]]).

## Compléments (hors du cours)

**ACL étendues numérotées** : plages 100 à 199 et 2000 à 2699 ; le numéro suffit au routeur pour connaître le type. Syntaxe :

```
access-list 100 permit tcp <source> <wildcard> <destination> <wildcard> eq 80
```

Le protocole est `ip` (tout le trafic IP), `tcp`, `udp` ou `icmp` ; `eq <port>` désigne un [[Numéro de port|port]] de destination (ici HTTP).

**Raccourcis** : `host A.B.C.D` équivaut à `A.B.C.D 0.0.0.0` (un seul hôte) ; `any` équivaut à `0.0.0.0 255.255.255.255` (toutes les adresses).

**ACL nommée** : `ip access-list standard NOM` ou `ip access-list extended NOM` ouvre un sous-mode où l'on saisit les ACE, chacune avec un numéro de séquence (10, 20, 30… par défaut) ; on peut insérer une ligne entre deux autres (`15 deny host …`) ou en supprimer une (`no 20`), ce qu'une ACL numérotée classique ne permet pas.

**Ordre des ACE** : les plus précises en premier. Avec `permit 192.168.1.0 0.0.0.255` puis `deny host 192.168.1.1`, l'hôte 192.168.1.1 passe, car la première ligne correspond déjà. Une ACL qui ne contient que des `deny` bloque **tout** le trafic, à cause du refus implicite : il faut au moins un `permit`.

**Placement** : une ACL étendue se place **près de la source**, pour rejeter le trafic au plus tôt, puisqu'elle désigne précisément la destination ; une ACL standard, qui ne voit que la source, se place près de la destination, sinon elle couperait la source de tous les autres réseaux.

**Entrée ou sortie** : en entrée, l'ACL filtre avant la décision de routage (un paquet refusé ne coûte pas de recherche de route) ; en sortie, après le routage, juste avant l'envoi. Une ACL en sortie ne filtre pas le trafic émis par le routeur lui-même.

**Vérification et suppression** : `show access-lists` affiche les ACE avec le nombre de correspondances de chacune ; `show ip interface` indique quelle ACL est appliquée à une interface et dans quel sens. `no access-list 10` supprime toute l'ACL 10, pas une seule ligne.

**ACL et pare-feu à états** : une ACL est **sans état** : elle juge chaque paquet isolément, sans savoir s'il répond à une connexion déjà autorisée. Pour laisser revenir les réponses, il faut une ACE explicite. Un [[Pare-feu|pare-feu à états]] suit les connexions et laisse passer ces réponses automatiquement.

Voir aussi : [[NAT et PAT]], [[CLI Cisco IOS]], [[Numéro de port]], [[Pare-feu]], [[Routeur]]

Résumés : [[6 - Access Control List]], [[5 - NAT ／ PAT]]
