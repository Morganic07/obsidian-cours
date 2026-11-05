• **Recherche séquentielle d'une valeur dans un tableau**

Le calcul de la complexité se fait comme suit :

- Pire des cas : il s'agit d'un tableau où $x$ n'y figure pas. Le nombre d'itérations est alors $n$. Donc $T(n) = O(n)$.
- Meilleur des cas : il s'agit d'un tableau où $x$ est le premier élément du tableau. Donc $T(n) = O(1)$.
- Complexité moyenne : on suppose que les données sont réparties selon la probabilité $\frac{1}{n}$. Donc $T(n) = \Sigma_{i=1}^{n} \frac{1}{n} * i = \frac{1}{n} * \frac{n(n+1)}{2} = \frac{n+1}{2}$. Il s'ensuit que $T(n) = O(n)$
