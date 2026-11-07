---
type: concept
tags:
  - year2
aliases:
  - awk
  - AWK
  - commande awk
  - gawk
matieres:
  - Operating System
sources:
  - "[[5 - TP5 (résumé)|Cours TP5]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5]]"
  - "[[Raw/Year 2/Operating System/DM/TP6/log.docx|log (TP6)]]"
maj: 2026-11-06
---

Outil et langage de traitement de texte pour fichiers en lignes et colonnes. Syntaxe : `awk [-F sép] 'motif {action}' fichier`. Séparateur par défaut : l'espace ; `-F,` ou `BEGIN {FS=","}` pour une virgule ; `-F'\t'` pour une tabulation.

**Variables prédéfinies** : `$0` (ligne entière), `$1`, `$2`… (champs), `NF` (nombre de champs de la ligne), `NR` (numéro de ligne sur l'ensemble des fichiers), `FNR` (numéro de ligne dans le fichier courant, remis à zéro à chaque fichier), `FS` (séparateur d'entrée), `OFS` (séparateur de sortie).

**Blocs** : `BEGIN {…}` avant la lecture, `END {…}` après.

**Exemples du TP** : `awk '{print $2}'` (deuxième colonne) ; `{count[$4]++} END {for (p in count) print p, count[p]}` (compter les valeurs identiques) ; `$3=="Golf"` (égalité exacte) ; `$4>150` (filtre numérique) ; `/Peugeot/` (motif) ; `tolower($0) ~ /peugeot/` (insensible à la casse) ; `$6~/youtube/ || $6~/facebook/` (motif dans un champ, avec `~` plutôt que `==`).

Le sujet du TP5 mobilise aussi les blocs `BEGIN` et `END`, l'option `-F` pour le séparateur, et les fonctions `gsub` et `tolower`.

Dans `awk 'pattern {action}' file`, le motif est facultatif (sinon toutes les lignes sont traitées) et l'action aussi (sinon la ligne est affichée). Usages cités : analyse de journaux, transformation de données, administration, fichiers [[Fichier CSV|CSV]] et [[Fichier TSV|TSV]]. Somme d'une colonne : `{sum += $N} END {print sum}`.

Liens : [[Variables intégrées d'AWK]], [[Blocs BEGIN et END d'AWK]], [[Fonctions intégrées d'AWK]], [[Séparateur de champs]], [[Expression régulière]], [[Redirection et tube]], [[Shell et Bash]]

## À vérifier

- Le sujet [[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5]] contient une phrase égarée du TP4 et des tirets demi-cadratins dans `–F` (signalés par le résumé).

Résumés : [[5 - TP5 (résumé)]]
