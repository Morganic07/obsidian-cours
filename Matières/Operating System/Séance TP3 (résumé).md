---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Cours TP3.docx|Cours TP3]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/Cours TP3.docx|Cours TP3]], dans [[Operating System (matière)]]. Séance de TP sur le réseau sous Linux (adresse IP, interfaces, `/etc/hosts`, `ping`, Netplan) puis sur la sauvegarde de fichiers par script. Les extraits du support (captures de texte) sont recopiés ; les captures du terminal sont intégrées.

## Adresse IP

Définition du support : l'IP (*Internet Protocol*, voir [[Adressage IPv4 et CIDR]]) est une étiquette numérique attribuée à un appareil qui participe à un réseau utilisant IPv4. Deux rôles :
- **identification de l'appareil** : il identifie de façon unique un appareil sur le réseau ;
- **adressage de localisation** : il indique la position de l'appareil dans le réseau pour faciliter la communication.

Voir son adresse IP ([[Commande ip]], [[Commande ifconfig]]) :

```bash
ip addr          # ou : ip address
sudo ifconfig
```

![[Séance TP3 - image13.png]]
*Figure : sorties de `ip address` et de `sudo ifconfig` : interface `lo` (127.0.0.1/8, ::1) et interface `eth0` (100.115.92.201/28, masque 255.255.255.240, diffusion 100.115.92.207, IPv6 fe80::216:3eff:fe68:6580), avec compteurs RX et TX.*

Annotations de l'étudiante sur la capture (« `ip address` et `sudo ifconfig` ont quasiment la même sortie ») :

| Champ | Signification |
|---|---|
| `eth0` | première interface Ethernet (la note dit « internet ») |
| `lo` | interface de bouclage ([[Adresse de bouclage]], *loopback*) |
| `inet` | adresse IPv4 |
| `netmask` | masque de sous-réseau |
| `broadcast` | adresse de diffusion |
| `inet6` | adresse [[IPv6]] |
| `RX` | paquets reçus, ici 199 578 (393,1 Mo) |
| `TX` | paquets envoyés, ici 48 988 (12,4 Mo) |
| *flags* | état de l'interface |

### Interfaces réseau possibles

Voir [[Interface réseau]].
- **`lo`** (*loopback interface*) : interface réseau virtuelle pour tester le système et interagir avec lui ; l'ordinateur s'envoie des données à lui-même par le réseau sans passer par le matériel physique (carte Ethernet ou Wi-Fi).
- **`eth0`** : interface Ethernet ; le 0 peut être un autre nombre.
- **`wlan0`** : interface Wi-Fi ; même remarque.

## Résolution de noms et fichier `/etc/hosts`

- Convertir un nom d'hôte en adresse IP s'appelle la **résolution d'adresse** ; elle est faite par le [[DNS]] (*Domain Name Server*).
- Le fichier `/etc/hosts` ([[Fichier hosts]]), sous [[Ubuntu]] et les autres [[Linux]], est un mécanisme local simple qui associe des noms d'hôte à des adresses IP.
- Il fait partie de la configuration réseau du système et sert surtout à la résolution DNS locale, aux tests rapides et au blocage d'accès.

![[Séance TP3 - image3.png]]
*Figure : `cat /etc/hosts` : `127.0.1.1 penguin`, `127.0.0.1 localhost`, `100.115.92.201 penguin`, puis les entrées IPv6 (`::1 localhost ip6-localhost ip6-loopback`, `ff02::1 ip6-allnodes`, `ff02::2 ip6-allrouters`).*

**Points clés** du support :
1. le fichier est du texte brut, modifiable avec n'importe quel [[Éditeur de texte]] ([[Éditeur nano|nano]], [[Vim|vim]], [[Gedit|gedit]]) ;
2. les modifications prennent effet immédiatement, sans redémarrer de service ;
3. toujours vérifier que l'entrée `localhost` (127.0.0.1) est présente et correcte, pour éviter des problèmes de fonctionnement.

**Ajouter une entrée locale** :

```bash
sudo nano /etc/hosts
```

puis, à la fin du fichier, ajouter sans les chevrons :

```
<ip of the local system> <hostname>
```

Enregistrer : le changement est immédiat, pas de redémarrage.

## Tester la connectivité avec `ping`

Vérifier qu'une adresse IP répond ([[Commande ping]], [[Nom d'hôte]]) :

```bash
ping <hostname>
ping <IP address>
```

![[Séance TP3 - image15.png]]
*Figure : `ping youtube.com` (2 paquets reçus, 0 % de perte), `ping penguin` (127.0.1.1), `ping 127.0.0.1` répondent ; `ping 238.239.22.31` : 8 paquets envoyés, 0 reçu, 100 % de perte.*

Annotations : ping de YouTube, du nom de la machine et de son IP fonctionnent ; ping d'une IP aléatoire ne fonctionne pas.

## Configurer l'IP à la main

- Sur les versions récentes d'Ubuntu, les fichiers de configuration réseau sont dans **`/etc/netplan`** ([[Netplan]]).
- Ils sont au format **[[YAML]]** et configurent les interfaces réseau ; par exemple `01-netcfg.yaml` dans `/etc/netplan/`.
- Le YAML est sensible à l'indentation, comme Python.
- Si Netplan n'est pas installé, chercher le fichier `/etc/network/interfaces`.

## Sauvegarde (*Backup*)

Définition du support ([[Sauvegarde de fichier]]) : sauvegarder un fichier, c'est en créer une copie à intervalles réguliers et la stocker à un autre endroit du système. Si l'original est perdu, corrompu ou modifié, on garde une copie à jour ailleurs.

### Exemple 1 : la date

Script qui crée `date.txt` et y ajoute la date courante toutes les 2 secondes ([[Boucle (programmation)|boucle infinie]], [[Commande date]], [[Commande sleep]]) :

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
done   # absent de la note, voir point à vérifier 2
```

Script qui sauvegarde `date.txt` toutes les 15 secondes ([[Commande cp]]) :

```bash
#!/bin/bash
# Define the source file and destination directory
SOURCE="/home/user/data/date.txt"
DESTINATION="/home/backup/"
# Infinite loop to copy the file every 15 seconds
while true; do
  # Copy the file to the destination, replacing any existing file
  cp "$SOURCE" "$DESTINATION"
  # Wait for 15 seconds before the next copy
  sleep 15
done   # absent de la note
```

### Exemple 2 : la mémoire

Script qui ajoute toutes les 5 secondes l'état de la mémoire ([[Commande free|free -h]]) dans `memory.txt` :

```bash
#!/bin/bash
while true
do
    free -h >> memory.txt
    sleep 5
done
```

Script qui sauvegarde `memory.txt` toutes les 20 secondes :

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

Pour lancer les deux scripts d'un exemple en même temps, on peut utiliser `&` (voir [[Séance TP2 (résumé)]], [[Tâche en arrière-plan]]) — complément, la note ne le dit pas.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`echo "$Backup Successful!"`** : le `$` devant « Backup » est probablement une faute, la variable n'existe pas et le mot disparaîtrait de l'affichage (complément ; alerte de la transcription confirmée).
2. **Script `time.sh` et de sauvegarde** : le `done` final de la boucle est absent des extraits recopiés (la note s'arrête avant). Le script de copie utilise des chemins `/home/user/...` génériques (complément).
3. **Dernière ligne de la définition de l'IP** : la transcription la dit coupée, le mot manquant est « communication » ; fausse alerte.
4. **Mélange des interfaces** : `ifconfig` demande le paquet `net-tools`, ce qui n'est pas dit dans la note (complément).
5. **Exemple 2, chemins inversés** : le script de mémoire écrit `memory.txt` dans le répertoire courant, alors que la sauvegarde copie depuis `/home/momo/backup/` vers `/home/momo/data/` ; les noms de dossiers semblent intervertis par rapport à l'exemple 1 (complément, à vérifier).
6. **« Eth 0 is the first internet interface »** : il s'agit de la première interface Ethernet.
