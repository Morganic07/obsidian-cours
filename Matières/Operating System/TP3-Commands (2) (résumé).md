---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF TP3-Commands (2) ([[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]) (8 pages, 25 novembre 2024, « TP-3 : Network Management, and Backup »), dans [[Operating System (matière)]]. Sujet de TP, en anglais. Le rendu est [[TP3 (résumé)]] ; les notes de cours, [[Séance TP3 (résumé)]]. Les trois figures du sujet sont des extraits de fichiers texte (hosts, YAML) : elles sont recopiées en blocs de code, sans image. Aucun corrigé.

## Partie 1 : réseau

### 1. Adresse IPv4

L'IP (*Internet Protocol*, voir [[Adressage IPv4 et CIDR]]) est une étiquette numérique attribuée à un appareil d'un réseau IPv4. Deux rôles :
- **identification de l'appareil** : identifie de façon unique un appareil sur le réseau ;
- **adressage de localisation** : indique sa position dans le réseau pour faciliter la communication.

Trouver l'adresse IP locale ([[Commande ifconfig]], [[Commande ip]]) :

```bash
ifconfig        # nécessite le paquet net-tools
ip address      # nécessite le paquet iproute2
```

Si une commande ne marche pas, installer le paquet ([[APT]]) :

```bash
sudo apt update
sudo apt install net-tools
sudo apt install iproute2
```

**Figure 1 : exemple de sortie de `ifconfig` à trois interfaces** (texte du sujet) :

```
eth0   Link encap:Ethernet HWaddr 00:1a:2b:3c:4d:5e
       inet addr:192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0
       inet6 addr: fe80::21a:2bff:fe3c:4d5e/64 Scope:Link
       UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
       RX packets:4321 errors:0 dropped:0 overruns:0 frame:0
       TX packets:5678 errors:0 dropped:0 overruns:0 carrier:0
       collisions:0 txqueuelen:1000
       RX bytes:9876543 (9.8 MB) TX bytes:12345678 (12.3 MB)
       Interrupt:20 Memory:de000000-de100000

wlan0  Link encap:Ethernet HWaddr 00:11:22:33:44:55
       inet addr:192.168.0.105 Bcast:192.168.0.255 Mask:255.255.255.0
       ...
       RX packets:1234 ... TX packets:5678 ...
       RX bytes:1234567 (1.2 MB) TX bytes:7654321 (7.6 MB)

eth1   Link encap:Ethernet HWaddr 00:1a:2b:3c:4d:6f
       inet addr:10.0.0.50 Bcast:10.0.0.255 Mask:255.255.255.0
       ...
       RX packets:567 ... TX packets:1234 ...
       RX bytes:678912 (678.9 KB) TX bytes:987654 (987.7 KB)
```

Explication du sujet ([[Interface réseau]]) :

| Interface | Type | IPv4 | Diffusion | Masque | Trafic |
|---|---|---|---|---|---|
| `eth0` | Ethernet classique | 192.168.1.100 | 192.168.1.255 | 255.255.255.0 | 4 321 paquets reçus, 5 678 envoyés ; 9,8 Mo reçus, 12,3 Mo envoyés |
| `wlan0` | Wi-Fi | 192.168.0.105 | 192.168.0.255 | 255.255.255.0 | 1 234 reçus, 5 678 envoyés ; 1,2 Mo / 7,6 Mo |
| `eth1` | deuxième interface Ethernet (autre carte réseau) | 10.0.0.50 | 10.0.0.255 | 255.255.255.0 | 567 reçus, 1 234 envoyés ; 678,9 Ko / 987,7 Ko |

### 2. Résolution DNS locale

- Convertir des noms d'hôte en adresses IP s'appelle la **résolution d'adresse** ; elle est faite par le [[DNS]] (*Domain Name Server*).
- Le fichier `/etc/hosts` ([[Fichier hosts]]) sous Ubuntu et Linux est un mécanisme local et simple qui associe noms d'hôte et adresses IP.
- Il fait partie de la configuration réseau de l'OS ; il sert surtout à la résolution DNS locale, aux tests rapides et au blocage d'accès.

**Figure 2 : exemple de fichier `/etc/hosts` typique** :

```
127.0.0.1    localhost
127.0.1.1    my-machine-name

# Custom mappings
192.168.1.100  dev-server
10.0.0.5       test-environment

# Block a website
127.0.0.1    example.com
```

(Associer `example.com` à `127.0.0.1` bloque le site en le renvoyant vers la machine elle-même, [[Adresse de bouclage]].)

**Points clés** :
1. fichier texte brut, modifiable avec n'importe quel [[Éditeur de texte]] (nano, vim, gedit) ;
2. les modifications prennent effet immédiatement, sans redémarrer de service ;
3. toujours garder l'entrée `localhost` (127.0.0.1) présente et correcte ;
4. il sert aux petites tâches ou au dépannage, car il ne passe pas à l'échelle comme le DNS.

**2.2 Ajouter une entrée locale** : ouvrir le fichier et écrire l'IP et le nom d'hôte à la fin.

```bash
sudo nano /etc/hosts
```

puis, sans les chevrons :

```
<ip of the local system> <hostname>
```

L'IP locale et le nom d'hôte se trouvent avec `ifconfig` et `hostname` ([[Commande hostname]]).

**2.3 Tester le nom** ([[Commande ping]]) :

```bash
ping <hostname>
```

Si le nom est bien configuré dans `/etc/hosts`, on reçoit une réponse.

### 3. Configurer l'adresse IP à la main

Plusieurs fichiers et méthodes permettent de configurer les interfaces ; le fichier à modifier dépend de la distribution et du gestionnaire réseau. Depuis **Ubuntu 18.04**, l'outil par défaut est **[[Netplan]]**, qui utilise des fichiers [[YAML]] dans `/etc/netplan`.

**3.1 Voir le fichier** :

```bash
cat /etc/netplan/<.yaml>
```

**3.2 Créer le fichier** s'il n'existe pas :

```bash
sudo nano /etc//netplan/01-netcfg.yaml
```

Le YAML suit la règle d'indentation de Python : une mauvaise indentation produit des erreurs de syntaxe, la configuration est alors invalide ou ignorée, et les interfaces peuvent ne pas démarrer ou les réglages ne pas s'appliquer.

**3.3 Exemple d'IP statique** (figure 3.1), pour l'interface `eth0` :

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

Voir [[Passerelle par défaut]].

**3.4 Exemple d'IP dynamique** (figure 3.2) : au lieu d'une attribution manuelle, obtenir l'adresse automatiquement par [[DHCP]] (*Dynamic Host Configuration Protocol*) :

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: yes
```

### Tâche 1

- a. Trouver l'adresse IP du système ; relever dans la sortie les interfaces réseau et les adresses ; les écrire explicitement avec la capture.
- b. Capturer le contenu de `/etc/hosts`.
- c. Capturer le contenu du fichier `.yaml`.
- d. Si aucun `.yaml` n'est dans `/etc/netplan/`, le système utilise un autre fichier de configuration réseau : le trouver. Indice : `cat /etc/network/interfaces`, `ls /etc/system/network/`.
- e. Trouver l'IP locale et l'ajouter dans `/etc/hosts` avec le bon nom d'hôte.

## Partie 2 : sauvegarde d'un fichier

**Définition** ([[Sauvegarde de fichier]]) : sauvegarder un fichier, c'est en créer une copie à intervalles réguliers et la stocker ailleurs dans le système ; si l'original est perdu, corrompu ou modifié, on dispose d'une copie à jour.

### 4.1 Méthode

1. Créer un répertoire `data` dans `/home/user` et s'y placer.
2. Créer un fichier de test qui se met à jour en continu, avec le script `time.sh` (`sudo nano time.sh`) :

```bash
#!/bin/bash

# Infinite loop to append the current date and time every 2 seconds
while true
do
    # Get the current date and time in a particular format
    current_time=$(date '+%Y-%m-%d %H:%M:%S')

    # Append the current time to the file
    echo "$current_time" >> date.txt

    # Wait for 2 seconds before repeating
    sleep 2
done
```

3. Enregistrer et fermer ; donner les droits d'exécution ([[Commande chmod]]) ; lancer en arrière-plan avec `./time.sh &` ([[Tâche en arrière-plan]]).
4. Lancer plusieurs fois `cat date.txt` : le contenu doit grandir ; sinon, revoir les étapes.
5. Créer un répertoire `backup` dans `/home/user`. Source : `/home/user/data/date.txt` ; destination : `/home/user/backup/`.
6. Dans `/home/user/backup/`, créer `backup.sh` :

```bash
#!/bin/bash

# Define the source file and destination directory
SOURCE="/home/user/data/date.txt"
DESTINATION="/home/backup/"

# Infinite loop to copy the file every 15 seconds
while true; do
  # Copy the file to the destination, replacing any existing file
  cp "$SOURCE" "$DESTINATION"

  # Notify the user of the successful copy operation
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $Backup Successful!"

  # Wait for 15 seconds before the next copy
  sleep 15
done
```

7. Enregistrer, donner les droits d'exécution, lancer avec `./backup.sh &`.
8. Dans le dossier de sauvegarde, observer `date.txt` : il doit se mettre à jour toutes les 15 secondes ; le terminal affiche « Backup Successful! » toutes les 15 secondes.
9. Les « trois » tâches tournant en arrière-plan, les arrêter toutes ([[Commande jobs]], [[Commandes fg et bg]]) :

```bash
jobs
fg <job ID>
# puis Ctrl + C ; recommencer jusqu'à ce que toutes les tâches soient supprimées
```

### Tâche 2

- a. `free –h` affiche la RAM et le swap totaux, utilisés et libres ([[Commande free]]). Écrire un script Bash qui ajoute en continu la sortie de `free –h` à `memory.txt` toutes les 5 secondes.
- b. Écrire un script qui sauvegarde en continu `memory.txt` à un autre endroit toutes les 20 secondes.
- c. Terminer toutes les tâches de fond correspondantes avec les commandes appropriées.

## Notions mobilisées

[[Shell et Bash]], [[Script Bash]], [[Redirection et tube]], [[Permissions Unix]] (droit d'exécution des scripts), [[Processus]] (tâches de fond), [[Système de fichiers]].

## Points à vérifier

1. Dans `backup.sh`, la destination est `/home/backup/` alors que le texte annonce `/home/user/backup/` ; l'affichage utilise `$Backup`, variable jamais définie.
2. Le sujet nomme le fichier `time.sh` « sudo nano time.sh » : `sudo` n'est pas nécessaire pour un fichier du répertoire de l'utilisateur (complément).
3. **« Trois tâches » en arrière-plan** : la méthode n'en lance que deux (`time.sh` et `backup.sh`) ; à vérifier.
4. **Légende de la figure 3.2** : elle reprend « Example Static IP Configuration » alors qu'il s'agit de la configuration dynamique (DHCP), annoncée comme telle dans le titre de la section 3.4.
5. **Indice de la tâche 1 d** : `/etc/system/network/` n'est pas un chemin standard (on attendrait par exemple `/etc/systemd/network/`) ; complément, à vérifier.
6. **`gateway4`** : clé dépréciée dans les versions récentes de Netplan au profit de `routes` (complément).
