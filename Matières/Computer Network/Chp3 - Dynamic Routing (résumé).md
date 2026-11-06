---
type: source
tags: [year3]
sources: ["[[Chp3 - Dynamic Routing]]"]
maj: 2026-11-05
---

Résumé de [[Chp3 - Dynamic Routing]], dans [[Computer Network (matière)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi.

## Contenu, dans l'ordre du cours

- **Route par défaut** : utilisée quand la table n'a pas de route précise, fréquente en bordure de réseau vers Internet. Elle s'écrit `0.0.0.0/0` : `ip route 0.0.0.0 0.0.0.0 <next hop ip>` (exemple : `203.0.113.2`). Voir [[Routage statique]].
- **Routage dynamique** : les routeurs apprennent seuls les chemins en échangeant leurs informations par des protocoles de routage. Avantages : adaptation aux pannes de lien et aux nouveaux réseaux, moins de configuration manuelle. Voir [[Routage dynamique]].
- **Types de protocoles** : IGP à l'intérieur d'un système autonome (RIP, EIGRP, OSPF), EGP entre systèmes autonomes (BGP). Analogie : IGP = routage entre les rues d'une ville, EGP = routage entre villes.
- **RIP** : protocole à vecteur de distance, métrique = nombre de sauts, mises à jour toutes les 30 secondes, 15 sauts au maximum (16 = inatteignable). RIPv1 est classful (mises à jour sans masque), RIPv2 est classless et gère le VLSM. Avantages : simple, répandu, petites tables. Limites : convergence lente, 15 sauts, boucles de routage possibles.
- **Configuration** : `router rip`, `version 2`, `no auto-summary`, `network <réseau>`, `default-information originate`. `version 2` active aussi l'authentification et les mises à jour multicast (224.0.0.9). `no auto-summary` désactive le résumé automatique de classe. `default-information originate` annonce `0.0.0.0/0` dans RIP si le routeur en a une.
- **Commandes de gestion** : `show ip protocols`, `show ip rip database`, `show ip route rip`, `show ip route`, `no router rip`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images lues par leur transcription, aucune ouverte.

1. **`network` sans argument** : dans l'exemple de configuration, la ligne `network` n'a pas d'adresse. Elle est incomplète, il faut un réseau (le tableau de commandes écrit `network <network address>`).
2. **`default information-originate`** : le tableau de l'image l'écrit sans trait d'union ; l'exemple de configuration écrit `default-information originate`, qui est la forme correcte (complément).
3. **Titre du chapitre** : le chapitre s'appelle « Dynamic Routing » mais n'aborde que RIP. OSPF et EIGRP sont seulement nommés.
4. **Dernières lignes** : « Vlan is always connected to the switch » et « Dividing the broadcast domain ... called V-LAN » terminent la note, sans lien avec le routage. Elles relèvent du chapitre sur les VLAN, voir [[Chp4 - VLAN ／ IVR Commands (résumé)|Chp4 - VLAN]].
5. **Schéma de la route par défaut** : l'adresse « 113.1 » est lue sur l'image, probablement 203.0.113.1.
