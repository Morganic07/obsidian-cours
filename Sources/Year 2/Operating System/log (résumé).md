---
type: source
sources: ["[[Cours/Year 2/Operating System/DM/TP6/log|log (TP6)]]"]
maj: 2026-11-05
---

Résumé de [[Cours/Year 2/Operating System/DM/TP6/log|log (TP6)]], dans [[Year 2 - Operating System]]. Ce n'est pas un cours mais le fichier de données du TP6 : un journal `log.txt` à champs séparés par `|` (horodatage, utilisateur, connexion, déconnexion, durée, sites visités) pour cinq utilisateurs fictifs. Il sert à s'exercer à [[AWK]] : chercher les utilisateurs de YouTube ou Facebook sur la colonne 6.

## Points à vérifier dans le cours

1. **Données incohérentes** : trois durées ne correspondent pas aux heures (charlie : 10:00 à 10:30 pour « 2h 30m » ; diana : déconnexion avant connexion ; edward : 10:30 à 14:00 pour « 1h 30m »). Probablement voulues, sans effet sur les commandes.
2. **Domaines différents** : ce fichier écrit `technews.com` et `facebook.com`, la version recopiée dans [[Cours TP5]] `technews.org` et `facebook.org`.
