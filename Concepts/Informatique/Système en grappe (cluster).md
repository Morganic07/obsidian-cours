---
type: concept
tags: [year2]
aliases: [clustered systems, clustered system, système en grappe, asymmetric clustering, symmetric clustering, hot-standby, high availability, haute disponibilité]
matieres: [Operating System]
sources: ["[[OS - chp 1]]"]
maj: 2026-11-06
---

Plusieurs ordinateurs (nœuds) qui travaillent ensemble et partagent un stockage centralisé via un [[Réseau de stockage SAN|SAN]]. **Haute disponibilité** : si un nœud tombe, le cluster continue.

- **Clustering asymétrique** : un nœud en veille active (hot-standby) attend la panne d'un autre pour prendre le relais.
- **Clustering symétrique** : tous les nœuds travaillent et se surveillent mutuellement ; en cas de panne, la charge est répartie.

Notion parente : [[Système multiprocesseur]]. Voir aussi : [[Calcul haute performance]], [[Gestionnaire de verrous distribué]].

Résumés : [[OS - chp 1 (résumé)]]
