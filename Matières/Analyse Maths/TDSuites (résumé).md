---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]] (122 diapositives, texte, « Analyse, premier semestre 2023-2024 »), dans [[Analyse Maths (matière)]]. Ce sont les diapositives corrigées du TD sur les suites numériques. La numérotation compte deux exercices 15 (l'un sur les suites adjacentes, l'autre sur Cesàro). Lu par sections, sans relecture en image. Notion centrale : [[Suite numérique]].

## Exercices et méthodes de résolution

| Ex. | Sujet | Méthode du corrigé |
|---|---|---|
| 1, 2 | Exemples de suites (croissante majorée, ni croissante ni décroissante, ni majorée ni minorée) ; propriétés « à partir d'un certain rang » en quantificateurs | $u_n = 1 - \frac1{n+1}$ (croissante, majorée par 1) ; $\exists N, \forall n \ge N, \dots$ |
| 3 | Limites par la définition ($\frac{n+1}{n+2}$, $\frac{n^2+1}{n+1}$, $-3\cdot 2^{n+1}$) | Écrire $\lvert u_n - \ell\rvert < \varepsilon$ (ou $> M$, ou $< m$), isoler $n$, puis prendre $N = E(\cdot) + 1$ |
| 4 à 7 | Calculs de limites : racines à conjuguer, $\frac{\sin n}{n}$, $(-1)^n$, sommes de fractions, $(1 + x/n)^n$, $\sqrt[n]{n^2}$, $n e^{-n}$, $E(nx)/n$, $n!/n^n$ | Quantité conjuguée, factorisation du terme dominant, encadrement et gendarmes, passage au logarithme pour $(1+x/n)^n$ (indication $\ln(1+t)/t \to 1$), croissances comparées. Pour $a^n - b^n \over a^n + b^n$ : trois cas $a = b$, $a > b$, $a < b$ |
| 8 | $\frac{E(x) + E(2x) + \dots + E(nx)}{n^2}$ ; $\mathbb{Q}$ dense dans $\mathbb{R}$ | Encadrement $kx - 1 < E(kx) \le kx$, somme, gendarmes : la limite est $x/2$ ; la densité s'en déduit |
| 9 | Vrai ou faux (limites, sommes, produits) | Contre-exemples : $(-1)^n$ pour la somme et le produit de suites divergentes ; $x_n = (1 + (-1)^n)/2$, $y_n = (1 - (-1)^n)/2$ pour $x_n y_n \to 0$ sans que l'un des deux tende vers 0 |
| 11 | Divergence de $n\sin(n\pi/2)$, etc. | Deux sous-suites de limites différentes |
| 12 | $(u_{2n})$, $(u_{3n})$, $(u_{2n+1})$ convergent, donc $(u_n)$ converge | $(u_{6n})$ est extraite de $(u_{2n})$ et de $(u_{3n})$ : les limites coïncident ; $(u_{6n+3})$ relie $u_{2n+1}$ et $u_{3n}$ ; les indices pairs et impairs recouvrent $\mathbb{N}$ |
| 13 | Critère $u_{n+1}/u_n \to l$ : $l < 1$ donne limite 0, $l > 1$ donne $+\infty$, $l = 1$ indéterminé | Comparer à une suite géométrique ; applications à $a^n/n!$ etc. Voir [[Critère de d'Alembert et de Cauchy]] |
| 14, 15 | Suites adjacentes : $\sum 1/\sqrt k - 2\sqrt{n+1}$ et $\sum 1/\sqrt k - 2\sqrt n$ ; série alternée $\sum (-1)^{k-1}/k$ | Montrer $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; pour l'alternée, les suites paire et impaire sont adjacentes. Voir [[Série numérique]] |
| 16 | Deux suites imbriquées ($\frac{u + 2v}{3}$, $\frac{u + 3v}{4}$) | $w_n = v_n - u_n$ géométrique ; $t_n = 3u_n + 8v_n$ est constante, ce qui donne la limite commune |
| 17 | Si $u_n \to l$ et $a < l$, alors $u_n > a$ à partir d'un rang | Prendre $\varepsilon < l - a$ |
| 18 à 21 | Suites récurrentes $u_{n+1} = f(u_n)$ ($\sqrt{u_n + 1}$, $\sqrt{3 - u_n/2}$, $1 + 2/u_n$, $\frac12 u(u^2 - 3u + 4)$) | Intervalle stable par $f$, monotonie de $f$, points fixes ; $f$ croissante donne une suite monotone ; $f$ décroissante donne deux suites extraites (paire et impaire) monotones de sens contraires ; signe de $f(x) - x$ et cas selon $u_0$ |
| 22 à 24 | Suites complexes (module, partie réelle et imaginaire), $z_{n+1} = \frac13(2z_n - \bar z_n)$, relation de récurrence entre $z_n$ et $z_{n+1}$ | Passer au module ou séparer $\mathrm{Re}$ et $\mathrm{Im}$. Voir [[Nombre complexe]] |
| 25 (Cesàro) | Si $u_n \to l$, la moyenne $\frac1n\sum u_k \to l$ ; réciproque fausse ; cas $+\infty$ | Découper la somme à un rang $N$ fixé |
| 26 | Constante d'Euler : $\frac1{n+1} \le \ln(n+1) - \ln n \le \frac1n$, $\ln(n+1) \le H_n \le 1 + \ln n$, $H_n - \ln n$ décroissante positive donc convergente | Comparaison série-intégrale pour la fonction $1/x$ décroissante. La limite $\gamma \approx 0{,}5772$ : on ignore si elle est rationnelle |
| 27 | $z_n = a^n$ avec $a \in \mathbb{C}$ | $\lvert a\rvert < 1$ : limite nulle ; $\lvert a\rvert > 1$ : module infini, divergence ; $\lvert a\rvert = 1$ : cas selon $\theta/2\pi$ |

## À retenir

- Pour une suite récurrente : stabilité de l'intervalle, monotonie de $f$, points fixes, puis monotonie de la suite et limite. Si $f$ est décroissante, étudier $f \circ f$ ou les suites paire et impaire.
- Pour montrer la convergence d'une suite alternée ou encadrée : suites adjacentes.
- Une démonstration par la définition suit toujours le schéma : fixer $\varepsilon$ (ou $M$), isoler $n$, choisir $N$.

## Points à vérifier

- **Exercice 27, question 3** : le corrigé écrit que si $\theta/2\pi \in \mathbb{Q} \setminus \mathbb{Z}$, la suite est « périodique et donc divergente ». Une suite périodique peut converger (une suite constante est périodique). Ici la divergence vient du fait que la suite prend plusieurs valeurs distinctes, répétées indéfiniment ($q \ge 2$ valeurs $e^{2ip\pi n/q}$), donc deux sous-suites ont des limites différentes (complément).

## Liens

[[Suite numérique]], [[Limite et continuité]], [[Série numérique]], [[Critère de d'Alembert et de Cauchy]], [[Récurrence]], [[Borne supérieure]].
