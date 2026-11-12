---
type: concept
tags: [year4]
aliases: [comparaison de flottants, epsilon de comparaison, floating-point comparison, tolérance de comparaison]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp2/2.4.c|2.4.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un [[Nombre à virgule flottante|nombre à virgule flottante]] (`float`, `double`) est stocké en binaire selon la [[Norme IEEE 754|norme IEEE 754]]. Seules les fractions dont le dénominateur est une puissance de 2 (0,5 ; 0,25 ; 0,375…) y sont exactes ; 0,1, 1/3 ou −1/3 n'y sont qu'approchés, et chaque opération ajoute une erreur d'arrondi. Tester l'égalité de deux flottants avec `==` est donc fragile :

```c
double x = 0.1 + 0.2;
printf("%d\n", x == 0.3);   // affiche 0 : x vaut 0.30000000000000004…
```

On compare plutôt l'écart à une **tolérance** $\varepsilon$, avec la valeur absolue `fabs` de `<math.h>` ([[Valeur absolue]]) :

- tolérance **absolue** : `fabs(x - y) < 1e-9`, adaptée quand les valeurs sont de l'ordre de 1 ;
- tolérance **relative** : `fabs(x - y) <= eps * fmax(fabs(x), fabs(y))`, qui s'adapte à la taille des valeurs (un écart de $10^{-9}$ n'a pas le même sens pour $10^{-12}$ et pour $10^{12}$).

Les constantes `FLT_EPSILON` et `DBL_EPSILON` (`<float.h>`) donnent l'écart entre 1 et le flottant représentable suivant : environ $1{,}19 \times 10^{-7}$ pour un `float`, $2{,}22 \times 10^{-16}$ pour un `double`. Elles servent d'échelle pour choisir `eps`, pas de tolérance universelle. [[GCC]] signale les comparaisons `==` entre flottants avec l'option `-Wfloat-equal`.

Quand l'exactitude compte (monnaie, fractions), on évite les flottants : entiers de centimes, nombres rationnels représentés par un numérateur et un dénominateur, ou types décimaux.

## Dans le cours

- [[tp2]] : le programme 2.4 vérifie la solution d'une [[Équation du premier degré|équation du premier degré]] par `a*x+b==0` avec des `float` ; pour $3x + 1 = 0$, la réponse `-0.333333` est déclarée fausse, parce que $3 \times (-0{,}333333) + 1$ ne vaut pas exactement 0.

Voir aussi : [[Norme IEEE 754]], [[Nombre à virgule flottante]], [[Opérateur de comparaison]].
