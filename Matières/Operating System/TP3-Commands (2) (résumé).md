---
type: source
tags: [year2]
sources: [".raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf"]
maj: 2026-11-06
---

Résumé du PDF TP3-Commands (2) (`.raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf`) (8 pages, 25 novembre 2024, « TP-3 : Network Management, and Backup »), dans [[Operating System (matière)]]. Sujet de TP, en anglais. Le rendu est [[TP3 (résumé)]] ; les notes de cours, [[Séance TP3 (résumé)]].

## Ce qui est demandé

**Partie 1, réseau.**

- Trouver l'adresse IPv4 locale avec `ifconfig` (paquet `net-tools`) ou `ip address` (paquet `iproute2`). Le sujet explique une sortie d'exemple à trois interfaces (`eth0`, `wlan0`, `eth1`) : adresse, broadcast, masque de sous-réseau, paquets et octets échangés. Voir [[Adressage IPv4 et CIDR]].
- Résolution locale avec `/etc/hosts` : fichier texte qui associe un nom d'hôte à une adresse IP, effet immédiat, entrée `127.0.0.1` à conserver ; ajout d'une ligne avec `sudo nano /etc/hosts`, test avec `ping <nom>`.
- Configuration manuelle de l'adresse avec Netplan (Ubuntu 18.04 et suivants) : fichiers YAML dans `/etc/netplan` (indentation obligatoire), exemples d'adresse statique et de DHCP.
- Tâche 1 : relever les interfaces et adresses, capturer `/etc/hosts` et le fichier YAML (ou trouver le fichier de configuration utilisé), ajouter l'entrée du nom d'hôte local.

**Partie 2, sauvegarde.** Script `time.sh` qui ajoute la date toutes les 2 secondes à `date.txt` (boucle infinie, lancé avec `&`), puis script `backup.sh` qui copie ce fichier toutes les 15 secondes vers un dossier de sauvegarde. Arrêt des trois tâches de fond avec `jobs`, `fg` et `Ctrl + C`. Tâche 2 : script qui ajoute la sortie de `free -h` à `memory.txt` toutes les 5 s, script qui sauvegarde ce fichier toutes les 20 s, puis terminaison des tâches.

## Notions mobilisées

[[Shell et Bash]], [[Script Bash]], [[Redirection et tube]], [[Permissions Unix]] (droit d'exécution des scripts), [[Processus]] (tâches de fond), [[Système de fichiers]].

## Points à vérifier

1. Dans `backup.sh`, la destination est `/home/backup/` alors que le texte annonce `/home/user/backup/` ; l'affichage utilise `$Backup`, variable jamais définie.
2. Le sujet nomme le fichier `time.sh` « sudo nano time.sh » : `sudo` n'est pas nécessaire pour un fichier du répertoire de l'utilisateur (complément).
