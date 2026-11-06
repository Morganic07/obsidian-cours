---
type: concept
tags: [year1]
aliases: [composée de fonctions, fonction composée, composée, composition des fonctions, composée de deux applications, matrice de la composée]
matieres: [Analyse Maths, Outil Maths, Algèbre Linéaire]
sources: ["[[Chp4 - dérivabilité]]", "[[raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1]]", "[[raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1)]]", "[[raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions]]", "[[chp2]]", "[[chp4]]"]
maj: 2026-11-06
---

Pour $f : X \to Y$ et $g : Y \to Z$, avec l'image de $f$ contenue dans le domaine de $g$, $(g \circ f)(x) = g(f(x))$.

**Analyse Maths** : les limites et la continuité passent à la composée ; la dérivée est $(u \circ v)' = v' \times (u' \circ v)$ ; la composée de fonctions de classe $\mathcal{C}^n$ est de classe $\mathcal{C}^n$.

**Outil Maths** : le TD 4 relie composée, injectivité et surjectivité : si $g \circ f$ est surjective, $g$ l'est ; si $g \circ f$ est injective, $f$ l'est. Le DS2 fait aussi calculer des composées et utilise « $g \circ f$ surjective implique $g$ surjective ».

**Algèbre Linéaire** : la composée de deux applications linéaires est linéaire, et $M_{g \circ f} = M_g \times M_f$.

Notion parente : [[Application (mathématiques)]]. Voir aussi : [[Dérivabilité]], [[Injectivité et surjectivité]], [[Limite et continuité]], [[Fonction identité]], [[Bijection]], [[Produit matriciel]], [[Matrice d'une application linéaire]].

## À vérifier

- Chp4 (dérivabilité) : le tableau écrit « $u \circ v = u(v(x)) = v'(u' \circ v)$ » ; il faut lire $(u \circ v)'$.
- chp2 (Algèbre Linéaire) : avec $f \in L(E,F)$ et $g \in L(F,G)$, le cours écrit « fog ∈ L(E,G) » au lieu de $g \circ f$.

Résumés : [[AnalyseID1 (résumé)]], [[Chp4 - dérivabilité (résumé)]], [[Contrôles (résumé)]], [[Chapitre4-Fonctions (1) (résumé)]], [[TD4Applications (résumé)]], [[TD4Applications-Solutions (résumé)]], [[chp2 (résumé)]], [[chp4 (résumé)]]
