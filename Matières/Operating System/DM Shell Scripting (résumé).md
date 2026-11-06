---
type: source
tags: [year2]
sources: ["[[DM Shell Scripting]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[DM Shell Scripting]] (TP du 30/09/2024), dans [[Operating System (matière)]]. Un énoncé commenté de 19 questions de cours (shell, Bash, variables, tests, boucles), puis 11 tâches de DM avec les réponses de l'étudiante. Il apprend à écrire des [[Script Bash]]. Une capture d'écran (`lscpu`). Les réponses sont celles de l'étudiante, pas un corrigé officiel.

## Partie 1 : questions de cours

### 1. Qu'est-ce qu'un shell ?

- Un [[Shell et Bash|shell]] est une [[Interface en ligne de commande]] (CLI) qui permet à l'utilisateur d'interagir avec le [[Système d'exploitation]].
- C'est un programme qui prend des commandes textuelles et les transmet au système pour exécution.
- Exemples : [[Bourne Shell (sh)]], Bash (*Bourne-Again Shell*), [[Shell rbash|rbash]], [[Shell dash|dash]].

### 2. Quels shells le système supporte-t-il ?

`cat /etc/shells` ([[Fichier shells]]). Sortie relevée :

```
# /etc/shells: valid login shells
/bin/sh
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/bin/dash
/usr/bin/dash
```

### 3. Où se trouve bash ?

`which bash` ([[Commande which]]) → `/usr/bin/bash`.

### 4. Répertoire de travail courant

`pwd` ([[Commande pwd]]) → `/home/momo`.

### 5. Créer un répertoire `ostasks` et s'y placer

```bash
cd /home/{user name}
mkdir ostasks
cd ostasks
```

Voir [[Commande cd]], [[Commande mkdir]], [[Répertoire personnel]].

### 6. Créer `firstprogram.sh`

`touch {file name}.sh` ([[Commande touch]]), l'ouvrir dans un éditeur ([[Gedit|gedit]], [[Éditeur nano|nano]], [[Vim|vim]]), y afficher « Hello », exécuter et observer la sortie.

### 7. Donner la permission d'exécution

`chmod +x {file name}.extension` ([[Commande chmod]], [[Permissions Unix]]).

### 8. Enregistrer puis afficher la date et l'heure

```bash
#!/bin/bash
echo "hello"
current_datetime=$(date)
echo "Current Date and Time: $current_datetime"
```

Voir [[Substitution de commande]] et [[Commande date]].

### 9. Commentaires

On écrit `#` avant le commentaire : `# this is a comment` ([[Commentaire en Bash]]).

### 10. Deux types de variables

Voir [[Variable Bash]].
1. **Variables système** (majuscules) :

```bash
echo "$BASH"          # nom du shell
echo "$BASH_VERSION"  # version de bash
echo "$HOME"          # répertoire personnel
echo "$PWD"           # répertoire de travail courant
```

2. **Variables définies par l'utilisateur** (minuscules) :

```bash
temp=10
echo "the value of temp = $temp"
```

### 11. Variable utilisateur de la question 8

`current_datetime`.

### 12. Lire une saisie au terminal

Voir [[Commande read]].

```bash
#! /bin/bash
echo "Enter name: "
read name
echo "Entered name: $name"
# lire sur la même ligne
read -p "username: " username_val     # -p : saisie sur la même ligne que le prompt
read -s -p "password: " password_val  # -s : saisie masquée (mot de passe)
echo "username : $username_val"
echo "password: $password_val"
```

### 13. Tableaux (*arrays*)

```bash
# lire des entrées et les ranger dans un tableau
echo "enter names: "
read -a names       # -a : lire l'entrée comme un tableau
echo "names: ${name[0]}, ${name[1]}"   # sic : voir point à vérifier 2
```

Voir [[Tableau (programmation)]].

### 14. `if` en Bash

```bash
#!/bin/bash
if [ condition ]
then
  statement
fi
```

Voir [[Structure conditionnelle]] et [[Opérateur de comparaison]].

**Opérateurs de comparaison d'entiers**

| Opérateur | Sens | Exemple |
|---|---|---|
| `-eq` | égal à | `if [ "$a" -eq "$b" ]` |
| `-ne` | différent de | `if [ "$a" -ne "$b" ]` |
| `-gt` | strictement supérieur | `if [ "$a" -gt "$b" ]` |
| `-ge` | supérieur ou égal | `if [ "$a" -ge "$b" ]` |
| `-lt` | strictement inférieur | `if [ "$a" -lt "$b" ]` |
| `-le` | inférieur ou égal | `if [ "$a" -le "$b" ]` |
| `<` | strictement inférieur | `if (( "$a" < "$b" ))` |
| `<=` | inférieur ou égal | `if (( "$a" <= "$b" ))` |
| `>` | strictement supérieur | `if (( "$a" > "$b" ))` |
| `>=` | supérieur ou égal | `if (( "$a" >= "$b" ))` |

**Opérateurs de comparaison de chaînes**

| Opérateur | Sens | Exemple |
|---|---|---|
| `=` | égal à | `if [ "$a" = "$b" ]` |
| `==` | égal à | `if [ "$a" == "$b" ]` |
| `!=` | différent de | `if [ "$a" != "$b" ]` |
| `<` | inférieur dans l'ordre alphabétique [[Code ASCII\|ASCII]] | `if [[ "$a" < "$b" ]]` |
| `>` | supérieur dans l'ordre ASCII | `if [[ "$a" > "$b" ]]` |
| `-z` | chaîne nulle, de longueur zéro | `if [ -z "$string" ]` |

Exemple :

```bash
# comparer deux chaînes
word="school"
if [ "$word" = "school" ]
then
  echo "condition is true"
fi
```

### 15 et 16. `if … else` et `if … elif … else`

```bash
if [ condition ]
then
  statement
else
  statement
fi

if [ condition ]
then
  statement
elif [ condition ]
then
  statement
else
  statement
fi
```

### 17. ET et OU logiques

Voir [[Opérateur logique]].

```bash
if [ condition ] && [ condition ]   # logical AND
if [ condition -a condition ]       # logical AND
if [[ condition && condition ]]     # logical AND
if [ condition ] || [ condition ]   # logical OR
if [ condition -o condition ]       # logical OR
if [[ condition || condition ]]     # logical OR
```

(chacun suivi de `then statement fi`).

### 18. Boucle `while`

Voir [[Boucle (programmation)]] et [[Arithmétique en Bash]].

```bash
while [ condition ]
do
  command 1
  command 2
done

# exemple : afficher les valeurs jusqu'à 10
n=1
while [ $n -le 10 ]        # ou : while (( $n <= 10 ))
do
  echo "$n"
  n=$(( n+1 ))             # ou : (( n++ ))
done
```

### 19. Boucle `for`

```bash
for (( initialization; test condition; loop counter ))
do
  command 1
  command 2
done
```

## Partie 2 : le DM (énoncés et réponses)

### Tâche 1 : `lshw`

*Énoncé* : lancer `lshw`, expliquer son rôle, trouver la solution si la commande ne marche pas.

*Réponse* : `lshw` ([[Commande lshw]]) doit être installé : `sudo apt install lshw` ([[APT]], [[Commande sudo]]). Il liste le matériel de l'ordinateur ; pour une vue complète, lancer `sudo lshw`.

### Tâche 2 : les 500 premiers nombres premiers

*Énoncé* : script Bash qui trouve les 500 premiers [[Nombre premier|nombres premiers]].

*Démarche* : l'étudiante écrit d'abord le programme en Python, puis le traduit en Bash. Elle s'appuie sur :
- **Propriété** : tout nombre non premier $n > 2$ admet un diviseur premier $p$ tel que $p \le \sqrt{n}$.
- **Lemme** : si $n$ n'a aucun diviseur entre $2$ et $\sqrt{n}$, alors $n$ est premier.

Version Python :

```python
NombreActuel = 2
NombreActuelPremier = 0
CompteurNombrePremier = 0
while True:
    NombreActuelPremier = 1          # on suppose le nombre premier
    for i in range(2, int(NombreActuel**0.5)):
        if NombreActuel % i == 0:
            NombreActuelPremier = 0  # i divise : pas premier
            break
    if NombreActuelPremier == 1:
        print(NombreActuel)
        CompteurNombrePremier += 1
    if CompteurNombrePremier == 500: # 500 premiers trouvés : arrêt
        break
    NombreActuel += 1
```

Version Bash. Comme on ne peut pas utiliser `sqrt` ni `**0.5` dans la condition, on remplace $i \le \sqrt{n}$ par $i^2 \le n$ (équivalent car $i$ et $n$ sont positifs). Pour les comparaisons arithmétiques, on utilise `(( condition ))` au lieu de `[ condition ]`.

```bash
#!/bin/bash
NombreActuel=2
CompteurNombrePremier=0
while [ true ]
do
  NombreActuelPremier=1
  for ((i=2; i*i<=NombreActuel; i++))
  do
    if ((NombreActuel%i==0))
    then
      NombreActuelPremier=0
      break
    fi
  done
  if ((NombreActuelPremier == 1))
  then
    echo $NombreActuel
    ((CompteurNombrePremier++))
  fi
  if ((CompteurNombrePremier==500))
  then
    break
  fi
  ((NombreActuel++))
done
```

### Tâche 3 : nombre de cœurs

```bash
#! /bin/bash
echo "There is $(nproc --all) cores on your machine"
```

Voir [[Commande nproc]] et [[Cœur de processeur]].

### Tâche 4 : état des cœurs

*Énoncé* : par défaut tous les cœurs sont en ligne (*online* = actif, voir [[Cœur en ligne et hors ligne]]) ; trouver la commande qui donne leur état.

*Réponse* : [[Commande lscpu|lscpu]].

![[DM Shell Scripting - image1.png]]
*Figure : sortie de `lscpu` sur la machine de l'étudiante : architecture x86_64, 2 CPU, « On-line CPU(s) list: 0,1 », Intel Celeron N3350 @ 1.10GHz, 1 thread par cœur, 2 sockets.*

La ligne « On-line CPU(s) list » donne les [[Processeur|CPU]] en ligne (ici 0 et 1, chaque CPU étant indexé par un numéro). S'il y avait des CPU hors ligne, une ligne supplémentaire « Off-line CPU(s) list » apparaîtrait. Pour n'extraire que l'état :

```bash
lscpu | grep "On-line CPU(s) list"
lscpu | grep "Off-line CPU(s) list"
```

`grep` extrait la ligne qui contient le motif ([[Commande grep]], [[Redirection et tube|tube]]).

### Tâche 5 : cœur par défaut

Les cœurs sont numérotés de 0 à n ; le cœur par défaut est le **cœur 0** (`default_core=0` dans le script suivant).

### Tâche 6 : mettre hors ligne tous les cœurs sauf le défaut

Commande unitaire (remplacer X par l'indice du CPU), voir [[Commande tee]] :

```bash
echo 0 | sudo tee /sys/devices/system/cpu/cpuX/online
```

Boucle :

```bash
#!/bin/bash
total_cores=$(nproc)
default_core=0
for ((i=0; i<total_cores; i++)); do
  if [ $i -ne $default_core ]; then
    echo "Désactivation du core $i"
    echo 0 | sudo tee /sys/devices/system/cpu/cpu$i/online
  fi
done
echo "Tous les cores sauf le core par défaut ($default_core) ont été désactivés."
```

### Tâche 7 : remettre les cœurs en ligne

```bash
echo 1 | sudo tee /sys/devices/system/cpu/cpuX/online
```

```bash
#!/bin/bash
total_cores=$(nproc)
for ((i=0; i<total_cores; i++)); do
  echo "Activation du core $i"
  echo 1 | sudo tee /sys/devices/system/cpu/cpu$i/online
done
echo "Tous les cores ont été activés."
```

### Tâche 8 : créer cinq fichiers texte

*Énoncé* : lire le nom de cinq fichiers et créer cinq fichiers texte dans le répertoire courant.

```bash
#!/bin/bash
echo "Entrez le nom des fichiers"
for ((i=1; i<=5; i++))
do
  read -p "Entrez le nom du fichier $i : " nomfichier
  touch "$nomfichier".txt
  echo "Le fichier $nomfichier.txt a été créé"
done
```

### Tâche 9 : supprimer ces fichiers

```bash
#!/bin/bash
for ((i=1; i<=5; i++)) do
  echo "entrez le nom du fichier $i à supprimer"
  read fichier
  rm "$fichier".txt
done
echo "your files have been deleted"
```

Voir [[Commande rm]].

### Tâche 10 : afficher la date `n` fois, toutes les 2 secondes

```bash
#! /bin/bash
echo "entrez le nombre de récursion : "
read n
for ((i = 1; i <=n; i++)) do
  date
  sleep 2
done
```

Voir [[Commande sleep]].

### Tâche 11 : comparer deux chaînes

```bash
#! /bin/bash
read -p "Entrez chaine 1 : " chaine1
read -p "Entrez chaine 2 : " chaine2
if [ $chaine1 = $chaine2 ]; then
  echo "same"
else
  echo "not same"
fi
```

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les exemples de l'énoncé utilisent des guillemets typographiques et des tirets longs (`–eq`, `–p`, `–a`) ; ils sont réécrits ici avec des caractères ASCII, seuls valables dans un vrai script.

1. **Version Python des nombres premiers** : `range(2, int(NombreActuel**0.5))` exclut la racine carrée, si bien que 4 serait jugé premier et 9 aussi (complément). La version Bash (`i*i <= n`) est correcte. Les caractères accentués du fichier sont abîmés (« Ã »).
2. **Tâche 12 sur les tableaux** (question 13 de l'énoncé) : `read -a names` puis `${name[0]}` : nom différent, l'affichage serait vide.
3. **Tâche 11** : `[ $chaine1 = $chaine2 ]` sans guillemets échoue si une chaîne est vide ou contient des espaces (complément).
4. **Tâche 7** : le script remet en ligne aussi le cœur 0 (`cpu0/online` n'existe souvent pas) ; l'énoncé voulait tous les cœurs sauf le défaut (complément).
5. **Énoncé tronqué** : « Write a bash script that reads the names of five files and creates five text files in the current » est coupé dans la note (la liste des tâches en tête donne la fin : « current working directory »).
6. **Tâches 6 et 7** : après la mise hors ligne, `nproc` ne compte plus que les cœurs en ligne ; la boucle de la tâche 7, bornée par `$(nproc)`, ne parcourt donc pas les cœurs désactivés (complément, à vérifier).
7. **Capture `lscpu`** : les deux dernières lignes (Flags) sont coupées sur le bord droit de l'image (transcription). Sans importance pour l'exercice.
