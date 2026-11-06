---
type: source
tags: [year2]
sources: ["[[Cours TP5]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Cours TP5]], dans [[Operating System (matière)]]. Travail pratique sur [[AWK]] : réponses de l'étudiante aux questions a à h, avec ses essais dans le terminal (captures intégrées), puis la recherche par motif dans `log.txt`. Les questions de l'énoncé, en captures de texte, sont recopiées.

## a. Qu'est-ce qu'AWK ?

AWK est un outil de traitement de texte et un langage de programmation disponible sous [[Linux]] / Unix. Il sert à manipuler, chercher et analyser des fichiers texte structurés en lignes et en colonnes.

Exemple avec un fichier texte :

![[Séance TP5 - image2.png]]
*Figure : `cat food.txt` : steak 2.50, lettuce 1.00, bun 1.50, tomato 0.90.*

```bash
awk '{print $2}' food.txt
```

affiche la deuxième colonne (`$2`), les prix. Pas de séparateur précisé : par défaut, c'est l'espace.

![[Séance TP5 - image6.png]]
*Figure : sortie : 2.50, 1.00, 1.50, 0.90.*

Avec un [[Fichier CSV]] :

![[Séance TP5 - image19.png]]
*Figure : `cat food.csv` : bread,1.00 ; pasta,1.20 ; sauce,1.90 ; cheese,2.30.*

```bash
awk -F, '{print $1,$2}' food.csv
```

affiche les colonnes 1 et 2 en précisant le séparateur virgule avec l'option `-F,`.

![[Séance TP5 - image5.png]]
*Figure : sortie : bread 1.00, pasta 1.20, sauce 1.90, cheese 2.30 (séparées par un espace).*

## b. Les séparateurs

*Question* : quels séparateurs (*delimiters*) sépare les données d'un fichier ? Donner au moins quatre exemples.

*Réponse* ([[Séparateur de champs]]) : l'espace (fichiers `.txt`), la tabulation (fichiers `.tsv`, voir [[Fichier TSV]]), la virgule (`.csv`), le point-virgule (`.txt` ou `.csv`) ; on peut aussi citer les deux-points et la barre verticale (*pipe*).

## c. Les variables intégrées d'AWK

*Question* : quelles sont les principales variables intégrées (*built-in variables*) d'AWK ? Les expliquer avec exemples et commandes. Voir [[Variables intégrées d'AWK]].

| Variable | Sens |
|---|---|
| `FNR` | numéro de ligne dans le fichier en cours ; repart à zéro à chaque nouveau fichier |
| `NR` | numéro de la ligne courante dans l'ensemble des données ; s'incrémente à chaque ligne, même sur plusieurs fichiers |
| `NF` | nombre de champs (colonnes) de la ligne courante |
| `FS` | séparateur des données en entrée ; par défaut l'espace |
| `OFS` | séparateur utilisé par AWK pour afficher |
| `$0` | la ligne complète |

**FNR** :

```bash
awk '{print FNR}' food.txt food.csv
```

![[Séance TP5 - image9.png]]
*Figure : 1, 2, 3, 4 puis de nouveau 1, 2, 3, 4 : la numérotation repart pour le second fichier.*

**NR** :

```bash
awk '{print NR}' food.txt food.csv
```

![[Séance TP5 - image26.png]]
*Figure : 1 à 8 : la numérotation continue d'un fichier à l'autre.*

**NF**, sur un fichier dont les lignes n'ont pas le même nombre de colonnes :

![[Séance TP5 - image25.png]]
*Figure : `cat food2.txt` : « bread complete 1.20 », « sauce tomato 1.30 », « cereals 1.20 », « water ».*

```bash
awk '{print NF}' food2.txt
```

![[Séance TP5 - image8.png]]
*Figure : 3, 3, 2, 1 champs.*

**FS** : dans `food.csv` les données sont séparées par des virgules ; il faut l'indiquer à AWK. Deux écritures équivalentes :

```bash
awk 'BEGIN {FS=","} {print $1, $2}' food.csv
awk -F, '{print $1, $2}' food.csv     # plus rapide
```

![[Séance TP5 - image16.png]]
*Figure : les deux commandes donnent la même sortie (bread 1.00 … cheese 2.30).*

**OFS** : afficher les données séparées par `/` au lieu d'un espace.

```bash
awk -F, '{OFS="/"} {print $1, $2}' food.csv
```

![[Séance TP5 - image23.png]]
*Figure : bread/1.00, pasta/1.20, sauce/1.90, cheese/2.30.*

**$0** : afficher la 2e ligne complète en combinant `NR` et `$0`.

```bash
awk 'NR==2 {print $0}' food.txt
```

![[Séance TP5 - image3.png]]
*Figure : `food.txt` (salami 4.0 ; Carrot rapee cru Leclerc 1.20 ; steak 2.50), puis la 2e ligne seule : « Carrot rapee cru Leclerc 1.20 ».*

## d. Créer `car.tsv`

*Consigne* : créer un fichier `car.tsv` de constructeurs automobiles avec les colonnes ID, Manufacturer, Model, Power ; au moins 10 enregistrements, dont plusieurs avec la même puissance.

![[Séance TP5 - image14.png]]
*Figure : `cat car.tsv` : les dix voitures ci-dessous.*

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

- `count[$4]++` lit la 4e colonne (puissance) et incrémente un compteur par valeur (tableau associatif).
- Une fois le fichier lu, le bloc `END` s'exécute ([[Blocs BEGIN et END d'AWK]]).
- La [[Boucle (programmation)|boucle for]] parcourt chaque valeur distincte (variable `power`) et affiche la valeur avec son nombre (`count[power]`).

![[Séance TP5 - image22.png]]
*Figure : 100 → 2, 335 → 1, 160 → 1, 120 → 2, 165 → 2, 130 → 1, 249 → 1 (ordre non trié).*

## f. Trouver un modèle donné

```bash
awk -F'\t' '$3=="Golf" {print $0}' car.tsv
```

`$3=="car_model"` garde les lignes dont le 3e champ vaut exactement le modèle ; `{print $0}` affiche la ligne entière.

![[Séance TP5 - image7.png]]
*Figure : résultat : `9 VW Golf 120`.*

## g. Opérations de la section 1.6 sur `car.tsv`

**Filtrer sur la valeur d'une colonne** : voitures de puissance > 150.

```bash
awk -F'\t' '$4>150 {print $0}' car.tsv
```

`$4 > 150` ne garde que les lignes dont la 4e colonne dépasse 150 ; `{print $0}` les affiche en entier.

![[Séance TP5 - image15.png]]
*Figure : résultat : 1 Peugeot 308 165 ; 6 Ford Focus 160 ; 7 BMW X5 335 ; 8 Audi Q5 249 ; 10 Peugeot 5008 165.*

**Chercher une chaîne (sensible à la casse)** : toutes les Peugeot.

```bash
awk -F'\t' '/Peugeot/ {print $0}' car.tsv
```

![[Séance TP5 - image12.png]]
*Figure : 1 Peugeot 308 165 ; 3 Peugeot 208 130 ; 10 Peugeot 5008 165.*

**Recherche insensible à la casse** : si le fichier contenait des noms en majuscules et en minuscules, on convertit chaque ligne en minuscules avec `tolower` ([[Fonctions intégrées d'AWK]]) avant de comparer.

```bash
awk -F'\t' 'tolower($0) ~ /peugeot/ {print $0}' car.tsv
```

![[Séance TP5 - image11.png]]
*Figure : même résultat que la recherche sensible à la casse (trois Peugeot).*

## h. En-tête et message de fin avec `BEGIN` et `END`

*Consigne* : afficher ID, constructeur et puissance ; en tête, la phrase *« The list of manufacturers and the car powers they produced »* ; à la fin, *« The file is finished. »* ; utiliser `BEGIN` et `END` (section 1.7).

```bash
awk -F'\t' 'BEGIN {print "The list of manufacturers and the car powers they produced"} {print $0} END {print "The file is finished."}' car.tsv
```

`BEGIN` affiche l'en-tête avant la lecture du fichier, `print $0` affiche chaque ligne, `END` affiche le message final.

![[Séance TP5 - image1.png]]
*Figure : l'en-tête, les dix lignes de `car.tsv`, puis « The file is finished. ».*

## Recherche par motif dans une chaîne (*pattern-based search*)

Fichier `log.txt` : journal de connexions (voir [[Fichier journal]]).

| Timestamp | Username | Login Time | Logout Time | Duration | Web Activity |
|---|---|---|---|---|---|
| 2024-10-31 08:00:00 | alice | 2024-10-31 08:00 | 2024-10-31 10:15 | 2h 15m | youtube.com, technews.com |
| 2024-10-31 09:30:00 | bob | 2024-10-31 09:30 | 2024-10-31 11:00 | 1h 30m | opensource.org, linux.org |
| 2024-10-31 10:00:00 | charlie | 2024-10-31 10:00 | 2024-10-31 10:30 | 2h 30m | youtube.com, facebook.com |
| 2024-10-31 11:45:00 | diana | 2024-10-31 11:45 | 2024-10-31 10:45 | 1h 00m | researchgate.net, youtube.com |
| 2024-10-31 10:30:00 | edward | 2024-10-31 10:30 | 2024-10-31 14:00 | 1h 30m | github.com, docs.python.org |

*Objectif* : trouver les utilisateurs qui ont consulté youtube.com et facebook.com.

Raisonnement :
1. dans `log.txt`, le séparateur des champs est la barre verticale `|` ;
2. la colonne utile est la 6e (*Web Activity*) ;
3. le texte est en minuscules : pas besoin de recherche insensible à la casse ;
4. la forme de la question f (`$3=="Golf"`) ne marche pas ici : les sites sont séparés par des virgules dans un même champ, et `==` exige une correspondance littérale du champ entier ;
5. pour chercher un motif **à l'intérieur** d'une chaîne, on utilise l'opérateur `~` et on met le motif entre deux `/` ([[Expression régulière]]).

```bash
awk -F"|" '$6~/youtube/ || $6~/facebook/ {print $2}' log.txt
```

`||` signifie « OU » ; pour les utilisateurs ayant consulté YouTube **et** Facebook, on écrirait `&&` ([[Opérateur logique]]).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Sortie du filtre `$4>150`** : la transcription donnait « 2 Ford Focus 160 » alors que la Ford est le numéro 6 dans `car.tsv`. **Vérifié sur l'image** : la capture affiche bien « 6 Ford Focus 160 » ; l'erreur venait de la transcription, l'image fait foi. L'alerte de la transcription sur les colonnes décalées est une fausse alerte (tabulations).
2. **Question h** demande ID, constructeur et puissance, mais la commande donnée imprime `$0` (toute la ligne, modèle compris) (complément).
3. **Exemple `OFS`** : `{OFS="/"}` est exécuté après la lecture de la première ligne ; il marche ici parce que `$0` n'est pas reconstruit, mais `BEGIN {OFS="/"}` est la forme sûre (complément).
4. **Tableau de connexions** : durées incohérentes avec les heures (charlie, diana, edward), déjà signalées par la transcription ; ce sont des données d'exemple et non une erreur de cours.
5. **Version du tableau** : les sites diffèrent d'une version à l'autre de `log.txt` (voir [[Cours/Year 2/Operating System/DM/TP6/log|log (TP6)]]).
6. **Séparateur `-F"|"`** : le tableau affiché est une mise en forme ; dans le fichier, les champs sont séparés par `|`, éventuellement entourés d'espaces, ce qui laisserait des espaces dans `$2` (complément, à vérifier sur le fichier).
7. **« youtube.com and facebook.com »** : la transcription lisait `facebook.org` (et `technews.org`) ; **vérifié sur l'image** : la capture affiche `facebook.com` et `technews.com`, comme la question.
8. **Question h, apostrophe typographique** : la capture montrait `-F’\t’` selon la transcription ; le texte de la note a des apostrophes droites.
