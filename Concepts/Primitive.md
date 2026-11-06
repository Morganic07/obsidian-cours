---
type: concept
aliases: [primitives, théorème fondamental de l’analyse, théorème fondamental de l'analyse, primitives usuelles, tableau des primitives]
matieres: [Analyse, Analyse Maths, Probability]
sources: ["[[Chap7-Integration]]", "[[démonstrations - integration]]", "[[Intégration UTILITAIRE]]"]
maj: 2026-11-06
---

Une primitive de $f$, continue sur l'intervalle $I$, est une fonction $F$ de classe $\mathcal{C}^1$ telle que $F' = f$. Deux primitives diffèrent d'une constante.

**Théorème fondamental de l'analyse** : $x \mapsto \int_a^x f(t)\,dt$ est l'unique primitive de $f$ nulle en $a$. Pour toute primitive $F$, $\int_a^x f(t)\,dt = F(x) - F(a)$. La preuve de [[démonstrations - integration]] repose sur la continuité de $f$ en $x_0$.

**Techniques** :

- **Bornes variables** : si $g(x) = \int_{u(x)}^{v(x)} f$, alors $g'(x) = f(v(x))v'(x) - f(u(x))u'(x)$.
- **[[Intégration par parties]]** : $\int_a^b f'g = [fg]_a^b - \int_a^b fg'$.
- **[[Changement de variable dans une intégrale|Changement de variable]]** $x = \varphi(t)$ : $\int_{\varphi(a)}^{\varphi(b)} f(x)\,dx = \int_a^b f(\varphi(t))\varphi'(t)\,dt$. Il faut changer la variable, $dx$ et les bornes.

**Primitives usuelles** :

- $x^\alpha \to \frac{x^{\alpha+1}}{\alpha+1}$ pour $\alpha \neq -1$, et $\frac{1}{x} \to \ln|x|$
- $e^x \to e^x$, et $\ln x \to x\ln x - x$
- $\sin x \to -\cos x$, $\cos x \to \sin x$, et $\tan x \to -\ln|\cos x|$
- $\frac{1}{u^2 + a^2} \to \frac{1}{a}\arctan\frac{u}{a}$
- $\frac{u'}{u} \to \ln|u|$, $u'u^n \to \frac{u^{n+1}}{n+1}$, $\frac{u'}{\sqrt{u}} \to 2\sqrt{u}$, et $u'e^u \to e^u$
- la fiche [[Intégration UTILITAIRE]] ajoute $\int u'\ln u = u\ln u - u + C$

**Fractions rationnelles** : [[Décomposition en éléments simples|décomposer]] en partie entière et éléments simples, $\frac{\gamma}{(x - x_0)^k}$ ou $\frac{\alpha x + \beta}{(ax^2 + bx + c)^k}$ avec $b^2 - 4ac < 0$. On se ramène à $\ln$, $\arctan$, et à $I_k = \int\frac{du}{(u^2 + 1)^k}$ par parties.

**Fonctions trigonométriques, [[Règles de Bioche]]** : avec $\omega(x) = f(x)\,dx$, si $\omega(-x) = \omega(x)$, poser $u = \cos x$. Si $\omega(\pi - x) = \omega(x)$, poser $u = \sin x$. Si $\omega(\pi + x) = \omega(x)$, poser $u = \tan x$. Sinon, $t = \tan(x/2)$ fonctionne toujours, avec $\cos x = \frac{1 - t^2}{1 + t^2}$, $\sin x = \frac{2t}{1 + t^2}$ et $dx = \frac{2\,dt}{1 + t^2}$.

Les exercices de [[TD7-integration (1) (résumé)|TD7]] appliquent ces techniques (changements de variable, intégrations par parties répétées, fractions rationnelles). En Probability, la [[Fonction de répartition]] $F(x) = \int_{-\infty}^x f(y)\,dy$ est une primitive de la densité $f$ ([[Chp 5 - Continuous random variable (résumé)]]).

Notion parente : [[Intégrale]]. Voir aussi : [[Intégration par parties]], [[Changement de variable dans une intégrale]], [[Règles de Bioche]], [[Décomposition en éléments simples]], [[Dérivabilité]], [[Fonction de classe Ck]], [[Équation aux dérivées partielles]]

## À vérifier

- [[Chap7-Integration]] (point 2 du résumé) écrit « La primitive de $f$ est toute fonction » : il faudrait « Une primitive ».

Résumés : [[Chap7-Integration (résumé)]], [[démonstrations - integration (résumé)]], [[Intégration UTILITAIRE (résumé)]], [[TD7-integration (1) (résumé)]], [[Chp 5 - Continuous random variable (résumé)]]
