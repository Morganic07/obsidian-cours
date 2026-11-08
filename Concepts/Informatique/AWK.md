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
  - "[[5 - TP5|Cours TP5]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5]]"
  - "[[Raw/Year 2/Operating System/DM/TP6/log.docx|log (TP6)]]"
  - "[[Raw/Year 2/Operating System/Cours OS/Cours TP5.docx|Cours TP5]]"
maj: 2026-11-08
---

Outil et langage de traitement de texte pour fichiers en lignes et colonnes. Syntaxe : `awk [-F sép] 'motif {action}' fichier`. Séparateur par défaut : l'espace ; `-F,` ou `BEGIN {FS=","}` pour une virgule ; `-F'\t'` pour une tabulation.

**Variables prédéfinies** : `$0` (ligne entière), `$1`, `$2`… (champs), `NF` (nombre de champs de la ligne), `NR` (numéro de ligne sur l'ensemble des fichiers), `FNR` (numéro de ligne dans le fichier courant, remis à zéro à chaque fichier), `FS` (séparateur d'entrée), `OFS` (séparateur de sortie).

**Blocs** : `BEGIN {…}` avant la lecture, `END {…}` après.

**Exemples du TP** : `awk '{print $2}'` (deuxième colonne) ; `{count[$4]++} END {for (p in count) print p, count[p]}` (compter les valeurs identiques) ; `$3=="Golf"` (égalité exacte) ; `$4>150` (filtre numérique) ; `/Peugeot/` (motif) ; `tolower($0) ~ /peugeot/` (insensible à la casse) ; `$6~/youtube/ || $6~/facebook/` (motif dans un champ, avec `~` plutôt que `==`).

Le sujet du TP5 mobilise aussi les blocs `BEGIN` et `END`, l'option `-F` pour le séparateur, et les fonctions `gsub` et `tolower`.

Dans `awk 'pattern {action}' file`, le motif est facultatif (sinon toutes les lignes sont traitées) et l'action aussi (sinon la ligne est affichée). Usages cités : analyse de journaux, transformation de données, administration, fichiers [[Fichier CSV|CSV]] et [[Fichier TSV|TSV]]. Somme d'une colonne : `{sum += $N} END {print sum}`.

## Compléments (hors du cours)

- **Nom** : formé des initiales de ses trois auteurs, Alfred Aho, Peter Weinberger et Brian Kernighan (Bell Labs, 1977).
- **Séparateur par défaut** : plus précisément une suite de blancs (espaces ou tabulations), les blancs en début et fin de ligne étant ignorés. `FS` peut aussi être une expression régulière : `-F'[,;]'` coupe sur la virgule ou le point-virgule.
- **Autres variables** : `$NF` désigne le dernier champ (puisque `NF` en est le numéro), `ORS` le séparateur d'enregistrements en sortie (saut de ligne par défaut), `FILENAME` le nom du fichier en cours de lecture.
- **`OFS`** ne s'insère qu'entre les arguments séparés par une virgule dans `print` : `print $1, $2` utilise `OFS`, `print $1 $2` colle les deux champs.
- **`printf`** formate comme en C : `printf "%-10s %5.1f\n", $1, $4`.
- **Motifs** : `/motif/` seul équivaut à `$0 ~ /motif/`. Une comparaison est numérique si les deux opérandes ressemblent à des nombres, sinon elle compare des chaînes.
- **Tableaux** : ils sont associatifs, indexés par des chaînes quelconques, ce qui permet le comptage `count[$4]++` (voir [[Table de hachage]]).

Liens : [[Variables intégrées d'AWK]], [[Blocs BEGIN et END d'AWK]], [[Fonctions intégrées d'AWK]], [[Séparateur de champs]], [[Expression régulière]], [[Redirection et tube]], [[Shell et Bash]]

**Sujet du TP5** : `awk -F, '{print $1, $3}'` affiche la première et la troisième colonne d'un fichier CSV (tiret simple et apostrophes droites, sans quoi la commande échoue). [[Erreurs du cours#^e-awk|✎]]

Résumés : [[5 - TP5]]
