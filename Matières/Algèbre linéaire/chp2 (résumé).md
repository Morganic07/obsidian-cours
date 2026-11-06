---
type: source
tags: [year1]
sources: ["[[Cours/Year 1/Algèbre Linéaire/Cours/chp2|chp2 (Algèbre)]]"]
maj: 2026-11-05
---

Résumé de [[Cours/Year 1/Algèbre Linéaire/Cours/chp2|chp2 (Algèbre)]], dans [[Algèbre linéaire (matière)]]. En cas d'écart, le cours fait foi.

## Contenu

- **[[Transformation linéaire|Application linéaire]]** : $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$, donc $f(0_E) = 0_F$. L'homothétie $f(x) = \lambda x$ en est un exemple.
- **[[Morphisme|Morphismes]]** : homomorphisme, endomorphisme, isomorphisme, automorphisme. $L(E, F)$ et $L(E)$ sont des espaces vectoriels, mais pas $GL(E)$.
- **Image** : Im$(f)$ est un sev de $F$, et Im$(f) = \text{vect}(f(v_1), \dots, f(v_n))$ pour une base $(v_i)$. $f$ est [[Injectivité et surjectivité|surjective]] si et seulement si Im$(f) = F$.
- **[[Espace nul|Noyau]]** : Ker $f$ est un sev de $E$, et $f$ est injective si et seulement si Ker $f = \{0\}$.
- **Effet sur les familles** : une application injective conserve les familles libres, une surjective les familles génératrices, une bijective les bases.
- **[[Rang d'une matrice|Théorème du rang]]** : $\dim E = \text{rg}(f) + \dim \text{Ker}(f)$, avec $\text{rg}(f) = \dim \text{Im}(f)$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« dim E = dim F ⇒ f bijective, injective et surjective »** : faux tel quel, car l'application nulle est un contre-exemple. L'énoncé juste est : si $\dim E = \dim F$, alors injective, surjective et bijective sont équivalentes (complément). **À corriger avant un examen.**
2. **Inverse d'une composée** : le cours écrit $(f \circ g)^{-1} = f^{-1}(g^{-1}(x))$. L'ordre s'inverse : $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$ (complément). **À corriger avant un examen.**
3. **Composition** : avec $f \in L(E, F)$ et $g \in L(F, G)$, l'application de $L(E, G)$ est $g \circ f$, et non $f \circ g$.
4. **Vocabulaire** : « stable par application linéaire » désigne la stabilité par combinaison linéaire, et « endomorphisme nul » l'application nulle, qui n'est un endomorphisme que si $E = F$.
