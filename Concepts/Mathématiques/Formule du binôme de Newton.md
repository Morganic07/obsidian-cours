---
type: concept
tags: [year1]
aliases: [binôme de Newton, formule du binôme]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]", "[[Raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé.pdf]]", "[[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]]"]
maj: 2026-11-07
---

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k},$$

démontrée par récurrence au chapitre 0 d'analyse. Avec $a = b = 1$ on obtient $2^n$ ; avec $a = 1, b = -1$, on obtient $0$. Les DS s'en servent pour des sommes comme $\sum (-1)^k\binom{n}{k} / 3^{k+1}$.

**Outil Maths** : le cours ne développe pas la formule. L'exercice 19 de la feuille 1 demande d'exprimer $(a+b)^n$ avec les $\binom{n}{k}$, puis de calculer $\sum_{k=0}^{n} \binom{n}{k}$ et $\sum_{k=0}^{n} \binom{n}{k}(-1)^k$. L'exercice 18 demande de prouver $\binom{n}{k}\binom{n-k}{p-k} = \binom{p}{k}\binom{n}{p}$.

Notion parente : [[Dénombrement]]. Voir aussi : [[Coefficient binomial]], [[Récurrence]], [[Formule de Leibniz]], [[Formule de Pascal]].

## Erreurs du cours

- [[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]], exercice 18, écrit « pour tout $n, p, k \in \mathbb{N}$, $n \geq p \geq q$ » ; il faut « $n \geq p \geq k$ » ($q$ n'apparaît nulle part ailleurs). Vérifié sur l'image.

Résumés : [[0 - Rappels-etc]]
