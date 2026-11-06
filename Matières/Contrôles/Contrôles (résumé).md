---
type: source
tags: [year1]
sources: [".raw/Year 1/Contrôles.pdf"]
maj: 2026-11-06
complet: true
---

Résumé de `.raw/Year 1/Contrôles.pdf` (35 pages, scan photographié, sans texte), lu en image. Ce sont des énoncés de contrôles de la 1re année (DD Ingénieur-Designer / PréING1, 2022-2023), **sans corrigé**. Le PDF est découpé en trois blocs par des pages de titre : **Analyse** (pages 1 à 17), **Algèbre** (pages 18 à 28) et **Informatique** (pages 29 à 35). Des annotations manuscrites (coches, brouillons) figurent sur les copies : elles ne sont pas reprises. Pour l'analyse, voir aussi [[Analyse Maths (matière)]] ; pour l'algèbre, [[Outil Maths (matière)]] et [[Algèbre linéaire (matière)]].

Aucun énoncé n'est corrigé dans le document : les indications de méthode données sous chaque devoir sont un complément, pas une correction du cours.

# Analyse (8 devoirs surveillés)

Tous portent l'en-tête « DD ING-Design », « L'usage de tout appareil électronique est interdit ». L'ordre suit le cours : réels, suites, limites de fonctions, continuité, dérivabilité, équivalents, DL. Chaque DS commence par des définitions ou théorèmes à connaître par cœur (quantificateurs compris), puis des calculs, puis un exercice de synthèse.

## DS1, Analyse I (24 octobre 2022, 1 h 30, pages 2-3)

**Exercice 1.** Trouver le domaine de définition puis résoudre dans $\mathbb{R}$ :
1. $\dfrac{x-2}{x+1} \le 1$ ;
2. $\sqrt{2x^2 - 4} \ge x + 1$.

**Exercice 2.** Résoudre dans $\mathbb{R}$ :
1. $\cos\left(3x - \frac{\pi}{3}\right) = \cos(x)$ ;
2. $\sin\left(2x - \frac{\pi}{4}\right) = -\cos(x)$.

**Exercice 3.** Calculer la somme et le produit :
1. $S = \displaystyle\sum_{k=1}^{n} \ln\left(1 + \frac1k\right)$ ;
2. $P = \displaystyle\prod_{k=2}^{n} \left(1 - \frac{1}{k^2}\right)$.

**Exercice 4.** Soit $A$ une partie de $\mathbb{R}$ ; donner la définition de : (1) $A$ est majoré, respectivement minoré ; (2) la borne supérieure, respectivement inférieure, de $A$ ; (3) le plus grand, respectivement le plus petit élément de $A$.

**Exercice 5.** Pour chaque ensemble, dire s'il est majoré, minoré, et déterminer s'ils existent bornes supérieure et inférieure, plus grand et plus petit élément :
1. $A = \left\{\dfrac{1}{n+1},\ n \in \mathbb{N}\right\}$ ;
2. $B = \left\{\dfrac{2^n}{2^n - 1},\ n \in \mathbb{N}^*\right\}$.

Méthodes : domaine puis tableau de signe, ou élévation au carré avec condition de signe ; $\cos a = \cos b$ ; [[Somme télescopique]] ($\ln(1 + 1/k) = \ln(k+1) - \ln k$) ; sup et inf (voir [[Borne supérieure]], [[Majorant et minorant]], [[Plus grand élément]]).

## DS2, Analyse I (28 novembre 2022, 1 h 30, pages 4-5)

**Exercice 1.** Donner la définition : (1) d'une suite décroissante ; (2) d'une suite bornée ; (3) avec les quantificateurs, de « la limite de la suite $(u_n)_{n \in \mathbb{N}}$ vaut $-\infty$ » ; (4) de deux suites adjacentes.

**Exercice 2.** Déterminer, si elle existe, la limite de :
1. $a_n = \sqrt{n^3 + 2} - \sqrt{n^3 + 3n}$ ;
2. $b_n = \dfrac{e^{2n} + 2^n}{e^n + 1}$ ;
3. $c_n = n\left(3^{1/n} - 1\right)$, en utilisant $\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x} = 1$ ;
4. $d_n = \dfrac{n^2 + (-1)^n}{n^2 - \ln(n) + \sin(n)}$ ;
5. $e_n = 2^n e^{-n}$.

**Exercice 3.** Déterminer, si elle existe, la limite de $u_n = (-1)^n n$ et de $v_n = \sin\left(n\frac{\pi}{3}\right)$.

**Exercice 4.** Soit $u_n = \displaystyle\sum_{k=1}^{n} \frac{(-1)^k}{k!}$. On pose $a_n = u_{2n}$ et $b_n = u_{2n+1}$. Montrer, à l'aide de ces deux suites, que $(u_n)$ est convergente.

**Exercice 5.** Déterminer la limite de la suite complexe $z_n = \dfrac{2n+3}{5n^2 - 1} + i\,\dfrac{3n^2 + (-1)^n}{n^2 + 1}$.

Méthodes : [[Quantité conjuguée]], factorisation du terme dominant, limite usuelle $(e^x - 1)/x \to 1$ (avec $3^{1/n} = e^{\ln 3 / n}$), divergence par deux sous-suites de limites différentes, [[Suites adjacentes]] ; une suite complexe converge si ses parties réelle et imaginaire convergent ([[Suite complexe]]). Voir [[Suite numérique]].

## DS3, Analyse I (16 janvier 2023, 1 h 30, pages 6-7)

**Exercice 1.**
1. Donner la définition exacte, avec les quantificateurs, de : a) $\displaystyle\lim_{x \to a} f(x) = \ell$, où $a$ et $\ell$ sont réels ; b) $\displaystyle\lim_{x \to a} f(x) = +\infty$.
2. Donner le théorème du prolongement par continuité d'une fonction $f$ en un point $a$.

**Exercice 2.** Calculer :
1. $\displaystyle\lim_{x \to +\infty} \sqrt{x^2 + 2x} - x$ ;
2. $\displaystyle\lim_{x \to 0^+} \frac{\sqrt x - x}{\sqrt x + x}$ ;
3. $\displaystyle\lim_{x \to 2} \frac{x^2 - 4}{-x^2 + 3x - 2}$ ;
4. $\displaystyle\lim_{x \to 1} \left(\frac{3}{x^3 - 1} - \frac{2}{x^2 - 1}\right)$ ;
5. $\displaystyle\lim_{x \to +\infty} \sqrt{x + \sqrt x} - \sqrt x$.

**Exercice 3.** Les fonctions suivantes sont-elles prolongeables par continuité ?
1. $f(x) = \sin(x)\sin\left(\frac1x\right)$ ;
2. $g(x) = \dfrac{e^{\sin(x)} - 1}{x}$ ;
3. $h(x) = \dfrac{1}{1-x} - \dfrac{2}{1-x^2}$.

Méthodes : quantité conjuguée, factorisation (racines du trinôme), réduction au même dénominateur, théorème des gendarmes pour $\sin x \sin(1/x)$. Voir [[Limite et continuité]], [[Prolongement par continuité]].

## DS4, Analyse I (30 janvier 2023, 1 h 30, pages 8-9)

**Exercice 1.** Donner : (1) le théorème de la bijection ; (2) le théorème des valeurs intermédiaires (TVI) ; (3) le théorème du prolongement par continuité d'une fonction $f$ en un point $a$.

**Exercice 2.** Calculer :
1. $\displaystyle\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$ ;
2. $\displaystyle\lim_{x \to 1} \frac{x^2 - 3x + 2}{-2x^2 - 4x + 6}$ ;
3. $\displaystyle\lim_{x \to 1} \frac{\ln(x)}{\sqrt x - 1}$ ;
4. $\displaystyle\lim_{x \to +\infty} \left(\sqrt{e^{2x} + e^x + 1} - e^x\right)$.

**Exercice 3.** Les fonctions suivantes sont-elles prolongeables par continuité ? $f(x) = \dfrac{\ln(1+x)}{x}$ ; $g(x) = x + \dfrac{\sqrt{x^2}}{x}$.

**Exercice 4.** Soit $n \in \mathbb{N}^*$ et $f_n$ définie sur $[0, 1]$ par $f_n(x) = 1 - \dfrac{x}{2} - x^n$.
1. Montrer qu'il existe un unique $x_n \in [0, 1]$ tel que $f_n(x_n) = 0$.
2. Montrer que pour tout $n \in \mathbb{N}^*$, $f_{n+1}(x_n) > 0$.
3. En déduire que $(x_n)$ est monotone et converge vers une limite $L$.
4. a) Si l'on suppose $L \neq 1$, calculer $f_n(x_n)$ et en déduire une contradiction. b) Donner alors la valeur de $L$.

Méthodes : quantité conjuguée ; TVI et stricte monotonie pour l'unicité ([[Théorème des valeurs intermédiaires]], [[Bijection]]) ; $f_{n+1}(x_n) > 0 = f_{n+1}(x_{n+1})$ et décroissance de $f_{n+1}$ donnent la monotonie ; suite monotone bornée convergente ; $\sqrt{x^2} = |x|$ pour $g$.

## DS5, Analyse II (31 mars 2023, 1 h 30, pages 10-11)

**Exercice 1.** Donner : (1) la [[Formule de Leibniz]] ; (2) le théorème de Rolle ; (3) le théorème des accroissements finis.

**Exercice 2.** Calculer :
1. $\displaystyle\lim_{x \to 4} \frac{\sqrt x - 2}{x - 4}$ ;
2. $\displaystyle\lim_{x \to \pi/2} \frac{e^{\cos(x)} - 1}{x - \frac{\pi}{2}}$ ;
3. $\displaystyle\lim_{x \to -1} \frac{x^3 + 5x^2 + 7x + 3}{2 - \sqrt{x^2 - x + 2}}$ ;
4. $\displaystyle\lim_{x \to +\infty} \left(1 + \frac1x\right)^x$.

**Exercice 3.** Calculer la dérivée $n$-ième de : (1) $f : x \mapsto a^x$, où $a \in \mathbb{R}_+^*$ ; (2) $g : x \mapsto (x^3 + 2x - 7)e^x$.

**Exercice 4.**
1. Soit $P(X) = X^4 - 2X - 1$. Montrer que ce polynôme admet au plus trois racines réelles distinctes.
2. Soient $a, b$ réels avec $0 < a < b$ et $n \ge 2$ entier. À l'aide du théorème des accroissements finis appliqué à $f(x) = x^n$ sur $[a, b]$, montrer que
$$na^{n-1}(b - a) \le b^n - a^n \le nb^{n-1}(b - a).$$

Méthodes : reconnaître un nombre dérivé (taux d'accroissement) ; $(1 + 1/x)^x = e^{x\ln(1 + 1/x)}$ ; Leibniz pour la dérivée $n$-ième d'un produit ; Rolle appliqué à $P$ puis à $P'$ pour borner le nombre de racines ([[Théorème de Rolle]]) ; théorème des accroissements finis pour l'encadrement (voir [[Inégalité des accroissements finis]]). Voir [[Dérivabilité]].

## DS6, Analyse II (12 mai 2023, 1 h 30, pages 12-13)

**Exercice 1.** Donner la définition : (1) de deux suites équivalentes ; (2) de « $f$ est négligeable devant $g$ au voisinage d'un point $a$ ».

**Exercice 2.** Calculer :
1. $\displaystyle\lim_{x \to 0} \frac{\sin(x)}{x + 3x^2}$ ;
2. $\displaystyle\lim_{x \to 0} \frac{x\sin(x)}{1 - \cos(x)}$ ;
3. $\displaystyle\lim_{x \to 0} \frac{4e^{x^2} - 1}{\ln(\cos(x))}$ ;
4. $\displaystyle\lim_{x \to +\infty} \sqrt{4x + 1}\,\ln\left(1 - \frac{\sqrt{x+1}}{x+2}\right)$ ;
5. $\displaystyle\lim_{x \to +\infty} \left(\ln(1 + e^{-x})\right)^{1/x}$.

**Exercice 3.** Donner un équivalent simple de :
1. $\ln(\sin x)$ en 0 ;
2. $\ln(\cos x)$ en 0 ;
3. $\sqrt{\sin(x)} - \sqrt{\tan(x)}$ en 0 ;
4. $u_n = \dfrac{\ln(n^3 + n)}{n + 4}$ ;
5. $u_n = \dfrac{1}{n+2} - \dfrac{1}{n+4} - \dfrac{2}{n^2}$ (exposant du dernier terme peu lisible, voir « Points à vérifier ») ;
6. $\sqrt{n^2 + 2n + 3} - \sqrt{n^2 + n + 1}$.

Méthodes : équivalents usuels ($\sin x \sim x$, $1 - \cos x \sim x^2/2$, $\ln(1+u) \sim u$), produits et quotients d'équivalents, ne pas sommer des équivalents. Voir [[Comparaison asymptotique]], [[Équivalent (comparaison asymptotique)]].

## DS7, Analyse II (16 juin 2023, 1 h 30, pages 14-15)

**Exercice 1.** Soit $a \in \mathbb{R}$.
1. Donner le DL en 0 à l'ordre 2 de $f : x \mapsto \sqrt{1+x}$.
2. Donner le DL en 0 à l'ordre 2 de $g : x \mapsto e^{ax}$.
3. En déduire pour quelles valeurs de $a$ la fonction $h : x \mapsto \dfrac{\sqrt{1+x} - e^{ax}}{x^2}$ a une limite finie en 0, et préciser cette limite.

**Exercice 2.** Donner un équivalent simple aux points indiqués :
1. $\dfrac{\ln(1+x) - \sin(x)}{x}$ en 0 ;
2. $\dfrac{\cos(x) - \sqrt{1 - x^2}}{x^4}$ en 0 ;
3. $\dfrac{e^{x^2} - \cos(x)}{x^2}$ en 0 ;
4. $\dfrac{e^x - 1}{x\ln(x+1) - x^2}$ en 0 ;
5. la même fonction $\dfrac{e^x - 1}{x\ln(x+1) - x^2}$ en $+\infty$.

**Exercice 3.** Donner le DL : (1) de $x \mapsto \frac1x$ en 2 à l'ordre 3 ; (2) de $x \mapsto \sqrt x$ en 1 à l'ordre 3 ; (3) de $x \mapsto e^{\sqrt x}$ en 1 à l'ordre 3.

**Exercice 4.** Déterminer l'asymptote oblique et la position de la courbe par rapport à cette asymptote pour $f : x \mapsto e^{1/x}\sqrt{1 + x^2}$.

Méthodes : DL pour lever une indétermination ([[Développement limité]]) ; DL en $a \neq 0$ par $x = a + h$ ; [[Asymptote oblique]] par un DL en $+\infty$ (poser $t = 1/x$), le signe du terme suivant donnant la position.

## DS8, Analyse II (26 juin 2023, 2 h, pages 16-17)

**Exercice 1.** Soit $a \in \mathbb{R}$.
1. Donner le DL en 0 à l'ordre 2 de $f : x \mapsto \dfrac{e^x + e^{ax} - 2}{x^2}$.
2. En déduire pour quelles valeurs de $a$ la fonction $f$ a une limite finie en 0, et préciser cette limite.

**Exercice 2.** Donner un équivalent simple aux points indiqués :
1. $\dfrac{\sin(x) - x}{x^3}$ en 0 ;
2. $\dfrac{1 + \ln(1+x) - e^x}{1 - \cos(x)}$ en 0 ;
3. $\dfrac{(1 + 3x)^{1/3} - 1 - \sin(x)}{1 - \cos(x)}$ en 0 ;
4. $\dfrac{2x}{\ln\left(\frac{1+x}{1-x}\right)}$ en 0 ;
5. $2e^x - \sqrt{1 + 4x} - \sqrt{1 + 6x^2}$ en 0 ;
6. $\sqrt{x^2 + 1} - 2\sqrt[3]{x^3 + x} + \sqrt[4]{x^4 + x^2}$ en $+\infty$.

**Exercice 3.** Donner le DL de : (1) $f : x \mapsto \sqrt{1 + \sin(x)}$ en 0 à l'ordre 3 ; (2) $g_1 : x \mapsto \dfrac{xe^{-x}}{1 + 2x}$ en 0 à l'ordre 3 ; (3) $g_2 : x \mapsto \ln(x + 3)$ en 0 à l'ordre 3 ; (4) $h : x \mapsto \dfrac{\ln(x)}{x}$ en 3 à l'ordre 2.

**Exercice 4.** Soit $f(x) = x\sqrt{\dfrac{x-1}{x+1}}$. Montrer que $f$ possède une asymptote oblique en $+\infty$, en donner l'équation, et déterminer la position relative de la courbe par rapport à cette asymptote.

Méthodes : combiner les DL à l'ordre juste nécessaire, repérer les annulations du terme principal ; $\ln(x+3) = \ln 3 + \ln(1 + x/3)$.

# Algèbre (Outils mathématiques et Algèbre linéaire)

## Outils mathématiques, DS1 (vendredi 28 octobre 2022, 1 h 40, pages 19-20)

« Il sera tenu compte de la qualité de la rédaction et de la précision des justifications. » Sept exercices, dans l'ordre souhaité.

**Exercice 1 (2 points).** Dire si les phrases suivantes sont des propositions ; si oui, écrire leur négation : (1) P = « toute personne dans cette salle possède un téléphone portable » ; (2) Q = « pour tout $x$ dans $\mathbb{R}$, il existe $y$ dans $\mathbb{R}$ tel que $x = 2y$ ».

**Exercice 2 (4 points).** Soit $f$ définie sur $\mathbb{R}$ à valeurs dans $\mathbb{R}$. Écrire avec les quantificateurs : (1) $f$ prend toujours la valeur 1 ; (2) $f$ prend au moins une fois la valeur 1 ; (3) $f$ prend ses valeurs entre 2 et 3 ; (4) $f$ ne prend que des valeurs entières ; (5) $f$ s'annule au moins une fois sur $[-1, 1]$. Voir [[Quantificateur]].

**Exercice 3 (4 points).** Soient $P, Q, R$ des propositions. Montrer l'équivalence $[P \Rightarrow (Q \Rightarrow R)] \iff [(P \text{ et } Q) \Rightarrow R]$. Voir [[Équivalence logique]], [[Implication logique]].

**Exercice 4 (4 points).** Démontrer que pour $x, y$ réels : $(x \neq y) \Rightarrow \big((x+1)(y-1) \neq (x-1)(y+1)\big)$ (une [[Preuve par contraposition]] convient).

**Exercice 5 (4 points).**
1. Soient $A, B, C$ trois ensembles ; montrer que $A \cap C = A \cup B \iff B \subset A \subset C$.
2. Soient $E, F$ deux ensembles ; montrer que $\mathcal{P}(E) \cup \mathcal{P}(F) \subset \mathcal{P}(E \cup F)$.

**Exercice 6 (4 points).** Démontrer que $\forall n \ge 5$, $2^n > n^2$ ([[Récurrence]]).

**Exercice 7 (6 points).** Soit $E$ non vide et $A, B, C, D \in \mathcal{P}(E)$. Montrer que :
1. $(A \setminus B) \setminus C = A \setminus (B \cup C)$ ;
2. $(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D)$ ;
3. Soient $E = \{1, 2, 3, 4\}$, $A = \{1, 2, 3\}$, $B = \{3, 4\}$. Donner les éléments de : a) $A \times B$ ; b) $(E \setminus A) \times B$ ; c) $A \times (E \setminus B)$ ; d) $(E \setminus A) \times (E \setminus B)$ ; e) $(E \times E) \setminus (A \times B)$.

Voir [[Logique propositionnelle]], [[Opérations sur les ensembles]], [[Différence d'ensembles]], [[Produit cartésien]].

## Outils mathématiques, DS2 (vendredi 9 décembre 2022, 1 h 30, pages 21-22)

En-tête « DD-DESIGN ». Cinq exercices.

**Exercice 1 (2 points).** Soit $f : E \to F$. Donner la définition d'une fonction injective (« $f$ est injective si et seulement si… ») et surjective.

**Exercice 2 (5 points).** Soit $f : E \to F$.
1. Soient $C, D \subset F$ : démontrer $f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D)$.
2. Soit $A \subset E$. (a) Montrer que $\forall A \subset E$, $A \subset f^{-1}(f(A))$. (b) Montrer que $f$ injective $\iff A = f^{-1}(f(A))$.

**Exercice 3 (7 points).** Soient $f : \mathbb{R} \to \mathbb{R}^2,\ x \mapsto (x^2, 2x)$ et $g : \mathbb{R}^2 \to \mathbb{R},\ (a, b) \mapsto a - b + 1$.
1. Étude de $f$ : (a) injectivité ; (b) surjectivité.
2. Étude de $g$ : (a) injectivité ; (b) surjectivité ; (c) déterminer $g([0,1] \times [0,1])$.
3. Composées : (a) pour $x \in \mathbb{R}$, déterminer $(f \circ g)(x)$ ; (b) pour $(a, b) \in \mathbb{R}^2$, déterminer $(g \circ f)(x)$ ; (c) étudier la surjectivité de $f \circ g$ ; (d) étudier l'injectivité de $g \circ f$.
4. (a) Déterminer $h([-1, 2])$ ; (b) déterminer $h^{-1}([-2, 4])$.

**Exercice 4 (4 points).** Soient $f : E \to F$ et $g : F \to G$. Montrer : (1) $g \circ f$ surjective $\Rightarrow g$ surjective ; (2) $g \circ f$ injective et $f$ surjective $\Rightarrow g$ injective.

**Exercice 5 (5 points).** Soit $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2 - 1$.
1. $f$ est-elle injective ? surjective ?
2. Soit $g : [1, +\infty[ \to [0, +\infty[$, $g(x) = x^2 - 1$ : montrer que $g$ est bijective et donner l'expression de sa fonction inverse.

Voir [[Injectivité et surjectivité]], [[Image et image réciproque]], [[Composition de fonctions]], [[Bijection]].

## Outils mathématiques I, DS2 (vendredi 27 janvier 2023, 1 h 30, page 23)

**Exercice 1.** Sur $\mathbb{R}$, $xRy \iff x^2 - y^2 = x - y$. Montrer que $R$ est une relation d'équivalence, calculer la classe d'un élément $x$ ; combien d'éléments a-t-elle ? (Cet exemple est traité dans [[Chapitre3-Relation binaire (résumé)|le cours]] : $\mathrm{Cl}(x) = \{x, 1 - x\}$.)

**Exercice 2.** Sur $\mathbb{R}$, $xRy$ si $xy \ge 0$. (1) $R$ est-elle réflexive ? symétrique ? transitive ? (2) Est-ce une relation d'équivalence ? une relation d'ordre (total ou partiel) ?

**Exercice 3.** Sur $\mathbb{C}$, $zRz' \iff |z| = |z'|$. (1) Montrer que $R$ est une relation d'équivalence. (2) Déterminer la classe de $z \in \mathbb{C}$.

**Exercice 4.** Soient $z_1 = e^{i\pi/3}$ et $z_2 = e^{-i\pi/4}$. (1) Écrire $z_1$ et $z_2$ sous forme algébrique. (2) Déterminer les formes algébrique, exponentielle et trigonométrique de $z_1 z_2$. (3) En déduire les valeurs exactes de $\cos(\pi/12)$ et $\sin(\pi/12)$.

**Exercice 5.** Résoudre dans $\mathbb{C}$ : $z^2 + z + 1 = 0$.

Voir [[Relation d'équivalence]], [[Relation binaire]], [[Nombre complexe]], [[Forme trigonométrique et exponentielle]].

## Outils mathématiques (février 2023, 1 h 30, page 24)

En-tête « DD DESIGN 1ère année ». Cinq exercices.

**Exercice 1 (7 points).** Soient $P, Q \in \mathbb{C}[X]$ :
$$P(X) = X^7 - iX^6 + iX^4 + X^3 + (-1 + i)X + 1 + i, \qquad Q(X) = X - i.$$
1. Calculer $P(i)$, $Q(i)$. Que peut-on en déduire ?
2. Effectuer la division euclidienne de $P$ par $Q$.
3. Résoudre dans $\mathbb{C}$ l'équation $(E) : X^6 + iX^3 - 1 + i = 0$.
4. En déduire toutes les racines de $P$ dans $\mathbb{C}$.

**Exercice 2 (5 points).** Factoriser dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$ : $P(X) = X^3 + 3X^2 - 5X + 1$ (indication : trouver une racine évidente) et $Q(X) = X^4 + 1$.

**Exercice 3 (5 points).** (1) Calculer une forme exponentielle de $\dfrac{1 + i\sqrt3}{\sqrt2 + i\sqrt2}$. (2) En déduire $\cos(\pi/12)$ et $\sin(\pi/12)$.

**Exercice 4 (4 points).** Résoudre dans $\mathbb{C}$ : $Z^2 + (-1 + 2i)Z + 1 + 5i = 0$.

**Exercice 5 (5 points).** I. Linéariser $\sin^4 x$, $x \in \mathbb{R}$. II. Soit $a \in \mathbb{R}$. (1) Exprimer $\cos(5a)$ en fonction de $\cos a$ et $\sin(5a)$ en fonction de $\sin a$. (2) En utilisant $\cos(5\pi/10) = 0$ et la question précédente, donner une expression de $\cos(\pi/10)$.

Méthodes : (E) se ramène à une équation du second degré en $Y = X^3$ ; P a pour racine évidente 1 ; formule de Moivre et binôme pour $\cos 5a$. Voir [[Polynôme]], [[Division euclidienne]], [[Équation du second degré]], [[Linéarisation trigonométrique]].

## Algèbre linéaire, évaluation 1 (30 mars 2023, page 25-26, en anglais)

Bachelor PIB 1, 2022/2023. « Justify each step carefully. Brevity and clarity will be taken into consideration. »

**Exercise 1.** Soient
$$A = \begin{pmatrix} 1 & 0 & -1 & 2 \\ 0 & 3 & 1 & -1 \\ 2 & 4 & 0 & 3 \\ -3 & 1 & -1 & 2 \end{pmatrix},\quad B = \begin{pmatrix} 1 & 2 \\ 3 & -1 \\ 0 & -2 \\ 4 & 1 \end{pmatrix},\quad C = \begin{pmatrix} 3 & -2 & 0 & 5 \\ 1 & 0 & -3 & 4 \end{pmatrix},\quad D = \begin{pmatrix} 1 & 0 & 0 & 1 \end{pmatrix}.$$
1. Calculer $AB$, puis en déduire $ABC$.
2. Calculer si possible $DA$, $DB$ et $DC$ ; sinon, justifier.
3. Calculer si possible $CD^\top$ ; sinon, justifier ($D^\top$ est la transposée de $D$).

**Exercise 2.** Soit $A = \begin{pmatrix} 1 & 1/3 \\ c & d \end{pmatrix}$, $c, d$ réels. (1) Trouver $c$ et $d$ tels que $A^2 = -I_2$. (2) Trouver $c$ et $d$ tels que $A^2 = 0_{\mathbb{R}^{2 \times 2}}$.

**Exercise 3.** Résoudre par élimination de Gauss :
$$\text{(a)}\ \begin{cases} x_1 - 2x_2 + x_3 = 0 \\ 2x_2 - 8x_3 = 8 \\ -4x_1 + 5x_2 + 9x_3 = -9 \end{cases} \qquad \text{(b)}\ \begin{cases} x_1 - 5x_2 + 4x_3 = -3 \\ 2x_1 - 7x_2 + 3x_3 = -2 \\ -2x_1 + x_2 + 7x_3 = -1 \end{cases}$$

**Exercise 4.** La matrice suivante est la matrice augmentée d'un système linéaire. Énoncer en mots les deux prochaines opérations élémentaires sur les lignes à effectuer pour le résoudre :
$$\left(\begin{array}{cccc|c} 1 & -6 & 4 & 0 & -1 \\ 0 & 2 & -7 & 0 & 4 \\ 0 & 0 & 1 & 2 & -3 \\ 0 & 0 & 4 & 1 & 2 \end{array}\right)$$

**Exercise 5.** Transfert de chaleur : on cherche la distribution de température à l'équilibre d'une plaque mince dont la température au bord est connue (section d'une poutre métallique, flux de chaleur négligeable dans la direction perpendiculaire). $T_1, \dots, T_4$ sont les températures des quatre nœuds intérieurs du maillage. La température d'un nœud est approximativement la moyenne de ses quatre voisins (gauche, haut, droite, bas). Par exemple $T_1 = (10 + 20 + T_2 + T_4)/4$, soit $4T_1 - T_2 - T_4 = 30$.

![[Contrôles - p26.jpg]]
*Figure : plaque maillée, nœuds intérieurs 1, 2 (haut) et 4, 3 (bas) ; bords à 20° en haut, 40° à droite, 30° en bas, 10° à gauche.*

1. Écrire un système de quatre équations dont la solution donne $T_1, \dots, T_4$.
2. Résoudre ce système (indication : échanger les lignes 1 et 4 avant de commencer).

Voir [[Produit matriciel]], [[Matrice]], [[Système linéaire]], [[Matrice augmentée]], [[Opérations élémentaires sur les lignes]], [[Forme échelonnée]].

## Algèbre linéaire, évaluation 2 (8 juin 2023, page 27, en anglais)

**Exercise 1.**
1. Déterminer si $S_1 = \{(1, -1, 0), (2, -1, 2)\}$ est une base de $\mathbb{R}^3$, en justifiant.
2. Soit $S_2 = \{(1,1,3), (3,4,5), (-2,5,7), (8,-1,9)\} \subset \mathbb{R}^3$. Expliquer pourquoi $S_2$ ne peut pas être une base de $\mathbb{R}^3$. Si possible, donner une base de $\mathbb{R}^3$ formée de vecteurs de $S_2$.
3. Soit $S_3 = \{(1, -1, 0), (2, -1, 2), (1, 0, a)\}$. Trouver le réel $a$ tel que $S_3$ soit une base de $\mathbb{R}^3$.

**Exercise 2.** Lesquels sont des sous-espaces de $\mathbb{R}^3$ ? Justifier.
1. $A = \{(x, y, z) \in \mathbb{R}^3 \mid 3x - 7y = z\}$ ;
2. $B = \{(x, y, z) \in \mathbb{R}^3 \mid x^2 - z^2 = 0\}$ ;
3. $C = \{(x, y, z) \in \mathbb{R}^3 \mid x + y - z = x + y + z = 0\}$ ;
4. $D = \{(x, y, z) \in \mathbb{R}^3 \mid z(x^2 + y^2) = 0\}$.

**Exercise 3.** Donner une base et la dimension de : (1) $F = \{(x, y, z) \in \mathbb{R}^3 \mid x - 2y + z = 0\}$ ; (2) $G = \{(a, a + b, b) \mid a, b \in \mathbb{R}\}$ ; (3) $H = \{(a - b, a - b, a - b) \mid a, b \in \mathbb{R}\}$.

**Exercise 4.** Soit $E = \mathbb{R}^4$. (1) $F = \{(x, y, z, t) \in \mathbb{R}^4 \mid x + y + z = 0 \text{ et } 2x + y + z - t = 0\}$ : donner une base de $F$. (2) $G = \{(a, a, a, a) \mid a \in \mathbb{R}\}$ : donner une base de $G$. (3) Donner une base de $F + G$.

Voir [[Sous-espace vectoriel]], [[Base (algèbre linéaire)]], [[Dimension (algèbre linéaire)]], [[Indépendance linéaire]].

## Algèbre linéaire, évaluation 3 (22 juin 2023, page 28, en anglais)

**Exercise 1.** $u_1 = (1, -1, 2)$, $u_2 = (1, 1, -1)$, $u_3 = (-1, -5, 7)$ ; $E = \mathrm{Span}(u_1, u_2, u_3)$ et $F = \{(x, y, z) \in \mathbb{R}^3,\ x + y + z = 0\}$.
1. Trouver la dimension de $E$ et une base de $E$.
2. Montrer que $F$ est un sous-espace de $\mathbb{R}^3$.
3. Trouver la dimension de $F$ et une base.
4. Donner une base de $E \cap F$.

**Exercise 2.** $E = \{P \in \mathbb{R}_3[X] : P(-1) = 0 \text{ et } P(1) = 0\}$, où $\mathbb{R}_3[X]$ est l'ensemble des polynômes de degré au plus 3. (1) Montrer que $E$ est un sous-espace de $\mathbb{R}_3[X]$. (2) Trouver sa dimension et une base.

**Exercise 3.** Les applications suivantes sont-elles linéaires ? Justifier.

| | Application |
|---|---|
| 1 | $f_1(x, y) = (0, 2x)$ |
| 2 | $f_2(x, y) = (x + y, x - y)$ |
| 3 | $f_3(x, y, z) = (x, x + y, \sqrt{x + z})$ |
| 4 | $f_4(x, y, z) = (x + y, 0, xz)$ |
| 5 | $f_5(x, y, z) = (0, 0, x + y + z)$ |
| 6 | $f_6(x, y, z) = (x^2, y^2, z^2)$ |
| 7 | $f_7(x, y, z) = (x + 1, y + 1, z + 1)$ |

**Exercise 4.** Soit $\mathcal{B} = \{(1, 0, 2); (2, 1, -1); (3, 0, 7)\}$.
1. Montrer que $\mathcal{B}$ est une base de $\mathbb{R}^3$.
2. Trouver les coordonnées de $(x, y, z) \in \mathbb{R}^3$ dans $\mathcal{B}$.
3. En déduire les coordonnées de $(1, 0, 1)$ dans $\mathcal{B}$.
4. Soit $\varphi : \mathbb{R}^3 \to \mathbb{R}^3$, $\varphi(x, y, z) = (x, y, z)$. (a) Montrer que $\varphi$ est linéaire. (b) Trouver la matrice $A$ de $\varphi$ dans la base $\mathcal{B}$.

Voir [[Espace engendré]], [[Transformation linéaire]], [[Coordonnées dans une base]], [[Changement de base]], [[Matrice d'une application linéaire]].

# Informatique (examens PréING1 en pseudo-code)

## Examen du 14 novembre 2022 (2 h, sans document ni calculatrice, pages 30 à 33)

### Partie 1 : questions de cours et de réflexion (6 points)

**Question 1.** Programme :

```
PROGRAMME monProg

FONCTION maFonction(x : Entier) : Entier
VARIABLES
    y : Entier
DEBUT
    x ← x+1
    y ← x+2
    z ← x+3
    RETOURNER x+y+z
FIN

VARIABLES
    x, y, z : Entier

DEBUT
    x ← 0
    y ← 4
    z ← 5
    x ← maFonction(y)
    ECRIRE("Valeur de x : " & x)
    ECRIRE("Valeur de y : " & y)
    ECRIRE("Valeur de z : " & z)
FIN
```

1.a. Qu'affiche ce programme ? Pourquoi ? 1.b. Où sont les variables globales ? les variables locales ? les paramètres ? Voir [[Portée d'une variable]], [[Passage par valeur]], [[Passage de paramètres]].

**Question 2.** Programme :

```
PROGRAMME QuiFaitNimp
VARIABLES
    n, res : Entier
DEBUT
    res ← 0
    POUR i DE 1 A n faire
        res ← res+i
        i ← i +1
    FINPOUR
    ECRIRE("La valeur finale est " & res)
FIN
```

2.a. Deux erreurs et une très mauvaise idée se sont glissées dans ce code : où sont-elles ? 2.b. Proposer une correction. (Indications de lecture, non corrigées par le sujet : `n` n'a pas de valeur, `i` n'est pas déclaré, et l'on modifie le compteur d'une boucle `POUR`.)

**Question 3.** Expliquer les paramètres d'entrée et de sortie d'un algorithme.

**Question 4.** Pourquoi ne faut-il pas parler de « boucle si » ou de « boucle if » ? (Un `SI` est une structure conditionnelle, pas une [[Boucle (programmation)|boucle]].)

**Question 5.** Quelle est la différence entre : fonction et procédure ([[Fonction et procédure]]) ? initialisation et affectation ([[Affectation]]) ? type structuré et type primitif ?

### Partie 2 : algorithmique et pseudo-code (14 points)

1. Écrire la fonction `cube(n : entier) : entier` qui calcule $n^3$.
2. **[[Nombre d'Armstrong]]** : « Un nombre est considéré comme un nombre d'Armstrong s'il est égal à la somme des cubes des chiffres qui le composent. » Exemple : $153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27$. Écrire la fonction `armstrong(n : entier) : booléen` qui retourne vrai si `n` est un nombre d'Armstrong et faux sinon.
3. Écrire la fonction `divise(a : entier, b : entier) : booléen` qui retourne vrai si `b` divise `a` et faux sinon (voir [[Divisibilité]]).
4. **[[Nombre parfait]]** : « Un nombre est dit parfait s'il est égal à la moitié de la somme de ses diviseurs. » Exemple : $6 = (1 + 2 + 3 + 6)/2$. Écrire la fonction `parfait(n : entier) : booléen`.
5. La fonction `ent(n : réel) : entier` retourne la partie entière d'un réel (`ent(3.14) = 3`) et `sqrt(n : entier) : réel` la racine carrée d'un entier. En les utilisant, écrire `sqrt_ent(n : entier) : booléen`, qui dit si la racine carrée de `n` est entière : `sqrt_ent(25) -> true` car $\sqrt{25} = 5$, `sqrt_ent(18) -> faux` car $\sqrt{18} = 4{,}242$ (voir [[Partie entière]], [[Racine carrée]]).
6. **Nombre triangulaire** : entier naturel non nul égal au nombre de pastilles d'un triangle construit comme sur la figure. Test : on le multiplie par 8, on ajoute 1 et on prend la racine carrée ; si le résultat est entier, le nombre est triangulaire. Exemple : 3 est triangulaire car $3 \times 8 + 1 = 25$ et $\sqrt{25} = 5$. Écrire `triangulaire(n : entier) : booléen`.

![[Contrôles - p32.jpg]]
*Figure : les premiers nombres triangulaires, 1, 3, 6, 10 pastilles disposées en triangle.*

7. Programme principal : l'utilisateur saisit un nombre, puis choisit le test à appliquer. Affichage attendu :

```
Veuillez saisir un nombre : _
153 // En supposant que 153 est ce que l'utilisateur saisit
Quel test souhaitez-vous effectuer :
1. Armstrong
2. Parfait
3. Triangulaire
```

Si l'utilisateur saisit 1, le programme affiche `Vrai`. Le programme continue à afficher le menu, en proposant de saisir un nouveau nombre, jusqu'à ce que l'utilisateur saisisse 0. Écrire le programme principal (structure attendue : une boucle `TANT QUE n <> 0` et un `SELON` sur le choix).

Voir [[Pseudo-code]], [[Algorithme]].

## Examen du 9 janvier 2023 (2 h, sans document ni calculatrice, pages 34-35)

### EXO1 : chaînes de caractères

1. **Compression** : toute suite de caractères identiques est remplacée par sa taille suivie du caractère ; la forme compressée de « aaabccd » est « 3a1b2c1d ». Écrire une fonction `Compress` (la forme compressée est une chaîne), puis une fonction qui décompresse une chaîne compressée.
2. Écrire `suppCar(chaîne, caractère)`, qui supprime le caractère de la chaîne et retourne le résultat ; la chaîne est inchangée si le caractère n'y figure pas. Exemples : `suppCar("Eisti","i")` retourne « Est » ; `suppCar("je suis en prepa 1"," ")` retourne « jesuisenprepa1 » ; `suppCar("salut","n")` retourne « salut ».
3. Une chaîne est **correctement parenthésée** si elle contient autant de « ( » que de « ) » et si, en la parcourant de gauche à droite, on trouve toujours au moins autant d'ouvrantes que de fermantes. Exemple : « ((a)((x( » et « ((b))y)( » ne sont pas bien parenthésées, « ((a)(b))(c) » l'est. Écrire une fonction qui vérifie qu'une chaîne est correctement parenthésée.

Rappels : `longueur(s)` renvoie le nombre de caractères de `s` ; `s[n]` lit le n-ième caractère. Voir [[Chaîne de caractères]].

### EXO2 : structures

1. Un joueur de foot est défini par son nom, son prénom et sa date de naissance : définir le type `t_joueur`.
2. Une équipe est définie par son nom, ses 11 joueurs, le nombre de matchs gagnés et perdus dans la saison : définir le type `t_equipe`.
3. Écrire une fonction qui renvoie le nombre de matchs gagnés et perdus d'une équipe donnée.
4. Étant donné un ensemble d'équipes, écrire une procédure qui affiche le classement des équipes, basé seulement sur le nombre de matchs gagnés.

Voir [[Structure (struct)]].

### EXO3 : récursivité

1. Écrire une fonction `div7` qui trouve le nombre divisible par 7 le plus proche d'une valeur donnée (plus grand ou plus petit). Exemple : `div7(241)` renvoie 238.
2. Écrire une fonction qui calcule successivement la somme des chiffres jusqu'à ce qu'il ne reste qu'un chiffre. Exemple : `hyperSomme(11346239)` retourne 2 car $11346239 \Rightarrow 29 \Rightarrow 11 \Rightarrow 2$.

Voir [[Récursivité]].

### EXO4 : questions de cours et réflexions

1. Expliquer la différence entre une itération et une récursion.
2. Algorithme : créer deux variables numériques A et B ; les initialiser à des valeurs quelconques ; afficher A et B ; stocker A + B dans A ; stocker A − B dans B ; stocker A − B dans A ; afficher A et B. Que fait cet algorithme ? Quel intérêt peut-on en tirer ? (Il échange les deux valeurs sans variable tampon : voir [[Échange de deux variables]].)
3. Quelle est la différence entre : structure de contrôle et structure de données ? itération et indentation ?

## Points à vérifier

- **Nombre d'Armstrong** (examen du 14 novembre 2022) : l'énoncé le définit avec la somme des **cubes** des chiffres, quel que soit le nombre de chiffres. La définition usuelle élève chaque chiffre à la puissance du nombre de chiffres ; les deux coïncident pour les nombres à trois chiffres comme 153. Comparer avec la page [[Nombre d'Armstrong]].
- **Nombre parfait** : l'énoncé dit « égal à la moitié de la somme de ses diviseurs » (en comptant le nombre lui-même), ce qui équivaut à « égal à la somme de ses diviseurs stricts ». Comparer avec [[Nombre parfait]].
- **DS6, exercice 3.5** : l'exposant du dernier terme $\frac{2}{n^?}$ est illisible sur le scan ; $n^2$ est la lecture la plus probable.
- **Outils math (février 2023), exercice 1** : le terme constant de $P$ est peu lisible ; il est lu $1 + i$, seule valeur pour laquelle $P(X) = (X - i)(X^6 + iX^3 - 1 + i)$, ce que suppose l'enchaînement des questions.
- **Outils math DS2 (9 décembre 2022), exercice 3** : les questions 3(a) et 3(b) semblent inversées ($f \circ g$ s'applique à $(a, b) \in \mathbb{R}^2$ et $g \circ f$ à $x \in \mathbb{R}$), et $h$ n'est pas défini dans l'énoncé imprimé de la question 4 ; une annotation manuscrite indique $h = g \circ f$.
- **DS8, exercice 2.3** : l'exposant de $(1 + 3x)$ est lu $1/3$.
- **Algèbre linéaire, évaluation 1, exercice 4** : « the next tow elementary row operations » (coquille pour *two*) ; indication de l'exercice 5 « To speed us » (pour *up*).
- Les en-têtes des DS2, DS3 et DS4 d'analyse indiquent « Nombre de pages : 1h30 » (coquille de l'en-tête).
- Le document ne contient aucun corrigé : les méthodes indiquées sous chaque devoir sont des pistes, pas des solutions vérifiées.

## Liens

[[Analyse Maths (matière)]], [[Limite et continuité]], [[Dérivabilité]], [[Développement limité]], [[Comparaison asymptotique]], [[Borne supérieure]], [[Suite numérique]].
