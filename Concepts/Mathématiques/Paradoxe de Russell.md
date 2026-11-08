---
type: concept
tags: [year1]
aliases: [Russell's paradox, paradoxe du barbier, barber paradox]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : paradoxe découvert par Bertrand Russell en 1901, qui montre qu'on ne peut pas former un ensemble à partir de n'importe quelle propriété. On considère
$$R = \{x \mid x \notin x\},$$
la « collection » des ensembles qui ne s'appartiennent pas à eux-mêmes.

- Si $R \in R$, alors $R$ vérifie la propriété qui définit $R$, donc $R \notin R$.
- Si $R \notin R$, alors $R$ vérifie cette propriété, donc $R \in R$.

On obtient $R \in R \iff R \notin R$ : contradiction ([[Raisonnement par l'absurde]]). La collection $R$ ne peut donc pas être un ensemble.

**Conséquences** :

- il n'existe pas d'« ensemble de tous les ensembles » $U$ : sinon $R = \{x \in U : x \notin x\}$ serait un ensemble, et la même contradiction apparaîtrait ;
- la [[Définition par compréhension|définition par compréhension]] doit prendre ses éléments dans un ensemble déjà donné : $\{x \in E : P(x)\}$, et non $\{x \mid P(x)\}$. C'est le schéma de séparation de l'axiomatique de Zermelo (1908), à la base de la théorie des ensembles ZF utilisée aujourd'hui. Avec $E$ fixé, $\{x \in E : x \notin x\}$ est un ensemble sans contradiction : il ne peut simplement pas appartenir à $E$.

**Histoire** : Russell l'a communiqué à Gottlob Frege en 1902, au moment où celui-ci achevait ses *Lois fondamentales de l'arithmétique*, dont le système permettait de former $R$. Le paradoxe a ouvert la « crise des fondements » des mathématiques au début du XXᵉ siècle.

**Version populaire (paradoxe du barbier)** : dans un village, le barbier rase tous ceux, et seulement ceux, qui ne se rasent pas eux-mêmes. Le barbier se rase-t-il ? S'il se rase, il ne doit pas se raser ; s'il ne se rase pas, il doit se raser. Conclusion : un tel barbier ne peut pas exister.

## Dans le cours

Le cours ne le nomme pas. [[2 - ensembles]] présente les « ensembles d'ensembles », par exemple $\mathcal{A} = \{A,\ A \subseteq \mathbb{N} ;\ \forall a \in A,\ a \text{ est pair}\}$, et définit toujours par compréhension à l'intérieur d'un ensemble $E$ donné ; le paradoxe apparaît dans les compléments de cette fiche pour expliquer cette précaution.

Notion parente : [[Ensemble (mathématiques)]]. Voir aussi : [[Définition par compréhension]], [[Raisonnement par l'absurde]].

Résumés : [[2 - ensembles]], [[2 - pdf]]
