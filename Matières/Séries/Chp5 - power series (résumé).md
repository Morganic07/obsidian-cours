---
type: source
tags: [year3]
sources: ["[[Chp5 - power series]]"]
maj: 2026-11-05
---

Résumé de [[Chp5 - power series]], dans [[Séries (matière)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Les séries entières $\sum a_n(x - \alpha)^n$ : domaine de convergence, régularité de la somme, développement de Taylor et séries usuelles. Voir [[Série entière]].

## Contenu, dans l'ordre du cours

- **Définition** : série de fonctions centrée en 0 ou en $\alpha$.
- **Rayon de convergence** : trois cas. Convergence en $\alpha$ seulement ($R = 0$), partout ($R = +\infty$), ou $0 < R < +\infty$ avec convergence absolue pour $|x - \alpha| < R$ et divergence pour $|x - \alpha| > R$. Aux bords, tout peut arriver. Le rayon est unique.
- **Intervalle de convergence** : $\{\alpha\}$, $\mathbb{R}$, ou l'un des quatre intervalles de bornes $\alpha \pm R$.
- **Rapport et racine** : $\lim \frac{|a_{n+1}|}{|a_n|} = \ell$ ou $\lim \sqrt[n]{|a_n|} = \ell$ donne $R = 1/\ell$ (avec $1/0 = +\infty$ et $1/{+\infty} = 0$). En cas de coefficients nuls, appliquer le critère aux termes complets de rangs $n$ et $n+1$.
- **Opérations** : $\lambda a_n$ garde le rayon. Pour la somme, $R_{a+b} \ge \min(R_a, R_b)$, avec égalité si $R_a \ne R_b$.
- **Continuité** : convergence normale sur tout $[\alpha - r, \alpha + r]$ avec $r < R$, donc somme continue sur $]\alpha - R, \alpha + R[$. Continuité aussi au bord où la série converge.
- **Dérivation et intégration terme à terme** : même rayon, mais l'intervalle de convergence peut changer aux bords. La somme est indéfiniment dérivable.
- **Séries de Taylor et de Maclaurin** : si $f$ est somme d'une série entière, $a_n = f^{(n)}(\alpha)/n!$. Polynômes de Taylor $T_n$ et reste $R_n = f - T_n$. Si $R_n(x) \to 0$, $f$ est somme de sa série de Taylor.
- **Restes** : inégalité de Taylor ($|f^{(n+1)}| \le M$ donne $|R_n(x)| \le \frac{M}{(n+1)!}|x - \alpha|^{n+1}$), forme intégrale $\frac{1}{n!}\int_\alpha^x (x - t)^n f^{(n+1)}(t)\,dt$, forme de Lagrange $\frac{f^{(n+1)}(c)}{(n+1)!}(x - \alpha)^{n+1}$.
- **Série de $\sin$** : dérivées successives, puis majoration du reste (cas $x > 0$ et $x < 0$) par $\frac{|x|^{n+1}}{(n+1)!} \to 0$.
- **$(1 + x)^a$** pour $|x| < 1$, série binomiale, rayon 1. Aux bords : $a > 0$ absolument convergente en $\pm 1$ ; $-1 < a \le 0$ conditionnellement convergente en 1 et divergente en $-1$ ; $a \le -1$ divergente aux deux bords. Cas particuliers $\sqrt{1+x}$ sur $[-1, 1]$ et $\frac{1}{\sqrt{1+x}}$ sur $]-1, 1]$, avec coefficients en $\binom{2n}{n}$.
- **Séries usuelles** : $e^x$, $\sinh$, $\cosh$, $\sin$, $\cos$ sur $\mathbb{R}$ ; $\arctan$, $\frac{1}{1-x}$, $\frac{1}{(1-x)^2}$, $\frac{1}{1+x}$, $\ln(1+x)$, $(1+x)^a$ sur $]-1, 1[$.
- **Applications** : $\sum \frac{(-1)^{n-1}}{n 2^n} = \ln\frac{3}{2}$ ; $\pi = 4\sum \frac{(-1)^n}{2n+1}$, précision $10^{-2}$ pour $n \ge 49$ ; $e = \sum \frac{1}{n!}$ avec $0 \le R_n(1) \le \frac{3}{(n+1)!}$, précision $10^{-5}$ pour $n = 8$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Inégalité de Taylor** : « $\forall x \in [d - \alpha, d + \alpha]$ » est incohérent avec $|x - \alpha| \le d$ ; il faut $[\alpha - d, \alpha + d]$ (alerte confirmée, complément).
2. **Approximation de $\pi$** : $|R_n(1)| \le \frac{1}{2n+3}$ vaut pour la série $\sum \frac{(-1)^n}{2n+1}$, qui donne $\pi/4$. Pour une précision de $10^{-2}$ sur $\pi$, il faut $\frac{4}{2n+3} \le 10^{-2}$, soit $n \ge 199$ ; $n \ge 49$ donne $10^{-2}$ sur $\pi/4$ (complément). **À corriger avant un examen.**
3. **Série du $\sin$** : le terme « $\frac{x^7}{7}$ » doit être $\frac{x^7}{7!}$ (alerte confirmée). Dans la majoration, « $|x_t|^n$ » doit se lire $|x - t|^n$.
4. **Reste de $e$** : le cours écrit $R_n(1) = \frac{f^{(n+1)}(c)}{(n+1)!}$ avec $f^{(n+1)}(c) = e^c \le e \le 3$, d'où $\frac{3}{(n+1)!}$. Le calcul est juste : $9! = 362880$ donne $n = 8$ pour $10^{-5}$. L'alerte de la transcription tient à la lecture d'une image sans $e^c$.
5. **Cas $\lambda = 0$ et bords** : « $R_{\lambda a} = R_a$ » est faux pour $\lambda = 0$ (série nulle, $R = +\infty$). De plus, $|x| \le R_a$ pour égaler les sommes devrait être $|x| < R_a$, car la série peut diverger au bord ; idem pour la somme de deux séries (complément).
6. **Binôme avec $a = 0$** : la proposition « $-1 < a \le 0$ conditionnellement convergente en 1 » ne vaut que pour $-1 < a < 0$ ; pour $a = 0$ la série se réduit à 1 (complément).
7. **Intervalles des séries usuelles** : $\arctan$ et $\ln(1+x)$ sont données sur $]-1, 1[$, mais le cours applique $\arctan$ en $x = 1$ pour $\pi$ grâce au théorème de continuité au bord. La formule vaut en fait sur $[-1, 1]$ pour $\arctan$ et sur $]-1, 1]$ pour $\ln(1+x)$ (complément).
8. **Double intitulé** : deux versions de l'intervalle de convergence (centrée en 0 puis en $\alpha$) se suivent ; la seconde généralise la première.
