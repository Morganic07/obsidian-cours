---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp1 .docx|chp1 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp1 .docx|chp1 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 1, espaces vectoriels et sous-espaces vectoriels.

## Espace vectoriel et sous-espace vectoriel

### Définitions

| $E$ est un $\mathbb{K}$-[[Espace vectoriel\|espace vectoriel]] si : | $F$ est un [[Sous-espace vectoriel\|sous-espace vectoriel]] (sev) de $E$ si : |
|---|---|
| **Une loi interne** $+$ de $E \times E$ dans $E$ : commutative et associative ; il existe $0_E$, élément neutre, tel que $u + 0_E = u$ ; pour tout $x$, il existe $y$ tel que $x + y = 0_E$ | $0_E \in F$ |
| **Une loi externe** $\times$ de $\mathbb{K} \times E$ dans $E$ : $\forall (a,b) \in \mathbb{K}^2, \forall x \in E$, $(a+b)x = ax + bx$ ; $\forall a \in \mathbb{K}, \forall (x,y) \in E^2$, $a(x+y) = ax + ay$ ; $\forall x \in E$, $1 \cdot x = x$ | $\forall (x,y) \in F^2$, $x + y \in F$ ; $\forall (\lambda, x) \in \mathbb{K} \times F$, $\lambda x \in F$ |

La loi interne fait de $(E, +)$ un **groupe commutatif** ; l'élément $y$ tel que $x + y = 0_E$ est l'opposé de $x$, noté $-x$. La liste des axiomes de la loi externe se complète par l'**associativité mixte** : $\forall (a,b) \in \mathbb{K}^2, \forall x \in E$, $a(bx) = (ab)x$. Le corps $\mathbb{K}$ est $\mathbb{R}$ ou $\mathbb{C}$ ; ses éléments s'appellent les **scalaires**, ceux de $E$ les **vecteurs**. [[Complément hors du cours|ⓘ]]

**En pratique**, pour montrer que $F$ est un sev, on vérifie en une fois : $F \subset E$, $0_E \in F$ et $\forall (x,y) \in F^2, \forall (\lambda, \mu) \in \mathbb{K}^2$, $\lambda x + \mu y \in F$ (stabilité par [[Combinaison linéaire|combinaison linéaire]]). Un sev est lui-même un espace vectoriel : c'est souvent le moyen le plus court de prouver qu'un ensemble est un espace vectoriel, en le plaçant dans un espace connu. [[Complément hors du cours|ⓘ]]

Exemple : $F = \{(x,y,z) \in \mathbb{R}^3 \mid x + y + z = 0\}$ est un sev de $\mathbb{R}^3$ (il contient $0$, et si $x+y+z = 0$ et $x'+y'+z' = 0$, alors $\lambda(x+y+z) + \mu(x'+y'+z') = 0$). Contre-exemple : la droite $\{(x,y) \in \mathbb{R}^2 \mid x + y = 1\}$ ne contient pas $(0,0)$, ce n'est pas un sev. Règle à retenir : un ensemble défini par des équations linéaires **sans terme constant** est un sev. [[Complément hors du cours|ⓘ]]

Espaces vectoriels de référence : $\mathbb{R}^n$, $\mathbb{C}^n$, $\mathbb{K}[X]$ (polynômes), $\mathbb{R}^{\mathbb{N}}$ (suites).

Leurs dimensions : $\dim \mathbb{K}^n = n$, de **base canonique** $e_1 = (1, 0, \dots, 0), \dots, e_n = (0, \dots, 0, 1)$ ; $\mathbb{K}_n[X]$ (polynômes de degré au plus $n$) est de dimension $n + 1$, de base canonique $(1, X, \dots, X^n)$ ; $\mathbb{K}[X]$ et $\mathbb{R}^{\mathbb{N}}$ sont de dimension infinie. Autres exemples : $\mathcal{M}_{n,p}(\mathbb{K})$, les [[Matrice|matrices]] à $n$ lignes et $p$ colonnes (dimension $np$), et les fonctions de $\mathbb{R}$ dans $\mathbb{R}$. [[Complément hors du cours|ⓘ]]

### Théorème (opérations sur les sev)

Soient $F$ et $G$ deux sev de $E$ :

- $F \cap G$ est un sev de $E$ ;
- $F \cup G$ n'est **pas forcément** un sev ;
- « $F \setminus E$ » n'est **jamais** un sev.

Précisément, $F \cup G$ est un sev **si et seulement si** $F \subset G$ ou $G \subset F$. Exemple : dans $\mathbb{R}^2$, l'union des deux axes contient $(1,0)$ et $(0,1)$ mais pas leur somme $(1,1)$. Un complémentaire $E \setminus F$ n'est jamais un sev, puisqu'il ne contient pas $0_E$. [[Complément hors du cours|ⓘ]]

Le bon substitut de l'union est la **somme** $F + G = \{x + y \mid x \in F, y \in G\}$ : c'est le plus petit sev contenant $F$ et $G$, c'est-à-dire $\text{vect}(F \cup G)$ ([[Espace engendré]]). Quand $F \cap G = \{0\}$, la somme est dite **directe**, notée $F \oplus G$, et toute décomposition $x + y$ est unique ; si de plus $F \oplus G = E$, $F$ et $G$ sont **supplémentaires** (voir [[Somme directe]], vue au chapitre 7). En dimension finie, la **formule de Grassmann** relie ces dimensions : $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$. [[Complément hors du cours|ⓘ]]

### Dimension d'un sev

Soit $E$ un espace vectoriel et $F$ un sev de $E$, avec $\dim E = n$ et $\dim F = p$. Alors $p \le n$, et **si $p = n$ alors $E = F$**. [[Erreurs du cours#^e-1-algebre-lineaire|✎]]

## Familles de vecteurs

| [[Indépendance linéaire\|Famille libre]] de $E$ : vecteurs linéairement indépendants | [[Espace engendré\|Famille génératrice]] de $E$ : tout vecteur de $E$ est [[Combinaison linéaire\|combinaison linéaire]] des vecteurs de la famille |
|---|---|
| $\lambda_1 v_1 + \dots + \lambda_n v_n = 0 \Rightarrow \lambda_1 = \lambda_2 = \dots = \lambda_n = 0$ | $\forall x \in E$, $x = \lambda_1 v_1 + \dots + \lambda_n v_n$ avec $\lambda_1, \dots, \lambda_n \in \mathbb{K}$ et $v_1, \dots, v_n$ dans la famille |
| Une famille non libre est **liée** | S'il existe une famille génératrice (finie), $E$ est de [[Dimension (algèbre linéaire)\|dimension]] **finie** ; sinon $E$ est de dimension infinie |
| La décomposition d'un vecteur sur une famille libre est **unique** | |

- Cas particuliers : une famille d'un seul vecteur $(v)$ est libre si et seulement si $v \neq 0$ ; une famille de deux vecteurs $(u, v)$ est libre si et seulement si $u$ et $v$ ne sont pas **colinéaires** (aucun n'est multiple de l'autre). Une famille est liée si et seulement si l'un de ses vecteurs est combinaison linéaire des autres. [[Complément hors du cours|ⓘ]]
- L'ensemble des combinaisons linéaires de $v_1, \dots, v_p$ est un sev, noté $\text{vect}(v_1, \dots, v_p)$ ([[Espace engendré|sous-espace engendré]]) : c'est le plus petit sev qui contient ces vecteurs, et la famille est génératrice de $E$ exactement quand $\text{vect}(v_1, \dots, v_p) = E$. La dimension de $\text{vect}(v_1, \dots, v_p)$ s'appelle le **rang** de la famille. [[Complément hors du cours|ⓘ]]
- Exemple : dans $\mathbb{R}^2$, $u = (1, 2)$ et $v = (3, 1)$. Si $\lambda u + \mu v = 0$, alors $\lambda + 3\mu = 0$ et $2\lambda + \mu = 0$, d'où $\mu = -2\lambda$ puis $\lambda - 6\lambda = 0$ : $\lambda = \mu = 0$. La famille est libre, et comme elle a 2 vecteurs dans un espace de dimension 2, c'est une base. Tester la liberté revient toujours à résoudre un [[Système linéaire homogène|système homogène]] (voir le chapitre 3). [[Complément hors du cours|ⓘ]]
- **[[Base (algèbre linéaire)|Base]] = libre + génératrice.**
- Si une famille est une base, il existe une [[Bijection|bijection]] qui associe à tout vecteur ses composantes dans cette base.
- Ces composantes sont les [[Coordonnées dans une base|coordonnées]] du vecteur : si $B = (e_1, \dots, e_n)$ est une base, tout $x$ s'écrit de façon unique $x = x_1 e_1 + \dots + x_n e_n$, et la bijection $x \mapsto (x_1, \dots, x_n)$ va de $E$ dans $\mathbb{K}^n$. Elle est linéaire : tout espace de dimension $n$ « se comporte comme » $\mathbb{K}^n$ (ils sont isomorphes, voir le chapitre 2). Exemple : dans la base $(1, X, X^2)$ de $\mathbb{R}_2[X]$, le polynôme $3 - X + 2X^2$ a pour coordonnées $(3, -1, 2)$. [[Complément hors du cours|ⓘ]]

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

Conséquence pratique : pour montrer qu'une famille de $n$ vecteurs est une base d'un espace de dimension $n$, il suffit de vérifier **une seule** des deux propriétés, en général la liberté. Et toute famille de plus de $n$ vecteurs est forcément liée : dans $\mathbb{R}^3$, quatre vecteurs sont toujours liés. [[Complément hors du cours|ⓘ]]

Le cours l'illustre par un dessin (axe du nombre d'éléments : en dessous de $n$, les familles libres ; au-dessus, les génératrices ; à $n$, les bases). Sa disposition est perdue à l'export ; il n'en reste que les mots « n ; Nombre d'éléments ; > n ; < n ; base ; génératrice ; libre ».

### Théorèmes d'extraction et de base incomplète

Soit $E$ un espace vectoriel de dimension $n$, $E \neq \{0\}$ :

- **Extraction** : de toute famille génératrice, on peut extraire une famille libre génératrice, donc une base. [[Erreurs du cours#^e-1-algebre-lineaire|✎]]
- **[[Théorème de la base incomplète]]** : toute famille libre peut être complétée en une base.

Méthode pour compléter : on ajoute, un par un, des vecteurs d'une famille génératrice connue (par exemple la base canonique) qui ne sont pas combinaisons linéaires des vecteurs déjà retenus ; d'après la propriété d'inclusion ci-dessus, la famille reste libre à chaque ajout, et on s'arrête à $n$ vecteurs. Exemple : $(1, 1, 0)$ dans $\mathbb{R}^3$ se complète par $e_2 = (0,1,0)$ puis $e_3 = (0,0,1)$. Le théorème a pour conséquence que tout sev $F$ d'un espace de dimension finie admet un **supplémentaire** : on complète une base de $F$ en une base de $E$, et les vecteurs ajoutés engendrent un sev $G$ tel que $E = F \oplus G$. [[Complément hors du cours|ⓘ]]