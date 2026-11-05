---
type: concept
aliases: [redirection, redirections, pipe, tube, wildcards, jokers, pattern matching shell, job control, commandes en arrière-plan]
matieres: [Operating System]
sources: ["[[Cours TP2]]"]
maj: 2026-11-05
---

Mécanismes du shell vus au TP2.

- **Jokers** : `*` (zéro ou plusieurs caractères), `?` (exactement un), `[123]` (un caractère de la liste), `{1,2,3}` ou `{1..20}` (génération de plusieurs noms : `touch file{1..20}.txt`).
- **Redirections** : `>` écrase le fichier, `>>` ajoute, `<` lit depuis un fichier, `|` envoie la sortie d'une commande vers l'entrée d'une autre. Exemple : `ls | grep "\.txt" | wc -l` compte les `.txt`. `sort -g | uniq` trie numériquement et supprime les doublons.
- **Tâches de fond** : `&` lance en arrière-plan, `;` enchaîne, `jobs` liste, `fg %1` ramène au premier plan, `bg %1` relance en arrière-plan, `kill %1` termine.
- **Regroupement** : `( )` exécute dans un sous-shell (le `cd` n'affecte pas le shell courant), `{ }` dans le shell courant.
- **Guillemets** : simples, texte littéral (`'$USER'` reste `$USER`) ; doubles, expansion des variables. `\` échappe un caractère (`My\ File.txt`). `` `date` `` ou `$(date)` substitue la sortie d'une commande.
- **Chemins** : `/`, `~` (dossier personnel), `.` (dossier courant), `..` (parent).

Liens : [[Shell et Bash]], [[Script Bash]], [[AWK]]

Résumé : [[Cours TP2 (résumé)]]
