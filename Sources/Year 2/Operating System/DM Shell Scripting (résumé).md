---
type: source
sources: ["[[DM Shell Scripting]]"]
maj: 2026-11-05
---

Résumé de [[DM Shell Scripting]] (TP du 30/09/2024), dans [[Year 2 - Operating System]]. Un énoncé commenté de 19 questions de cours (shell, Bash, variables, tests, boucles), puis 11 tâches de DM avec les réponses de l'étudiant. Il apprend à écrire des [[Script Bash]]. Aucune image.

## Ce qu'apprend le DM

- Tâche 1 : `lshw` (à installer avec `apt`) liste le matériel ; `sudo lshw` donne la vue complète.
- Tâche 2 : les 500 premiers nombres premiers. L'étudiant écrit d'abord le programme en Python, puis en Bash avec `for ((i=2; i*i<=n; i++))`, car `sqrt` n'est pas utilisable directement dans le test.
- Tâches 3 à 7 : `nproc --all` (nombre de cœurs), `lscpu` (ligne « On-line CPU(s) list »), cœur par défaut = 0, mise hors ligne ou en ligne des cœurs par `echo 0|1 | sudo tee /sys/devices/system/cpu/cpuX/online`.
- Tâches 8 à 11 : lire cinq noms et créer les fichiers `.txt`, les supprimer, répéter `date` `n` fois avec `sleep 2`, comparer deux chaînes.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Version Python des nombres premiers** : `range(2, int(NombreActuel**0.5))` exclut la racine carrée, si bien que 4 serait jugé premier et 9 aussi (complément). La version Bash (`i*i <= n`) est correcte. Les caractères accentués du fichier sont abîmés (« Ã »).
2. **Tâche 12 sur les tableaux** : `read -a names` puis `${name[0]}` : nom différent, l'affichage serait vide.
3. **Tâche 11** : `[ $chaine1 = $chaine2 ]` sans guillemets échoue si une chaîne est vide ou contient des espaces (complément).
4. **Tâche 7** : le script remet en ligne aussi le cœur 0 (`cpu0/online` n'existe souvent pas) ; l'énoncé voulait tous les cœurs sauf le défaut (complément).
5. **Énoncé tronqué** : « Write a bash script that reads the names of five files and creates five text files in the current » est coupé dans la note.
