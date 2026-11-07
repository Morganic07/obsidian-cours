---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Cours TP2.docx|Cours TP2]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/Cours TP2.docx|Cours TP2]], dans [[Operating System (matière)]]. Séance de TP sur les caractères spéciaux du shell : extraits du support (captures de texte, recopiées ici) et essais de l'étudiante dans le terminal (captures intégrées). Voir [[Redirection et tube]] et [[Méta-caractère]].

## Les six familles de caractères spéciaux

| Famille | Caractères |
|---|---|
| a) *Pattern matching* ou *wildcards* ([[Joker (wildcard)]]) | `*`, `?`, `[]` |
| b) *Redirection* ([[Redirection et tube]]) | `>`, `>>`, `<`, `\|` |
| c) *Background and Job Control* ([[Tâche en arrière-plan]]) | `&`, `;` |
| d) *Grouping and Quoting* ([[Groupement de commandes]]) | `( )`, `{ }`, `' '`, `" "` |
| e) *Path Navigation* | `/`, `~`, `.`, `..` |
| f) *Escaping* ([[Caractère d'échappement]]) | `\` |

## 1.1 Jokers (*Pattern matching or Wildcards*)

Servent à désigner des noms de fichiers ou des motifs de texte.

```bash
ls *.txt                # * : zéro caractère ou plus → tous les fichiers .txt
ls file?.txt            # ? : exactement un caractère → file1.txt, file4.txt…
ls file[123].txt        # [] : un caractère parmi ceux entre crochets → file1.txt, file2.txt, file3.txt
touch file{1,2,3}.txt   # {} : génère plusieurs options → crée file1.txt, file2.txt, file3.txt
```

Les accolades relèvent de l'[[Expansion d'accolades]].

## 1.2 Redirection

Redirige la sortie ou l'entrée d'une commande vers ou depuis un fichier ou une autre commande.

```bash
echo "Hello" > file.txt    # > : écrit dans le fichier, le crée ou l'écrase
echo "World" >> file.txt   # >> : ajoute à la fin du fichier
wc -l < file.txt           # < : prend l'entrée dans un fichier (compte les lignes)
ls | grep "file"           # | : tube, la sortie d'une commande devient l'entrée de la suivante
```

`wc -l` ([[Commande wc]]) compte seulement les lignes (la note dit « write count », voir point à vérifier 1).

### Essais de l'étudiante

![[Séance TP2 - image3.png]]
*Figure : `wc -l lab_output.txt` → `2 lab_output.txt` : le fichier n'a que 2 lignes.*

Lister seulement les fichiers `.conf` du répertoire avec [[Commande grep|grep]] :

![[Séance TP2 - image8.png]]
*Figure : `ls | grep "\.conf"` liste file1.conf à file15.conf.*

Compter les fichiers `.txt` : `ls | grep "\.txt"` les liste, et `wc -l` compte les lignes de cette sortie.

![[Séance TP2 - image14.png]]
*Figure : `ls | grep "\.txt" | wc -l` → 21.*

Créer un fichier de nombres aléatoires avec [[Commande shuf|shuf]] :

![[Séance TP2 - image1.png]]
*Figure : `shuf -i 1-10 -n 10 -r > number.txt` puis `cat number.txt` : 3, 6, 5, 9, 10, 4, 4, 9, 3, 2.*

Trier la sortie du fichier, sans modifier le fichier lui-même ([[Commande sort]], [[Commande uniq]]) :

![[Séance TP2 - image2.png]]
*Figure : `cat number.txt | sort -g | uniq` → 2, 3, 4, 5, 6, 9, 10 (tri numérique, doublons retirés).*

Ajouter la date courante à la fin d'un fichier ([[Commande date]]) :

![[Séance TP2 - image18.png]]
*Figure : `date >> directory_list.txt ; cat directory_list.txt` : la liste des fichiers du répertoire, puis la date « Mon Nov 18 10:33:48 AM CET 2024 » ajoutée en dernière ligne.*

## 1.3 Tâches de fond (*Background and Job Control*)

Gérer l'ordre d'exécution ou lancer des tâches en arrière-plan.

- `&` : lance une commande en arrière-plan ;
- `;` : sépare plusieurs commandes exécutées l'une après l'autre.

Commandes de contrôle des tâches ([[Commande jobs]], [[Commandes fg et bg]]) :

| Commande | Rôle |
|---|---|
| `jobs` | voir les tâches en cours |
| `fg %1` | mettre la tâche [1] au premier plan |
| `bg %1` | mettre la tâche [1] en arrière-plan (comme `&`) |

## 1.4 Regroupement et guillemets (*Grouping and Quoting*)

Regrouper des commandes ou préserver la valeur littérale d'un texte.

```bash
(cd folder && ls)    # ( ) : groupe dans un sous-shell ; va dans folder, liste, puis revient
{ mkdir new_folder; cd new_folder; touch newfile.txt; }   # { } : groupe dans le shell courant
```

Voir [[Sous-shell]] et [[Guillemets en shell]].

- `' '` (apostrophes, *single quotes*) : préserve la valeur littérale de chaque caractère.
- `" "` (guillemets, *double quotes*) : préserve la plupart des caractères mais permet l'expansion des variables.

Exemples du support (commentaires recopiés tels quels, voir point à vérifier 2) :

```bash
echo 'path $PWD'      # Outputs "Hello $PWD" (without expanding $PWD)
echo $PWD             # Outputs the path to the working directory. Note the output difference in the two commands.
echo 'Hello $USER'    # Outputs "Hello $USER" (without expanding $USER)
echo $USER            # outputs "Hello <username>"
echo "Hello $USER"    # Outputs "Hello <username>"
echo "Path $PWD"      # Outputs "Path </path to the working directory>
```

![[Séance TP2 - image4.png]]
*Figure : `echo 'Hello $USER'` affiche `Hello $USER` ; `echo "Hello $USER"` affiche `Hello momo`.*

## 1.5 Caractères des chemins (*Special Characters for File Paths and Locations*)

Voir [[Chemin de fichier]] et [[Répertoire personnel]].

```bash
cd /home/user    # / : sépare les répertoires dans un chemin
cd ~             # ~ : répertoire personnel de l'utilisateur courant
./script.sh      # . : répertoire courant ; exécute script.sh qui s'y trouve
cd ..            # .. : répertoire parent ; remonte d'un niveau
```

Créer un fichier dont le nom contient des espaces, en les échappant :

![[Séance TP2 - image11.png]]
*Figure : `touch My\ File\ With\ Spaces.txt` puis `ls` affiche `'My File With Spaces.txt'` entre apostrophes.*

## 1.6 Caractères d'échappement (*Special Escaping Characters*)

Traiter certains caractères comme des littéraux.

```bash
rm file\ name.txt     # \ : échappe le caractère suivant → supprime "file name.txt"
rm file\ file2.txt    # commentaire du support : supprime "file2.txt" (voir point à vérifier 2)
echo `pwd`            # `` (backticks) : exécute la commande et substitue sa sortie → affiche le répertoire courant
```

Les apostrophes inversées (*backticks*) réalisent une [[Substitution de commande]]. Sur le clavier : Alt+7 (« Alt Gr + 7 » sur un clavier AZERTY, voir point à vérifier 5). On s'en sert pour mettre le résultat d'une commande dans une variable ou un fichier.

![[Séance TP2 - image13.png]]
*Figure : ``CURRENT_DATE=`date` ; echo $CURRENT_DATE`` → « Mon Nov 18 11:52:40 AM CET 2024 ».*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Wc = write count »** : `wc` signifie *word count*, l'étudiante le dit elle-même mal (complément).
2. **Commentaires de code erronés** : `echo 'path $PWD'` annoncé comme sortie « Hello $PWD » ; `rm file\ file2.txt` annoncé comme supprimant « file2.txt » (la commande supprime en réalité un fichier nommé « file file2.txt »). **Vérifié sur l'image** pour le premier : l'erreur est bien dans le support. De même, `echo $USER` est annoncé comme affichant « Hello <username> » alors qu'il n'affiche que le nom.
3. **Écart blanc entre `&` et `;`** : la transcription évoquait un symbole perdu (`&&` ou `||`). **Vérifié sur l'image** : simple espacement, aucun symbole manquant. Fausse alerte.
4. **Fin de la liste du `grep`** : l'alerte sur la ligne coupée est sans conséquence.
5. **« backsticks = alt + 7 »** : raccourci noté par l'étudiante ; sur un clavier AZERTY français c'est Alt Gr + 7 (complément).
6. **`ls | grep "\txt"`** : le texte de la note écrit `"\txt"` sans point, la capture montre `"\.txt"` (la capture fait foi).
