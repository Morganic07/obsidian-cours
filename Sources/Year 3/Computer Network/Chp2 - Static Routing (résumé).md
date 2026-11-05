---
type: source
sources: ["[[Chp2 - Static Routing]]"]
maj: 2026-11-05
---

Résumé de [[Chp2 - Static Routing]], dans [[Year 3 - Computer Network]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Un routeur utilise sa table de routage pour décider du chemin d'un paquet. Il apprend seul les réseaux directement connectés, mais pas les réseaux distants : il faut des routes explicites, statiques ou dynamiques. Voir [[Routage statique]].

## Contenu, dans l'ordre du cours

- **Routage IP** : acheminer des paquets d'un réseau source vers un réseau de destination à travers des routeurs. Routes statiques (configurées à la main) ou dynamiques (apprises par protocole).
- **Réseaux connectés** : exemple Packet Tracer avec R1 (réseaux 192.168.1.0/24 et 192.168.2.0/24, lien 203.0.113.0/30 par G0/0) et R2 (réseaux 10.0.1.0/24 et 10.0.2.0/24). Tableau des réseaux directement connectés par routeur et interface.
- **Réseaux distants** : tableau avec interface de sortie et adresse du saut suivant (next hop) : R1 vers 10.0.1.0/24 et 10.0.2.0/24 via G0/0 et 203.0.113.2, R2 vers 192.168.1.0/24 et 192.168.2.0/24 via G0/0 et 203.0.113.1.
- **`show ip route`** : `C` pour connecté, `L` pour local (adresse de l'interface en /32), `S` pour statique.
- **Route statique avec interface de sortie** : `ip route <réseau> <masque> <interface>` (par exemple `ip route 10.0.1.0 255.255.255.0 gigabitEthernet 0/0` sur R1). Sur R2, deux routes vers les réseaux 192.168.x.0/24, affichées `S ... is directly connected, GigabitEthernet0/0`.
- **Route statique avec adresse du saut suivant** : `ip route 10.0.1.0 255.255.255.0 203.0.113.2`, affichée `S 10.0.1.0/24 [1/0] via 203.0.113.2`.
- **Supprimer une route** : préfixer la commande par `no`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. L'image 2 (tableau des réseaux connectés) a été ouverte ; les autres sont lues par leur transcription.

1. **Dernière ligne du tableau des réseaux connectés** : image ouverte, « R3 » est écrit pour la ligne 203.0.113.0/30, alors que l'interface citée est « R2: GigabitEthernet 0/0 » et que le schéma n'a que deux routeurs. C'est une erreur du cours, il faut lire R2.
2. **Interface de sortie et adresse du saut suivant** (complément) : sur un lien Ethernet entre deux routeurs, la route avec le saut suivant est la forme usuelle, car la route avec l'interface de sortie oblige le routeur à résoudre l'adresse de chaque destination sur ce lien. Packet Tracer accepte les deux.
3. **Image 1** : la sortie `show ip route` de R1 avant configuration n'a que des routes `C` et `L`, aucune `S`, ce qui est cohérent avec le texte.
