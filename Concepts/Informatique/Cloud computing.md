---
type: concept
tags: [year2]
aliases: [informatique en nuage, IaaS, PaaS, SaaS, Infrastructure as a Service, Platform as a Service, Software as a Service, cloud public, cloud privé, cloud hybride]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition** (d'après [[1 - OS]]) : le cloud computing fournit du calcul, du stockage et même des applications comme service à travers un réseau. C'est une extension logique de la virtualisation, sur laquelle il repose. Exemples du cours : Shadow, Amazon EC2.

## Modèles de service (complément, hors du cours)

On distingue trois modèles, selon ce que le fournisseur gère à la place du client :

| Modèle | Ce qui est fourni | Ce que gère le client | Exemples |
|---|---|---|---|
| **IaaS** (*Infrastructure as a Service*) | [[Machine virtuelle\|machines virtuelles]], stockage, réseau | l'OS, les logiciels, les données | Amazon EC2, Shadow (un PC Windows distant) |
| **PaaS** (*Platform as a Service*) | une plateforme d'exécution (OS, environnement, base de données) où déployer son code | son application et ses données | Google App Engine, Heroku |
| **SaaS** (*Software as a Service*) | une application complète, utilisée dans un navigateur | ses données seulement | Google Drive, Gmail, Microsoft 365 |

Plus on va de l'IaaS vers le SaaS, moins le client a de travail d'administration, mais moins il a de contrôle.

## Modèles de déploiement (complément, hors du cours)

- **cloud public** : l'infrastructure appartient à un fournisseur et est partagée entre ses clients (AWS, Microsoft Azure, Google Cloud) ;
- **cloud privé** : infrastructure réservée à une seule organisation, chez elle ou chez un hébergeur ;
- **cloud hybride** : combinaison des deux, par exemple les données sensibles en privé et les pics de charge en public.

## Dans le cours

Le cours définit le cloud comme extension de la virtualisation, avec les exemples Shadow et Amazon EC2 ; les modèles de service et de déploiement sont des compléments de [[1 - OS]].

Notion parente : [[Environnement informatique]]. Voir aussi : [[Machine virtuelle]], [[Modèle client-serveur]], [[Système distribué]].

Résumés : [[1 - OS]]
