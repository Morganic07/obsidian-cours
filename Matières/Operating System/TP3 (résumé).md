---
type: source
tags: [year2]
sources: ["TP3 du dossier DM/TP3"]
maj: 2026-11-06
complet: true
---

Résumé de la note TP3 du dossier `DM/TP3` de [[Operating System (matière)]] (la note porte le nom de l'étudiante, d'où l'absence de lien direct). C'est la version rendue de [[Cours TP3]] (voir [[Séance TP3 (résumé)]]) : réseau, `/etc/hosts`, puis scripts de sauvegarde lancés en arrière-plan. Les captures du terminal ne sont pas intégrées, car leur chemin contient le nom de l'étudiante ; leur contenu est recopié ci-dessous en texte, d'après les transcriptions.

## Tâche 1 : réseau

### 1. Adresse IP

```
$ ip address
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 ... state UNKNOWN
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
5: eth0@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ... state UP
    link/ether 00:16:3e:68:65:80 brd ff:ff:ff:ff:ff:ff
    inet 100.115.92.201/28 brd 100.115.92.207 scope global eth0
    inet6 fe80::216:3eff:fe68:6580/64 scope link
```

Réponse : adresse locale interne `127.0.0.1` (voir point à vérifier 4 et [[Adresse de bouclage]]) ; adresse sur le réseau `100.115.92.201` ([[Adressage IPv4 et CIDR]], [[Commande ip]]).

![[TP3 - image8.png]]
*Capture : sortie de `ip address`.*

### 2. Fichier `/etc/hosts`

```
$ cat /etc/hosts
127.0.1.1       penguin
127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters
```

Voir [[Fichier hosts]].

![[TP3 - image18.png]]
*Capture : `cat /etc/hosts`.*

### 3. Configuration réseau

Pas de fichier [[YAML|.yaml]] dans [[Netplan|/etc/netplan]]/ : le système utilise un autre fichier, `/etc/network/interfaces`.

```
$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
# The loopback network interface
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet dhcp
source /etc/network/interfaces.d/*
```

L'interface `lo` est la boucle locale ; `eth0` obtient son adresse par [[DHCP]] (`inet dhcp`).

![[TP3 - image2.png]]
*Capture : `cat interfaces` dans `/etc/network`.*

### 4. Nom d'hôte, IP, et modification de `/etc/hosts`

```
$ hostname ; hostname -I
penguin
100.115.92.201
```

Voir [[Commande hostname]] et [[Nom d'hôte]].

Fichier `/etc/hosts` avant modification :

```
127.0.1.1          penguin
127.0.0.1          localhost
::1                localhost ip6-localhost ip6-loopback
ff02::1            ip6-allnodes
ff02::2            ip6-allrouters
```

Après modification (ajout de l'IP réseau associée au nom d'hôte) :

```
127.0.1.1       penguin
127.0.0.1       localhost
100.115.92.201  penguin

::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters
```

Vérification avec [[Commande ping|ping]] :

```
$ ping penguin
PING penguin (127.0.1.1) 56(84) bytes of data.
64 bytes from penguin (127.0.1.1): icmp_seq=1 ttl=64 time=0.048 ms
64 bytes from penguin (127.0.1.1): icmp_seq=2 ttl=64 time=0.280 ms
...
64 bytes from penguin (127.0.1.1): icmp_seq=18 ttl=64 time=0.075 ms
```

Conclusion de l'étudiante : « tout semble correct ».

![[TP3 - image15.png]]
*Capture : `hostname ; hostname -I`.*

![[TP3 - image9.png]]
*Capture : `/etc/hosts` avant la modification.*

![[TP3 - image17.png]]
*Capture : `/etc/hosts` après la modification.*

![[TP3 - image14.png]]
*Capture : `ping penguin`.*

## Script `time.sh`

Après avoir créé le répertoire `data`, l'étudiante crée `time.sh` (qui ajoute la date toutes les 2 secondes dans `date.txt`, voir le script dans [[Séance TP3 (résumé)]]) et le lance en arrière-plan ([[Tâche en arrière-plan]]) :

```
~/data$ ./time.sh &
[1] 22736
```

`[1]` est le numéro de tâche, `22736` le [[Identifiant de processus|PID]]. Plusieurs `cat date.txt` montrent que le fichier grossit : le script fonctionne.

```
$ cat date.txt
2024-11-25 10:48:51
2024-11-25 10:48:53
2024-11-25 10:48:55
2024-11-25 10:49:00
...
2024-11-25 10:49:10
2024-11-25 10:49:10
2024-11-25 10:49:12
2024-11-25 10:49:12
...
```

![[TP3 - image10.png]]
*Capture : lancement de `./time.sh &` dans `~/data`.*

![[TP3 - image6.png]]
*Capture : `cat date.txt`.*

## Script `backup.sh`

Création du répertoire `backup` et de `backup.sh` (copie de `date.txt` toutes les 15 secondes, avec un message de réussite horodaté), lancé en arrière-plan ([[Sauvegarde de fichier]]) :

```
~/backup$ sudo ./backup.sh &
[1] 23696
~/backup$ 2024-11-25 11:06:11 -  Successful!
2024-11-25 11:06:26 -  Successful!
```

```
~/backup$ ls
backup.sh  date.txt
```

Deux `cat` successifs de la copie montrent qu'elle s'allonge (de 10:56:07 à 10:56:23) : « le fichier `date.txt` est mis à jour toutes les 15 secondes ». Ensuite, l'étudiante arrête toutes les tâches en cours.

![[TP3 - image13.png]]
*Capture : lancement de `sudo ./backup.sh &` dans `~/backup`.*

![[TP3 - image16.png]]
*Capture : `ls` dans `~/backup`.*

![[TP3 - image11.png]]
*Capture : sortie horodatée (2024-11-25 10:55:28…).*

![[TP3 - image19.png]]
*Capture : sortie horodatée (2024-11-25 10:55:28…), seconde capture.*

## Tâche 2 : sauvegarde de la mémoire

### 1. Écrire l'état de la mémoire toutes les 5 secondes

```bash
#!/bin/bash
while true
do
    free -h >> memory.txt
    sleep 5
done
```

Voir [[Commande free]] et [[Boucle (programmation)]]. Après avoir donné les droits d'exécution et lancé le script en arrière-plan, `memory.txt` est créé et complété toutes les 5 secondes :

```
~/backup$ ./memory.sh &
[1] 23747
~/backup$ cat memory.txt
               total        used        free      shared  buff/cache   available
Mem:            6.4Gi       125Mi       4.7Gi       4.3Mi       1.6Gi       6.3Gi
Swap:              0B          0B          0B
               total        used        free      shared  buff/cache   available
Mem:            6.4Gi       125Mi       4.7Gi       4.3Mi       1.6Gi       6.3Gi
Swap:              0B          0B          0B
...
```

Le second `cat` montre six blocs au lieu de quatre : le fichier grandit.

![[TP3 - image1.png]]
*Capture : le script `memory.sh`.*

![[TP3 - image12.png]]
*Capture : lancement de `./memory.sh &`.*

![[TP3 - image3.png]]
*Capture : `cat memory.txt`.*

### 2. Sauvegarder `memory.txt` toutes les 20 secondes

```bash
#!/bin/bash
SOURCE="/home/momo/backup/memory.txt"
DESTINATION="/home/momo/data/"
while true; do
 cp "$SOURCE" "$DESTINATION"
 echo "$Backup Successful!"
 sleep 20
done
```

Le script copie `memory.txt` (dans `/home/momo/backup`) vers `/home/momo/data` toutes les 20 secondes ([[Commande cp]], [[Script Bash]]). Après lancement en arrière-plan :

```
~/data$ ls
date.txt  memory.txt  time.sh
```

Un `cat memory.txt` répété montre que la copie s'allonge toutes les 20 secondes.

![[TP3 - image4.png]]
*Capture : le script de sauvegarde de `memory.txt`.*

![[TP3 - image7.png]]
*Capture : `ls` dans `~/data`.*

### 3. Arrêter les tâches

Voir [[Commande jobs]] et [[Commande kill]].

```
~/backup$ jobs
[1]-  Running                 ./backup.sh &
[2]+  Running                 ./memory.sh &
~/backup$ kill %1; kill %2
~/backup$ jobs
[1]-  Terminated              ./backup.sh
[2]+  Terminated              ./memory.sh
```

![[TP3 - image5.png]]
*Capture : `jobs` dans `~/backup`.*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Adresse `127.0.0.1.1`** : la transcription la signale ; probablement `127.0.1.1` (curseur sur le premier caractère). **Vérifié sur l'image** : il s'agit bien de `127.0.1.1`, le curseur recouvre le premier chiffre.
2. **`ping penguin` après modification** : la sortie montre `127.0.1.1`, ce qui concorde avec le fichier modifié, dont la première ligne reste `127.0.1.1 penguin`. La transcription lisait `127.0.0.1 penguin` ; **vérifié sur l'image** : c'est `127.0.1.1`, le curseur recouvre le premier chiffre. `penguin` y est donc associé à deux adresses, `127.0.1.1` puis `100.115.92.201`, et `ping` prend la première (complément).
3. **Doublons dans `date.txt`** : les horodatages se répètent deux fois par intervalle, ce qui indique que deux copies du script écrivaient en même temps (complément).
4. **Adresse affichée comme « interne »** : `127.0.0.1` est l'adresse de bouclage, pas une adresse locale du réseau.
5. **Message de `backup.sh`** : la sortie affiche « 2024-11-25 11:06:11 - Successful! » ; le script de `backup.sh` n'est pas montré dans la note, et celui de la tâche 2 (`echo "$Backup Successful!"`) n'afficherait que « Successful! » car `$Backup` est vide (complément).
6. **Captures** : les 19 captures de la note sont intégrées dans les sections correspondantes ; le texte recopié vient de leurs transcriptions automatiques, l'image fait foi.
