---
type: source
sources: ["[[Chp2 - Alternating and absolutly convergent series]]"]
maj: 2026-11-05
---

Résumé de [[Chp2 - Alternating and absolutly convergent series]], dans [[Year 3 - Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Séries de signe quelconque : séries alternées, convergence absolue, puis critères de d'Alembert et de Cauchy. Voir [[Série numérique]] et [[Critère de d'Alembert et de Cauchy]].

## Contenu, dans l'ordre du cours

- **Série alternée** $\sum (-1)^n b_n$ avec $b_n = |a_n|$. **Critère** : si $(b_n)$ décroît et tend vers 0, elle converge. Exercices : série harmonique alternée, $\sum (-1)^n \frac{n^2}{n^3 + 1}$ (« fait sur feuille », non rédigé).
- **Reste** : la somme $S$ est entre deux sommes partielles consécutives et $|R_n| \le b_{n+1}$.
- **$p$-série alternée** $\sum \frac{(-1)^n}{n^p}$ : converge si et seulement si $p > 0$.
- **Remarque de l'étudiant** : on ne peut pas utiliser les équivalents sur des séries alternées, ils sont réservés aux termes positifs.
- **Convergence absolue** : $\sum |a_n|$ converge. Elle implique la convergence, avec $|\sum a_n| \le \sum |a_n|$. Pour des termes positifs, absolue et simple coïncident. **Convergence conditionnelle** : convergente sans être absolument convergente (exemple : série harmonique alternée).
- **Critère du rapport (d'Alembert)** : $|a_{n+1}/a_n| \to L$. $L < 1$ : absolument convergente. $L > 1$ ou $+\infty$ : divergente. $L = 1$ : aucune conclusion, avec trois exemples (conditionnellement convergente, divergente, absolument convergente).
- **Critère de la racine (Cauchy)** : même énoncé avec $\sqrt[n]{|a_n|}$, utile avec des puissances $n$-ièmes. Exercices : $\sum \left(\frac{2n+3}{3n+2}\right)^n$ et $\sum \frac{n^{\ln n}}{n^n}$. Remarque : si $L = 1$ pour l'un, $L = 1$ pour l'autre, et les deux échouent.
- **Choix du critère** : $p$-série ou géométrique reconnaissables ; forme voisine, comparaison ou équivalent (pour $|a_n|$ si le signe varie) ; $a_n \not\to 0$, divergence grossière ; $(-1)^n b_n$, critère des séries alternées ; factorielles ou produits, rapport ; $(b_n)^n$, racine ; $f(n)$ avec intégrale calculable, comparaison série-intégrale.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Réciproque de la remarque sur $L = 1$** : « si $L = 1$ pour le rapport alors $L = 1$ pour la racine, et réciproquement ». Le sens rapport vers racine est vrai quand la limite du rapport existe. Le sens inverse ne vaut que si la limite du rapport existe aussi : la limite de la racine peut exister sans que celle du rapport existe (complément).
2. **Séries indexées par $n \in \mathbb{N}$ avec $1/n$ ou $1/n^2$** : le terme en $n = 0$ n'est pas défini ; il faut lire $n \ge 1$ (complément, sans conséquence).
3. **Série alternée $\sum (-1)^n \frac{n^2}{n^3+1}$** : la suite $b_n$ n'est décroissante qu'à partir de $n = 1$ ($b_0 = 0 < b_1$) ; le critère s'applique à partir de ce rang (complément).
4. **« $N \in \mathbb{N}$ » en majuscule** dans une somme du choix des critères : coquille, signalée par la transcription.
