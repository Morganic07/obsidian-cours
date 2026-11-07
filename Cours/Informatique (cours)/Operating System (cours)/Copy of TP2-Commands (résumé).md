---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF Copy of TP2-Commands ([[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]) (6 pages, 18 novembre 2024, cours « UNIX Commands », partie « File Management »), dans [[Operating System (index)]]. Sujet de TP, en anglais, sans figure. Le rendu correspondant est [[TP2 (résumé)]] ; les notes de cours, [[Séance TP2 (résumé)]]. Pour chaque tâche, le sujet demande une capture du terminal avant et après la commande. Aucun corrigé dans le document.

## 1. Méta-caractères (*Meta characters*)

Les méta-caractères ([[Méta-caractère]]) sont des symboles spéciaux qui ont un sens particulier dans les utilitaires en ligne de commande et les langages de programmation : ils contrôlent l'interprétation des commandes au lieu de représenter des valeurs littérales. Ce sont des outils essentiels sous Ubuntu pour gérer fichiers, répertoires et opérateurs de la ligne de commande ([[Shell et Bash]]).

| Rôle | Caractères |
|---|---|
| a) *Pattern matching* ou *wildcards* | `*`, `?`, `[]` |
| b) *Redirection* | `>`, `>>`, `<`, `\|` |
| c) *Background and Job Control* | `&`, `;` |
| d) *Grouping and Quoting* | `( )`, `{ }`, `' '`, `" "` |
| e) *Path Navigation* | `/`, `~`, `.`, `..` |
| f) *Escaping* | `\` |

## 1.1 Jokers (*Pattern matching or Wildcards*)

Voir [[Joker (wildcard)]] et [[Expansion d'accolades]].

```bash
ls *.txt                # * : zéro caractère ou plus → tous les .txt
ls file?.txt            # ? : exactement un caractère → file1.txt, file4.txt
ls file[123].txt        # [ ] : un caractère parmi ceux entre crochets → file1.txt, file2.txt, file3.txt
touch file{1,2,3}.txt   # { } : génère plusieurs options → crée file1.txt, file2.txt, file3.txt
```

**Tâche 1.1**
- a. Créer un répertoire `wildcard_lab` dans `/home/user`.
- b. Y créer 20 fichiers texte `file1.txt` … `file20.txt` avec le caractère d'expansion.
- c. Y créer 15 fichiers `file1.conf` … `file15.conf`.
- d. Lister tous les fichiers `.txt`.
- e. Lister tous les fichiers `.conf`.
- f. Lister les fichiers 9 à 15, quelle que soit l'extension.
- g. Renommer le répertoire `wildcard_lab_` en `wildcard_lab2` avec le caractère `?` ; le renommage manuel est interdit.

## 1.2 Redirection

Rediriger la sortie ou l'entrée d'une commande vers ou depuis des fichiers ou d'autres commandes ([[Redirection et tube]]).

```bash
echo "Hello" > file.txt    # > : écrit "Hello" dans file.txt, en l'écrasant (le crée au besoin)
echo "World" >> file.txt   # >> : ajoute "World" à la fin
wc -l < file.txt           # < : entrée lue dans un fichier ; compte les lignes
ls | grep "file"           # | : tube ; liste les fichiers et filtre ceux qui contiennent "file"
```

**Tâche 1.2**
- a. Créer `lab_output.txt` avec `>` seulement et y écrire « Welcome to the Linux lab! », dans `wildcard_lab`.
- b. Afficher son contenu pour vérifier.
- c. Ajouter « This is the second line. ».
- d. Afficher le contenu pour vérifier l'ajout.
- e. Que fait `wc` ? Quelles sont ses options ? Comment sa sortie est-elle organisée ? ([[Commande wc]])
- f. Compter les lignes de `lab-output.txt` avec `wc –l` et l'opérateur de redirection d'entrée.
- g. Lister les fichiers du répertoire courant et ne garder que les `.conf`, avec un tube ([[Commande grep]]).
- h. Compter les fichiers `.txt` du répertoire en combinant `ls`, `grep` et `wc –l` par des tubes.
- i. Créer `number.txt` avec 10 nombres aléatoires, dont des doublons ; afficher avec `cat`, `sort` et `uniq` en tubes la liste triée des nombres uniques ([[Commande sort]], [[Commande uniq]]).
- j. Lister avec `ls` les fichiers de `wildcard_lab` et enregistrer la sortie dans `directory_list.txt`.
- k. Ajouter la date et l'heure à `directory_list.txt` ([[Commande date]]).

## 1.3 Tâches de fond (*Background and Job Control*)

Gérer l'ordre d'exécution ou lancer des tâches en arrière-plan ([[Tâche en arrière-plan]]).

- `&` : lance une commande en arrière-plan. Exemple : ouvrir `file1.txt`, y écrire « Hello » sur 5 lignes, puis :

```bash
cp file1.txt ./backup.txt &   # copie en arrière-plan
ls                            # on voit apparaître backup.txt
cat backup.txt
```

- `;` : sépare plusieurs commandes exécutées l'une après l'autre :

```bash
mkdir new_folder; cd new_folder; touch newfile.txt
```

**Tâche 1.3**
- a. Créer avec `sleep` une tâche de fond de 90 secondes ([[Commande sleep]]).
- b. Lister les tâches de fond avec `jobs` et vérifier si le `sleep` tourne encore ([[Commande jobs]]).
- c. Lancer en même temps en arrière-plan deux `sleep`, de 60 et de 90 secondes.
- d. Ramener au premier plan le `sleep` de 90 secondes avec `fg` ([[Commandes fg et bg]]).
- e. Créer un répertoire `job_control` et s'y placer en exécutant les deux commandes sur la même ligne avec `;`.

## 1.4 Regroupement et guillemets (*Grouping and Quoting*)

Voir [[Groupement de commandes]], [[Sous-shell]] et [[Guillemets en shell]].

```bash
(cd folder && ls)    # ( ) : sous-shell ; va dans folder, liste, puis revient
{ mkdir new_folder; cd new_folder; touch newfile.txt; }   # { } : groupe dans le shell courant
```

- `' '` (apostrophes) : préserve la valeur littérale de chaque caractère.
- `" "` (guillemets) : préserve la plupart des caractères mais autorise l'expansion des variables.

Exemples du sujet, commentaires recopiés tels quels (voir point à vérifier 2) :

```bash
echo 'path $PWD'     # Outputs "Hello $PWD" (without expanding $PWD)
echo $PWD            # Outputs the path to the working directory. Note the output difference in the two commands.
echo 'Hello $USER'   # Outputs "Hello $USER" (without expanding $USER)
echo $USER           # outputs "Hello <username>"
echo "Hello $USER"   # Outputs "Hello <username>"
echo "Path $PWD"     # Outputs "Path </path to the working directory>
```

**Tâche 1.4**
- a. Aller dans `/home/user` ; lancer deux commandes dans un sous-shell `( )` pour changer de répertoire puis lister les fichiers ; vérifier qu'on revient au répertoire d'origine.
- b. Grouper deux commandes avec `{ }` pour afficher un message puis lister les fichiers du répertoire courant.
- c. Afficher avec `" "` une chaîne qui contient les valeurs de `$USER` et `$HOME`, développées ([[Variable Bash]]).

## 1.5 Caractères des chemins (*Special Characters for File Paths and Locations*)

Voir [[Chemin de fichier]] et [[Répertoire personnel]].

```bash
cd /home/user    # / : sépare les répertoires d'un chemin
cd ~             # ~ : répertoire personnel de l'utilisateur courant
./script.sh      # . : répertoire courant ; exécute script.sh qui s'y trouve
cd ..            # .. : répertoire parent ; remonte d'un niveau
```

**Tâche 1.5**
- a. Créer `My File With Spaces.txt` avec `touch`, en échappant les espaces par `\`.
- b. Vérifier la création en listant le répertoire.
- c. Essayer de créer un fichier avec un astérisque dans le nom, comme `File*Test.txt`, et observer.
- d. Créer `Price$100.txt` avec `\`.

## 1.6 Caractères d'échappement (*Special Escaping Characters*)

Voir [[Caractère d'échappement]] et [[Substitution de commande]].

```bash
rm file\ name.txt    # \ : échappe le caractère suivant → supprime "file name.txt"
rm file\ file2.txt   # commentaire du sujet : supprime "file2.txt" (voir point à vérifier 3)
echo `pwd`           # `` : exécute la commande et substitue sa sortie → affiche le répertoire courant
```

**Tâche 1.6**
- a. Avec des apostrophes inversées, capturer la date et l'heure (`date`) dans une variable `CURRENT_DATE`.
- b. Afficher `CURRENT_DATE` avec `echo`.
- c. Avec des apostrophes inversées, stocker la durée de fonctionnement du système (`uptime`, [[Commande uptime]]) dans `UPTIME`.
- d. Afficher `UPTIME`.
- e. Imbriquer des commandes : compter les fichiers du répertoire avec `ls | wc -l` entre apostrophes inversées, stocker le résultat dans une variable et l'afficher dans un message.

## Notions mobilisées

[[Shell et Bash]], [[Redirection et tube]], [[Permissions Unix]] (chemins et fichiers), et la gestion des tâches en arrière-plan ([[Processus]]).

## Points à vérifier

1. L'en-tête du sujet de TP2 porte « TP1 » (complément : coquille d'en-tête).
2. Exemple d'apostrophes : `echo 'path $PWD'` est commenté « Outputs "Hello $PWD" » ; la sortie réelle est `path $PWD`. De même, `echo $USER` est commenté « outputs "Hello <username>" » alors qu'il n'affiche que le nom.
3. Exemple d'échappement : `rm file\ file2.txt` est commenté « deletes a file named file2.txt » ; la commande supprime un fichier nommé `file file2.txt`.
4. **Tâche 1.1 g** : elle parle de renommer `wildcard_lab_` alors que le dossier créé en a s'appelle `wildcard_lab` ; la tâche 1.2 f parle de `lab-output.txt` (tiret) au lieu de `lab_output.txt`. Coquilles probables du sujet.
5. **Tirets longs** : le sujet écrit `wc –l` et `Cp` (majuscule) ; à taper `wc -l` et `cp` (complément).
