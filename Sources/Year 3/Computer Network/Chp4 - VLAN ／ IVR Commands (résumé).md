---
type: source
sources: ["[[Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-05
---

Résumé de [[Chp4 - VLAN ／ IVR Commands]], dans [[Year 3 - Computer Network]]. Cours en anglais, sans image. Voir [[VLAN]].

## Contenu, dans l'ordre du cours

- **Définitions** : le routeur relie des réseaux différents, le switch relie les terminaux au LAN, un VLAN crée plusieurs domaines de diffusion (broadcast) sur un switch. Par défaut, un switch Cisco a un seul domaine de diffusion : tous ses ports sont dans le VLAN 1, qui est le VLAN par défaut et ne peut pas être supprimé. Un lien access est associé à un seul VLAN, un lien trunk transporte plusieurs VLAN.
- **Créer les VLAN** : `vlan <ID>` puis `name <nom>` (exemples : 10 ADMIN, 20 SALES, 30 WORKGROUP).
- **Associer les ports** : `interface range fastEthernet 0/1-5`, `switchport mode access`, `switchport access vlan 10`, de même pour 0/6-10 (VLAN 20) et 0/11-15 (VLAN 30).
- **Trunk entre deux switchs** : `switchport mode trunk` et `switchport trunk allowed vlan add 10` (puis 20, 30) des deux côtés.
- **Routage inter-VLAN (IVR)** : un routeur est nécessaire, relié au switch par un lien trunk. Sur le routeur, une sous-interface par VLAN (`interface gigabitEthernet 0/1.10`), avec `encapsulation dot1q <VLAN>` et l'adresse IP, qui sert de passerelle par défaut aux hôtes. Il faut aussi activer l'interface physique (`no shutdown`) : tous les ports d'un routeur sont désactivés par défaut.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`encapsulation dot1q 10` sur les trois sous-interfaces** (complément). **À corriger avant un examen.** Les sous-interfaces `.20` et `.30` répètent `dot1q 10`. Elles devraient porter `dot1q 20` et `dot1q 30`, un copier-coller du premier bloc.
2. **`ip 192.168.10.254 255.255.255.0`** (complément) : la commande est `ip address ...`. Le cours écrit `ip` suivi de l'adresse.
3. **Titre** : le document s'intitule « Chp5 : VLANs and InterVLANRouting » alors que la note est le chapitre 4. Le chapitre 5 est NAT et PAT.
4. **Le switch est dit relier les « terminaux »** : formulation du cours, pas d'erreur de fond.
