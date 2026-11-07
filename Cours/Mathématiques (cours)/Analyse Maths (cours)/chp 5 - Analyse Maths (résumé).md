---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Analyse Maths/Cours/chp5.docx|chp5 (Analyse)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 1/Analyse Maths/Cours/chp5.docx|chp5 (Analyse)]] (chapitre 5, « Analyse asymptotique »), dans [[Analyse Maths (index)]]. En cas d'écart, le cours et ses images font foi. Les images de la note ne contiennent que des énoncés et des formules : leur contenu est recopié ci-dessous, sans les intégrer.

Dans cette note, plusieurs formules en image sont décalées par rapport au texte qu'elles complètent, par exemple « Alors : » après sa formule. C'est un effet de la mise en page d'origine ; la fiche remet chaque formule à sa place.

## 1. Suites : définitions et opérations

Voir [[Comparaison asymptotique]]. On suppose $(v_n)$ non nulle à partir d'un certain rang.

| Notation | Définition | Lecture |
|---|---|---|
| $u_n = O(1)$ | $(u_n)$ est bornée | « $u_n$ est un grand O de 1 » |
| $u_n = O(v_n)$ | $u_n = v_n \times O(1)$, c'est-à-dire $\dfrac{u_n}{v_n}$ est bornée | « $u_n$ est dominée par $v_n$ » |
| $u_n = o(1)$ | $u_n \to 0$ | « $u_n$ est un petit o de 1 » |
| $u_n = o(v_n)$ | $u_n = v_n \times o(1)$, c'est-à-dire $\dfrac{u_n}{v_n} \to 0$ | « $u_n$ est négligeable devant $v_n$ » |

Remarques du cours :

- une suite qui converge vers 0 est bornée, donc $u_n = o(v_n) \Rightarrow u_n = O(v_n)$ ;
- le signe « = » de ces notations ne se lit que de gauche à droite : $o(x) = o(y)$ ne permet pas d'écrire $o(y) = o(x)$ (le cours note « o(x) = o(y) ≠ o(y) = o(x) »).

**Propriété (addition et multiplication)**. Soient $(u_n), (v_n), (w_n), (t_n)$ quatre suites, $(w_n)$ et $(t_n)$ ne s'annulant pas à partir d'un certain rang, et $(\lambda, \mu) \in \mathbb{K}^2$.

1. Si $u_n = O(w_n)$ et $v_n = O(w_n)$, alors $\lambda u_n + \mu v_n = O(w_n)$. Si $u_n = o(w_n)$ et $v_n = o(w_n)$, alors $\lambda u_n + \mu v_n = o(w_n)$.
2. Si $u_n = O(w_n)$ et $v_n = O(t_n)$, alors $u_n v_n = O(w_n t_n)$. Si $u_n = O(w_n)$ et $v_n = o(t_n)$, alors $u_n v_n = o(w_n t_n)$.

**Propriété (transitivité)**. Soient $(u_n), (v_n), (w_n)$ trois suites.

1. Si $u_n = O(v_n)$ et $v_n = O(w_n)$, alors $u_n = O(w_n)$.
2. Si $u_n = o(v_n)$ et $v_n = o(w_n)$, alors $u_n = o(w_n)$.

**Propriété ([[Croissances comparées]], suites)**. Soient $\alpha, \beta > 0$ et $q > 1$. Alors

$$q^{-n} = o\!\left(\frac{1}{n^\alpha}\right),\quad \frac{1}{n^\alpha} = o(\ln^\beta n),\quad \ln^\beta n = o(n^\alpha),\quad n^\alpha = o(q^n),\quad q^n = o(n!),\quad n! = o(n^n).$$

En notant $u_n \ll v_n$ pour $u_n = o(v_n)$, quand $n \to +\infty$ :

$$\frac{1}{n!} \ll q^{-n} \ll \frac{1}{n^\alpha} \ll \ln^\beta n \ll n^\alpha \ll q^n \ll n! \ll n^n.$$

## 2. Suites : équivalents

**Définition** : $u_n \sim v_n \iff \dfrac{u_n}{v_n} \to 1$. Voir [[Équivalent (comparaison asymptotique)]].

- Si $u_n \sim \ell$ (avec $\ell \ne 0$), alors $u_n \to \ell$ en $+\infty$.
- $\sim$ est une relation d'équivalence (de même pour deux fonctions $f$ et $g$) :
  - réflexive : $u_n \sim u_n$ ;
  - symétrique : $u_n \sim v_n \Rightarrow v_n \sim u_n$ ;
  - transitive : $u_n \sim v_n$ et $v_n \sim w_n \Rightarrow u_n \sim w_n$.

**Propriété**. Soient $(u_n), (v_n)$.

1. $u_n \sim v_n \iff u_n - v_n = o(v_n)$.
2. $u_n \sim v_n \implies u_n = O(v_n)$ et $v_n = O(u_n)$.

**Propriété (multiplication, quotient, puissance)**. Si $u_n \sim w_n$ et $v_n \sim t_n$ :

1. $u_n v_n \sim w_n t_n$ ;
2. $\dfrac{u_n}{v_n} \sim \dfrac{w_n}{t_n}$ ;
3. $\forall p \in \mathbb{N}$, $u_n^p \sim w_n^p$.

**Remarques (pièges)** :

- on ne peut ni ajouter ni soustraire des équivalents ;
- on ne compose pas les équivalents : $u_n \sim v_n$ n'entraîne pas forcément $f(u_n) \sim f(v_n)$ ;
- pour élever un équivalent à une puissance, l'exposant doit être constant (pas dépendre de $n$).

**Propriété (même signe et même [[Limite et continuité|limite]])**. Si $u_n \sim v_n$ :

1. $u_n$ et $v_n$ ont le même signe strict ($> 0$ ou $< 0$) à partir d'un certain rang ;
2. $(u_n)$ admet une limite (finie ou infinie) si et seulement si $(v_n)$ en admet une, et alors $\lim u_n = \lim v_n$.

## 3. Fonctions : définitions et opérations

Mêmes notions au [[Boule et voisinage|voisinage]] d'un point $a$ (réel ou $\pm\infty$) :

| Notation | Définition |
|---|---|
| $f \underset{a}{=} O(1)$ | $f$ est bornée au voisinage de $a$ |
| $f(x) \underset{a}{=} O(g(x))$ | $\dfrac{f}{g}$ est bornée au voisinage de $a$ |
| $f \underset{a}{=} o(1)$ | $f$ converge vers 0 au voisinage de $a$ |
| $f(x) \underset{a}{=} o(g(x))$ | $\displaystyle\lim_{x \to a} \frac{f(x)}{g(x)} = 0$ |

**Propriété (croissances comparées, fonctions)**. Soit $(\alpha, \beta) \in (\mathbb{R}_+^*)^2$ :

$$(\ln x)^\beta \underset{+\infty}{=} o(x^\alpha),\qquad x^\beta \underset{+\infty}{=} o(e^{\alpha x}),\qquad |\ln x|^\beta \underset{0}{=} o\!\left(\frac{1}{x^\alpha}\right),\qquad e^{\alpha x} \underset{-\infty}{=} o\!\left(\frac{1}{x^\beta}\right).$$

## 4. Fonctions : équivalents

**Définition** : $f \underset{a}{\sim} g \iff \displaystyle\lim_{x \to a} \frac{f(x)}{g(x)} = 1$.

**Remarques** :

- si $f$ est continue en $a$ et $f(a) \ne 0$, alors $f(x) \underset{a}{\sim} f(a)$ ;
- si $f$ est [[Dérivabilité|dérivable]] en $a$ et $f'(a) \ne 0$, alors $f(x) - f(a) \underset{a}{\sim} f'(a)(x - a)$.

**Propriété ([[Polynôme|polynômes]])**. Si $P(x) = a_p x^p + a_{p-1}x^{p-1} + \ldots + a_q x^q$ avec $p \ge q$ (et $a_p, a_q \ne 0$), alors

$$P(x) \underset{+\infty}{\sim} a_p x^p \qquad\text{et}\qquad P(x) \underset{0}{\sim} a_q x^q.$$

Un polynôme est équivalent à son terme de plus haut degré en $+\infty$, à son terme de plus bas degré en 0.

**Propriété**. Soient $f$ et $g$ définies sur $\mathcal{D}$.

- $f(x) \underset{a}{\sim} g(x) \iff f(x) - g(x) \underset{a}{=} o(g(x))$ ;
- $f(x) \underset{a}{\sim} g(x) \implies f(x) \underset{a}{=} O(g(x))$ et $g(x) \underset{a}{=} O(f(x))$.

**Propriété (opérations)**. Si $f \underset{a}{\sim} g$ et $h \underset{a}{\sim} u$ :

1. $fh \underset{a}{\sim} gu$ ;
2. $\dfrac{f}{h} \underset{a}{\sim} \dfrac{g}{u}$ ;
3. $\forall p \in \mathbb{N}$, $f^p \underset{a}{\sim} g^p$ ;
4. pour $\alpha \in \mathbb{R}_+^*$, si $f^\alpha$ et $g^\alpha$ sont bien définies sur $\mathcal{D}$, $f^\alpha \underset{a}{\sim} g^\alpha$.

**Propriété (équivalents classiques en 0)** (voir aussi [[Fonctions hyperboliques]]) :

| Équivalent en 0 | |
|---|---|
| $e^x - 1 \sim x$ | $\ln(1 + x) \sim x$ |
| $\sin x \sim x$ | $\tan x \sim x$ |
| $\arcsin x \sim x$ | $\arctan x \sim x$ |
| $\operatorname{sh} x \sim x$ | $\operatorname{th} x \sim x$ |
| $(1 + x)^\alpha - 1 \sim \alpha x$, $\alpha \in \mathbb{R}^*$ | |
| $1 - \cos x \sim \dfrac{x^2}{2}$ | $1 - \operatorname{ch} x \sim -\dfrac{x^2}{2}$ |

**Propriété (composition à droite dans un équivalent)**. Soit $f \underset{a}{\sim} g$, avec $g$ qui ne s'annule pas au voisinage de $a$. Soit $\varphi$ une fonction telle que $\displaystyle\lim_{t \to b} \varphi(t) = a$, avec $b \in \mathbb{R} \cup \{\pm\infty\}$. Alors

$$f \circ \varphi(t) \underset{b}{\sim} g \circ \varphi(t).$$

(On peut remplacer la variable par une fonction qui tend vers $a$ : c'est la [[Composition de fonctions|composition]] « à droite ».)

**Propriété (composition par ln et exp)** :

- si $f \sim g$ et que la limite de $g$ (au point considéré) est différente de 1, alors $\ln f \sim \ln g$ ;
- si $f \sim g$ et $\lim (f - g) = 0$, alors $e^f \sim e^g$.

**Attention** : il ne faut pas additionner, soustraire ou composer à gauche des équivalents sans justifier : les résultats sont généralement faux.

**Propriété (même signe et même limite)**. Soient $f, g : \mathcal{D} \to \mathbb{R}$ avec $f \underset{a}{\sim} g$.

1. Si $g$ est de signe constant strict au voisinage de $a$, $f$ est de même signe strict que $g$ au voisinage de $a$.
2. Si $g$ admet une limite finie ou infinie en $a$, alors $f$ aussi et $\lim_a f = \lim_a g$.

## 5. Développements limités

### Définition

$f$ admet un [[Développement limité]] en $a$ à l'ordre $n$, noté $DL_n(a)$, s'il existe $(a_0, \ldots, a_n) \in \mathbb{K}^{n+1}$ tels que

$$f(x) \underset{x \to a}{=} a_0 + a_1(x - a) + \cdots + a_n(x - a)^n + o\big((x - a)^n\big).$$

Le polynôme $a_0 + \dots + a_n(x-a)^n$ est la **partie régulière** du DL.

**Propriété (retour en 0)**. $f$ admet un $DL_n(a)$ si et seulement si $g : h \mapsto f(a + h)$ admet un $DL_n(0)$, et

$$f(x) \underset{x \to a}{=} \sum_{k=0}^{n} a_k (x - a)^k + o((x - a)^n) \iff g(h) = f(a + h) \underset{h \to 0}{=} \sum_{k=0}^{n} a_k h^k + o(h^k).$$

Le cours écrit bien $o(h^k)$ ; il faut lire $o(h^n)$ (voir « Points à vérifier »).

### Propriétés

- **Unicité** : si $f$ admet un $DL_n(a)$, il est unique.
- **Troncature** : si $f$ admet un $DL_n(a)$, alors pour tout $p \in [\![0, n]\!]$, $f$ admet un $DL_p(a)$, obtenu en tronquant le DL à l'ordre $p$ :
$$f(x) \underset{x \to a}{=} a_0 + a_1(x - a) + \cdots + a_p(x - a)^p + o((x - a)^p).$$
- **Parité** ([[Fonction paire et impaire]]) : si $f$ est paire et admet un $DL_n(0)$, ce DL ne contient que des termes pairs ; si $f$ est impaire, que des termes impairs.

**Propriété (DL et équivalent)**. Supposons que $f$ admet un $DL_n(a)$ de partie régulière non nulle, $f(x) = a_0 + a_1(x-a) + \ldots + a_n(x-a)^n + o((x-a)^n)$. En notant $p$ le plus petit entier tel que $a_p \ne 0$ :

$$f(x) \underset{x \to a}{\sim} a_p (x - a)^p.$$

Conséquence : $f$ est du même signe strict que le premier terme non nul de son DL (au voisinage de $a$).

### Primitivation

**Théorème**. Soient $I$ un intervalle et $g \in \mathcal{D}(I, \mathbb{R})$. Si $g'(x) \underset{x \to a}{=} o((x - a)^n)$, alors $g(x) \underset{x \to a}{=} g(a) + o((x - a)^{n+1})$.

**Théorème (primitivation des DL)**. Soient $I$ un intervalle, $f \in \mathcal{D}(I, \mathbb{R})$ et $a \in I$. Si $f'$ possède un $DL_n(a)$ :

$$f'(x) \underset{x \to a}{=} \sum_{k=0}^{n} a_k (x - a)^k + o((x - a)^n),\quad a_0, \ldots, a_n \in \mathbb{R},$$

alors $f$ possède un $DL_{n+1}(a)$ :

$$f(x) \underset{x \to a}{=} f(a) + \sum_{k=0}^{n} a_k \frac{(x - a)^{k+1}}{k+1} + o((x - a)^{n+1}).$$

On primitive terme à terme ([[Primitive]]), sans oublier la constante $f(a)$.

### Existence : formule de Taylor-Young

**Théorème (formule générale de Taylor-Young)**. Soient $I$ un intervalle, $n \in \mathbb{N}$, $f \in \mathcal{C}^n(I, \mathbb{R})$ ([[Fonction de classe Ck]]) et $a \in I$. Alors $f$ possède un $DL_n(a)$ et

$$f(x) \underset{x \to a}{=} \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k + o((x - a)^n).$$

Liens avec la régularité :

- continuité en $a$ $\iff$ existence d'un $DL_0(a)$ ;
- dérivabilité en $a$ $\iff$ existence d'un $DL_1(a)$ ;
- classe $\mathcal{C}^n$ $\Rightarrow$ existence d'un $DL_n(a)$ (sans réciproque).

### Opérations sur les DL

On suppose que $f$ et $g$ admettent des $DL_n(0)$ : $f(x) = P_n(x) + o(x^n)$ et $g(x) = Q_n(x) + o(x^n)$.

**[[Combinaison linéaire]] et produit** :

1. pour tous $\lambda, \mu \in \mathbb{K}$, $(\lambda f + \mu g)(x) \underset{x \to 0}{=} (\lambda P_n + \mu Q_n)(x) + o(x^n)$ ;
2. $(fg)(x) \underset{x \to 0}{=} T_n(PQ)(x) + o(x^n)$, où $T_n(PQ)$ est la troncature à l'ordre $n$ du polynôme $PQ$.

**Composition**. Si $f : I \to J$ et $g : J \to \mathbb{K}$ ont des $DL_n(0)$, $f(x) = P_n(x) + o(x^n)$ et $g(x) = Q_n(x) + o(x^n)$, et si $\lim_{x \to 0} f(x) = 0$, alors

$$g \circ f(x) = T_n(Q_n \circ P_n)(x) + o(x^n).$$

**Quotient**. Si $f$ et $g$ ont des $DL_n(0)$ et que $g$ a une limite non nulle en 0, alors $f/g$ admet un $DL_n(0)$.

**Remarque (quotient quand $g \to 0$)**. Le quotient peut encore avoir un DL. Si $f$ et $g$ ont des DL de formes normalisées (le cours écrit $x^{n_1}$, $x^{n_2}$ en facteur ; voir « Points à vérifier »)

$$f(x) = x^{p_1}\left(a_{p_1} + a_{p_1+1}x + \ldots + a_{n_1}x^{n_1 - p_1} + o(x^{n_1 - p_1})\right),$$
$$g(x) = x^{p_2}\left(b_{p_2} + b_{p_2+1}x + \ldots + b_{n_2}x^{n_2 - p_2} + o(x^{n_2 - p_2})\right),$$

avec $a_{p_1}, b_{p_2} \ne 0$, alors

$$\frac{f(x)}{g(x)} = x^{p_1 - p_2}\, \underbrace{\frac{a_{p_1} + a_{p_1+1}x + \ldots + o(x^{n_1 - p_1})}{b_{p_2} + b_{p_2+1}x + \ldots + o(x^{n_2 - p_2})}}_{= h(x)}.$$

Comme $b_{p_2} \ne 0$, $h$ possède un DL (proposition précédente), de terme constant $\dfrac{a_{p_1}}{b_{p_2}} \ne 0$. Donc $f/g$ admet un DL si et seulement si $p_1 - p_2 \in \mathbb{N}$, c'est-à-dire $p_2 \le p_1$, et son ordre est $\min(n_1 - p_1, n_2 - p_2)$.

### DL en l'infini et asymptote oblique

**Définition**. Soit $f : I \to \mathbb{R}$ définie au voisinage de $\pm\infty$. $f$ possède un $DL_n(\pm\infty)$ si la fonction $g : u \mapsto f(1/u)$ possède un $DL_n(0)$.

**Définition**. $f$ admet une [[Asymptote oblique]] en $\pm\infty$ s'il existe $(a, b) \in \mathbb{R}^2$ tel que $f(x) - ax - b \to 0$ en $\pm\infty$ ; la droite $y = ax + b$ est l'asymptote.

## 6. Développements limités usuels (en 0)

$$\frac{1}{1 - x} = \sum_{k=0}^{n} x^k + o(x^n) = 1 + x + x^2 + \ldots + x^n + o(x^n)$$

$$\ln(1 + x) = \sum_{k=1}^{n} (-1)^{k-1}\frac{x^k}{k} + o(x^n) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \ldots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$$

$$e^x = \sum_{k=0}^{n} \frac{x^k}{k!} + o(x^n) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \ldots + \frac{x^n}{n!} + o(x^n)$$

$$(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2}x^2 + \frac{\alpha(\alpha - 1)(\alpha - 2)}{6}x^3 + \ldots + \frac{\alpha(\alpha - 1)\cdots(\alpha - n + 1)}{n!}x^n + o(x^n)$$

$$\sin x = \sum_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{(2k+1)!} + o(x^{2n+1}) = x - \frac{x^3}{6} + \frac{x^5}{120} - \ldots + (-1)^n\frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+1})$$

$$\cos x = \sum_{k=0}^{n} (-1)^k \frac{x^{2k}}{(2k)!} + o(x^{2n}) = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \ldots + (-1)^n\frac{x^{2n}}{(2n)!} + o(x^{2n})$$

$$\operatorname{Arctan} x = \sum_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{2k+1} + o(x^{2n+1}) = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \ldots + (-1)^n\frac{x^{2n+1}}{2n+1} + o(x^{2n+1})$$

$$\tan x = x + \frac{x^3}{3} + o(x^3)$$

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Fausses alertes des transcriptions** : deux mentions « À vérifier » de cette note sont à ignorer. $\frac{1}{n^\alpha} = o(\ln^\beta n)$ est bien vrai, car le quotient tend vers 0. « En tronquant à l'ordre $p$ » est bien correct. Le seul défaut réel est $(\alpha, \beta) \in \mathbb{R}$, à lire $\mathbb{R}^2$.
2. **Quotient de DL** : les formes normalisées mettent en facteur $x^{n_1}$ et $x^{n_2}$. Le quotient utilisant $x^{p_1 - p_2}$, il faut lire $x^{p_1}$ et $x^{p_2}$ (complément). La fiche écrit $x^{p_1}$, $x^{p_2}$.
3. **Signe** : « $f$ est du même signe strict que le premier terme non nul » vaut seulement au voisinage de $a$.
4. **Composition par ln** : « lim g (+∞) ≠ 1 » porte sur la limite au point étudié, pas seulement en $+\infty$ (complément).
5. **Polynômes** : dans l'énoncé en image, la parenthèse « ($p \geq q$ » n'est pas fermée et il manque un « + » avant $a_q x^q$ ; il faut aussi $a_p \ne 0$ et $a_q \ne 0$ pour que les équivalents aient un sens (complément).
6. **Premier théorème de primitivation** : la ligne de l'image est coupée à droite, la parenthèse finale de $o((x-a)^{n+1})$ est peut-être incomplète. Le cours le titre « primitivation des développements limités » comme le suivant.
7. **Second théorème de primitivation** : le bas de l'image de l'hypothèse est coupé (ligne tronquée avec $(x-a)^{k+1}$) ; la conclusion est lisible dans l'image suivante.
8. **$u_n \sim \ell \Rightarrow u_n \to \ell$** : le cours n'écrit pas la condition $\ell \ne 0$, nécessaire car on ne peut pas être équivalent à 0 (complément).
9. **« o(x) = o(y) ≠ o(y) = o(x) »** : notation de l'étudiant, interprétée ici comme le sens unique de lecture du signe « = » ; à confirmer.
10. **Retour en 0** : le cours écrit $g(h) = \sum_{k=0}^{n} a_k h^k + o(h^k)$ (vérifié sur l'image). L'indice $k$ est muet hors de la somme : il faut lire $o(h^n)$, comme dans le membre de gauche $o((x-a)^n)$. Mention « À vérifier » de la transcription.
