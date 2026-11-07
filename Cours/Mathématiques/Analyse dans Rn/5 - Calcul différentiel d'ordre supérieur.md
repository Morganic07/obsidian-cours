---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]], dans [[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]]. En cas d'écart, le cours et ses images font foi.

## 1. Différentiation d'ordre supérieur ou égal à 2

Pour $f$ de deux variables, les dérivées partielles d'ordre 2 sont
$$f''(x, y) = \left(\frac{\partial^2 f}{\partial x^2}\ ;\ \frac{\partial^2 f}{\partial y^2}\ ;\ \frac{\partial^2 f}{\partial x\partial y}\ ;\ \frac{\partial^2 f}{\partial y\partial x}\right),$$
avec par exemple
$$\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right), \qquad \frac{\partial^2 f}{\partial y\partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right).$$
Le cours écrit la dérivée croisée comme limite :
$$\frac{\partial^2 f}{\partial y\partial x} = \lim_{t \to 0}\frac1t\left[\left.\frac{\partial f}{\partial x}\right|_{x,\,y+t} - \left.\frac{\partial f}{\partial y}\right|_{x,\,y+t}\right]$$
(second terme erroné, voir Erreurs du cours : on attend $\left.\frac{\partial f}{\partial x}\right|_{x,y}$). Voir [[Dérivée partielle]].

> **Définition 2 (classe $\mathcal C^k$, $\mathcal C^\infty$)** : soit $U$ un [[Ouvert et fermé|ouvert]] de $\mathbb R^p$ et $f : U \to \mathbb R^n$. $f$ est de classe $\mathcal C^k$ sur $U$ si et seulement si toutes ses dérivées partielles d'ordre $k$ existent et sont continues sur $U$. $f$ est de classe $\mathcal C^\infty$ si et seulement si elle est $\mathcal C^k$ pour tout $k \in \mathbb N$ ([[Fonction de classe Ck]]).

> **Propriété 1** : si $f$ est $\mathcal C^k$ sur $U$, toutes ses dérivées partielles d'ordre **inférieur ou égal** à $k$ sont définies et continues.

Notes de cours :
- $f$ de classe $\mathcal C^k$ $\iff$ les composantes de $f$ sont $\mathcal C^k$ ;
- $f$ de classe $\mathcal C^k$ $\Rightarrow$ les dérivées partielles de $f$ sont continues jusqu'à l'ordre $k$ inclus.

> **Théorème 1 (stabilité de $\mathcal C^k$ par composition)** : soit $f$ de classe $\mathcal C^k$ de $U$ (ouvert de $\mathbb R^p$) dans $\mathbb R^q$, et $g$ de classe $\mathcal C^k$ de $V$ (ouvert de $\mathbb R^q$) dans $\mathbb R^n$. Si $f(U) \subset V$, alors $g \circ f$ est $\mathcal C^k$ sur $U$.

> **Théorème 2** : soit $f : U \to \mathbb R^n$ (le cours écrit « une application $\mathcal C^k$ », voir Erreurs du cours). Sont équivalents :
> 1. $f$ est de classe $\mathcal C^k$ ;
> 2. les fonctions coordonnées de $f$ dans la base de $\mathbb R^n$ sont de classe $\mathcal C^k$.

> **Théorème 3 ([[Théorème de Schwarz]])** : soit $f$ de classe $\mathcal C^1$ de $U$ (ouvert de $\mathbb R^p$) dans $\mathbb R^q$, $a \in U$ et $(i, j) \in [\![1, p]\!]^2$. Si $\frac{\partial^2 f}{\partial x_j\partial x_i}$ et $\frac{\partial^2 f}{\partial x_i\partial x_j}$ sont définies et continues en $a$, alors
> $$\left.\frac{\partial^2 f}{\partial x_j\partial x_i}\right|_a = \left.\frac{\partial^2 f}{\partial x_i\partial x_j}\right|_a.$$

Remarques du cours :
- si $f$ est $\mathcal C^2$, les dérivées croisées sont continues, donc Schwarz s'applique : être $\mathcal C^2$ est une [[Condition nécessaire et suffisante|condition suffisante]] mais non nécessaire ;
- si $f$ n'est pas $\mathcal C^2$, cela ne veut pas dire que les dérivées croisées ne sont pas égales ;
- la condition « être $\mathcal C^2$ » est trop forte pour Schwarz : seule la [[Limite et continuité|continuité]] des dérivées croisées est requise.

## 2. Systèmes d'EDP d'ordre 1

On résout un système d'[[Équation aux dérivées partielles|équations aux dérivées partielles]]
$$\left.\frac{\partial f}{\partial x}\right|_{x,y} = g(x, y), \qquad \left.\frac{\partial f}{\partial y}\right|_{x,y} = h(x, y),$$
avec $g$, $h$ de classe $\mathcal C^1$.

**Étape 1 : condition de compatibilité.** Vérifier que
$$\left.\frac{\partial g}{\partial y}\right|_{x,y} = \left.\frac{\partial h}{\partial x}\right|_{x,y}.$$
Justification : si $g$ et $h$ sont $\mathcal C^1$, leurs dérivées partielles sont continues, donc $\frac{\partial^2 f}{\partial x^2} = \frac{\partial g}{\partial x}$, $\frac{\partial^2 f}{\partial y^2} = \frac{\partial h}{\partial y}$, $\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial h}{\partial x}$ et $\frac{\partial^2 f}{\partial y\partial x} = \frac{\partial g}{\partial y}$ sont continues : $f$ est $\mathcal C^2$ et vérifie Schwarz, $\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial^2 f}{\partial y\partial x}$, d'où $\frac{\partial g}{\partial y} = \frac{\partial h}{\partial x}$.

**Étape 2** : résoudre l'une des deux EDP, par exemple la première : $f(x, y) = G(x, y) + K_1(y)$, où $G$ est une [[Primitive|primitive]] de $g$ selon $x$ et $K_1$ une fonction quelconque $\mathcal C^2$.

**Étape 3** : dériver cette solution par rapport à l'autre variable (ici $y$) et l'injecter dans l'EDP non encore utilisée : on obtient une équation sur $K_1$.

**Étape 4** : résoudre l'équation de l'étape 3.

**Étape 5** : écrire la solution en combinant les étapes 2 et 4.

### Exemple complet

Résoudre sur $\mathbb R^2$ :
$$\begin{cases}
\left.\dfrac{\partial f}{\partial x}\right|_{x,y} = (x + 1)\cos(x + y) + \sin(x + y) - \sin x = g(x, y) \\[2mm]
\left.\dfrac{\partial f}{\partial y}\right|_{x,y} = (x + 1)\cos(x + y) = h(x, y)
\end{cases}$$

1. **Compatibilité** : $\dfrac{\partial g}{\partial y} = -(x + 1)\sin(x + y) + \cos(x + y) = \dfrac{\partial h}{\partial x}$ : le système admet des solutions.
2. **Intégrer la seconde EDP par rapport à $y$** (plus simple) : $f(x, y) = (x + 1)\sin(x + y) + K_1(x)$, avec $K_1$ de classe $\mathcal C^2$ sur $\mathbb R$.
3. **Dériver par rapport à $x$** : $\dfrac{\partial f}{\partial x} = \sin(x + y) + (x + 1)\cos(x + y) + K_1'(x)$. On injecte dans la première EDP :
$$\sin(x + y) + (x + 1)\cos(x + y) + K_1'(x) = (x + 1)\cos(x + y) + \sin(x + y) - \sin x,$$
d'où $K_1'(x) = -\sin x$ (le cours écrit $\partial K_1/\partial x$).
4. **Intégrer** : $K_1(x) = \cos x + C$, $C \in \mathbb R$.
5. **Solution** :
$$f(x, y) = (x + 1)\sin(x + y) + \cos x + C, \qquad C \in \mathbb R.$$

## 3. EDP d'ordre 2

La démarche est la même qu'à l'ordre 1 : utiliser des changements de variables pour se ramener à une EDP dont on connaît la solution.

> **Théorème 4** : soit $U$ un ouvert de $\mathbb R^2$. Les solutions de classe $\mathcal C^2$ de $\dfrac{\partial^2 f}{\partial x^2} = 0$ sont de la forme
> $$f(x, y) = xG(y) + H(y),$$
> où $G$ et $H$ sont $\mathcal C^2$ sur la projection de $U$ sur l'axe $Oy$.

> **Théorème 5** : soit $U$ un ouvert de $\mathbb R^2$. Les solutions de classe $\mathcal C^2$ de $\dfrac{\partial^2 f}{\partial x\partial y} = 0$ sont de la forme
> $$f(x, y) = G(x) + H(y),$$
> où $G$ et $H$ sont $\mathcal C^2$ sur les projections de $U$ sur les axes $Ox$ et $Oy$ respectivement.

Le cours ne donne pas d'exemple d'EDP d'ordre 2 dans cette note.

## Erreurs du cours

- [[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]] écrit $\frac{\partial^2 f}{\partial y\partial x} = \lim_{t \to 0}\frac1t\left[\left.\frac{\partial f}{\partial x}\right|_{x,\,y+t} - \left.\frac{\partial f}{\partial y}\right|_{x,\,y+t}\right]$ ; il faut $\lim_{t \to 0}\frac1t\left[\left.\frac{\partial f}{\partial x}\right|_{x,\,y+t} - \left.\frac{\partial f}{\partial x}\right|_{x,\,y}\right]$.
- Théorème 2 : le cours écrit « soit $f$ une application $\mathcal C^k$ » en hypothèse d'une équivalence dont le premier énoncé est « $f$ est de classe $\mathcal C^k$ » ; il faut « soit $f$ une application de $U$ dans $\mathbb R^n$ ».
