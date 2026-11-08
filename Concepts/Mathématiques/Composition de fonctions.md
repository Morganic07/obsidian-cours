---
type: concept
tags:
  - year1
aliases:
  - composée de fonctions
  - fonction composée
  - composée
  - composition des fonctions
  - composée de deux applications
  - matrice de la composée
matieres:
  - Analyse Maths
  - Outil Maths
  - Algèbre Linéaire
sources:
  - "[[4 - dérivabilité|Chp4 - dérivabilité]]"
  - "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]"
  - "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]"
  - "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]"
  - "[[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2]]"
  - "[[4 - Algèbre linéaire|chp4]]"
maj: 2026-11-08
---

Pour $f : X \to Y$ et $g : Y \to Z$, avec l'image de $f$ contenue dans le domaine de $g$, $(g \circ f)(x) = g(f(x))$.

**Analyse Maths** : les limites et la continuité passent à la composée ; la dérivée est $(u \circ v)' = v' \times (u' \circ v)$ [[Erreurs du cours#^e-composition-de-fonctions|✎]] ; la composée de fonctions de classe $\mathcal{C}^n$ est de classe $\mathcal{C}^n$.

**Outil Maths** : le TD 4 relie composée, injectivité et surjectivité : si $g \circ f$ est surjective, $g$ l'est ; si $g \circ f$ est injective, $f$ l'est. Le DS2 fait aussi calculer des composées et utilise « $g \circ f$ surjective implique $g$ surjective ».

**Algèbre Linéaire** : la composée de deux applications linéaires est linéaire : si $f \in L(E,F)$ et $g \in L(F,G)$, alors $g \circ f \in L(E,G)$, et $M_{g \circ f} = M_g \times M_f$. [[Erreurs du cours#^e-composition-de-fonctions|✎]]

Notion parente : [[Application (mathématiques)]]. Voir aussi : [[Dérivabilité]], [[Injectivité et surjectivité]], [[Limite et continuité]], [[Fonction identité]], [[Bijection]], [[Produit matriciel]], [[Matrice d'une application linéaire]].

Résumés : [[0 - rappels pdf]], [[4 - dérivabilité]], [[4 - pdf]], [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire]], [[4 - Algèbre linéaire]]
