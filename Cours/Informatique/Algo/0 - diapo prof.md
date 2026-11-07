---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-07
complet: true
---

Résumé du recueil AlgoID1 (PDF) ([[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]) (163 pages, CY Tech, pré-ING 1re année), dans [[Cours/Informatique/Algo/_index|Algo]]. Plusieurs supports sont collés bout à bout : cours d'introduction, éléments de base en pseudo-code (avec TD), fonctions et procédures, fonctions en Python, introduction à Python (en anglais), types structurés, récursivité, puis les TD de récursivité et d'enregistrements. Notions déjà dans le wiki : [[Récursivité]], [[Tours de Hanoï]], [[Structure (struct)]], [[Portée d'une variable]], [[Pile et file]], [[Récurrence]], et le document [[Raw/Year 1/Algo Maths/Python.docx|Python]].

Limite de lecture : le texte est extrait en entier ; les diapositives où le code Python est une image ont été lues sur l'image et recopiées en blocs de code. Les schémas (organigrammes, appels, carte, tours de Hanoï) sont intégrés en pages entières. Les exercices ne sont **pas corrigés** dans le document, sauf ceux dont la solution suit sur la diapositive d'après (signalé à chaque fois).

## 1. Introduction à l'algorithmique (« Concepts fondamentaux »)

### Objectifs et évaluation

- S'initier aux fondements de l'algorithmique procédurale ; se familiariser avec la programmation (en C).
- « Tout le monde doit et va programmer » ; « C'est en forgeant qu'on devient forgeron » ; « Nous sommes ce que nous faisons de manière répétée. L'excellence n'est pas une action mais une habitude » (Aristote).
- Évaluation : DS papier ou machine, projets.

### Algorithmique et programmation

- **Algorithmique** : le mot vient du nom d'un mathématicien persan, Al-Khowarizmi (le cours dit « du VIIe siècle ») ; c'est concevoir une solution (un algorithme) pour un problème donné.
- **Programmation** : dire à un ordinateur ce qu'il doit faire (« This machine has no brain. Use your own ») ; écrire un algorithme dans un langage compréhensible par la machine.
- L'informatique a progressé (matériel : miniaturisation, performances, coûts, ubiquité ; logiciel : facilité d'utilisation), mais le concept de base reste le **calcul** : suite de transformations effectuées automatiquement à l'aide d'un nombre fini de règles préétablies, sur des données symboliques (nombres, expressions mathématiques, données de toutes sortes).

### Définition d'un algorithme

[[Algorithme]] : « procédure de calcul bien définie qui prend en entrée une [ou plusieurs] valeurs, et qui donne en sortie une [ou plusieurs] valeurs » (Cormen et al.). Autrement dit, une séquence d'instructions qui transforment l'entrée en sortie. Un **problème** spécifie une relation entre l'entrée et la sortie ; un algorithme est conçu pour résoudre un problème.

### Spécifier un algorithme

| Moyen | Usage |
|---|---|
| Langage humain | « dégrossir » le problème |
| [[Pseudo-code]] sur papier | le spécifier plus formellement, pour le traduire ensuite sur ordinateur |
| Langage informatique | le résoudre concrètement via une machine |

Dans tous les cas, la spécification doit décrire précisément la procédure de calcul. Plusieurs solutions sont souvent possibles, et il n'est pas facile de savoir laquelle convient le mieux.

### Exemples

- **Gâteau aux pommes** (capture d'une recette) : ingrédients (120 g de sucre semoule, 1 paquet de sucre vanillé, 3 œufs, 0,5 paquet de levure chimique, 125 g de farine, 0,5 verre d'huile de colza, 3 pommes), temps total 57 min (préparation 12 min, cuisson 45 min), puis six étapes : 1. découper les pommes en petits cubes ; 2. préchauffer le four à 160 °C ; 3. mélanger les ingrédients de la pâte, ajouter les pommes ; 4. mélanger à la spatule ; 5. verser dans un moule beurré et cuire 40 à 50 min ; 6. déguster. Une recette est un algorithme : des entrées, des étapes ordonnées, une sortie.
- **[[Problème du passeur]]** : un passeur doit faire traverser une rivière à un loup, une chèvre et un chou ; il ne peut transporter qu'une chose à la fois ; le loup et la chèvre ne doivent pas rester seuls, ni la chèvre et le chou. Décrire l'algorithme qui résout le problème (pas de solution dans le document).
- **Tri** : trier une suite de nombres dans l'ordre croissant. Énoncé formel : entrée, une suite de $n$ nombres $(a_1, \ldots, a_n)$ ; sortie, une réorganisation $(a'_1, \ldots, a'_n)$ telle que $a'_1 \le a'_2 \le \ldots \le a'_n$. Exemple : $(31, 41, 59, 26, 41, 58)$ donne $(26, 31, 41, 41, 58, 59)$. La suite d'entrée est une **instance** du problème.
- **Les algorithmes de tri** : opération majeure, beaucoup d'algorithmes existent ; le meilleur dépend du nombre d'éléments, de leur ordre initial, des restrictions sur les valeurs et du périphérique de stockage.

### Correction

[[Correction d'un algorithme]] : un algorithme est correct si, pour chaque entrée, il se termine en produisant la bonne sortie. Un algorithme incorrect risque de ne pas se terminer sur certaines instances, ou de rendre une autre réponse ; il peut pourtant être utile si son taux d'erreur est contrôlé.

### Problèmes difficiles

« Correctness may be theoretical, but incorrectness has a practical impact. » Exemple du [[Problème du voyageur de commerce]] : une entreprise de camionnage charge un camion au dépôt, l'envoie livrer plusieurs villes, et il revient au dépôt. Comment choisir l'ordre des livraisons pour minimiser la distance ? Il n'existe pas d'algorithme efficace donnant la solution exacte en un temps raisonnable, mais il existe des [[Algorithme d'approximation|algorithmes d'approximation]] qui donnent rapidement une distance proche du minimum.

### Modélisation

[[Modélisation d'un problème]] : le tri est déjà abstrait ; les problèmes réels doivent être **modélisés** avant d'être résolus (identifier et formaliser les objets et opérations). Cela peut être facile (passeur, voyageur de commerce) ou très difficile (donner par téléphone les instructions pour lacer ses chaussures).

Exemples de problèmes réels :

| Problème | Solutions |
|---|---|
| Carte routière : trajet le plus court entre deux localités, les distances entre localités adjacentes étant connues | modéliser la carte en graphe, chercher le plus court chemin entre deux sommets |
| Gestion et allocation des ressources d'une compagnie aérienne (équipement, personnel, planification, risques) | recherche opérationnelle, programmation linéaire |
| Commerce électronique (échanges, confidentialité des données sensibles) | cryptographie, signature numérique, théorie des nombres |

![[AlgoID1 - p15.jpg]]
*Figure : instance du problème du plus court chemin, trajet en voiture de l'EISTI à la tour Eiffel sur une carte routière.*

### Approche par décomposition

Un seul algorithme pour un problème complexe est souvent trop difficile à trouver : on le **décompose** en sous-problèmes, plus faciles à modéliser et abordables séparément. **Modularité** : certaines sous-solutions sont réutilisables ([[Programmation modulaire]]). Citation : « Diviser chacune des difficultés que j'examinerais, en autant de parcelles qu'il se pourrait, et qu'il serait requis pour les mieux résoudre » (Descartes, *Discours de la méthode*).

### Un algorithme réussit-il toujours ?

Non. Exemple d'**Ariane 5**, premier vol (4 juin 1996) : la fusée explose 37 secondes après le décollage. Cause : un programme d'Ariane 4 non reconfiguré pour Ariane 5 donne de fausses informations ; l'ordinateur de bord fait une mauvaise correction de trajectoire. 370 M$ perdus, sans victime.

A-t-on encore besoin d'algorithmique avec des ordinateurs ultra-rapides et une mémoire bon marché ? **Oui** : la capacité des machines augmente, mais la taille des problèmes aussi. « Work expands so as to fill the time available for its completion » ([[Loi de Parkinson]]).

Source principale du cours : *Algorithmique*, 3e édition (2010), de Cormen, Leiserson, Rivest et Stein.

## 2. Éléments de base en pseudo-code

Plan : programme et instructions ; variables, types, expressions ; affectation et saisie ; structure conditionnelle (`SI`, `SELON`) ; boucles (`TANTQUE`, `JUSQUACEQUE`, `POUR`).

### Programme et instructions

Un `PROGRAMME` a au moins un nom, un `DEBUT` et une `FIN`. Un programme impératif est une suite finie d'instructions.

```text
PROGRAMME monProgramme
DEBUT
    /* Zone de commentaires non pris en compte à la compilation */
    // Commentaires sur une ligne
    /* Commentaires sur plusieurs lignes */
FIN
```

Instruction de base : l'écriture dans le terminal, `ECRIRE(argument)`.

```text
PROGRAMME Bonjour
DEBUT
    ECRIRE("Bonjour !")
FIN
```

### Variables, types et expressions

- [[Variable (programmation)|Variable]] : élément du programme qui stocke des valeurs ; elle a un nom et un type. Déclaration dans une zone `VARIABLES`, avant le début du programme : `nom_variable : TYPE_VARIABLE`.
- **Type** : collection de valeurs sur lesquelles on applique des opérateurs. Valeurs et variables reliées par des opérateurs forment une **expression**, dont le résultat est une seule valeur. Tout langage a des types prédéfinis ; on peut aussi définir ses propres types.

[[Type primitif|Types primitifs]] :

| Type | Valeurs / opérateurs |
|---|---|
| `ENTIER` | `+`, `-`, `*`, `DIV`, `MOD` |
| `REEL` | `+`, `-`, `*`, `/` |
| `BOOLEEN` | `VRAI` / `FAUX` ; `ET`, `OU`, `NON` |
| `CARACTERE` | un caractère |
| `CHAINE` | chaîne de caractères ; concaténation `&` |

```text
VARIABLES
    x, y : ENTIER
    a : BOOLEEN
    r1, r2 : REEL
    mot : CHAINE
```

Exemples d'expressions : `5 + x * 9` ; `"Bonjour les amis"` ; `"Je m'appelle" & nom` ; `a + (100 * b) mod 47`.

### Affectation

[[Affectation]] : assigner une valeur (une expression du **même type** que la variable) à une variable. La première affectation est l'**initialisation**. Notation : `Variable ← expression` (« Variable prend la valeur de expression »).

```text
x ← 2
y ← x + 3
mot ← 'Bonjour'
somme ← 8 * x + (y - x DIV 2) * 3

PROGRAMME ecriture_message
VARIABLES
    rep : INTEGER
DEBUT
    rep ← 42
    ECRIRE("La reponse a la question universelle est : " & rep)
FIN
```

### Saisie

`LIRE(variable)` : la variable prend la valeur saisie par l'utilisateur.

```text
PROGRAMME Lecture_message
VARIABLES
    message : CHAINE
DEBUT
    ECRIRE("Que voulez-vous dire ?")
    LIRE(message)            // Lecture et retour à la ligne
    ECRIRE("Vous avez voulu dire : " & message)
FIN
```

### Conditionnelle

[[Structure conditionnelle]]. Expressions booléennes : [[Opérateur de comparaison|opérateurs de comparaison]] `=`, `<>`, `>=`, `<=`, `>`, `<` (valables pour tous les types primitifs), combinables avec les [[Opérateur logique|opérateurs booléens]]. Exemples : `a = 5`, `mot = "toto"`, `x < 0`, `lettre > "r"`, `(x>0) OU (x<y)`, `(mois>=1) ET (mois<=12)`.

**SI … ALORS … SINON** : offre une alternative selon la valeur d'une condition.

```text
SI (condition) ALORS (* instructions 1 *)
FINSI

SI (condition) ALORS (* instructions 1 *)
SINON (* instructions 2 *)
FINSI

PROGRAMME saisie_notes
VARIABLES
    note : ENTIER
DEBUT
    ECRIRE("Entrez la note")
    LIRE(note)
    SI (note > 18) ALORS
        ECRIRE("C'est pas trop mal")
    SINON
        ECRIRE("C'est nul !!!")
    FINSI
FIN
```

Exercices (sans corrigé) :

1. **Température** : saisir la température de l'eau (entier, en degrés) et dire si c'est de la glace (en dessous de 0), du liquide (entre 0 et 100) ou de la vapeur (au-delà de 100).
2. **Année bissextile** : les années divisibles par 4 sont bissextiles, pas les autres ; exception, les années divisibles par 100 ne le sont pas ; exception à l'exception, les années divisibles par 400 le sont.

**SELON LE CAS** : exécute une suite d'instructions selon la valeur d'une variable ; le cas `DEFAUT` est à prévoir obligatoirement.

```text
SELON variable
    CAS valeur_1 : (* Instructions_1 *)
    CAS valeur_2 : (* Instructions_2 *)
    [...]
    CAS valeur_n : (* Instructions_n *)
    DEFAUT (* instructions quand aucun cas ne convient *)
FINSELON

PROGRAMME exo_cas
VARIABLES
    note : ENTIER
DEBUT
    ECRIRE("Entrez la note")
    LIRE(note)
    SELON note
        CAS 20 : ECRIRE("C'est correct")
        CAS 19 : ECRIRE("C'est moyen")
        DEFAUT : ECRIRE("C'est nul !!!")
    FINSELON
FIN
```

### Boucles

[[Boucle (programmation)|Boucles]].

**TANTQUE** : répète une suite d'instructions tant qu'une condition de continuation est vraie (test **avant** chaque tour).

![[AlgoID1 - p41.jpg]]
*Figure : organigramme de la boucle TANTQUE : condition testée d'abord, instructions exécutées si elle est vraie, sortie sinon.*

```text
TANTQUE (condition)
    (* Suite d'instructions *)
FINTANTQUE

PROGRAMME Dites33
VARIABLES
    nombre : ENTIER
DEBUT
    ECRIRE('Dites 33')
    LIRE(nombre)
    TANTQUE (nombre <> 33)
        ECRIRE('Erreur ! Dites 33')
        LIRE(nombre)
    FINTANTQUE
FIN
```

Exercice (sans corrigé) : demander la réponse à la question universelle et la redemander indéfiniment jusqu'à ce que l'utilisateur réponde « 42 » (clin d'œil au *Guide du voyageur galactique* de Douglas Adams).

**REPETER … JUSQUACEQUE** : à l'inverse, on répète **jusqu'à** ce qu'une condition d'arrêt soit vraie (test **après** chaque tour : au moins une exécution). Pas besoin de `DEBUT … FIN` autour des instructions.

![[AlgoID1 - p44.jpg]]
*Figure : organigramme de REPETER … JUSQUACEQUE : instructions d'abord, puis test de la condition d'arrêt.*

```text
REPETER
    (* Suite d'instructions *)
JUSQUACEQUE (condition)

PROGRAMME Dites33bis
VARIABLES
    nombre : ENTIER
DEBUT
    REPETER
        ECRIRE('Dites 33')
        LIRE(nombre)
    JUSQUACEQUE (nombre = 33)
FIN
```

**POUR** : répète un nombre déterminé de fois, avec un compteur (itérateur) qui augmente de 1 à chaque tour. On ne doit pas modifier l'itérateur dans la boucle.

![[AlgoID1 - p46.jpg]]
*Figure : organigramme de la boucle POUR : compteur initialisé, comparé à la valeur finale, incrémenté après les instructions.*

```text
VARIABLES
    i : ENTIER   // itérateur
[...]
POUR i DE initial A final
    (* Suite d'instructions *)
FINPOUR

PROGRAMME Somme
VARIABLES
    n, i, resultat : ENTIER
DEBUT
    ECRIRE('Entrez la valeur de n')
    LIRE(n)
    resultat ← 0
    POUR i DE 1 A n          // Attention, on ne doit pas manipuler i !!
        resultat ← resultat + i
    FINPOUR                  // À chaque retour de boucle, i ← i+1
    ECRIRE('La somme est de : ' & resultat)
FIN
```

Exercice (sans corrigé) : calculer le produit $1 \times 2 \times \ldots \times N$ ($N$ saisi), en trois versions, une par boucle (`POUR`, `TANTQUE`, `JUSQUACEQUE`). Voir [[Factorielle]].

**Rappel** : `SI … ALORS … SINON` n'est **pas** une boucle : il n'y a pas de répétition, parler de « boucle si » n'a pas de sens.

### TD Éléments de base (sans corrigé)

**A. Travail sur les variables.**

1. Valeurs de $x$ et $y$ après :
   - a) `x ← 1 ; y ← x + 1 ; x ← 3`
   - b) `x ← 1 ; y ← x + 1 ; x ← y + 5`
   - c) `x ← 1 ; x ← x + 5 ; y ← 13 ; y ← y - x`
   - d) (chaînes) `x ← "123" ; y ← x & "abc"`
2. Valeurs de $x, y, z$ après :
   - a) `x ← 1 ; z ← 2 ; y ← x + z ; x ← 3 ; z ← y - x`
   - b) (chaînes) `x ← "12" ; y ← "34" ; z ← x & y`
3. Valeurs de $x, y, z, t$ (entiers) et $u, v$ (booléens) après :
   ```text
   x ← 7 ; y ← 12 ; z ← y - x ; z ← z * 3 ; t ← x ; x ← y
   v ← faux ; u ← non v ; u ← u ou (y=4) ; v ← (y=12) et (z=2)
   ```
4. **La permutation** ([[Échange de deux variables]]) :
   - a) valeurs de $x$ et $y$ après `x ← 3 ; y ← 2 ; x ← y ; y ← x` ; cela change-t-il quelque chose d'inverser les deux dernières instructions ?
   - b) écrire un algorithme qui échange le contenu de deux variables $x$ et $y$ quel que soit leur contenu (il faudra sûrement une troisième variable).

**B. Saisie et affichage** (programmes clairs dans l'affichage et les données demandées) :

1. saisir un nombre et afficher son carré ;
2. saisir deux nombres et afficher leur moyenne ;
3. saisir le prix d'un produit, la quantité achetée et le taux de TVA, puis afficher le total à payer ;
4. sachant que 1 pouce = 2,54 cm, saisir la taille d'un écran en pouces et afficher sa correspondance en centimètres ;
5. saisir un montant en euros (sans centimes) et afficher sa décomposition en un minimum de billets de 100, 50, 10, 5 € et de pièces de 2 et 1 € (utiliser la division entière `DIV` et le reste `MOD`, voir [[Division euclidienne]]) ;
6. saisir un temps en secondes et afficher son équivalent en heures, minutes, secondes. Exemple : 7512 s donne 2 heures 5 minutes 12 secondes.

## 3. Fonctions et procédures (cours 2)

Voir [[Fonction et procédure]].

### Définitions et syntaxe

- **Fonction** : suite d'instructions qui peut prendre des paramètres en entrée et qui **retourne** un résultat à la fonction appelante.
- **Procédure** : suite d'instructions réalisant une tâche, à laquelle on donne un nom pour l'appeler ultérieurement ; elle ne retourne pas de valeur.
- **Programme** : suite d'instructions particulière, point d'entrée d'une application ; il peut appeler fonctions et procédures, mais ne peut pas être appelé par elles.

```text
Fonction nom(liste de paramètres) : type de retour
Variables
    variables locales
Début
    Instructions
    Retourner …
Fin

Procédure nom(liste de paramètres)
Variables
    variables locales
Début
    Instructions
Fin

Programme nom
Variables
    variables locales
Début
    Instructions
Fin
```

Exemples du cours :

```text
Fonction calculeCarre(n : Entier) : Entier
Variables
    res : Entier
Début
    res ← n * n
    Retourner res
Fin

Procédure equation(a : Entier, b : Entier)     // résout ax + b = 0
Variables x : Réel
Début
    Si a = 0 Alors
        Si b = 0 Alors
            Ecrire "Il y a une infinité de solutions"
        Sinon
            Ecrire "L'ensemble des solutions est vide"
        FinSi
    Sinon
        x ← -b/a
        Ecrire "La solution unique est : ", x
    FinSi
Fin
```

### Appel d'une fonction ou d'une procédure

L'appel arrête momentanément l'appelant pour exécuter la fonction (ou procédure) appelée. À la fin de celle-ci, l'exécution reprend chez l'appelant, à l'endroit de l'appel. Le résultat d'une fonction **doit être stocké** (dans une variable ou ailleurs) pour être utilisé.

![[AlgoID1 - p60.jpg]]
*Figure : appel d'une fonction : l'appelant exécute `x ← F(…)`, la main passe à F, puis revient à l'appelant (« appeler » / « retourner »).*

![[AlgoID1 - p62.jpg]]
*Figure : appel d'une procédure P : même aller-retour, sans valeur à récupérer.*

```text
Programme testCarre
Variables
    res : Entier
Début
    res ← calculCarre(12)
    Ecrire res
Fin

Programme test
Variables x, y : Entier
Début
    equation(2,5)
    x ← 0
    y ← 2
    equation(x,y)
Fin
```

### Exercices corrigés dans le cours

**Exercice 1** : fonction qui retourne $a^n$ ($n \ge 0$). Solution du cours :

```text
Fonction puissance(a : Entier, n : Entier) : Entier
Variables p, i : Entier
Début
    p ← 1
    Pour i ← 1 à n
        p ← p*a
    FinPour
    Retourner p
Fin
```

**Exercice 2** : programme qui saisit $a$ et $n$ et affiche $a^n$. Solution :

```text
Programme Test
Variables a, n, p : Entier
Début
    Ecrire "Saisir le 1er entier : "
    Lire a
    Ecrire "Saisir le 2eme entier : "
    Lire n
    p ← puissance(a,n)
    Ecrire "La puissance est : ", p
Fin
```

**Exercice 3** : procédure qui résout $ax^2 + bx + c = 0$ ([[Équation du second degré]]), par disjonction de cas sur $\Delta = b^2 - 4ac$. Solution :

```text
Procédure Equation2Degre(a, b, c : Entier)
Variables delta : Réel
Début
    Si a = 0 Alors
        Equation(b,c)                 // cas du premier degré
    Sinon
        delta ← b*b - 4*a*c
        Si delta < 0 Alors
            Ecrire "Delta négatif, il n'y a pas de solution"
        Sinon
            Si delta = 0 Alors
                Ecrire "Delta nul, il n'y a qu'une seule solution : ", -b/(2*a)
            Sinon
                Ecrire "Delta positif, il y a 2 racines:", (-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)
            FinSi
        FinSi
    FinSi
Fin
```

**Exercice 4** : programme qui saisit trois coefficients $x, y, z$ et résout l'équation correspondante. Solution :

```text
Programme Test
Variables x, y, z : Entier
Début
    Ecrire "Saisir les coefficients : "
    Lire x, y, z
    Equation2Degre(x,y,z)
Fin
```

### Variables locales et globales

[[Portée d'une variable]] :

- **variable locale** : déclarée dans une fonction/procédure, visible uniquement par celle-ci ;
- **variable globale** : visible dans tout le programme, par toutes les fonctions et procédures.

Trois exemples (« affiche quoi ? », réponse non donnée dans le document) :

```text
// Exemple 1
Fonction maFonction(y : Entier) : Entier
Variables tmp : Entier
Début
    tmp ← y*3
    Retourner tmp
Fin
Programme Test
Variables res, x : Entier
Début
    x ← 7
    res ← maFonction(x)
    Ecrire res              // affiche quoi ?
Fin

// Exemple 2 : maFonction fait tmp ← y + 2 puis y ← 8, retourne tmp
//   x ← 7 ; res ← maFonction(x) ; Ecrire res ; Ecrire x   // 7 ou 8 ?

// Exemple 3 : variable globale « global »
//   maFonction fait tmp ← y + 2 puis global ← 8, retourne tmp
//   global ← 7 ; res ← maFonction(global) ; Ecrire res ; Ecrire global   // 7 ou 8 ?
```

Réponses attendues (complément, non données par le cours) : exemple 1, 21 ; exemple 2, 9 puis 7 (modifier le paramètre `y` ne change pas `x`) ; exemple 3, 9 puis 8 (la globale est modifiée).

### Retourner plusieurs valeurs : paramètres de sortie

Question : comment rendre plusieurs valeurs à l'appelant, par exemple le quotient **et** le reste d'une division entière ? Deux solutions : une fonction qui retourne une **structure de données** ; une fonction/procédure avec des **paramètres de sortie**. Voir [[Passage de paramètres]].

![[AlgoID1 - p78.jpg]]
*Figure : les deux types de paramètres : paramètres d'entrée (par défaut) de l'appelant vers l'appelé, paramètres de sortie de l'appelé vers l'appelant.*

| Mode | Sens |
|---|---|
| `E` | entrée (par défaut) |
| `S` | sortie |
| `ES` | entrée-sortie |

Exemples d'en-têtes : `Procédure divisionEntiere(E a, b : Entier, S quotient, reste : Entier)` ; `Procédure inversion(ES s : Caractère)`.

**Exercice** : écrire `divisionEntiere` et un programme qui l'appelle. Solution du cours (division par soustractions successives) :

```text
Procédure divisionEntiere(E a, b : Entier, S quotient, reste : Entier)
Début
    quotient ← 0
    Tantque a ≥ b
        a ← a - b
        quotient ← quotient + 1
    FinTantque
    reste ← a
Fin

Programme Test
Variables x, y, q, r : Entier
Début
    x ← 10
    y ← 3
    divisionEntière(x,y,q,r)
    Ecrire "quotient = ", q
    Ecrire "reste = ", r
Fin
```

**Permutation par procédure** : avec `Procédure permuter(x, y : Entier)` (tmp ← x ; x ← y ; y ← tmp), le programme `a ← 1 ; b ← 5 ; permuter(a,b)` affiche toujours `a = 1, b = 5` : **il n'y a pas de modification sur a et b**, car les paramètres sont en entrée seulement ([[Passage par valeur]]). Solution : des paramètres en entrée-sortie.

```text
Procédure permuter2(ES x, y : Entier)
Variables tmp : Entier
Début
    tmp ← x
    x ← y
    y ← tmp
Fin
// a ← 1 ; b ← 5 ; permuter2(a,b) affiche a = 5, b = 1
```

### Fonctions prédéfinies

| Fonctions numériques | Fonctions de texte |
|---|---|
| `ent : Réel → Entier` | `longueur : Chaîne → Entier` |
| `aléa : Entier → Entier` | `extrait : Chaîne × Entier × Entier → Chaîne` |
| `sqrt : Réel → Réel` | `trouve : Chaîne × Chaîne → Booléen` |
| | `ascii : Caractère → Entier` |
| | `carac : Entier → Caractère` |

### Présentation modulaire

[[Programmation modulaire]]. Objectifs : architecture claire ; modules concis et spécifiques ; modules testables et modifiables indépendamment. Mise en œuvre : limiter au maximum les variables (notamment globales) ; adapter les modules aux unités fonctionnelles de l'application ; découper l'algorithme pour le rendre léger, lisible et performant.

## 4. Fonctions en Python

Voir [[Langage Python]] et le document [[Raw/Year 1/Algo Maths/Python.docx|Python]].

### Rappels

Une fonction encapsule un algorithme particulier, utilisable à chaque besoin en **invoquant** la fonction. Avantages : pas besoin de réécrire l'algorithme à chaque usage (programmes plus petits) ; découpage modulaire qui facilite la recherche d'erreurs et la vérification ; réutilisation dans plusieurs programmes. Une fonction peut avoir des arguments et une valeur retournée, tous deux optionnels.

### Types de fonctions

Sans argument (définition, puis invocation) :

```python
def cinqespaces():          # définition
    i = 1
    while i <= 5:
        print(" ", end="")
        i = i + 1

cinqespaces()               # invocation
print("OK")
```

Avec un argument (`n` est l'argument, `k` la valeur passée) :

```python
def nespaces(n):
    i = 1
    while i <= n:
        print(" ", end="")
        i = i + 1

k = int(input("combien d'espaces ?"))
nespaces(k)
print("OK")
```

Avec plusieurs arguments (affiche un rectangle d'étoiles de largeur `l` et de hauteur `h`) :

```python
def rectangle(l, h):
    i = 1
    while i <= h:
        j = 1
        while j <= l:
            print("*", end="")
            j = j + 1
        print("")
        i = i + 1

rectangle(7, 5)
```

### Fonctions retournant une valeur

Le corps contient une ou plusieurs instructions `return`, qui déterminent la valeur retournée et terminent l'exécution de la fonction ; l'exécution reprend à l'instruction qui suit l'invocation.

```python
def cube(n):
    return n**3

def volumeSphere(r):
    return 4 * 3.1416 * cube(r) / 3

r = float(input("Entrez la valeur du rayon de la sphere: "))
v = volumeSphere(r)
print("Le volume de cette sphère vaut : ", v)
```

![[AlgoID1 - p95.jpg]]
*Figure : enchaînement des appels : le programme appelle `volumeSphere(r)`, qui appelle `cube(r)` ; les flèches montrent le passage de la valeur et le retour.*

Exercice (sans corrigé) : programme qui saisit un entier positif $n$ et affiche le nombre d'entiers premiers inférieurs ou égaux à $n$ ([[Nombre premier]]).

### Transmission des arguments

En Python, la transmission d'un argument et du résultat se fait **toujours par valeur**. Attention avec les valeurs **mutables** : la valeur transmise est la **référence**, donc l'appel peut créer des **effets secondaires** (*side effects*) hors de la fonction ([[Effet de bord]]).

Exemple du cours, avec un entier (non mutable) :

```python
def incr(n):
    n = n + 1
    print("En fin d'execution de incr, n vaut : ", n)

i = 1
print("Avant l'appel de incr, i vaut :  ", i)
incr(i)
print("Apres l'appel de incr, i vaut :  ", i)
```

Sortie :

```text
Avant l'appel de incr, i vaut :   1
En fin d'execution de incr, n vaut :   2
Apres l'appel de incr, i vaut :   1
```

`i` n'est pas modifié. Le document n'a pas d'exemple avec une valeur mutable (voir « Erreurs du cours »).

### Résumé : structure d'un programme Python type

Un programme Python contient en général, dans l'ordre : des instructions d'initialisation (importation de fonctions ou de classes, variables globales) ; les définitions locales de fonctions ou de classes ; le corps principal du programme.

![[AlgoID1 - p100.jpg]]
*Figure : programme type annoté (1/2) : en-tête, importation `from math import sqrt`, définition de `occurrences(car, ch)` ; annotations sur les paramètres et sur les quatre éléments d'une boucle `while`.*

![[AlgoID1 - p101.jpg]]
*Figure : programme type annoté (2/2) : `return nc` et corps principal qui appelle `occurrences` et `sqrt`.*

```python
# -*- coding:Utf8 -*-
# Programme Python type  (auteur : G.Swinnen, Liège, 2009 ; licence : GPL)

# Importation de fonctions externes :
from math import sqrt

# Définition locale de fonctions :
def occurrences(car, ch):
    "Cette fonction renvoie le nombre de caractères <car> contenus dans la chaîne <ch>"
    nc = 0
    i = 0
    while i < len(ch):
        if ch[i] == car:
            nc = nc + 1
        i = i + 1
    return nc

# Corps principal du programme :
print("Veuillez entrer un nombre :")
nbr = eval(input())
print("Veuillez entrer une phrase :")
phr = input()
print("Entrez le caractère à compter :")
cch = input()
no = occurrences(cch, phr)
rc = sqrt(nbr**3)
print("La racine carrée du cube", end=' ')
print("du nombre fourni vaut", end=' ')
print(rc)
print("La phrase contient", end=' ')
print(no, "caractères", cch)
```

Annotations de la figure :

- un programme peut utiliser un nombre quelconque de fonctions, définies localement ou importées de modules externes (qu'on peut écrire soi-même) ;
- la définition d'une fonction comporte souvent une liste de **paramètres** : ce sont toujours des variables, qui reçoivent leur valeur à l'appel ;
- une boucle `while` doit toujours comporter au moins quatre éléments : l'initialisation d'un compteur, l'instruction `while` avec sa condition, le bloc à répéter, une instruction d'incrémentation du compteur ;
- la fonction « renvoie » toujours une valeur au programme appelant ; sans `return`, ou avec un `return` sans argument, elle renvoie `None` ;
- l'appelant transmet d'habitude des **arguments** : valeurs, variables ou expressions.

### Modules

Python fournit d'office de nombreux modules pré-programmés : des fichiers qui regroupent des fonctions apparentées (des **bibliothèques**). Exemple : le module `math` (sinus, cosinus, tangente, racine carrée…), invoqué par `from math import *`.

```python
# Démo : utilisation des fonctions du module <math>
from math import *

nombre = 121
angle = pi/6        # soit 30° (la bibliothèque math inclut aussi la définition de pi)
print("racine carrée de", nombre, "=", sqrt(nombre))
print("sinus de", angle, "radians", "=", sin(angle))
```

Exercices (sans corrigé) :

- calculer le périmètre et l'aire d'un triangle quelconque dont l'utilisateur fournit les trois côtés ;
- définir `maximum(n1, n2, n3)` qui renvoie le plus grand de trois nombres ;
- écrire `inverse(ch)` qui inverse l'ordre des caractères d'une chaîne et la renvoie au programme appelant.

## 5. Introduction à Python (« Algorithmic and programming », 2018-2019, en anglais)

- Python, développé par Guido van Rossum ; **[[Langage interprété]]**, **[[Typage dynamique|typé dynamiquement]]**.
- **Interpréteur** : il affiche son invite `>>>` (exemple : Python 3.7.1) et évalue les entrées : `3+2` donne `5` ; `"Hello "+"world"` donne `'Hello world'` ; `"you"*3` donne `'youyouyou'`. On le quitte par `exit()`, ou Ctrl-D (Unix, Mac OS), Ctrl-Z (Windows).
- L'**indentation** a un sens : elle délimite les blocs. Le type des variables n'est pas déclaré, Python le détermine. L'affectation s'écrit `=`.

**Types de base** :

```python
x = 3            # Integer
y = x + 3
x = 3.5          # Float
y = 5/2
x = 'Hello'      # String
y = "Hello"
z = """ Hello """
x = True         # Boolean
```

**Affectation** : simple `x = 7` ; simultanée `x = y = 7` ; concurrente `x, y = 7, 53.2`. Connaître le type : `type(x)` ; tester le type : `isinstance(x, float)`.

**Opérateurs** :

| Opérateur | Description |
|---|---|
| `a+b` | addition |
| `a-b` | soustraction de $b$ à $a$ |
| `a*b` | multiplication |
| `a/b` | division |
| `a//b` | division entière (*floor division*) |
| `a**b` | $a$ puissance $b$ |
| `%` | reste (cité dans la liste) |

Opérateurs logiques : `and`, `or`, `not`. Opérateurs relationnels : `>`, `<`, `>=`, `<=`, `==`, `!=`. Bonus : `x += 1` ($x = x+1$), `x -= 1`, `x *= 1`.

**Entrées-sorties** : `print(expression1, expression2, …)`, par exemple `print("the value is :", x)` ; `input([string])`, par exemple `x = input("please enter a value")` ou `x = input()`.

**Structures de contrôle** :

```python
if x > 0:        # les deux instructions dépendent du test
    x = x + 1
    z = x / 2

if x > 0:        # seule la première dépend du test
    x = x + 1
z = x / 2

if condition:
    statements_1
elif condition:
    statements_2
else:
    statements_3

i = 1
while i < 10:
    print(i, "looping")
    i += 1

for i in range(0, 3):
    print(i, "looping")

str = "abcd"
for i in str:
    print i          # syntaxe Python 2 : print(i) en Python 3
```

`for element in sequence:` parcourt une séquence (voir [[Fonction range (Python)]]). `break` arrête la boucle ; `continue` arrête l'itération en cours et passe directement à la suivante.

## 6. Types structurés (enregistrements)

Voir [[Structure (struct)]].

### Définitions

- Les **enregistrements** sont des structures de données dont les éléments peuvent être de types différents ; ces éléments sont les **champs**.
- Pour toute variable enregistrement, il faut avoir défini au préalable son type (nom et type des champs) : c'est un **type structuré**. Les variables de ce type sont des enregistrements.
- Exemples : un complexe (partie réelle, partie imaginaire) ; une date (jour 1..31, mois 1..12, année strictement positive) ; un stage (intitulé, date de début, date de fin, nombre de places).

### Syntaxe

```text
Type
    Structure nom_type
        nom_champ1 : type_champ1
        …
        nom_champN : type_champN
    FinStruct

Type
    Structure tpersonne
        nom : chaîne
        prenom : chaîne
        age : entier
    FinStruct

Variables pers1, pers2, pers3 : tpersonne
```

On déclare un enregistrement comme une variable de type primitif : `Variables nom_variable : nom_type`.

### Manipulation

- On manipule un enregistrement par ses champs ; pour l'afficher, il faut afficher ses champs un par un.
- Accès : `nom_enregistrement.nom_champ`, la valeur mémorisée dans ce champ. Exemple : `pers2.age`, qui se lit de droite à gauche : « l'âge de la personne 2 ».
- Un nom de champ ne peut pas apparaître seul, sans l'enregistrement.

**Exercice** : saisir le nom et l'âge de `pers1` et `pers2`, puis afficher leur différence d'âge. Solution du cours :

```text
Programme Exemple
Type
    Structure tpersonne
        nom : chaîne
        prenom : chaîne
        age : entier
    FinStruct
Variables
    pers1, pers2 : tpersonne
DEBUT
    Ecrire("Entrez le nom puis l'âge de la personne 1")
    Lire(pers1.nom, pers1.age)
    Ecrire("Entrez le nom puis l'âge de la personne 2")
    Lire(pers2.nom, pers2.age)
    Si pers1.age > pers2.age Alors
        Ecrire("La différence d'âge entre ", pers1.nom, " et ", pers2.nom, " est de ", pers1.age - pers2.age, " ans")
    SINON
        Ecrire("La différence d'âge entre ", pers1.nom, " et ", pers2.nom, " est de ", pers2.age - pers1.age, " ans")
    FINSI
FIN
```

### Enregistrement comme champ

Si l'on remplace l'âge par la date de naissance : une date (jour, mois, année) est une entité indissociable, donc un type enregistrement à trois champs, utilisé comme champ d'un autre type.

```text
TYPE
    Structure date
        jour : entier
        mois : chaîne
        année : entier
    FinStruct
    Structure personne
        nom : chaîne
        ddn : date
    FinStruct
```

Accès à l'année de naissance : deux fois l'opérateur `.`, soit `pers1.ddn.année`.

Exemple-exercice (sans corrigé) : un produit a un code, un libellé, un prix et est livré par un seul fournisseur ; un fournisseur a un code, une raison sociale et un numéro de téléphone. Écrire un programme qui affiche le numéro de téléphone du fournisseur d'un produit.

### TD Enregistrements (2022-2023, sans corrigé)

1. **Fraction** : a. définir un type fraction pour représenter les rationnels ; b. afficher un rationnel ; c. additionner deux rationnels.
2. **Nombre complexe** : a. définir un type complexe ; b. additionner deux complexes.
3. **Divers** : une personne a un prénom, un nom et une date de naissance de 3 entiers (jour, mois, année).
   - a. écrire les structures pour manipuler personnes et dates ;
   - b. écrire une fonction qui calcule l'âge en années d'une personne à une date donnée. Exemple de l'énoncé : née le 3/10/1998, à la date du 21/7/2019, « 19 ans » (le bon résultat est 20 ans, voir « Erreurs du cours »). Si la date donnée est antérieure à la naissance (1/1/1972 pour une personne née le 1/1/2000), retourner 0. On ne teste pas la validité des dates.

## 7. Récursivité (cours 3)

### Définition

[[Récursivité]] : un algorithme est **récursif** s'il s'appelle lui-même dans sa propre définition. Correspondance mathématique : le principe de [[Récurrence]] ; exemple, la définition des entiers (0 est un entier ; si $n$ est un entier, $n+1$ est un entier).

### Exemples

```text
Fonction fact(n : Entier) : Entier          // Exemple 1 : factorielle
Début
    Si (n = 1) Alors
        Retourner 1
    Sinon
        Retourner fact(n-1) * n
    FinSi
Fin

Fonction pgcd(a : Entier, b : Entier) : Entier   // Exemple 2 : PGCD
Début
    Si (b = 0) Alors
        Retourner a
    Sinon
        Retourner pgcd(b, a mod b)
    FinSi
Fin
```

Voir [[Factorielle]] et [[Algorithme d'Euclide]].

**Exemple 3 : [[Tours de Hanoï]]**.

![[AlgoID1 - p144.jpg]]
*Figure : les tours de Hanoï : une pile de disques de tailles décroissantes sur le premier des trois piquets.*

```text
Procédure Déplacer(n, de, à, par : Entier)
Début
    Si n > 0 Alors
        Déplacer(n-1, de, par, à)     // les n-1 disques du dessus vers le piquet intermédiaire
        BougerUnDisque(de, à)         // le plus grand disque vers la destination
        Déplacer(n-1, par, à, de)     // les n-1 disques par-dessus
    FinSi
Fin
```

### Forme générale

Fonction récursive :

$$f(x) = \text{si } c(x) \text{ alors } g(x) \text{ sinon } h\big(f(s(x)), x\big) \text{ finsi}$$

- $c(x)$ : la **condition d'arrêt**, un booléen ;
- $g(x)$ : le **cas trivial**, en général une valeur constante retournée quand $c(x)$ est vrai ;
- $s(x)$ : le **successeur** de $x$ ;
- $h(f(s(x)), x)$ : l'**appel récursif**, fonction de $x$ et de son successeur.

Procédure récursive :

```text
p(x) = si c(x) alors
           p0(x)          // cas trivial
       sinon
           p1(x)
           p(s(x))        // appel récursif
           p2(x)
       finsi
```

### Types de récursivité

- **Simple** : chaque appel engendre au plus un nouvel appel. **Multiple** : chaque appel en implique plusieurs.
- **Non terminale** (enveloppée) : l'appel récursif n'est pas la dernière instruction. **Terminale** : l'appel récursif est la dernière instruction, par exemple $f(x) = \text{si } c(x) \text{ alors } g(x) \text{ sinon } f(s(x))$, ou une procédure qui finit par $p(s(x))$. Voir [[Récursivité terminale]].

### Terminaison

[[Terminaison d'un algorithme]] : un algorithme récursif doit s'arrêter ; la condition d'arrêt doit impérativement finir par prendre la valeur vrai. Exemples à discuter (« cet algorithme se termine-t-il ? », sans réponse dans le document) :

```text
Fonction exemple1(n : Entier) : Entier
Début
    Si (n <= 0) Alors retourner 1
    Sinon retourner n + exemple1(n-1) + exemple1(n-2)
    FinSi
Fin

Fonction exemple2(n : Entier) : Entier
Début
    Si (n = 0) Alors retourner 1
    Sinon retourner n * exemple2(n-2)
    FinSi
Fin

Fonction exemple3(n : Entier) : Entier
Début
    Si estPremier(n) Alors retourner n
    Sinon retourner exemple3(n+2)
    FinSi
Fin

Fonction exemple4(n : Entier) : Entier      // conjecture de Syracuse
Début
    Si (n = 1) Alors retourner 1
    Sinon
        Si ((n mod 2) = 0) Alors retourner exemple4(n/2)
        Sinon retourner exemple4(3*n+1)
        FinSi
    FinSi
Fin
```

Pistes (complément) : `exemple1` se termine (récursion multiple, $n$ décroît jusqu'à $\le 0$) ; `exemple2` ne se termine que pour $n$ pair et positif ; `exemple3` boucle si aucun premier n'est atteint (par exemple pour $n$ pair supérieur à 2) ; `exemple4` est la [[Conjecture de Syracuse]], dont on ne sait pas démontrer la terminaison pour tout $n$.

**La terminaison est un [[Problème indécidable|problème indécidable]]** : il n'existe pas d'algorithme qui prend un programme en entrée et rend *true* si et seulement si ce programme termine.

### Avantages et inconvénients

- Très économique pour le programmeur : simple et intuitif (élégant, compact), proche d'une description mathématique (récurrence), plus facile à analyser, bien adapté aux structures de données récursives.
- Très coûteux en ressources machine : une **pile** conserve les informations de chaque appel en cours ([[Pile d'exécution]], [[Pile et file]]).
- Une solution : la récursivité terminale (placer les opérations qui suivent l'appel récursif à l'intérieur de l'appel lui-même).
- Tout algorithme récursif peut aussi s'écrire de façon itérative.

### Factorielle : non terminale, terminale, itérative

```text
Fonction fact(n : Entier) : Entier          // non terminale : « * n » après l'appel
Début
    Si (n = 1) Alors Retourner 1
    Sinon Retourner fact(n-1) * n
    FinSi
Fin

Fonction factRT(n : Entier, acc : Entier) : Entier   // terminale, avec accumulateur
Début
    Si (n = 1) Alors Retourner acc
    Sinon Retourner factRT(n-1, acc*n)
    FinSi
Fin

Fonction fact(n : Entier) : Entier
Début
    Retourner factRT(n, 1)
Fin
```

Factorielle itérative : laissée en exercice.

### Suite de Fibonacci

[[Suite de Fibonacci]]. Version non terminale (récursion multiple) :

```text
Fonction fibo(n : Entier) : Entier
Début
    Si (n < 2) Alors Retourner n
    Sinon Retourner fibo(n-1) + fibo(n-2)
    FinSi
Fin
```

$\text{Fibo}(5) \Rightarrow \text{Fibo}(4) + \text{Fibo}(3) \Rightarrow \ldots$ : $\text{Fibo}(3)$ est calculé 2 fois, $\text{Fibo}(2)$ 3 fois. Les sous-calculs se répètent.

Version terminale (d'abord laissée en exercice, puis corrigée sur la diapositive suivante) : on transporte les deux derniers termes.

```text
Fonction fiboRT(n, f_{n-2}, f_{n-1} : Entier) : Entier
Début
    Si (n = 0) Alors Retourner f_{n-2}
    Sinon Retourner fiboRT(n-1, f_{n-1}, f_{n-1} + f_{n-2})
    FinSi
Fin

fiboRT(12, 0, 1)        // appel initial : renvoie F(12) = 144 (complément)
```

### TD3 : Récursivité (sans corrigé)

1. Fonction récursive qui calcule le quotient de la division entière de deux nombres strictement positifs.
2. Fonction récursive qui calcule le reste de la division entière de deux nombres strictement positifs.
3. [[Palindrome]] : chaîne qui se lit dans les deux sens, comme « radar », « elle », « été », « esope reste ici et se repose » (en faisant abstraction des blancs). Écrire un algorithme récursif qui vérifie si une chaîne est un palindrome.
4. Fonction **miroir** : l'inverse d'une chaîne, par exemple `miroir("séminaire") = "erianimés"`. Version récursive, puis version itérative équivalente.
5. Fonction récursive `puissance(n réel, k entier)` qui calcule $n^k$ :
   - a. de façon naïve, avec $n^k = n \cdot n^{k-1}$ et $n^0 = 1$ ;
   - b. transformer en récursivité terminale ;
   - c. par **dichotomie** : si $k$ est pair, $n^k = (n \cdot n)^{k/2}$, sinon $n^k = n \cdot n^{k-1}$ ; écrire `puissance-dic` ([[Exponentiation rapide]]) ;
   - d. transformer cette version en récursivité terminale.

## Erreurs du cours

- [[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]], TD Enregistrements (exercice 3.b) : écrit que, née le 3/10/1998, la personne a « 19 ans » le 21/7/2019 ; il faut « 20 ans » ($2019 - 1998 = 21$, moins 1 car l'anniversaire n'est pas encore passé). À corriger avant de s'en servir comme test.
- [[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]], factorielle récursive : écrit le cas d'arrêt « Si (n = 1) Alors Retourner 1 » ; il faut « Si (n = 0) Alors Retourner 1 » pour que `fact(0)` se termine (avec le cas `n = 1`, `fact(0)` appelle `fact(-1)`, `fact(-2)`… sans fin). Même remarque pour `factRT`.
- [[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]], fonctions : écrit `res ← calculCarre(12)` ; il faut `calculeCarre(12)`, nom de la fonction définie. Dans le même support, `rep : INTEGER` est écrit au lieu de `ENTIER`, et la syntaxe donne `FINTANQUE` au lieu de `FINTANTQUE` (orthographe de l'exemple).
- [[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]], boucle `for` sur une chaîne : écrit `print i` ; il faut `print(i)` en Python 3 (`print i` est la syntaxe de Python 2 ; l'exemple voisin écrit bien `print(i, "looping")`).
- [[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]], structure `date` : écrit « mois: chaîne » ; il faut un entier, comme le décrivent l'introduction (numéro de mois 1..12) et le TD (date « constituée de 3 entiers »).
- [[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]], transmission des valeurs mutables (diapositives 11 à 13) : annonce un exemple d'effet de bord avec une valeur mutable, mais le seul exemple (`incr`) porte sur un entier, non mutable, qui n'est pas modifié ; il faut un objet mutable pour illustrer l'effet de bord, par exemple une liste passée à une fonction qui fait `l.append(…)`, modifiée chez l'appelant (complément).
