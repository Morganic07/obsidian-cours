---
type: concept
tags: [year2]
aliases: [redirection, redirections, pipe, tube, pattern matching shell]
matieres: [Operating System]
sources: ["[[Cours TP2]]", ".raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf"]
maj: 2026-11-06
---

Mécanismes du shell vus au TP2, qui reposent sur des [[Méta-caractère|méta-caractères]].

- **[[Joker (wildcard)|Jokers]]** : `*` (zéro ou plusieurs caractères), `?` (exactement un), `[123]` (un caractère de la liste), `{1,2,3}` ou `{1..20}` (génération de plusieurs noms : `touch file{1..20}.txt`).
- **Redirections** : `>` redirige la sortie vers un fichier en le créant ou en l'écrasant, `>>` l'ajoute à la fin, `<` prend l'entrée dans un fichier (`wc -l < file.txt`), `|` (pipe) envoie la sortie d'une commande vers l'entrée d'une autre. Exemple : `ls | grep "\.txt" | wc -l` compte les `.txt` ([[Commande grep]], [[Commande wc]]). `sort -g | uniq` trie numériquement et supprime les doublons ([[Commande sort]]).
- **[[Tâche en arrière-plan|Tâches de fond]]** : `&` lance en arrière-plan, `;` enchaîne, `jobs` liste, `fg %1` ramène au premier plan, `bg %1` relance en arrière-plan, `kill %1` termine.
- **Regroupement** : `( )` exécute dans un sous-shell (le `cd` n'affecte pas le shell courant), `{ }` dans le shell courant.
- **Guillemets** : simples, texte littéral (`'$USER'` reste `$USER`) ; doubles, expansion des variables. `\` échappe un caractère (`My\ File.txt`). `` `date` `` ou `$(date)` substitue la sortie d'une commande.
- **Chemins** : `/`, `~` (dossier personnel), `.` (dossier courant), `..` (parent).

Notion parente : [[Méta-caractère]]. Voir aussi : [[Shell et Bash]], [[Script Bash]], [[AWK]], [[Joker (wildcard)]], [[Tâche en arrière-plan]], [[Commande grep]], [[Commande wc]], [[Commande sort]]

Résumés : [[Séance TP2 (résumé)]], [[TP2 (résumé)]], [[Copy of TP2-Commands (résumé)]]
