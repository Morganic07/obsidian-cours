---
type: concept
tags: [year1]
aliases: [quantificateurs, quantificateur universel, quantificateur existentiel, négation des quantificateurs, distributivité des quantificateurs]
matieres: [Analyse Maths, Outil Maths]
sources: ["[[1 - logique (résumé)|Chapitre 1 logique]]", "[[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]]", "[[Raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf]]", "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

Le cours de logique note $\exists a \in A,\ p(a)$ (quantificateur existentiel) et $\forall a \in A,\ p(a)$ (quantificateur universel).

**Distributivité** : $\forall x\,(p(x) \wedge q(x)) \equiv \forall x\,p(x) \wedge \forall x\,q(x)$.

**Négation** : $\neg[\forall x \in A,\ p(x)] \equiv \exists x \in A,\ \neg p(x)$, appliquée de proche en proche : $\neg[\forall x\, \exists y\, \exists z,\ p] \equiv \exists x\, \forall y\, \forall z,\ \neg p$.

**Ordre** : les exercices d'Outil Maths insistent sur l'ordre des quantificateurs ; $\forall x\, \exists y$ et $\exists y\, \forall x$ ne disent pas la même chose (définition d'une application, surjectivité, application constante).

**Analyse Maths** : les TD traduisent en quantificateurs « majorant », « majoré », « borné », « à partir d'un certain rang » et les limites ; la négation échange $\forall$ et $\exists$ (« $A$ non minoré » : $\forall m,\ \exists x \in A,\ x < m$). Chaque DS d'analyse demande des définitions avec quantificateurs, et un DS d'Outils math porte sur propositions, négations et quantificateurs.

Notion parente : [[Logique propositionnelle]]. Voir aussi : [[Relation d'ordre]], [[Suite numérique]], [[Limite et continuité]], [[Lois de De Morgan]], [[Injectivité et surjectivité]].

Résumés : [[1 - logique (résumé)]]
