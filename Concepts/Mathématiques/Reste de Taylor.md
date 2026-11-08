---
type: concept
tags: [year2, year3]
aliases: [Taylor's inequality, inégalité de Taylor, Lagrange's form of the remainder, forme de Lagrange du reste, reste de Lagrange, integral form of the remainder, reste intégral, Taylor-Lagrange, formule de Taylor avec reste intégral, Taylor's formula with integral remainder]
matieres: [Séries, Analyse]
sources: ["[[5 - power series|Chp5 - power series]]", "[[Raw/Year 2/Analyse/chp7/Chap7-Integration.docx|Chap7-Integration]]"]
maj: 2026-11-08
---

$R_n = f - T_n$, où $T_n$ est le polynôme de Taylor d'ordre $n$ en $\alpha$. Si $R_n(x) \to 0$, $f$ est la somme de sa série de Taylor ([[5 - power series|Chp5 - power series]]).

- **Inégalité de Taylor** : si $|f^{(n+1)}(x)| \le M$ pour $|x - \alpha| \le d$, alors $|R_n(x)| \le \dfrac{M}{(n+1)!}|x - \alpha|^{n+1}$ pour tout $x \in [\alpha - d, \alpha + d]$. [[Erreurs du cours#^e-reste-de-taylor|✎]]
- **Forme intégrale** : $R_n(x) = \dfrac{1}{n!}\displaystyle\int_\alpha^x (x - t)^n f^{(n+1)}(t)\,dt$.
- **Forme de Lagrange** : $R_n(x) = \dfrac{f^{(n+1)}(c)}{(n+1)!}(x - \alpha)^{n+1}$.

## Lien avec l'intégration de year2 (complément, hors du cours)

**Formule de Taylor avec reste intégral.** Pour $f$ de classe $C^{n+1}$ sur un intervalle contenant $a$ et $b$ :
$$f(b) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^k + \int_a^b \frac{(b-t)^n}{n!}\, f^{(n+1)}(t)\,dt.$$

**Preuve par récurrence sur $n$.**
- $n = 0$ : c'est le théorème fondamental de l'analyse, $f(b) = f(a) + \int_a^b f'(t)\,dt$ (voir [[Primitive]]).
- Hérédité : si $f$ est de classe $C^{n+2}$, une [[Intégration par parties]] avec $u(t) = f^{(n+1)}(t)$ et $v(t) = -\dfrac{(b-t)^{n+1}}{(n+1)!}$ (donc $v'(t) = \dfrac{(b-t)^n}{n!}$) donne
$$\int_a^b \frac{(b-t)^n}{n!} f^{(n+1)}(t)\,dt = \frac{f^{(n+1)}(a)}{(n+1)!}(b-a)^{n+1} + \int_a^b \frac{(b-t)^{n+1}}{(n+1)!} f^{(n+2)}(t)\,dt,$$
car $v(b) = 0$. En reportant dans la formule au rang $n$, on obtient la formule au rang $n+1$.

L'inégalité de Taylor s'en déduit : si $|f^{(n+1)}| \le M$ entre $a$ et $b$, alors $\left|\int_a^b \frac{(b-t)^n}{n!} f^{(n+1)}(t)\,dt\right| \le M \dfrac{|b-a|^{n+1}}{(n+1)!}$.

Notion parente : [[Série entière]]. Voir aussi : [[Développement limité]], [[Reste d'une série]], [[Intégrale]], [[Intégration par parties]].

Résumés : [[5 - power series]], [[1 - Integration]]
