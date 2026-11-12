---
type: concept
tags: [year4]
aliases: [Gregorian calendar, réforme grégorienne, calendrier julien]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.8.c|3.8.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : le calendrier grégorien est le calendrier solaire instauré en 1582 par le pape Grégoire XIII (bulle *Inter gravissimas*) pour remplacer le calendrier julien, établi par Jules César en 46 av. J.-C. Le calendrier julien comptait une [[Année bissextile|année bissextile]] tous les 4 ans, soit une année moyenne de 365,25 jours, un peu plus longue que l'année tropique (environ 365,2422 jours) : il prenait du retard sur les saisons d'environ un jour tous les 128 ans, et l'équinoxe de printemps, qui fixe la date de Pâques, avait glissé d'une dizaine de jours depuis le concile de Nicée (325).

La réforme fait deux choses :

- elle rattrape le retard d'un coup : le jeudi 4 octobre 1582 est suivi du vendredi 15 octobre 1582 ;
- elle supprime trois années bissextiles tous les 400 ans : les années séculaires (1700, 1800, 1900) ne sont bissextiles que si elles sont divisibles par 400 (1600, 2000). L'année moyenne vaut alors $365 + \frac{97}{400} = 365{,}2425$ jours, et l'écart avec l'année tropique n'atteint plus un jour qu'au bout d'environ 3 000 ans.

Adopté aussitôt par les pays catholiques (Italie, Espagne, Portugal, France en décembre 1582), il ne l'a été qu'en 1752 en Grande-Bretagne et en 1918 en Russie, d'où l'expression « révolution d'Octobre » pour des événements de novembre 1917 dans le calendrier grégorien. C'est aujourd'hui le calendrier civil de la plupart des pays et celui de la [[Norme ISO 8601|norme ISO 8601]] des dates.

En informatique, ses irrégularités (mois de longueurs différentes, années bissextiles) rendent les calculs de dates délicats : les bibliothèques et la [[Commande date|commande `date`]] les traitent, plutôt que du code écrit à la main.

## Dans le cours

- [[tp3]] : la règle du programme 3.8 (une année est bissextile si elle est divisible par 4 sans l'être par 100, ou divisible par 400) est celle du calendrier grégorien.

Voir aussi : [[Année bissextile]], [[Norme ISO 8601]].
