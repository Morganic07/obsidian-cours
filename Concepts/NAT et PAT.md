---
type: concept
aliases: [NAT, PAT, static NAT, NAT overload, Network Address Translation, adresses privées, RFC 1918, inside local, inside global]
matieres: [Computer Network]
sources: ["[[Chp5 - NAT ／ PAT]]"]
maj: 2026-11-05
---

IPv4 n'offre qu'environ 4,2 milliards d'adresses. À court terme : CIDR, adresses privées et NAT. Les plages privées (RFC 1918) sont 10.0.0.0/8, 172.16.0.0/12 et 192.168.0.0/16 : elles n'ont pas à être uniques et ne passent pas sur Internet.

**NAT** : le routeur modifie l'adresse source et ou destination des paquets pour que des hôtes à adresse privée joignent Internet.

**Static NAT** : correspondance 1 pour 1 d'une adresse privée vers une adresse publique, donc aucune économie d'adresses.
- Inside local : adresse de l'hôte interne, vue du réseau local. Inside global : même hôte, après NAT, vu de l'extérieur. Outside local et outside global : l'hôte externe, vu du local et de l'extérieur.
- Configuration : `ip nat inside` et `ip nat outside` sur les interfaces, `ip nat inside source static <locale> <globale>`. Contrôle : `show ip nat translations`, `show ip nat statistics`, `clear ip nat translation *`.

**PAT (NAT overload)** : traduit l'adresse et le port, ce qui permet à plusieurs hôtes de partager une adresse publique (plus de 65 000 ports). Configuration : une `access-list` qui désigne le trafic, puis `ip nat inside source list 1 interface g0/0 overload`.

> [!warning] Écart dans le cours
> Le cours écrit `overlead` au lieu de `overload`, et présente NAT comme un pare-feu. NAT n'est pas un mécanisme de sécurité (complément).

Liens : [[Liste de contrôle d'accès]], [[CLI Cisco IOS]]

Résumé : [[Chp5 - NAT ／ PAT (résumé)]]
