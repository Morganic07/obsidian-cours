---
type: concept
tags: [year4]
aliases: [ISO 8601, format de date ISO, date au format ISO]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp2/2.7.c|2.7.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : ISO 8601 est la norme internationale de l'[[Organisation internationale de normalisation]] qui fixe la représentation écrite des dates et des heures. Publiée en 1988, elle a été révisée plusieurs fois ; la version actuelle, en deux parties, date de 2019 (ISO 8601-1 et 8601-2). Elle s'appuie sur le [[Calendrier grégorien|calendrier grégorien]] et l'horloge de 24 heures.

Formats principaux :

| Élément | Format | Exemple |
|---|---|---|
| Date | `AAAA-MM-JJ` | `2026-11-12` |
| Heure | `hh:mm:ss` | `14:30:00` |
| Date et heure | `AAAA-MM-JJThh:mm:ss` | `2026-11-12T14:30:00` |
| Instant en temps universel | suffixe `Z` | `2026-11-12T13:30:00Z` |
| Décalage horaire | `±hh:mm` | `2026-11-12T14:30:00+01:00` |
| Semaine | `AAAA-Www-J` | `2026-W46-4` |

Les éléments vont du plus grand au plus petit, avec un nombre fixe de chiffres (zéros à gauche). Conséquence très utile en informatique : le **tri alphabétique** de dates ISO est identique au **tri chronologique**. C'est pourquoi on l'emploie pour nommer des fichiers, dans les [[Fichier journal|journaux]], les formats d'échange ([[JSON]], [[Fichier CSV|CSV]]) et les [[Système de gestion de base de données|bases de données]] ; elle lève aussi l'ambiguïté entre l'ordre français `jour/mois/année` et l'ordre américain `mois/jour/année` (`03/05/2026` est le 3 mai ou le 5 mars).

En [[Langage C|C]], `printf("%04d-%02d-%02d", annee, mois, jour)` produit une date ISO : `%02d` complète par des zéros sur deux chiffres ([[Fonctions printf et scanf]]). Sous [[Linux]], `date -I` l'affiche ([[Commande date]]).

## Dans le cours

- [[tp2]] : le programme 2.7 lit et affiche une date au format français `jour/mois/année` avec `scanf("%d/%d/%d", …)` ; la fiche présente le modificateur `%02d` et le format ISO.

Voir aussi : [[Calendrier grégorien]], [[Année bissextile]], [[Organisation internationale de normalisation]].
