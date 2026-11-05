---
type: source
sources: ["[[Chp5 - NAT ／ PAT]]"]
maj: 2026-11-05
---

Résumé de [[Chp5 - NAT ／ PAT]], dans [[Year 3 - Computer Network]]. Cours mêlant français et anglais. En cas d'écart, le cours et ses images font foi. Voir [[NAT et PAT]].

## Contenu, dans l'ordre du cours

- **Pourquoi** : IPv4 offre environ 4,2 milliards d'adresses, trop peu. Solution à long terme : IPv6. À court terme : CIDR, adresses IPv4 privées, NAT.
- **Adresses privées (RFC 1918)** : 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Elles n'ont pas à être uniques globalement mais ne passent pas sur Internet. NAT les traduit en adresses publiques (le routeur traduit par exemple une adresse privée en une adresse publique, et inversement).
- **Fonctionnement** : NAT modifie l'adresse source et ou destination des paquets. Exemple : PC1 (192.168.0.167) vers 8.8.8.8, R1 remplace la source par 203.0.113.1 à l'aller, et fait l'inverse au retour.
- **Static NAT** : correspondance 1 pour 1 entre une adresse privée et une adresse publique. Vocabulaire : inside local (adresse de l'hôte interne vue du réseau local), inside global (adresse de l'hôte interne après NAT, vue de l'extérieur), outside local et outside global (adresses de l'hôte externe, vues du local et de l'extérieur). Il n'économise pas d'adresses.
- **Configuration du static NAT** : `ip nat inside` sur l'interface interne, `ip nat outside` sur l'externe, `ip nat inside source static 192.168.0.167 100.0.0.1`. Gestion : `show ip nat translations`, `show ip nat statistics`, `clear ip nat translation *`.
- **PAT (NAT overload)** : traduit l'adresse et le numéro de port. Chaque flux a son port, une seule adresse publique sert à plusieurs hôtes (plus de 65 000 ports). Exemple : 192.168.0.167:65205 et 192.168.0.168:59641 deviennent tous deux 203.0.113.1, avec leur port. Le routeur retient quelle adresse locale utilise quelle adresse globale et quel port.
- **Configuration de PAT** : mêmes interfaces `inside` et `outside`, `access-list 1 permit 192.168.0.0 0.0.0.255` pour le trafic à traduire, puis `ip nat inside source list 1 interface g0/0 overload`. Voir [[Liste de contrôle d'accès]] pour la liste d'accès et son wildcard mask.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les images 3 et 4 ont été ouvertes ; les autres sont lues par leur transcription.

1. **`overlead`** : image 3 ouverte. Le cours écrit bien `overlead` dans la commande et dans le texte. La commande Cisco est `overload` (complément). **À corriger avant un examen.**
2. **`R1(config)#ip nat outside`** (complément) : l'image montre ce prompt (images 1 et 3) après `interface gigabitEthernet 0/0`. `ip nat outside` est une commande d'interface, il faut le prompt `R1(config-if)#`.
3. **`196.168.0.167`** : image 4 ouverte. La note du bas écrit bien « 196.168.0.167 », alors que le PC est en 192.168.0.167. Faute du cours.
4. **« NAT acts as a firewall »** (complément). Le cours affirme que NAT joue un rôle de pare-feu en cachant les adresses internes et réduit les risques d'attaque. C'est un effet de bord, pas un mécanisme de sécurité : NAT ne remplace pas un pare-feu ou des ACL.
5. **Adresses du static NAT** : l'exemple traduit vers `100.0.0.1`, alors que l'interface externe de R1 est en 203.0.113.1 et que le PAT, juste après, traduit vers 203.0.113.1. `100.0.0.0/8` n'est pas une plage privée du RFC 1918, c'est un choix d'exemple.
6. **Phrase de transition** : « le routeur va traduire la private IP 192.168.0.0 en une public IP 150.50.0.0 » mêle adresses de réseau et adresses d'hôtes, formulation simplifiée.
7. **Fausses alertes** : le « 7 » en coin de l'image 4 est un numéro de page, sans contenu. Le PAT garde le port d'origine dans l'exemple ; en pratique, le routeur peut aussi le changer (complément).
