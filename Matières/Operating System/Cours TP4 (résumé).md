---
type: source
tags: [year2]
sources: ["[[Cours TP4]]"]
maj: 2026-11-05
---

Résumé de [[Cours TP4]], dans [[Operating System (matière)]].

## Contenu, dans l'ordre du cours

- **Programme C à deux processus** : le parent ajoute l'heure dans `time.txt` toutes les 5 s, le fils copie le fichier toutes les 10 s (appel `system("cp ...")`), voir [[Création et terminaison de processus]].
- **cron** : planificateur de tâches, démarrage, syntaxe, exemples, intervalle minimal d'une minute ; voir [[Tâche planifiée cron]]. Exemple à lire : `* * * * * cp .../temperature.txt .../temperature.txt`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`waitpid(pid, &status, 0)`** placé après une boucle infinie `while(1)` dans le parent : il n'est jamais atteint (complément). Le chemin relatif `"time.txt"` dépend du dossier de lancement.
2. **Fichier `time.txt` et dossier de sauvegarde** : le programme ne crée pas les dossiers `data` et `backup` ; ils doivent exister avant.
3. **Mention « Dimanche = 0 »** : en cron, 0 et 7 désignent tous deux dimanche (complément).
