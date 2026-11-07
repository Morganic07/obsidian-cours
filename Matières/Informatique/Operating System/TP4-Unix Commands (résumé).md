---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF TP4-Unix Commands ([[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]) (3 pages, 2 décembre 2024, « TP-4 : Backup processes, and automating the backup using Cron »), dans [[Operating System (matière)]]. Sujet de TP, en anglais. Le rendu est [[TP4 (résumé)]] ; les notes de cours, [[Séance TP4 (résumé)]]. La seule figure (schéma de la syntaxe crontab) est du texte, recopiée ci-dessous. Aucun corrigé.

## 1. Processus père et fils pour journaliser l'heure et la sauvegarder

**Tâche 1** : écrire un programme C pour systèmes de type Unix qui crée un processus père et un fils avec l'appel système `fork()` ([[Appel fork()]], [[Création et terminaison de processus]], [[Processus]]). Avant de lancer le programme, créer le fichier `/home/user/data/time.txt`.
- Le **père** ajoute en continu l'heure système à `time.txt` toutes les 5 secondes.
- Le **fils** sauvegarde `time.txt` en le copiant vers `/home/user/backup/time.txt` toutes les 10 secondes ; la copie écrase la version précédente ([[Sauvegarde de fichier]]).

Une fois écrit, lancer le programme en arrière-plan ([[Tâche en arrière-plan]]), vérifier que les deux processus fonctionnent indépendamment, puis terminer la tâche.

## 2. L'utilitaire cron

**Cron** ([[Tâche planifiée cron]]) est un ordonnanceur de tâches fondé sur le temps, dans les systèmes de type Unix dont Ubuntu. Il permet de programmer des tâches (*cron jobs*) qui s'exécutent automatiquement à intervalles donnés : toutes les heures, chaque jour, chaque semaine, chaque mois. On s'en sert pour automatiser des tâches répétitives : sauvegardes, maintenance, scripts. Les tâches sont définies dans un fichier de configuration, la **crontab** (*cron table*).

### 2.1 Composants

1. **Démon cron** : le service qui tourne en arrière-plan et exécute les tâches planifiées ([[Démon (informatique)]]).
2. **Crontab** : le fichier qui contient le calendrier des commandes.

### 2.2 Installation et utilisation

Cron est en général préinstallé sur Ubuntu ; sinon ([[APT]]) :

```bash
sudo apt update
sudo apt install cron
```

a) Démarrer et activer le service ([[Commande systemctl]]) :

```bash
sudo systemctl start cron
sudo systemctl enable cron
```

b) Vérifier qu'il tourne :

```bash
sudo systemctl status cron
```

c) Éditer la crontab (chaque utilisateur a la sienne) :

```bash
crontab -e
```

La commande ouvre la crontab de l'utilisateur courant dans nano. Ne pas l'exécuter avec `sudo`, sinon on édite celle de root et non celle de l'utilisateur ([[Super-utilisateur root]]).

d) **Syntaxe** : « une entrée de crontab comporte six champs » (voir point à vérifier 1) :

```
*  *  *  *  *  command_to_run
-  -  -  -  -
|  |  |  |  |
|  |  |  |  +---- Day of the week (0 - 7, where both 0 and 7 are Sunday)
|  |  |  +------- Month (1 - 12)
|  |  +---------- Day of the month (1 - 31)
|  +------------- Hour (0 - 23)
+---------------- Minute (0 - 59)
```

Exemple : lancer un script chaque jour à 3 h :

```
0 3 * * * /path/to/script.sh
```

e) Lister les tâches de l'utilisateur courant :

```bash
crontab -l
```

### 2.3 Exemple

Sauvegarder un répertoire chaque jour à minuit :

```
0 0 * * * cp /home/user/data /home/backup/
```

### 2.4 À retenir

1. `* * * * *` : la commande s'exécute toutes les minutes.
2. Par défaut, cron ne permet pas de lancer une tâche toutes les `x` secondes : son intervalle minimal est d'une minute.

## Tâche 2

- a. Avec cron, planifier une tâche qui sauvegarde `/home/user/data/temperature.txt` vers `/home/user/backup/` **toutes les minutes** ; la sauvegarde écrase le fichier précédent.
- b. Même chose **toutes les 3 minutes**.
- c. Même chose **chaque nuit à 2 h**.

(Réponses de l'étudiante dans [[TP4 (résumé)]] : `* * * * *`, `*/3 * * * *`, `0 2 * * *`.)

## Notions mobilisées

`fork`, processus père et fils, boucles et attente (`sleep`, [[Commande sleep]]), copie de fichiers ([[Commande cp]]), [[Tâche planifiée cron]], [[Script Bash]].

## Points à vérifier

1. Le sujet dit qu'une entrée de crontab a « six fields » : il y a cinq champs de temps (minute, heure, jour du mois, mois, jour de la semaine) suivis de la commande (complément).
2. L'exemple `0 0 * * * cp /home/user/data /home/backup/` copie un dossier sans l'option `-r`, ce qui échoue (complément).
3. **Jour de la semaine** : la figure de ce sujet donne `0 - 7` (0 et 7 = dimanche), alors que les notes de [[Séance TP4 (résumé)]] écrivent `0 - 6` (dimanche = 0). Les deux notations sont acceptées par cron (complément).
4. **Chemins** : la tâche 1 sauvegarde vers `/home/user/backup/`, l'exemple 2.3 vers `/home/backup/` ; même écart que dans le TP3.
