---
type: source
sources: ["[[Chp1 - Intro Java]]"]
maj: 2026-11-05
---

Résumé de [[Chp1 - Intro Java]], dans [[Year 3 - Java]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les bases du langage : variables, types, opérateurs, structures de contrôle, méthode `main`, compilation et tableaux.

## Contenu, dans l'ordre du cours

- **Variables** : `<Type> <nom>;`, plusieurs noms séparés par des virgules. Un nom commence par une lettre, `_` ou `$`, n'est pas un mot-clé, et peut ensuite contenir lettres, chiffres, `_` ou `$`. Java est sensible à la casse. Une constante se déclare avec `final` et s'écrit en majuscules ; la modifier est une erreur de compilation.
- **Types** : primitifs (`byte` 8 bits, `short` 16, `int` 32, `long` 64, `float` 32, `double` 64, `char` 16 en Unicode, `boolean`), types objets (définis par des classes et interfaces) et `void`.
- **[[Portée d'une variable]]** : région délimitée par des accolades. Deux variables d'une même portée ne peuvent pas avoir le même nom. Exemple d'erreur : `x` déclarée dans un bloc `do { ... }` n'existe pas dans la condition du `while`.
- **Opérations** : `print` et `println` ; comparaisons ; opérateurs booléens `&`, `|`, `^`, `&&`, `||`, `!` (voir [[Évaluation en court-circuit]]) ; caractères spéciaux `\n`, `\t`, `\r` ; `++` et `--`, où l'ordre compte (`y = ++x` donne `y = 11`, `y = x++` donne `y = 10` si `x` vaut 10).
- **Associativité** : toutes les opérations binaires s'associent à gauche, sauf l'affectation. Les opérandes sont évalués de gauche à droite, ce qui compte avec les effets de bord : avec `a = 0`, `a + ++a` vaut 1 et `++a + a` vaut 2.
- **Opérateur conditionnel** : `condition ? vrai : faux`.
- **[[Transtypage]]** : implicite (automatique) si le type d'arrivée suffit, explicite (fait par le programmeur) sinon.
- **Structures de contrôle** : `if` / `else`, `switch` (types `char`, `byte`, `short`, `int`, `default` optionnel), `while`, `do-while` (au moins une exécution), `for` (initialisation, condition, itération ; quand le nombre d'itérations est connu). `break` sort de la boucle, `continue` saute la fin de l'itération.
- **Méthode `main`** : toute application doit en avoir une, exécutée en premier. Le fichier porte le nom de la classe (`Premier.java`).
- **Compilation** : `javac Premier.java` produit `Premier.class` qui contient le bytecode, puis `java Premier` l'exécute.
- **Tableaux** : `type[] nom = new type[taille]` (matrices : `new type[t1][t2]`), indices de 0 à taille − 1, initialisation par `{...}`, taille par `.length`. Exemple de l'aire d'un cercle avec `args[0]` et `Double.parseDouble`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les images 2 et 23 ont été ouvertes, les autres sont lues par leur transcription.

1. **« ELSE IF N'EXISTE PAS EN JAVA »** (complément). **À corriger avant un examen.** C'est faux : `else if` s'écrit en Java, c'est un `else` suivi d'un `if`. L'image du cours ne montre d'ailleurs que `if` et `if/else`.
2. **`valeurs.length` vaut 4** : image ouverte, le cours écrit bien « → 4 » pour le tableau `{ 5, 2, 4, 8, 9 }`, qui a 5 éléments. La bonne valeur est 5 (complément). **À corriger avant un examen.** Les deux lignes suivantes (2 et 3 pour la matrice `{{1,2,3},{4,5,6}}`) sont justes. La ligne `matrice[01.length` est coupée, probablement `matrice[0].length`.
3. **`quotient = (int)(x/y);` marqué « incorrect »** : image ouverte, l'annotation rouge y est bien. Ce cast explicite est pourtant valide en Java (complément) : la transcription avait raison de le signaler. Seule `i = r;` (`float` vers `int` sans cast) est incorrecte.
4. **Cas de `switch`** (complément) : sans `break`, l'exécution continue dans le cas suivant. Le cours écrit seulement « les break sont optionnels ». Le `switch` accepte aussi `String` et les énumérations, absents de la liste du cours.
5. **« break casse les boucles for, while et while-do »** : il faut lire `do-while`.
6. **Guillemets et typographie** : `“Bonjour Monde”` aux guillemets courbes et `Systemt.out` sont des coquilles de la source ; `Final` avec majuscule dans le texte, `final` dans le code.
7. **Tableau des types** : « boolean 1 bit » est une simplification, le cours ne dit rien de plus. Les exposants de `int` et `long` ($-2^{31}$, $-2^{63}$) sont déduits de la transcription et non vérifiés.
8. **Exemple `do { ... } while (x < 10)`** : la transcription le qualifie d'erreur de portée, et c'est l'intention du cours (texte au-dessus de l'image).
