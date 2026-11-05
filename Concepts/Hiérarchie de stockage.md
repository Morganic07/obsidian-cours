---
type: concept
aliases: [storage hierarchy, storage structure, primary storage, secondary storage, tertiary storage, mémoire principale, main memory, stockage secondaire]
matieres: [Operating System]
sources: ["[[OS - chp 1]]", "[[OS - chp 2]]"]
maj: 2026-11-05
---

Les mémoires sont classées en pyramide : plus on descend, plus la capacité grandit et plus l'accès ralentit.

| Niveau | Contenu | Volatilité |
|---|---|---|
| primaire | registres, cache, mémoire principale (RAM, en DRAM) | volatile |
| secondaire | mémoire non volatile (SSD en mémoire flash), disques durs (HDD, disque magnétique) | non volatile |
| tertiaire (archivage) | disques optiques (CD, DVD, Blu-ray), bandes magnétiques (lues séquentiellement) | non volatile |

Vitesse : SSD très inférieure à RAM, très inférieure au cache. La mémoire principale est la seule à laquelle le CPU accède directement (accès aléatoire). Un programme doit donc être copié du SSD vers la RAM pour être traité ; avant d'aller en RAM, le CPU consulte ses caches.

**Interfaces du stockage secondaire** (chapitre 2) : IDE/PATA (ancien, câbles parallèles, 133 Mo/s), SATA (série, 600 Mo/s), SCSI et SAS (serveurs, SAS 12 Gbit/s), NVMe (SSD, 32 Gbit/s).

Liens : [[Système de fichiers]], [[Interruption]]

Résumé : [[OS - chp 1 (résumé)]], [[OS - chp 2 (résumé)]]
