---
type: concept
tags:
  - year4
aliases:
  - segmentation fault
  - segfault
matieres:
  - C++
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une erreur de segmentation (*segmentation fault*) se produit quand un programme accède à une zone de mémoire qu'il n'a pas le droit d'utiliser, par exemple en déréférençant un [[Pointeur NULL|pointeur nul]] ou invalide, ou en écrivant hors des bornes d'un [[Tableau (programmation)|tableau]] (un débordement de peu d'octets ne la déclenche pas toujours : il corrompt alors la mémoire sans signal). Le matériel détecte l'accès interdit, et le [[Système d'exploitation|système d'exploitation]] termine le processus en lui envoyant le signal `SIGSEGV`.

## Dans le cours

Nommé dans [[1 - basiques|Chp1 - basiques]] sans définition : le cours cite le *Segmentation fault* comme exemple de plantage brutal à l'exécution, que le [[Typage statique]] aide à éviter.

Voir aussi : [[Typage statique]], [[Pointeur et adresse mémoire]].

Résumés : [[1 - basiques]]
