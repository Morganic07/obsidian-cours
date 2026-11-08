---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
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
| `sh testfile.sh` | Exécuter un programme avec l'interpréteur `sh` (souvent [[Shell dash\|dash]] sous Debian et Ubuntu), quel que soit le [[Shebang\|shebang]] [[Erreurs du cours#^e-8-os-commandes-sh\|✎]] |
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

Pour toute commande, `man commande` affiche son manuel complet, et `commande --help` un résumé de ses options ([[Commande man]]). [[Complément hors du cours|ⓘ]]

Précisions sur quelques lignes du tableau : [[Complément hors du cours|ⓘ]]
- `rm` ne passe pas par une corbeille : le fichier est perdu. `rm -r dossier` supprime un répertoire **non vide** avec tout son contenu, `rm -i` demande confirmation pour chaque fichier ; `rm -rf` sans vérifier le chemin est l'erreur classique à éviter, surtout avec `sudo`. [[Complément hors du cours|ⓘ]]
- `sudo` exécute **une** commande avec les droits de [[Super-utilisateur root|root]], après le mot de passe de l'utilisateur, si celui-ci y est autorisé ([[Fichier sudoers]]) ; chaque usage est journalisé. `sudo su` (ou `sudo -i`) ouvre un shell root où tout est permis sans garde-fou : à réserver aux longues tâches d'administration. Inutile de mettre `sudo` pour éditer ou modifier ses propres fichiers : `sudo nano testfile.sh` crée le fichier au nom de root, et l'utilisateur ne pourra plus le modifier sans `sudo`. [[Complément hors du cours|ⓘ]]
- Avec [[APT]] : `sudo apt install paquet` installe, `sudo apt remove paquet` désinstalle, `apt search mot` cherche un paquet dans les dépôts. [[Complément hors du cours|ⓘ]]
- Options courantes de `grep` : `-i` ignore la casse, `-n` affiche les numéros de ligne, `-v` inverse (lignes qui **ne** contiennent **pas** le motif), `-c` compte les lignes trouvées, `-r` cherche dans tout un répertoire. Exemple : `grep -in "erreur" journal.log`. [[Complément hors du cours|ⓘ]]
- `wc -l` ne compte que les lignes, `wc -w` les mots, `wc -c` les octets ; `ls | wc -l` compte les fichiers d'un répertoire. [[Complément hors du cours|ⓘ]]
- `uniq` ne supprime que les doublons **consécutifs** : il faut trier d'abord. `sort fichier | uniq` élimine tous les doublons, `sort fichier | uniq -c` compte les occurrences de chaque ligne, et `sort -u` fait le tri et l'élimination d'un coup. [[Complément hors du cours|ⓘ]]
- `jobs` ne montre que les tâches lancées depuis **le shell courant** (en arrière-plan avec `&` ou suspendues par Ctrl+Z), pas tous les processus du système : pour ceux-là, `ps aux` ou `top` ([[Commande ps]]). [[Complément hors du cours|ⓘ]]
- `ping` envoie des messages [[ICMP]] *echo request* et attend les *echo reply* ; il affiche pour chacun le temps aller-retour en millisecondes. Sous Linux, il continue jusqu'à Ctrl+C ; `ping -c 4 example.com` s'arrête après quatre envois. Une absence de réponse ne prouve pas que l'hôte est éteint : beaucoup de pare-feu bloquent l'ICMP. [[Complément hors du cours|ⓘ]]

### Options de `shuf`

- `-i` : *input-range*, l'intervalle des valeurs ;
- `-n` : *head-count*, le nombre de lignes en sortie ; [[Erreurs du cours#^e-8-os-commandes-sh|✎]]
- `-r` : répétition autorisée (une même valeur peut sortir plusieurs fois).

Sans `-r`, chaque valeur ne sort qu'une fois : `shuf -i 1-10` donne une permutation aléatoire de 1 à 10, et un `-n` plus grand que l'intervalle n'en donne pas davantage (10 valeurs au plus ici). Le premier usage de `shuf` est d'ailleurs de mélanger les lignes d'un fichier : `shuf liste.txt` les affiche dans un ordre aléatoire, `shuf -n 1 liste.txt` en tire une au hasard. [[Complément hors du cours|ⓘ]]

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

Avec `cat > filename.ext`, la saisie se termine par **Ctrl+D** (fin de fichier) en début de ligne. `>` écrase le fichier s'il existe déjà, `>>` ajoute à la fin sans effacer : `cat file2.txt >> file1.txt` complète `file1.txt`. Le nom `cat` vient de *concatenate*. Pour un long fichier, `less fichier` permet de défiler page par page, et `head` / `tail` n'affichent que le début ou la fin (10 lignes par défaut). [[Complément hors du cours|ⓘ]]

## Utilisation de `chmod`

Voir [[Commande chmod]] et [[Permissions Unix]].

| Commande | Rôle |
|---|---|
| `sudo chmod 777 file.txt` | Change les permissions du fichier (ici tout pour tous) |
| `sudo chmod +x file.txt` | Ajoute l'exécution pour le propriétaire, le groupe et les autres |
| `sudo chmod +w file.txt` | Ajoute l'écriture pour le propriétaire seulement, d'après l'observation de l'étudiante (« peut-être que c'est mon [[Distribution Linux\|Debian]] ») |
| `sudo chmod +r file.txt` | Ajoute la lecture pour le propriétaire, le groupe et les autres |
| `sudo chmod +rwx file.txt` | Ajoute lecture, écriture et exécution pour le propriétaire, le groupe et les autres |

**Pourquoi `+w` ne touche que le propriétaire.** Écrit sans préciser à qui (`+x`, `+w`), `chmod` applique le changement à tous **sauf** aux droits bloqués par le **masque** de l'utilisateur, l'`umask` ([[Masque umask]]). Le masque courant est `022`, qui retire l'écriture au groupe et aux autres, et une commande lancée par `sudo` a par défaut un masque au moins aussi strict : `+r` et `+x` passent pour tous, `+w` seulement pour le propriétaire. L'observation de l'étudiante est donc le comportement normal, pas une particularité de sa Debian. La commande `umask` affiche le masque en cours. [[Complément hors du cours|ⓘ]]

Pour viser une catégorie précise, on la nomme : `u` (propriétaire, *user*), `g` (groupe), `o` (autres, *others*), `a` (tous). `chmod u+x script.sh` rend un script exécutable pour soi seul, `chmod go-w fichier` retire l'écriture au groupe et aux autres, `chmod a+w fichier` donne l'écriture à tous, masque compris. En octal, chaque chiffre additionne r = 4, w = 2, x = 1 : `755` (rwxr-xr-x) convient à un script ou un répertoire, `644` (rw-r--r--) à un fichier ordinaire, et `777` donne tout à tout le monde, ce qu'on évite pour des raisons de sécurité ([[Permissions Unix]]). Le `sudo` n'est nécessaire que si l'on n'est pas propriétaire du fichier. [[Complément hors du cours|ⓘ]]

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

On entoure presque toujours la variable de guillemets doubles, `echo "$Name"` : sans eux, une valeur contenant des espaces est coupée en plusieurs mots, et une variable vide disparaît de la commande (ce qui casse un test comme `[ $a = "x" ]`). Les guillemets doubles laissent remplacer `$Name` par sa valeur, les apostrophes l'empêchent : `echo '$Name'` affiche littéralement `$Name` ([[Guillemets en shell]]). La forme `${Name}` délimite le nom quand du texte suit : `"${Name}_bis"`. [[Complément hors du cours|ⓘ]]

**Arguments d'un script.** Un script lancé par `./script.sh a b c` reçoit ses arguments dans `$1`, `$2`, `$3` ; `$0` est le nom du script, `$#` le nombre d'arguments, `"$@"` la liste de tous. [[Complément hors du cours|ⓘ]]

Une variable n'est visible que dans le shell qui la crée ; `export NOM=valeur` la transmet aussi aux programmes lancés depuis ce shell (variable d'environnement). C'est le cas de `PATH`, la liste des répertoires où le shell cherche les commandes : c'est pourquoi on tape `ls` et non `/bin/ls`, et pourquoi un script du répertoire courant se lance par `./script.sh`, le répertoire courant n'étant pas dans `PATH` ([[Commande which]]). [[Complément hors du cours|ⓘ]]

### Saisie avec `read`

Exemples de saisie : [[Erreurs du cours#^e-8-os-commandes-sh|✎]]

```bash
read -p "entrez un nom: " username_val        # -p affiche un prompt
read -s -p "entrez un mdp: " password_val     # -s masque la saisie (mots de passe)
echo "enter names: "
read -a names        # -a lit l'entrée comme un tableau (éléments séparés par des espaces)
echo "names: ${names[0]}, ${names[1]}"
```

Un [[Tableau (programmation)|tableau]] (*array*) stocke plusieurs éléments sous un seul nom, chacun accessible par son indice.

En Bash, les indices partent de 0. `"${names[@]}"` donne tous les éléments, `${#names[@]}` leur nombre ; un tableau se crée aussi directement : `names=(Alice Bob Chloé)`. Pour le parcourir : `for n in "${names[@]}"; do echo "$n"; done`. Les accolades sont obligatoires : `$names[0]` afficherait le premier élément suivi du texte `[0]`. [[Complément hors du cours|ⓘ]]

### Conditions

Exemple de condition : [[Erreurs du cours#^e-8-os-commandes-sh|✎]]

```bash
#!/bin/bash
read -p "enter a number :" number
if [ $number -gt 10 ]
then
  echo "The number is greater than 10."
fi
```

**Attention** : ne pas oublier les espaces autour de `[` et `]` (correct : `[ $a -eq 10 ]`). Ne pas confondre chaînes et nombres : pour les chaînes, `=` ou `!=` ; `-eq`, `-ne` sont pour les nombres.

**Pourquoi ces espaces.** `[` n'est pas de la ponctuation mais une **commande** (un autre nom de la commande `test`), dont `]` est le dernier argument. `[ $a -eq 10 ]` appelle `[` avec les arguments `$a`, `-eq`, `10` et `]` ; sans espace, `[$a` devient un seul mot que le shell cherche comme nom de commande, d'où l'erreur « command not found ». [[Complément hors du cours|ⓘ]]

Plus généralement, `if` ne teste pas une expression mais le [[Code de retour]] d'une commande : 0 (succès) vaut « vrai », toute autre valeur « faux ». On peut donc écrire `if grep -q "root" /etc/passwd; then … fi`. Après chaque commande, `$?` contient son code de retour, et un script renvoie le sien avec `exit 0` (succès) ou `exit 1` (erreur). [[Complément hors du cours|ⓘ]]

`[[ … ]]` est propre à Bash (le `[` simple vient du shell POSIX et marche aussi sous `sh`) : on n'y a pas besoin de guillemets autour des variables, on peut y écrire `&&`, `||`, `<`, `>`, et `==` y accepte un motif (`[[ $f == *.txt ]]`). Dans un script lancé par `sh`, il faut s'en tenir à `[ … ]`. [[Complément hors du cours|ⓘ]]

**Tests sur les fichiers**, évoqués dans les règles plus bas sans être détaillés : [[Complément hors du cours|ⓘ]]

| Test | Vrai si |
|---|---|
| `[ -e chemin ]` | le chemin existe |
| `[ -f chemin ]` | c'est un fichier ordinaire |
| `[ -d chemin ]` | c'est un répertoire |
| `[ -r chemin ]`, `[ -w chemin ]`, `[ -x chemin ]` | l'utilisateur peut le lire, y écrire, l'exécuter |
| `[ -s chemin ]` | le fichier existe et n'est pas vide |

Exemple : `if [ ! -d sauvegarde ]; then mkdir sauvegarde; fi` crée le répertoire s'il n'existe pas ; `!` inverse le test. [[Complément hors du cours|ⓘ]]

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

Exemples concrets des deux formes, qui affichent chacune les nombres de 1 à 5 : [[Complément hors du cours|ⓘ]]

```bash
i=1
while [ $i -le 5 ]
do
  echo $i
  i=$(( i + 1 ))
done

for (( i=1; i<=5; i++ ))
do
  echo $i
done
```

Bash a une troisième forme, la plus courante, qui parcourt une liste de mots : `for f in *.txt; do echo "$f"; done` traite chaque fichier `.txt` du répertoire, et `for i in {1..5}` parcourt 1 à 5. `until [ condition ]` répète tant que la condition est **fausse** ; `break` sort de la boucle et `continue` passe au tour suivant. Avec `while`, il faut faire évoluer la variable dans le corps, sinon la boucle ne s'arrête pas. [[Complément hors du cours|ⓘ]]

**Fonctions.** Bash permet de regrouper des commandes sous un nom, appelé ensuite comme une commande : les arguments arrivent dans `$1`, `$2`…, comme pour un script, et `local` limite une variable à la fonction. [[Complément hors du cours|ⓘ]]

```bash
saluer() {
  local nom="$1"
  echo "Bonjour $nom"
}
saluer Alice      # affiche : Bonjour Alice
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

Les trois écritures ne sont pas tout à fait égales : `-a` et `-o` sont déclarés obsolètes par la norme POSIX, car ambigus dans certains cas ; on préfère `[ … ] && [ … ]` ou `[[ … && … ]]`. Hors d'un `if`, `&&` et `||` enchaînent aussi des commandes selon leur réussite : `mkdir rep && cd rep` n'entre dans `rep` que si sa création a réussi, `cd rep || exit 1` arrête le script si `cd` échoue. [[Complément hors du cours|ⓘ]]

### Règles à retenir

- `#` sert à écrire un [[Commentaire en Bash|commentaire]].
- `Name = "Morgane"` ne fonctionne pas : **pas d'espace** avant ni après `=` ; on écrit `Name="Morgane"`. [[Erreurs du cours#^e-8-os-commandes-sh|✎]]
- `$test` récupère la valeur d'une variable ; `$(test)` exécute une commande et récupère son résultat.
- `if [ condition ]` sert aux comparaisons de chaînes, de fichiers et aux conditions simples ; `if (( condition ))` aux expressions arithmétiques ([[Arithmétique en Bash]]).
- Deux types de variables : **variables système** (majuscules : `$BASH`, `$HOME`…) et **variables définies par l'utilisateur** (minuscules).

### Comparaison d'entiers

Voir [[Opérateur de comparaison]]. [[Erreurs du cours#^e-8-os-commandes-sh|✎]]

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

Dans `(( … ))`, le `$` et les guillemets sont facultatifs : `if (( a >= b ))` suffit, car tout nom y est lu comme une variable numérique. On y écrit aussi `==` et `!=` pour l'égalité et la différence. À l'inverse, `<` et `>` ne comparent pas des nombres dans `[ … ]` : le shell y voit des redirections, `[ $a > $b ]` crée un fichier nommé d'après `$b` ([[Redirection et tube]]). [[Complément hors du cours|ⓘ]]

### Comparaison de chaînes

| Opérateur | Sens | Exemple |
|---|---|---|
| `=` | égal à | `if [ "$a" = "$b" ]` |
| `==` | égal à | `if [ "$a" == "$b" ]` |
| `!=` | différent de | `if [ "$a" != "$b" ]` |
| `<` | inférieur, dans l'ordre alphabétique [[Code ASCII\|ASCII]] | `if [[ "$a" < "$b" ]]` [[Erreurs du cours#^e-8-os-commandes-sh\|✎]] |
| `>` | supérieur, dans l'ordre ASCII | `if [[ "$a" > "$b" ]]` [[Erreurs du cours#^e-8-os-commandes-sh\|✎]] |
| `-z` | chaîne nulle, de longueur zéro | `if [ -z "$string" ]` |

Son contraire est `-n` : `[ -n "$string" ]` est vrai si la chaîne n'est pas vide, par exemple pour vérifier qu'un utilisateur a bien saisi quelque chose après un `read`. Les guillemets autour de `"$string"` sont indispensables ici : sans eux, une variable vide disparaît et `[ -n ]` est toujours vrai. [[Complément hors du cours|ⓘ]]