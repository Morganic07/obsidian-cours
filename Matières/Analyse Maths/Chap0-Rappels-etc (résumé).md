---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc]] (PDF de 6 pages), dans [[Analyse Maths (matière)]]. Le PDF est un scan sans texte : il a été lu en image.

## Contenu, dans l'ordre du cours

**I. Équations, inéquations, valeur absolue, racine carrée**
- Résoudre une équation : appliquer des transformations autorisées (ajouter, soustraire, multiplier ou diviser par un nombre non nul). Degré 2 : discriminant. Degré supérieur : racine évidente puis factorisation, sinon étude de fonction.
- Inégalités : la réciproque de « strict implique large » est fausse. Multiplier par un négatif renverse l'inégalité. On peut additionner des inégalités de même sens, jamais les soustraire. Passage à l'inverse pour deux réels de même signe. Pour majorer une fraction de positifs : majorer le numérateur et minorer le dénominateur.
- Exemple type : $x + 1/x \ge 2$ pour $x > 0$ se ramène à $(x-1)^2 \ge 0$ (partir du résultat au brouillon, partir de la fin sur la copie).
- Valeur absolue : $|x|$ est la distance de $0$ à $x$. Inégalité triangulaire $|x+y| \le |x| + |y|$ et $|xy| = |x||y|$. Pour $|x-a| \le \varepsilon$ : $x \in [a-\varepsilon, a+\varepsilon]$ (utile plus tard pour les limites). Piège : $|x-y| \le |x| + |y|$, pas $|x| - |y|$.
- Méthode : lever les valeurs absolues en distinguant des intervalles, ou élever au carré ($|a| = |b| \iff a^2 = b^2$).
- Puissances et racines : $\sqrt{x^2} = |x|$, pas $x$. $\sqrt{x+y} \ne \sqrt{x} + \sqrt{y}$. Erreurs graves à éviter : $ax = ay \Rightarrow x = y$ (oublie $a = 0$), $a^2 = b^2 \Rightarrow a = b$ (oublie $a = -b$). Outil : un produit est nul si et seulement si l'un des facteurs l'est.
- **Principe des substitutions** : une inégalité vraie pour tout réel donne de nouveaux résultats en remplaçant la variable. On obtient ainsi l'inégalité triangulaire généralisée $\big||x| - |y|\big| \le |x+y| \le |x| + |y|$.

**II. Trigonométrie** : renvoi à deux formulaires (`00_inegalites.pdf`, `formtrig.pdf`), non intégrés au PDF.

**III. Symboles somme et produit**
- Définition sur une famille finie, conventions $\sum_\emptyset = 0$ et $\prod_\emptyset = 1$. L'indice est muet. Linéarité de la somme, $\prod (\lambda a_i) = \lambda^p \prod a_i$ avec $p$ le nombre de termes.
- Méthodes : sommes et produits télescopiques ($\sum (u_{k+1} - u_k) = u_{n+1} - u_m$, exemples $\sum 1/(k(k+1))$ et $\prod (1 - 1/k)$), changement d'indice, regroupement de termes (exemple $\sum \min(k, n)$).
- Factorielle, coefficient binomial $\binom{n}{p}$, symétrie, relation de Pascal, triangle de Pascal. $\binom{n}{p}$ est entier, par [[Récurrence]] avec Pascal.
- Formule du binôme de Newton $(a+b)^n = \sum \binom{n}{k} a^k b^{n-k}$, preuve par récurrence. Cas $a = b = 1$ donne $2^n$ ; $a = 1, b = -1$ donne $0$.

## Liens

[[Récurrence]], [[Dénombrement]] (coefficients binomiaux), [[Norme]] (la valeur absolue en est le cas réel).
