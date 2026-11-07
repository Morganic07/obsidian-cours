---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF TP6-Assignment ([[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]) (2 pages, 31 décembre 2024, « TP-6 : Assignment »), dans [[Operating System (matière)]]. Sujet de TP, en anglais, sans figure ni corrigé. Les rendus des TP1 à TP6 sont regroupés dans [[UNIX Commands - Semester report (résumé)]]. Le fichier de données de la tâche 4 est résumé dans [[log (résumé)]].

## Les cinq tâches

Chaque tâche demande les commandes et une capture d'écran du terminal.

### Tâche 1 : informations système

En tant qu'administrateur système, utiliser des commandes Linux pour obtenir :
- a) **processeur** : modèle, vitesse, nombre de cœurs, architecture ;
- b) **mémoire vive** : mémoire totale disponible et mémoire utilisée ;
- c) **stockage** : taille totale et espace disponible ;
- d) **matériel** : un résumé de tous les composants.

Exécuter les commandes appropriées et capturer la sortie de chacune. (Commandes vues dans le cours : [[Commande lscpu]], [[Commande nproc]], [[Commande free]], [[Commande df]], [[Commande lshw]] ; voir [[Commandes Shell + explications (résumé)]] — complément, le sujet ne les nomme pas.)

### Tâche 2 : `sudo` sans mot de passe

Expliquer pas à pas, avec les commandes Linux et des captures, comment se passer du mot de passe pour exécuter des commandes avec `sudo` ([[Commande sudo]], [[Fichier sudoers]] ; méthode dans [[séance TP1 (résumé)]]).

### Tâche 3 : sauvegarde planifiée

1. Créer trois répertoires dans le répertoire de l'utilisateur : `/home/First`, `/home/Second`, `/home/Third` ([[Commande mkdir]]).
2. Y créer les fichiers `/home/First/first.txt`, `/home/Second/second.txt`, `/home/Third/third.txt`, avec un texte quelconque.
3. Mettre en place une tâche cron qui copie automatiquement ces trois fichiers vers un seul répertoire de sauvegarde, `/home/Backup`, **toutes les 2 minutes** ([[Tâche planifiée cron]], [[Sauvegarde de fichier]]).

Fournir toutes les commandes et des captures qui montrent clairement la mise en œuvre.

### Tâche 4 : AWK sur `log.txt`

Un fichier délimité par des barres verticales (`log.txt`, fourni dans le dossier du devoir sur Teams) contient : *Timestamp, Username, Login Time, Logout Time, Duration, Web Activity*. Donner **deux** commandes [[AWK]] qui trouvent les utilisateurs ayant utilisé `youtube.com` et `facebook.com`, avec la capture de leur sortie. (Méthode : opérateur `~` sur la 6e colonne avec `-F"|"`, voir [[Séance TP5 (résumé)]].)

### Tâche 5 : programme C avec `fork`

La fonction `rand()` du C génère des entiers aléatoires ; elle est déclarée dans `stdlib.h` ([[Nombres aléatoires en C]]). Écrire un programme C qui crée un père et un fils avec `fork()` ([[Appel fork()]], [[Création et terminaison de processus]]) : le père génère un nombre aléatoire et le passe au fils par une **variable globale** ; le fils vérifie si le nombre est pair ou impair ([[Parité d'un entier]]) et affiche le résultat. Fournir le code et la capture de la sortie.

## Notions mobilisées

[[Shell et Bash]], [[Permissions Unix]], [[Tâche planifiée cron]], [[AWK]], [[Processus]], [[Appel système]].

## Points à vérifier

1. **Tâche 5** : après `fork`, le père et le fils ont chacun leur copie de la mémoire, variables globales comprises. Le fils ne voit la valeur que si elle est tirée avant le `fork` ; une valeur tirée par le père après le `fork` ne lui parvient pas (complément : comportement de `fork`).
2. **Tâche 3** : les répertoires `/home/First` etc. sont dits « dans le répertoire de l'utilisateur » mais sont placés directement sous `/home`, ce qui demande les droits root (complément).
3. **Tâche 4, « youtube.com and facebook.com »** : le sujet ne précise pas s'il faut les utilisateurs de l'un **ou** l'autre site, ou des deux ; d'où peut-être les « deux commandes » demandées (`||` et `&&`).
