---
type: source
tags: [year2]
sources: ["[[Cours TP5]]"]
maj: 2026-11-05
---

Résumé de [[Cours TP5]], dans [[Operating System (matière)]]. Images lues par transcription seulement, sans ouvrir l'image de la sortie de `$4>150`.

## Contenu, dans l'ordre du cours

Travail pratique sur [[AWK]] avec `food.txt`, `food.csv`, `food2.txt` puis `car.tsv` (10 voitures) : colonnes, séparateurs (espace, tabulation, virgule, point-virgule, deux-points, barre verticale), variables `NR`, `FNR`, `NF`, `FS`, `OFS`, `$0`, comptage par valeur de puissance, filtres (égalité, `>`, motif, insensible à la casse), blocs `BEGIN` / `END`, puis recherche dans `log.txt` (séparateur `|`) des utilisateurs ayant consulté YouTube ou Facebook : `awk -F"|" '$6~/youtube/ || $6~/facebook/ {print $2}'`. Le ET se note `&&`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Sortie du filtre `$4>150`** : la ligne « 2 Ford Focus 160 » porte l'identifiant 2 alors que la Ford est le numéro 6 dans `car.tsv`. L'erreur vient soit de la transcription, soit de l'image (non rouverte). L'alerte de la transcription (colonnes décalées) est donc fondée sur ce point.
2. **Question h** demande ID, constructeur et puissance, mais la commande donnée imprime `$0` (toute la ligne, modèle compris) (complément).
3. **Exemple `OFS`** : `{OFS="/"}` est exécuté après la lecture de la première ligne ; il marche ici parce que `$0` n'est pas reconstruit, mais `BEGIN {OFS="/"}` est la forme sûre (complément).
4. **Tableau de connexions** : durées incohérentes avec les heures (charlie, diana, edward), déjà signalées par la transcription ; ce sont des données d'exemple et non une erreur de cours.
5. **Version du tableau** : les sites diffèrent d'une version à l'autre de `log.txt` (voir [[Cours/Year 2/Operating System/DM/TP6/log|log (TP6)]]).
