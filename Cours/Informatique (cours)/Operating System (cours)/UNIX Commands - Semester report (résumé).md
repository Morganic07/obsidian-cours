---
type: source
tags: [year2]
sources: ["UNIX Commands - Semester report"]
maj: 2026-11-05
---

Résumé de UNIX Commands - Semester report, dans [[Operating System (index)]]. Très longue note (plus de 2 400 lignes) : rapport qui reprend les rendus des TP1 à TP6, avec captures. Lue par parties (table des matières, titres, énoncés et commentaires de l'étudiant, sorties de terminal parcourues), images non rouvertes.

## Ce qu'apprend le rapport

- **TP1** : aide du shell, `sudo`, `apt`, `visudo`, clavier, nom de machine, arborescences et droits ; voir [[TP1 (résumé)]]. Le rapport ajoute les réponses courtes sur `cp --help` avec la liste des options.
- **TP2** : jokers, redirections, tâches de fond, regroupement, échappement, substitution ; voir [[TP2 (résumé)]] et [[Redirection et tube]].
- **TP3** : adresses IP, `/etc/hosts`, `ping`, scripts de sauvegarde en boucle ; voir [[TP3 (résumé)]].
- **TP4** (2 décembre 2024) : programme C parent / fils avec sauvegarde de `time.txt`, lancé en arrière-plan puis arrêté par `kill %1`, puis cron pour sauvegarder `temperature.txt` ; voir [[TP4 (résumé)]] et [[Tâche planifiée cron]].
- **TP5** : [[AWK]], voir [[TP5 (résumé)]].
- **TP6** (31 décembre 2024) : synthèse des commandes de diagnostic (`lscpu` pour le processeur, `free -h` pour la RAM, `df -h` pour le stockage, `sudo lshw -short` pour le matériel), `sudo` sans mot de passe, création de dossiers `first`, `second`, `third` avec un fichier chacun par boucle `for`, tâche cron toutes les 2 minutes, recherche AWK dans `log.txt`, et un programme C où le parent génère un nombre aléatoire avant `fork()`, l'affiche et attend (`wait`), tandis que le fils dit s'il est pair ou impair (`srand(time(NULL))` ajouté pour éviter la même valeur à chaque lancement). Voir [[Création et terminaison de processus]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Mêmes erreurs que les TP d'origine** : accolades avec espaces, programme C du TP4, `$Backup`, sortie `2 Ford Focus` ; voir les résumés cités.
2. **Programme du TP6** : `rand()` est appelé avant `fork()`, donc le fils reçoit une copie de la variable globale (le sujet exact du programme) ; ses `printf` du fils n'ont pas de saut de ligne final (complément).
3. **Parties non relues en détail** : les longues sorties de `ls`, `ping` et `cat` répétées dans les TP1 à TP5 n'ont pas été relues ligne à ligne, et le TP6 a été lu de manière plus rapide que les autres.
4. **Alertes de transcription** nombreuses (lignes coupées, `127.0.0.1.1`, apostrophes) : elles portent sur les captures, et aucune n'a été confirmée en ouvrant les images.
