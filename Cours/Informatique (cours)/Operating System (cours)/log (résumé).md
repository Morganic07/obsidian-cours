---
type: source
tags:
  - year2
sources:
  - "[[Raw/Year 2/Operating System/DM/TP6/log.docx|log (TP6)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/DM/TP6/log.docx|log (TP6)]], dans [[Operating System (index)]]. Ce n'est pas un cours mais le fichier de données du TP6 : un journal `log.txt` ([[Fichier journal]]) à champs séparés par `|` (horodatage, utilisateur, connexion, déconnexion, durée, sites visités) pour cinq utilisateurs fictifs. Il sert à s'exercer à [[AWK]] : chercher les utilisateurs de YouTube ou Facebook sur la colonne 6. Voir l'énoncé dans [[TP6-Assignment (résumé)]] et la méthode dans [[Séance TP5 (résumé)]].

## Contenu du fichier

Ligne d'en-tête, puis une ligne de tirets, puis cinq enregistrements :

```
Timestamp | Username| Login Time | Logout Time | Duration | Web Activity
---------------------------------------------------------------------------------------------------------------
2024-10-31 08:00:00 | alice | 2024-10-31 08:00 | 2024-10-31 10:15 | 2h 15m | youtube.com, technews.com
2024-10-31 09:30:00 | bob | 2024-10-31 09:30 | 2024-10-31 11:00 | 1h 30m | opensource.org, linux.org
2024-10-31 10:00:00 | charlie | 2024-10-31 10:00 | 2024-10-31 10:30 | 2h 30m | youtube.com, facebook.com
2024-10-31 11:45:00 | diana | 2024-10-31 11:45 | 2024-10-31 10:45 | 1h 00m | researchgate.net, youtube.com
2024-10-31 10:30:00 | edward | 2024-10-31 10:30 | 2024-10-31 14:00 | 1h 30m | github.com, docs.python.org
```

| N° | Champ | Exemple |
|---|---|---|
| 1 | *Timestamp* | 2024-10-31 08:00:00 |
| 2 | *Username* | alice |
| 3 | *Login Time* | 2024-10-31 08:00 |
| 4 | *Logout Time* | 2024-10-31 10:15 |
| 5 | *Duration* | 2h 15m |
| 6 | *Web Activity* | youtube.com, technews.com |

## Usage dans le TP

La commande proposée dans [[Séance TP5 (résumé)]] :

```bash
awk -F"|" '$6~/youtube/ || $6~/facebook/ {print $2}' log.txt
```

donnerait alice, charlie et diana (YouTube ou Facebook) ; avec `&&` au lieu de `||`, seulement charlie (complément : résultat déduit des données, non montré dans le fichier).

## Points à vérifier dans le cours

1. **Données incohérentes** : trois durées ne correspondent pas aux heures (charlie : 10:00 à 10:30 pour « 2h 30m » ; diana : déconnexion avant connexion ; edward : 10:30 à 14:00 pour « 1h 30m »). Probablement voulues, sans effet sur les commandes.
2. **Mêmes domaines** : ce fichier écrit `technews.com` et `facebook.com`, comme la capture de [[Séance TP5 (résumé)|Cours TP5]] (sa transcription automatique lisait `technews.org` et `facebook.org` ; l'image fait foi).
3. **En-tête et ligne de tirets** : ils sont traités par AWK comme des enregistrements ; l'en-tête ne contient ni « youtube » ni « facebook », donc sans effet ici (complément).
