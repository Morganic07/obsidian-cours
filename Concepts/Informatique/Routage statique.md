---
type: concept
tags: [year3]
aliases: [route statique, routes statiques, static route, static routing, route par défaut, default route, table de routage, next hop, directly connected network, réseau directement connecté, réseaux directement connectés, remote network, réseau distant, show ip route, route statique entièrement spécifiée, fully specified static route, réseau stub, stub network, gateway of last resort]
matieres: [Computer Network]
sources: ["[[2 - Static Routing|Chp2 - Static Routing]]", "[[3 - Dynamic Routing|Chp3 - Dynamic Routing]]", "[[1 - Computer Networks|chp1 - Computer Networks]]", "[[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]]"]
maj: 2026-11-08
---

**Définition** (d'après [[2 - Static Routing]]) : un routeur décide du chemin d'un paquet avec sa **table de routage**. Il apprend seul les réseaux directement connectés (codes `C` et `L` dans `show ip route`) mais pas les réseaux distants : il lui faut des routes explicites, statiques (écrites par l'administrateur) ou dynamiques (voir [[Routage dynamique]]).

**Route statique** : `ip route <réseau> <masque> <sortie>`, où la sortie est une interface ou l'adresse du saut suivant (next hop). Elle apparaît avec le code `S`. Exemples du cours :
- `ip route 10.0.1.0 255.255.255.0 gigabitEthernet 0/0`
- `ip route 10.0.1.0 255.255.255.0 203.0.113.2` (affichée `[1/0] via 203.0.113.2`)
- suppression : `no ip route ...`

**Route par défaut** : utilisée quand aucune route précise n'existe, fréquente en bordure vers Internet. Réseau `0.0.0.0/0` : `ip route 0.0.0.0 0.0.0.0 <next hop>`.

Dans `show ip route`, `L` (local) désigne l'adresse de l'interface elle-même, en /32.

## Compléments (hors du cours)

**Avantages et limites face au [[Routage dynamique]]**

| Avantages | Limites |
|---|---|
| ne consomme ni processeur, ni mémoire, ni bande passante | tout est configuré à la main, à chaque ajout de réseau |
| chemin prévisible, rien n'est annoncé aux voisins (plus sûr) | une panne de lien n'est pas contournée automatiquement |
| simple sur un petit réseau | ne passe pas à l'échelle |

Usages typiques : petits réseaux, **réseau stub** (une seule sortie, comme un site relié par un seul lien), route par défaut vers le fournisseur d'accès.

**Configurer les deux sens** : chaque routeur doit avoir une route vers le réseau de l'autre ; sinon le paquet aller arrive mais la réponse est détruite au retour, et le `ping` échoue.

**Saut suivant** : c'est l'adresse IP du routeur voisin **sur le lien commun**, jamais une adresse d'un réseau lointain.

**Trois formes de route statique**
- par saut suivant : `ip route 10.0.1.0 255.255.255.0 203.0.113.2` ;
- par interface de sortie : `ip route 10.0.1.0 255.255.255.0 g0/0` ; convient à un lien série point à point, mais sur Ethernet (multi-accès) le routeur doit trouver l'[[Adresse MAC]] de chaque destination par ARP et compte sur le *proxy ARP* du voisin ;
- **entièrement spécifiée** (interface et saut suivant) : `ip route 10.0.1.0 255.255.255.0 g0/0 203.0.113.2`, préférable sur Ethernet.

**Route statique flottante** : route de secours, avec une [[Distance administrative]] plus grande que celle de la route principale, donnée en dernier paramètre (`ip route 10.0.1.0 255.255.255.0 198.51.100.2 130`). Le `1` de `[1/0]` est la distance administrative par défaut d'une route statique, le `0` sa métrique.

**Route par défaut dans la table** : elle s'affiche avec le code `S*` (le `*` marque la candidate par défaut), et la ligne « Gateway of last resort is 203.0.113.2 to network 0.0.0.0 » apparaît en tête. Sans route par défaut : « Gateway of last resort is not set ».

**Vérification** : `show ip route static` (routes statiques seules), `ping` vers le réseau distant, `traceroute` pour voir les sauts traversés (voir [[Commande ping]]).

Notion parente : [[Routage IP]]. Liens : [[Routage dynamique]], [[Routeur]], [[CLI Cisco IOS]], [[Adressage IPv4 et CIDR]]

Résumés : [[2 - Static Routing]], [[3 - Dynamic Routing]], [[1 - Computer Networks]]
