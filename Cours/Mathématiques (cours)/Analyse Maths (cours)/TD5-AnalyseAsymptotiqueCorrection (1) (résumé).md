---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/TD5-AnalyseAsymptotiqueCorrection (1).pdf|TD5-AnalyseAsymptotiqueCorrection (1).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de TD5-AnalyseAsymptotiqueCorrection ([[Raw/Year 1/Analyse Maths/Exos/TD5-AnalyseAsymptotiqueCorrection (1).pdf|TD5-AnalyseAsymptotiqueCorrection (1).pdf]]) (32 pages, texte, « Analyse II 2021/2022 »), dans [[Analyse Maths (index)]]. C'est le corrigé détaillé du TD d'analyse asymptotique dont l'énoncé 2020-2021 est dans [[TD5-AnalAsympt (résumé)]]. Cette version compte 5 affirmations à l'exercice 1 au lieu de 4. Cette fiche reprend, pour chacun des 24 exercices, l'énoncé, puis la correction du document avec ses étapes clés et son résultat ; les méthodes sont regroupées à la fin. Le document ne contient aucune figure. Cours associé : [[chp 5 - Analyse Maths (résumé)|chp5 (résumé)]].

Notations du corrigé : $u_n = o(v_n)$ ($u$ négligeable devant $v$), $u_n = O(v_n)$ ($u$ dominée par $v$), $u_n \sim v_n$ ([[Équivalent (comparaison asymptotique)|équivalent]]), voir [[Comparaison asymptotique]]. « Règle d'or » rappelée par le corrigé : $u_n \sim v_n \iff u_n = v_n + o(v_n)$.

## Comparaison de suites

### Exercice 1 — Vrai ou faux

**Énoncé.** Parmi les affirmations suivantes, lesquelles sont vraies, lesquelles sont fausses et pourquoi ?
1. Si $u_n = o(v_n)$ alors $u_n = O(v_n)$.
2. Si $u_n = O(v_n)$ et $v_n = O(u_n)$ alors $u_n \sim v_n$.
3. Si $u_n \sim v_n$ alors $u_n - v_n = o(v_n)$.
4. Si $u_n \sim v_n$ alors $(u_n - v_n) \to 0$ quand $n \to +\infty$.
5. $\dfrac{3^n}{n} = O(2^n)$.

**Correction.**
1. **VRAI** : $u_n = o(v_n) \iff \lim \frac{u_n}{v_n} = 0$, donc $\frac{u_n}{v_n}$ est convergente, donc bornée, donc $u_n = O(v_n)$.
2. **FAUX** : $u_n = 1$ et $v_n = 2$ (constantes). On a bien $u_n = O(v_n)$ et $v_n = O(u_n)$, mais $u_n$ n'est pas équivalente à $v_n$ ([[Preuve par contre-exemple|contre-exemple]]).
3. **VRAI** : $\lim \frac{u_n}{v_n} = 1 \Rightarrow \lim \frac{u_n - v_n}{v_n} = \lim \left(\frac{u_n}{v_n} - 1\right) = 0$, donc $u_n - v_n = o(v_n)$.
4. **FAUX** : $u_n = n + 1$ et $v_n = n$ vérifient $u_n \sim v_n$, mais $\lim (u_n - v_n) = 1$.
5. **FAUX** : $r_n = \dfrac{3^n/n}{2^n} = \dfrac{(3/2)^n}{n}$. Or $\lim_{x\to+\infty} \frac{(3/2)^x}{x} = \lim \frac{e^{x\ln(3/2)}}{x} = +\infty$ par [[Croissances comparées|croissances comparées]]. Donc $r_n \to +\infty$ : la suite n'est pas bornée et $\frac{3^n}{n} \neq O(2^n)$.

### Exercice 2 — Équivalents simples

**Énoncé.** Donner des équivalents simples de :
a) $u_n = \ln\left(1 + \frac1n\right)$ ; b) $v_n = \ln\left(n + \sqrt{n^2+1}\right)$ ; c) $w_n = \sqrt{1 + \sqrt n}$ ; d) $x_n = \sqrt{n^3 + 2n^2} - \sqrt{n^3 + n^2}$ ; e) $y_n = \sin\left(\frac{n^2+n+1}{n+1}\pi\right)$.

**Correction.**
- a) $\frac1n \to 0$ donc $u_n = \ln\left(1+\frac1n\right) \sim \frac1n$.
- b) On factorise $n$ :
$$v_n = \ln(n) + \ln\left(1 + \frac{\sqrt{n^2+1}}{n}\right) = \ln(n) + \ln\left(1 + \sqrt{1 + \tfrac{1}{n^2}}\right).$$
Le second terme tend vers $\ln 2$ et $\ln n \to +\infty$, donc il est $o(\ln n)$ : $\boxed{v_n \sim \ln n}$.
- c) La relation $\sqrt{1+u_n} - 1 \sim \frac12 u_n$ suppose $u_n \to 0$, ce qui n'est pas le cas de $\sqrt n$ : elle ne sert à rien ici. On a simplement $1 + \sqrt n \sim \sqrt n$, puis on élève à la puissance $\frac12$ : $\boxed{w_n \sim \sqrt{\sqrt n} = n^{1/4}}$.
- d) Par la [[Quantité conjuguée|quantité conjuguée]] :
$$x_n = \frac{n^2}{\sqrt{n^3+2n^2} + \sqrt{n^3+n^2}} = \frac{\sqrt n}{\sqrt{1+\frac2n} + \sqrt{1+\frac1n}},$$
et le dénominateur tend vers 2, donc $\boxed{x_n \sim \frac{\sqrt n}{2}}$.
 *Autre méthode* : $x_n = \sqrt{n^3}\left(\sqrt{1+\frac2n} - \sqrt{1+\frac1n}\right)$. On ne peut pas additionner des équivalents (« opération totalement interdite »), on passe donc par les petits $o$ : $\sqrt{1+u_n} = 1 + \frac12 u_n + o(u_n)$, d'où
$$x_n = \sqrt{n^3}\left(1 + \frac1n + o\left(\tfrac1n\right) - 1 - \frac{1}{2n} - o\left(\tfrac1n\right)\right) = \sqrt{n^3}\left(\frac{1}{2n} + o\left(\tfrac1n\right)\right) = \frac{\sqrt n}{2} + o(\sqrt n).$$
- e) Division euclidienne : $n^2 + n + 1 = n(n+1) + 1$, donc $y_n = \sin\left(n\pi + \frac{\pi}{n+1}\right)$. Or $\sin(x + n\pi) = (-1)^n \sin x$, donc $y_n = (-1)^n \sin\frac{\pi}{n+1}$. Comme $\frac{\pi}{n+1} \to 0$, $\sin\frac{\pi}{n+1} \sim \frac{\pi}{n+1}$ et $\boxed{y_n \sim \frac{(-1)^n \pi}{n+1}}$.

### Exercice 3 — Limites par équivalents

**Énoncé.** Déterminer les limites suivantes en utilisant des équivalents :
a) $\lim \left(1 + \frac xn\right)^n$, $x \in \mathbb R$ ; b) $\lim \sqrt[n]{n^2}$ ; c) $\lim \sin\left(\frac{n^2+2n+3}{n+1}\pi\right)$ ; d) $\lim \left(\sqrt{n^2+2n+3} - \sqrt{n^2+n+1}\right)$.

**Correction.**
- a) Pour $x \in \mathbb R^*$ : $a_n = e^{n\ln(1 + x/n)}$ et $\ln\left(1+\frac xn\right) \sim \frac xn$, donc $n\ln\left(1+\frac xn\right) \sim x$.
 **Piège** : écrire $a_n \sim e^x$ en composant l'équivalent par $\exp$ est faux : « on n'a pas le droit de composer une relation d'équivalence à gauche par une fonction ». La bonne méthode : $n\ln\left(1+\frac xn\right) \sim x \neq 0 \Rightarrow \lim n\ln\left(1+\frac xn\right) = x$, puis on compose la **limite** par l'exponentielle (continue) : $\boxed{\lim a_n = e^x}$.
- b) $b_n = \sqrt[n]{n^2}$ a pour limite $1$ (sans autre justification dans le corrigé ; on peut écrire $b_n = e^{2\ln n / n}$ et $\frac{\ln n}{n} \to 0$).
- c) $\frac{n^2+2n+3}{n+1} = (n+1) + \frac{2}{n+1}$, donc $c_n = \sin\left((n+1)\pi + \frac{2\pi}{n+1}\right) = (-1)^{n+1}\sin\frac{2\pi}{n+1}$, et $\boxed{\lim c_n = 0}$.
- d) Quantité conjuguée : $d_n = \dfrac{n+2}{\sqrt{n^2+2n+3} + \sqrt{n^2+n+1}} = \dfrac{1 + \frac2n}{\sqrt{1 + \frac2n + \frac{3}{n^2}} + \sqrt{1 + \frac1n + \frac{1}{n^2}}}$, donc $\boxed{\lim d_n = \frac12}$.

### Exercice 4 — Équivalents plus délicats

**Énoncé.** Déterminer un équivalent le plus simple possible quand $n \to +\infty$ de :
a) $(1+\sqrt n)^{-\sqrt n}$ ; b) $\ln\left(\cos\frac1n\right)\ln\left(\sin\frac1n\right)$ ; c) $\sqrt{1 + \frac{(-1)^n}{\sqrt n}} - 1$ ; d) $e^{\sqrt{n+1} - \sqrt n}$.

**Correction.**
- a) $x_n = \exp\left(-\sqrt n \ln(1+\sqrt n)\right)$ et $\ln(1 + \sqrt n) = \ln\left(\sqrt n\left(1 + \frac{1}{\sqrt n}\right)\right) = \ln\sqrt n + \ln\left(1 + \frac{1}{\sqrt n}\right)$, d'où
$$x_n = \exp\left(-\sqrt n \ln\sqrt n\right) \times \exp\left(-\sqrt n \ln\left(1 + \tfrac{1}{\sqrt n}\right)\right).$$
L'exposant du second facteur vérifie $-\sqrt n \ln\left(1 + \frac{1}{\sqrt n}\right) \sim -\sqrt n \cdot \frac{1}{\sqrt n} = -1$ ; il tend donc vers $-1$ et le second facteur tend vers $e^{-1}$ (donc lui est équivalent). Finalement
$$\boxed{x_n \sim \sqrt n^{\,-\sqrt n} \times e^{-1} = \frac{1}{e\,\sqrt n^{\sqrt n}}}.$$
- b) Premier facteur : $\ln\left(\cos\frac1n\right) = \ln\left(1 + \left(\cos\frac1n - 1\right)\right) \sim \cos\frac1n - 1$ (car $\cos\frac1n - 1 \to 0$ et $\ln(1+u_n) \sim u_n$), et $\cos(u_n) - 1 \sim -\frac{u_n^2}{2}$, donc $\ln\left(\cos\frac1n\right) \sim -\frac{1}{2n^2}$.
 Second facteur : $\sin\frac1n \sim \frac1n$, mais on ne compose pas par $\ln$. On écrit $\sin\frac1n = \frac1n + o\left(\frac1n\right) = \frac1n(1 + o(1))$, donc
$$\ln\left(\sin\tfrac1n\right) = -\ln n + \ln(1 + o(1)) = a_n + b_n,$$
avec $a_n = -\ln n \to -\infty$ et $b_n \to 0$, donc $b_n = o(a_n)$ et $\ln\left(\sin\frac1n\right) \sim -\ln n$.
 Conclusion : $y_n \sim -\frac{1}{2n^2} \times (-\ln n)$, soit $\boxed{y_n \sim \frac{\ln n}{2n^2}}$.
- c) Avec $(1+u_n)^\alpha - 1 \sim \alpha u_n$ ($\alpha$ réel fixé, $u_n \to 0$) : $z_n = \left(1 + \frac{(-1)^n}{\sqrt n}\right)^{1/2} - 1 \sim \frac12 \cdot \frac{(-1)^n}{\sqrt n}$, soit $\boxed{z_n \sim \frac{(-1)^n}{2\sqrt n}}$.
- d) $t_n = e^{\sqrt{n+1}-\sqrt n} = e^{\frac{1}{\sqrt{n+1}+\sqrt n}}$. Avec $e^{u_n} = 1 + u_n + o(u_n)$ : $t_n = 1 + \frac{1}{\sqrt{n+1}+\sqrt n} + o\left(\frac{1}{\sqrt{n+1}+\sqrt n}\right)$, donc $\boxed{t_n \sim 1}$. On pouvait le voir dès le début : $\lim t_n = 1$. Mais attention, l'implication $\lim u_n = \ell \Rightarrow u_n \sim \ell$ n'est correcte que pour $\ell \in \mathbb R^*$.

### Exercice 5 — Somme des factorielles

**Énoncé.** Montrer que $\displaystyle\sum_{k=0}^n k! \sim n!$.

**Correction.** On note $u_n = \sum_{k=0}^n k!$.
- *Première idée (insuffisante)* : on met de côté le dernier terme, égal à 1 :
$$\frac{u_n}{n!} = \frac{1}{n!} + \frac{1}{n!} + \frac{2}{n!} + \dots + \frac{(n-1)!}{n!} + 1 = \frac{1}{n!} + \frac{1}{n!} + \frac{2}{n!} + \dots + \frac1n + 1.$$
$\frac{u_n}{n!} - 1$ est une somme de termes qui tendent tous vers 0, mais cela ne suffit pas pour dire que la somme tend vers 0 : il suffit de penser à $\sum_{k=1}^n \frac1n = 1$.
- *Deuxième idée* : on met de côté les deux derniers termes :
$$\frac{u_n}{n!} - 1 - \frac1n = \sum_{k=0}^{n-2} \frac{k!}{n!}.$$
Sachant que $\frac{(n-2)!}{n!} = \frac{1}{n(n-1)}$ et que pour $k \le n-2$, $\frac{k!}{n!} \le \frac{(n-2)!}{n!}$, la somme de ces $n-1$ termes est majorée par $\sum_{k=0}^{n-2}\frac{1}{n(n-1)} = \frac1n$. D'où
$$1 \le \frac{u_n}{n!} \le 1 + \frac1n + \frac1n = 1 + \frac2n,$$
et le [[Théorème des gendarmes|théorème des gendarmes]] donne $\lim \frac{u_n}{n!} = 1$, soit $u_n \sim n!$.

### Exercice 6 — Suite telle que $s_n + s_{n+1} \sim 1/n$

**Énoncé.** Soit $(s_n)$ une suite de réels de limite 0 telle que $s_n + s_{n+1} \sim \frac1n$.
1. On suppose $(s_n)$ décroissante : montrer que $s_n \sim \frac{1}{2n}$.
2. En considérant la suite $\left(\frac{1}{2n} + \frac{(-1)^n}{\sqrt n}\right)_{n \ge 1}$, prouver que ce résultat est en défaut si $(s_n)$ n'est pas décroissante.

**Correction.**
1. $s_n + s_{n+1} \sim \frac1n \iff \lim n(s_n + s_{n+1}) = 1 \iff \lim (n-1)(s_{n-1} + s_n) = 1$. On veut $\lim 2n\, s_n = 1$. Par décroissance, $s_{n+1} \le s_n \le s_{n-1}$, donc $s_n + s_{n+1} \le 2s_n \le s_n + s_{n-1}$, et en multipliant par $n$ :
$$n(s_n + s_{n+1}) \le 2n\,s_n \le n(s_n + s_{n-1}).$$
À gauche, la limite est 1 ; à droite, $n(s_{n-1}+s_n) = \frac{n}{n-1}(n-1)(s_{n-1}+s_n) \to 1 \times 1 = 1$. Par les gendarmes, $\lim 2n\,s_n = 1$, soit $s_n \sim \frac{1}{2n}$.
2. $s_n = \frac{1}{2n} + \frac{(-1)^n}{\sqrt n}$ tend bien vers 0. Puis
$$s_n + s_{n+1} = \frac{2n+1}{2n(n+1)} + (-1)^n\left(\frac{1}{\sqrt n} - \frac{1}{\sqrt{n+1}}\right) = \frac{2n+1}{2n(n+1)} + (-1)^n \frac{1}{(\sqrt{n+1}+\sqrt n)\sqrt{n(n+1)}}$$
(quantité conjuguée). Le premier terme $a_n$ est équivalent à $\frac1n$ ($2n+1 \sim 2n$, $n+1 \sim n$). Pour le second, $\sqrt{n+1} + \sqrt n = \sqrt n\left(\sqrt{1+\frac1n} + 1\right) = 2\sqrt n + o(\sqrt n) \sim 2\sqrt n$ et $\sqrt{n(n+1)} \sim n$, donc $b_n \sim \frac{(-1)^n}{2n\sqrt n}$. Ainsi $b_n = o(a_n)$ et $s_n + s_{n+1} \sim a_n \sim \frac1n$.
 Mais $s_n$ n'est pas décroissante ($s_1 = -\frac12$, $s_2 = \frac14 + \frac{1}{\sqrt2} > s_1$), et $s_n \sim \frac{(-1)^n}{\sqrt n}$ car $\frac{1}{2n} = o\left(\frac{(-1)^n}{\sqrt n}\right)$ : le résultat de la question 1 n'est pas vérifié, malgré le respect des autres hypothèses.

## Comparaison de fonctions

### Exercice 7 — Limites par équivalents usuels

**Énoncé.** Calculer :
a) $\lim_{x\to0} \frac{\sin x}{x + 3x^2}$ ; b) $\lim_{x\to0} \frac{\sin(x^4)}{x(\tan x - \sin x)}$ ; c) $\lim_{x\to+\infty} \sqrt{4x+1}\,\ln\left(1 - \frac{\sqrt{x+1}}{x+2}\right)$ ; d) $\lim_{x\to0} \frac{e^{4x^2} - 1}{\ln(\cos x)}$ ; e) $\lim_{x\to0} \frac{x^4 + 3x^2 + x}{2x^3 + x^2}$ ; f) $\lim_{x\to\pi} \frac{3e^{x^2} - 5x^4}{\ln(7x^2) + 2x}$.

**Correction.**
- a) $\frac{\sin x}{x(1+3x)} \underset{0}{\sim} \frac{x}{x} = 1$, donc la limite vaut $\boxed{1}$.
- b) $\tan x - \sin x = \frac{\sin x}{\cos x} - \sin x = \frac{\sin x(1 - \cos x)}{\cos x}$, donc $f(x) = \frac{\sin(x^4)\cos x}{x \sin x (1 - \cos x)}$. On remplace chaque facteur par son équivalent ($\sin(x^4) \sim x^4$, $\cos x \to 1$, $\sin x \sim x$, $1 - \cos x \sim \frac{x^2}{2}$) : $f(x) \underset{0}{\sim} \frac{x^4}{x \cdot x \cdot \frac{x^2}{2}} = 2$, limite $\boxed{2}$.
- c) $-\frac{\sqrt{x+1}}{x+2} \to 0$ et $\ln(1+X) \underset{0}{\sim} X$, donc $\ln\left(1 - \frac{\sqrt{x+1}}{x+2}\right) \underset{+\infty}{\sim} -\frac{\sqrt{x+1}}{x+2} \sim -\frac{\sqrt x}{x} = -\frac{1}{\sqrt x}$ ; de même $\sqrt{4x+1} \sim 2\sqrt x$. Donc $g(x) \sim \frac{-2\sqrt x}{\sqrt x} = -2$, limite $\boxed{-2}$.
- d) $e^{4x^2} - 1 \underset{0}{\sim} 4x^2$ (car $e^x - 1 \sim x$) ; $\ln(\cos x) = \ln(1 + (\cos x - 1)) \sim \cos x - 1 \sim -\frac{x^2}{2}$. Donc $h(x) \sim \frac{4x^2}{-x^2/2} = -8$, limite $\boxed{-8}$.
- e) $x^4 + 3x^2 + x \underset{0}{\sim} x$ et $2x^3 + x^2 \underset{0}{\sim} x^2$, donc $k(x) \sim \frac1x$. La fonction $x \mapsto \frac1x$ n'a pas de limite en 0 (résultats différents en $0^-$ et $0^+$) : **$k$ n'a pas de limite en 0**.
- f) Le corrigé dit que $l$ est continue sur $\mathbb R^*$ (somme, composée et rapport de fonctions continues), donc $\lim_{x\to\pi} l(x) = l(\pi) = \boxed{\dfrac{3e^{\pi^2} - 5\pi^4}{\ln(7\pi^2) + 2\pi}}$ (voir « Points à vérifier »).

### Exercice 8 — Limites (dont formes $1^\infty$ et $0^0$)

**Énoncé.** Calculer les limites de :
a) $\frac{\sin x \ln(1+x^2)}{x\tan x}$ en 0 ; b) $\frac{\ln(1+\sin x)}{\tan(6x)}$ en 0 ; c) $(\ln(e+x))^{1/x}$ en 0 ; d) $(\ln(1+e^{-x}))^{1/x}$ en $+\infty$.

**Correction.**
- a) $\frac{\sin x \ln(1+x^2)}{x \tan x} \underset{0}{\sim} \frac{x \cdot x^2}{x \cdot x} = x$, limite $\boxed{0}$.
- b) $\frac{\ln(1+\sin x)}{\tan(6x)} \underset{0}{\sim} \frac{\sin x}{6x} \sim \frac16$, limite $\boxed{\frac16}$.
- c) **Non corrigé** dans le document (la solution numérotée 3 traite la limite d)).
- d) $(\ln(1+e^{-x}))^{1/x} = \exp\left(\frac1x \ln(\ln(1+e^{-x}))\right)$. Comme $e^{-x} \to 0$, $\ln(1+e^{-x}) \underset{+\infty}{\sim} e^{-x}$ ; par l'exercice 11 (la limite, 0, est différente de 1), on peut composer par $\ln$ : $\ln(\ln(1+e^{-x})) \sim \ln(e^{-x}) = -x$. Donc $\frac1x\ln(\ln(1+e^{-x})) \sim \frac{-x}{x} = -1$, et par continuité de $\exp$ la limite vaut $\boxed{e^{-1}}$.

### Exercice 9 — Limites diverses

**Énoncé.** Déterminer :
a) $\lim_{x\to1} \frac{x^3 - 2x^2 + 2x - 1}{x^3 - x^2 + x - 1}$ ; b) $\lim_{x\to0} \frac{x\sin x}{1 - \cos x}$ ; c) $\lim_{x\to+\infty} \left((x+1) - \sqrt[3]{x^3+1}\right)$ ; d) $\lim_{x\to0} \exp\left(\frac{(1-\cos x)\sin x}{x^3}\right)$ ; e) $\lim_{x\to0} \frac{\ln(\cos x)}{1 - \cos 2x}$ ; f) $\lim_{x\to+\infty} \left(\frac{\ln(x+1)}{\ln x}\right)^{x\ln x}$ ; g) $\lim_{x\to\pi/2} \frac{\ln(2x/\pi)}{\cos x}$ ; h) $\lim_{x\to+\infty} x^2\left(e^{\frac{1}{x+1}} - e^{\frac1x}\right)$.

**Correction.**
- a) Factorisation par $(x-1)$ : $\frac{(x-1)(x^2-x+1)}{(x-1)(x^2+1)} = \frac{x^2-x+1}{x^2+1} \to \boxed{\frac12}$.
- b) $\sin x \underset{0}{\sim} x$ et $1 - \cos x \underset{0}{\sim} \frac{x^2}{2}$, donc $\frac{x\sin x}{1-\cos x} \sim \frac{x^2}{x^2/2} = 2$, limite $\boxed{2}$.
- c) $(x+1) - \sqrt[3]{x^3+1} = (x+1) - x\sqrt[3]{1 + \frac{1}{x^3}} = 1 + x\left(1 - \sqrt[3]{1 + \frac{1}{x^3}}\right)$. Or $\sqrt[3]{1 + \frac{1}{x^3}} - 1 \underset{+\infty}{\sim} \frac{1}{3x^3}$, soit $\sqrt[3]{1 + \frac{1}{x^3}} = 1 + \frac{1}{3x^3} + o\left(\frac{1}{x^3}\right)$. Donc l'expression vaut $1 - \frac{1}{3x^2} + o\left(\frac{1}{x^2}\right)$, limite $\boxed{1}$.
- d) Par continuité de $\exp$ : $\lim \exp\left(\frac{(1-\cos x)\sin x}{x^3}\right) = \exp\left(\lim \frac{\frac{x^2}{2}\cdot x}{x^3}\right) = \boxed{e^{1/2}}$.
- e) $\ln(\cos x) = \ln(1 - (1 - \cos x)) \sim \cos x - 1 \sim -\frac{x^2}{2}$ et $1 - \cos 2x \sim \frac{(2x)^2}{2}$, donc le quotient $\sim -\frac{x^2}{4x^2}$, limite $\boxed{-\frac14}$.
- f) $\left(\frac{\ln(x+1)}{\ln x}\right)^{x\ln x} = \exp\left(x\ln x \cdot \ln\frac{\ln(x+1)}{\ln x}\right)$. Comme $\frac{\ln(x+1)}{\ln x} \to 1$ :
$$x\ln x \cdot \ln\left(\frac{\ln(x+1)}{\ln x}\right) \underset{+\infty}{\sim} x\ln x\left(\frac{\ln(x+1)}{\ln x} - 1\right) = x(\ln(x+1) - \ln x) = x\ln\left(1 + \frac1x\right) \sim x \cdot \frac1x = 1.$$
La limite vaut $\boxed{e}$.
- g) $\cos x = \sin\left(\frac\pi2 - x\right)$, donc
$$\frac{\ln(2x/\pi)}{\cos x} = \frac{\ln\left(1 - \left(1 - \frac{2x}{\pi}\right)\right)}{\sin\left(\frac\pi2 - x\right)} \underset{\pi/2}{\sim} \frac{\frac{2x}{\pi} - 1}{\frac\pi2 - x} = \frac{\frac{2x - \pi}{\pi}}{\frac{\pi - 2x}{2}} = -\frac2\pi,$$
limite $\boxed{-\frac{2}{\pi}}$.
- h) $x^2\left(e^{\frac{1}{x+1}} - e^{\frac1x}\right) = x^2 e^{\frac1x}\left(e^{\frac{1}{x+1} - \frac1x} - 1\right) = x^2 e^{\frac1x}\left(e^{\frac{-1}{x(x+1)}} - 1\right)$. Avec $e^u - 1 \underset{0}{\sim} u$ : $e^{\frac{-1}{x(x+1)}} - 1 \underset{+\infty}{\sim} -\frac{1}{x(x+1)}$. Donc l'expression $\sim -\frac{x^2 e^{1/x}}{x(x+1)}$, qui tend vers $-1 \cdot 1$ : limite $\boxed{-1}$ (le corrigé écrit $\frac{x^2}{x^2+1}$ à l'avant-dernière ligne, voir « Points à vérifier »).

### Exercice 10 — Quand a-t-on $e^f \sim e^g$ ?

**Énoncé.** À quelle condition sur $f$ et $g$ a-t-on $e^f \underset{a}{\sim} e^g$ ?

**Correction.** Pour tous $x, y \in \mathbb R$, $\frac{e^x}{e^y} = e^{x-y}$, donc
$$e^f \underset{a}{\sim} e^g \iff \lim_{x\to a} e^{f(x) - g(x)} = 1 \iff \lim_{x\to a}(f(x) - g(x)) = 0.$$
**Attention** : $f \underset{a}{\sim} g \Rightarrow e^f \underset{a}{\sim} e^g$ est faux en général. Contre-exemple : $f(x) = x^2 + x$ et $g(x) = x^2$ ; $f \underset{\infty}{\sim} g$, mais $\frac{e^{f(x)}}{e^{g(x)}} = e^x \to +\infty$.

### Exercice 11 — Composer un équivalent par $\ln$

**Énoncé.** Soient $f$ et $g$ équivalentes au voisinage de $a$ et strictement positives. Montrer que si $f$ admet en $a$ une limite dans $\overline{\mathbb R}$ différente de 1, alors $\ln f \underset{a}{\sim} \ln g$.

**Correction.** Comme $u \sim v \iff u - v = o(v)$, il suffit de montrer $\ln f - \ln g = o(\ln f)$, c'est-à-dire
$$\lim_{x\to a} \frac{\ln f(x) - \ln g(x)}{\ln f(x)} = \lim_{x\to a} \ln\left(\frac{f(x)}{g(x)}\right) \cdot \frac{1}{\ln f(x)} = 0.$$
Avec $\ell = \lim_a f$ : $\lim_a \frac{1}{\ln f(x)} = \frac{1}{\ln \ell} \in \mathbb R$ si $\ell \in \mathbb R \setminus \{0, 1\}$, et $0$ si $\ell = 0$ ou $\ell = +\infty$. (Le corrigé s'arrête là ; il reste à noter que $\frac fg \to 1$, donc $\ln\frac fg \to 0$, et le produit tend vers 0.)

### Exercice 12 — Limites et équivalents (suite)

**Énoncé.**
a) Limite en $+\infty$ de $\sqrt[3]{x^3+x^2} - \sqrt[3]{x^3-x^2}$ ;
b) Équivalent en $+\infty$ de $\sqrt{x^2 + \sqrt{x^4+1}} - x\sqrt2$ ;
c) Limite en 0 de $\frac{\tan(ax) - \sin(ax)}{\tan(bx) - \sin(bx)}$ ;
d) Limite en $\frac\pi4$ de $\left(x - \frac\pi4\right)\tan\left(x + \frac\pi4\right)$ ;
e) Limite en $\frac\pi4$ de $\frac{\cos x - \sin x}{(4x - \pi)\tan x}$ ;
f) Équivalent en 0 de $\frac{\tan(x - x\cos x)}{\sin x + \cos x - 1}$ ;
g) Limite en 0 de $x^{\frac{1}{1 + 2\ln x}}$ ;
h) Limite en $\frac12$ de $(2x^2 - 3x + 1)\tan(\pi x)$ ;
i) Équivalent en $+\infty$ de $\frac{\sqrt{1+x^2}}{\sin\left(\frac1x\right)}\ln\left(\frac{x}{x+1}\right)$.

**Correction.**
- a) On factorise $x$ : $x\left(\sqrt[3]{1 + \frac1x} - \sqrt[3]{1 - \frac1x}\right)$, et $\sqrt[3]{1 \pm \frac1x} = 1 \pm \frac{1}{3x} + o\left(\frac{1}{3x}\right)$. Donc l'expression vaut $x\left(\frac{2}{3x} + o\left(\frac1x\right)\right) = \frac23 + o(1)$, limite $\boxed{\frac23}$.
- b) $\sqrt{x^2 + x^2\sqrt{1 + \frac{1}{x^4}}} - x\sqrt2 = x\left(\sqrt{1 + \sqrt{1 + \frac{1}{x^4}}} - \sqrt2\right)$. Avec $\sqrt{1 + \frac{1}{x^4}} = 1 + \frac{1}{2x^4} + o\left(\frac{1}{x^4}\right)$ :
$$\sqrt{2 + \frac{1}{2x^4} + o\left(\tfrac{1}{x^4}\right)} = \sqrt2\sqrt{1 + \frac{1}{4x^4} + o\left(\tfrac{1}{x^4}\right)} = \sqrt2\left(1 + \frac{1}{8x^4} + o\left(\tfrac{1}{x^4}\right)\right).$$
Donc l'expression $\underset{+\infty}{\sim} x\sqrt2 \cdot \frac{1}{8x^4}$, soit $\boxed{\frac{\sqrt2}{8x^3}}$.
- c) $\frac{\tan(ax) - \sin(ax)}{\tan(bx) - \sin(bx)} = \frac{\sin(ax)}{\sin(bx)} \cdot \frac{1 - \cos(ax)}{1 - \cos(bx)} \cdot \frac{\cos(bx)}{\cos(ax)} \underset{0}{\sim} \frac{ax}{bx} \cdot \frac{a^2x^2/2}{b^2x^2/2} \cdot \frac{\cos(bx)}{\cos(ax)} = \frac{a^3}{b^3}\cdot\frac{\cos(bx)}{\cos(ax)}$, limite $\boxed{\frac{a^3}{b^3}}$.
- d) Changement de variable $u = x - \frac\pi4$ : $u\tan\left(u + \frac\pi2\right) = u\,\frac{\sin(u + \pi/2)}{\cos(u + \pi/2)} = u\,\frac{\sin(u + \pi/2)}{-\sin u}$, donc la limite vaut $-\lim \frac{u}{\sin u} \cdot \lim \sin\left(u + \frac\pi2\right) = -1 \cdot 1 = \boxed{-1}$.
- e) $\cos x - \sin x = \frac{2}{\sqrt2}\left(\sin\frac\pi4\cos x - \cos\frac\pi4\sin x\right) = \frac{2}{\sqrt2}\sin\left(\frac\pi4 - x\right)$, donc
$$\frac{\cos x - \sin x}{(4x-\pi)\tan x} \underset{\pi/4}{\sim} \frac{2}{\sqrt2\tan x}\cdot\frac{\frac\pi4 - x}{4x - \pi} = \frac{2}{\sqrt2 \tan x}\cdot\left(-\frac14\right),$$
et avec $\tan\frac\pi4 = 1$ la limite vaut $\boxed{-\frac{1}{2\sqrt2}}$.
- f) $x - x\cos x \to 0$, donc $\tan(x - x\cos x) \underset{0}{\sim} x - x\cos x$. Par ailleurs $\frac{\sin x}{x} \to 1$ et $\frac{1 - \cos x}{x} \sim \frac{x^2}{2x} \to 0$, donc $\frac{\sin x + \cos x - 1}{x} \to 1$ : $\sin x + \cos x - 1 \underset{0}{\sim} x$. D'où le quotient $\sim \frac{x - x\cos x}{x} = 1 - \cos x \sim \boxed{\frac{x^2}{2}}$.
- g) $x^{\frac{1}{1+2\ln x}} = \exp\left(\frac{\ln x}{1 + 2\ln x}\right)$ et $\frac{\ln x}{1 + 2\ln x} \sim \frac{\ln x}{2\ln x} = \frac12$ en $0^+$, limite $\boxed{e^{1/2} = \sqrt e}$.
- h) $2x^2 - 3x + 1 = \left(x - \frac12\right)(2x - 2)$. Avec $u = x - \frac12$ : $u(2u - 1)\tan\left(\pi u + \frac\pi2\right) = u(2u-1)\frac{\sin(\pi u + \pi/2)}{-\sin(\pi u)}$, donc la limite vaut $-\lim \frac{u(2u-1)}{\pi u} = -\frac1\pi \lim(2u - 1) = \boxed{\frac1\pi}$.
- i) $\ln\left(\frac{x}{x+1}\right) = \ln\left(1 - \frac{1}{x+1}\right) \sim -\frac{1}{x+1}$, $\sqrt{1+x^2} \sim x$, $\sin\frac1x \sim \frac1x$. Donc l'expression $\underset{+\infty}{\sim} \frac{x}{1/x}\cdot\left(-\frac{1}{x+1}\right) = -\frac{x^2}{x+1} \sim \boxed{-x}$.

## Développements limités

### Exercice 13 — Ordres d'existence d'un DL en 0

**Énoncé.** Déterminer les ordres pour lesquels les fonctions suivantes admettent un [[Développement limité|DL]] en 0 : a) $x \mapsto \sqrt x$ ; b) $x \mapsto x^{17/4}$ ; c) $x \mapsto |x|^n$.

**Correction.**
- a) $\sqrt x$ est continue mais pas [[Dérivabilité|dérivable]] en 0 : $\lim_{x\to0^+}\frac{\sqrt x - \sqrt0}{x - 0} = \lim \frac{1}{\sqrt x} = +\infty$. En 0, $f$ admet **uniquement un DL à l'ordre 0**.
- b) $x^{17/4} = x^4 \cdot x^{1/4}$, donc $\frac{f(x)}{x^4} = x^{1/4} \to 0$ : $f(x) = o(x^4)$, et $f$ admet le DL à l'ordre 4 $x^{17/4} = 0 + 0x + 0x^2 + 0x^3 + 0x^4 + o(x^4)$. Pas de DL à l'ordre 5 : sinon $x^{17/4} = a_5x^5 + o(x^5)$ et $\frac{x^{17/4}}{x^5} = a_5 + o(1)$ aurait une limite finie, or $\frac{x^{17/4}}{x^5} = \frac{1}{x^{3/4}} \to +\infty$. **DL uniquement jusqu'à l'ordre 4**.
- c) $|x|^n = (\mathrm{sgn}(x))^n x^n$, donc $\frac{|x|^n}{x^{n-1}} = (\mathrm{sgn}\,x)^n\,x \to 0$ : $|x|^n = 0 + 0x + \dots + 0x^{n-1} + o(x^{n-1})$ (DL à l'ordre $n-1$).
 - **$n$ pair** : $|x|^n = x^n$, donc pour tout $k \ge n$, $|x|^n = x^n + o(x^k)$ : DL à **tout ordre**.
 - **$n$ impair** : un DL à l'ordre $n$, $|x|^n = a_nx^n + o(x^n)$, impliquerait l'existence de $\lim \frac{|x|^n}{x^n} = \lim (\mathrm{sgn}\,x)^n$, qui n'existe pas. DL **uniquement jusqu'à l'ordre $n-1$**.

### Exercice 14 — DL nul, fonction non nulle ; DL sans dérivée seconde

**Énoncé.**
1. Soit $f : \mathbb R \to \mathbb R$ définie par $f(x) = 0$ si $x \le 0$ et $f(x) = \exp\left(-\frac1x\right)$ sinon. Calculer, pour tout $n \in \mathbb N$, le DL de $f$ en 0. Quelles conclusions en tirer ?
2. Soit $g : \mathbb R \to \mathbb R$ définie par $g(0) = 0$ et, si $x \ne 0$, $g(x) = x^3\sin\left(\frac1x\right)$. Montrer que $g$ a un DL d'ordre 2 en 0 mais n'a pas de dérivée seconde (en 0).

**Correction.**
1. Changement de variable $u = \frac1x$ : $\lim_{x\to0}\frac{f(x)}{x^n} = \lim \frac{e^{-1/x}}{x^n} = \lim_{u\to+\infty}\frac{u^n}{e^u} = 0$. Donc pour tout $n$, $f(x) = o(x^n)$ et $\exp\left(-\frac1x\right) \underset{x\to0}{=} 0 + 0x + \dots + 0x^n + o(x^n)$.
 **Conclusion** : une partie régulière de DL nulle à n'importe quel ordre n'implique pas que la fonction soit nulle ; deux fonctions dont les parties régulières sont égales à tout ordre ne sont pas pour autant égales.
2. $\frac{g(x)}{x^2} = x\sin\frac1x \to 0$, donc $g(x) = 0 + 0x + 0x^2 + o(x^2)$ : DL d'ordre 2. Sur $\mathbb R^*$, $g'(x) = 3x^2\sin\frac1x - x\cos\frac1x$. Le DL donne $\lim_0 g = 0 = g(0)$ (continuité) et $\lim \frac{g(x) - g(0)}{x} = \lim o(x) = 0$ : $g'(0) = 0$. Mais
$$\frac{g'(x) - g'(0)}{x - 0} = 3x\sin\frac1x - \cos\frac1x$$
n'a pas de limite en 0 : $g$ n'est pas deux fois dérivable en 0.

### Exercice 15 — $(\cos x)^{1/x}$

**Énoncé.** Soit $f(x) = (\cos x)^{1/x}$ pour $x \in \left]-\frac\pi2, \frac\pi2\right[ \setminus \{0\}$.
1. Montrer que $f$ est [[Prolongement par continuité|prolongeable par continuité]] en 0.
2. Déterminer un DL de $f$ en 0 à l'ordre 2.
3. Étudier la dérivabilité du prolongement de $f$.

**Correction.** (Le corrigé traite les questions 1 et 2 ensemble, puis la question 3.)
- $(\cos x)^{1/x} = \exp\left(\frac1x\ln(\cos x)\right)$, avec $\cos x = 1 - \frac{x^2}{2} + o(x^3)$, donc
$$\ln(\cos x) = \ln\left(1 + \left(-\tfrac{x^2}{2} + o(x^3)\right)\right) = -\frac{x^2}{2} + o(x^3), \qquad \frac1x\ln(\cos x) = -\frac x2 + o(x^2).$$
Puis $\exp\left(-\frac x2 + o(x^2)\right) = 1 - \frac x2 + \frac12\left(-\frac x2\right)^2 + o(x^2)$ :
$$\boxed{(\cos x)^{1/x} \underset{x\to0}{=} 1 - \frac x2 + \frac{x^2}{8} + o(x^2)}.$$
Donc $\lim_0 f = 1$ : on prolonge par $f(0) = 1$.
- Dérivabilité : $\lim \frac{f(x) - f(0)}{x} = \lim \left(-\frac12 + \frac x8 + o(x)\right) = -\frac12$ : le prolongement est dérivable en 0, avec $f'(0) = -\frac12$.

### Exercice 16 — Dérivées successives de $\frac{x^3}{1+x^6}$ en 0

**Énoncé.** Soit $f(x) = \frac{x^3}{1+x^6}$ sur $\mathbb R$. Calculer $f^{(n)}(0)$ pour tout $n \in \mathbb N$.

**Correction.** Avec $\frac{1}{1 - (-x^6)}$ :
$$f(x) = x^3\left(1 - x^6 + x^{12} - \dots + (-1)^n x^{6n} + o(x^{6n})\right) = \sum_{k=0}^n (-1)^k x^{3+6k} + o(x^{6n+3}).$$
$f$ est de classe $\mathcal C^\infty$ ([[Fonction de classe Ck]]), donc la formule de Taylor(-Young) donne $f(x) = f(0) + f'(0)x + \dots + \frac{f^{(n)}(0)}{n!}x^n + o(x^n)$. Par unicité du DL, $\frac{f^{(n)}(0)}{n!} = (-1)^k$ si $n = 3 + 6k$, et 0 sinon ; avec $k = \frac{n-3}{6}$ :
$$\boxed{f^{(n)}(0) = \begin{cases} (-1)^{\frac{n-3}{6}}\,n! & \text{si } n \equiv 3 \pmod 6,\\ 0 & \text{sinon.}\end{cases}}$$

### Exercice 17 — DL par Taylor et par produit

**Énoncé.** Déterminer : a) $DL_3(0)$ de $f_1(x) = x^4 - x^2 + 1$ ; b) $DL_3(2)$ de $f_1$ ; c) $DL_3(1)$ de $f_2(x) = (\sqrt x - 1)\ln x$.

**Correction.**
- a) $f_1$ est de classe $\mathcal C^\infty$ ; $f_1'(x) = 4x^3 - 2x$, $f_1''(x) = 12x^2 - 2$, $f_1'''(x) = 24x$. Taylor en 0 : $f_1(x) = 1 + 0\cdot x - \frac22x^2 + 0\cdot x^3 + o(x^3) = \boxed{1 - x^2 + o(x^3)}$.
- b) Taylor en 2 : $f_1(2) = 13$, $f_1'(2) = 28$, $\frac{f_1''(2)}{2!} = 23$, $\frac{f_1'''(2)}{3!} = 8$ :
$$\boxed{f_1(x) \underset{x\to2}{=} 13 + 28(x-2) + 23(x-2)^2 + 8(x-2)^3 + o((x-2)^3)}.$$
- c) On pose $x - 1$ petit : $\ln x = \ln(1 + (x-1)) = (x-1) - \frac{(x-1)^2}{2} + o((x-1)^2)$ et $\sqrt x - 1 = \sqrt{1 + (x-1)} - 1 = \frac{x-1}{2} - \frac{(x-1)^2}{8} + o((x-1)^2)$. Le produit (le facteur $(x-1)$ commun permet de s'arrêter à l'ordre 2 dans chaque facteur) donne
$$\boxed{(\sqrt x - 1)\ln x \underset{x\to1}{=} \frac{(x-1)^2}{2} - \frac{3(x-1)^3}{8} + o((x-1)^3)}.$$

### Exercice 18 — DL en 0 de $\tan$, d'un quotient, d'une racine composée

**Énoncé.** Donner les DL en 0 de : a) $f_1(x) = \tan x$ à l'ordre 4 ; b) $f_2(x) = \frac{\ln(1+x)}{\sin x}$ à l'ordre 3 ; c) $f_3(x) = \sqrt{1 + \sqrt{1 + x^2}}$ à l'ordre 4.

**Correction.**
- a) $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} + o(x^4)$, $\sin x = x - \frac{x^3}{6} + o(x^4)$. $\frac{1}{\cos x} = \frac{1}{1-u}$ avec $u = \frac{x^2}{2} - \frac{x^4}{24} + o(x^4)$, $u^2 = \frac{x^4}{4} + o(x^4)$ :
$$\frac{1}{\cos x} = 1 + u + u^2 + o(u^2) = 1 + \frac{x^2}{2} + \frac{5x^4}{24} + o(x^4),$$
puis $\tan x = \sin x \cdot \frac{1}{\cos x} = \left(x - \frac{x^3}{6} + o(x^4)\right)\left(1 + \frac{x^2}{2} + \frac{5x^4}{24} + o(x^4)\right) = \boxed{x + \frac{x^3}{3} + o(x^4)}$.
- b) $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + o(x^4)$ et $\sin x = x - \frac{x^3}{6} + o(x^4)$. On simplifie par $x$ :
$$\frac{\ln(1+x)}{\sin x} = \left(1 - \frac x2 + \frac{x^2}{3} - \frac{x^3}{4} + o(x^3)\right)\cdot\frac{1}{1-u},\quad u = \frac{x^2}{6} + o(x^3),\ u^2 = o(x^3),$$
d'où $\left(1 - \frac x2 + \frac{x^2}{3} - \frac{x^3}{4} + o(x^3)\right)\left(1 + \frac{x^2}{6} + o(x^3)\right) = \boxed{1 - \frac x2 + \frac{x^2}{2} - \frac{x^3}{3} + o(x^3)}$.
- c) $\sqrt{1+x} = 1 + \frac x2 - \frac{x^2}{8} + o(x^2)$, donc $\sqrt{1+x^2} = 1 + \frac{x^2}{2} - \frac{x^4}{8} + o(x^4)$ et
$$\sqrt{1 + \sqrt{1+x^2}} = \sqrt{2 + \frac{x^2}{2} - \frac{x^4}{8} + o(x^4)} = \sqrt2\sqrt{1 + \frac{x^2}{4} - \frac{x^4}{16} + o(x^4)} = \sqrt2\left(1 + \frac12\left(\frac{x^2}{4} - \frac{x^4}{16}\right) - \frac18\left(\frac{x^2}{4}\right)^2 + o(x^4)\right).$$
Le corrigé conclut : $\sqrt2 + \frac{\sqrt2\,x^2}{8} - \frac{3\sqrt2\,x^4}{128} + o(x^4)$. **Le coefficient de $x^4$ est faux** : $-\frac{1}{32} - \frac{1}{128} = -\frac{5}{128}$, donc le bon résultat est $\sqrt2 + \frac{\sqrt2\,x^2}{8} - \frac{5\sqrt2\,x^4}{128} + o(x^4)$ (voir « Points à vérifier »).

### Exercice 19 — DL de fonctions composées

**Énoncé.** Donner le DL en 0 de : a) $\exp(\sin x)$ (ordre 3) ; b) $\sin(\tan x)$ (ordre 3) ; c) $(\ln(1+x))^2$ (ordre 3) ; d) $\exp(\cos x)$ (ordre 4) ; e) $\sin^6 x$ (ordre 9).

**Correction.**
- a) $e^X = 1 + X + \frac{X^2}{2!} + \frac{X^3}{3!} + o(X^3)$ avec $X = \sin x = x - \frac{x^3}{3!} + o(x^3)$ ; $\sin^2 x = x^2 + o(x^3)$, $\sin^3 x = x^3 + o(x^3)$. D'où $\exp(\sin x) = 1 + \left(x - \frac{x^3}{6}\right) + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3) = \boxed{1 + x + \frac{x^2}{2} + o(x^3)}$.
- b) $\sin X = X - \frac{X^3}{3!} + o(X^3)$ avec $X = \tan x = x + \frac{x^3}{3} + o(x^3)$ (ex. 18.a), $\tan^3 x = x^3 + o(x^3)$ : $\sin(\tan x) = x + \frac{x^3}{3} - \frac{x^3}{6} + o(x^3) = \boxed{x + \frac{x^3}{6} + o(x^3)}$.
- c) $\ln(1+x) = x - \frac12x^2 + \frac13x^3 + o(x^3)$ ; en développant le produit $\ln(1+x)\cdot\ln(1+x)$ : $\left(x^2 - \frac12x^3\right) - \frac12x^3 + o(x^3) = \boxed{x^2 - x^3 + o(x^3)}$.
- d) $\exp(\cos x) = e \cdot \exp(\cos x - 1)$, avec $\cos x - 1 = -\frac{x^2}{2} + \frac{x^4}{4!} + o(x^4)$, $(\cos x - 1)^2 = \frac{x^4}{4} + o(x^4)$, $(\cos x - 1)^3 = o(x^4)$, $(\cos x - 1)^4 = o(x^4)$ :
$$\exp(\cos x) = e\left(1 - \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^4}{8} + o(x^4)\right) = \boxed{e - \frac{e\,x^2}{2} + \frac{e\,x^4}{6} + o(x^4)}.$$
- e) $\sin^6 x = \left(x - \frac{x^3}{3!} + o(x^3)\right)^6$ ; par le [[Formule du binôme de Newton|binôme de Newton]], en commençant par les plus petits degrés : $x^6 + 6x^5\cdot\left(-\frac{x^3}{6}\right) + o(x^9) = \boxed{x^6 - x^8 + o(x^9)}$ (voir « Points à vérifier » sur l'ordre du reste).

### Exercice 20 — DL en un point $a \ne 0$

**Énoncé.** Déterminer : a) $DL_2(1)$ de $f_1(x) = \cos(\ln x)$ ; b) $DL_3\left(\frac\pi4\right)$ de $f_2(x) = \ln(\tan x)$ ; c) $DL_2(1)$ de $f_3(x) = \frac{\sqrt x - 1}{\ln x}$.

**Correction.**
- a) $x = 1 + h$ : $f_1(1+h) = \cos(\ln(1+h)) = \cos\left(h - \frac{h^2}{2} + o(h^2)\right) = 1 - \frac12\left(h - \frac{h^2}{2}\right)^2 + o(h^2)$, donc $\boxed{f_1(x) = 1 - \frac12(x-1)^2 + o((x-1)^2)}$.
- b) Par la formule de Taylor-Young ([[Reste de Taylor]]). $f_2'(x) = \frac{1 + \tan^2 x}{\tan x}$, $f_2''(x) = \frac{(1 + \tan^2 x)(\tan^2 x - 1)}{\tan^2 x} = \frac{\tan^4 x - 1}{\tan^2 x}$, puis
$$f_2'''(x) = \frac{\tan^2 x \cdot 4\tan^3 x(1 + \tan^2 x) - (\tan^4 x - 1)\,2\tan x(1 + \tan^2 x)}{\tan^4 x} = \frac{(1+\tan^2 x)\tan x\,(2 + 2\tan^4 x)}{\tan^4 x}.$$
En $\frac\pi4$ ($\tan = 1$) : $f_2 = 0$, $f_2' = 2$, $f_2'' = 0$, $f_2''' = 8$. D'où
$$\boxed{\ln\tan x = 2\left(x - \frac\pi4\right) + \frac{8}{3!}\left(x - \frac\pi4\right)^3 + o\left(\left(x - \frac\pi4\right)^3\right) = 2\left(x - \frac\pi4\right) + \frac43\left(x - \frac\pi4\right)^3 + o\left(\left(x-\frac\pi4\right)^3\right)}.$$
(Deux coquilles dans les dernières lignes du corrigé, voir « Points à vérifier ».)
- c) $x = 1 + h$ :
$$f_3(1+h) = \frac{\frac h2 - \frac{h^2}{8} + \frac{h^3}{16} + o(h^3)}{h - \frac{h^2}{2} + \frac{h^3}{3} + o(h^3)} = \frac12\left(1 - \frac h4 + \frac{h^2}{8} + o(h^2)\right)\left(1 + \left(\frac h2 - \frac{h^2}{3}\right) + \frac{h^2}{4} + o(h^2)\right)$$
$$= \frac12\left(1 - \frac h4 + \frac{h^2}{8}\right)\left(1 + \frac h2 - \frac{h^2}{12}\right) + o(h^2) = \frac12\left(1 + \frac h4 - \frac{h^2}{12}\right) + o(h^2),$$
donc $\boxed{f_3(x) = \frac12 + \frac{x-1}{8} - \frac{(x-1)^2}{24} + o((x-1)^2)}$.

### Exercice 21 — Limites par DL

**Énoncé.** Déterminer :
a) $\lim_{x\to0}(\cos x)^{1/x^2}$ ; b) $\lim_{x\to0}\left(\frac{1+x}{1-x}\right)^{1/x}$ ; c) $\lim_{x\to e}\frac{\sqrt x - \sqrt e}{\ln x - 1}$ ; d) $\lim_{x\to0}\frac{(1+3x)^{1/3} - 1 - \sin x}{1 - \cos x}$ ; e) $\lim_{x\to0}\left(\frac1x - \frac{\ln(1+x)}{x^2}\right)$ ; f) $\lim_{x\to0}\frac{1}{x^2}\ln\left(\frac{\sin x}{x}\right)$.

**Correction.**
- a) $\exp\left(\frac{1}{x^2}\ln\left(1 - \frac{x^2}{2} + o(x^2)\right)\right) = \exp\left(\frac{1}{x^2}\left(-\frac{x^2}{2} + o(x^2)\right)\right) = \exp\left(-\frac12 + o(1)\right) \to \boxed{\frac{1}{\sqrt e}}$.
- b) $\exp\left(\frac1x(\ln(1+x) - \ln(1-x))\right)$ avec $\ln(1+x) - \ln(1-x) = \left(x - \frac{x^2}{2}\right) - \left(-x - \frac{x^2}{2}\right) + o(x^2) = 2x + o(x^2)$, donc $\exp(2 + o(x)) \to \boxed{e^2}$.
- c) $x = e + (x - e)$ : $\sqrt x - \sqrt e = \sqrt e\left(\sqrt{1 + \frac{x-e}{e}} - 1\right)$ et $\ln x - 1 = \ln\left(1 + \frac{x-e}{e}\right)$. Donc
$$\frac{\sqrt e\left(\frac12\cdot\frac{x-e}{e} + o(x-e)\right)}{\frac{x-e}{e} + o(x-e)} = \frac{\sqrt e\left(\frac{1}{2e} + o(1)\right)}{\frac1e + o(1)} \to \frac{\sqrt e/(2e)}{1/e} = \boxed{\frac{\sqrt e}{2}}.$$
- d) $(1+3x)^{1/3} = 1 + \frac{3x}{3} - \frac{9x^2}{9} + o(x^2) = 1 + x - x^2 + o(x^2)$ et $\sin x = x + o(x^2)$ : le numérateur vaut $-x^2 + o(x^2)$, le dénominateur $\frac{x^2}{2} + o(x^2)$, limite $\frac{-1}{1/2} = \boxed{-2}$.
- e) $\frac{x - \ln(1+x)}{x^2} = \frac{x - \left(x - \frac{x^2}{2} + o(x^2)\right)}{x^2} = \frac12 + o(1) \to \boxed{\frac12}$.
- f) $\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + o(x^2)$, donc $\frac{1}{x^2}\ln\left(1 - \frac{x^2}{6} + o(x^2)\right) = \frac{1}{x^2}\left(-\frac{x^2}{6} + o(x^2)\right) \to \boxed{-\frac16}$.

### Exercice 22 — Tangente et position

**Énoncé.** Étudier, au voisinage de 1, la fonction $g(x) = x + 2\sqrt x - \sqrt{2 + 2x}$ : tangente, position de la courbe par rapport à cette tangente, allure de la courbe au voisinage de 1.

**Correction.** On écrit tout en $x - 1$ :
$$g(x) = 1 + (x-1) + 2\sqrt{1 + (x-1)} - 2\sqrt{1 + \tfrac{x-1}{2}}$$
$$= 1 + (x-1) + 2\left(1 + \frac{x-1}{2} - \frac{(x-1)^2}{8}\right) - 2\left(1 + \frac{x-1}{4} - \frac{(x-1)^2}{32}\right) + o((x-1)^2) = 1 + \frac{3(x-1)}{2} - \frac{3(x-1)^2}{16} + o((x-1)^2).$$
[[Tangente à une courbe|Tangente]] en 1 : $\boxed{y = 1 + \frac{3(x-1)}{2}}$. Position : $g(x) - \left(1 + \frac{3(x-1)}{2}\right) \underset{1}{\sim} -\frac{3(x-1)^2}{16} \le 0$ : **la courbe est en dessous de sa tangente** en 1. Le corrigé conclut : « la courbe a l'allure d'une droite au voisinage de 1 ».

### Exercice 23 — $\arctan$ : DL en 0 et développement asymptotique

**Énoncé.** $f(x) = \arctan x$, réciproque de la tangente ([[Fonctions trigonométriques réciproques]]), est de classe $\mathcal C^\infty$ sur $\mathbb R$, de dérivée $f'(x) = \frac{1}{1+x^2}$.
1. Donner un DL d'ordre 5 en 0 de $f$.
2. Montrer que $\forall x > 0$, $\arctan x + \arctan\frac1x = \frac\pi2$.
3. En déduire un [[Développement asymptotique|développement asymptotique]] d'ordre 3 de $f$ au voisinage de $+\infty$.

**Correction.**
1. $\arctan'(x) = \frac{1}{1+x^2} = 1 - x^2 + x^4 + o(x^4)$ ; on intègre terme à terme, avec $\arctan(0) = 0$ : $\boxed{\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} + o(x^5)}$.
2. $F(x) = \arctan x + \arctan\frac1x$ : pour $x > 0$, $F'(x) = \frac{1}{1+x^2} + \frac{1}{1 + \frac{1}{x^2}}\cdot\left(-\frac{1}{x^2}\right) = \frac{1}{1+x^2} - \frac{1}{1+x^2} = 0$. $F$ est donc constante sur $]0, +\infty[$, et $F(1) = 2\arctan 1 = 2\cdot\frac\pi4 = \frac\pi2$.
3. $\arctan x = \frac\pi2 - \arctan\frac1x$ et $\frac1x \to 0$ ; avec le $DL_3(0)$ de la question 1 :
$$\boxed{\arctan x \underset{x\to+\infty}{=} \frac\pi2 - \frac1x + \frac{1}{3x^3} + o\left(\frac{1}{x^3}\right)}.$$

### Exercice 24 — Asymptotes en $+\infty$

**Énoncé.** Rechercher si les courbes suivantes admettent une [[Asymptote oblique|asymptote]] en $+\infty$ et déterminer la position s'il y a lieu :
a) $y = \sqrt{x(x+1)}$ ; b) $y = \sqrt{\frac{x^3}{x-1}}$ ; c) $y = (x^2 - 1)\ln\left(\frac{x+1}{x-1}\right)$ ; d) $y = (x+1)\arctan(1 + 2/x)$ ; e) $y = x\arctan x\,e^{1/x}$ ; f) $y = e^{2/x}\sqrt{1+x^2}\arctan x$ ; g) $y = \sqrt{x^2 - x}\exp\left(\frac{1}{x+1}\right)$.

**Correction.** Méthode : écrire $f(x) = ax + b + \frac cx + o\left(\frac1x\right)$ (souvent en posant $u = \frac1x$ et en étudiant $\frac{f(x)}{x} = u\,f\left(\frac1u\right)$) ; la droite $y = ax + b$ est asymptote, et le signe de $\frac cx$ donne la position.
- a) $\sqrt{x(x+1)} = x\sqrt{1 + \frac1x} = x\left(1 + \frac{1}{2x} - \frac{1}{8x^2} + o\left(\frac{1}{x^2}\right)\right) = x + \frac12 - \frac{1}{8x} + o\left(\frac1x\right)$. Asymptote $\boxed{y = x + \frac12}$ ; $\sqrt{x(x+1)} - x - \frac12 \sim -\frac{1}{8x} \le 0$ pour $x > 0$ : courbe **en dessous**.
- b) Avec $u = \frac1x$ : $\frac{f(x)}{x} = u\sqrt{\frac{1/u^3}{1/u - 1}} = \frac{1}{\sqrt{1-u}} = 1 + \frac u2 + \frac{3u^2}{8} + o(u^2)$. Donc $\frac{f(x)}{x} = 1 + \frac{1}{2x} + \frac{3}{8x^2} + o\left(\frac{1}{x^2}\right)$ et $\sqrt{\frac{x^3}{x-1}} = x + \frac12 + \frac{3}{8x} + o\left(\frac1x\right)$. Asymptote $\boxed{y = x + \frac12}$ ; écart $\sim \frac{3}{8x} \ge 0$ : courbe **au-dessus**.
- c) Avec $u = \frac1x$ : $\frac{f(x)}{x} = u\left(\frac{1}{u^2} - 1\right)\ln\left(\frac{1/u + 1}{1/u - 1}\right) = (1 - u^2)\frac1u\left(\ln(1+u) - \ln(1-u)\right)$
$$= (1-u^2)\frac1u\left(2u + \frac{2u^3}{3} + o(u^3)\right) = (1 - u^2)\left(2 + \frac{2u^2}{3} + o(u^2)\right) = 2 - \frac{4u^2}{3} + o(u^2).$$
D'où $(x^2-1)\ln\frac{x+1}{x-1} = 2x - \frac{4}{3x} + o\left(\frac1x\right)$. Asymptote $\boxed{y = 2x}$ ; écart $\sim -\frac{4}{3x} \le 0$ : courbe **en dessous**.
- d) **Non corrigé** dans le document.
- e) $e^{1/x} = 1 + \frac1x + \frac{1}{2x^2} + o\left(\frac{1}{x^2}\right)$ et (ex. 23) $\arctan x = \frac\pi2 - \frac1x + o\left(\frac{1}{x^2}\right)$. Donc
$$x\arctan x\,e^{1/x} = \left(\frac{\pi x}{2} - 1 + o\left(\tfrac1x\right)\right)\left(1 + \frac1x + \frac{1}{2x^2} + o\left(\tfrac{1}{x^2}\right)\right) = \frac{\pi x}{2} + \frac\pi2 - 1 + \frac{\frac\pi4 - 1}{x} + o\left(\frac1x\right).$$
Asymptote $\boxed{y = \frac{\pi x}{2} + \frac\pi2 - 1}$ ; écart $\sim \frac{\frac\pi4 - 1}{x} \le 0$ : courbe **en dessous**.
- f) $e^{2/x} = 1 + \frac2x + \frac{2}{x^2} + o\left(\frac{1}{x^2}\right)$ et $\sqrt{1+x^2} = x\sqrt{1 + \frac{1}{x^2}} = x + \frac{1}{2x} + o\left(\frac1x\right)$, dont le produit vaut $x + 2 + \frac{5}{2x} + o\left(\frac1x\right)$. En multipliant par $\frac\pi2 - \frac1x + o\left(\frac{1}{x^2}\right)$ :
$$e^{2/x}\sqrt{1+x^2}\arctan x = \frac{\pi x}{2} + \pi - 1 + \frac{\frac{5\pi}{4} - 2}{x} + o\left(\frac1x\right).$$
Asymptote $\boxed{y = \frac{\pi x}{2} + \pi - 1}$ ; écart $\sim \frac{\frac{5\pi}{4} - 2}{x} \ge 0$ : courbe **au-dessus**.
- g) **Non corrigé** dans le document.

## Méthodes de résolution

**Équivalents de suites et de fonctions**
- Règle d'or : $u \sim v \iff u = v + o(v)$.
- Pour un équivalent d'un produit, d'un quotient ou d'une puissance, on remplace chaque facteur par son équivalent. Pour une **somme ou une différence**, on ne peut pas remplacer terme à terme : on factorise le terme dominant, ou on passe par la forme $\sqrt{1+u} = 1 + u/2 + o(u)$ puis on regroupe, ou on multiplie par la quantité conjuguée (ex. 2.4 : $\sqrt{n^3+2n^2} - \sqrt{n^3+n^2} \sim \sqrt n / 2$).
- Piège de l'ex. 2.3 : $\sqrt{1 + u} - 1 \sim u/2$ exige $u \to 0$. Pour $\sqrt{1 + \sqrt n}$, on a simplement $1 + \sqrt n \sim \sqrt n$, donc $w_n \sim n^{1/4}$.
- Pour un logarithme : $\ln(n + \sqrt{n^2+1}) = \ln n + \ln(1 + \sqrt{1 + 1/n^2})$, où le second terme tend vers $\ln 2$, négligeable devant $\ln n$.

**Vrai ou faux (ex. 1)**
- $o$ implique $O$ (un quotient qui converge est borné) ; $O$ dans les deux sens n'implique pas $\sim$ (contre-exemple $1$ et $2$) ; $u_n \sim v_n$ donne $u_n - v_n = o(v_n)$ mais pas $u_n - v_n \to 0$ (contre-exemple $n+1$ et $n$) ; $3^n/n = O(2^n)$ est faux car $(3/2)^n/n \to +\infty$ par croissances comparées.

**Ex. 5 et 6 (suites)**
- $\sum_{k=0}^n k! \sim n!$ : retirer les deux derniers termes et majorer chacun des $n-1$ autres ($k \le n-2$) par $\frac{(n-2)!}{n!} = \frac{1}{n(n-1)}$, d'où une somme $\le \frac1n$, puis gendarmes. Piège : « chaque terme tend vers 0 » ne suffit pas pour que la somme tende vers 0.
- Ex. 6 : encadrer $2n\,s_n$ entre $n(s_n + s_{n+1})$ et $n(s_{n-1} + s_n)$ grâce à la décroissance, puis gendarmes ; le contre-exemple $\frac1{2n} + \frac{(-1)^n}{\sqrt n}$ vérifie les hypothèses sauf la monotonie.

**Équivalents de fonctions**
- Ex. 10 : $e^f \sim e^g$ en $a$ si et seulement si $f - g \to 0$. Donc $f \sim g$ n'implique pas $e^f \sim e^g$ (exemple $x^2 + x$ et $x^2$ en $+\infty$).
- Ex. 11 : $f \sim g$, strictement positives, avec $\lim f \ne 1$, alors $\ln f \sim \ln g$ : on écrit $\frac{\ln f - \ln g}{\ln f} = \ln\frac{f}{g} \cdot \frac{1}{\ln f}$. La condition $\lim f \ne 1$ est nécessaire.
- Ex. 7 à 9 et 12 : se ramener aux équivalents usuels ($\sin x \sim x$, $1 - \cos x \sim x^2/2$, $\tan x - \sin x \sim x^3/2$, $\ln(1+u) \sim u$), changer de variable pour les limites en un point $a \ne 0$, passer à l'exponentielle pour les formes $1^\infty$.

**Développements limités**
- Ex. 13 : $\sqrt x$ n'a qu'un DL d'ordre 0 en 0 (continue, non dérivable).
- Ex. 14 : $e^{-1/x}$ ($0$ pour $x \le 0$) est négligeable devant toute puissance de $x$ : son DL est nul à tout ordre sans que la fonction soit nulle. Donc des DL égaux à tout ordre n'impliquent pas des fonctions égales. $x^3 \sin(1/x)$ a un DL d'ordre 2 (nul) mais pas de dérivée seconde en 0 : **un DL d'ordre $n$ n'implique pas que $f$ soit $n$ fois dérivable** (le sens réciproque, Taylor-Young, est le bon).
- Ex. 16 : développer $x^3/(1 + x^6) = \sum (-1)^k x^{3+6k}$, puis identifier avec Taylor par unicité : $f^{(n)}(0) = (-1)^{(n-3)/6}\, n!$ si $n \equiv 3 \pmod 6$, et $0$ sinon.
- Ex. 17 à 20 : DL en un point $a \ne 0$ par $x = a + h$ ; composée par substitution ; produit en tronquant à l'ordre voulu ; quotient par $1/(1+u)$.
- Ex. 22 : tangente = partie d'ordre $\le 1$ du DL ; position = signe du premier terme non nul suivant (ici $-\frac{3}{16}(x-1)^2 \le 0$ : la courbe est sous sa tangente).
- Ex. 23 : DL de $\arctan$ par intégration du DL de $1/(1+x^2)$ ; $\arctan x + \arctan(1/x) = \pi/2$ pour $x > 0$ donne le développement asymptotique en $+\infty$.
- Ex. 24 : asymptote oblique en $+\infty$ : écrire $f(x) = ax + b + \frac{c}{x} + o(1/x)$ par DL en $u = 1/x$ ; la position est donnée par le signe de $c$ (ex. $\sqrt{x(x+1)} = x + \frac12 - \frac{1}{8x} + \dots$ : courbe sous l'asymptote $y = x + 1/2$).

## Points à vérifier

Relevés en relisant le corrigé ; rien n'a été corrigé dans les sections ci-dessus sans être signalé.

- **Ex. 18 c) — erreur de calcul** : le corrigé donne $-\frac{3\sqrt2\,x^4}{128}$ comme terme d'ordre 4 de $\sqrt{1+\sqrt{1+x^2}}$. Le calcul donne $\frac12\cdot\left(-\frac{1}{16}\right) - \frac18\cdot\frac{1}{16} = -\frac{5}{128}$, donc $-\frac{5\sqrt2\,x^4}{128}$ (confirmé numériquement : en $x = 0{,}01$, le quotient du reste par $x^4$ vaut $\approx -0{,}0552 = -\frac{5\sqrt2}{128}$, et non $-0{,}0331$).
- **Ex. 20 b) — deux coquilles** : la dernière simplification de $f_2'''$ écrit $\frac{2(1+\tan^2 x)^2\tan x}{\tan^3 x}$, alors que $\frac{(1+\tan^2 x)\tan x(2 + 2\tan^4 x)}{\tan^4 x} = \frac{2(1+\tan^2 x)(1+\tan^4 x)}{\tan^3 x}$ ($(1+\tan^2)^2 \ne 1 + \tan^4$). La valeur en $\frac\pi4$ reste $8$. Puis la dernière ligne écrit $\frac{4(x - \pi/4)^2}{3}$ au lieu de $\frac{4(x - \pi/4)^3}{3}$ (la ligne précédente a bien l'exposant 3).
- **Ex. 8 c) non corrigé** : la solution numérotée « 3 » traite en fait la limite d). Pour mémoire (calcul hors corrigé) : $\ln(e+x) = 1 + \ln\left(1 + \frac xe\right)$ donne $\frac1x\ln(\ln(e+x)) \to \frac1e$, d'où une limite $e^{1/e}$, à confirmer.
- **Ex. 24 d) et g) non corrigés** : le corrigé passe de c) à e) (« 4. » traite e), « 5. » traite f)) et ne traite pas g).
- **Ex. 9 h) — coquille** : l'avant-dernière ligne écrit $\lim \frac{x^2}{x^2+1}$ au lieu de $\frac{x^2}{x(x+1)} = \frac{x^2}{x^2+x}$ ; la limite (1) et le résultat ($-1$) ne changent pas.
- **Ex. 7 f)** : le corrigé affirme que $l$ est continue sur $\mathbb R^*$. Or le dénominateur $\ln(7x^2) + 2x$ s'annule pour un $x \approx 0{,}284$ ; $l$ est bien continue au voisinage de $\pi$ (dénominateur non nul), ce qui suffit pour le résultat.
- **Ex. 11** : le corrigé s'arrête au calcul de $\lim \frac{1}{\ln f}$ sans conclure (il manque : $\frac fg \to 1$ donc $\ln\frac fg \to 0$, et le produit tend vers 0). Le cas « $\ell \in \mathbb R \setminus \{0,1\}$ » devrait être $\ell \in\, ]0, +\infty[ \setminus \{1\}$, puisque $f > 0$.
- **Ex. 19 e) — ordre du reste** : avec $\sin x = x - \frac{x^3}{6} + o(x^3)$, le produit ne donne qu'un $o(x^8)$. Pour obtenir $o(x^9)$, il faut écrire $\sin x = x - \frac{x^3}{6} + o(x^4)$ (le terme en $x^4$ est nul). Le résultat $x^6 - x^8 + o(x^9)$ est juste.
- **Ex. 19 b)** : la ligne finale écrit $o(\tan(x))$ au lieu de $o(\tan^3 x)$ (coquille).
- **Ex. 14.2** : « $f$ admet le D.L à l'ordre 2 » désigne $g$ (coquille).
- **Ex. 13 c)** : le corrigé parle de « la limite $\lim_{x\to0^+}\frac{|x|^n}{x^n}$ », alors que l'argument porte sur la limite bilatérale en 0 (à droite elle existe et vaut 1). Le cas $n = 0$ n'est pas discuté.
- **Ex. 3 a)** : l'énoncé dit $x \in \mathbb R$, la correction suppose $x \in \mathbb R^*$ ($x = 0$ est immédiat : $a_n = 1$). **Ex. 3 b)** : la limite 1 est donnée sans justification.
- **Ex. 12 c)** : le résultat $\frac{a^3}{b^3}$ suppose implicitement $a, b \ne 0$.
- **Ex. 15** : le corrigé n'a que deux parties pour trois questions (le DL d'ordre 2 est obtenu dans la partie 1, la dérivabilité dans la partie 2).
- **Ex. 22** : la conclusion « la courbe a l'allure d'une droite au voisinage de 1 » est celle du corrigé ; le DL montre aussi que la courbe est localement sous sa tangente (terme $-\frac{3}{16}(x-1)^2$).
- Coquilles mineures sans effet : « deriner » pour « dernier » (ex. 5), « $f(x) ==$ » et « $+ =$ » (ex. 20 a).

## Liens

[[Comparaison asymptotique]], [[Équivalent (comparaison asymptotique)]], [[Croissances comparées]], [[Quantité conjuguée]], [[Théorème des gendarmes]], [[Développement limité]], [[Développement asymptotique]], [[Reste de Taylor]], [[Limite et continuité]], [[Prolongement par continuité]], [[Dérivabilité]], [[Fonction de classe Ck]], [[Tangente à une courbe]], [[Asymptote oblique]], [[Fonctions trigonométriques réciproques]], [[Formule du binôme de Newton]], [[Suite numérique]].
