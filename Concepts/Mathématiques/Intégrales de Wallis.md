---
type: concept
tags:
  - year2
aliases:
  - intégrale de Wallis
  - Wallis
matieres:
  - Analyse
sources:
  - "[[0 - Intégration UTILITAIRE|Intégration UTILITAIRE]]"
  - "[[Raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1).pdf]]"
  - "[[Raw/Year 2/Analyse/chp7/Intégration UTILITAIRE .docx|Intégration UTILITAIRE]]"
maj: 2026-11-08
---

$$W_n=\int_0^{\pi/2}\sin^n x\,dx=\int_0^{\pi/2}\cos^n x\,dx,$$
l'égalité venant du changement $t\mapsto\pi/2-t$ (TD7, ex. 15).

Le TD7 (ex. 9-10) établit par [[Intégration par parties]] une relation de récurrence, les valeurs pour un indice pair et pour un indice impair, la décroissance, $I_n\sim I_{n+1}$, le calcul de $nI_nI_{n+1}$ (c'est $(n+1)I_nI_{n+1}$ qui est constant, égal à $\frac{\pi}{2}$) [[Erreurs du cours#^e-integrales-de-wallis|✎]], puis un équivalent de $I_n$. Le TD n'a pas de corrigé : ces valeurs ne sont pas données.

## Résultats classiques (complément, hors du cours)

- **Premières valeurs** : $W_0 = \frac{\pi}{2}$, $W_1 = \int_0^{\pi/2} \sin x\,dx = 1$.
- **Récurrence** : on écrit $W_{n+2} = \int_0^{\pi/2} \sin^{n+1}x \cdot \sin x\,dx$ et on intègre par parties ($u = \sin^{n+1}x$, $v' = \sin x$, le crochet $[-\cos x \sin^{n+1}x]_0^{\pi/2}$ étant nul) :
$$W_{n+2} = (n+1)\int_0^{\pi/2} \sin^n x \cos^2 x\,dx = (n+1)(W_n - W_{n+2}), \quad \text{d'où} \quad W_{n+2} = \frac{n+1}{n+2}\,W_n.$$
- **Valeurs explicites** :
$$W_{2p} = \frac{(2p)!}{2^{2p}(p!)^2}\cdot\frac{\pi}{2}, \qquad W_{2p+1} = \frac{2^{2p}(p!)^2}{(2p+1)!}.$$
Par exemple $W_2 = \frac{\pi}{4}$, $W_3 = \frac{2}{3}$, $W_4 = \frac{3\pi}{16}$.
- **Monotonie** : $(W_n)$ est positive et décroissante, car $0 \le \sin^{n+1}x \le \sin^n x$ sur $[0, \frac{\pi}{2}]$.
- **Produit constant** : la suite $(n+1)\,W_n W_{n+1}$ est constante (la récurrence le montre), égale à sa valeur en $n = 0$ : $(n+1)\,W_nW_{n+1} = \frac{\pi}{2}$.
- **Équivalent** : de $W_{n+2} \le W_{n+1} \le W_n$ et $\frac{W_{n+2}}{W_n} = \frac{n+1}{n+2} \to 1$, on tire $W_{n+1} \sim W_n$ ; alors $(n+1)W_n^2 \sim \frac{\pi}{2}$, donc
$$W_n \sim \sqrt{\frac{\pi}{2n}}.$$

**Pour la culture** : on en déduit le **produit de Wallis**
$$\frac{\pi}{2} = \prod_{k=1}^{+\infty} \frac{4k^2}{4k^2 - 1} = \frac{2}{1}\cdot\frac{2}{3}\cdot\frac{4}{3}\cdot\frac{4}{5}\cdot\frac{6}{5}\cdots,$$
et c'est par les intégrales de Wallis qu'on identifie la constante $\sqrt{2\pi}$ de la **formule de Stirling** $n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$.

Notion parente : [[Intégrale]]. Voir aussi : [[Intégration par parties]], [[Comparaison asymptotique]], [[Changement de variable dans une intégrale]].

Résumés : [[0 - Intégration UTILITAIRE]]
