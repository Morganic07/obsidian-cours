---
type: source
sources: ["[[raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment]] (2 pages, 31 décembre 2024, « TP-6 : Assignment »), dans [[Year 2 - Operating System]]. Sujet de TP, en anglais. Les rendus des TP1 à TP6 sont regroupés dans [[UNIX Commands - Semester report (résumé)]].

## Ce qui est demandé

Cinq tâches, chacune avec capture d'écran :

1. **Informations système** (rôle d'administrateur) avec des commandes Linux : processeur (modèle, vitesse, nombre de cœurs, architecture), mémoire vive (totale, utilisée), stockage (taille, espace libre), résumé du matériel.
2. **Sudo sans mot de passe** : expliquer pas à pas, avec les commandes, comment supprimer l'exigence du mot de passe pour `sudo`.
3. **Sauvegarde planifiée** : créer `/home/First`, `/home/Second`, `/home/Third` avec un fichier texte chacun, puis une tâche cron qui copie les trois fichiers vers `/home/Backup` toutes les 2 minutes. Voir [[Tâche planifiée cron]].
4. **AWK** : sur `log.txt`, fichier délimité par des barres verticales (horodatage, utilisateur, heures de connexion et de déconnexion, durée, activité web), donner deux commandes [[AWK]] qui trouvent les utilisateurs de `youtube.com` et de `facebook.com`.
5. **Programme C avec `fork`** : le père génère un nombre avec `rand()` (`stdlib.h`) et le passe au fils par une variable globale ; le fils indique s'il est pair ou impair. Voir [[Création et terminaison de processus]].

## Notions mobilisées

[[Shell et Bash]], [[Permissions Unix]], [[Tâche planifiée cron]], [[AWK]], [[Processus]], [[Appel système]].

## Points à vérifier

1. **Tâche 5** : après `fork`, le père et le fils ont chacun leur copie de la mémoire, variables globales comprises. Le fils ne voit la valeur que si elle est tirée avant le `fork` ; une valeur tirée par le père après le `fork` ne lui parvient pas (complément : comportement de `fork`).
