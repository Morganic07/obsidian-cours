---
type: source
tags: [year2]
sources: ["[[raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command]] (6 pages, 9 décembre 2024, « TP-5 : AWK Command »), dans [[Operating System (matière)]]. Sujet de TP, en anglais. Le rendu est [[TP5 (résumé)]] ; les notes de cours, [[Cours TP5 (résumé)]].

## Idée générale

Présentation de [[AWK]], outil et langage de traitement de texte pour données en lignes et colonnes (journaux, CSV), puis exercices sur un fichier de constructeurs automobiles.

## Contenu du cours intégré au sujet

- **Syntaxe** : `awk 'pattern {action}' file`. Le motif est facultatif, l'action aussi (par défaut, afficher la ligne). Les champs sont `$1`, `$2`, ..., la ligne entière `$0`.
- **Variables intégrées** : `NR` (numéro de ligne), `NF` (nombre de champs), `FS` (séparateur de champs), `OFS` (séparateur de sortie).
- **Types de fichiers** : `.txt` (séparateur espace ou tabulation), `.csv` (`-F,`), `.tsv` (`-F"\t"`).
- **Exemples** : filtrer par valeur (`$1 > 2`), chercher une chaîne (`/Paris/`), recherche insensible à la casse (`tolower($0) ~ /paris/`).
- **Blocs `BEGIN` et `END`** : avant et après le traitement des lignes (en-tête, bilan).
- **Somme d'une colonne** : `{sum += $N} END{print sum}`. **Comptage d'occurrences** d'un mot avec `gsub`, ou d'un nombre avec `$0 ~ /5/ {count++}`.

## Ce qui est demandé (Tâche 1)

a. Expliquer le rôle d'AWK avec un exemple `.txt` et un exemple `.csv`. b. Citer au moins quatre séparateurs de fichiers. c. Décrire les variables intégrées avec des exemples. d. Créer `car.tsv` (ID, Manufacturer, Model, Power, au moins 10 lignes, des puissances répétées). e. Compter les enregistrements de même puissance. f. Chercher un modèle. g. Refaire les opérations de la section 1.6. h. Afficher ID, fabricant et puissance avec l'en-tête « The list of manufacturers and the car powers they produced » et la fin « The file is finished. », avec `BEGIN` et `END`.

## Liens

[[Shell et Bash]], [[Redirection et tube]].

## Points à vérifier

1. L'exemple `.tsv` utilise `awk –F"\t" '{print $1, $3}' file.csv` : le nom du fichier devrait être `file.tsv` (complément).
2. Une phrase du sujet (« The parent process should continuously append the current system time... ») est un reste du sujet du TP4, sans rapport avec AWK.
3. Les tirets des options `–F` sont des demi-cadratins dans le PDF : copiées telles quelles, les commandes ne marchent pas (complément).
