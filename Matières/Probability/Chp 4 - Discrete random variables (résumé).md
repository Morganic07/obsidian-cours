---
type: source
tags: [year2]
sources: ["[[Chp 4 - Discrete random variables]]"]
maj: 2026-11-05
---

Résumé de [[Chp 4 - Discrete random variables]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Passer des événements aux variables aléatoires : une fonction qui associe un nombre à chaque issue. Le chapitre traite le cas discret : loi de probabilité, fonction de répartition, espérance, variance.

## Contenu, dans l'ordre du cours

- **[[Variable aléatoire]]** : fonction de l'espace d'échantillonnage vers une partie de $\mathbb{R}$. Elle est discrète si ses valeurs forment un ensemble fini ou dénombrable, continue si elles forment un intervalle (ou une union) et qu'aucune valeur n'a de probabilité positive. Une variable de Bernoulli prend les valeurs 0 et 1.
- **Loi de probabilité** (pmf) : $p(x) = P(X = x) = P(\{s \in S : X(s) = x\})$, avec $p(x) \ge 0$ et $\sum_x p(x) = 1$. Représentations : diagramme en bâtons, histogramme de probabilité (rectangles de même base centrés en chaque $x$, de hauteur proportionnelle à $p(x)$).
- **$P(X \le x)$** : exemple des lits d'urgence (0 à 4), $P(X \le 2) = 0{,}75$. Comme $X$ est discrète, $\{X \le 2{,}7\} = \{X \le 2\}$.
- **[[Fonction de répartition]]** : $F(x) = P(X \le x) = \sum_{y \le x} p(y)$. C'est une fonction en escalier, valant la valeur de $F$ au point possible le plus proche à gauche. Exemple des clés USB (1, 2, 4, 8, 16 Go) : $F(4) = 0{,}50$, $F(2{,}7) = F(2) = 0{,}15$.
- **De $F$ à $p$** : pour $a \le b$, $P(a \le X \le b) = F(b) - F(a^-)$, où $a^-$ est la plus grande valeur possible strictement inférieure à $a$. Exemple : $p(3) = F(3) - F(2)$ ; $P(2 \le X \le 4) = F(4) - F(1) \ne F(4) - F(2)$, mais $P(2 < X \le 4) = F(4) - F(2)$.
- **[[Espérance et variance]]** : $E(X) = \sum_{x \in D} x\,p(x)$ ; pour une fonction, $E(h(X)) = \sum h(x)p(x)$ (exemple du coût de diagnostic $h(X) = 20 + 3X + 0{,}5X^2$ : valeurs 40, 56, 76).
- **Linéarité** : $E(a_1h_1(X) + a_2h_2(X) + b) = a_1E(h_1(X)) + a_2E(h_2(X)) + b$. En particulier $E(aX + b) = aE(X) + b$, $\mu_{aX} = a\mu_X$, $\mu_{X+b} = \mu_X + b$. Le cours souligne que $\mu_{aX+b} = a\mu_X + b$ ne vaut que pour une fonction affine de $X$.
- **Variance** : $\mathrm{Var}(X) = \sum (x-\mu)^2p(x) = E[(X-\mu)^2]$, écart-type $\sigma = \sqrt{\mathrm{Var}(X)}$. Formule raccourcie $\mathrm{Var}(X) = E(X^2) - \mu^2$. $\mathrm{Var}(aX+b) = a^2\sigma_X^2$ et $\sigma_{aX+b} = |a|\sigma_X$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **$p(x) > 0$** : le texte écrit « $p(x) > 0$ et $\sum p(x) = 1$ ». Une loi de probabilité demande $p(x) \ge 0$ : $p$ vaut 0 hors des valeurs possibles, et les exemples le montrent (complément).
2. **Formule de $P(a \le X \le b)$** : le texte écrit « F(b) \_ F(a<sup>\_</sup>) ». Le « \_ » est un signe moins perdu à la conversion, comme le prouvent les exemples qui suivent. Image non ouverte.
3. **Définition de variable continue** : « aucune valeur n'a de probabilité positive » est une propriété, reprise au chapitre 5, qui n'identifie pas à elle seule une variable continue. Le chapitre 5 la définit par une densité (complément).
4. **Corrections de transcription** : la transcription signale des « carrés pointillés » autour de $\sigma_X$ et des indices de $h_1$, $h_2$. Ce sont des artefacts d'images, sans conséquence sur les formules.
