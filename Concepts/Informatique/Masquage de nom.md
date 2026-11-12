---
type: concept
tags: [year4]
aliases: [name shadowing, shadowing, masquage de variable, variable masquée]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp7/7.3.c|7.3.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : il y a masquage de nom (*shadowing*) quand un nom déclaré dans une [[Portée d'une variable|portée]] intérieure (variable locale, paramètre, variable d'une boucle) porte le même [[Identificateur (programmation)|identificateur]] qu'une entité d'une portée englobante (variable globale, fonction, attribut, variable d'un [[Bloc d'instructions|bloc]] extérieur). Dans la portée intérieure, le nom désigne la déclaration **la plus proche** ; l'autre entité y devient inaccessible par ce nom, sans être détruite ni modifiée.

```c
int x = 1;                 // variable globale
void f(void) {
    int x = 2;             // masque la globale dans f
    printf("%d\n", x);     // affiche 2
    { int x = 3; }         // masque encore, dans ce bloc seulement
}
```

C'est légal en [[Langage C|C]] et en [[Langage C++|C++]], mais source de confusion : on croit modifier une variable et l'on en modifie une autre. Cas typique en C++, un paramètre de [[Constructeur (programmation)|constructeur]] qui porte le nom d'un attribut : `x = x;` affecte le paramètre à lui-même et laisse l'attribut non initialisé. On lève l'ambiguïté avec le [[Pointeur this|pointeur `this`]] (`this->x = x;`), avec la [[Liste d'initialisation|liste d'initialisation]] (`: x(x)`), ou avec l'[[Opérateur de résolution de portée|opérateur de résolution de portée]] `::x` pour une variable globale.

L'[[Option de compilation|option]] `-Wshadow` de [[GCC]] et de [[Clang]] signale les masquages ; elle n'est pas incluse dans `-Wall` ni `-Wextra`. Le remède le plus simple est de choisir des noms distincts.

## Dans le cours

- [[tp7]] : dans la procédure `moyenne` (7.3), la variable locale s'appelle aussi `moyenne` et masque le nom de la fonction à l'intérieur de son bloc.
- [[formation C++]] : le constructeur `Point(int x, int y)` (programme 6) montre qu'un paramètre de même nom que l'attribut le masquerait.

Voir aussi : [[Portée d'une variable]], [[Pointeur this]], [[Espace de noms (namespace)]].
