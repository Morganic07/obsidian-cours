---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp2 .docx|chp2 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp2 .docx|chp2 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 2, applications linéaires et [[Morphisme|morphismes]] d'espaces vectoriels.
## Application linéaire

Une application est linéaire si elle respecte les combinaisons linéaires.

**Définition.** Soit $f : E \to F$, avec $E$ et $F$ deux espaces vectoriels.
$$f \text{ linéaire} \iff \forall (x,y) \in E^2,\ \forall (\alpha, \beta) \in \mathbb{K}^2,\ f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$$

- Conséquence : $f(0_E) = 0_F$.

Pourquoi : $f(0_E) = f(0 \cdot 0_E) = 0 \cdot f(0_E) = 0_F$. La contraposée sert de test rapide : si $f(0) \neq 0$, $f$ n'est pas linéaire. Exemples : $f(x, y) = (x + y, 2x)$ est linéaire de $\mathbb{R}^2$ dans $\mathbb{R}^2$ (chaque composante est une combinaison linéaire des variables, sans terme constant) ; $g(x, y) = (x + 1, y)$ ne l'est pas, car $g(0,0) = (1, 0)$ ; $h(x) = x^2$ ne l'est pas non plus, car $h(2x) = 4h(x) \neq 2h(x)$. Attention, $f(0) = 0$ ne suffit pas à prouver la linéarité. [[Complément hors du cours|ⓘ]]

Exemples classiques d'applications linéaires : la dérivation $P \mapsto P'$ sur $\mathbb{K}[X]$ ; l'intégration $f \mapsto \int_a^b f(t)\,dt$ sur les fonctions continues, à valeurs dans $\mathbb{R}$ (une application linéaire à valeurs dans $\mathbb{K}$ s'appelle une [[Forme linéaire|forme linéaire]]) ; $X \mapsto AX$ pour une matrice $A$ fixée ; les rotations et symétries du plan centrées en l'origine ([[Transformations géométriques du plan]]). [[Complément hors du cours|ⓘ]]
- $L(E, F)$ désigne l'ensemble des [[Transformation linéaire|applications linéaires]] de $E$ dans $F$.
- **[[Homothétie]]** : soit $E$ un espace vectoriel et $\lambda \in \mathbb{R}$ ; l'homothétie de rapport $\lambda$ est $f \in L(E)$, $f(x) = \lambda x$.

### Propriétés de la composition

- Si $f \in L(E,F)$ et $g \in L(F,G)$, la composée $g \circ f$ est dans $L(E,G)$ ($f$ s'applique en premier). [[Erreurs du cours#^e-2-algebre-lineaire|✎]]
- Si $f$ et $g$ sont des endomorphismes de $E$, $f \circ g$ est un endomorphisme de $E$.
- Si $f$ est un automorphisme de $E$, $f^{-1}$ est un automorphisme de $E$.
- Si $f$ et $g$ sont des automorphismes, $f \circ g$ est un automorphisme de $E$.
- Si $f \circ g$ est un automorphisme, elle admet une [[Bijection|bijection réciproque]] $(f \circ g)^{-1}$, automorphisme de $E$. Le cours l'illustre par un dessin $E \to E \to E$ avec les flèches $f$, $g$, $f^{-1}$, $g^{-1}$ (disposition perdue). Attention à l'ordre : $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$, soit $(f \circ g)^{-1}(x) = g^{-1}(f^{-1}(x))$ : on défait d'abord $f$, appliquée en dernier. [[Erreurs du cours#^e-2-algebre-lineaire|✎]]

### Propriétés de distributivité

Soient $(f, g, h) \in L(E)^3$ :

- $(f + g) \circ h = f \circ h + g \circ h \in L(E)$ ;
- $h \circ (f + g) = h \circ f + h \circ g \in L(E)$ ;
- $f^n = f \circ f \circ \dots \circ f = f^{n-1} \circ f = f \circ f^{n-1} \in L(E)$ ;
- $f^0 = \text{Id}_E$, avec $\text{Id}(x) = x$ ([[Fonction identité]]).

La composition n'est en revanche **pas commutative** : en général $f \circ g \neq g \circ f$. Exemple dans $\mathbb{R}^2$ : avec $f(x, y) = (y, x)$ et $g(x, y) = (x, 0)$, on a $f \circ g(x, y) = (0, x)$ mais $g \circ f(x, y) = (y, 0)$. C'est pourquoi l'ordre compte dans $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$, et pourquoi les identités remarquables du type $(f + g)^2 = f^2 + 2 f \circ g + g^2$ ne valent que si $f$ et $g$ commutent. [[Complément hors du cours|ⓘ]]

Deux familles d'endomorphismes reviennent sans cesse : un **projecteur** vérifie $p \circ p = p$, et une **symétrie** vérifie $s \circ s = \text{Id}_E$ ; si $E = F \oplus G$ ([[Somme directe]]), la projection sur $F$ parallèlement à $G$ envoie $x = x_F + x_G$ sur $x_F$, et la symétrie par rapport à $F$ parallèlement à $G$ l'envoie sur $x_F - x_G$ (voir [[Projecteur]]). [[Complément hors du cours|ⓘ]]

## Morphismes

|  | $E$ dans $F$ | $E$ dans $E$ |
|---|---|---|
| $f$ linéaire | Homomorphisme | Endomorphisme |
| $f$ linéaire et bijective | Isomorphisme ($f^{-1} \in L(F,E)$) | Automorphisme [[Erreurs du cours#^e-2-algebre-lineaire\|✎]] |

- $L(E)$ : ensemble des endomorphismes de $E$ (abréviation de $L(E,E)$).
- [[Groupe linéaire|$GL(E)$]] : ensemble des automorphismes de $E$ (groupe linéaire).

### Propriétés des ensembles d'applications linéaires

- $L(E,F)$ est stable par combinaison linéaire : si $f, g \in L(E,F)$, alors $\alpha f + \beta g \in L(E,F)$.
- $L(E,F)$ est un espace vectoriel ; $L(E)$ est un espace vectoriel.
- $GL(E)$ n'est **pas** un espace vectoriel.

Raison : l'application nulle n'est pas bijective, donc $0 \notin GL(E)$ ; et la somme de deux automorphismes peut ne pas en être un : $\text{Id}_E + (-\text{Id}_E) = 0$. En revanche, $GL(E)$ est un **groupe** pour la composition (d'où son nom) : la composée de deux automorphismes en est un, $\text{Id}_E$ est l'élément neutre et chaque $f$ a un inverse $f^{-1}$. [[Complément hors du cours|ⓘ]]

En dimension finie, $\dim L(E, F) = \dim E \times \dim F$ : une application linéaire est entièrement déterminée par les images des vecteurs d'une base de $E$, et ces images peuvent être choisies librement dans $F$. C'est ce qui permet de la représenter par une [[Matrice d'une application linéaire|matrice]] (chapitre 4). [[Complément hors du cours|ⓘ]]

## Image, noyau, rang

### Image

Soit $f \in L(E,F)$ : $\text{Im}(f) = \{ f(x) \mid x \in E \}$ ([[Image d'une application linéaire]]).

- $\text{Im}(f)$ est un sev de $F$.
- L'image de tout sev de $E$ par $f$ est un sev de $F$.
- $f$ [[Injectivité et surjectivité|surjective]] $\iff f(E) = \text{Im}(f) = F$.

**Propriété.** Si $B = \{v_1, \dots, v_n\}$ est une [[Base (algèbre linéaire)|base]] de $E$, alors
$$\text{Im}(f) = \text{vect}(f(v_1), \dots, f(v_n)),$$
c'est-à-dire l'[[Espace engendré|espace vectoriel engendré]] par $f(v_1), \dots, f(v_n)$.

**Théorème.** Pour toute famille $\{e_1, \dots, e_n\}$ de $E$ :
$$f(\text{vect}(e_1, \dots, e_n)) = \text{vect}(f(e_1), \dots, f(e_n)).$$

**Théorème (effet sur les familles).** Soit $B = \{v_1, \dots, v_n\}$ une famille de $E$ et $B' = \{f(v_1), \dots, f(v_n)\}$ :

- si $f$ est injective et $B$ libre, alors $B'$ est libre dans $F$ ;
- si $f$ est surjective et $B$ génératrice, alors $B'$ est génératrice de $F$ ;
- si $f$ est bijective et $B$ une base, alors $f(B)$ est une base de $F$.

### Noyau

[[Espace nul|Noyau]] de $f$ : $\text{Ker} f = \{ x \in E \mid f(x) = 0 \}$.

- $f$ injective $\iff \text{Ker} f = \{0\}$.
- Pour tout $f \in L(E,F)$, $0 \in \text{Ker} f$, car $f(0) = 0$.
- $\text{Ker} f$ est un sev de $E$.

Pourquoi $\text{Ker} f = \{0\}$ suffit pour l'injectivité : si $f(x) = f(y)$, alors $f(x - y) = f(x) - f(y) = 0$, donc $x - y \in \text{Ker} f$ ; si le noyau est réduit à $\{0\}$, $x = y$. Réciproquement, si $f$ est injective, seul $0$ a pour image $0$. [[Complément hors du cours|ⓘ]]

Exemple de calcul : pour $f(x, y, z) = (x + y,\ y - z)$ de $\mathbb{R}^3$ dans $\mathbb{R}^2$, $\text{Ker} f$ s'obtient en résolvant le système $x + y = 0$, $y - z = 0$ : $y = z$, $x = -z$, donc $\text{Ker} f = \text{vect}((-1, 1, 1))$, de dimension 1. L'image est engendrée par $f(e_1) = (1, 0)$, $f(e_2) = (1, 1)$, $f(e_3) = (0, -1)$, qui engendrent $\mathbb{R}^2$ : $\text{Im} f = \mathbb{R}^2$ et $f$ est surjective mais pas injective. [[Complément hors du cours|ⓘ]]

### Théorème du rang

[[Théorème du rang]] : soit $f \in L(E,F)$, avec $E$ de [[Dimension (algèbre linéaire)|dimension finie]] :
$$\dim E = \text{rg}(f) + \dim \text{Ker}(f)$$

- $\text{rg} f = \dim \text{Im}(f) = \dim \text{vect}(f(e_1), \dots, f(e_n))$ (voir [[Rang d'une matrice]]).
- $\text{rg}(f) = 0 \iff \text{Im}(f) = \{0\}$ : $f$ est l'application nulle.
- Si $\dim E = \dim F$ (finie) : $f$ injective $\iff$ $f$ surjective $\iff$ $f$ bijective. L'égalité des dimensions ne suffit pas seule à rendre $f$ bijective : l'application nulle est un contre-exemple. [[Erreurs du cours#^e-2-algebre-lineaire|✎]]

Vérification sur l'exemple du noyau ci-dessus : $\dim \mathbb{R}^3 = 3 = \text{rg}(f) + \dim \text{Ker}(f) = 2 + 1$. [[Complément hors du cours|ⓘ]]

Conséquences utiles du théorème du rang, pour $f \in L(E, F)$ en dimension finie : [[Complément hors du cours|ⓘ]]
- $\text{rg}(f) \le \min(\dim E, \dim F)$ ;
- $f$ injective $\iff \text{rg}(f) = \dim E$, et $f$ surjective $\iff \text{rg}(f) = \dim F$ ;
- si $\dim E < \dim F$, $f$ ne peut pas être surjective ; si $\dim E > \dim F$, elle ne peut pas être injective (son noyau est non nul) ;
- si $\dim E = \dim F$, en particulier pour un endomorphisme, « injective », « surjective » et « bijective » sont équivalentes (il suffit de vérifier $\text{Ker} f = \{0\}$ pour conclure que $f$ est bijective).

Deux espaces de dimension finie sont **isomorphes** (il existe un isomorphisme entre eux) si et seulement s'ils ont la même dimension : tout espace de dimension $n$ est isomorphe à $\mathbb{K}^n$, par l'application qui associe à un vecteur ses [[Coordonnées dans une base|coordonnées]] dans une base. [[Complément hors du cours|ⓘ]]
