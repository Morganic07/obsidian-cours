---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]], dans [[Operating System (index)]]. Note de cours sur les bases de l'administration : extraits du support (captures de texte, recopiées ici) et réponses de l'étudiante aux questions courtes. Le rendu correspondant est résumé dans [[TP1 (résumé)]].

## Obtenir de l'aide sur une commande

```bash
man command        # manuel
command --help     # aide courte
info command       # page info
```

Voir [[Commande man]], [[Option --help]] et [[Commande info]].

## `sudo`

Voir [[Commande sudo]] et [[Super-utilisateur root]].
- `sudo` signifie *superuser do* ;
- il permet aux utilisateurs autorisés d'exécuter des commandes avec les privilèges du super-utilisateur (root) ;
- il donne un accès élevé sans se connecter en tant que root ;
- il préserve la sécurité du système et le contrôle d'accès.

### `sudo` sans mot de passe (*passwordless*)

1. Ouvrir le fichier `sudoers` ([[Fichier sudoers]]) :

```bash
sudo visudo
```

2. Ajouter à la fin du fichier, en remplaçant `username` par le vrai nom :

```
username ALL=(ALL) NOPASSWD:ALL
```

### Mot de passe avec délai (*timestamp*)

1. `sudo visudo` ;
2. ajouter ou modifier la valeur `timestamp_timeout`. Exemple du support, pour un délai de 15 minutes (« plus de demande de mot de passe pendant 30 minutes après la première commande `sudo` réussie », voir point à vérifier 1) :

```
Defaults timestamp_timeout=15
```

## Changer de mot de passe

```bash
sudo passwd
```

Voir [[Commande passwd]].

- Pour des raisons de sécurité et de confidentialité, [[Ubuntu]] et les autres systèmes de type Unix **ne permettent pas de voir son mot de passe actuel**. Les mots de passe sont stockés sous forme hachée (« chiffrée ») dans des fichiers système : même les administrateurs ne peuvent pas les lire directement.
- **Où sont-ils stockés ?** Dans `/etc/shadow`, sous forme de valeurs hachées ([[Hachage de mot de passe]], [[Fichiers de mots de passe]]). Ce fichier ne révèle pas le mot de passe lui-même ; seuls les utilisateurs ayant les privilèges root peuvent y accéder.

## Disposition du clavier

Voir [[Disposition du clavier]].

**Temporaire** (ne survit pas à un redémarrage) :

```bash
setxkbmap <layout>
setxkbmap us
```

**Permanente** :
1. ouvrir le fichier : `sudo nano /etc/default/keyboard` ;
2. modifier la ligne `XKBLAYOUT` avec le code de disposition voulu :

```
XKBLAYOUT="us"
# ou
XKBLAYOUT="fr"
```

## Nom d'hôte (*hostname*)

Changer le nom d'hôte du système ([[Commande hostname]], [[Nom d'hôte]]) :

```bash
sudo hostname new_hostname
```

**Rôles du nom d'hôte** :
1. **Identification** : il identifie de façon unique un ordinateur ou un appareil sur le réseau ; chaque appareil doit avoir un nom distinct pour éviter conflits et confusions.
2. **Adresse lisible** : plutôt que des adresses IP difficiles à retenir, les noms d'hôte offrent une façon lisible de désigner les appareils.
3. **Fonctions réseau** : ils servent dans diverses fonctions réseau, dont l'adressage des mails et l'accès aux services.

**Utilité en réseau** :
1. **Résolution de noms** : les noms d'hôte sont traduits en [[Adressage IPv4 et CIDR|adresses IP]] par la résolution [[DNS]] (*Domain Name System*) ; quand on tape un nom dans un navigateur, les serveurs DNS le résolvent en adresse IP pour joindre le bon serveur.
2. **Réseau local** : on peut accéder à des appareils (imprimantes, serveurs, ordinateurs) par leur nom sans connaître leur IP, par exemple `ssh user@hostname`.
3. **Identification des services** : les noms d'hôte aident à repérer les services d'une machine (les services web tournent souvent sur des serveurs aux noms précis).

## Créer plusieurs fichiers et des arborescences

Voir [[Expansion d'accolades]], [[Commande touch]] et [[Commande mkdir]].

```bash
sudo touch test{1..3}.txt     # crée test1.txt, test2.txt, test3.txt
```

`mkdir` au lieu de `touch` pour créer des arborescences de répertoires :

```bash
mkdir -p semester/{first/{os,uc},second/{cn,db,ns,cs},third/{iot,sp,dc}}
```

![[séance TP1 - image12.png]]
*Figure : la commande `mkdir -p semester/{…}`, puis `tree semester/` : first (os, uc), second (cn, cs, db, ns), third (dc, iot, sp) ; 13 répertoires, 0 fichier.*

Voir [[Commande tree]].

## Ajouter du texte dans un fichier

```bash
touch semester/first/semester.txt && echo "first" | cat > semester/first/semester.txt
```

Ajoute « first » dans le fichier `semester.txt` ([[Redirection et tube]]).

## `chmod` récursif

Le manuel de [[Commande chmod|chmod]] indique l'option `-R` pour changer le mode de tous les éléments d'un répertoire :

```
-R, --recursive
       change files and directories recursively
```

D'où :

```bash
sudo chmod -R 444 semester/
```

Voir [[Permissions Unix]].

## Questions courtes (réponses de l'étudiante)

La numérotation de la note repart à 1 à chaque question (voir point à vérifier 4).

- **`whoami` ou `hostname`** : `whoami` ([[Commande whoami]]) donne l'utilisateur connecté à la machine ; `hostname` le nom de la machine utilisée.
- **Raccourcis de `cd`** ([[Commande cd]]) :
  - `cd ..` : va au répertoire parent (de `/home/momo/test` à `/home/momo`) ;
  - `cd ~` : comme `cd` seul, va au [[Répertoire personnel]] de l'utilisateur ;
  - `cd -` : revient au répertoire précédent (de `/etc/apt` à `/home/momo` si l'on venait de là).
- **`./`** représente le répertoire courant ([[Chemin de fichier]]).
- **Éteindre le système** : `sudo shutdown now` ou `sudo poweroff` ([[Commandes shutdown et poweroff]]).
- **Informations système** : [[Commande uname|uname]] ; d'après le manuel, `-r` donne la version du [[Noyau]].

![[séance TP1 - image5.png]]
*Figure : `uname -r` → `6.6.30-02726-gb84bbdf6955e`.*

- **`apt upgrade` ou `apt full-upgrade`** ([[APT]]) : `apt upgrade` ne fait que mettre à jour les paquets installés, sans permettre d'installer ni de supprimer des paquets ; `apt full-upgrade` peut en supprimer et en installer de nouveaux.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Délai sudo** : le texte dit 15 minutes mais l'explication entre parenthèses dit 30. **Vérifié sur l'image** : l'incohérence est bien dans le support d'origine. `timestamp_timeout=15` correspond à 15 minutes (complément).
2. **`sudo chmod -R 444 semester/`** : retire aussi le droit `x` des dossiers, qui ne peuvent alors plus être traversés (complément).
3. **`sudo hostname`** : le changement ne dure que jusqu'au redémarrage ; le fichier `/etc/hostname` rend le changement permanent (complément).
4. **Question 1 « chmod -R »** et renvoi à l'ordre des questions : la numérotation de la note repart à 1 plusieurs fois, ce qui ne permet pas de relier chaque réponse à son énoncé.
5. **« hashed (encrypted) »** : le support assimile hachage et chiffrement ; un hachage n'est pas réversible, contrairement à un chiffrement (complément).
6. **`apt upgrade` « n'installe aucun paquet »** : le manuel d'`apt` (cité dans [[TP1 (résumé)]]) dit que de nouveaux paquets peuvent être installés pour satisfaire des dépendances ; la réponse est trop stricte.
