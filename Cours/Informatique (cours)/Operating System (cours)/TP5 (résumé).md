---
type: source
tags:
  - year2
sources:
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5 (DM)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5 (DM)]], dans [[Operating System (index)]]. C'est la version rendue du TP5 (Task 1, questions a à h) : même contenu que [[Séance TP5 (résumé)|Cours TP5]] (voir [[Séance TP5 (résumé)]]), avec en plus le tableau des variables prédéfinies d'AWK issu de la page de manuel, mais sans la partie sur `log.txt`. Le TP apprend à manipuler des fichiers en colonnes avec [[AWK]]. Réponses de l'étudiante, captures du terminal intégrées.

## a. À quoi sert AWK ?

*Question* : quel est le rôle de la commande AWK sous les systèmes de type Unix ? Deux exemples, l'un avec un fichier `.txt`, l'autre avec un [[Fichier CSV|.csv]].

*Réponse* : AWK est un outil de traitement de texte et un langage de programmation disponible sous [[Linux]] / Unix ; il sert à manipuler, chercher et analyser des fichiers texte structurés en lignes et colonnes. L'étudiante crée `food.txt` et `food.csv`.

![[TP5 - image2.png]]
*Figure : `cat food.txt` : steak 2.50, lettuce 1.00, bun 1.50, tomato 0.90.*

```bash
awk '{print $2}' food.txt    # 2e colonne (prix) ; séparateur par défaut : l'espace
```

![[TP5 - image1.png]]
*Figure : 2.50, 1.00, 1.50, 0.90.*

![[TP5 - image9.png]]
*Figure : `cat food.csv` : bread,1.00 ; pasta,1.20 ; sauce,1.90 ; cheese,2.30.*

```bash
awk -F, '{print $1,$2}' food.csv    # -F, : le séparateur est la virgule
```

![[TP5 - image5.png]]
*Figure : bread 1.00, pasta 1.20, sauce 1.90, cheese 2.30.*

## b. Les séparateurs

Au moins quatre ([[Séparateur de champs]]) : espace (`.txt`), tabulation (`.tsv`, [[Fichier TSV]]), virgule (`.csv`), point-virgule (`.txt` ou `.csv`) ; aussi les deux-points et la barre verticale.

## c. Les variables intégrées d'AWK

On peut ouvrir le manuel d'AWK à la section *Builtin-variables* ([[Variables intégrées d'AWK]]). Ces variables sont prédéfinies et initialisées avant l'exécution du programme :

| Variable | Description (manuel) |
|---|---|
| `ARGC` | nombre d'arguments de la ligne de commande |
| `ARGV` | [[Tableau (programmation)\|tableau]] des arguments, indices 0 à ARGC-1 |
| `CONVFMT` | format de conversion interne des nombres en chaînes, initialement `"%.6g"` |
| `ENVIRON` | tableau indexé par les variables d'environnement : `var=value` est stocké comme `ENVIRON[var] = value` |
| `FILENAME` | nom du fichier d'entrée courant |
| `FNR` | numéro d'enregistrement courant dans FILENAME |
| `FS` | découpe les enregistrements en champs, comme une [[Expression régulière]] |
| `NF` | nombre de champs de l'enregistrement courant |
| `NR` | numéro d'enregistrement courant dans tout le flux d'entrée |
| `OFMT` | format d'affichage des nombres, initialement `"%.6g"` |
| `OFS` | inséré entre les champs en sortie, initialement `" "` |
| `ORS` | termine chaque enregistrement en sortie, initialement `"\n"` |
| `RLENGTH` | longueur fixée par le dernier appel à `match()` |
| `RS` | séparateur d'enregistrements en entrée, initialement `"\n"` |
| `RSTART` | indice fixé par le dernier appel à `match()` |
| `SUBSEP` | sert à construire des indices de tableau multiples, initialement `"\034"` |

Les plus importantes, avec exemples :

**FNR** : numéro de ligne dans le fichier en cours, repart à zéro à chaque nouveau fichier.

```bash
awk '{print FNR}' food.txt food.csv
```

![[TP5 - image20.png]]
*Figure : 1 à 4, puis de nouveau 1 à 4.*

**NR** : numéro de la ligne courante, incrémenté à chaque ligne lue dans les fichiers ou l'entrée standard.

```bash
awk '{print NR}' food.txt food.csv
```

![[TP5 - image27.png]]
*Figure : 1 à 8.*

**NF** : nombre de champs de la ligne courante.

![[TP5 - image16.png]]
*Figure : `cat food2.txt` : « bread complete 1.20 », « sauce tomato 1.30 », « cereals 1.20 », « water ».*

```bash
awk '{print NF}' food2.txt
```

![[TP5 - image18.png]]
*Figure : 3, 3, 2, 1.*

**FS** : séparateur des données en entrée (espace par défaut).

```bash
awk 'BEGIN {FS=","} {print $1, $2}' food.csv
awk -F, '{print $1, $2}' food.csv      # équivalent, plus rapide
```

![[TP5 - image25.png]]
*Figure : même sortie pour les deux commandes.*

**OFS** : séparateur utilisé à l'affichage.

```bash
awk -F, '{OFS="/"} {print $1, $2}' food.csv
```

![[TP5 - image26.png]]
*Figure : bread/1.00, pasta/1.20, sauce/1.90, cheese/2.30.*

**$0** : la ligne complète ; combiné avec `NR` pour afficher la 2e ligne.

```bash
awk 'NR==2 {print $0}' food.txt
```

![[TP5 - image4.png]]
*Figure : `food.txt` à trois lignes, puis « Carrot rapee cru Leclerc 1.20 ».*

## d. Le fichier `car.tsv`

*Consigne* : colonnes ID, Manufacturer, Model, Power ; au moins 10 enregistrements, plusieurs de même puissance.

![[TP5 - image10.png]]
*Figure : `cat car.tsv`.*

| ID | Constructeur | Modèle | Puissance |
|---|---|---|---|
| 1 | Peugeot | 308 | 165 |
| 2 | Renault | Clio | 100 |
| 3 | Peugeot | 208 | 130 |
| 4 | Citroën | C3 | 120 |
| 5 | Renault | Mégane | 100 |
| 6 | Ford | Focus | 160 |
| 7 | BMW | X5 | 335 |
| 8 | Audi | Q5 | 249 |
| 9 | VW | Golf | 120 |
| 10 | Peugeot | 5008 | 165 |

## e. Compter les enregistrements de même puissance

```bash
awk -F'\t' '{count[$4]++} END {for (power in count) print power, count[power]}' car.tsv
```

`count[$4]++` incrémente un compteur par valeur de la 4e colonne ; une fois le fichier lu, le bloc `END` ([[Blocs BEGIN et END d'AWK]]) parcourt avec une [[Boucle (programmation)|boucle for]] chaque valeur (`power`) et affiche son nombre (`count[power]`).

![[TP5 - image11.png]]
*Figure : 100 → 2, 335 → 1, 160 → 1, 120 → 2, 165 → 2, 130 → 1, 249 → 1.*

## f. Trouver un modèle donné

```bash
awk -F'\t' '$3=="Golf" {print $0}' car.tsv
```

`$3=="car_model"` garde les lignes dont le 3e champ est exactement ce modèle ; `{print $0}` les affiche entières.

![[TP5 - image6.png]]
*Figure : `9 VW Golf 120`.*

## g. Opérations de la section 1.6

**Filtrer sur une valeur de colonne** (puissance > 150) :

```bash
awk -F'\t' '$4>150 {print $0}' car.tsv
```

![[TP5 - image3.png]]
*Figure : 1 Peugeot 308 165 ; 6 Ford Focus 160 ; 7 BMW X5 335 ; 8 Audi Q5 249 ; 10 Peugeot 5008 165.*

**Chercher une chaîne, sensible à la casse** (les Peugeot) :

```bash
awk -F'\t' '/Peugeot/ {print $0}' car.tsv
```

![[TP5 - image8.png]]
*Figure : lignes 1, 3 et 10.*

**Recherche insensible à la casse** : `tolower($0)` ([[Fonctions intégrées d'AWK]]) met la ligne en minuscules avant la comparaison avec `~`.

```bash
awk -F'\t' 'tolower($0) ~ /peugeot/ {print $0}' car.tsv
```

![[TP5 - image12.png]]
*Figure : mêmes trois Peugeot.*

## h. En-tête et fin avec `BEGIN` / `END`

*Consigne* : afficher ID, constructeur et puissance ; en-tête *« The list of manufacturers and the car powers they produced »* ; à la fin *« The file is finished. »* (section 1.7).

```bash
awk -F'\t' 'BEGIN {print "The list of manufacturers and the car powers they produced"} {print $0} END {print "The file is finished."}' car.tsv
```

`BEGIN` affiche l'en-tête avant la lecture, `print $0` chaque ligne, `END` le message final.

![[TP5 - image7.png]]
*Figure : l'en-tête, les dix lignes, puis « The file is finished. ».*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Même incohérence que dans [[Séance TP5 (résumé)]]** : la ligne « 2 Ford Focus 160 » de la sortie de `$4>150` devrait porter l'identifiant 6. **Vérifié sur l'image** : la capture affiche bien « 6 Ford Focus 160 » ; l'erreur venait de la transcription, l'image fait foi.
2. **Question h** : demande ID, constructeur, puissance mais la commande affiche toute la ligne (complément).
3. **Tableau des connexions** : les durées ne correspondent pas aux heures (déjà signalé par la transcription), sans effet sur la commande.
4. **Exemple `OFS`** : `{OFS="/"}` placé hors de `BEGIN` ne s'applique qu'après la lecture de la première ligne ; `BEGIN {OFS="/"}` est la forme sûre (complément).
5. **Apostrophe typographique** dans la capture de la question h (`-F’\t’`, signalée par la transcription) ; le texte de la note a des apostrophes droites.
