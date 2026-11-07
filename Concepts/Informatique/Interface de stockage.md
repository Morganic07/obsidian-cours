---
type: concept
tags: [year2]
aliases: [secondary storage interface, interface de disque, interfaces de stockage]
sources: ["[[2 - OS|OS - chp 2]]"]
maj: 2026-11-07
---

Méthode de connexion et de communication entre le disque et le reste de l'ordinateur. Le cours en donne un tableau, du moins au plus rapide :

| Interface | Débit selon le cours |
|---|---|
| [[IDE (PATA)]] | 133 MB/s |
| [[SCSI]] | jusqu'à 12 GB/s |
| [[SATA]] | 600 MB/s |
| [[SAS (interface de stockage)\|SAS]] | 12 Gbps |
| [[NVMe]] | 32 Gbps |

Notion parente : [[Hiérarchie de stockage]].

## Erreurs du cours

- [[2 - OS]] donne au SCSI « Up to 12GB/s » (vérifié sur l'image du tableau), plus que le SAS (« 12Gbps ») qui en est la version plus rapide ; il faut un débit inférieur à celui du SAS (complément, hors du cours : le SCSI parallèle plafonne à 640 MB/s, et 12 Gb/s est le débit du SAS). Le tableau mélange aussi les unités (MB/s, GB/s, Gbps).

Résumés : [[2 - OS]]
