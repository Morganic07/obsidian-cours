---
type: source
sources: ["[[Chapitre 1 logique]]"]
maj: 2026-11-05
---

Résumé de [[Chapitre 1 logique]], dans [[Year 1 - Outil Maths]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre pose le langage des propositions (connecteurs, tables de vérité, quantificateurs) puis les grands types de preuve. Voir [[Logique propositionnelle]].

## Contenu, dans l'ordre du cours

- **Interprétations** : $n$ variables donnent $2^n$ interprétations. Tables de vérité de $\Leftrightarrow$, $\wedge$, $\neg$, $\Rightarrow$, $\vee$. Le cours retient $p \Rightarrow q \equiv \neg p \vee q \equiv \neg q \Rightarrow \neg p$.
- **Condition suffisante, nécessaire, nécessaire et suffisante** : si $p \Rightarrow q$, $p$ est suffisante pour $q$ et $q$ est nécessaire pour $p$ (« $p$ seulement si $q$ »). Exemple du cours : être un rectangle est nécessaire pour être un carré. Nécessaire et suffisante revient à $\Leftrightarrow$.
- **Tautologie** (toujours vraie), **contradiction** (toujours fausse), **équivalence logique** (même table de vérité).
- **Propriétés des connecteurs** : idempotence, associativité, commutativité, distributivité, identité, involution, complément, lois de De Morgan.
- **Précédence** : négation, conjonction, disjonction, puis implication et équivalence. À priorité égale, le connecteur de droite l'emporte.
- **Argument** $p_1, \ldots, p_k \vdash q$ : valide si les prémisses vraies donnent une conclusion vraie, sinon fallacieux. Il est valide si et seulement si $p_1 \wedge \ldots \wedge p_k \Rightarrow q$ est une tautologie. Exemples : $p \wedge q \vdash p$ est valide, $q, p \Rightarrow q \vdash p$ est fallacieux.
- **Règles d'inférence** : introduction de la disjonction et de la conjonction, élimination de la conjonction, résolution (Robinson), modus ponens, modus tollens, syllogismes disjonctif et hypothétique. Le cours prouve le modus ponens par table de vérité.
- **Quantificateurs** $\exists$ et $\forall$. $\forall x\,(p \wedge q) \equiv (\forall x\,p) \wedge (\forall x\,q)$. Négation : $\neg[\forall x\,p(x)] \equiv \exists x\,\neg p(x)$, appliquée de proche en proche, par exemple $\neg[\forall x \exists y \exists z\, p] \equiv \exists x \forall y \forall z\, \neg p$.
- **Types de preuve** : contraposition (prouver $\neg q \Rightarrow \neg p$), absurde, contre-exemple (un seul suffit pour réfuter), disjonction des cas, récurrence (exemple $1 + \ldots + n = n(n+1)/2$, avec initialisation, hérédité, conclusion). Voir [[Récurrence]].
- **Théorèmes à connaître** : somme de deux impairs paire ; $x + y$ pair implique même parité (par contraposition) ; $a^2$ pair implique $a$ pair (lemme) ; $\sqrt{2}$ irrationnel par l'absurde, avec une fraction $a/b$ sans facteur commun.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes pour cette note.

1. **« $q(x,x)$ »** dans la démonstration de la parité : la transcription le recopie tel quel avec un « À vérifier ». On attendrait $q(x,y)$, d'après le raisonnement. Je n'ai pas ouvert l'image : c'est probablement une coquille du cours, sans conséquence sur la preuve.
