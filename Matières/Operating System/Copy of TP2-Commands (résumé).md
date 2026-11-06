---
type: source
tags: [year2]
sources: [".raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf"]
maj: 2026-11-06
---

Résumé du PDF Copy of TP2-Commands (`.raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf`) (6 pages, 18 novembre 2024, cours « UNIX Commands »), dans [[Operating System (matière)]]. Sujet de TP, en anglais. Le rendu correspondant est [[TP2 (résumé)]] ; les notes de cours, [[Séance TP2 (résumé)]].

## Ce qui est demandé

Le sujet présente les méta-caractères du shell, avec un rappel de cours puis une tâche (avec capture d'écran avant et après chaque commande).

| Section | Notion | Tâche |
|---|---|---|
| 1.1 | Jokers `*`, `?`, `[ ]`, `{ }` | créer `wildcard_lab`, 20 fichiers `.txt` et 15 `.conf` avec l'expansion, les lister, lister ceux numérotés de 9 à 15, renommer le dossier avec `?` |
| 1.2 | Redirections `>`, `>>`, `<`, `\|` | écrire et ajouter du texte, expliquer `wc` et ses options, compter les lignes, filtrer avec `grep`, compter les `.txt`, trier et dédoublonner avec `sort` et `uniq`, enregistrer `ls` et la date |
| 1.3 | Tâches de fond `&`, `;` | tâche `sleep` de 90 s, `jobs`, deux `sleep` en parallèle, `fg`, enchaîner `mkdir` et `cd` avec `;` |
| 1.4 | Groupement et guillemets `( )`, `{ }`, `' '`, `" "` | sous-shell avec `( )`, groupe avec `{ }`, message avec expansion de `$USER` et `$HOME` |
| 1.5 | Chemins `/`, `~`, `.`, `..` | créer des fichiers dont le nom contient des espaces, un `*` ou un `$` |
| 1.6 | Échappement `\` et apostrophes inversées | stocker `date` et `uptime` dans des variables, compter les fichiers avec `ls \| wc -l` |

## Notions mobilisées

[[Shell et Bash]], [[Redirection et tube]], [[Permissions Unix]] (chemins et fichiers), et la gestion des tâches en arrière-plan ([[Processus]]).

## Points à vérifier

1. L'en-tête du sujet de TP2 porte « TP1 » (complément : coquille d'en-tête).
2. Exemple d'apostrophes : `echo 'path $PWD'` est commenté « Outputs "Hello $PWD" » ; la sortie réelle est `path $PWD`.
3. Exemple d'échappement : `rm file\ file2.txt` est commenté « deletes a file named file2.txt » ; la commande supprime un fichier nommé `file file2.txt`.
