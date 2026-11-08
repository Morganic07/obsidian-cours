---
type: concept
tags: [year3]
aliases: [firewall, pare-feu à états, stateful firewall, filtrage à états, filtrage sans état, stateless]
matieres: [Computer Network]
sources: ["[[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]]", "[[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un pare-feu (*firewall*) est un dispositif, matériel ou logiciel, qui filtre le trafic réseau entre deux zones de confiance différentes (par exemple un réseau interne et Internet) selon une politique de sécurité : il autorise ou bloque les paquets d'après leurs adresses, leurs ports, leur protocole et, pour un pare-feu à états, la connexion à laquelle ils appartiennent. Les [[Liste de contrôle d'accès|listes de contrôle d'accès]] d'un routeur en sont une forme simple.

## Dans le cours

Nommé dans le cours sans définition. Le cours affirme que NAT « agit comme un pare-feu » : il cache les adresses internes aux réseaux externes et réduit le risque d'accès non autorisé et d'attaques.

Le chapitre sur les [[Liste de contrôle d'accès|ACL]] ([[6 - Access Control List]]) présente le filtrage de paquets par un routeur, sans parler de pare-feu.

## Filtrage sans état et à états (complément, hors du cours)

- **Sans état** (*stateless*) : chaque paquet est jugé isolément, d'après ses en-têtes (adresses, protocole, ports). C'est le cas d'une ACL : pour qu'un client interne reçoive les réponses d'un serveur web, il faut une règle explicite qui autorise aussi le trafic de retour, ce qui ouvre plus large que nécessaire.
- **À états** (*stateful*) : le pare-feu tient une table des connexions en cours (adresses, ports, état TCP). Une réponse à une requête autorisée est reconnue comme appartenant à une connexion existante et passe automatiquement ; un paquet entrant qui ne correspond à aucune connexion est rejeté, sauf règle explicite.

Voir aussi : [[NAT et PAT]], [[Liste de contrôle d'accès]], [[Numéro de port]].

Résumés : [[5 - NAT ／ PAT]], [[6 - Access Control List]]
