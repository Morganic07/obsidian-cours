---
type: source
tags:
  - year1
sources:
  - "[[chp2|chp2 (Algèbre)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[chp2|chp2 (Algèbre)]], dans [[Algèbre linéaire (matière)]] : chapitre 2, applications linéaires et [[Morphisme|morphismes]] d'espaces vectoriels. En cas d'écart, le cours fait foi.

## Application linéaire

Une application est linéaire si elle respecte les combinaisons linéaires.

**Définition.** Soit $f : E \to F$, avec $E$ et $F$ deux espaces vectoriels.
$$f \text{ linéaire} \iff \forall (x,y) \in E^2,\ \forall (\alpha, \beta) \in \mathbb{K}^2,\ f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$$

- Conséquence : $f(0_E) = 0_F$.
- $L(E, F)$ désigne l'ensemble des [[Transformation linéaire|applications linéaires]] de $E$ dans $F$.
- **[[Homothétie]]** : soit $E$ un espace vectoriel et $\lambda \in \mathbb{R}$ ; l'homothétie de rapport $\lambda$ est $f \in L(E)$, $f(x) = \lambda x$.

### Propriétés de la composition

- Si $f \in L(E,F)$ et $g \in L(F,G)$, la composée est dans $L(E,G)$ (le cours écrit $f \circ g$, voir les points à vérifier).
- Si $f$ et $g$ sont des endomorphismes de $E$, $f \circ g$ est un endomorphisme de $E$.
- Si $f$ est un automorphisme de $E$, $f^{-1}$ est un automorphisme de $E$.
- Si $f$ et $g$ sont des automorphismes, $f \circ g$ est un automorphisme de $E$.
- Si $f \circ g$ est un automorphisme, elle admet une [[Bijection|bijection réciproque]] $(f \circ g)^{-1}$, automorphisme de $E$. Le cours l'illustre par un dessin $E \to E \to E$ avec les flèches $f$, $g$, $f^{-1}$, $g^{-1}$ (disposition perdue). Il écrit : « Attention : $(f \circ g)^{-1} = f^{-1}(g^{-1}(x))$ » (voir les points à vérifier).

### Propriétés de distributivité

Soient $(f, g, h) \in L(E)^3$ :

- $(f + g) \circ h = f \circ h + g \circ h \in L(E)$ ;
- $h \circ (f + g) = h \circ f + h \circ g \in L(E)$ ;
- $f^n = f \circ f \circ \dots \circ f = f^{n-1} \circ f = f \circ f^{n-1} \in L(E)$ ;
- $f^0 = \text{Id}_E$, avec $\text{Id}(x) = x$ ([[Fonction identité]]).

## Morphismes

|  | $E$ dans $F$ | $E$ dans $E$ |
|---|---|---|
| $f$ linéaire | Homomorphisme | Endomorphisme |
| $f$ linéaire et bijective | Isomorphisme ($f^{-1} \in L(F,E)$) | Automorphisme |

- $L(E)$ : ensemble des endomorphismes de $E$ (abréviation de $L(E,E)$).
- [[Groupe linéaire|$GL(E)$]] : ensemble des automorphismes de $E$ (groupe linéaire).

### Propriétés des ensembles d'applications linéaires

- $L(E,F)$ est stable par combinaison linéaire : si $f, g \in L(E,F)$, alors $\alpha f + \beta g \in L(E,F)$.
- $L(E,F)$ est un espace vectoriel ; $L(E)$ est un espace vectoriel.
- $GL(E)$ n'est **pas** un espace vectoriel.

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

### Théorème du rang

[[Théorème du rang]] : soit $f \in L(E,F)$, avec $E$ de [[Dimension (algèbre linéaire)|dimension finie]] :
$$\dim E = \text{rg}(f) + \dim \text{Ker}(f)$$

- $\text{rg} f = \dim \text{Im}(f) = \dim \text{vect}(f(e_1), \dots, f(e_n))$ (voir [[Rang d'une matrice]]).
- $\text{rg}(f) = 0 \iff \text{Im}(f) = \{0\}$ : $f$ est l'application nulle.
- Le cours écrit : « $\dim E = \dim F \Rightarrow f$ bijective, injective et surjective » (voir les points à vérifier).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« dim E = dim F ⇒ f bijective, injective et surjective »** : faux tel quel, car l'application nulle est un contre-exemple. L'énoncé juste est : si $\dim E = \dim F$, alors injective, surjective et bijective sont équivalentes (complément). **À corriger avant un examen.**
2. **Inverse d'une composée** : le cours écrit $(f \circ g)^{-1} = f^{-1}(g^{-1}(x))$. L'ordre s'inverse : $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$ (complément). **À corriger avant un examen.**
3. **Composition** : avec $f \in L(E, F)$ et $g \in L(F, G)$, l'application de $L(E, G)$ est $g \circ f$, et non $f \circ g$.
4. **Vocabulaire** : « stable par application linéaire » désigne la stabilité par combinaison linéaire, et « endomorphisme nul » l'application nulle, qui n'est un endomorphisme que si $E = F$.
5. **Isomorphisme** : le tableau du cours écrit $f^{-1} \in L(E,F)$ ; la réciproque va de $F$ dans $E$, donc $f^{-1} \in L(F,E)$ (complément).
6. **Théorème sur vect** : le cours écrit « vect($e_1, \dots, e_n$) l'ev engendré par F » ; il s'agit du sev de $E$ engendré par les $e_i$.
