---
type: source
sources: ["TP2 du dossier DM/TP2"]
maj: 2026-11-05
---

Résumé de la note TP2 du dossier `DM/TP2` de [[Year 2 - Operating System]] (la note porte le nom de l'étudiant, d'où l'absence de lien direct). Captures lues par transcription seulement.

## Ce qu'apprend le TP

Même contenu que [[Cours TP2]], en version rendue.
- Tâche 1 (jokers) : créer `wildcard_lab`, `touch file{1..20}.txt`, `file{1..15}.conf`, `ls *.txt`, `ls file{9..15}.*`, renommer un dossier avec `mv`.
- Tâche 2 (redirections) : `>`, `>>`, `wc -l`, `grep`, `shuf`, `sort -g | uniq`, `ls > directory_list.txt`, `date >> ...`.
- Tâche 3 (tâches de fond) : `sleep 90 &`, `jobs`, `fg`, `bg`.
- Tâche 4 : sous-shell `( )` et groupe `{ }`.
- Tâche 5 : fichiers aux noms spéciaux (espaces, `*`, `$`) par échappement.
- Tâche 6 : substitution de commande (`date`, `uptime`, `ls | wc -l`).
Voir [[Redirection et tube]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Compte de 21 fichiers `.txt`** : 20 `file*.txt` plus `lab_output.txt` ; cohérent.
2. **Questions 9 et 4 sans énoncé** : la note ne reprend pas les énoncés de la tâche, les réponses ne sont lisibles qu'avec le sujet.
3. **`mv wildcard_lab?  wildcard_lab2`** : le point d'interrogation devine un caractère final inconnu (nom tronqué dans la capture) ; non éclairci.
4. **Sortie de `fg` après deux `sleep 60`** : le message `Done` s'affiche pour les deux tâches déjà finies, comme prévu.
