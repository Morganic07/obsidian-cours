---
type: source
sources: ["[[Chp1 - récursivité et complexité]]"]
maj: 2026-11-05
---

Résumé de [[Chp1 - récursivité et complexité]], dans [[Year 2 - Algo]]. En cas d'écart, le cours et ses images font foi. Les exemples sont en Python.

## Idée générale

Une fonction récursive s'appelle elle-même, et l'on mesure le coût d'un algorithme par son ordre de grandeur plutôt que par un temps exact. Le chapitre relie les deux : le coût d'une fonction récursive se met en équation, puis se résout.

## Contenu, dans l'ordre du cours

- **[[Récursivité]]** : directe (la fonction s'appelle) ou indirecte (B appelle C, C appelle D, D rappelle B). Deux phases : descente jusqu'à la condition d'arrêt, puis montée. Exemples comparés en itératif et en récursif : factorielle ($n! = n \times (n-1)!$, $0! = 1$) et somme des $n$ premiers entiers.
- **Pile de récursion** : les appels en cours sont empilés. Chaque bloc contient les paramètres, l'adresse de retour et les variables locales. En Python, la pile est limitée à environ 1000 appels. La pile de récursion est un cas particulier de la pile d'exécution, qui gère tous les appels. Voir [[Pile et file]].
- **[[Calcul de complexité et théorème de résolution|Calcul de complexité]]** (voir aussi [[Complexité algorithmique]]) : au meilleur, au pire et en moyenne, pour une entrée de taille $n$, indépendamment de la machine. Règles de calcul : une instruction de base coûte une unité, une boucle additionne ses itérations, un appel ajoute le coût de la fonction. Règles de la notation $O$ : on oublie les constantes, on garde le terme dominant ($O(T_1) + O(T_2) = \max$, $O(T_1)\,O(T_2) = O(T_1 T_2)$). Pour un `while` de $m$ itérations : $O(m\,(g(n) + f(n)))$. Pour un `if/else` : $O(g + f_1 + f_2)$.
- **Classes de complexité** : constante, logarithmique, linéaire, quadratique, polynomiale, exponentielle ($a^n$). Exemple annoté de la factorielle itérative : $O(n)$.
- **Complexité d'une fonction récursive** : coût des appels plus coût de la séparation et de la reconstruction. Méthode par substitution : $T(n) = T(n-1) + b$ donne $O(n)$. Forme générale $T(n) = a\,T(n/b) + f(n)$ avec $f(n) = c\,n^k$ : $O(n^{\log_b a})$ si $a > b^k$, $O(n^k \log_b n)$ si $a = b^k$, $O(n^k)$ si $a < b^k$. Schéma « diviser pour régner » : diviser, régner, combiner.
- **[[Recherche dichotomique]]** : version itérative et version récursive. Pour la version récursive, $a = 1$, $b = 2$, $f(n) = \Theta(1)$, donc $T(n) = T(n/2) + \Theta(1)$ et la complexité est $O(\log_2 n)$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Toutes les images ont été lues par leur transcription ; aucune n'a été ouverte.

1. **Substitution de $T(n) = T(n-1) + b$** (complément) : la base est $T(0) = c$, mais la dernière ligne s'arrête sur $T(1)$ et écrit $nb - b + c$. Avec la base $T(0)$, on obtient $nb + c$. Le résultat $O(n)$ est le même.
2. **Exemple annoté de la factorielle** : la transcription signale que les annotations sont décalées par rapport au code. Alerte confirmée par le texte, pas par l'image. La conclusion écrite à côté (« La complexité est $O(n)$ ») est juste.
3. **Fausse alerte** : le « 1 » de la factorielle lu comme un « I » dans les transcriptions est bien le chiffre 1, le calcul de la phase de montée le confirme.
4. **Pied de page « TIME UN — 4 2 »** du graphique des complexités : bruit de mise en page, sans contenu.
5. **Master theorem** : le cours le donne sans démonstration, pour $f(n) = c\,n^k$ seulement. Le cours le nomme aussi « Master Theorem » dans l'analyse de la dichotomie.
