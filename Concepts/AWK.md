---
type: concept
aliases: [awk, AWK, commande awk, gawk]
matieres: [Operating System]
sources: ["[[Cours TP5]]"]
maj: 2026-11-05
---

Outil et langage de traitement de texte pour fichiers en lignes et colonnes. Syntaxe : `awk [-F sép] 'motif {action}' fichier`. Séparateur par défaut : l'espace ; `-F,` ou `BEGIN {FS=","}` pour une virgule ; `-F'\t'` pour une tabulation.

**Variables prédéfinies** : `$0` (ligne entière), `$1`, `$2`… (champs), `NF` (nombre de champs de la ligne), `NR` (numéro de ligne sur l'ensemble des fichiers), `FNR` (numéro de ligne dans le fichier courant, remis à zéro à chaque fichier), `FS` (séparateur d'entrée), `OFS` (séparateur de sortie).

**Blocs** : `BEGIN {…}` avant la lecture, `END {…}` après.

**Exemples du TP** : `awk '{print $2}'` (deuxième colonne) ; `{count[$4]++} END {for (p in count) print p, count[p]}` (compter les valeurs identiques) ; `$3=="Golf"` (égalité exacte) ; `$4>150` (filtre numérique) ; `/Peugeot/` (motif) ; `tolower($0) ~ /peugeot/` (insensible à la casse) ; `$6~/youtube/ || $6~/facebook/` (motif dans un champ, avec `~` plutôt que `==`).

Le sujet du TP5 mobilise aussi les blocs `BEGIN` et `END`, l'option `-F` pour le séparateur, et les fonctions `gsub` et `tolower`.

Liens : [[Redirection et tube]], [[Shell et Bash]]

Résumés : [[Cours TP5 (résumé)]], [[TP5-AWK Command (résumé)]]
