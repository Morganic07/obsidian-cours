---
type: concept
tags: [year2]
aliases: [stdin, stdout, stderr, entrée standard, sortie standard, sortie d'erreur, descripteur de fichier, standard streams, file descriptor]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Cours TP2.docx|Cours TP2]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : tout [[Processus|processus]] Unix démarre avec trois flux ouverts, hérités du shell qui l'a lancé et identifiés par un **descripteur de fichier**, un petit entier qui désigne un fichier ouvert pour ce processus :

| Descripteur | Nom | Par défaut |
|---|---|---|
| 0 | entrée standard, *stdin* | le clavier |
| 1 | sortie standard, *stdout* | le terminal |
| 2 | sortie d'erreur, *stderr* | le terminal |

Un programme écrit ses résultats sur stdout et ses messages d'erreur sur stderr : les deux s'affichent mélangés à l'écran, mais peuvent être séparés par redirection.

**Redirections** (syntaxe de [[Shell et Bash|Bash]]) :

- `commande < f` : stdin lu depuis le fichier `f` ;
- `commande > f` et `commande >> f` : stdout écrit dans `f` (écrasé, ou complété à la fin) ; `>` équivaut à `1>`, et ne redirige donc pas les erreurs ;
- `commande 2> f` et `commande 2>> f` : stderr seul dans `f` ;
- `commande > f 2>&1` : les deux flux dans le même fichier. `2>&1` signifie « le flux 2 va là où va le flux 1 à cet instant », d'où l'importance de l'ordre : `commande 2>&1 > f` envoie stderr au terminal et seulement stdout dans `f` ;
- `commande &> f` : raccourci Bash de `> f 2>&1` ;
- `commande 2> /dev/null` : jette les messages d'erreur ([[Fichier de périphérique|`/dev/null`]] absorbe tout ce qu'on y écrit).

**Tube** : `cmd1 | cmd2` relie le stdout de `cmd1` au stdin de `cmd2` ; le stderr de `cmd1` n'y passe pas et reste affiché, sauf avec `cmd1 2>&1 | cmd2` ou son raccourci Bash `cmd1 |& cmd2`.

Exemple : `ls dossier_absent 2> erreurs.txt` n'affiche rien à l'écran ; le message « No such file or directory » est dans `erreurs.txt`.

## Dans le cours

Le TP2 ([[2 - TP2]]) présente `>`, `>>`, `<` et `|` ([[Redirection et tube]]) sans parler des numéros de flux ni de la sortie d'erreur ; la notion apparaît dans les compléments de la fiche.

Voir aussi : [[Redirection et tube]], [[Commande tee]], [[Méta-caractère]], [[Flux d'entrée-sortie (C++)]] (`cin`, `cout` et `cerr` sont reliés à ces trois flux).

Résumés : [[2 - TP2]]
