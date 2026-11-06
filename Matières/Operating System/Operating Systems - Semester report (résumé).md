---
type: source
tags: [year2]
sources: ["[[Operating Systems - Semester report]]"]
maj: 2026-11-05
---

Résumé de [[Operating Systems - Semester report]], dans [[Operating System (matière)]]. Rapport de semestre qui rassemble le « Lab 1 Shell scripting » (30 septembre 2024) et le « Lab 2 Processes » (21 octobre 2024), avec captures d'écran. Les images n'ont pas été rouvertes ; seules leurs transcriptions ont été lues, et la note a été lue en entier mais vite pour les sorties de terminal.

## Ce qu'apprend le rapport

- **Lab 1** : mêmes questions et mêmes tâches que [[DM Shell Scripting (résumé)]] (shells, `which`, `pwd`, `mkdir`, scripts, `lshw`, `lscpu`, cœurs en ligne ou hors ligne, `core.sh` dont la sortie `0` est vérifiée par `cat online`), avec les captures de résultats.
- **Lab 2** : mêmes programmes C que [[Copy of 08 Processes-TP (résumé)]] (labs 1 à 8), avec commentaires et sorties. Pour le lab 8, l'étudiant explique qu'il a d'abord mis à jour le lab 7 en retirant `wait`, puis propose une version qui ajoute un `fork` au lab 3. Sortie obtenue : le message final du parent s'affiche avant la fin de l'enfant (`L'enfant a fini...` puis `0 3 6 ... 39`). Voir [[Création et terminaison de processus]].

## Points à vérifier dans le cours

1. **Lab 8** : au lab 8 version simultanée, le message du parent s'affiche avant la fin de l'enfant ; il porte pourtant « L'enfant a fini » : le message est faux dans ce cas (complément).
2. **Lab 7 simultané** : parent et fils lisent tous deux `scanf` sur le terminal au même moment ; les saisies se mélangent (complément).
3. **Alertes de transcription** (« Cat » en majuscule, « used » pour « user », lignes coupées) : portent sur des captures de l'énoncé, sans effet sur le contenu.
4. **Programme de nombres premiers du lab 1** : voir [[DM Shell Scripting (résumé)]], point 1.
