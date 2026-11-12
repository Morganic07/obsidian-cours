---
type: concept
tags: [year4]
aliases: [return, return statement, instruction de retour, valeur de retour, type de retour]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp6/6.1.c|6.1.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : l'instruction `return` termine l'exécution d'une fonction et rend la main à l'appelant, à l'endroit de l'[[Appel de fonction|appel]]. Suivie d'une [[Expression (programmation)|expression]], elle transmet sa valeur, convertie dans le **type de retour** déclaré dans l'en-tête de la fonction ; l'appel est alors lui-même une expression qui vaut cette valeur.

```c
int maximum(int a, int b) {
    if (a > b)
        return a;        // sort immédiatement : la suite n'est pas exécutée
    return b;
}
void affiche(int x) {
    if (x < 0) return;   // fonction void : return sans valeur
    printf("%d\n", x);
}
```

Règles en [[Langage C|C]] et en [[Langage C++|C++]] :

- une fonction peut avoir plusieurs `return` ; le premier exécuté termine la fonction, ce qui permet de sortir tôt d'une boucle ;
- une fonction `void` ([[Fonction et procédure|procédure]]) n'a pas de valeur de retour ; `return;` y est permis pour sortir avant la fin ;
- une fonction non `void` doit exécuter un `return valeur;` sur **tous** ses chemins. En C, si l'exécution atteint l'accolade finale sans `return` et que l'appelant utilise la valeur, le [[Comportement indéfini|comportement est indéfini]] (C17, § 6.9.1, al. 12) ; en C++, il l'est dès que l'accolade est atteinte, même si la valeur n'est pas utilisée. [[GCC]] le signale avec `-Wall` : `warning: control reaches end of non-void function` ([[Avertissement de compilation]]) ;
- seule la [[Fonction main (C et C++)|fonction `main`]] fait exception : atteindre sa fin équivaut à `return 0;` (depuis C99 en C), et la valeur renvoyée devient le [[Code de retour|code de retour]] du processus ;
- une fonction ne renvoie qu'**une** valeur. Pour en rendre plusieurs, on renvoie une [[Structure (struct)|structure]] ou un objet, ou l'on passe des adresses en paramètre ([[Passage de paramètres]]) ; en C++, `std::pair` et `std::tuple` ([[Paire et tuple (C++)]]). `return x, y;` ne renvoie que `y` ([[Opérateur virgule]]) ;
- ne jamais renvoyer l'adresse d'une variable locale, détruite à la sortie ([[Pointeur pendant]]).

`return` n'est pas une fonction : les parenthèses de `return(x);` sont celles d'une expression, inutiles.

## Dans le cours

- [[tp6]] : `puissance` (6.1) renvoie son résultat à `printf` ; `NombreOrdonnes` (6.2) et `volume` (6.3) n'avaient pas de `return` sur tous leurs chemins, corrigés dans la fiche.
- [[formation C++]] : `return x, y;` dans `getCoord()` (programme 10) ne renvoie que `y`.
- [[1 - basiques]] : `return` figure parmi les mots réservés de « rupture de séquence ».

Voir aussi : [[Fonction et procédure]], [[Appel de fonction]], [[Pile d'exécution]], [[Code de retour]].
