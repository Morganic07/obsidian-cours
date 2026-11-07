---
type: concept
tags: [year1]
aliases: [table de vérité, tables de vérité, connecteurs logiques]
matieres: [Outil Maths]
sources: ["[[Chapitre 1 logique (résumé)|Chapitre 1 logique]]", "[[Chapitre 2 ensembles (résumé)|Chapitre 2 ensembles]]", "[[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

La logique propositionnelle étudie des propositions vraies ou fausses, reliées par des connecteurs ($\neg$, $\wedge$, $\vee$, $\Rightarrow$, $\Leftrightarrow$), que le cours pose par leurs tables de vérité. Avec $n$ variables, une table de vérité compte $2^n$ lignes (interprétations possibles). Une **[[Tautologie|tautologie]]** est toujours vraie, une **contradiction** toujours fausse, et deux propositions sont **équivalentes** si elles ont la même table ([[Équivalence logique]]).

**[[Implication logique|Implication]]** : $p \Rightarrow q \equiv \neg p \vee q \equiv \neg q \Rightarrow \neg p$ (contraposée). $p$ est une condition suffisante pour $q$, et $q$ une condition nécessaire pour $p$. $p \Leftrightarrow q$ : [[Condition nécessaire et suffisante|condition nécessaire et suffisante]].

**Arguments** : $p_1, \ldots, p_k \vdash q$ est valide si et seulement si $p_1 \wedge \ldots \wedge p_k \Rightarrow q$ est une tautologie. [[Règle d'inférence|Règles d'inférence]] du cours : [[Modus ponens et modus tollens|modus ponens, modus tollens]], résolution, syllogismes.

**[[Quantificateur|Quantificateurs]]** : $\neg(\forall x\, p) \equiv \exists x\, \neg p$, et réciproquement, appliqué de gauche à droite sur plusieurs quantificateurs.

**Preuves** : [[Preuve par contraposition|contraposition]], [[Raisonnement par l'absurde|absurde]], contre-exemple, disjonction des cas, [[Récurrence]].

Le DS1 d'Outils math demande propositions et négations, quantificateurs, l'équivalence de $P \Rightarrow (Q \Rightarrow R)$ avec $(P \wedge Q) \Rightarrow R$, et la démonstration d'une implication ([[Contrôles (résumé)]]).

Liens : [[Opérations sur les ensembles]] (inclusion, intersection, union et complémentaire correspondent à implication, conjonction, disjonction et négation).

Les exercices et le DS insistent sur la négation des propositions quantifiées ($\forall$ devient $\exists$ et inversement) et sur l'ordre des quantificateurs : $\forall x, \exists y$ ne dit pas la même chose que $\exists y, \forall x$.

Résumés : [[Chapitre 1 logique (résumé)]], [[Exo_Chapitre1_Logique (résumé)]], [[CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022 (résumé)]], [[Chapitre 2 ensembles (résumé)]], [[Chapitre2-Ensemble (4) (résumé)]], [[Contrôles (résumé)]]
