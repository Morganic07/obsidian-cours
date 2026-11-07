---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]], dans [[Cours/Informatique/OS/_index|Operating System]]. Fiche de référence rédigée par l'étudiante (mélange de français et d'anglais) : commandes de base, `cat`, `chmod`, puis langage Bash. Une seule image, une capture de `shuf`.

## Tableau des commandes de base

Voir [[Shell et Bash]] et [[Interface en ligne de commande]].

| Commande | Rôle |
|---|---|
| `cat /etc/shells` | Voir quels shells le système supporte ([[Fichier shells]]) |
| `which bash` | Voir où se trouve l'exécutable `bash` ([[Commande which]]) |
| `rm filename.ext` | Supprimer un fichier ([[Commande rm]]) |
| `rmdir DirectoryName` | Supprimer un répertoire **vide** ([[Commande rmdir]]) |
| `ls` | Lister les fichiers du répertoire courant ([[Commande ls]]) |
| `cd` | Changer de répertoire courant ([[Commande cd]]) |
| `sudo nano testfile.sh` | Ouvrir `testfile.sh` dans [[Éditeur nano\|nano]] ; le fichier est créé s'il n'existe pas ([[Commande sudo]]) |
| `sh testfile.sh` | Exécuter un programme dans le shell « avec l'interpréteur bash », quel que soit le [[Shebang\|shebang]] (voir Erreurs du cours) |
| `./testfile.sh` | Exécuter en respectant le shebang ; exige la permission d'exécution ([[Exécution d'un script]]) |
| `sudo apt update` | Télécharge seulement la liste des nouvelles versions de paquets disponibles dans les dépôts, sans rien mettre à jour ([[APT]]) |
| `sudo apt upgrade` | Installe les nouvelles versions des paquets installés, après un `apt update` |
| `date` | Affiche la date courante ([[Commande date]]) |
| `pwd` | *Print working directory* : affiche le répertoire courant ([[Commande pwd]]) |
| `whoami` | Affiche le nom d'utilisateur ([[Commande whoami]]) |
| `mkdir` | *Make a directory* : crée un répertoire ([[Commande mkdir]]) |
| `echo` | Affiche du texte, « comme un print » ([[Commande echo]]) |
| `sudo su` | Donne les droits d'administrateur sans devoir retaper `sudo` aux commandes suivantes ([[Commande su]], [[Super-utilisateur root]]) |
| `touch file1.txt` | Crée un fichier vide ; si le fichier existe, met à jour son horodatage ([[Commande touch]]) |
| `read variable` | Demande une saisie à l'utilisateur et la stocke dans `variable` ([[Commande read]]) |
| `grep [OPTIONS] PATTERN [FICHIER...]` | Cherche un motif dans un fichier ou dans une sortie du terminal ([[Commande grep]]) |
| `wc [OPTION]... [FILE]...` | Affiche le nombre de lignes, de mots et d'octets de chaque fichier ([[Commande wc]]) |
| `shuf [OPTIONS]` | Génère des nombres aléatoires ([[Commande shuf]]) — options ci-dessous |
| `sort [OPTION]... [FILE]...` | Trie les lignes d'un fichier ou d'une sortie ; `-g` compare selon la valeur numérique générale ([[Commande sort]]) |
| `uniq` | Omet les lignes répétées ([[Commande uniq]]) |
| `jobs [option]` | Voir les [[Processus\|processus]] en cours ([[Commande jobs]]) |
| `ping 192.168.1.1` / `ping example.com` | Tester la connectivité entre deux hôtes d'un réseau IP, par une [[Adressage IPv4 et CIDR\|adresse IP]] ou un [[Nom d'hôte]] : envoie des paquets à l'hôte cible et attend une réponse ; vérifie qu'un appareil est accessible et mesure le délai de transmission ([[Commande ping]]) |
| `free -h` | Affiche la [[Mémoire vive\|RAM]] utilisée et restante ; `-h` = sortie lisible (*human readable*) ([[Commande free]]) |
| `df -h` | Affiche le stockage utilisé et restant, `-h` lisible ([[Commande df]]) |
| `lscpu` | Liste les informations du processeur ([[Commande lscpu]]) |
| `lshw` | Liste les informations matérielles ([[Commande lshw]]) |

### Options de `shuf`

- `-i` : *input-range*, l'intervalle des valeurs ;
- `-n` : *head-count*, le nombre de valeurs en sortie (la fiche dit « nb de character à la sortie ») ;
- `-r` : répétition autorisée (une même valeur peut sortir plusieurs fois).

```bash
shuf -i 1-10 -n 10 -r > number.txt   # 10 nombres entre 1 et 10, répétitions permises
cat number.txt
```

![[Commandes Shell + explications - image1.png]]
*Figure : `man shuf`, puis `shuf -i 1-10 -n 10 -r > number.txt` et `cat number.txt` qui affiche 3, 6, 5, 9, 10, 4, 4, 9, 3, 2.*

## Utilisation de `cat`

Voir [[Commande cat]].

| Commande | Rôle |
|---|---|
| `cat filename.txt` | Afficher le contenu du fichier dans le terminal |
| `cat -n filename.txt` | Afficher avec les numéros de ligne, pratique pour du code |
| `cat file1.txt file2.txt` | Afficher plusieurs fichiers à la suite |
| `cat > filename.ext` | Créer un nouveau fichier (saisie au clavier) |
| `cat file1.txt file2.txt > fileConcatenate.txt` | Fusionner deux fichiers ([[Redirection et tube\|redirection]]) |

## Utilisation de `chmod`

Voir [[Commande chmod]] et [[Permissions Unix]].

| Commande | Rôle |
|---|---|
| `sudo chmod 777 file.txt` | Change les permissions du fichier (ici tout pour tous) |
| `sudo chmod +x file.txt` | Ajoute l'exécution pour le propriétaire, le groupe et les autres |
| `sudo chmod +w file.txt` | Ajoute l'écriture pour le propriétaire seulement, d'après l'observation de l'étudiante (« peut-être que c'est mon [[Distribution Linux\|Debian]] ») |
| `sudo chmod +r file.txt` | Ajoute la lecture pour le propriétaire, le groupe et les autres |
| `sudo chmod +rwx file.txt` | Ajoute lecture, écriture et exécution pour le propriétaire, le groupe et les autres |

## Comprendre le langage Bash

Voir [[Script Bash]] et [[Variable Bash]].

### Substitution de commande et variables

```bash
#!/bin/bash
current_datetime=$(date)
echo "Current Date and Time: $current_datetime"
```

- `$(...)` : [[Substitution de commande]]. Le contenu des parenthèses est exécuté comme une commande, et son résultat est stocké dans la variable.
- `$` devant un nom de variable donne accès à sa valeur : `$current_datetime` est remplacé par la date et l'heure stockées.

```bash
#!/bin/bash
Name="Morgane"
echo $Name
```

La variable contient la valeur ; pour l'utiliser dans le script, on la précède de `$`.

### Saisie avec `read`

```bash
read -p "entrez un nom: " username_val        # -p affiche un prompt
read -s -p "entrez un mdp: " password_val     # -s masque la saisie (mots de passe)
echo "enter names: "
read -a names        # -a lit l'entrée comme un tableau (éléments séparés par des espaces)
echo "names: ${name[0]}, ${name[1]}"          # sic : voir Erreurs du cours
```

Un [[Tableau (programmation)|tableau]] (*array*) stocke plusieurs éléments sous un seul nom, chacun accessible par son indice.

### Conditions

```bash
#!/bin/bash
read -p "enter a number :" number
if [ $number -gt 10 ]
then
  echo "The number is greater than 10."
fi
```

**Attention** : ne pas oublier les espaces autour de `[` et `]` (correct : `[ $a -eq 10 ]`). Ne pas confondre chaînes et nombres : pour les chaînes, `=` ou `!=` ; `-eq`, `-ne` sont pour les nombres.

Structure de la [[Structure conditionnelle]] (la fiche dit « boucles conditionnelles ») :

```bash
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

### Boucles

Voir [[Boucle (programmation)]].

```bash
while [ condition ]
do
  command 1
  command 2
done

for (( initialization; test condition; loop counter ))
do
  command 1
  command 2
done
```

### ET et OU logiques

Voir [[Opérateur logique]]. Trois écritures équivalentes pour chacun :

```bash
if [ condition ] && [ condition ]      # logical AND
if [ condition -a condition ]          # logical AND
if [[ condition && condition ]]        # logical AND

if [ condition ] || [ condition ]      # logical OR
if [ condition -o condition ]          # logical OR
if [[ condition || condition ]]        # logical OR
```

(chaque `if` suivi de `then … fi`). Pour le ET : `&&` ou `-a` ; pour le OU : `||` ou `-o`.

### Règles à retenir

- `#` sert à écrire un [[Commentaire en Bash|commentaire]].
- `Name = "Morgane"` ne fonctionne pas : **pas d'espace** avant ni après `=`.
- `$test` récupère la valeur d'une variable ; `$(test)` exécute une commande et récupère son résultat.
- `if [ condition ]` sert aux comparaisons de chaînes, de fichiers et aux conditions simples ; `if (( condition ))` aux expressions arithmétiques ([[Arithmétique en Bash]]).
- Deux types de variables : **variables système** (majuscules : `$BASH`, `$HOME`…) et **variables définies par l'utilisateur** (minuscules).

### Comparaison d'entiers

Voir [[Opérateur de comparaison]].

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

### Comparaison de chaînes

| Opérateur | Sens | Exemple |
|---|---|---|
| `=` | égal à | `if [ "$a" = "$b" ]` |
| `==` | égal à | `if [ "$a" == "$b" ]` |
| `!=` | différent de | `if [ "$a" != "$b" ]` |
| `<` | inférieur, dans l'ordre alphabétique [[Code ASCII\|ASCII]] | `if [[ "$a" < "$b" ]]` |
| `>` | supérieur, dans l'ordre ASCII | `if [[ "$a" > "$b" ]]` |
| `-z` | chaîne nulle, de longueur zéro | `if [ -z "$string" ]` |

(Les exemples sont réécrits avec des guillemets droits et un tiret simple ; la fiche utilise des guillemets typographiques et un tiret long `–eq`.)

## Erreurs du cours

- [[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]] écrit que `sh testfile.sh` exécute le programme « en utilisant l'interpréteur bash » ; il faut « avec l'interpréteur `sh` » : sous Debian et Ubuntu, `sh` pointe en général vers `dash`, pas Bash (voir [[Shell dash]]).
- L'exemple des tableaux écrit `read -a names` puis `echo "names: ${name[0]}, ${name[1]}"` ; il faut `${names[0]}, ${names[1]}` : `name` n'existe pas et l'affichage serait vide.
- Les exemples sont écrits avec des guillemets typographiques (`“ ”`), un tiret long (`–eq`, `–ne`…) et `[ [ … ] ]` ou `[[ … ] ]` avec des espaces ; il faut des guillemets droits, `-eq` et `[[ … ]]`, sinon le script ne fonctionne pas (réécrits ainsi dans les tableaux de cette fiche).
