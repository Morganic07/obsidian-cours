---
type: source
tags:
  - year1
sources:
  - "[[chp1|chp1 (Algèbre)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[chp1|chp1 (Algèbre)]], dans [[Algèbre linéaire (matière)]] : chapitre 1, espaces vectoriels et sous-espaces vectoriels. En cas d'écart, le cours fait foi.

## Espace vectoriel et sous-espace vectoriel

### Définitions

| $E$ est un $\mathbb{K}$-[[Espace vectoriel\|espace vectoriel]] si : | $F$ est un [[Sous-espace vectoriel\|sous-espace vectoriel]] (sev) de $E$ si : |
|---|---|
| **Une loi interne** $+$ de $E \times E$ dans $E$ : commutative et associative ; il existe $0_E$, élément neutre, tel que $u + 0_E = u$ ; pour tout $x$, il existe $y$ tel que $x + y = 0_E$ | $0_E \in F$ |
| **Une loi externe** $\times$ de $\mathbb{K} \times E$ dans $E$ : $\forall (a,b) \in \mathbb{K}^2, \forall x \in E$, $(a+b)x = ax + bx$ ; $\forall a \in \mathbb{K}, \forall (x,y) \in E^2$, $a(x+y) = ax + ay$ ; $\forall x \in E$, $1 \cdot x = x$ | $\forall (x,y) \in F^2$, $x + y \in F$ ; $\forall (\lambda, x) \in \mathbb{K} \times F$, $\lambda x \in F$ |

Espaces vectoriels de référence : $\mathbb{R}^n$, $\mathbb{C}^n$, $\mathbb{K}[X]$ (polynômes), $\mathbb{R}^{\mathbb{N}}$ (suites).

### Théorème (opérations sur les sev)

Soient $F$ et $G$ deux sev de $E$ :

- $F \cap G$ est un sev de $E$ ;
- $F \cup G$ n'est **pas forcément** un sev ;
- « $F \setminus E$ » n'est **jamais** un sev (voir les points à vérifier).

### Dimension d'un sev

Soit $E$ un espace vectoriel et $F$ un sev de $E$, avec $\dim E = n$ et $\dim F = p$. Alors $p \le n$ (le cours écrit $p < n$), et **si $p = n$ alors $E = F$**.

## Familles de vecteurs

| [[Indépendance linéaire\|Famille libre]] de $E$ : vecteurs linéairement indépendants | [[Espace engendré\|Famille génératrice]] de $E$ : tout vecteur de $E$ est [[Combinaison linéaire\|combinaison linéaire]] des vecteurs de la famille |
|---|---|
| $\lambda_1 v_1 + \dots + \lambda_n v_n = 0 \Rightarrow \lambda_1 = \lambda_2 = \dots = \lambda_n = 0$ | $\forall x \in E$, $x = \lambda_1 v_1 + \dots + \lambda_n v_n$ avec $\lambda_1, \dots, \lambda_n \in \mathbb{K}$ et $v_1, \dots, v_n$ dans la famille |
| Une famille non libre est **liée** | S'il existe une famille génératrice (finie), $E$ est de [[Dimension (algèbre linéaire)\|dimension]] **finie** ; sinon $E$ est de dimension infinie |
| La décomposition d'un vecteur sur une famille libre est **unique** | |

- **[[Base (algèbre linéaire)|Base]] = libre + génératrice.**
- Si une famille est une base, il existe une [[Bijection|bijection]] qui associe à tout vecteur ses composantes dans cette base.

### Propriétés (inclusion de familles)

Soient $X$ et $Y$ deux familles de vecteurs de $E$ avec $X \subset Y$ :

- si $Y$ est libre, alors $X$ est libre ;
- si $X$ est génératrice, alors $Y$ est génératrice ;
- si $X$ est génératrice et si $x \in X$ est combinaison linéaire des vecteurs de $X \setminus \{x\}$, alors $X \setminus \{x\}$ est encore génératrice ;
- si $X$ est libre et si $x \in E$ n'est pas combinaison linéaire des vecteurs de $X$, alors $X \cup \{x\}$ est libre ;
- toute famille dont l'un des vecteurs est nul est liée. Donc si $(x_1, \dots, x_n)$ est libre, chaque $x_i \neq 0$.

### Propriétés (dimension $n$)

Dans un espace vectoriel de dimension $n$ :

- toute base possède $n$ vecteurs ;
- toute famille génératrice possède au moins $n$ éléments ;
- toute famille libre possède au plus $n$ éléments ;
- une famille libre ou génératrice qui possède exactement $n$ éléments est une base.

Le cours l'illustre par un dessin (axe du nombre d'éléments : en dessous de $n$, les familles libres ; au-dessus, les génératrices ; à $n$, les bases). Sa disposition est perdue à l'export ; il n'en reste que les mots « n ; Nombre d'éléments ; > n ; < n ; base ; génératrice ; libre ».

### Théorèmes d'extraction et de base incomplète

Soit $E$ un espace vectoriel de dimension $n$, $E \neq \{0\}$ :

- **Extraction** : de toute famille génératrice, on peut extraire une famille libre génératrice, donc une base.
- **[[Théorème de la base incomplète]]** : toute famille libre peut être complétée en une base.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Dimension d'un sev** : le cours écrit $p < n$, puis « si $p = n$ alors $E = F$ ». Il faut lire $p \le n$.
2. **« F\E jamais sev »** : l'énoncé attendu porte sans doute sur $E \setminus F$, qui ne contient pas $0_E$ (complément).
3. **Extraction** : le cours écrit « extraire une famille libre donc une base » ; la famille extraite doit être libre **et** génératrice pour être une base (complément).
