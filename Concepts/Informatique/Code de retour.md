---
type: concept
tags: [year2, year4]
aliases: [exit status, exit code, code de sortie, statut de sortie, return code]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]", "[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : le code de retour (*exit status*) est l'entier qu'un processus renvoie à son parent en se terminant, par `exit(n)` ou par le `return n` de `main`. Par convention, **0 signifie succès** et toute autre valeur (de 1 à 255, car seul l'octet de poids faible est conservé) une erreur.

**En C**, le parent le récupère avec `wait(&status)` ou `waitpid` ([[Appels wait() et waitpid()]]), puis le décode avec les macros de `<sys/wait.h>` :

- `WIFEXITED(status)` : vrai si le fils s'est terminé normalement ;
- `WEXITSTATUS(status)` : la valeur passée à `exit()` ;
- `WIFSIGNALED(status)` : vrai si le fils a été tué par un signal (`WTERMSIG(status)` en donne le numéro).

**Dans le shell** :

- `$?` contient le code de retour de la dernière commande (`echo $?`) ; un processus tué par le signal $n$ y apparaît comme $128 + n$ (par exemple 130 après Ctrl+C, signal 2) ;
- `if` teste ce code, 0 valant « vrai » : `if grep -q motif fichier; then … fi` ([[Structure conditionnelle]]) ;
- `&&` et `||` enchaînent des commandes selon leur réussite : `mkdir rep && cd rep`, `cd rep || exit 1` ;
- un [[Script Bash|script]] renvoie le sien avec `exit 0` ou `exit 1`.

## Dans le cours

[[7 - OS]] présente `exit()` comme la fin normale d'un processus, qui renvoie une valeur au parent par `wait()` ([[Création et terminaison de processus]]) ; le décodage par `WIFEXITED` et `WEXITSTATUS` et le lien avec `$?` sont des compléments de la fiche. [[8 - OS commandes sh]] y rattache en complément le fonctionnement de `if`, `&&` et `||`.

[[4 - Cours complet]] (C++) : `main` retourne 0 au « système » qui l'a appelée ; sous Unix/Linux, 0 indique un succès (convention Unix), une autre valeur une erreur dont elle peut préciser le type.

Voir aussi : [[Appels wait() et waitpid()]], [[Création et terminaison de processus]], [[Structure conditionnelle]], [[Script Bash]], [[Processus zombie et orphelin]], [[Fonction main (C et C++)]].

Résumés : [[7 - OS]], [[8 - OS commandes sh]], [[4 - Cours complet]]
