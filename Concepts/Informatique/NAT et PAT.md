---
type: concept
tags: [year3]
aliases: [NAT, PAT, static NAT, NAT overload, Network Address Translation, adresses privées, RFC 1918, inside local, inside global, outside local, outside global, Port Address Translation, ip nat inside, ip nat outside, show ip nat translations]
matieres: [Computer Network]
sources: ["[[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]]"]
maj: 2026-11-07
---

IPv4 n'offre qu'environ 4,3 milliards d'adresses ($2^{32}$). À court terme : CIDR, adresses privées et NAT. Les plages privées (RFC 1918) sont 10.0.0.0/8, 172.16.0.0/12 et 192.168.0.0/16 : elles n'ont pas à être uniques et ne passent pas sur Internet.

**NAT** : le routeur modifie l'adresse source et ou destination des paquets pour que des hôtes à adresse privée joignent Internet.

**Static NAT** : correspondance 1 pour 1 d'une adresse privée vers une adresse publique, donc aucune économie d'adresses.
- Inside local : adresse de l'hôte interne, vue du réseau local. Inside global : même hôte, après NAT, vu de l'extérieur. Outside local et outside global : l'hôte externe, vu du local et de l'extérieur.
- Configuration : `ip nat inside` et `ip nat outside` sur les interfaces, `ip nat inside source static <locale> <globale>`. Contrôle : `show ip nat translations`, `show ip nat statistics`, `clear ip nat translation *`.

**PAT (NAT overload)** : traduit l'adresse et le port, ce qui permet à plusieurs hôtes de partager une adresse publique (plus de 65 000 ports). Configuration : une `access-list` qui désigne le trafic, puis `ip nat inside source list 1 interface g0/0 overload`.

Le PAT exploite les [[Numéro de port|numéros de port]]. À long terme, le cours renvoie la pénurie d'adresses à [[IPv6]].

> [!warning] Écart dans le cours
> Le cours présente NAT comme un [[Pare-feu|pare-feu]]. NAT n'est pas un mécanisme de sécurité (complément).

Liens : [[Liste de contrôle d'accès]], [[CLI Cisco IOS]], [[Adressage IPv4 et CIDR]], [[Numéro de port]], [[IPv6]], [[Pare-feu]]

## Erreurs du cours

Vérifié sur les images de [[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]] :

- La configuration du PAT écrit `ip nat inside source list 1 interface g0/0 overlead` ; il faut `overload`.
- Le schéma du NAT écrit « R1 translates 203.0.113.1 to 196.168.0.167 » ; il faut 192.168.0.167, l'adresse de PC1.
- Les configurations du static NAT et du PAT écrivent `R1(config)#ip nat outside` après `interface gigabitEthernet 0/0` ; il faut l'invite `R1(config-if)#`, car la commande s'applique à l'interface.
- Le cours écrit « IPv4 provides only 4.2 milliards de IP » ; il faut 4,3 milliards ($2^{32}$), comme dans 02 IP Addressing ([[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]).

Résumé : [[5 - NAT ／ PAT]]
