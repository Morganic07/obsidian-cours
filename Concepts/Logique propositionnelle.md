---
type: concept
aliases: [table de vérité, tables de vérité, tautologie, tautologies, modus ponens, modus tollens, preuve par contraposition, contraposée, raisonnement par l'absurde, condition nécessaire et suffisante, connecteurs logiques]
matieres: [Outil Maths]
sources: ["[[Chapitre 1 logique]]"]
maj: 2026-11-05
---

La logique propositionnelle étudie des propositions vraies ou fausses, reliées par des connecteurs ($\neg$, $\wedge$, $\vee$, $\Rightarrow$, $\Leftrightarrow$). Avec $n$ variables, une table de vérité compte $2^n$ lignes. Une **tautologie** est toujours vraie, une **contradiction** toujours fausse, et deux propositions sont **équivalentes** si elles ont la même table.

**Implication** : $p \Rightarrow q \equiv \neg p \vee q \equiv \neg q \Rightarrow \neg p$. $p$ est une condition suffisante pour $q$, et $q$ une condition nécessaire pour $p$. $p \Leftrightarrow q$ : condition nécessaire et suffisante.

**Arguments** : $p_1, \ldots, p_k \vdash q$ est valide si et seulement si $p_1 \wedge \ldots \wedge p_k \Rightarrow q$ est une tautologie. Règles d'inférence du cours : modus ponens, modus tollens, résolution, syllogismes.

**Quantificateurs** : $\neg(\forall x\, p) \equiv \exists x\, \neg p$, et réciproquement, appliqué de gauche à droite sur plusieurs quantificateurs.

**Preuves** : contraposition, absurde, contre-exemple, disjonction des cas, [[Récurrence]].

Liens : [[Opérations sur les ensembles]] (inclusion, intersection, union et complémentaire correspondent à implication, conjonction, disjonction et négation).

Résumé : [[Chapitre 1 logique (résumé)]]
