---
type: source
sources: ["[[Copy of 08 Processes-TP]]"]
maj: 2026-11-05
---

Résumé de [[Copy of 08 Processes-TP]] (TP « Processes » du 03/11/2024), dans [[Year 2 - Operating System]]. Il apprend à programmer en C avec les [[Processus]]. Les énoncés sont recopiés, suivis du code de l'étudiant (transcriptions seulement, images non rouvertes).

## Ce qu'apprend le TP

- Labs 1 à 3 : programmes C simples (somme de deux entiers, nombres impairs jusqu'à une limite, suite arithmétique), compilés avec GCC.
- Lab 4 : `fork()` avec `switch` sur le retour (`-1` erreur, `0` fils, sinon parent), affichage des PID, `wait(&status)`, `WIFEXITED` / `WEXITSTATUS`.
- Lab 5 : arbre de processus (A crée B et C ; B crée D et E ; E crée F ; C crée K ; K crée L ; la suite ajoute M) par `fork()` imbriqués, chaque processus terminant par `exit(0)` et le parent attendant avec `waitpid`.
- Lab 6 : deux processus affichent les tables de multiplication de 5 et de 7, l'un après l'autre.
- Lab 7 : le fils calcule une factorielle, puis le parent affiche les nombres premiers jusqu'à une borne (test `i*i <= num`).
- Lab 8 : exécution simultanée, obtenue en retirant le `wait`.
Voir [[Création et terminaison de processus]].

## Points à vérifier dans le cours

1. **Lab 5, processus F** : dans le premier extrait, `exit(0)` est après le `printf` de F ; la transcription propose de le placer dans le `if(f==0)`. Sans `exit`, F poursuit le code de E (complément). Image non rouverte.
2. **Lab 6** : l'énoncé demande deux processus ; le parent attend chaque fils avant d'en créer un autre, donc l'exécution n'est pas simultanée.
3. **Fonctions sans `return`** : `int lab1(void)` (lab 1) et `int primenumber` (lab 7) sont déclarées `int` sans renvoyer de valeur (complément) ; sans effet sur le résultat. Au lab 7, l'énoncé voulait que le fils s'exécute en premier : c'est le cas grâce au `waitpid`.
4. **Lab 8 « Update Lab 3 »** : l'énoncé concerne le lab 3, qui n'a pas de processus ; la note ne dit pas lequel est visé.
