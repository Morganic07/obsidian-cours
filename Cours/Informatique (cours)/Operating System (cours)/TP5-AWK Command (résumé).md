---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF TP5-AWK Command ([[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]) (6 pages, 9 décembre 2024, « TP-5 : AWK Command »), dans [[Operating System (index)]]. Sujet de TP, en anglais. Le rendu est [[TP5 (résumé)]] ; les notes de cours, [[Séance TP5 (résumé)]]. La seule figure est un tableau (capture), recopié en Markdown. Aucun corrigé.

## Idée générale

Présentation de [[AWK]], outil et langage de traitement de texte pour données en lignes et colonnes (journaux, CSV), puis exercices sur un fichier de constructeurs automobiles.

## 1. La commande AWK

AWK est un outil puissant de traitement de texte et un langage de programmation disponible sous Linux / Unix. Il permet de manipuler, chercher et analyser des fichiers et des flux de texte ; on s'en sert souvent pour repérer des motifs et extraire des données.

### 1.1 Rôle

- **Traiter des données structurées** : idéal pour des données en lignes et colonnes, comme les fichiers CSV ou les journaux.
- **Manipuler du texte** : extraire, filtrer et transformer selon des motifs ou des conditions.
- **Produire des rapports** automatiquement à partir de fichiers de données.

### 1.2 Applications

- **Analyse de journaux** : extraire des messages d'erreur ou des champs précis ([[Fichier journal]]).
- **Transformation de données** : mettre en forme ou traiter de gros jeux de données.
- **Administration système** : automatiser des tâches répétitives de traitement de texte.
- **Manipulation de CSV / TSV** : traiter des fichiers délimités pour l'analyse.

### 1.3 Syntaxe de base

```bash
awk 'pattern {action}' file
```

- `pattern` : la condition (facultative ; sans elle, l'action s'applique à toutes les lignes) ;
- `{action}` : ce qu'on fait des lignes retenues (facultative ; sans elle, la ligne est affichée) ;
- l'entrée est lue ligne par ligne ; les champs sont `$1`, `$2`, … pour la 1re, 2e… colonne.

### 1.4 Variables intégrées principales

Voir [[Variables intégrées d'AWK]].

| Variable | Sens |
|---|---|
| `NR` | numéro de l'enregistrement (ligne) courant |
| `NF` | nombre de champs de l'enregistrement courant |
| `$0` | ligne entière |
| `$1`, `$2`, … | champs (colonnes) |
| `FS` | séparateur de champs (par défaut espace / tabulation) |
| `OFS` | séparateur de champs en sortie |

### 1.5 Types de fichiers

Voir [[Séparateur de champs]], [[Fichier CSV]] et [[Fichier TSV]].

**1. Fichier `.txt`** : texte brut, souvent non structuré, mais qui peut contenir des colonnes séparées par des espaces, des tabulations ou d'autres délimiteurs. Délimiteur : en général espace ou tabulation, ou personnalisé, qu'il faut alors indiquer.

```
# file.txt
1 France Paris
2 Italy Rome
3 Spain Madrid
4 Germany Berlin
5 England London
```

```bash
awk '{print $1, $3}' file.txt    # 1re et 3e colonnes → 1 Paris, 2 Rome, 3 Madrid, 4 Berlin, 5 London
```

**2. Fichier `.csv`** (*Comma-Separated Values*) : fichier structuré dont les champs sont séparés par des virgules ; courant pour les données tabulaires (tableurs). On indique `-F,`.

```
# file.csv
1,France,Paris
2,Italy,Rome
...
```

```bash
awk -F, '{print $1, $3}' file.csv    # même sortie
```

**3. Fichier `.tsv`** (*Tab-Separated Values*) : champs séparés par des tabulations ; utile quand les données contiennent des virgules, car la tabulation réduit l'ambiguïté. On indique `-F"\t"`.

```bash
awk -F"\t" '{print $1, $3}' file.tsv    # le sujet écrit file.csv, voir point à vérifier 1
```

**1.5.1 Différences** (tableau du sujet) :

| Type | Délimiteur habituel | Structure | Usage dans AWK |
|---|---|---|---|
| `.txt` | espace / tabulation (ou personnalisé) | structuré ou non | AWK par défaut, ou `-F<délimiteur>` si personnalisé |
| `.csv` | virgule (`,`) | structuré, tabulaire | `-F,` pour la virgule |
| `.tsv` | tabulation (`\t`) | structuré, tabulaire | `-F"\t"` pour la tabulation |

### 1.6 Exemples de commandes

```bash
awk -F, '$1 > 2 {print $1, $2}' file.csv      # filtrer : colonnes 1 et 2 des lignes dont la 1re valeur > 2
awk '/Paris/ {print}' file.txt                # chercher une chaîne, sensible à la casse
awk 'tolower($0) ~ /paris/ {print}' file.txt  # recherche insensible à la casse
```

Pour `tolower($0)` : `$0` est la ligne entière ; `tolower()` est une fonction intégrée qui met une chaîne en minuscules ([[Fonctions intégrées d'AWK]]) ; en convertissant toute la ligne, la recherche devient insensible à la casse. L'opérateur `~` teste la correspondance avec une [[Expression régulière]].

### 1.7 Blocs `BEGIN` et `END`

Voir [[Blocs BEGIN et END d'AWK]].

- **`BEGIN`** : exécuté avant la lecture de la première ligne ; sert à initialiser des variables, afficher un en-tête, fixer `FS`, toute préparation à faire une seule fois.

```bash
awk 'BEGIN {print "No. Country Capital"} {print}' file.txt
```

- **`END`** : exécuté après le traitement de toutes les lignes ; sert aux bilans, aux calculs finaux, à ce qui vient après les données.

```bash
awk 'BEGIN {print "No. Country Capital"} {print} END {print "The file contains the list of countries and their capitals"}' file.txt
```

### 1.8 Somme d'une colonne

```bash
awk '{sum += $N} END{print sum}' file.txt      # N = numéro de la colonne à sommer
awk -F, '{sum += $N} END{print sum}' file.csv  # pour un CSV
```

### 1.9 Compter les occurrences

D'un mot, sans tenir compte de la casse (`gsub` remplace chaque occurrence et renvoie leur nombre) :

```bash
awk '{line = tolower($0); count += gsub(/paris/, "", line)} END {print count}' file.txt
```

D'un nombre dans un CSV (compte les **lignes** qui contiennent 5) :

```bash
awk '$0 ~ /5/ {count++} END{print count}' file.csv
```

## Tâche 1

- a. Quel est le rôle de la commande AWK dans les systèmes de type Unix ? L'expliquer avec deux exemples, l'un sur un `.txt`, l'autre sur un `.csv`.
- b. Quels délimiteurs séparent les données dans un fichier ? Au moins quatre exemples.
- c. Quelles sont les principales variables intégrées d'AWK ? Les expliquer avec exemples et commandes.
- d. Créer `car.tsv` de constructeurs automobiles avec les colonnes ID, Manufacturer, Model, Power ; au moins 10 enregistrements, plusieurs avec la même puissance.
- e. Écrire une commande AWK qui compte les enregistrements de même puissance.
- f. Écrire une commande AWK qui trouve les enregistrements d'un modèle donné.
- g. Refaire sur `car.tsv` toutes les opérations de la section 1.6.
- h. Afficher ID, Manufacturer et Power ; en-tête *« The list of manufacturers and the car powers they produced »* au début, message *« The file is finished. »* à la fin, avec les blocs `BEGIN` et `END` (section 1.7).

Réponses de l'étudiante : [[TP5 (résumé)]].

## Liens

[[Shell et Bash]], [[Redirection et tube]].

## Points à vérifier

1. L'exemple `.tsv` utilise `awk –F"\t" '{print $1, $3}' file.csv` : le nom du fichier devrait être `file.tsv` (complément).
2. Une phrase du sujet (« The parent process should continuously append the current system time... ») est un reste du sujet du TP4, sans rapport avec AWK.
3. Les tirets des options `–F` sont des demi-cadratins dans le PDF : copiées telles quelles, les commandes ne marchent pas (complément). Les apostrophes `‘ ’` et guillemets `”` typographiques posent le même problème ; elles sont réécrites ici en caractères droits.
4. **Section 1.9, comptage d'un nombre** : `$0 ~ /5/ {count++}` compte les lignes qui contiennent un 5, pas le nombre d'occurrences (une ligne avec deux 5 compte une fois) ; et le motif trouve aussi 15, 50… (complément).
5. **Section 1.4** : `FS` « par défaut espace / tabulation » ; plus exactement, par défaut AWK découpe sur toute suite de blancs (complément).
