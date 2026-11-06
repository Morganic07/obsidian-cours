---
type: source
tags: [year2]
sources: ["[[Cours TP2]]"]
maj: 2026-11-05
---

Résumé de [[Cours TP2]], dans [[Operating System (matière)]]. Images lues par transcription seulement.

## Contenu, dans l'ordre du cours

Six familles de caractères spéciaux du shell, détaillées dans [[Redirection et tube]] : jokers (`*`, `?`, `[]`, `{}`), redirections (`>`, `>>`, `<`, `|`), tâches de fond (`&`, `;`, `jobs`, `fg`, `bg`), regroupement et guillemets, chemins (`/`, `~`, `.`, `..`), échappement (`\`, apostrophes inversées).

Exercices montrés : `wc -l` compte les lignes, `ls | grep "\.conf"`, `ls | grep "\.txt" | wc -l` (21), `shuf -i 1-10 -n 10 -r`, `sort -g | uniq`, `date >> fichier`, `CURRENT_DATE=\`date\``.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Wc = write count »** : `wc` signifie *word count*, l'étudiant le dit lui-même mal (complément).
2. **Commentaires de code erronés** : `echo 'path $PWD'` annoncé comme sortie « Hello $PWD » ; `rm file\ file2.txt` annoncé comme supprimant « file2.txt ». La transcription signale ces écarts, ils sont bien dans l'image d'origine (non rouverte).
3. **Écart blanc entre `&` et `;`** : la transcription évoque un symbole perdu (`&&` ou `||`). Fausse alerte probable, rien d'illisible dans le sens du cours (image non rouverte).
4. **Fin de la liste du `grep`** : l'alerte sur la ligne coupée est sans conséquence.
