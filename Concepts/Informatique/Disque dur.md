---
type: concept
tags: [year2]
aliases: [HDD, hard disk drive, hard-disk drive, hard drive, disques durs]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[2 - OS|OS - chp 2]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un disque dur (HDD) est un support de stockage non volatil qui enregistre les données magnétiquement sur des plateaux en rotation, lus et écrits par des têtes montées sur un bras mobile.

Disque magnétique qui tourne en moyenne à 7 200 tr/min ; une tête lit et écrit des points magnétiques (un point vaut 1, son absence 0). Le cours affirme que le HDD est plus fiable que le [[SSD]], car un disque abîmé reste lisible.

## Fonctionnement (complément, hors du cours)

- **Codage des bits** : chaque bit est une petite zone de la couche magnétique aimantée dans un sens ou dans l'autre ; c'est plus exactement le sens de l'aimantation (et ses inversions), et non la présence ou l'absence d'un point, qui code l'information. La tête flotte sur un coussin d'air à quelques nanomètres du plateau, sans le toucher ; un contact (« crash de tête ») raye la surface.
- **Organisation** : chaque face de plateau est divisée en **pistes** concentriques, elles-mêmes découpées en **secteurs**, la plus petite unité lue ou écrite (512 octets, ou 4 096 octets sur les disques récents dits « Advanced Format ») ; l'ensemble des pistes de même rayon sur tous les plateaux forme un **cylindre**.
- **Temps d'accès** : $t_{\text{accès}} = t_{\text{recherche}} + t_{\text{latence}} + t_{\text{transfert}}$, où le temps de recherche (seek time, quelques ms) amène la tête sur la bonne piste et la latence rotationnelle attend que le secteur passe sous la tête. À 7 200 tr/min, un tour dure $60/7\,200 \approx 8{,}33$ ms, d'où une latence moyenne d'un demi-tour, $\approx 4{,}17$ ms. C'est ce délai mécanique qui rend le HDD bien plus lent qu'un SSD en accès aléatoire.
- **Fiabilité comparée** : le HDD, mécanique, craint surtout les chocs (surtout en marche), l'usure des moteurs et les [[Secteur défectueux|secteurs défectueux]] ; le SSD n'a pas de pièce mobile mais ses cellules de mémoire flash supportent un nombre limité d'écritures, ce que le contrôleur compense en répartissant les écritures (wear leveling), et une panne du contrôleur peut rendre toutes les données inaccessibles d'un coup. Les deux types de disque exposent des indicateurs d'état **S.M.A.R.T.** (Self-Monitoring, Analysis and Reporting Technology), lisibles sous Linux avec `smartctl` (paquet smartmontools), pour anticiper une panne.

Notion parente : [[Hiérarchie de stockage]]. Voir aussi : [[Partition (disque)]], [[Interface de stockage]], [[Secteur défectueux]], [[Mémoire volatile et non volatile]].

Résumés : [[1 - OS]], [[2 - OS]]
