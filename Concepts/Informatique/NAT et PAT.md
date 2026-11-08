---
type: concept
tags: [year3]
aliases: [NAT, PAT, static NAT, NAT overload, Network Address Translation, adresses privées, RFC 1918, inside local, inside global, outside local, outside global, Port Address Translation, ip nat inside, ip nat outside, show ip nat translations, NAT dynamique, dynamic NAT, ip nat pool, table de traduction NAT, redirection de port, port forwarding, carrier-grade NAT, CGN]
matieres: [Computer Network]
sources: ["[[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]]", "[[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]]"]
maj: 2026-11-08
---

IPv4 n'offre qu'environ 4,3 milliards d'adresses ($2^{32}$). À court terme : CIDR, adresses privées et NAT. Les plages privées (RFC 1918) sont 10.0.0.0/8, 172.16.0.0/12 et 192.168.0.0/16 : elles n'ont pas à être uniques et ne passent pas sur Internet. [[Erreurs du cours#^e-nat-et-pat|✎]]

**NAT** : le routeur modifie l'adresse source et ou destination des paquets pour que des hôtes à adresse privée joignent Internet.

**Static NAT** : correspondance 1 pour 1 d'une adresse privée vers une adresse publique, donc aucune économie d'adresses.
- Inside local : adresse de l'hôte interne, vue du réseau local. Inside global : même hôte, après NAT, vu de l'extérieur. Outside local et outside global : l'hôte externe, vu du local et de l'extérieur.
- Configuration : `ip nat inside` et `ip nat outside` sur les interfaces, `ip nat inside source static <locale> <globale>`. Contrôle : `show ip nat translations`, `show ip nat statistics`, `clear ip nat translation *`.

**PAT (NAT overload)** : traduit l'adresse et le port, ce qui permet à plusieurs hôtes de partager une adresse publique (plus de 65 000 ports). Configuration : une `access-list` qui désigne le trafic, puis `ip nat inside source list 1 interface g0/0 overload`.

Le PAT exploite les [[Numéro de port|numéros de port]]. À long terme, le cours renvoie la pénurie d'adresses à [[IPv6]].

Le cours présente le NAT comme un [[Pare-feu|pare-feu]] qui cache les adresses internes. (Complément, hors du cours) Cet effet n'est que la conséquence de la traduction : un paquet entrant qui ne correspond à aucune entrée de la table de traduction n'a pas de destinataire interne et est abandonné. Ce n'est pas un filtrage choisi : le NAT ne contrôle ni les ports, ni les protocoles, ni le contenu, et ne remplace pas un vrai pare-feu ou des [[Liste de contrôle d'accès|ACL]].

## Compléments (hors du cours)

**NAT dynamique.** Entre le NAT statique et le PAT : les adresses internes sont associées à un **groupe** (*pool*) d'adresses publiques, attribuées à la demande et libérées après inactivité. La correspondance reste une pour une à un instant donné ; si le groupe est épuisé, l'hôte suivant ne peut pas sortir. Configuration, après `ip nat inside` et `ip nat outside` sur les interfaces et une ACL qui désigne les adresses internes :

```
R1(config)#ip nat pool PUBLIC 100.0.0.1 100.0.0.10 netmask 255.255.255.0
R1(config)#ip nat inside source list 1 pool PUBLIC
```

Le PAT peut aussi porter sur un groupe d'adresses plutôt que sur l'adresse de l'interface : `ip nat inside source list 1 pool PUBLIC overload`.

**Table de traduction.** Le routeur inscrit chaque correspondance (inside local ↔ inside global, avec les ports pour le PAT) au passage du premier paquet sortant, puis la consulte pour les paquets de retour, dont il rétablit l'adresse (et le port) de destination interne. C'est cette table qu'affiche `show ip nat translations`. Les entrées dynamiques expirent après un délai d'inactivité ; les entrées statiques sont permanentes.

**Ports et conflits.** Un numéro de port tient sur 16 bits, soit $2^{16} = 65\,536$ valeurs par adresse publique et par protocole (TCP, UDP). Si deux hôtes internes utilisent le même port source, le routeur réattribue un autre port source à l'un d'eux pour que chaque couple (adresse publique, port) reste unique dans la table.

**Usage du NAT statique.** Rendre joignable depuis Internet un **serveur interne** (site web, messagerie), qui doit garder la même adresse publique : la correspondance étant permanente, un hôte externe peut ouvrir une connexion vers elle.

**Limites.**
- Le NAT rompt le principe du **bout en bout** d'Internet : l'adresse d'un hôte interne n'est pas celle que voit son correspondant.
- Les protocoles qui écrivent des adresses IP ou des ports dans leurs **données** (FTP en mode actif, VoIP avec SIP, IPsec) cassent si le routeur ne les réécrit pas aussi ; il faut des modules d'aide (ALG, *Application Level Gateway*) ou des contournements (NAT-T pour IPsec).
- Aucune **connexion entrante** n'est possible vers un hôte interne sans correspondance statique ou **redirection de port** (*port forwarding*, un NAT statique limité à un port).

**PAT domestique et CGN.** Une box Internet fait du PAT : tous les appareils du foyer, en 192.168.x.x, sortent avec l'unique adresse publique fournie par l'opérateur. Faute d'adresses IPv4, certains opérateurs ajoutent un second niveau, le **CGN** (*carrier-grade NAT*) : les box reçoivent une adresse de la plage partagée 100.64.0.0/10, traduite à nouveau par l'opérateur. Une redirection de port sur la box devient alors inopérante.

Liens : [[Liste de contrôle d'accès]], [[CLI Cisco IOS]], [[Adressage IPv4 et CIDR]], [[Numéro de port]], [[IPv6]], [[Pare-feu]]

Résumé : [[5 - NAT ／ PAT]]
