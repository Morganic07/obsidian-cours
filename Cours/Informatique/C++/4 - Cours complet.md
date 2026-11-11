---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
complet: true
enrichi: 2026-11-11
---

Résumé de [[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]] (polycopié de TP de 40 pages, « TP Développement C++ », version 1.0 de 2012, en trois parties avec questions de révision, six exercices et un bilan par partie), dans [[Cours/Informatique/C++/_index|C++]]. Il double le diaporama du même chapitre, [[4 - C++]], sur les bases du [[Langage C++|C++]] : fabrication d'un [[Programme informatique|programme]], [[Variable (programmation)|variables]] et [[Type primitif|types]], [[Flux d'entrée-sortie (C++)|entrées-sorties]], [[Structure conditionnelle|conditions]] et [[Boucle (programmation)|boucles]], [[Fonction et procédure|fonctions]] et [[Programmation modulaire|programmation modulaire]]. La [[Programmation orientée objet|programmation objet]] (classes, constructeurs, surcharge) n'y figure pas : voir [[4 - C++]].

Le polycopié s'appuie sur le livre de référence de Bjarne Stroustrup, créateur du C++ ([[Principes et pratique avec C++ (livre)]]), dont il reprend beaucoup de conseils et d'exemples. Il rappelle que les TP servent à **pratiquer** : comprendre en lisant ne suffit pas, la répétition est nécessaire, comme en sport ou en musique.

**Le polycopié date de 2012**, juste après la publication de la [[Norme du C++|norme C++11]] (ISO/IEC 14882:2011, septembre 2011), et son code est écrit en C++98 : pas d'[[Initialisation (programmation)|initialisation par accolades]], pas de [[Mot-clé auto|`auto`]], pas de `nullptr`. Les normes suivantes (C++14, C++17, C++20, C++23) n'invalident aucun des programmes donnés, mais changent les conseils : les encadrés « En C++ moderne » de cette fiche le signalent. Depuis GCC 11 (2021), [[GCC|g++]] compile par défaut en C++17 (`-std=gnu++17`). [[Complément hors du cours|ⓘ]]

## Sommaire

1. **Le premier programme** : « Hello world », [[Compilateur|compilation]], [[Édition de liens|édition des liens]], [[Environnement de développement intégré|environnement de programmation]], manipulations sous [[Linux]], exercices 1 et 2.
2. **Structure d'un programme informatique simple** : objets, types et valeurs, entrée avec `cin`, opérateurs, [[Règle de codage|règles de codage]], [[Affectation|affectation]] et [[Initialisation (programmation)|initialisation]], exercice 3.
3. **Programmation modulaire** : [[Expression (programmation)|expressions]] et [[Instruction (programmation)|instructions]], [[Constante (programmation)|constantes]], [[Référence (C++)|références]] et [[Pointeur et adresse mémoire|pointeurs]], fonctions, règles de codage, exercices 4 à 6.

# Première partie : le premier programme

## Hello world

Le [[Programme Hello world|programme « Hello world »]] est le premier programme qu'on étudie habituellement : il affiche « Hello world ! » à l'écran.

```cpp
// Ce programme affiche le message "Hello world !" à l'écran

#include <iostream>

using namespace std;

int main()
{
    cout << "Hello world !\n"; // Affiche "Hello world !"

    return 0;
}
```

## Explications

**La fonction `main`.** Tout programme C/C++ doit posséder une [[Fonction main (C et C++)|fonction nommée `main`]] (« principale »), qui indique où commencer l'exécution. Une [[Fonction et procédure|fonction]] est une suite d'[[Instruction (programmation)|instructions]] que l'ordinateur exécute dans l'ordre où elles sont écrites. Elle comprend **quatre parties** :

- un **type de retour** : ici `int` (*integer*, entier), le genre de résultat que la fonction retournera. `int` est un [[Mot réservé|mot réservé]] (mot-clé) : il ne peut pas nommer autre chose ;
- un **nom** : ici `main` ;
- une **liste de paramètres** entre parenthèses, ici vide (voir [[Argument et paramètre]]) ;
- un **corps** entre accolades, qui énumère les instructions à exécuter (un [[Bloc d'instructions|bloc]]).

La plupart des instructions C/C++ se terminent par un **point-virgule** (`;`).

**Chaînes et caractères spéciaux.** Une [[Chaîne de caractères|chaîne de caractères]] est délimitée par des guillemets anglais (`"`) : `"Hello world !\n"` en est une. `\n` est un caractère spécial qui passe à la ligne (*newline*) : c'est une séquence d'[[Caractère d'échappement|échappement]].

**Sortie.** `cout` (*character output stream*) désigne le **flux de sortie standard**, l'écran par défaut ([[Flux standard]]) ; les caractères « placés dans `cout` » avec l'**opérateur de sortie** `<<` apparaissent à l'écran (voir [[Flux d'entrée-sortie (C++)]]).

**Commentaires.** Tout ce qui suit `//` sur une ligne est un [[Commentaire (programmation)|commentaire]], ignoré par le [[Compilateur|compilateur]]. Il rend le code lisible pour les programmeurs : on y décrit ce que le programme est censé faire, et ce qu'on ne peut pas exprimer dans le code. La première ligne du programme est le **commentaire classique** à mettre en tête de tout programme : il dit ce que le programme est **censé** faire (pas ce qu'on a voulu qu'il fasse). Le C++ a aussi des commentaires sur plusieurs lignes, `/* … */`, hérités du [[Langage C|C]] ; ils ne s'imbriquent pas. [[Complément hors du cours|ⓘ]]

**`return 0;`** La fonction `main` retourne 0 à celui qui l'a appelée, le « système ». Sous [[Unix]]/[[Linux]], cette valeur sert à vérifier que le programme s'est bien exécuté : par convention Unix, **0 signifie succès**, une autre valeur signale une erreur et peut en préciser le type (voir [[Code de retour]]). En C++, `main` est la seule fonction non `void` qui peut omettre son `return` : atteindre sa fin équivaut à `return 0;`. [[Complément hors du cours|ⓘ]]

**`#include`.** Une ligne qui commence par `#` est une **directive** du [[Préprocesseur|préprocesseur]] (ou de précompilation), qui ne traite pas d'instructions C/C++ (donc pas de `;`). [[Directive include|`#include <iostream>`]] rend accessibles les fonctionnalités du fichier `iostream`, fourni avec le compilateur, qui permet d'utiliser `cout` et `<<`. Un fichier inclus porte généralement l'[[Extension de nom de fichier|extension]] `.h` : c'est un [[Fichier d'en-tête|fichier d'en-tête]] (*header*). En C++, les en-têtes standard n'ont pas d'extension.

Plus précisément, depuis la norme C++98 les en-têtes de la [[Bibliothèque standard du C++|bibliothèque standard]] s'écrivent sans `.h` (`<iostream>`, `<string>`, `<cmath>`) ; les anciens `<iostream.h>` d'avant la norme n'existent plus, et les en-têtes du C s'écrivent `<cmath>` plutôt que `<math.h>` (voir [[Bibliothèque cmath]]). Les fichiers d'en-tête du programmeur gardent `.h` (ou `.hpp`). [[Complément hors du cours|ⓘ]]

**`using namespace std;`** indique qu'on utilise par défaut l'[[Espace de noms (namespace)|espace de noms]] `std`, celui de la bibliothèque standard. `cout` et `cin` y sont définis, mais le même nom pourrait exister dans un autre espace de noms : leur nom complet est `std::cout`. L'[[Opérateur de résolution de portée|opérateur `::`]] réalise la **résolution de portée**, « un peu comme le `/` dans un chemin ». Comme on utilise presque tout le temps la bibliothèque standard, on écrit presque toujours `using namespace std;` pour se simplifier la vie.

En C++ moderne, cette habitude est déconseillée hors des petits programmes : elle importe des centaines de noms (`count`, `distance`, `max`…) qui peuvent entrer en conflit avec les siens, et elle est à proscrire dans un fichier d'en-tête, où elle s'imposerait à tous les fichiers qui l'incluent (C++ Core Guidelines, règle SF.7). On préfère écrire `std::cout`, ou n'importer que les noms utiles : `using std::cout;`. [[Complément hors du cours|ⓘ]]

## Compilation

Le C++ (comme le C) est un [[Langage compilé|langage compilé]] : avant d'exécuter un programme, il faut traduire sa forme lisible par un humain en une forme que la machine « comprend ». Cette traduction est faite par un programme, le [[Compilateur|compilateur]]. Ce que le programmeur écrit est le [[Code source|code source]] (ou programme source) ; ce que l'ordinateur exécute s'appelle [[Exécutable|exécutable]], [[Fichier objet|code objet]] ou [[Code machine|code machine]].

*Figure (schéma du polycopié)* : code source C++ (extension `.cpp` ou `.cc`) → compilateur C++ (g++ par exemple), qui **vérifie la syntaxe** et **traduit** le code source en code objet → code objet (extension `.obj` sous [[Microsoft Windows|Windows]], `.o` sous Unix/Linux). Le même schéma vaut pour le C : fichier `.c`, compilateur C (gcc par exemple).

Le compilateur est **pointilleux sur la syntaxe**, et la plupart du temps le code contient des erreurs. S'il refuse un programme, il a généralement raison : on a écrit quelque chose qui n'est pas défini précisément par la [[Norme du C++|norme C++]], et il ne peut pas produire de code objet. Il est dénué de bon sens, d'où sa rigueur : il faut lire et analyser ses messages d'[[Erreur de compilation|erreur]], car « le compilateur est votre ami ».

Le passage du source à l'exécutable comprend en fait plusieurs étapes, que la commande `g++` enchaîne : le [[Préprocesseur|prétraitement]] (`#include`, `#define`), la compilation proprement dite vers le [[Langage d'assemblage|langage d'assemblage]], l'assemblage en code objet, puis l'[[Édition de liens|édition de liens]]. L'ensemble forme la [[Chaîne de compilation|chaîne de compilation]] ; `g++ -E` s'arrête après le préprocesseur, `g++ -S` après la compilation, `g++ -c` après l'assemblage. [[Complément hors du cours|ⓘ]]

## Édition des liens

Un programme est fait de plusieurs parties, souvent écrites par des personnes différentes : « Hello world » contient la partie que nous avons écrite et d'autres issues de la [[Bibliothèque standard du C++|bibliothèque standard]] du C++ (`cout` par exemple). Le programme qui lie ces parties en un exécutable est l'**éditeur de liens** (*linker*), voir [[Édition de liens]].

*Figure (schéma du polycopié)* : code objet (`.obj` ou `.o`) + autre(s) code(s) objet(s) → éditeur de liens (`ld`, mais gcc/g++ peuvent réaliser cette tâche), qui **lie les références aux symboles** (internes et externes) et **produit le programme exécutable** → exécutable (extension `.exe` sous Windows, aucune sous Unix/Linux).

- Le code objet et les exécutables **ne sont pas portables** d'un système à l'autre : compilé pour Windows, un programme ne fonctionne pas sous Linux (voir [[Portabilité (informatique)]]). Le code source, lui, est portable s'il s'en tient à la norme : il suffit de le recompiler sur chaque système. [[Complément hors du cours|ⓘ]]
- Une **bibliothèque** n'est que du code (sans fonction `main`), auquel on accède par des **déclarations** placées dans un fichier d'en-tête. Une déclaration indique comment utiliser une portion de code qui se trouve dans une bibliothèque (voir [[Déclaration et définition]], [[Module, paquet, bibliothèque et framework|bibliothèque logicielle]]). Le débutant confond souvent bibliothèque et fichier d'en-tête : l'en-tête dit **ce qui existe**, la bibliothèque contient **le code compilé**.
- Une **bibliothèque dynamique** contient du code intégré **au moment de l'exécution** : le programme est plus petit et profite des mises à jour de la bibliothèque, mais il dépend de sa présence sur le système cible. Elle s'appelle *Dynamic Link Library* (`.dll`) sous Windows et *shared object* (`.so`) sous Unix/Linux : c'est un fichier utilisé par l'exécutable sans en faire partie (voir [[Bibliothèque partagée]]).
- À l'inverse, une [[Bibliothèque statique|bibliothèque statique]] (`.a` sous Linux, `.lib` sous Windows) est recopiée dans l'exécutable à l'édition de liens : le programme est plus gros mais autonome. [[Complément hors du cours|ⓘ]]

**Trois sortes d'erreurs** :

| Erreur | Détectée par | Difficulté |
|---|---|---|
| [[Erreur de compilation\|erreur de compilation]] | le compilateur | la plus facile à comprendre et corriger |
| erreur de liaison (d'édition de liens) | l'éditeur de liens | intermédiaire |
| erreur d'exécution ou de logique ([[Bogue (informatique)\|bug]]) | à l'exécution | la plus difficile |

Exemple typique d'erreur de liaison : une fonction déclarée et appelée, mais jamais définie ou dont le fichier objet n'est pas fourni ; g++ (par `ld`) répond `undefined reference to 'carre(int)'`. [[Complément hors du cours|ⓘ]]

## Environnement de programmation

Pour programmer, il faut un **langage de programmation**, un **compilateur** (source → code objet), un **éditeur de liens** (codes objets → exécutable) et un [[Éditeur de texte|éditeur de texte]] pour saisir et modifier le source, à ne pas confondre avec un [[Traitement de texte|traitement de texte]]. C'est la boîte à outils du programmeur, ou **environnement de développement**.

- **En ligne de commande** (« mode console ») : on tape soi-même les commandes qui produisent puis lancent l'exécutable (voir [[Interface en ligne de commande]]). *Figure 1* : développement sur la console.
- **Dans un [[Environnement de développement intégré|environnement de développement intégré]]** (EDI, *IDE*) : un clic sur le bon bouton suffit. *Figure 2* : développement avec [[Qt Creator]]. Un EDI réunit aussi la documentation en ligne, la [[Git|gestion de version]] et surtout un [[Débogueur|débogueur]] (*debugger*), qui aide à trouver et éliminer les erreurs.

EDI cités : Visual C++ ([[Visual Studio]]), C++ Builder, [[Qt Creator]], Code::Blocks, Dev-C++, [[Eclipse (logiciel)|Eclipse]]. Ce ne sont que des outils, qui améliorent surtout la productivité professionnelle : apprendre le C/C++ n'en demande pas.

En 2026, les outils les plus répandus sont [[Visual Studio Code]] (éditeur extensible, gratuit), Visual Studio (Windows), CLion (JetBrains) et Qt Creator ; Dev-C++ et C++ Builder sont devenus marginaux. Les compilateurs courants sont GCC (g++), Clang (LLVM) et MSVC (Microsoft). [[Complément hors du cours|ⓘ]]

## Manipulations

L'objectif est de mettre en œuvre la **chaîne de fabrication g++ sous Linux** (voir [[GCC]]).

**Étape 1 : espace de travail.** Dans son [[Répertoire personnel|répertoire personnel]], créer un répertoire `C-C++` pour tous les TP, et dedans un répertoire `tp1`. On peut passer par l'interface graphique (un [[Gestionnaire de fichiers|gestionnaire de fichiers]] comme Dolphin) ou par une console ([[Émulateur de terminal|Konsole]] sous [[KDE]]) :

```bash
mkdir C-C++
cd C-C++
mkdir tp1
cd tp1
```

Voir [[Commande mkdir]] et [[Commande cd]].

**Étape 2 : édition du source.** Avec un éditeur de texte ([[Vim|vi, vim]], [[Emacs|emacs]], kwrite, kate, [[Gedit|gedit]] sous Linux ; Notepad, [[Notepad++]], UltraEdit sous Windows), taper **à la main** (pas de copier-coller, pour s'habituer à la syntaxe) le programme suivant dans `helloWorld.cpp` :

```cpp
#include <iostream>

using namespace std;

int main()
{
    int decompte = 5;

    while(decompte > 0)
    {
        cout << "Hello ";
        cout << "world" << " !" << endl;
        decompte = decompte - 1;
    }

    return 0;
}
```

Il affiche cinq fois « Hello world ! » : la [[Boucle (programmation)|boucle `while`]] se répète tant que `decompte > 0`, et `decompte` diminue de 1 à chaque tour. `endl` passe à la ligne et vide le [[Tampon (buffer)|tampon]] de sortie. [[Complément hors du cours|ⓘ]]

**Étape 3 : vérifier le compilateur.** Dans une console, taper `g++`. La réponse « `g++: no input file` » (« pas de fichier à l'entrée ») signifie que tout va bien : le compilateur est installé et se plaint seulement qu'on ne lui a rien donné à compiler. « `bash: g++ : commande introuvable` » signifie que l'[[Shell et Bash|interpréteur de commandes]] (bash) ne le trouve pas ou qu'il n'est pas installé. Les versions récentes de GCC répondent `g++: fatal error: no input files` ; sous Debian ou Ubuntu, on installe le compilateur avec `sudo apt install g++` (ou le paquet `build-essential`). [[Complément hors du cours|ⓘ]]

**Étape 4 : se placer dans le bon répertoire.**

- `ls` (`ls -l` pour plus de détails) affiche le contenu du répertoire courant ; l'équivalent Windows est `dir` (voir [[Commande ls]]).
- `cd` change de répertoire : `cd C-C++`, puis `cd tp1`.
- L'[[Invite de commande|invite de commande]] (*prompt*, le message qui précède le curseur) affiche toujours le nom du répertoire courant.
- `..` désigne le **répertoire parent** (`cd ..` remonte d'un niveau) et `.` le **répertoire courant** (voir [[Chemin de fichier]], [[Commande pwd]]).
- Sous Linux, on lance un programme du répertoire courant par `./helloWorld` (« dans le répertoire courant, le fichier helloWorld ») : les exécutables n'y ont pas d'extension, contrairement à Windows (`.exe`).
- Le séparateur de [[Chemin de fichier|chemin]] est `\` sous Windows et `/` sous Linux : `cd C-C++\tp1` (Windows), `cd C-C++/tp1` (Linux).

Question du polycopié : que fait `cd .` et pourquoi ? Rien : `.` désigne le répertoire où l'on est déjà, on y reste. Il faut écrire `./helloWorld` parce que le shell ne cherche les commandes que dans les répertoires de la variable `PATH`, qui ne contient pas le répertoire courant (par sécurité). [[Complément hors du cours|ⓘ]]

**Étape 5 : fabriquer le programme**, en deux commandes :

```bash
g++ -Wall -c helloWorld.cpp           # préprocesseur + compilation + assemblage → helloWorld.o
g++ -Wall -o helloWorld helloWorld.o  # édition des liens → exécutable helloWorld
./helloWorld                          # exécution
```

La première produit le [[Fichier objet|fichier objet]] `helloWorld.o` dans le même répertoire (vérifier avec `ls -l`) ; la seconde fait l'édition des liens entre les `.o` (unification des variables et des fonctions qu'ils contiennent) et produit l'[[Exécutable|exécutable]] `helloWorld`. Les [[Option de compilation|options]] : `-Wall` active les principaux avertissements, `-c` s'arrête au fichier objet, `-o` nomme le fichier produit.

En une seule commande, `g++ -Wall -o helloWorld helloWorld.cpp` fait les deux étapes ; sans `-o`, l'exécutable s'appelle `a.out` (c'est le `./a.out` des exemples suivants). On ajoute volontiers `-Wextra` (avertissements supplémentaires), `-std=c++17` ou `-std=c++20` (choix de la norme) et `-g` (informations pour le débogueur). [[Complément hors du cours|ⓘ]]

## Questions de révision (première partie)

Les réponses sont des compléments ; le polycopié ne les donne pas.

1. **Quel est le but du programme « Hello world » ?**
   - Se familiariser avec les outils (éditeur, compilateur, éditeur de liens, lancement) sur un programme minimal, pour vérifier que toute la chaîne fonctionne avant d'écrire du vrai code. [[Complément hors du cours|ⓘ]]
2. **Quelles sont les quatre parties d'une fonction ?**
   - Le type de retour, le nom, la liste de paramètres entre parenthèses, le corps entre accolades. [[Complément hors du cours|ⓘ]]
3. **Citez une fonction qui doit apparaître dans tout programme C ou C++.**
   - `main`. [[Complément hors du cours|ⓘ]]
4. **À quoi sert la ligne `return 0;` ?**
   - À terminer `main` en renvoyant au système le [[Code de retour|code de retour]] 0, qui signifie « exécution réussie » (lisible dans le shell par `echo $?`). [[Complément hors du cours|ⓘ]]
5. **Quel est le rôle du compilateur ?**
   - Vérifier la syntaxe et les types du code source, puis le traduire en code objet (code machine). [[Complément hors du cours|ⓘ]]
6. **À quoi sert la directive `#include` ?**
   - À faire recopier par le préprocesseur le contenu d'un fichier (en général un en-tête) à cet endroit, pour disposer de ses déclarations. [[Complément hors du cours|ⓘ]]
7. **Que signifie l'extension `.h` ?**
   - Un fichier d'en-tête (*header*), qui contient des déclarations destinées à être incluses. [[Complément hors du cours|ⓘ]]
8. **Que fait l'éditeur de liens pour votre programme ?**
   - Il réunit les fichiers objets et les bibliothèques en un exécutable, en reliant chaque appel (`cout`, `carre`…) au code qui le définit. [[Complément hors du cours|ⓘ]]
9. **Différence entre fichier source et fichier objet ?**
   - Le [[Fichier source|fichier source]] (`.cpp`) est du texte écrit par le programmeur ; le fichier objet (`.o`) est sa traduction en code machine, pas encore exécutable car ses références externes ne sont pas résolues. [[Complément hors du cours|ⓘ]]
10. **Qu'est-ce qu'un EDI et que fait-il pour vous ?**
    - Un logiciel qui réunit éditeur, compilation, édition de liens, exécution, débogueur et documentation dans une même interface, et lance la fabrication en un clic. [[Complément hors du cours|ⓘ]]

## Exercice 1 : corriger des erreurs

But : apprendre à interpréter les erreurs signalées par le compilateur.

**Q11.** Éditer `aCorriger.cpp` et tenter de le compiler. Faut-il utiliser g++ ou gcc ?

```cpp
/Qu'est censé faire ce programme ?

// auteur : …

include <iostrem>

using namespace std;

integer main()
{
 /* Vous devez corriger ce programme et arriver à le compiler puis l'exécuter.
 cout << 'Le programme marche !' << end;
 int valeur = 10
 cout << "valeur =" << valeur << end;
 // Attention : la division de deux entiers est une division euclidienne,
 // c'est-à-dire une division ***ENTIERE*** !
 int quotient = 10 / 3
 cout << "quotient=" << quotient << end;
 int reste = 10 % 3
 cout << "reste=" << reste << end;
 // Si vous voulez faire une division réelle, il faut convertir un des
 // arguments en réel :
 out << "quotient reel =" << valeur / 3.0 <<end; // Cette fois-ci 3.0 est réel
 out << "Fin du programme;
 return 0;
}
```

**Q12.** Corriger jusqu'au bon fonctionnement, puis ajouter le commentaire classique en tête.

Consignes du polycopié :

- corriger d'abord ce qu'on voit en lisant ; au-delà, c'est au compilateur de dire où sont les erreurs de syntaxe ;
- **ne considérer que la première erreur signalée** : les suivantes peuvent n'être que des conséquences de la première, mal comprise par le compilateur ; la corriger, recompiler, recommencer ;
- utiliser le numéro de ligne indiqué : l'erreur est à cette ligne **ou un peu avant**, là où il devient manifeste pour le compilateur que le programme est faux ;
- demander de l'aide, ou une relecture à un camarade : on voit mal ses propres fautes quand on a « le nez dedans ».

Corrigé : il faut **g++**, car c'est un programme C++ (`iostream`, `cout`) ; `gcc` compilerait le `.cpp` en C++ mais ne lierait pas la bibliothèque standard du C++, d'où des erreurs d'édition de liens. Les erreurs : `/` au lieu de `//` en ligne 1 ; `#` manquant devant `include` ; `iostrem` pour `iostream` ; `integer` n'existe pas (`int`) ; le commentaire `/*` n'est jamais fermé et avale tout le programme ; `'…'` délimite un seul caractère, une chaîne s'écrit entre `"…"` ; `end` pour `endl` ; trois `;` manquants ; `out` pour `cout` ; guillemet fermant manquant. [[Complément hors du cours|ⓘ]]

```cpp
// Affiche un message, puis le quotient et le reste de 10 par 3 (division entière et réelle)

#include <iostream>

using namespace std;

int main()
{
    // Vous devez corriger ce programme et arriver à le compiler puis l'exécuter.
    cout << "Le programme marche !" << endl;
    int valeur = 10;
    cout << "valeur =" << valeur << endl;
    int quotient = 10 / 3;                              // 3 : division entière
    cout << "quotient=" << quotient << endl;
    int reste = 10 % 3;                                 // 1 : reste de la division
    cout << "reste=" << reste << endl;
    cout << "quotient reel =" << valeur / 3.0 << endl;  // 3.33333
    cout << "Fin du programme" << endl;
    return 0;
}
```

Entre deux entiers, `/` donne le quotient de la [[Division euclidienne|division euclidienne]] et `%` son reste (voir [[Opérateurs arithmétiques]]) ; dès qu'un opérande est réel (`3.0`, un `double`), l'autre est converti et la division est réelle (voir [[Transtypage]], [[Nombre à virgule flottante]]). [[Complément hors du cours|ⓘ]]

## Exercice 2 : faire évoluer un programme

**Q13.** Tester le programme suivant. Que permet de faire `cin` ? En proposer une définition.

```cpp
// Affiche à l'écran un entier saisi par l'utilisateur

#include <iostream>

int main (int argc, char **argv)
{
    int n;

    std::cout << "Donnez un entier : " << std::endl;
    std::cin >> n;
    std::cout << "Vous avez donné l'entier : " << n << std::endl;

    return 0;
}
```

Réponse : `cin` (*character input stream*) est le **flux d'entrée standard** (le clavier par défaut) ; `cin >> n` lit au clavier une valeur du type de `n` et la range dans `n`. Les paramètres `argc` et `argv` de `main` reçoivent les arguments de la ligne de commande (leur nombre et leur texte) ; ce programme ne s'en sert pas, `int main()` suffirait. [[Complément hors du cours|ⓘ]]

**Q14.** Modifier « Hello world (version 2) » pour afficher n fois le message, n étant saisi par l'utilisateur. Que se passe-t-il si n est négatif ?

Solution courte : remplacer `int decompte = 5;` par `int decompte = 0; cin >> decompte;`. Si n ≤ 0, la condition `decompte > 0` est fausse dès le départ : la boucle ne s'exécute pas et rien ne s'affiche, sans erreur. [[Complément hors du cours|ⓘ]]

## Bilan (première partie)

« Hello world » sert à se familiariser avec les outils de base. Règle à retenir : **prendre un exemple extrêmement simple à chaque fois qu'on découvre un nouvel outil**, pour apprendre l'outil d'abord, puis le langage sans être distrait par l'outil ; découvrir les deux à la fois est bien plus difficile. Décomposer une tâche complexe en étapes plus petites vaut dans la plupart des domaines, surtout ceux qui demandent une compétence pratique.

Le polycopié cite Descartes, [[Discours de la méthode]] (1637), deuxième et troisième préceptes : « diviser chacune des difficultés que j'examinerais, en autant de parcelles qu'il se pourrait, et qu'il serait requis pour les mieux résoudre » ; « conduire par ordre mes pensées, en commençant par les objets les plus simples et les plus aisés à connaître, pour monter peu à peu comme par degrés jusques à la connaissance des plus composés ».

# Deuxième partie : structure d'un programme informatique simple

## Structure

Un programme est souvent structuré en trois blocs : **entrée(s)** (par exemple la lecture des données au clavier, `cin`) → **traitement, calcul** (le cœur du programme, la partie cachée de « l'iceberg ») → **sortie(s)** (par exemple l'affichage des résultats à l'écran, `cout`). Les vrais programmes produisent des résultats en fonction de l'entrée qu'on leur fournit. Pour lire quelque chose, il faut un « endroit » de la [[Mémoire vive|mémoire]] où le placer : on l'appelle un **objet**.

## Objets, types et valeurs

Un **objet** est une région de la mémoire dotée d'un **type**, qui spécifie quelle sorte d'information on peut y placer. Un objet nommé s'appelle une **[[Variable (programmation)|variable]]**. Exemples : les chaînes de caractères sont stockées dans des variables de type `string`, les entiers dans des `int`, les réels dans des `float`. On peut se représenter un objet comme **une boîte** qui porte un nom (`age`), un type (`int`) et contient une **valeur** (46).

Le mot « objet » a ici son sens de la norme C++ (une zone de mémoire typée), plus large que l'objet de la [[Programmation orientée objet|programmation objet]], instance d'une [[Classe et objet|classe]] (voir [[4 - C++]]). [[Complément hors du cours|ⓘ]]

```cpp
// Réalise la saisie de l'age et du nom de l'utilisateur

#include <iostream>
#include <string>

int main ()
{
    int age;          // Réserve une région de la mémoire destinée à contenir un entier et lui attribue le nom age
    std::string nom;  // Réserve une région de la mémoire destinée à contenir une chaîne et lui attribue le nom nom

    std::cout << "Donnez votre âge : " << std::endl; // Message d'invite
    std::cin >> age;                                 // Lit la valeur saisie et la place dans age
    std::cout << "Donnez votre nom : " << std::endl;
    std::cin >> nom;                                 // Lit les caractères et les place dans nom
    // ...
    return 0;
}
```

Sans `using namespace std;`, le type chaîne doit s'écrire `std::string`, et il se déclare dans l'en-tête `<string>` : écrit `string nom;` avec le seul `#include <iostream>`, ce programme ne compile pas (`'string' was not declared in this scope`). [[Erreurs du cours#^e-4-cours-complet|✎]]

Il est fondamentalement impossible de faire quoi que ce soit avec un ordinateur sans stocker des données en mémoire (la RAM).

**Définition et initialisation.** Une instruction qui définit une variable est une **définition** (voir [[Déclaration et définition]]). Une définition peut, et généralement doit, fournir une **valeur initiale** : trop de programmes ont eu des bugs dus à des [[Variable non initialisée|variables non initialisées]]. Le polycopié l'impose : c'est une **[[Règle de codage|règle de codage]]**.

```cpp
int nombreDeTours = 100;      // Correct : 100 est une valeur entière
string prenom = "Robert";     // Correct : "Robert" est une chaîne de caractères

int nombreDeTours = "Robert"; // Erreur : "Robert" n'est pas une valeur entière
string prenom = 100;          // Erreur : 100 n'est pas une chaîne (il manque les guillemets)
```

Le compilateur se souvient du type de chaque variable et vérifie qu'on l'utilise conformément à sa définition : c'est le [[Typage statique|typage statique]].

**Les cinq types usuels.** Le C++ a de nombreux types, mais la plupart des programmes se contentent de cinq :

| Type | Usage | Exemple |
|---|---|---|
| [[Type entier\|`int`]] | entiers | `int nombreDeTours = 100;` |
| [[Nombre à virgule flottante\|`double`]] | nombres en virgule flottante (double précision) | `double tempsDeVol = 3.5;` |
| [[Classe string (C++)\|`string`]] | chaînes de caractères | `string prenom = "Robert";` |
| [[Type char\|`char`]] | caractères individuels, ou entiers sur 8 bits (un [[Octet\|octet]]) | `char pointDecimal = '.';` |
| [[Booléen\|`bool`]] | variables logiques (booléennes) | `bool ouvert = true;` |

`string` n'existe pas en C, où une chaîne est un [[Tableau (programmation)|tableau]] de `char` terminé par `'\0'`. `bool` existe en revanche en C depuis la norme C99 (type `_Bool`, nommé `bool` par `<stdbool.h>`), et c'est un mot-clé depuis C23 (voir [[Norme du C]]). [[Erreurs du cours#^e-4-cours-complet|✎]]

Ordres de grandeur sur une machine actuelle (x86-64, Linux) : `int` occupe 4 octets (de −2 147 483 648 à 2 147 483 647), `double` 8 octets (environ 15 chiffres significatifs, norme [[Norme IEEE 754|IEEE 754]]), `char` 1 octet, `bool` 1 octet. La norme ne fixe que des minimums (un `int` fait au moins 16 bits) ; `sizeof(int)` donne la taille réelle. `string` n'est pas un type de base mais une classe de la bibliothèque standard, qui gère seule sa mémoire. [[Complément hors du cours|ⓘ]]

En C++ moderne, on initialise volontiers avec des accolades (C++11) : `int nombreDeTours{100};`. Cette forme interdit les conversions avec perte (`int n{3.5};` est refusé, alors que `int n = 3.5;` tronque silencieusement à 3) ; `int n{};` initialise à 0. Voir [[Initialisation (programmation)]]. [[Complément hors du cours|ⓘ]]

## Entrée

Rappel : une instruction qui introduit un nouveau nom et réserve de la mémoire pour une variable est une **définition**.

`cin` (*character input stream*) désigne le **flux d'entrée standard** (le clavier par défaut) de la bibliothèque standard. L'**opérateur `>>`** (« obtenir depuis ») indique où va l'entrée. Il est **sensible au type** : la lecture dépend du type de la variable de destination, comme l'écriture avec `<<`.

```cpp
std::string nom;
int age;
std::cout << "Donnez votre nom et votre âge : " << std::endl;
std::cin >> nom;  // Lit les caractères et les place dans nom
std::cin >> age;  // Lit la valeur saisie et la place dans age
```

Pourquoi `cin` ne met-il pas toute la saisie dans `nom` ? Par convention, la lecture d'une chaîne s'arrête au premier **[[Espace blanc|espace blanc]]** (*whitespace*) : espace, tabulation ou retour à la ligne ; et les espaces qui précèdent sont ignorés par défaut.

**Q15.** Inverser la saisie de `nom` et `age`. Que constate-t-on ? Si l'utilisateur tape toujours « Robert 25 », `cin >> age` rencontre `R`, qui ne peut pas commencer un entier : la lecture échoue, `cin` passe en **état d'échec** et toutes les lectures suivantes sont ignorées, donc `nom` reste vide. Depuis C++11, `age` reçoit alors 0 ; en C++98 il gardait sa valeur, indéterminée s'il n'était pas initialisé. L'ordre des lectures doit suivre celui de la saisie ; `if (cin >> age)` permet de tester la réussite. [[Complément hors du cours|ⓘ]]

**Q16.** Écrire un programme qui saisit le nom et le prénom et affiche « Bienvenue nom prénom ! ». Si le nom contient des espaces, il faut la [[Fonction getline|fonction `getline`]].

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string nom, prenom;
    cout << "Votre nom : ";
    getline(cin, nom);          // lit toute la ligne, espaces compris
    cout << "Votre prénom : ";
    getline(cin, prenom);
    cout << "Bienvenue " << nom << " " << prenom << " !" << endl;
    return 0;
}
```

Solution proposée [[Complément hors du cours|ⓘ]]. Le polycopié renvoie à la documentation de www.cplusplus.com ; la référence la plus utilisée aujourd'hui est [[Cppreference|cppreference.com]]. Piège classique : après un `cin >> n`, le retour à la ligne reste dans le flux et un `getline` qui suit lit une ligne vide ; on l'évite avec `cin >> ws` ou `cin.ignore()`. [[Complément hors du cours|ⓘ]]

## Opérations et opérateurs

Le type d'une variable fixe les valeurs qu'elle peut contenir, mais aussi **les opérations qu'on peut lui appliquer et leur sens**.

```cpp
string fils = nom + " Junior"; // Ajoute (concatène) des caractères à la fin
int ageApres = age + 1;        // Additionne des entiers

string s = nom - " Junior";    // Erreur : cet opérateur n'est pas défini pour string !
int ageAvant = age - 1;        // Soustrait des entiers
```

Le compilateur rejette la soustraction de chaînes, car il sait exactement quelles opérations s'appliquent à chaque type : `erreur: no match for 'operator-' in 'nom - " Junior"'`. Pour une `string`, `+` est la **[[Chaîne de caractères|concaténation]]** : c'est une [[Surcharge d'opérateurs|surcharge d'opérateur]] définie par la classe `string`. [[Complément hors du cours|ⓘ]]

En revanche, il accepte sans broncher des opérations **légales mais absurdes** : `int age = -100;`. Personne ne lui a dit qu'un âge ne peut pas être négatif ; il produit le code, et on aura peut-être un bug plus tard. C'est au programme de contrôler ses saisies (voir [[Validation des entrées]]). [[Complément hors du cours|ⓘ]]

Le polycopié renvoie au cours pour la liste des opérateurs ; voici les principaux [[Complément hors du cours|ⓘ]] :

| Catégorie | Opérateurs | Exemple |
|---|---|---|
| [[Opérateurs arithmétiques\|arithmétiques]] | `+ - * / %` | `7 / 2` vaut 3, `7 % 2` vaut 1 |
| [[Opérateur de comparaison\|comparaison]] | `== != < > <= >=` | `a == b` |
| [[Opérateur logique\|logiques]] | `&& \|\| !` | `x > 0 && x < 10` |
| [[Affectation\|affectation]] | `=` | `a = 3;` |
| [[Opérateur d'affectation composée\|affectation composée]] | `+= -= *= /= %=` | `a += 2;` (`a = a + 2;`) |
| [[Opérateur d'incrémentation\|incrémentation]] | `++ --` | `++i;` |
| flux | `<< >>` | `cout << x;` `cin >> x;` |

Leur ordre d'application suit des règles de priorité (`*` avant `+`, comparaisons avant `&&`) ; dans le doute, on met des parenthèses (voir [[Associativité et ordre d'évaluation]]). [[Complément hors du cours|ⓘ]]

**Comparaison de chaînes** : la comparaison est particulièrement utile, et montre un traitement réalisable par ordinateur.

```cpp
// Lit et compare deux noms
#include <iostream>
using namespace std;

int main()
{
    cout << "Donnez deux noms :\n";
    string premier;
    string second;
    cin >> premier >> second; // Lit deux chaînes

    if (premier == second) cout << "Les deux noms sont identiques.\n";
    if (premier < second)
        cout << premier << " est avant " << second << '\n';
    if (premier > second)
        cout << premier << " est après " << second << '\n';

    return 0;
}
```

Les [[Structure conditionnelle|instructions `if`]] sélectionnent des actions selon des conditions. Exécutions : `titi toto` → « titi est avant toto » ; `tata tata` → « Les deux noms sont identiques. » ; `toto Toto` → « toto est après Toto ».

**Q17.** Quelle est la définition d'« identique » ici ? Deux chaînes sont identiques si elles ont **la même longueur et exactement les mêmes caractères, dans le même ordre**, majuscules comprises : la comparaison est [[Sensibilité à la casse|sensible à la casse]]. `<` et `>` suivent l'[[Relation d'ordre|ordre lexicographique]] des codes de caractères : en [[Code ASCII|ASCII]], les majuscules (65 à 90) précèdent les minuscules (97 à 122), d'où « toto est après Toto ». [[Complément hors du cours|ⓘ]]

## Règles de codage

**Noms de variables.** Un nom de variable est un **nom** (surtout pas un verbe) suffisamment éloquent, complété au besoin par une caractéristique d'organisation ou d'usage, un qualificatif ou d'autres noms.

- **Convention** : il commence par une **minuscule**, et chaque nouveau mot commence par une **majuscule** : `distance`, `distanceMax`, `consigneCourante`, `etatBoutonGaucheSouris`, `nbreDEssais`. C'est la [[Casse chameau|casse chameau]] (*camelCase*).
- Abréviations admises si elles sont courantes : `nbre`, `max`, `min`…
- `i`, `j`, `k` seuls sont admis pour les indices de boucles.
- Un nom ne contient que des **lettres, des chiffres et le souligné** (`_`), et ne commence pas par un chiffre (voir [[Variable (programmation)|identificateur]]).
- Les noms qui commencent par un souligné suivi d'une majuscule (`_Valeur`), ou qui contiennent un double souligné (`__`), sont réservés à l'implémentation (compilateur et bibliothèque standard) ; ceux qui commencent par un souligné sont en outre réservés dans l'espace de noms global : le programmeur ne doit pas s'en servir. [[Erreurs du cours#^e-4-cours-complet|✎]]
- Ne pas distinguer deux identificateurs par la seule casse (`compteur` et `Compteur`), et les faire différer par au moins deux caractères. En C++, tous les caractères d'un identificateur sont significatifs (la norme recommande aux compilateurs d'en accepter au moins 1 024) : la limite aux premiers caractères ne valait que pour de très anciens compilateurs C (6 caractères significatifs pour les noms externes en C89). [[Erreurs du cours#^e-4-cours-complet|✎]]
- **Les [[Mot réservé|mots-clés]] du langage sont interdits comme noms.**

Le but des règles de codage est d'**augmenter la lisibilité** des programmes en se rapprochant d'expressions en langage naturel.

## Affectation et initialisation

L'**[[Affectation|opérateur d'affectation]]** `=` est le plus important à maîtriser : il attribue une nouvelle valeur à une variable. Il sert à deux opérations voisines mais intellectuellement distinctes :

- l'**[[Initialisation (programmation)|initialisation]]**, qui donne une valeur **initiale** à une variable, au moment de sa définition ;
- l'**affectation**, qui donne une **nouvelle** valeur à une variable qui existe déjà.

Exemple sur des entiers (figure du polycopié) :

| Instruction | Nature | `a` | `b` |
|---|---|---|---|
| `int a = 3;` | initialisation | 3 | |
| `a = 4;` | affectation | 4 | |
| `int b = a;` | initialisation par copie de `a` | 4 | 4 |
| `b = a + 5;` | affectation | 4 | 9 |
| `a = a + 7;` | affectation | 11 | 9 |

**Q18.** Compléter pour des chaînes. Réponse [[Complément hors du cours|ⓘ]] :

| Instruction | `a` | `b` |
|---|---|---|
| `string a = "alpha";` | `"alpha"` | |
| `a = "beta";` | `"beta"` | |
| `string b = a;` | `"beta"` | `"beta"` |
| `b = a + "gamma";` | `"beta"` | `"betagamma"` |
| `a = a + "delta";` | `"betadelta"` | `"betagamma"` |

`string b = a;` fait une **copie** : modifier `a` ensuite ne change pas `b`. [[Complément hors du cours|ⓘ]]

L'affectation est nécessaire dès qu'on fait quelque chose **plusieurs fois** avec une valeur différente : c'est le concept même de variable. Exemple, un **détecteur de mots répétés adjacents**, comme dans les vérificateurs de grammaire :

```cpp
// Détecte des mots répétés adjacents
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string motPrecedent = " ";      // signifiera "pas un mot" !
    string motCourant;
    while (cin >> motCourant)       // Lit un flux de mots
    {
        if (motPrecedent == motCourant) // Teste si le mot est le même que le précédent
            cout << "mot répété : " << motCourant << '\n';
        motPrecedent = motCourant;
    }
    return 0;
}
```

On lit un mot dans `motCourant`, on le compare à `motPrecedent`, on l'affiche s'ils sont identiques, puis on prépare le tour suivant en copiant `motCourant` dans `motPrecedent`. Pour le premier mot, il n'y a pas de mot précédent : on initialise `motPrecedent` à `" "` (un espace), valeur que `cin >>` ne peut jamais lire puisqu'il saute les espaces ; au premier tour, le test échoue, comme voulu. C'est une [[Valeur sentinelle|valeur sentinelle]].

Exécution : `toto et titi titi vont à la la plage avec titi` → « mot répété : titi », « mot répété : la ». La boucle `while (cin >> motCourant)` s'arrête quand la lecture échoue : sous Linux, **Ctrl-D** signale qu'il n'y a plus de saisie ([[Fin de fichier|fin de fichier]]). On peut aussi suspendre le programme avec Ctrl-Z ou l'interrompre avec Ctrl-C.

Ctrl-C envoie le [[Signal Unix|signal]] `SIGINT`, qui termine le programme ; Ctrl-Z envoie `SIGTSTP`, qui le **suspend** sans le terminer : il reste en mémoire, et `fg` le reprend (voir [[Commandes fg et bg]]). Ctrl-D n'est pas un signal : le terminal transmet une lecture vide, que le programme interprète comme la fin du flux. [[Complément hors du cours|ⓘ]]

**Conseil** : pour comprendre un programme, **« jouer à l'ordinateur »** : le suivre ligne par ligne en dessinant des boîtes sur papier pour les variables, et en changer les valeurs comme le dit le programme. Les programmeurs expérimentés le font. Un [[Débogueur|débogueur]] automatise cette exécution pas à pas. [[Complément hors du cours|ⓘ]]

**Q19.** Que signifie exactement « mots répétés » ? Deux suites de caractères **identiques** (casse comprise) lues **l'une juste après l'autre**, séparées seulement par des espaces blancs, éventuellement sur deux lignes. « titi » qui revient plus loin n'est pas compté, et « la » et « La » ne sont pas répétés ; une ponctuation collée (« la, la ») empêche aussi la détection. [[Complément hors du cours|ⓘ]]

**Q20.** Compter et afficher à la fin le nombre de mots répétés adjacents. Démarche imposée : a) un nom et un type pour le [[Compteur (programmation)|compteur]] ; b) sa valeur initiale ; c) sa définition ; d) l'endroit où la répétition est détectée ; e) l'incrémentation, en mettant des accolades (`{}`) si le `if` contient plusieurs instructions. L'affichage doit être grammaticalement correct : « Aucun mot répété adjacent dans cette suite », « un seul mot répété adjacent dans cette suite », « Il y a n mots répétés adjacents dans cette suite » (n > 1).

Pour incrémenter, on peut utiliser l'[[Opérateur d'incrémentation|opérateur d'incrémentation]] `++` ou l'addition :

```cpp
int a = 4;
++a;       // a vaut 5 (écriture conseillée)
a++;       // a vaut 6
a = a + 1; // a vaut 7
a += 1;    // a vaut 8
```

Seul, `++a` et `a++` ont le même effet ; ils diffèrent dans une expression : `b = ++a;` incrémente puis copie (pré-incrémentation), `b = a++;` copie l'ancienne valeur puis incrémente (post-incrémentation). `++a` est conseillé parce que, pour des objets comme les itérateurs, `a++` doit fabriquer une copie inutile. [[Complément hors du cours|ⓘ]]

Solution courte [[Complément hors du cours|ⓘ]] :

```cpp
string motPrecedent = " ";
string motCourant;
int nbreMotsRepetes = 0;               // a) b) c)
while (cin >> motCourant)
{
    if (motPrecedent == motCourant)    // d)
    {
        cout << "mot répété : " << motCourant << '\n';
        ++nbreMotsRepetes;             // e)
    }
    motPrecedent = motCourant;
}
if (nbreMotsRepetes == 0)
    cout << "Aucun mot répété adjacent dans cette suite\n";
else if (nbreMotsRepetes == 1)
    cout << "Un seul mot répété adjacent dans cette suite\n";
else
    cout << "Il y a " << nbreMotsRepetes << " mots répétés adjacents dans cette suite\n";
```

## Questions de révision (deuxième partie)

Réponses en complément.

21. **Qu'entend-on par « invite » ?**
    - Le message affiché pour demander à l'utilisateur une action ou une saisie (« Donnez votre âge : »). À ne pas confondre avec l'[[Invite de commande|invite du shell]]. [[Complément hors du cours|ⓘ]]
22. **Quel opérateur lit une valeur et la place dans une variable ?**
    - L'opérateur d'extraction `>>`, appliqué à `cin` : `cin >> x;`. [[Complément hors du cours|ⓘ]]
23. **Qu'est-ce qu'une variable ?**
    - Un objet nommé : une région de mémoire, dotée d'un type, qui contient une valeur et qu'on désigne par un nom. [[Complément hors du cours|ⓘ]]
24. **Différence entre `=` et `==` ?**
    - `=` affecte (ou initialise) une valeur ; `==` compare deux valeurs et donne un booléen. `if (x = 0)` est une erreur classique : il affecte 0 et le test est toujours faux (g++ `-Wall` avertit). [[Complément hors du cours|ⓘ]]
25. **Qu'est-ce qu'une définition ?**
    - Une instruction qui introduit un nouveau nom et réserve la mémoire correspondante (`int age = 0;`). [[Complément hors du cours|ⓘ]]
26. **Initialisation et affectation ?**
    - L'initialisation donne la première valeur, lors de la définition ; l'affectation remplace la valeur d'une variable qui existe déjà. Une constante peut être initialisée, jamais affectée. [[Complément hors du cours|ⓘ]]
27. **Qu'est-ce qu'une concaténation de chaînes ? Quel opérateur ?**
    - Mettre deux chaînes bout à bout (`"beta" + "gamma"` donne `"betagamma"` si l'un des deux est une `string`) ; l'opérateur est `+` (ou `+=`). [[Complément hors du cours|ⓘ]]
28. **Qu'est-ce qui termine l'entrée d'une chaîne ? d'un entier ?**
    - Une chaîne lue par `>>` se termine au premier espace blanc ; un entier, au premier caractère qui ne peut pas en faire partie (espace, lettre, point…). [[Complément hors du cours|ⓘ]]
29. **Bonnes règles pour nommer une variable ?**
    - Un nom (pas un verbe) éloquent, en casse chameau commençant par une minuscule, fait de lettres, chiffres et `_`, sans mot-clé ni `_` initial, et assez différent des autres noms. [[Complément hors du cours|ⓘ]]
30. **Qu'est-ce qu'une incrémentation ?**
    - Augmenter la valeur d'une variable, en général de 1 (`++i`, `i += 1`). [[Complément hors du cours|ⓘ]]

## Exercice 3 : calcul de notes

But : décomposer un problème simple en **itérations** successives.

- **Q31. Somme.** Lire une série de valeurs réelles tapées par l'utilisateur. La valeur **−1** signale la fin (c'est une [[Valeur sentinelle|marque de fin]], pas une vraie note). Additionner les notes, lues une à une dans `note`, dans un [[Accumulateur (programmation)|accumulateur]] initialisé à 0 (élément neutre de l'addition).
- **Q32. Compter** en même temps les valeurs, sans compter le −1.
- **Q33. Moyenne** : total divisé par le nombre de valeurs. Piège : si la note ou l'accumulateur est un `int`, la division est entière (quotient de la division euclidienne) ; il suffit qu'un opérande soit réel (choisir l'accumulateur), et dans ce cas la note devrait l'être aussi.
- **Q34. Contrôler les saisies** : n'accepter qu'une valeur entre 0 et 20 inclus, ou −1 ; sinon, redemander jusqu'à une saisie correcte ([[Validation des entrées]]).
- **Q35. Minimum et maximum** de la série, affichés à la fin (voir [[Recherche du minimum et du maximum]]).
- **Q36. Programme [[Robustesse (informatique)|robuste]]** : que se passe-t-il si on tape −1 tout de suite ? Un bon programme ne doit pas planter et doit prévoir ce cas.

Solution courte [[Complément hors du cours|ⓘ]] :

```cpp
#include <iostream>
using namespace std;

int main()
{
    const double FIN = -1.0;
    double note = 0.0;
    double accumulateur = 0.0;
    int nbreNotes = 0;
    double noteMin = 20.0, noteMax = 0.0;

    cout << "Note (-1 pour finir) : ";
    cin >> note;
    while (note != FIN)
    {
        if (note < 0.0 || note > 20.0)       // Q34 : saisie refusée, on redemande
        {
            cout << "Note invalide, recommencez : ";
        }
        else
        {
            accumulateur += note;            // Q31
            ++nbreNotes;                     // Q32
            if (note < noteMin) noteMin = note;   // Q35
            if (note > noteMax) noteMax = note;
            cout << "Note (-1 pour finir) : ";
        }
        cin >> note;
    }

    if (nbreNotes == 0)                      // Q36 : pas de division par zéro
        cout << "Aucune note saisie.\n";
    else
        cout << "Somme : " << accumulateur << ", " << nbreNotes << " notes, moyenne : "
             << accumulateur / nbreNotes      // Q33 : division réelle
             << ", min : " << noteMin << ", max : " << noteMax << endl;
    return 0;
}
```

Initialiser `noteMin` à 20 et `noteMax` à 0 (les bornes opposées de l'intervalle permis) garantit que la première note valide les remplace. Sans le test de Q36, `0.0 / 0` donne `nan` (*not a number*, norme IEEE 754) ; avec des entiers, une division par zéro serait un [[Comportement indéfini|comportement indéfini]], souvent un arrêt brutal. Comparer `note != FIN` entre réels est sûr ici parce que −1 est représentable exactement en binaire. Si l'utilisateur tape une lettre, `cin` passe en état d'échec et la boucle tourne sans fin : une version vraiment robuste teste `if (!(cin >> note))`. [[Complément hors du cours|ⓘ]]

## Bilan (deuxième partie)

Ces premiers programmes se sont construits **progressivement**, en modifiant un peu le code pour atteindre chaque nouvel objectif. Technique courante : devant un problème, chercher un problème similaire et adapter sa solution ; ne partir de zéro que si l'on y est obligé. Cette [[Réutilisation de code|réutilisation]] économise du temps, à condition que le programme d'origine soit proprement écrit : **clair, lisible, fonctionnel, robuste et documenté**.

Conclusion : **les types sont au centre des programmes corrects**, et plusieurs des meilleures techniques de construction reposent sur la conception et l'usage des types.

Rob Pike (ancien chercheur des [[Laboratoires Bell]], ingénieur chez [[Google]]), [[Règles de programmation de Pike|règle n° 5]] : « Les données prévalent sur le code. Si vous avez conçu la structure des données appropriée et bien organisé le tout, les algorithmes viendront d'eux-mêmes. La structure des données est le cœur de la programmation, et non pas les algorithmes. » Souvent résumée par « Écrivez du code stupide qui utilise des données futées ! » (voir [[Structure de données]], [[Algorithme]]).

# Troisième partie : programmation modulaire

Un programme ne fait jamais que **traiter des données** : il accepte des **entrées** et produit des **sorties**. *Figure* : entrées (clavier, souris, fichiers, base de données, réseau, autres périphériques, capteur, autres programmes) → traitement autour des **données** du programme, appelées ses structures de données ou son **état** (« beaucoup de code ») → sorties (écran, fichiers, base de données, réseau, autres périphériques, actionneur, autres programmes). Voir [[Opération d'entrée-sortie]].

Le travail du programmeur consiste surtout à exprimer un programme comme **un ensemble de parties qui coopèrent**, et à organiser le partage et l'échange de données entre elles. *Figure* : à l'intérieur du programme, plusieurs blocs « données + code » s'enchaînent, la sortie (E/S) de l'un étant l'entrée du suivant.

- Un **[[Traitement (informatique)|traitement]]** est l'action de produire des sorties à partir d'entrées.
- Les entrées d'une partie de programme s'appellent **arguments** (ou paramètres), ses sorties **résultats** (voir [[Argument et paramètre]]).
- Une **partie de programme** est par exemple une **fonction**, qui produit un résultat à partir d'arguments.

Exemple : produire le résultat 49 à partir de l'argument 7 avec une fonction `carre` (ou, dans l'autre sens, le résultat 7 à partir de 49 avec une fonction de [[Racine carrée|racine carrée]]). [[Erreurs du cours#^e-4-cours-complet|✎]]

## Objectifs et outils

Le métier de programmeur consiste à écrire des programmes qui, **dans cet ordre** :

1. donnent des **résultats corrects** (voir [[Correction d'un algorithme]]) ;
2. sont **simples** ;
3. sont **efficaces** (voir [[Complexité algorithmique]]).

Peu importe qu'un programme soit rapide si ses résultats sont faux ; un programme correct et efficace peut être si compliqué qu'il faudra le jeter ou le réécrire. Les programmes utiles sont toujours modifiés pour répondre à de nouveaux besoins (voir [[Maintenabilité]]). **Un programme (ou une fonction) doit s'acquitter de sa tâche aussi simplement que possible.**

En professionnel, on ne peut pas se contenter d'aligner du code jusqu'à ce qu'il ait l'air de marcher : il faut soigner sa **structure** ; paradoxalement, s'intéresser à la qualité du code est souvent le moyen le plus facile de faire fonctionner un programme. L'outil principal : **décomposer un gros traitement en parties plus petites**, jusqu'à obtenir des morceaux simples à comprendre et à résoudre (Descartes, [[Discours de la méthode]]). C'est la [[Décomposition fonctionnelle|décomposition fonctionnelle]], ou analyse descendante. [[Complément hors du cours|ⓘ]]

## Expressions et instructions

La brique de base d'un programme est l'**[[Expression (programmation)|expression]]**, qui calcule une valeur à partir d'**opérandes**. Une expression peut être une [[Valeur littérale|valeur littérale]] (`10`, `'a'`, `3.14`, `"rouge"`) ou le nom d'une variable.

*Figure* : dans `longueur = 40;`, `longueur` est une **lvalue** et `40` une **rvalue** (voir [[Lvalue et rvalue]]) :

- une **lvalue** (*left value*, valeur gauche) est un élément qui peut s'écrire **à gauche** de l'opérateur d'affectation `=` : elle doit désigner un emplacement de stockage en mémoire, d'un type précis, c'est-à-dire la référence à quelque chose de modifiable ;
- une **rvalue** (*right value*, valeur droite) est un élément qui peut s'écrire **à droite** de `=` : une valeur d'un type précis, sans forcément de zone de stockage en mémoire (une valeur, une constante, une variable, une expression…).

Précision : une lvalue désigne un objet qui a une adresse, mais pas forcément modifiable : une constante `const int n = 3;` est une lvalue non modifiable, qui ne peut pas être à gauche de `=`. Depuis C++11, la norme distingue plus finement *lvalue*, *xvalue* et *prvalue*, à cause de la sémantique de déplacement. [[Complément hors du cours|ⓘ]]

```cpp
// calcule une aire
int longueur = 40;
int largeur = 20;
int aire = longueur * largeur;
```

Il y a plusieurs sortes d'**[[Instruction (programmation)|instructions]]** : les déclarations, les instructions d'expression, les instructions conditionnelles, les instructions itératives (boucles)… Une **instruction d'expression** est une expression suivie d'un **point-virgule**, élément syntaxique qui permet au compilateur de « comprendre » le code, comme la ponctuation en français.

### Instructions conditionnelles : `if` et `switch`

Le C/C++ propose deux [[Structure conditionnelle|instructions conditionnelles]], `if` et `switch`. Un `if` choisit entre deux possibilités : si la condition est vraie, la première instruction (ou [[Bloc d'instructions|bloc]]) s'exécute, sinon la seconde.

```cpp
if (feuxPieton == vert) traverser();
else attendre();
```

Exemple : conversion cm/pouce (*inch*). Version 1 :

```cpp
int main()
{
    const double conversion = 2.54; // nombre de cm pour un pouce (inch)
    int longueur = 1;               // longueur (en cm ou en in)
    char unite = 0;                 // 'c' pour cm ou 'i' pour inch
    cout << "Donnez une longueur suivi de l'unité (c ou i):\n";
    cin >> longueur >> unite;

    if (unite == 'i')
        cout << longueur << " in == " << conversion*longueur << " cm\n";
    else
        cout << longueur << " cm == " << longueur/conversion << " in\n";
}
```

Ce programme ne fait que **sembler** fonctionner : tout ce qui n'est pas `'i'` est traité comme des cm, si bien qu'une unité `'f'` donne une conversion de cm en pouces que l'utilisateur ne voulait sans doute pas. **Un programme doit se comporter de manière sensée même si les utilisateurs ne le sont pas.** Version 2, avec un `if` imbriqué :

```cpp
    if (unite == 'i')
        cout << longueur << " in == " << conversion*longueur << " cm\n";
    else if (unite == 'c')
        cout << longueur << " cm == " << longueur/conversion << " in\n";
    else
        cout << "Désolé, je ne connais pas cette unité " << unite << endl;
```

On est alors tenté d'empiler un `if` par condition ; or le but est un code simple. Comparer une valeur à plusieurs **constantes** est la forme de sélection la plus courante, et le C/C++ fournit pour cela l'[[Structure conditionnelle|instruction `switch`]]. Version 3 :

```cpp
    switch (unite)
    {
      case 'i':
        cout << longueur << " in == " << conversion*longueur << " cm\n";
        break;
      case 'c':
        cout << longueur << " cm == " << longueur/conversion << " in\n";
        break;
      default:
        cout << "Désolé, je ne connais pas cette unité " << unite << endl;
        break;
    }
```

Le `switch` est toujours plus clair que des `if` imbriqués, surtout avec beaucoup de constantes. Ses particularités :

- la valeur testée doit être un entier, un `char` ou une [[Énumération (programmation)|énumération]] : pas de `string` ;
- les étiquettes des `case` doivent être des [[Expression constante|expressions constantes]], pas des variables ;
- une même valeur ne peut pas figurer dans deux `case` ;
- plusieurs `case` peuvent mener à la même instruction ;
- l'erreur la plus fréquente est l'**oubli d'un `break`** à la fin d'un `case` : comme il n'est pas obligatoire, le compilateur ne le détecte pas.

Sans `break`, l'exécution « tombe » dans le `case` suivant (*fall-through*) ; c'est ce qui permet d'écrire `case 'i': case 'I':` pour deux valeurs. Depuis GCC 7, l'option `-Wimplicit-fallthrough` (incluse dans `-Wextra`) signale les chutes non voulues, et C++17 permet de marquer les voulues par `[[fallthrough]];`. [[Complément hors du cours|ⓘ]]

Dans la version 1, `char unite = 0;` initialise le caractère au code 0 (le caractère nul), simple valeur « vide » de départ. Ces fonctions `main` sans `return` sont valides (voir la première partie). [[Complément hors du cours|ⓘ]]

### Instructions itératives : `while` et `for`

On fait rarement quelque chose une seule fois : tous les langages fournissent des moyens de répéter, c'est le **traitement itératif**, une [[Boucle (programmation)|boucle]] ou itération. Le C/C++ offre la boucle `while` (et sa variante `do … while`) et la boucle `for`.

Le polycopié présente le premier programme exécuté par l'[[EDSAC]], à Cambridge, le 6 mai 1949, écrit par David Wheeler : une table des carrés de 0 à 99 (`0 0`, `1 1`, `2 4`, … `99 9801`). Ce n'était pas le premier programme jamais exécuté sur un [[Architecture de von Neumann|ordinateur à programme enregistré]] : ce titre revient au [[Manchester Baby]], à l'université de Manchester, le 21 juin 1948 ; l'EDSAC, à l'[[Université de Cambridge]], fut le premier à offrir un service de calcul régulier. [[Erreurs du cours#^e-4-cours-complet|✎]]

En C++, ce programme ressemblerait à ceci :

```cpp
// Calcule et affiche le carré d'un nombre
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int i = 0; // commencer à 0

    // tant que i < 100 : on s'arrête quand i a atteint la valeur 100
    while (i < 100)
    {
        cout << i << '\t' << pow(i, 2) << '\n'; // i et son carré séparés par une tabulation
        ++i; // on incrémente et on recommence
    }
}
```

Les accolades délimitent le **corps de la boucle**, le bloc à répéter ; la condition de répétition est écrite dans le `while`. Écrire une boucle est simple, mais dangereux :

- si `i` n'était pas initialisé à 0, la boucle partirait d'une valeur quelconque : les [[Variable non initialisée|variables non initialisées]] sont une source d'erreurs courante ;
- sans `++i`, on obtient une **boucle infinie** (un programme qui ne répond plus). Il faut les éviter, et le polycopié déconseille d'écrire `while(1)` ou `while(true)`.

`pow` vient de l'en-tête `<cmath>` (voir [[Bibliothèque cmath]]) et renvoie un `double` ; pour un simple carré, `i * i` est plus simple et reste entier. [[Complément hors du cours|ⓘ]]

Itérer sur une suite de nombres est si courant qu'il existe l'instruction **`for`** : très semblable à `while`, mais elle concentre sur une seule ligne la gestion de la **variable de contrôle** : une zone d'**initialisation**, une zone de **condition** et une zone d'**incrémentation**. Il existe toujours un `while` équivalent à un `for` ; **n'utiliser `while` que lorsque ce n'est pas le cas** (pas de variable de contrôle simple).

```cpp
// avec i commençant à 0 (initialisation), tant que i < 100 (condition),
// en incrémentant i après chaque exécution du bloc (incrémentation)
for (int i = 0; i < 100; i++)
    cout << i << '\t' << pow(i, 2) << '\n';
```

Équivalences : `for (init; cond; incr) corps;` se comporte comme `{ init; while (cond) { corps; incr; } }`. La boucle `do { … } while (cond);` exécute son corps **au moins une fois** avant de tester : c'est la forme naturelle d'une saisie à recommencer tant qu'elle est invalide. Depuis C++11, la boucle « pour chaque » parcourt un conteneur : `for (int x : v)`. [[Complément hors du cours|ⓘ]]

## Constantes

Les programmes utilisent beaucoup de [[Constante (programmation)|constantes]], importantes pour garder un code lisible. Le C++ offre la **constante symbolique** : un objet nommé qui ne peut plus recevoir de nouvelle valeur une fois initialisé.

```cpp
const double pi = 3.14159;
pi = 22/7;                 // Erreur : affectation d'une constante
const double v = 7*pi/r;   // Ok : on ne fait que lire la constante pi
```

- **Règle de codage** : éviter les valeurs littérales dans le code et utiliser autant que possible des constantes aux noms significatifs. Les littéraux semés dans le code (hors définitions `const`) sont appelés par dérision **constantes magiques** (voir [[Nombre magique (programmation)]]).
- On peut aussi créer une constante avec la directive du préprocesseur `#define PI 3.14159` (voir [[Macro (préprocesseur)]]). C'est une simple **substitution de texte** (un copier-coller) faite avant la compilation, **sans aucun typage**. `#define` améliore surtout la lisibilité ; par convention, ces noms s'écrivent en **MAJUSCULES**.

En C++, on préfère `const` (ou `constexpr`, C++11, pour une valeur calculée à la compilation) à `#define` : la constante a un type vérifié, une portée, et apparaît dans le débogueur. Une macro mal parenthésée donne des surprises : avec `#define CARRE(x) x*x`, `CARRE(1+2)` vaut `1+2*1+2`, soit 5. Depuis C++20, `<numbers>` fournit `std::numbers::pi`. [[Complément hors du cours|ⓘ]]

À noter : `22/7` est une division entière, qui vaut 3 et non 3,142… ; il faudrait `22.0/7`. [[Complément hors du cours|ⓘ]]

## Références et pointeurs

### Pointeurs

Les **[[Pointeur et adresse mémoire|pointeurs]]** sont des variables spéciales qui stockent une **adresse**, en général l'emplacement mémoire d'une variable (ou d'une autre adresse). Comme la variable pointée a un type, le pointeur doit être du type correspondant pour la manipuler convenablement.

*Figure* : `i` (type `int`, adresse `&i` = `0xbfbec7a8`) contient 2, puis 3 ; `ptrInt` (type `int*`, à l'adresse `0xbfbec7ac`) contient la valeur `0xbfbec7a8`, l'adresse de `i` ; `*ptrInt = 3;` modifie le contenu de `i` par indirection.

```cpp
int *ptrInt;   // l'étoile (*) définit un pointeur : ptrInt pointe sur un int

int i = 2;
ptrInt = &i;   // & devant une variable donne son adresse : ptrInt reçoit l'adresse de i

*ptrInt = 3;   // * devant le pointeur accède à la variable pointée (indirection)
               // i contient maintenant 3
```

Voir [[Opérateur d'adresse]] (`&`) et [[Déréférencement]] (`*`).

- Les pointeurs peuvent être incrémentés, décrémentés, additionnés ou soustraits ; leur nouvelle adresse dépend du type pointé, ce qui sert par exemple à passer à la variable suivante du même type en mémoire (voir [[Arithmétique des pointeurs]]).
- **Règle de codage** : on peut préfixer les pointeurs par `ptr`.
- Les pointeurs sont délicats : mal utilisés, ils provoquent des erreurs d'accès mémoire ([[Erreur de segmentation]]). Certains langages, comme [[Langage Java|Java]], les ont interdits.

Un pointeur non initialisé contient une adresse quelconque ; on initialise donc un pointeur qui ne pointe sur rien à `nullptr` (C++11), plutôt qu'à `NULL` ou `0` comme en C++98 (voir [[Pointeur NULL]]). Java n'a pas de pointeurs manipulables, mais ses variables d'objets sont des références gérées par la machine virtuelle, sans arithmétique. [[Complément hors du cours|ⓘ]]

### Références

En C++ (pas en C), une **[[Référence (C++)|référence]]** est un nouveau nom, **synonyme** d'une variable définie ailleurs (un alias, un raccourci) : modifier la référence modifie la variable. Une référence est initialisée **une seule fois** et désigne la même variable toute sa durée de vie.

```cpp
int i = 2;     // i est un entier valant 2
int &j = i;    // & devant le nom : j est une référence sur un entier, et cet entier est i

//&j = x;      // Erreur : illégal (on ne peut pas faire désigner une autre variable à une référence déjà initialisée)
//int &k = 44; // Erreur : illégal (on ne peut pas créer une référence sur une valeur)

j = j + 1;     // équivaut à i = i + 1 : i contient maintenant 3
```

*Figure* : une seule boîte, d'adresse `&i`, porte deux noms, `i` et `j` ; `j = j + 1;` change sa valeur de 2 en 3.

Les références sont très utilisées en C++, notamment pour **passer les arguments d'une fonction** ; le mot-clé `const` interdit alors à la fonction de modifier (accidentellement) la variable passée.

Précision : `int &k = 44;` est refusé parce qu'une référence non constante doit désigner une lvalue ; une **référence constante** peut en revanche se lier à une valeur temporaire : `const int &k = 44;` est valide. Une référence n'est jamais nulle et n'a pas d'arithmétique, contrairement à un pointeur. [[Complément hors du cours|ⓘ]]

## Fonctions

Dans le programme des carrés, `pow(i, 2)` est un **[[Appel de fonction|appel de fonction]]** : un appel à la fonction `pow` avec les **arguments** `i` et `2`, qui retourne le **résultat** `i` élevé à la puissance 2.

*Figure* : entrées `i` et `2` (arguments) → fonction `pow` → sortie `i²` (résultat, valeur de retour). Sa **déclaration** est dans un fichier d'en-tête : `double pow(double x, double y);` ; sa **définition** est dans une bibliothèque (`libm.so` sous Linux, cf. édition de liens) ; sa **documentation** s'obtient par `man pow` sous Linux (voir [[Commande man]]).

La bibliothèque standard fournit beaucoup de fonctions utiles comme `pow()`, mais on en écrit beaucoup soi-même. Définition plausible d'une fonction `carre` :

```cpp
#include <iostream>
using namespace std;

int carre(int x)
{
    return x*x;
}

int main()
{
    for (int i = 0; i < 100; i++)
        cout << i << '\t' << carre(i) << '\n';
    return 0;
}
```

**Déclaration et définition** (figures du polycopié ; voir [[Déclaration et définition]]) :

- La **déclaration** d'une fonction est une instruction qui donne au compilateur des informations sur la fonction : ici, qu'une fonction nommée `carre` existe, qu'elle reçoit un `int` et retourne un `int`. La forme recommandée est le **prototype**, qui comprend la **signature** et le **type de retour** : `int carre(int);`.
  - **type de retour** : `int` ; si la fonction ne retourne rien, on écrit `void` (« rien ») ;
  - **nom de la fonction** : `carre` ;
  - **liste de paramètres** : leurs types ; leur nom est facultatif dans une déclaration ; la liste peut être vide `()`.
- La **définition** d'une fonction écrit son **corps**, les traitements entre accolades ; les paramètres y sont **nommés** comme des variables : `int carre(int x) { return x*x; }`.
- La définition tient lieu de déclaration, mais une fonction doit être **connue avant son appel**. En C++, appeler une fonction ni déclarée ni définie plus haut est une **erreur de compilation** (`'carre' was not declared in this scope`) : il faut placer sa définition, ou au moins son prototype, avant l'appel. La [[Déclaration implicite de fonction|déclaration implicite]] avec simple avertissement n'existait qu'en C ancien (C89), et a été retirée du C en C99. [[Erreurs du cours#^e-4-cours-complet|✎]]
- Une fonction qui ne retourne pas de résultat (`void`) s'appelle une **procédure** (voir [[Fonction et procédure]]).

La **signature**, au sens strict de la norme, comprend le nom et la liste des types des paramètres, mais **pas** le type de retour : c'est elle qui distingue deux fonctions surchargées (`int carre(int)` et `double carre(double)` peuvent coexister). [[Complément hors du cours|ⓘ]]

**L'appel** doit correspondre à la déclaration, que le compilateur vérifie : on n'est pas obligé d'utiliser le résultat, mais on doit donner exactement les arguments exigés.

```cpp
carre(2);               // Probablement une erreur : la valeur de retour n'est pas utilisée
int c1 = carre();       // Erreur : argument manquant
int c2 = carre;         // Erreur : parenthèses manquantes
int c3 = carre(1, 2);   // Erreur : trop d'arguments
int c4 = carre("deux"); // Erreur : mauvais type d'argument (int attendu)
int c5 = carre(2);      // Ok : enfin !
```

`carre(2);` compile (c'est une erreur de logique, pas de syntaxe) ; depuis C++17, l'attribut `[[nodiscard]]` sur une fonction fait avertir le compilateur quand on ignore son résultat. [[Complément hors du cours|ⓘ]]

**Pourquoi définir une fonction** ? Pour un traitement distinct et nommé, parce que cela :

- rend le traitement distinct du point de vue logique ;
- rend le programme plus clair et plus lisible ;
- permet de l'utiliser à plusieurs endroits, chaque fois qu'on en a besoin ;
- facilite les tests : on simule des entrées et on compare le résultat obtenu au résultat attendu (voir [[Test unitaire]]).

Les programmes sont plus faciles à écrire, comprendre et maintenir quand **chaque fonction réalise une SEULE action logique**, celle qui correspond à son nom (voir [[Principe de responsabilité unique]]).

**Règle de codage** : **pas de saisie ni d'affichage dans les fonctions**, pour pouvoir les réutiliser ; une fonction se concentre sur le traitement. Mauvais exemple :

```cpp
void saisirUnNombreEtAfficherSonCarre()
{
    int x;
    cout << "Donnez un nombre : ";
    cin >> x;
    cout << "Le carré de ce nombre est " << x*x;
}
```

Les fonctions qui ne reçoivent aucune entrée et ne produisent aucun résultat sont intellectuellement suspectes (des « trous noirs » de code) : à éviter. Bon exemple : `carre` ne fait que le calcul, et `main` s'occupe de la saisie et de l'affichage :

```cpp
int carre(int x)
{
    return x*x;
}

int main()
{
    int x;
    cout << "Donnez un nombre : ";
    cin >> x;
    cout << "Le carré de ce nombre est " << carre(x);
    return 0;
}
```

Une fonction sans entrée ni sortie n'agit que par [[Effet de bord|effets de bord]] (variables globales, affichage), ce qui la rend difficile à tester et à réutiliser. [[Complément hors du cours|ⓘ]]

**[[Passage par valeur|Passage par valeur]]** (figure) : au 1ᵉʳ appel, `int xx = 2; carre(xx);` **copie la valeur** de l'argument `xx` (2) dans le paramètre `x` de `carre`, qui retourne le résultat 4 ; au 2ᵉ appel, `int yy = 3; carre(yy);` copie 3 dans `x` et retourne 9. La fonction travaille sur une copie : modifier `x` ne changerait pas `xx`. [[Erreurs du cours#^e-4-cours-complet|✎]]

On peut aussi passer les arguments **par référence** ou **par pointeur** (exercices 5 et 6).

La copie est faite dans le cadre d'appel de la fonction, sur la [[Pile d'exécution|pile d'exécution]], et disparaît au retour. Passer par valeur convient aux petits types (`int`, `double`) ; pour un gros objet (`string`, `vector`), on passe une référence constante (`const string& s`) pour éviter la copie (voir [[Passage de paramètres]]). [[Complément hors du cours|ⓘ]]

## Règles de codage (fonctions)

- Un **nom de fonction** est construit autour d'un **verbe** (pas d'un nom), complété au besoin par une **quantité**, un **complément d'objet** ou un **adjectif représentatif d'un état**. Le verbe est au présent de l'indicatif ou à l'infinitif ; l'adjectif d'état sert surtout aux fonctions booléennes ; la quantité enrichit le complément.
- **Convention** : minuscule initiale, puis majuscule à chaque nouveau mot ([[Casse chameau|casse chameau]]) ; un nom de fonction pourra commencer par une majuscule dans des cas précisés plus tard.
- Exemples : `void ajouter()`, `void sauverValeur()`, `estPresent()`, `estVide()`, `viderAMoitieLeReservoir()`.
- Les mots-clés sont interdits comme noms.
- Les **noms des paramètres** suivent les règles des noms de variables (minuscule initiale).
- **Ordre des paramètres** : `nomFonction(parametrePrincipal, listeParametres)`, la donnée principale d'abord, puis les données secondaires nécessaires au traitement. Exemple : `ajouter(EnsembleMesures mesures, float uneMesure)` ajoute une mesure à un ensemble de mesures (la donnée principale), et non l'inverse.
- **Taille** : pour décomposer les gros traitements (Descartes encore), on limite les fonctions à **10 à 15 lignes au maximum**.

## Questions de révision (troisième partie)

Réponses en complément.

37. **Qu'est-ce qu'un traitement ?**
    - L'action de produire des sorties à partir d'entrées. [[Complément hors du cours|ⓘ]]
38. **Entrées et sorties d'un traitement ? Exemples.**
    - Les entrées sont les données reçues (arguments d'une fonction, saisie clavier, fichier lu, capteur) ; les sorties sont les résultats produits (valeur de retour, affichage, fichier écrit, actionneur). Pour `carre`, l'entrée 7 donne la sortie 49. [[Complément hors du cours|ⓘ]]
39. **Les trois exigences d'un programmeur ?**
    - Des résultats corrects, un code simple, un programme efficace, dans cet ordre de priorité. [[Complément hors du cours|ⓘ]]
40. **Qu'est-ce qu'une lvalue ?**
    - Une expression qui désigne un emplacement en mémoire (une variable), et peut donc se trouver à gauche d'une affectation si elle est modifiable. [[Complément hors du cours|ⓘ]]
41. **Qu'est-ce qu'une constante symbolique et pourquoi l'utiliser ?**
    - Un objet nommé, déclaré `const`, dont la valeur ne peut plus changer après l'initialisation ; on l'utilise pour remplacer les constantes magiques par un nom qui explique la valeur, et pour la modifier en un seul endroit. [[Complément hors du cours|ⓘ]]
42. **Quand préférer `switch` à `if` ?**
    - Quand on compare une même valeur entière (ou `char`, ou énumération) à plusieurs constantes. [[Complément hors du cours|ⓘ]]
43. **Rôle et ordre d'exécution des parties de l'en-tête d'un `for` ?**
    - L'initialisation s'exécute une fois au début ; puis, à chaque tour, la condition est testée (si elle est fausse, la boucle s'arrête), le corps s'exécute, puis l'incrémentation. [[Complément hors du cours|ⓘ]]
44. **Quand utiliser `for`, quand `while` ?**
    - `for` quand une variable de contrôle a une initialisation, une condition et une incrémentation simples (parcourir 0 à n−1) ; `while` quand le nombre de tours dépend d'un événement (fin de saisie, valeur sentinelle). [[Complément hors du cours|ⓘ]]
45. **Différence entre déclaration et définition de fonction ?**
    - La déclaration (prototype, terminé par `;`) annonce le nom, les types des paramètres et le type de retour ; la définition fournit en plus le corps. On peut déclarer une fonction plusieurs fois, mais la définir une seule fois (règle de la définition unique). [[Complément hors du cours|ⓘ]]
46. **Que signifie `char foo(int x, int y)` dans une définition ?**
    - C'est l'en-tête de la définition d'une fonction `foo`, qui prend deux paramètres entiers `x` et `y` (passés par valeur) et retourne un `char` ; le corps entre accolades suit. [[Complément hors du cours|ⓘ]]

## Exercice 4 : programmation modulaire

Éditer, étudier, fabriquer et tester `somme1-100.cpp` :

```cpp
#include <iostream> // Inclusion des déclarations de cout, endl, etc.

using namespace std;

//-------------------------------------------------//
// somme1-100.cpp                                  //
// Calcul de la somme des entiers de 1 à 100       //
//-------------------------------------------------//
int main ()
{
    unsigned int i=0U;            // variable de contrôle, valeur initiale : zéro.
    unsigned int accumulateur=0U; // la somme des entiers, initialement zéro.

    // calcul : utilise un traitement itératif : la boucle
    // while est l'une des instructions possibles en C/C++
    while (i <= 100U)
    {
        accumulateur = accumulateur + i;
        i = i + 1; // Avec un peu d'habitude, on écrira plutôt ++i
    }

    // affichage du résultat
    cout << "La somme des entiers de 1 a 100 est " << accumulateur << endl;

    return 0;
} // fin du main()
```

Le programme affiche 5050, la [[Somme des premiers entiers|somme des 100 premiers entiers]], n(n+1)/2. `unsigned int` est un [[Type entier|entier non signé]] (jamais négatif) et le suffixe `U` fait de `0U` et `100U` des littéraux non signés. [[Complément hors du cours|ⓘ]]

- **Q47.** Remplacer `100` par une constante `MAXIMUM`, définie avant le début du programme ; les programmeurs C/C++ nomment les constantes en majuscules.
- **Q48.** Remplacer la constante par une variable `maximum` (en minuscules, puisque ce n'est plus une constante), demandée à l'utilisateur avant le calcul.
- **Q49.** Déplacer le calcul (et lui seul) dans une fonction `unsigned int somme1aN(unsigned int n)`, définie au-dessus de `main()`, qui renvoie la somme de 1 à n. **Aucun `cin` ni `cout` dans la fonction** ; `main()` l'appelle et affiche le résultat.
- **Q50.** Rendre le programme **modulaire** : déplacer `somme1aN` dans `somme.cpp`, créer `somme.h` qui contient sa déclaration, inclure `somme.h` dans le fichier de `main()`. [[Compilation séparée|Compiler séparément]] chaque `.cpp` en `.o`, puis lier tous les `.o` en un exécutable.
- **Q51.** Sur le modèle de `somme1aN`, écrire `unsigned int factorielle(unsigned int n)`. Rappel : `somme1aN(n) = 0 + 0 + 1 + 2 + … + n` et `factorielle(n) = 1 * 1 * 2 * 3 * … * n`, où le premier terme (souligné dans le polycopié) est la **valeur initiale de l'accumulateur** et chaque terme suivant un tour de boucle. n peut valoir 0 : la boucle peut ne faire aucun tour.
- **Q52.** Dans `main.cpp`, une boucle `for` appelle `factorielle()` pour toutes les valeurs de 1 au nombre choisi et affiche chaque résultat. Que se passe-t-il quand n dépasse 20 ? Pourquoi ?

Solution courte (Q47 à Q51) [[Complément hors du cours|ⓘ]] :

```cpp
// somme.h
#ifndef SOMME_H
#define SOMME_H
unsigned int somme1aN(unsigned int n);
unsigned int factorielle(unsigned int n);
#endif
```

```cpp
// somme.cpp
#include "somme.h"

unsigned int somme1aN(unsigned int n)
{
    unsigned int accumulateur = 0U;
    for (unsigned int i = 1U; i <= n; ++i)
        accumulateur += i;
    return accumulateur;
}

unsigned int factorielle(unsigned int n)
{
    unsigned int accumulateur = 1U;    // 0! = 1 : aucun tour de boucle si n = 0
    for (unsigned int i = 2U; i <= n; ++i)
        accumulateur *= i;
    return accumulateur;
}
```

```cpp
// main.cpp
#include <iostream>
#include "somme.h"
using namespace std;

int main()
{
    unsigned int maximum = 0U;
    cout << "Valeur maximale : ";
    cin >> maximum;
    cout << "Somme de 1 a " << maximum << " : " << somme1aN(maximum) << endl;
    for (unsigned int n = 1U; n <= maximum; ++n)
        cout << n << "! = " << factorielle(n) << endl;
    return 0;
}
```

```bash
g++ -Wall -c somme.cpp          # → somme.o
g++ -Wall -c main.cpp           # → main.o
g++ -Wall -o main main.o somme.o
./main
```

Pour Q47, on écrit `const unsigned int MAXIMUM = 100U;` avant `main` (ou `#define MAXIMUM 100U`). Les lignes `#ifndef`/`#define`/`#endif` de `somme.h` sont une [[Garde d'inclusion|garde d'inclusion]], qui empêche une double inclusion ; le polycopié ne les demande pas. Les guillemets de `#include "somme.h"` font chercher le fichier d'abord dans le répertoire du projet, les chevrons dans les répertoires du système. [[Complément hors du cours|ⓘ]]

Réponse à Q52 : la [[Factorielle|factorielle]] croît très vite et dépasse la capacité du type : c'est un [[Dépassement d'entier|dépassement d'entier]]. Pour un entier non signé, le calcul se fait **modulo 2ⁿ** (n = nombre de bits) : le résultat est faux, sans message d'erreur. Avec un `unsigned int` de 32 bits (maximum 4 294 967 295), les résultats sont faux **dès n = 13** (13! = 6 227 020 800) ; la limite de 20 correspond à un entier de 64 bits (`unsigned long long`, maximum ≈ 1,8 × 10¹⁹ : 20! ≈ 2,43 × 10¹⁸ tient, 21! ≈ 5,1 × 10¹⁹ non). Pour un entier **signé**, le dépassement est un [[Comportement indéfini|comportement indéfini]]. [[Complément hors du cours|ⓘ]]

**Automatiser la fabrication avec `make`.** Les étapes de fabrication s'automatisent avec l'outil [[Make (logiciel)|make]], en écrivant les règles dans un fichier `Makefile` :

```makefile
main: main.o somme.o
	g++ -o main main.o somme.o
main.o: main.cpp somme.h
	g++ -c main.cpp
somme.o: somme.cpp somme.h
	g++ -c somme.cpp
```

Attention : une **tabulation**, et non des espaces, doit précéder les lignes de commande `g++`.

**Q53.** Modifier tour à tour `main.cpp`, `somme.h` et `somme.cpp`, et lancer `make` chaque fois. Intérêt de `make` ? Chaque règle se lit « cible : dépendances », puis la commande qui fabrique la cible. `make` compare les dates de modification et **ne refait que ce qui est nécessaire** : modifier `somme.cpp` recompile seulement `somme.o` puis refait l'édition de liens ; modifier `somme.h` recompile les deux `.o`, qui en dépendent. Sur un gros projet modulaire, on gagne beaucoup de temps et on n'oublie aucune étape. [[Complément hors du cours|ⓘ]]

## Exercice 5 : passage par adresse

Dans `main()`, trois réels simple précision (`float`) `a`, `b`, `c` reçoivent des valeurs arbitraires (par exemple `a = 11.5`, `b = -2.1`, `c = 0.0`). On veut une fonction `ordonne3()` qui manipule ces trois variables passées en paramètres et garantit qu'après l'appel **a ≤ b ≤ c**, en permutant leurs valeurs si nécessaire.

- **Q54.** Écrire d'abord `echange2ParAdresse()`, qui ordonne seulement deux paramètres, et la tester sur deux variables du `main()`.
- **Q55.** Écrire `ordonne3()` par des appels à `echange2ParAdresse()`. Combien d'appels faut-il au minimum pour être sûr du résultat ?
- Les affichages se font **uniquement dans `main()`**, jamais dans `echange2ParAdresse()` ni `ordonne3()`.

Solution courte [[Complément hors du cours|ⓘ]] :

```cpp
// Ordonne *x et *y pour que *x <= *y
void echange2ParAdresse(float *x, float *y)
{
    if (*x > *y)
    {
        float temp = *x;
        *x = *y;
        *y = temp;
    }
}

void ordonne3(float *a, float *b, float *c)
{
    echange2ParAdresse(a, b);   // a <= b
    echange2ParAdresse(b, c);   // c est maintenant le plus grand
    echange2ParAdresse(a, b);   // a <= b <= c
}

// dans main() : float a = 11.5f, b = -2.1f, c = 0.0f;
//               ordonne3(&a, &b, &c);   // a = -2.1, b = 0, c = 11.5
```

Il faut **trois appels** au minimum : le deuxième amène le maximum en `c`, le troisième ordonne les deux restants. La fonction reçoit les **adresses** des variables (`&a`) et les modifie par [[Déréférencement|déréférencement]] (`*x`) : c'est le [[Pointeur et adresse mémoire|passage par adresse]], seul moyen en C de modifier les variables de l'appelant. L'échange utilise une variable temporaire (voir [[Échange de deux variables]]). [[Complément hors du cours|ⓘ]]

## Exercice 6 : passage par référence

**Q56.** Même question qu'à l'exercice 5, mais avec des **passages par référence** au lieu des passages par adresse. Quelle solution paraît la plus simple ? Peut-on utiliser des références en C ? [[Erreurs du cours#^e-4-cours-complet|✎]]

Solution courte [[Complément hors du cours|ⓘ]] :

```cpp
void echange2ParReference(float &x, float &y)
{
    if (x > y)
    {
        float temp = x;
        x = y;
        y = temp;
    }
}

void ordonne3(float &a, float &b, float &c)
{
    echange2ParReference(a, b);
    echange2ParReference(b, c);
    echange2ParReference(a, b);
}

// dans main() : ordonne3(a, b, c);   // ni & à l'appel, ni * dans la fonction
```

La version par [[Référence (C++)|référence]] est plus simple : ni `&` à l'appel, ni `*` dans la fonction, et aucun risque de pointeur nul. **Les références n'existent pas en C** : en C, on passe par adresse. La bibliothèque standard fournit d'ailleurs `std::swap(x, y)` (en-tête `<utility>`), qui échange deux variables par référence. [[Complément hors du cours|ⓘ]]

## Bilan (troisième partie)

En théorie, on peut désormais faire tout ce qu'on peut faire avec un ordinateur, « le reste n'est que détails » ; mais ces détails et les compétences pratiques comptent, car la carrière de programmeur ne fait que commencer. Il reste à apprendre à écrire de **bons programmes : corrects, simples et efficaces**.

Avec des variables, des conditions et des boucles, on peut en effet écrire tout ce qui est [[Calculabilité|calculable]] : c'est le [[Théorème de Böhm-Jacopini|théorème de Böhm-Jacopini]] (1966), selon lequel séquence, sélection et itération suffisent à exprimer tout [[Algorithme|algorithme]]. [[Complément hors du cours|ⓘ]]

Rob Pike, [[Règles de programmation de Pike|règle n° 4]] : « Les algorithmes élégants comportent plus d'erreurs que ceux qui sont plus simples, et ils sont plus difficiles à appliquer. Utilisez des algorithmes simples ainsi que des structures de données simples. » C'est une application du [[Principe KISS|principe KISS]] (*Keep It Simple, Stupid*, « ne complique pas les choses ») : rechercher la simplicité dans la conception et éviter toute complexité non nécessaire.

## Ce que le C++ moderne change à ce polycopié

Récapitulatif des évolutions depuis 2012, pour écrire aujourd'hui le même code [[Complément hors du cours|ⓘ]] :

| Polycopié (C++98) | Aujourd'hui (C++11 et suivants) |
|---|---|
| `int n = 0;` | aussi `int n{0};` ou `int n{};` ([[Initialisation (programmation)\|initialisation par accolades]], refuse les conversions avec perte) |
| type écrit en entier | [[Mot-clé auto\|`auto`]] quand le type est évident : `auto total = 0.0;` |
| `NULL` ou `0` pour un pointeur vide | `nullptr` ([[Pointeur NULL]]) |
| tableaux C `int t[10];` | [[Classe vector (C++)\|`std::vector<int>`]] (taille variable) ou `std::array<int, 10>` |
| `#define PI 3.14159` | `constexpr double pi = 3.14159;` ou `std::numbers::pi` (C++20) |
| `using namespace std;` partout | `std::` explicite, jamais de `using namespace` dans un en-tête |
| `for (int i = 0; i < n; i++)` sur un conteneur | `for (auto x : v)` (boucle « pour chaque ») |
| www.cplusplus.com | [[Cppreference\|cppreference.com]] |
| g++ en C++98 par défaut | g++ en C++17 par défaut depuis GCC 11 ; `-std=c++20` pour C++20 |
