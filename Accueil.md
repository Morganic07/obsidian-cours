# Accueil

Catalogue de toutes les pages du wiki. À lire en premier pour répondre à une question.

État au 2026-11-06 : 1 265 concepts, rangés en six domaines dans `Concepts/` ; 223 résumés et 41 matières, rangés par matière dans `Matières/` ; aucune synthèse. Chaque page porte un tag `year1` à `year4` selon l'année de ses cours. Toutes les notes de `Cours/` et tous les PDF et PPTX de `.raw/` sont intégrés. Le texte des PDF n'est pas cherchable : seuls leurs résumés le sont.

## Concepts (1266)

### Systèmes et vecteurs

- [[Système linéaire]] : équations à résoudre, compatibles ou non, homogènes ou non
- [[Combinaison linéaire]] : somme de vecteurs multipliés par des scalaires, ce que calcule $A\mathbf{x}$
- [[Espace engendré]] : Span, l'ensemble des combinaisons de vecteurs donnés
- [[Indépendance linéaire]] : $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale
- [[Forme échelonnée]] : forme réduite d'une matrice, qui montre pivots et variables libres
- [[Transformation linéaire]] : application qui respecte l'addition et la multiplication par un scalaire
- [[Injectivité et surjectivité]] : au plus un ou au moins un antécédent
- [[Morphisme]] : homomorphisme, endomorphisme, isomorphisme, automorphisme
- [[Changement de base]] : matrice de passage et $A' = P^{-1}AP$

### Matrices

- [[Produit matriciel]] : $AB$ a pour colonnes les $A\mathbf{b}_j$, et n'est pas commutatif
- [[Matrice inversible]] : matrice carrée qui a un inverse, et ses 20 énoncés équivalents
- [[Transposée]] : la matrice $A^T$, dont les colonnes sont les lignes de $A$
- [[Déterminant]] : nombre associé à une matrice carrée, lié à l'inversibilité et au volume
- [[Matrice symétrique]] : $A^T = A$, orthogonalement diagonalisable
- [[Rang d'une matrice]] : dimension de l'espace des colonnes

### Espaces vectoriels

- [[Espace vectoriel]] : ensemble de vecteurs régi par dix axiomes
- [[Sous-espace vectoriel]] : partie stable contenant le vecteur nul
- [[Espace des colonnes]] : Col $A$, les combinaisons linéaires des colonnes de $A$
- [[Espace nul]] : Nul $A$, les solutions de $A\mathbf{x} = \mathbf{0}$
- [[Sous-espaces fondamentaux]] : Col $A$, Row $A$, Nul $A$ et Nul $A^T$
- [[Somme directe]] : sous-espaces supplémentaires, décomposition unique
- [[Base (algèbre linéaire)]] : famille libre qui engendre un sous-espace
- [[Dimension (algèbre linéaire)]] : nombre de vecteurs d'une base

### Valeurs propres et décompositions

- [[Valeur propre]] : scalaire $\lambda$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ a une solution non triviale
- [[Vecteur propre]] : vecteur non nul associé à une valeur propre
- [[Espace propre]] : Nul$(A - \lambda I)$, le vecteur nul et les vecteurs propres de $\lambda$
- [[Diagonalisation]] : écriture $A = PDP^{-1}$ avec $D$ diagonale
- [[Décomposition en valeurs singulières]] : écriture $A = U\Sigma V^T$, valable pour toute matrice
- [[Factorisation QR]] : écriture $A = QR$, avec $Q$ à colonnes orthonormales

### Orthogonalité

- [[Produit scalaire]] : opération $\mathbf{u} \cdot \mathbf{v}$, d'où vient la norme
- [[Orthogonalité]] : $\mathbf{u} \cdot \mathbf{v} = 0$
- [[Procédé de Gram-Schmidt]] : construit une base orthogonale à partir d'une base
- [[Moindres carrés]] : meilleure solution approchée de $A\mathbf{x} = \mathbf{b}$
- [[Norme]] : taille d'un vecteur, normes $\|\cdot\|_1$, $\|\cdot\|_2$, $\|\cdot\|_\infty$, et distance associée
- [[Complément orthogonal]] : $W^\perp$, les vecteurs orthogonaux à tout $W$
- [[Famille orthogonale]] : vecteurs deux à deux orthogonaux, et familles orthonormales
- [[Projection orthogonale]] : décomposition $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, et point de $W$ le plus proche de $\mathbf{y}$
- [[Matrice orthogonale]] : matrice carrée à colonnes orthonormales, avec $U^{-1} = U^T$
- [[Régression linéaire]] : droite qui minimise la somme des carrés des résidus

### Topologie et limites

- [[Boule et voisinage]] : boules ouvertes et fermées, et parties qui contiennent une boule autour d'un point
- [[Ouvert et fermé]] : parties voisinage de leurs points, et leurs complémentaires
- [[Intérieur et adhérence]] : plus grand ouvert contenu, plus petit fermé contenant, frontière
- [[Limite et continuité]] : définition en $\epsilon$ et $\eta$, et méthode en deux variables
- [[Application lipschitzienne]] : variation majorée par $k\|x - y\|$, et continuité uniforme

### Analyse d'une variable

- [[Dérivabilité]] : dérivée, opérations, Rolle, accroissements finis et règle de l'Hôpital
- [[Comparaison asymptotique]] : grand O, petit o, équivalents et croissances comparées
- [[Développement limité]] : Taylor-Young, opérations et DL usuels
- [[Intégrale]] : construction, propriétés, sommes de Riemann et trapèzes
- [[Primitive]] : théorème fondamental, parties, changement de variable, Bioche

### Calcul différentiel

- [[Dérivée partielle]] : dérivée selon une variable, dérivation en chaîne et théorème de Schwarz
- [[Différentielle]] : approximation linéaire de $f$ en un point
- [[Fonction de classe Ck]] : dérivées partielles continues jusqu'à l'ordre $k$
- [[Matrice jacobienne]] : matrice de la différentielle, et jacobien
- [[Gradient]] : vecteur des dérivées partielles, direction de plus grande pente
- [[Équation aux dérivées partielles]] : solutions connues et résolution des systèmes
- [[Difféomorphisme]] : bijection $\mathcal{C}^1$ de réciproque $\mathcal{C}^1$, changements de variables et polaires

### Formes

- [[Forme bilinéaire]] : fonction de deux vecteurs, linéaire en chacun
- [[Forme quadratique]] : $Q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}$ avec $A$ symétrique

### Probabilités et statistiques

- [[Espace probabilisé]] : espace d'échantillonnage, événements, sigma-algèbre, axiomes
- [[Probabilité conditionnelle]] : multiplication, probabilités totales, Bayes, indépendance
- [[Dénombrement]] : principe du produit, permutations, combinaisons
- [[Variable aléatoire]] : discrète (pmf) et continue (pdf), changement de variable
- [[Fonction de répartition]] : cdf discrète et continue, percentiles, médiane
- [[Espérance et variance]] : espérance, variance, écart-type, Tchebychev
- [[Loi binomiale]] : Bernoulli et binomiale, moments, approximations
- [[Loi de Poisson]] : limite de la binomiale, moments, stabilité par somme
- [[Loi normale]] : normale, centrée réduite, règle 68-95-99,7, log-normale
- [[Loi exponentielle]] : exponentielle, gamma, Weibull
- [[Loi conjointe]] : loi conjointe, marginales, indépendance, convolution
- [[Covariance et corrélation]] : covariance, corrélation, combinaisons de variables
- [[Fonction génératrice des moments]] : définition, moments, somme de variables indépendantes
- [[Échantillonnage]] : méthodes d'échantillonnage, biais, variables iid
- [[Quartiles et valeurs aberrantes]] : quartiles, iqr, boîte à moustaches, percentiles
- [[Variance et écart-type d'échantillon]] : moyenne, médiane, variance d'échantillon
- [[Théorème central limite]] : TCL et ses applications
- [[Loi des grands nombres]] : convergence de la moyenne empirique
- [[Estimateur]] : biais, variance, MSE, consistance, erreur type
- [[Distribution d'échantillonnage]] : loi d'une statistique, population finie
- [[Intervalle de confiance]] : moyenne, variance, proportion, taille d'échantillon
- [[Loi du khi-deux]] : définition, additivité, loi de la variance d'échantillon
- [[Loi de Student]] : définition, théorème de Gosset
- [[Diagramme de probabilité]] : diagrammes normal et de Weibull
- [[Méthode de la fonction de répartition inverse]] : simulation par inversion de F

### Analyse de données et IA

- [[ANOVA]] : test d'égalité de trois moyennes ou plus
- [[Statistique F]] : rapport de carrés moyens, en ANOVA et en régression
- [[Test du χ²]] : test d'indépendance sur tableau croisé, loi du χ², variance
- [[Analyse en composantes principales]] : composantes, loadings, scores, scree plot
- [[Paradoxe de Simpson]] : inversion d'une tendance par une variable cachée
- [[Intervalle de prédiction]] : encadrement d'une valeur individuelle en régression
- [[Arbre de décision]] : ID3, C4.5, CART, gain d'information et Gini
- [[K-moyennes]] : partitionnement par inertie, clustering hiérarchique
- [[Validation d'un classifieur]] : matrice de confusion, précision, rappel, validation croisée
- [[Méthodes d'ensemble]] : bagging, boosting, forêts aléatoires
- [[Approche symbolique et connexionniste]] : frise historique de l'IA
- [[Droit d'auteur et IA]] : protection des contenus générés

### Logique, ensembles et nombres

- [[Logique propositionnelle]] : connecteurs, tables de vérité, quantificateurs, types de preuve
- [[Récurrence]] : initialisation, hérédité, conclusion
- [[Opérations sur les ensembles]] : opérations, De Morgan, partitions, cardinal, produit cartésien
- [[Relation d'équivalence]] : relation binaire, classes, ensemble quotient
- [[Relation d'ordre]] : ordre total ou partiel, majorants, sup et inf
- [[Nombre complexe]] : formes, Moivre, Euler, géométrie

### Séries

- [[Série numérique]] : séries de référence, termes positifs, alternées, convergence absolue
- [[Critère de d'Alembert et de Cauchy]] : critères du rapport et de la racine
- [[Convergence uniforme]] : simple, uniforme, normale, échanges de limites
- [[Série entière]] : rayon, Taylor, séries usuelles
- [[Série de Fourier]] : coefficients, parité, convergence, Parseval

### Algorithmique et graphes

- [[Complexité algorithmique]] : temps, espace, $O$, $\Omega$, $\Theta$
- [[Calcul de complexité et théorème de résolution]] : règles du $O$, substitution, théorème de résolution
- [[Récursivité]] : fonction qui s'appelle, descente et montée, pile de récursion
- [[Recherche dichotomique]] : recherche dans un tableau trié, en $O(\log n)$
- [[Pile et file]] : LIFO et FIFO
- [[Liste chaînée]] : cellules reliées par un pointeur
- [[Arbre AVL]] : arbre binaire de recherche équilibré, rotations
- [[Tours de Hanoï]] : problème récursif, $2^n - 1$ coups
- [[Problème du sac à dos]] : $2^n$ configurations, méthodes du devoir
- [[Algorithme glouton]] : décision locale, sac à dos, Kruskal
- [[Graphe non orienté]] : définitions et graphes particuliers
- [[Graphe orienté]] : degrés, DFS, BFS, composantes fortement connexes
- [[Arbre couvrant minimal]] : arbres, forêts, Kruskal

### Programmation

- [[Portée d'une variable]] : région où une variable existe
- [[Transtypage]] : conversion implicite ou explicite
- [[Évaluation en court-circuit]] : `&&` et `||` s'arrêtent dès que le résultat est connu
- [[Pointeur et adresse mémoire]] : `&`, `*`, passage par adresse, `malloc`, double pointeur
- [[Structure (struct)]] : regroupement de types différents, `typedef`

### Bases de données

- [[Clé primaire et clé étrangère]] : identification et référence entre tables
- [[Modèle entité-association]] : MCD, cardinalités, héritage, entité faible
- [[Schéma relationnel]] : MLD et règles de passage du MCD
- [[Algèbre relationnelle]] : projection, restriction, jointure, division
- [[Langage SQL]] : DDL, DML, droits, architecture

### Réseaux

- [[CLI Cisco IOS]] : modes de la ligne de commande, running-config et startup-config
- [[Routage statique]] : table de routage, routes statiques, route par défaut
- [[Routage dynamique]] : IGP et EGP, RIP
- [[VLAN]] : VLAN, trunk, routage inter-VLAN
- [[NAT et PAT]] : adresses privées, static NAT, PAT
- [[Liste de contrôle d'accès]] : ACL, wildcard mask, refus implicite

### Systèmes d'exploitation

- [[Système d'exploitation]] : rôle et couches du système
- [[Noyau]] : cœur du système, noyau Linux
- [[Interruption]] : signal matériel, vecteur, ISR, DMA
- [[Appel système]] : demande logicielle au noyau
- [[Hiérarchie de stockage]] : registres à bandes, interfaces de disques
- [[Système de fichiers]] : partitions, NTFS, FAT32, EXT4
- [[BIOS et UEFI]] : démarrage, POST, MBR
- [[Distribution Linux]] : Ubuntu, LTS, ISO, installation
- [[Machine virtuelle]] : VMM bare metal ou hosted, cloud
- [[Processus]] : programme en exécution, mémoire, types
- [[États d'un processus]] : new, ready, running, waiting, terminated
- [[Bloc de contrôle de processus]] : PCB
- [[Ordonnancement des processus]] : files, LTS, STS, MTS
- [[Changement de contexte]] : sauvegarde et rechargement via le PCB
- [[Création et terminaison de processus]] : fork, exec, wait, exit
- [[Processus zombie et orphelin]] : processus terminé non attendu, ou sans parent
- [[Shell et Bash]] : shell, commandes de base, APT
- [[Permissions Unix]] : `ls -l`, `chmod`, octal
- [[Redirection et tube]] : jokers, redirections, tâches de fond, guillemets
- [[Script Bash]] : shebang, variables, tests, boucles
- [[Tâche planifiée cron]] : crontab et syntaxe
- [[AWK]] : champs, variables, BEGIN et END

### Philosophie

- [[Animal politique]] : thèse d'Aristote sur la vie dans la cité
- [[État de nature]] : situation avant l'état chez Hobbes
- [[Contrat social]] : l'état comme contrat, sécurité contre liberté
- [[Quatre causes d'Aristote]] : causes matérielle, formelle, efficiente, finale
- [[Animal-machine]] : nature-machine cartésienne et sa critique
- [[Cybernétique]] : Wiener, machine et organisme, Simondon
- [[Perfectibilité]] : propre de l'homme selon Rousseau
- [[Autonomie morale]] : se donner sa loi, Kant
- [[Progrès technique]] : technique, nature et progrès

### Écologie, numérique et société

- [[Limites planétaires]] : neuf limites, chiffres français et version 2025
- [[Collapsologie]] : étude de l'effondrement, courbe de deuil, World3
- [[Anthropocène]] : balance entre technosphère et biosphère
- [[Web sémantique]] : triplets, web 3.0 de Berners-Lee
- [[Communs numériques]] : définition, critères, trois murs
- [[Open design]] : design libre et en commun, exemples et faux libre
- [[Licences libres]] : CC0, MIT, OFL, ISC et limite face à l'IA
- [[Économie circulaire]] : réemploi, reconditionnement, recyclage

### Design et innovation

- [[Affordance]] : signifier, affordance, mood
- [[Entretien semi-directif]] : enquête par guide d'entretien, consentement, biais
- [[Analyse thématique d'entretien]] : mapping des thèmes, verbatims, idées fortes
- [[Persona]] : profil type d'usager
- [[Atelier de co-conception]] : atelier avec les usagers
- [[Tiers-lieu]] : lieu de rencontre et de projet
- [[Retail régénératif]] : point de vente à impact positif sur le vivant
- [[Cercle chromatique]] : primaires, complémentaires, chaudes et froides, gammes
- [[Contraste des couleurs]] : contraste simultané, illusions, perspective atmosphérique
- [[Typologie des innovations]] : produit, service, procédé, organisation, business model
- [[Servitisation]] : vendre l'usage plutôt que le produit
- [[Grille du management de la valeur]] : à qui, à quoi, que suffit-il, avec qui, par qui, pour qui

### Ajoutés avec les documents PDF et PPTX

- [[Borne supérieure]] : plus petit majorant d'une partie de $\mathbb{R}$, propriété fondamentale de $\mathbb{R}$
- [[Suite numérique]] : limites, gendarmes, limite monotone, suites adjacentes, extraites et récurrentes
- [[Intégrale multiple]] : domaines élémentaires, Fubini, changement de variable
- [[Image et image réciproque]] : image directe et réciproque d'une partie par une application
- [[Arbre binaire]] : définition récursive, vocabulaire, propriétés, parcours
- [[Arbre binaire de recherche]] : insertion, recherche, minimum, maximum, suppression
- [[Adressage IPv4 et CIDR]] : classes, masque, préfixe, broadcast, CIDR
- [[Héritage en base de données]] : spécialisation d'une entité en sous-entités
- [[Imaginaire]] : représentations collectives, notion centrale de SHS en 3e année
- [[Sémiotique]] : étude des signes et de leurs significations, en design
- [[Analyse techno-sémiotique]] : interfaces numériques comme dispositifs techniques et sémiotiques
- [[Architexte]] : outil qui régit les opérations et les formes du texte à l'écran
- [[Écrit d'écran]] : forme de l'écrit sur un support numérique
- [[Discours d'escorte]] : discours qui orientent l'appropriation des dispositifs numériques
- [[Value(s) Design]] : méthode de conception du cours de management de l'innovation

### Ajoutés le 2026-11-06, par matière

**Year 1 - Algo Maths**

- [[Affectation]] : en pseudo-code, la flèche ← affecte à une variable une expression de même type
- [[Algorithme]] : production automatique d'un résultat à partir d'une entrée, mot venu d'Al-Khwarizmi
- [[Algorithme d'Euclide]] : exemple de fonction récursive, pgcd(a, b) vaut a si b = 0, sinon pgcd(b, a mod b)
- [[Algorithme d'approximation]] : nommé dans le cours, sans définition
- [[Algorithme stochastique]] : algorithme qui intègre du hasard ou des probabilités dans ses décisions, contrairement au déterministe
- [[Bit]] : « Binary Digit », un bit est un chiffre binaire, selon le Cours 1
- [[Boucle (programmation)]] : structure qui répète un bloc d'instructions tant qu'une condition le demande
- [[Carré magique]] : grille 3 × 3 des nombres 1 à 9, lignes, colonnes et diagonales de même somme
- [[Chaîne de caractères]] : type CHAINE du pseudo-code, avec concaténation & et fonctions longueur, extrait, trouve
- [[Code de Gray]] : suite de codes binaires où deux valeurs successives ne diffèrent que d'un bit
- [[Conjecture de Syracuse]] : exemple d'algorithme récursif dont on ne sait pas démontrer la terminaison
- [[Correction d'un algorithme]] : un algorithme est correct s'il se termine avec la bonne sortie pour chaque instance
- [[Dataclass (Python)]] : décorateur @dataclass du module dataclasses, pour faire des classes de données en Python
- [[Division euclidienne]] : opérateurs DIV et MOD sur les entiers du pseudo-code, // et % en Python
- [[Exponentiation rapide]] : calcul de $n^k$ par dichotomie, avec $n^k = (n \cdot n)^{k/2}$ si k est pair
- [[Factorielle]] : $n! = n \times (n-1)!$ avec $0! = 1$, exemple type de fonction récursive
- [[Fonction et procédure]] : la fonction retourne une valeur à partir de paramètres, la procédure ne retourne rien
- [[Fonction range (Python)]] : fonction Python qui génère une suite d'entiers, range(3) comptant de 0 à 2
- [[Fractale]] : motif autosimilaire défini par récurrence, par une suite $u_0, u_1, \dots, u_n$
- [[Langage Python]] : langage de Guido van Rossum, interprété, typé dynamiquement, à indentation significative
- [[Langage interprété]] : nommé dans le cours, sans définition
- [[Loi de Parkinson]] : nommé dans le cours, sans définition
- [[Modélisation d'un problème]] : formaliser les objets et opérations d'un problème réel avant de chercher un algorithme
- [[Nombre premier]] : interprétation géométrique par des billes, rangeables seulement en ligne si le nombre est premier
- [[Nombre à virgule flottante]] : « un float n'est pas un nombre réel », il ne représente les réels qu'approximativement
- [[Numération binaire]] : écriture des nombres en base 2, le poids doublant d'une position à l'autre
- [[Palindrome]] : chaîne qui se lit de la même façon dans les deux sens, blancs non compris
- [[Passage de paramètres]] : en pseudo-code, un paramètre a un mode E (entrée), S (sortie) ou ES
- [[Problème des crayons]] : fausse preuve par récurrence que n crayons ont tous la même couleur
- [[Problème du passeur]] : exemple d'introduction (loup, chèvre, chou), problème facile à modéliser, non résolu dans le cours
- [[Problème du voyageur de commerce]] : problème difficile sans algorithme exact efficace connu, abordé par approximation
- [[Problème indécidable]] : nommé dans le cours, sans définition
- [[Programmation dynamique]] : nommé dans le cours, sans définition
- [[Programmation modulaire]] : décomposer un problème complexe en sous-problèmes, en référence au Discours de la méthode
- [[Pseudo-code]] : langage pour spécifier un algorithme sur papier avant de le programmer
- [[Recherche exhaustive]] : parcourir les $2^n$ configurations du sac à dos et garder la meilleure admissible
- [[Récursivité terminale]] : récursion dont l'appel récursif est la dernière instruction, sinon non terminale (enveloppée)
- [[Somme des premiers entiers]] : $1 + 2 + \dots + n = n(n+1)/2$
- [[Structure conditionnelle]] : instruction qui exécute un bloc ou un autre selon la valeur d'une condition
- [[Suite de Fibonacci]] : exemple de suite, dont la version récursive naïve refait des sous-calculs que la terminale évite
- [[Terminaison d'un algorithme]] : un algorithme récursif doit s'arrêter, sa condition d'arrêt devant être atteinte
- [[Typage dynamique]] : nommé dans le cours, sans définition
- [[Type primitif]] : types élémentaires fournis par le langage, par opposition aux types structurés ou objets
- [[Échange de deux variables]] : permuter deux variables à l'aide d'une variable temporaire, base du travail sur les variables
- [[Équation du second degré]] : équation $az^2 + bz + c = 0$ étudiée par le signe du discriminant $\Delta = b^2 - 4ac$

**Year 1 - Algèbre Linéaire**

- [[Bijection]] : application à la fois injective et surjective, tout élément d'arrivée ayant un unique antécédent
- [[Composition de fonctions]] : pour f de X dans Y et g de Y dans Z, $(g \circ f)(x) = g(f(x))$
- [[Coordonnées dans une base]] : coefficients uniques $\lambda_i$ de l'écriture de x dans une base $(e_1, \ldots, e_n)$
- [[Fonction identité]] : l'identité de X est l'application $\mathrm{Id}_X : x \mapsto x$
- [[Forme multilinéaire alternée]] : nommé dans le cours, sans définition
- [[Groupe linéaire]] : $GL(E)$, ensemble des automorphismes de E, mentionné dans le chp2 sans développement
- [[Homothétie]] : endomorphisme $f(x) = \lambda x$ de rapport $\lambda$ réel, donné en exemple au chp2
- [[Image d'une application linéaire]] : $\mathrm{Im}(f) = \{f(x) \mid x \in E\}$, sous-espace vectoriel de F
- [[Matrice]] : tableau de n lignes et p colonnes, $a_{ij}$ étant le coefficient ligne i, colonne j
- [[Matrice d'une application linéaire]] : sa colonne j donne les coordonnées dans B' de l'image du j-ième vecteur de B
- [[Opérations élémentaires sur les lignes]] : opérations autorisées sur les lignes d'un système pour le résoudre par pivot de Gauss
- [[Spectre (algèbre linéaire)]] : ensemble des valeurs propres d'un endomorphisme f, noté $\mathrm{Sp}(f)$
- [[Système linéaire homogène]] : système linéaire de second membre nul, qui s'écrit $A\mathbf{x} = \mathbf{0}$
- [[Théorème de la base incomplète]] : en dimension finie, toute famille libre peut être complétée en une base
- [[Théorème du rang]] : pour f linéaire sur E de dimension finie, $\dim E = \mathrm{rg}(f) + \dim \mathrm{Ker}(f)$

**Year 1 - Analyse Maths**

- [[Approximation décimale]] : approximation de x à $10^{-p}$ près par défaut, $E(10^p x)/10^p$, ou par excès
- [[Asymptote oblique]] : droite $y = ax + b$ telle que $f(x) - ax - b \to 0$ en $\pm\infty$
- [[Caractérisation séquentielle de la limite]] : $f(x) \to \ell$ en a si et seulement si $f(u_n) \to \ell$ pour toute suite tendant vers a
- [[Changement d'indice]] : méthode de calcul des sommes citée au chapitre 0
- [[Coefficient binomial]] : $\binom{n}{p}$, symétrique et entier, ce que prouve la relation de Pascal par récurrence
- [[Constante d'Euler]] : encadrement $\ln(n+1) \le H_n \le 1 + \ln n$ de la série harmonique par intégrale
- [[Convergence d'une suite]] : $u_n \to \ell$ si pour tout $\varepsilon > 0$ l'écart reste sous $\varepsilon$ à partir d'un rang N
- [[Croissances comparées]] : hiérarchie des suites et fonctions de référence, factorielle, exponentielles, puissances et logarithmes
- [[Densité de ℚ dans ℝ]] : entre deux réels distincts, il y a une infinité de rationnels et d'irrationnels
- [[Développement asymptotique]] : f possède un DL en $\pm\infty$ si $u \mapsto f(1/u)$ possède un DL en 0
- [[Ensembles de nombres]] : inclusions $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$, plus les décimaux $\mathbb{D}$
- [[Extremum local]] : maximum ou minimum de f sur un voisinage $[a - \eta, a + \eta]$ du point a
- [[Fonction paire et impaire]] : sur un intervalle symétrique, f est paire si $f(-x) = f(x)$, impaire si $f(-x) = -f(x)$
- [[Fonctions hyperboliques]] : nommé dans le cours, sans définition
- [[Fonctions trigonométriques]] : cos et sin, abscisse et ordonnée du point d'angle x sur le cercle unité
- [[Fonctions trigonométriques réciproques]] : arcsin et arctan, équivalents à x en 0, avec le développement limité d'arctan
- [[Forme indéterminée]] : cas laissés indéterminés par les opérations sur les limites, comme $\infty - \infty$ et $0 \times \infty$
- [[Formule de Leibniz]] : dérivée n-ième d'un produit, $(fg)^{(n)} = \sum \binom{n}{k} f^{(k)}g^{(n-k)}$
- [[Formule de Pascal]] : relation entre coefficients binomiaux, d'où vient le triangle de Pascal
- [[Formule du binôme de Newton]] : $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$
- [[Formules trigonométriques]] : formules d'addition des cosinus et sinus, et formules qui en découlent
- [[Identité d'Hermite]] : $\sum_{k=0}^{n-1} E(x + k/n) = E(nx)$, où E est la partie entière
- [[Intervalle réel]] : partie I de ℝ qui contient tout réel compris entre deux de ses éléments
- [[Intervalle stable]] : intervalle I tel que $f(I) \subset I$, qui garantit que $u_{n+1} = f(u_n)$ est bien définie
- [[Inégalité arithmético-géométrique]] : comparaison des moyennes arithmétique, géométrique et harmonique de deux réels positifs
- [[Inégalité de Bernoulli]] : pour $a \ge 0$ réel et n entier, $(1 + a)^n \ge 1 + na$
- [[Inégalité de Cauchy-Schwarz]] : majoration du carré d'une somme de produits $a_k b_k$ par le produit des sommes de carrés
- [[Inégalité triangulaire]] : pour des réels, la valeur absolue d'une somme est au plus la somme des valeurs absolues
- [[Monotonie et signe de la dérivée]] : f dérivable est croissante, décroissante ou constante selon le signe de f'
- [[Nombre rationnel]] : nombre dont l'écriture décimale est finie ou périodique
- [[Partie entière]] : E(x), unique entier tel que $E(x) \le x < E(x) + 1$
- [[Point fixe]] : réel tel que $f(\ell) = \ell$, seule limite possible d'une suite récurrente avec f continue
- [[Polynôme]] : polynômes complexes, division euclidienne, racines, factorisation, et équivalent en $+\infty$ et en 0
- [[Principe des substitutions]] : remplacer la variable d'une inégalité vraie pour tout réel donne de nouveaux résultats
- [[Prolongement par continuité]] : possible en a si et seulement si f a une limite finie en a, et unique
- [[Propriété d'Archimède]] : pour tout réel x, il existe un entier n tel que $n > x$
- [[Quantificateur]] : quantificateurs existentiel $\exists$ et universel $\forall$ du cours de logique
- [[Quantité conjuguée]] : multiplier et diviser par la somme des racines pour lever une indétermination $\infty - \infty$
- [[Racine carrée]] : $\sqrt{x^2}$ vaut la valeur absolue de x, et la racine d'une somme n'est pas la somme des racines
- [[Raisonnement par l'absurde]] : montrer p en établissant que sa négation mène à une conclusion absurde
- [[Règle de l'Hôpital]] : limite d'un quotient de fonctions qui s'annulent en $x_0$, par le quotient des dérivées
- [[Règles de calcul sur les inégalités]] : règles rappelées au chapitre 0 et appliquées au TD0
- [[Somme télescopique]] : $\sum_{k=m}^{n} (u_{k+1} - u_k) = u_{n+1} - u_m$
- [[Suite complexe]] : suite de ℂ, bornée ou convergente par le module, convergente si parties réelle et imaginaire convergent
- [[Suite extraite]] : suite $(u_{\varphi(n)})$ avec $\varphi$ strictement croissante de ℕ dans ℕ
- [[Suite géométrique]] : rappel de la formule de la somme géométrique pour une raison différente de 1
- [[Suites adjacentes]] : une croissante, une décroissante, d'écart tendant vers 0 : elles convergent vers la même limite
- [[Symboles somme et produit]] : $\sum$ et $\prod$ sur une famille finie, avec somme vide 0 et produit vide 1
- [[Tangente à une courbe]] : droite $y = f(a) + f'(a)(x - a)$ en un point où f est dérivable
- [[Théorème de Bolzano-Weierstrass]] : nommé dans le cours, sans définition
- [[Théorème de Cesàro]] : si $u_n \to l$, la moyenne des n premiers termes tend aussi vers l
- [[Théorème de Rolle]] : f continue sur [a, b], dérivable, avec $f(a) = f(b)$ : f' s'annule en un point
- [[Théorème de la bijection]] : une fonction continue est injective si et seulement si elle est strictement monotone
- [[Théorème de la limite monotone]] : une suite croissante majorée converge vers son sup, sinon tend vers $+\infty$
- [[Théorème des bornes atteintes]] : une fonction continue sur un segment est bornée et atteint ses bornes
- [[Théorème des gendarmes]] : une suite ou fonction encadrée par deux autres de même limite a cette limite
- [[Théorème des valeurs intermédiaires]] : f continue sur [a, b] avec $f(a)f(b) \le 0$ s'annule entre a et b
- [[Valeur absolue]] : la valeur absolue de x est la distance de 0 à x
- [[Équation trigonométrique]] : notation $x \equiv y\ [\theta]$, il existe k entier tel que $x = y + k\theta$
- [[Équivalent (comparaison asymptotique)]] : $u_n \sim v_n$ si $u_n / v_n \to 1$, soit $u_n - v_n = o(v_n)$

**Year 1 - Communication orale**

- [[Clonage animal]] : sujet d'un dossier de débat, avec arguments pour et contre préparés pour l'exercice
- [[Théorie de l'escalade]] : théorie tirée d'un argumentaire de débat sur le cannabis, et non d'un cours

**Year 1 - Corps à l'oeuvre**

- [[Consommation de geste]] : ce qui consomme dépend des mouvements mis en œuvre, pensés par le concepteur du lieu
- [[Design d'interface]] : conception de l'interface logicielle, là où l'utilisateur interagit avec la machine
- [[Expérience utilisateur]] : UX design, designer c'est proposer une expérience grâce aux sens
- [[Fonction, forme, structure]] : triade F.F.S qui s'applique dans le design pour créer objets et services
- [[Gestelligence]] : nommé dans le cours, sans définition
- [[Informations froides et chaudes]] : informations données, et sensations ressenties en les recevant, qui colorent nos souvenirs
- [[Mécanique du stress]] : niveaux du stress et réaction du corps, stress face au public expliqué par le cerveau primitif
- [[Neuf sens]] : ouïe, vue, odorat, goût, toucher, proprioception, thermoception, nociception, équilibrioception, et leur hiérarchie
- [[Triangle client-designer]] : situation et vision du client, manque à identifier par le designer, puis solution adéquate

**Year 1 - Dessein au cube**

- [[Biais cognitif]] : nommé dans le cours, sans définition
- [[Biais de confirmation]] : sélectionner uniquement les informations qui confirment des croyances ou idées préexistantes
- [[Biais de disponibilité]] : tendance à privilégier et surestimer les informations immédiatement disponibles en mémoire
- [[Biais de rétrospective]] : tendance à juger après coup un événement imprévu plus prévisible qu'il ne l'était
- [[Consentement éclairé]] : feuille signée avant l'entretien, participation volontaire et confidentielle, objectif expliqué en transparence

**Year 1 - HDA**

- [[Mola]] : vêtements des femmes kuna, faits de couches de tissu découpées laissant apparaître d'autres couleurs

**Year 1 - Outil Maths**

- [[Affixe]] : nombre complexe associé à un point ou un vecteur du plan, pour faire de la géométrie
- [[Application (mathématiques)]] : procédé associant à chaque élément de l'ensemble de départ une unique image à l'arrivée
- [[Application monotone]] : application entre ensembles ordonnés qui conserve (croissante) ou renverse (décroissante) l'ordre
- [[Argument valide]] : suite de prémisses et une conclusion, vraie dès que les prémisses le sont
- [[Cardinal d'un ensemble]] : nombre d'éléments d'un ensemble fini, avec la formule du cardinal d'une union
- [[Complémentaire d'un ensemble]] : $E \setminus A$, ensemble des éléments de E hors de A, correspondant à la négation
- [[Condition nécessaire et suffisante]] : si $p \Rightarrow q$, p est condition suffisante pour q, et q nécessaire pour p
- [[Congruence modulo n]] : $a \equiv b\ [n]$ si n divise $a - b$, relation d'équivalence à n classes
- [[Différence d'ensembles]] : $A \setminus B$, éléments de A qui ne sont pas dans B, égal à $A \cap \overline{B}$
- [[Différence symétrique]] : $A \Delta B = (A \cup B) \setminus (A \cap B)$, commutative et associative
- [[Divisibilité]] : a divise b s'il existe k avec $b = ak$, relation d'ordre non totale sur $\mathbb{N}^*$
- [[Domaine et rang d'une relation]] : ensembles des premières et des deuxièmes coordonnées des couples d'une relation
- [[Double inclusion]] : deux ensembles sont égaux si chacun est inclus dans l'autre, méthode de preuve
- [[Définition par compréhension]] : définir un ensemble par une propriété que ses éléments sont seuls à vérifier
- [[Ensemble (mathématiques)]] : collection d'objets distincts, ses éléments, avec les ensembles usuels et l'ensemble vide
- [[Ensemble de définition]] : ensemble des éléments de l'ensemble de départ qui ont une image par f
- [[Ensembles disjoints]] : deux ensembles A et B d'intersection vide, $A \cap B = \emptyset$
- [[Fonction indicatrice]] : fonction $1_A$ valant 1 sur la partie A et 0 ailleurs
- [[Forme normale conjonctive et disjonctive]] : nommé dans le cours, sans définition
- [[Forme trigonométrique et exponentielle]] : écritures d'un complexe par module et argument, en cos et sin ou $e^{i\theta}$
- [[Graphe d'une fonction]] : ensemble des couples $(x, f(x))$, relation où chaque x figure dans un unique couple
- [[Implication logique]] : $p \Rightarrow q$, fausse seulement si p vraie et q fausse, équivalente à $\neg p \vee q$
- [[Inclusion (ensembles)]] : E est inclus dans F si tout élément de E est élément de F
- [[Injection canonique]] : pour $A \subset X$, application $i : A \hookrightarrow X$ définie par $i(x) = x$
- [[Intersection et union d'ensembles]] : éléments communs à A et B, ou appartenant à A ou à B
- [[Irrationalité de √2]] : preuve par l'absurde, $\sqrt{2} = a/b$ forcerait a et b tous deux pairs
- [[Lois de De Morgan]] : négation d'une disjonction ou d'une conjonction, en logique et pour les ensembles
- [[Majorant et minorant]] : élément supérieur, ou inférieur, à tous les éléments d'une partie d'un ensemble ordonné
- [[Modus ponens et modus tollens]] : règles d'inférence $p, p \Rightarrow q \vdash q$ et $\neg q, p \Rightarrow q \vdash \neg p$
- [[Parité d'un entier]] : un entier est pair s'il s'écrit 2k, impair s'il s'écrit 2k + 1
- [[Partition d'un ensemble]] : famille de parties non vides, deux à deux disjointes, dont l'union est E
- [[Plus grand élément]] : majorant d'une partie qui lui appartient, noté max, unique s'il existe
- [[Preuve par contraposition]] : prouver $p \Rightarrow q$ en supposant non q et en démontrant non p
- [[Preuve par contre-exemple]] : un seul contre-exemple suffit pour montrer qu'une proposition universelle est fausse
- [[Priorité des connecteurs logiques]] : négation, puis conjonction, puis disjonction, puis implication et équivalence
- [[Produit cartésien]] : ensemble des n-uplets $(x_1, \ldots, x_n)$ avec $x_i \in E_i$, où l'ordre compte
- [[Propriétés des connecteurs logiques]] : idempotence, associativité, commutativité, distributivité, identité, données en tableau
- [[Raisonnement par disjonction des cas]] : traiter séparément chaque cas d'une disjonction pour établir la conclusion
- [[Relation antisymétrique]] : relation où aRb et bRa impliquent $a = b$, comme $\leq$ sur ℕ
- [[Relation binaire]] : partie de $A \times B$, on écrit aRb si le couple (a, b) lui appartient
- [[Relation fonctionnelle]] : relation où chaque x est en relation avec au plus un y, associée à une fonction
- [[Relation réflexive]] : relation où tout élément est en relation avec lui-même, comme l'égalité et $\leq$
- [[Relation symétrique]] : relation où aRb implique bRa, comme l'égalité, contrairement à $\leq$
- [[Relation transitive]] : relation où aRb et bRc impliquent aRc, comme l'égalité et $\leq$
- [[Représentation d'une relation binaire]] : diagramme cartésien, matrice de la relation ou diagramme sagittal, et lecture des propriétés
- [[Restriction d'une fonction]] : pour $A \subset X$, la restriction de f à A coïncide avec f en tout point de A
- [[Règle d'inférence]] : arguments valides de base, le cours en liste huit
- [[Règle de résolution]] : règle d'inférence $p \vee q,\ \neg p \vee r \vdash q \vee r$, dite aussi règle de Robinson
- [[Tautologie]] : proposition toujours vraie dans sa table de vérité, la contradiction étant toujours fausse
- [[Égalité de deux fonctions]] : même ensemble de définition, même ensemble d'arrivée et mêmes images en tout point
- [[Élément maximal]] : élément de A sans élément plus grand dans A, et symétriquement l'élément minimal
- [[Équivalence logique]] : deux propositions sont logiquement équivalentes si elles ont la même table de vérité

**Year 1 - Peinture**

- [[Anthropocentrisme]] : regarder le monde d'un point de vue humain, en se croyant supérieur aux autres espèces
- [[Art abstrait]] : art qui ne représente pas la réalité, Kandinsky en étant présenté comme l'inventeur
- [[Bauhaus]] : école de design pionnière, Berlin 1919-1933, où enseignait Paul Klee
- [[Dripping]] : technique de Jackson Pollock, au milieu du XXe siècle, qui consiste à jeter la peinture
- [[Encaustique]] : peinture dont le liant est la cire, le diluant restant incertain dans le cours
- [[Expressionnisme abstrait]] : nommé dans le cours, sans définition
- [[Fauvisme]] : nommé dans le cours, sans définition
- [[Gouache]] : peinture dont le diluant est l'eau et le liant la gomme arabique
- [[Impressionnisme]] : nommé dans le cours, sans définition
- [[Liant et diluant]] : composants d'une peinture avec le pigment, comparés pour gouache, encaustique et tempera
- [[Outrenoir]] : nommé dans le cours, sans définition
- [[Pigment]] : matière colorante d'origine végétale, minérale ou chimique, qu'on peut fabriquer soi-même
- [[Pop art]] : nommé dans le cours, sans définition
- [[Street art]] : nommé dans le cours, sans définition
- [[Surréalisme]] : nommé dans le cours, sans définition
- [[Symbolique des couleurs]] : couleurs polysémiques dont la symbolique évolue selon l'époque et la culture
- [[Synesthésie]] : mélange des sens, illustré par Rimbaud, l'orgue à couleur et le piano à cocktail
- [[Tempera]] : peinture dont le diluant est l'eau et le liant l'œuf

**Year 1 - Philosophie**

- [[Autoconstruction de soi]] : les formes de liberté servent à se faire soi-même, « deviens ce que tu es »
- [[Capitalisme]] : investir ses moyens pour en avoir plus, l'argent devenant une fin au lieu d'un moyen
- [[Darwinisme]] : la nature comme résultat de mutations et de sélections, causes et effets au lieu de finalité
- [[Droit et morale]] : le droit juridique porte sur les actions, le droit moral sur les intentions
- [[Désir]] : choisir entre les futurs possibles, le désir façonnant la technique
- [[Finalisme]] : pour Aristote la nature a une finalité propre, remise en cause dès le XVIIe siècle
- [[L'art imite la nature]] : principe dominant de l'Antiquité à la Renaissance, renversé par Oscar Wilde
- [[Liberté relative et liberté absolue]] : comprendre les causes extérieures pour s'en libérer, la liberté absolue restant inaccessible
- [[Logos]] : langage humain et raisonnement logique, opposé à la phonè, voix des animaux
- [[Sophistes]] : nommé dans le cours, sans définition
- [[Technique (philosophie)]] : mise à disposition des moyens en vue des fins, qui libère de l'impuissance

**Year 1 - Projet design**

- [[Biomimétisme]] : source d'inspiration du lieu imaginé pour Melvita, par une architecture biomimétique
- [[Brief]] : information donnée au designer sur un projet, présentée par le commanditaire avec la problématique
- [[Design d'expérience]] : niveau « groupe de je » de l'échelle du brief ELBA, culture du divertissement
- [[Design de services]] : design qui remet les conditions d'amélioration humaine au cœur du processus, selon le dossier ELBA
- [[Design produit]] : premier niveau de l'échelle du brief ELBA, le « je individuel » et la culture transactionnelle
- [[Démarche ascendante]] : pratique fondamentale d'un tiers-lieu, processus « bottom up » centré sur l'expression du besoin
- [[Ferme verticale]] : nommé dans le cours, sans définition
- [[Fréquence de Schumann]] : 7,83 Hz, « fréquence de la terre », citée dans un exposé étudiant sur Melvita
- [[Gifting]] : piste d'expérience pour Melvita autour des coffrets beauté et des produits test
- [[Greenwashing]] : pratique limitée d'un tiers-lieu, manque de sincérité dans l'affichage social ou écologique
- [[Géocaching]] : application de chasse au trésor dans la rue proposée par l'équipe pour le projet Bel-Air
- [[Merchandising]] : nommé dans le cours, sans définition
- [[Quartier prioritaire de la politique de la ville]] : QPV déterminés par l'État, 58 % de Villeneuve étant en QPV
- [[Responsabilité sociétale des entreprises]] : nommé dans le cours, sans définition
- [[Sentiment d'appartenance]] : s'identifier à une communauté et adhérer volontairement à ses valeurs et normes
- [[Soin (care)]] : geste culturel situé, apprendre à voir les vulnérabilités, y compris celles que produisent les dispositifs
- [[Stigmatisation]] : nommé dans le cours, sans définition
- [[Ville dortoir]] : nommé dans le cours, sans définition
- [[Écoquartier]] : quartier qui limite son impact environnemental, favorise le lien social et se développe durablement
- [[Étude-action]] : méthode qui repère les besoins précis et les inclut vite dans une réflexion collective

**Year 2 - Algo**

- [[Arborescence (graphe)]] : arbre enraciné, dont un sommet distingué, la racine, impose un sens de parcours
- [[Arbre (théorie des graphes)]] : graphe non orienté connexe et sans cycle, comme une chaîne ou une étoile
- [[Arbre m-aire]] : arbre d'ordre m, dont le degré maximum d'un nœud est égal à m
- [[B-arbre]] : arbre d'ordre n dont chaque nœud autre que la racine a entre n/2 et n fils
- [[Chemin (graphe)]] : suite de sommets reliés par des arcs dans un graphe orienté, élémentaire si sommets distincts
- [[Circuit (graphe)]] : chemin d'un graphe orienté qui revient à son sommet de départ, avec au moins un arc
- [[Classe de complexité]] : classement d'un algorithme selon l'ordre de grandeur de son coût, constant, logarithmique, linéaire…
- [[Cycle (graphe)]] : chaîne d'un graphe non orienté, de longueur au moins 2, qui revient à son départ
- [[Diviser pour régner]] : schéma en trois temps, diviser en sous-problèmes, les résoudre, puis combiner les solutions
- [[Hauteur d'un arbre]] : profondeur maximale des nœuds, longueur de la plus longue branche en nombre d'arêtes
- [[Méthode spéciale Python]] : nommé dans le cours, sans définition
- [[Pile d'exécution]] : pile qui gère tous les appels de fonctions, dont la pile de récursion est un cas particulier
- [[Sous-graphe]] : graphe dont les sommets et les arcs sont pris parmi ceux d'un autre graphe
- [[Vocabulaire des arbres]] : termes de base sur les arbres, racine, feuille, nœud interne, parent, fils

**Year 2 - Analyse**

- [[Changement de variable dans une intégrale]] : calcul d'une intégrale par une substitution $\varphi$ de classe $\mathcal{C}^1$ sur [a, b]
- [[Compact élémentaire]] : domaine d'intégrale double de 1er ou 2e type, calculée par intégrations successives
- [[Coordonnées elliptiques]] : changement de variables $x = ar\cos\theta$, $y = br\sin\theta$, de jacobien abr
- [[Coordonnées polaires]] : changement de variables $x = r\cos\theta$, $y = r\sin\theta$, adapté aux domaines circulaires
- [[Décomposition en éléments simples]] : écriture d'une fraction rationnelle comme somme d'un polynôme et d'éléments simples
- [[Dérivation d'une intégrale à bornes variables]] : dérivée de $x \mapsto \int_{u(x)}^{v(x)} f$, et étude de $F(x) = \int_0^x f$
- [[Ellipse]] : courbe d'équation $x^2/a^2 + y^2/b^2 = 1$, rappelée dans les notes du chapitre 9
- [[Intégrales de Wallis]] : $W_n = \int_0^{\pi/2}\sin^n x\,dx$, étudiées au TD7 par intégration par parties
- [[Intégration par parties]] : technique de calcul d'intégrale, démontrée en dérivant le produit fg
- [[Inégalité de la moyenne]] : valeur moyenne d'une fonction continue sur [a, b], $\frac{1}{b-a}\int_a^b f$, et son encadrement
- [[Méthode des trapèzes]] : approximation d'une intégrale par des trapèzes, d'erreur en $1/n^2$ pour f de classe $\mathcal{C}^2$
- [[Parité et périodicité d'une intégrale]] : l'intégrale d'une fonction T-périodique sur une période ne dépend pas de sa position
- [[Pavé]] : produit de segments $\prod [a_i, b_i]$ dans $\mathbb{R}^n$, segment, rectangle ou parallélépipède
- [[Relation de Chasles]] : pour c dans [a, b], l'intégrale sur [a, b] est la somme des intégrales sur [a, c] et [c, b]
- [[Règles de Bioche]] : choix du changement de variable pour intégrer une fraction en sin et cos
- [[Somme de Riemann]] : somme $\frac{b-a}{n}\sum f(a_k)$ aux points réguliers, approximation de l'intégrale
- [[Subdivision]] : suite finie $a = x_0 < x_1 < \dots < x_n = b$ d'un segment [a, b]

**Year 2 - Analyse dans Rn**

- [[Continuité uniforme]] : continuité où, pour toute précision fixée, un même $\delta$ convient en tout point
- [[Distance]] : application symétrique, positive, nulle seulement entre points égaux, vérifiant l'inégalité triangulaire
- [[Dérivation en chaîne]] : dérivée de $g(t) = f(u_1(t), \dots, u_n(t))$, $g'(t) = \sum u_i'(t)\,\partial f/\partial x_i$
- [[Espace séparé]] : deux points distincts y ont toujours des voisinages disjoints
- [[Inégalité des accroissements finis]] : majoration de $f(b) - f(a)$ par la norme du gradient pour f de classe $\mathcal{C}^1$
- [[Partie compacte]] : nommé dans le cours, sans définition
- [[Partie convexe]] : partie qui contient tout segment $(1-\lambda)x + \lambda y$ joignant deux de ses points
- [[Suite de Cauchy]] : nommé dans le cours, sans définition
- [[Théorème de Schwarz]] : dérivées partielles croisées définies et continues en a, alors égales en a

**Year 2 - Anglais**

- [[Accessibilité]] : capacité d'une entité à être utilisable par tous, quels que soient handicap ou connaissances
- [[Animation en stop-motion]] : la chuckimation, stop-motion fondée sur des poupées articulées de super-héros
- [[Animatique]] : animatic, timeline vidéo construite à partir du storyboard
- [[Application native et web app]] : application faite pour un système d'exploitation dédié, ou site web donnant l'expérience d'une application
- [[Architecture de l'information]] : fondation d'un projet, carte complète d'un produit numérique
- [[Autonomatronics]] : marque déposée d'animation robotique de Walt Disney, robots qui détectent la présence de personnes
- [[Brise-glace]] : ice breaker, court exercice qui aide les participants à prendre confiance et à partager
- [[Calque (image numérique)]] : layers, feuilles numériques transparentes superposées qui facilitent la modification d'une image
- [[Chevauchement]] : overlapping, un élément en recouvre partiellement un autre pour créer une illusion de volume
- [[Clair-obscur]] : chiaroscuro, technique de dessin centrée sur lumières et ombres, qui donne du volume
- [[Composition (arts visuels)]] : manière dont les éléments sont disposés dans l'espace de la page ou de la toile
- [[Compression vidéo]] : méthodes logicielles pour réduire la taille des vidéos, et termes associés
- [[Consigne d'écriture]] : writing prompt, idée, image ou texte initial qui inspire un texte de création
- [[Contrôle qualité et assurance qualité]] : quality control, test qui cherche les défauts d'un produit avant son lancement
- [[Croquis]] : mot venu du français, rapide dessin de la figure en dessin d'après modèle
- [[Design d'interaction]] : conception de produits numériques interactifs, les interactions liant humains et produit
- [[Design industriel]] : usage contemporain du design industriel, celui des cent dernières années
- [[Design responsive]] : capacité d'un site à s'adapter au mobile comme aux grands écrans, avec le même code
- [[Design sonore]] : sound design, art de créer le son pour le cinéma, la télévision ou le jeu vidéo
- [[Design system]] : bibliothèque de composants graphiques à réutiliser pour concevoir une interface
- [[Dessin technique]] : technical drawing, dessin incluant les aspects d'ingénierie pour montrer le fonctionnement d'un objet
- [[Effets visuels]] : VFX, manipulation vidéo hors du contexte de la prise de vue réelle
- [[Empâtement]] : impasto, superposition de couches de peinture épaisse pour créer de la texture
- [[Ergonomie]] : connaissances scientifiques sur l'homme et méthodes pour concevoir des systèmes utilisables par le plus grand nombre
- [[Espace positif et négatif]] : le sujet de l'image, et l'espace autour qui forme un autre sujet
- [[Forme implicite]] : implied shape, forme non représentée que le cerveau voit en comblant les vides
- [[Forme organique]] : forme irrégulière, asymétrique et courbe, associée aux objets de la nature
- [[Front end et back end]] : code de l'interface visible par l'utilisateur, et technologie cachée qui porte l'intelligence du produit
- [[Fusion nucléaire]] : réaction par laquelle une étoile produit de l'énergie en son cœur
- [[Gamification]] : enrichir contenus éducatifs, marketing ou processus métier par des mécaniques de jeu
- [[Gel du style]] : styling freeze, moment à partir duquel plus aucun changement n'est possible
- [[Guide de style]] : modèle présentant les polices, images et mises en page d'une entreprise ou d'une personne
- [[Hachure]] : hatching, fines lignes parallèles rapprochées pour représenter l'ombre
- [[Hiérarchie visuelle]] : point focal, éléments qui ressortent et éléments subordonnés d'une composition
- [[Identité visuelle]] : corporate identity, logos, couleurs, images, web design, slogan et ton d'une marque
- [[Idéation]] : exercice créatif pour partager des idées
- [[Image matricielle et vectorielle]] : image faite de pixels qui perd en qualité, ou graphique fait de points, courbes et lignes
- [[Images clés]] : key frames, marques de la timeline qui définissent aspect, mouvements et actions de l'animation
- [[Infographie animée]] : animation d'informations ou de données à l'aide d'éléments visuels
- [[Interface cerveau-machine]] : nommé dans le cours, sans définition
- [[Livrable]] : deliverables, ce qui peut être fourni dans le développement d'un produit
- [[Maquette (design)]] : wireframe, modèle basique pour planifier, et mockup, visuel du produit final
- [[Masse solaire]] : unité de masse des étoiles, un astre de 4 masses solaires pesant 4 Soleils
- [[Meuble en kit]] : flat-pack, meuble livré à plat que le client assemble lui-même
- [[Mise en page]] : layout, manière dont un design et ses éléments sont placés sur une page
- [[Moodboard]] : planche de tendances composée d'images, de textes et d'objets
- [[Motif décoratif]] : pattern, dessin à but décoratif fait d'éléments répétés
- [[Must-have et should-have]] : éléments non négociables à inclure, et éléments à inclure dans un monde idéal
- [[Méthode agile]] : capacité à modifier un plan et à réagir plus vite, par sprints et user stories
- [[Nature morte]] : still-life drawing, dessin d'objets inanimés comme bouteilles, fruits ou fleurs
- [[Nombre d'or]] : golden ratio, rapport mathématique pour une composition esthétique, la « divine proportion »
- [[Nomenclature]] : bill of materials, tableau des matériaux, quantités et ordre d'assemblage
- [[Parallaxe]] : animation à partir de photographies séparant personnages et arrière-plan pour un effet de mouvement
- [[Parcours utilisateur]] : user journey, parcours de l'utilisateur tout au long du service, avec ses pain points
- [[Peinture acrylique]] : peinture à base d'eau qui devient résistante à l'eau en séchant
- [[Perspective linéaire]] : illusion de profondeur en 2D, toutes les lignes convergeant vers un point de fuite
- [[Pitch]] : essayer de vendre un projet ou une œuvre à qui l'achètera ou le produira
- [[Propriété intellectuelle]] : projet ou concept imaginé par une personne et qui lui appartient, avec le copyright
- [[Prototype]] : première version d'un projet, ou version d'un produit avant sa production
- [[Raccourci (perspective)]] : foreshortening, technique de perspective qui place les choses dans l'espace
- [[Rendu (vidéo)]] : rendering, processus de calcul des effets dans un logiciel de montage vidéo
- [[Retouche et étalonnage]] : ajustement des niveaux, correction des couleurs et remplacement d'image
- [[Roman graphique]] : graphic novel, roman dessiné en bandes dessinées
- [[Scénario (cinéma)]] : screenplay, œuvre écrite décrivant histoire, décors, paroles et actions des personnages
- [[Service blueprint]] : cartographie des utilisateurs et des tâches qui leur sont liées, avec le back office
- [[Structure narrative]] : ordre et manière de raconter les événements, avec plot et setting
- [[Synchronisation labiale]] : lip sync, faire correspondre le mouvement des lèvres avec la voix de doublage
- [[Teinte et valeur]] : hue, apparence de la couleur pure, et value, degré de clarté d'une couleur
- [[Texture (arts visuels)]] : surfaces rough ou smooth, et texture visuelle recréée en image
- [[Timeline]] : représentation graphique, visuelle ou sonore du temps, support de l'animation
- [[Types de lignes en dessin]] : gesture lines, cross contour lines et autres lignes du dessin
- [[Typographie]] : style, allure, taille et aspect des lettres, avec typeface et kerning
- [[Voix off]] : voix utilisée sans faire partie de la narration d'origine
- [[Échelle hiérarchique]] : sujet représenté plus grand en raison de son importance, non de sa taille réelle
- [[Écoconception]] : eco-design, design utile ou bénéfique pour l'environnement, comme l'emballage biodégradable
- [[Équilibre visuel]] : balance, formes, couleurs, lignes et espaces bien répartis pour une stabilité visuelle
- [[Étoile]] : corps céleste massif d'hydrogène et d'hélium qui produit de l'énergie par fusion nucléaire

**Year 2 - Bilinear Algebra**

- [[Comatrice]] : développement du déterminant par cofacteurs, et matrice adjointe, transposée de la matrice des cofacteurs
- [[Conditionnement d'une matrice]] : rapport $\sigma_1/\sigma_n$ des valeurs singulières extrêmes d'une matrice inversible
- [[Corps (algèbre)]] : nommé dans le cours, sans définition
- [[Décomposition spectrale]] : écriture d'une matrice symétrique $A = \sum \lambda_i \mathbf{u}_i\mathbf{u}_i^T$
- [[Développement colonnes-lignes]] : produit AB écrit comme somme des produits colonne de A par ligne de B
- [[Forme linéaire]] : nommé dans le cours, sans définition
- [[Forme quadratique définie positive]] : forme Q telle que $Q(\mathbf{x}) > 0$ pour tout x non nul, et variantes
- [[Matrice augmentée]] : matrice des coefficients d'un système, complétée par la colonne du second membre
- [[Matrice diagonale]] : définie au chapitre 0b avec la matrice identité $I_n$, dont les colonnes forment la base standard
- [[Matrice triangulaire]] : son déterminant et ses valeurs propres se lisent sur sa diagonale principale
- [[Multiplicité d'une valeur propre]] : multiplicité de $\lambda$ comme racine de l'équation caractéristique
- [[Optimisation sous contrainte]] : optimiser une forme quadratique sur la sphère unité, extremums donnés par les valeurs propres
- [[Règle de Cramer]] : solution de $A\mathbf{x} = \mathbf{b}$ par $x_i = \det A_i(\mathbf{b}) / \det A$
- [[Théorème de Pythagore]] : u et v orthogonaux si et seulement si $\lVert u+v \rVert^2 = \lVert u \rVert^2 + \lVert v \rVert^2$
- [[Théorème de la matrice inversible]] : vingt énoncés équivalents sur une matrice carrée, dont son inversibilité
- [[Théorème des axes principaux]] : changement de variable orthogonal qui supprime les termes croisés d'une forme quadratique
- [[Théorème spectral]] : une matrice symétrique a n valeurs propres réelles et se diagonalise orthogonalement
- [[Transformations géométriques du plan]] : réflexions, contractions, cisaillements et projections, avec leur matrice standard
- [[Variable libre]] : variable dont la colonne n'est pas une colonne pivot de la matrice des coefficients
- [[Vecteur unitaire]] : vecteur de norme 1, obtenu en divisant un vecteur non nul par sa norme
- [[Équation caractéristique]] : $\det(A - \lambda I) = 0$, dont les racines sont les valeurs propres de A

**Year 2 - Corps à l'oeuvre**

- [[Biais du designer]] : avoir conscience qu'on est biaisé en tant que designer, illustré par une anecdote
- [[Geste]] : mouvement avec une intention, à partir duquel il faut designer
- [[Mécanique de succès et d'échec]] : chercher dans ses histoires de succès ou d'échec le réflexe constant
- [[Posture et sentiment]] : tête et corps ne sont pas séparés, les sentiments sont associés à une posture
- [[Système nerveux sympathique et parasympathique]] : nommé dans le cours, sans définition
- [[Émotion et sentiment]] : une émotion est brève, si elle dure dans le temps c'est un sentiment

**Year 2 - Operating System**

- [[APT]] : outil pour installer, supprimer et mettre à jour les paquets d'une distribution Linux
- [[Accès direct à la mémoire]] : DMA, mécanisme qui permet d'accéder à la RAM sans interrompre le CPU
- [[Adresse de bouclage]] : interface virtuelle lo, par laquelle l'ordinateur s'envoie des données à lui-même
- [[Appel exec()]] : appel système qui, après fork(), remplace l'espace mémoire du processus par un nouveau programme
- [[Appel fork()]] : appel système qui crée un nouveau processus, copie du parent en code, données et mémoire
- [[Appels wait() et waitpid()]] : le parent attend la fin d'un enfant et récupère son PID et son statut
- [[Arborescence des répertoires Linux]] : système hiérarchique de répertoires dont le sommet est la racine /
- [[Arbre de processus]] : les processus parents créent des enfants, qui en créent d'autres à leur tour
- [[Architecture multiprocessus de Chrome]] : Chrome sépare ses sites en processus pour qu'un site fautif ne fasse pas tomber le navigateur
- [[Arithmétique en Bash]] : expressions arithmétiques entre doubles parenthèses, comme ((compteur++)) ou $(( n+1 ))
- [[Bande magnétique]] : stockage tertiaire en cartouches de plusieurs To, lues séquentiellement, pour l'archivage
- [[Bibliothèque partagée]] : fichiers de /lib utilisés par plusieurs programmes, partagés pour économiser la mémoire
- [[Blocs BEGIN et END d'AWK]] : blocs exécutés avant la lecture de la première ligne et après la dernière
- [[Bourne Shell (sh)]] : shell cité parmi les shells, sh fichier.sh exécutant un script
- [[Bus système]] : circuits de la carte mère reliant le CPU aux composants, bus de données, d'adresses et de contrôle
- [[Calcul haute performance]] : HPC, clusters dédiés aux calculs complexes, avec des applications écrites pour eux
- [[Caractère d'échappement]] : l'antislash \ échappe le caractère suivant, traité alors littéralement
- [[Carte mère]] : squelette commun des ordinateurs, portant socket du processeur, emplacements de RAM et slots d'extension
- [[Chargeur de démarrage]] : nommé dans le cours, sans définition
- [[Chemin de fichier]] : / sépare les répertoires, ~ désigne le répertoire personnel, . le répertoire courant
- [[Cloud computing]] : calcul, stockage et applications fournis comme service à travers un réseau
- [[Clé USB amorçable]] : clé créée avec Rufus à partir d'une image ISO pour installer un système sur PC
- [[Code ASCII]] : correspondance entre nombres et caractères, chaque touche du clavier ayant un code
- [[Commande cat]] : affiche le contenu d'un ou plusieurs fichiers sur la sortie standard
- [[Commande cd]] : change de répertoire, cd .. remontant au parent et cd ~ au répertoire personnel
- [[Commande chmod]] : modifie les permissions d'un fichier ou dossier, en notation octale ou symbolique
- [[Commande cp]] : copie un fichier, utilisée par les scripts de sauvegarde
- [[Commande date]] : affiche la date actuelle, dans un format imposable avec '+%Y-%m-%d'
- [[Commande df]] : df -h affiche le stockage utilisé et restant dans un format lisible
- [[Commande echo]] : affiche un texte ou une variable, « comme un print », ou l'écrit dans un fichier
- [[Commande free]] : free -h affiche la RAM utilisée et restante, ainsi que le swap
- [[Commande grep]] : cherche un motif dans un fichier ou dans une sortie de terminal
- [[Commande hostname]] : affiche ou change le nom de la machine, -f donnant le FQDN
- [[Commande ifconfig]] : affiche les interfaces réseau et leurs adresses, avec le paquet net-tools
- [[Commande info]] : troisième moyen, avec man et --help, de voir le détail d'une commande
- [[Commande ip]] : ip address affiche l'adresse IP locale et les interfaces réseau, paquet iproute2
- [[Commande jobs]] : affiche les tâches en cours dans le shell, le « pool of current jobs »
- [[Commande journalctl]] : sudo journalctl _COMM=sudo affiche l'historique des commandes sudo
- [[Commande kill]] : arrête une tâche de fond par kill %n, n étant le numéro de la tâche
- [[Commande ls]] : liste les fichiers du répertoire courant, ls -l les détaillant colonne par colonne
- [[Commande lscpu]] : liste les informations du processeur, architecture, nombre de CPU et modèle
- [[Commande lshw]] : liste les informations matérielles, installée avec sudo apt install lshw
- [[Commande man]] : affiche le manuel d'une commande, avec son détail
- [[Commande mkdir]] : crée un répertoire, ou toute une arborescence avec -p et des accolades
- [[Commande mv]] : sert à renommer un répertoire dans les rendus du TP2
- [[Commande nproc]] : affiche le nombre de cœurs de la machine
- [[Commande passwd]] : sudo passwd change le mot de passe, à distinguer du fichier /etc/passwd
- [[Commande ping]] : teste la connectivité entre deux hôtes, par adresse IP ou nom d'hôte
- [[Commande pwd]] : print working directory, affiche le répertoire courant
- [[Commande read]] : demande une saisie à l'utilisateur et la stocke dans une variable Bash
- [[Commande rm]] : supprime un fichier, ou un dossier et tout son contenu avec -r
- [[Commande rmdir]] : supprime un répertoire vide
- [[Commande shuf]] : génère des nombres aléatoires, avec plage d'entrée, nombre de sorties et répétition
- [[Commande sleep]] : sleep n attend n secondes, sleep 90 & créant une tâche de fond
- [[Commande sort]] : trie les lignes d'un fichier ou d'une sortie, -g selon la valeur numérique
- [[Commande su]] : sudo su donne les droits d'administrateur sans réécrire sudo à chaque commande
- [[Commande sudo]] : exécuter des commandes avec les privilèges de root sans se connecter en root
- [[Commande systemctl]] : gère les services, start, enable au démarrage et status, par exemple pour cron
- [[Commande tee]] : employée dans le DM pour écrire dans un fichier système avec les droits root
- [[Commande touch]] : crée un fichier vide, ou met à jour l'horodatage d'un fichier existant
- [[Commande tree]] : affiche une arborescence de répertoires
- [[Commande uname]] : affiche des informations sur le système, uname -r donnant la version du noyau
- [[Commande uniq]] : omet les lignes répétées, après sort -g pour des valeurs uniques triées
- [[Commande uptime]] : nommé dans le cours, sans définition
- [[Commande wc]] : affiche le nombre de lignes, de mots et d'octets, wc -l ne comptant que les lignes
- [[Commande which]] : indique où se trouve l'exécutable d'une commande, comme /usr/bin/bash
- [[Commande whoami]] : affiche le nom de l'utilisateur connecté, à distinguer de hostname
- [[Commandes fg et bg]] : mettre une tâche au premier plan avec fg, ou en arrière-plan avec bg
- [[Commandes shutdown et poweroff]] : éteindre le système avec sudo shutdown now ou sudo poweroff
- [[Commentaire en Bash]] : # sert à écrire un commentaire dans un script shell
- [[Compteur de programme]] : champ du PCB contenant l'emplacement de la prochaine instruction à exécuter
- [[Contrôleur de périphérique]] : adaptateur relié à chaque périphérique, qui gère sa communication avec le CPU
- [[Cycle mémoire]] : interaction complète entre CPU et RAM pour accéder à une donnée, adresse, lecture ou écriture, transmission
- [[Cœur de processeur]] : unité qui lit et exécute des instructions, une tâche à la fois
- [[Cœur en ligne et hors ligne]] : un cœur en ligne est actif, et on peut mettre un cœur hors ligne
- [[DHCP]] : nommé dans le cours, sans définition
- [[DNS]] : service qui fait la résolution d'adresse, conversion des noms d'hôte en adresses IP
- [[Dispatcher]] : composant qui effectue la commutation de contexte et donne le CPU au processus choisi
- [[Disposition du clavier]] : changement temporaire avec setxkbmap, ou permanent dans /etc/default/keyboard
- [[Disque dur]] : disque magnétique tournant vers 7 200 tr/min, dont une tête lit et écrit des points
- [[Disque optique]] : nommé dans le cours, sans définition
- [[Démarrage sécurisé]] : nommé dans le cours, sans définition
- [[Démon (informatique)]] : service en arrière-plan, comme le démon cron qui exécute les tâches planifiées
- [[EXT4]] : système de fichiers Linux, jusqu'à 1 exaoctet, avec chiffrement et compression
- [[Environnement de bureau]] : nommé dans le cours, sans définition
- [[Environnement informatique]] : environnements traditionnel, mobile et autres, distingués au chp 1
- [[Espace d'échange (swap)]] : espace disque utilisé quand la RAM est pleine, mémoire virtuelle plus lente
- [[Espace mémoire d'un processus]] : sections text, pile, données et tas d'un processus en mémoire
- [[Expansion d'accolades]] : {} se développe en plusieurs options, comme touch file{1..20}.txt
- [[Expression régulière]] : en AWK, motif écrit entre deux /, sensible à la casse
- [[Exécution d'un script]] : ./fichier.sh respecte le shebang et exige la permission d'exécution
- [[FAT32]] : système de fichiers Windows limité à 4 Go par fichier, sans chiffrement ni compression
- [[Fichier CSV]] : fichier texte structuré dont les champs sont séparés par des virgules
- [[Fichier TSV]] : fichier texte structuré dont les champs sont séparés par des tabulations
- [[Fichier de périphérique]] : fichiers spéciaux de /dev qui représentent disques, interfaces réseau et imprimantes
- [[Fichier hosts]] : fichier texte local qui associe des noms d'hôte à des adresses IP
- [[Fichier journal]] : journaux rangés dans /var, comme l'historique de sudo dans auth.log
- [[Fichier shells]] : /etc/shells liste les shells installés, les valid login shells
- [[Fichier sudoers]] : fichier des droits sudo, ouvert avec sudo visudo
- [[Fichiers de mots de passe]] : /etc/passwd, présenté comme contenant les mots de passe des utilisateurs
- [[Fonction system() en C]] : employée au TP4 pour faire exécuter une commande shell par le processus fils
- [[Fonctions intégrées d'AWK]] : fonctions comme tolower() et gsub() pour traiter les chaînes en AWK
- [[Formatage d'un disque]] : créer sur un disque un système de fichiers géré par l'OS, pour y lire et écrire
- [[GCC]] : nommé dans le cours, sans définition
- [[Gedit]] : nommé dans le cours, sans définition
- [[Gestionnaire de verrous distribué]] : DLM, empêche plusieurs nœuds d'un cluster d'accéder en même temps aux mêmes données
- [[Groupement de commandes]] : accolades { } qui groupent des commandes exécutées dans le shell courant
- [[Guillemets en shell]] : apostrophes gardant la valeur littérale, guillemets laissant développer les variables
- [[Hachage de mot de passe]] : mot de passe stocké sous forme hachée, que le système ne laisse pas voir
- [[Hyperthreading]] : transformer chaque cœur physique en plusieurs cœurs virtuels exécutant plusieurs tâches
- [[IDE (PATA)]] : ancienne interface pour disques durs et lecteurs optiques, à câbles parallèles
- [[IPv6]] : nommé dans le cours, sans définition
- [[Identifiant de processus]] : PID, numéro unique par lequel chaque processus est identifié et géré
- [[Image ISO]] : copie complète et exacte d'un disque optique, pour distribuer des logiciels ou installer un système
- [[Image initrd]] : nommé dans le cours, sans définition
- [[Interface de stockage]] : méthode de connexion et de communication entre le disque et le reste de l'ordinateur
- [[Interface en ligne de commande]] : CLI, le shell permettant d'interagir avec le système par des commandes
- [[Interface graphique]] : GUI, moyen de lancer un programme qui a succédé à la seule CLI
- [[Interface réseau]] : sous Linux, eth0 pour l'Ethernet, wlan0 pour le Wi-Fi, lo pour la boucle locale
- [[Joker (wildcard)]] : méta-caractères * et ? du shell pour désigner plusieurs fichiers à la fois
- [[Lien symbolique]] : nommé dans le cours, sans définition
- [[Linux]] : famille de systèmes libres fondés sur le noyau Linux, complétés par une distribution
- [[M.2]] : connecteur de stockage de la carte mère pour de petites plaques souvent vissées
- [[MBR]] : Master Boot Record, indique au firmware la partition du système et charge l'OS en RAM
- [[Modèle client-serveur]] : serveurs de calcul et serveurs de fichiers répondant aux demandes des clients
- [[Multitâche sur mobile]] : certains systèmes mobiles ne laissent tourner qu'un processus au premier plan
- [[Mémoire cache]] : mémoire très rapide dans le CPU, qui garde les données et instructions souvent utilisées
- [[Mémoire morte]] : ROM, mémoire non modifiable qui conserve ses données après l'arrêt, où est stocké le BIOS
- [[Mémoire vive]] : espace où sont stockées et transférées les données que traite le CPU
- [[Mémoire volatile et non volatile]] : stockage qui perd ses données sans courant (registres, cache, RAM), ou les garde
- [[Méta-caractère]] : symboles spéciaux qui contrôlent l'interprétation des commandes, en six familles au TP2
- [[NFS]] : nommé dans le cours, sans définition
- [[NTFS]] : système de fichiers Windows avec gros fichiers, chiffrement et compression
- [[NVMe]] : interface surtout utilisée pour les SSD, extrêmement rapide, souvent via PCIe
- [[Netplan]] : outil de configuration réseau par défaut d'Ubuntu, en fichiers YAML dans /etc/netplan
- [[Nom d'hôte]] : identifiant unique et lisible d'une machine sur le réseau, à la place de l'adresse IP
- [[Nombres aléatoires en C]] : rand() de stdlib.h génère des entiers aléatoires, initialisé par srand(time(NULL))
- [[Option --help]] : affiche l'aide d'une commande, syntaxe, description et options
- [[Opérateur de comparaison]] : en Bash, -eq, -ne, -gt et autres dans [ ], ou <, > dans (( ))
- [[Opérateur logique]] : ET et OU en Bash et en AWK, dans ou entre les tests
- [[Opération d'entrée-sortie]] : requête d'E/S, transfert des données, puis interruption, en trois temps
- [[PCI Express]] : nommé dans le cours, sans définition
- [[Partition (disque)]] : section logique du disque, traitée par l'OS comme un disque séparé
- [[Partition de démarrage]] : /boot, petite partition contenant le noyau, l'initrd et la configuration du chargeur
- [[Partition système EFI]] : nommé dans le cours, sans définition
- [[Partitions Linux]] : partitions d'un système Linux, racine /, /boot, /home, swap, selon le cours
- [[Pilote de périphérique]] : driver, programme propre à un type de périphérique, intermédiaire entre contrôleur et OS
- [[Point de montage]] : répertoire où une partition est montée, pour accéder aux volumes depuis la racine
- [[Processeur]] : CPU, « cerveau » de l'ordinateur, qui interprète les instructions en quatre temps
- [[Processus init]] : processus système qui devient le parent des orphelins, et les gère et nettoie
- [[Processus limité par les entrées-sorties ou par le processeur]] : processus I/O bound surtout en attente, ou CPU bound surtout en calcul
- [[Quantum de temps]] : tranche de temps d'exécution d'un processus, qui revient en ready queue à son expiration
- [[ReFS]] : nommé dans le cours, sans définition
- [[Registre du processeur]] : mémoire située dans le CPU, au sommet de la hiérarchie de stockage
- [[Répertoire personnel]] : répertoire de chaque utilisateur sous /home, avec ses fichiers et réglages, noté ~
- [[Répertoire racine]] : répertoire le plus haut de la hiérarchie, noté /, point de départ de tous les autres
- [[Réseau de stockage SAN]] : nommé dans le cours, sans définition
- [[SAS (interface de stockage)]] : Serial Attached SCSI, version plus récente et plus rapide de SCSI
- [[SATA]] : Serial ATA, interface de disque la plus courante, en série, plus rapide que l'IDE
- [[SCSI]] : Small Computer System Interface, interface de stockage des serveurs et stations de travail
- [[SSD]] : stockage secondaire non volatile en mémoire flash, bien plus rapide que le HDD
- [[Sauvegarde de fichier]] : copier un fichier à intervalles réguliers et ranger la copie ailleurs dans le système
- [[Secteur défectueux]] : nommé dans le cours, sans définition
- [[Shebang]] : #! en tête de script, qui indique au système l'interpréteur à utiliser
- [[Shell dash]] : nommé dans le cours, sans définition
- [[Shell rbash]] : nommé dans le cours, sans définition
- [[Sous-shell]] : ( ) groupe des commandes exécutées dans un sous-shell, sans changer le shell courant
- [[Substitution de commande]] : $(...) exécute une commande et la remplace par son résultat
- [[Suite arithmétique]] : nommé dans le cours, sans définition
- [[Super-utilisateur root]] : utilisateur aux privilèges complets, dont sudo donne les droits
- [[Système de fichiers exFAT]] : système de fichiers Windows pour gros fichiers, sans chiffrement ni compression
- [[Système distribué]] : systèmes séparés, éventuellement hétérogènes, reliés en réseau
- [[Système en grappe (cluster)]] : ordinateurs qui travaillent ensemble et partagent un stockage centralisé via un SAN
- [[Système monoprocesseur]] : un processeur pour les tâches générales, avec des processeurs locaux spécialisés
- [[Système multiprocesseur]] : système parallèle dont les processeurs partagent bus, mémoire et périphériques
- [[Séparateur de champs]] : caractère qui sépare les données d'un fichier, espace, tabulation, virgule ou autre
- [[Tableau (programmation)]] : stocke plusieurs éléments sous un seul nom, chacun accessible par son indice
- [[Tampon (buffer)]] : petite mémoire propre à un périphérique, qui stocke les données avant leur transfert
- [[Terminaison en cascade]] : quand un parent s'arrête, l'OS termine aussi tous ses enfants
- [[Thread]] : flux d'exécution d'un processus, le thread principal exécutant les instructions en séquence
- [[Tâche en arrière-plan]] : & lance une commande en arrière-plan, ; enchaîne des commandes à la suite
- [[Ubuntu]] : distribution Linux libre, la plus populaire selon le cours, simple et stable
- [[Variable Bash]] : affectation sans espace autour de =, lecture par $, variables système ou utilisateur
- [[Variables intégrées d'AWK]] : variables prédéfinies d'AWK comme NR, numéro de la ligne courante
- [[Version LTS et version intermédiaire]] : publication stable supportée longtemps, ou version intermédiaire moins stable au support court
- [[Vim]] : nommé dans le cours, sans définition
- [[Wayland et X11]] : nommé dans le cours, sans définition
- [[XFS]] : système de fichiers Linux, jusqu'à 1 exaoctet, avec chiffrement et compression
- [[YAML]] : format des fichiers de configuration de Netplan, sensible à l'indentation
- [[Éditeur de texte]] : logiciel pour créer et modifier des fichiers texte, comme Nano, Vim et Gedit
- [[Éditeur nano]] : éditeur ouvert par nano fichier, Ctrl+O pour sauvegarder et Ctrl+X pour quitter

**Year 2 - Philosophie**

- [[Aliénation]] : selon Marx, division du travail et automatisation font de l'ouvrier un simple exécutant aliéné
- [[Espace qualitatif et espace quantitatif]] : espace qualitatif d'Aristote, contre lequel Pascal défend l'existence du vide
- [[Force plastique]] : notion de Nietzsche, principe d'individuation propre aux êtres vivants
- [[Homo faber]] : l'homme fabricateur, dont l'homo faber contemporain est « dispensé d'être lui-même technicien »
- [[Héliocentrisme]] : nommé dans le cours, sans définition
- [[Maîtrise de la nature]] : Bacon, « savoir, c'est pouvoir », et Descartes, se rendre maître de la nature
- [[Monde sublunaire et supralunaire]] : cosmos fini et harmonieux d'Aristote et Ptolémée, divisé en deux mondes
- [[Nature comme réserve de ressources]] : pour Heidegger, la technique moderne transforme tout en ressource exploitable, y compris l'homme
- [[Organisme et machine]] : selon Kant, l'organisme s'adapte, se reproduit et se répare, pas la machine
- [[Paysage dans l'art]] : genre devenu à la Renaissance lieu de virtuosité, sous trois formes dont le pittoresque
- [[Philosophie de l'histoire]] : donner un sens à l'histoire, à la différence de la simple étude du passé
- [[Pont aux ânes]] : nommé dans le cours, sans définition
- [[Principe responsabilité]] : Hans Jonas, la capacité de modifier la nature appelle-t-elle une responsabilité à son égard
- [[Progrès moral]] : Kant distingue le progrès scientifique et technique du progrès moral
- [[Progrès transhistorique]] : Pascal compare l'apprentissage de l'humanité à celui d'un individu, progrès qui traverse les époques
- [[Ruse de la raison]] : « l'outil est la ruse de la raison », citation attribuée à Hegel
- [[Révolution scientifique]] : la nature n'est plus expliquée par des causes mais par des lois mathématiques
- [[Sentience]] : concept d'éthologie désignant la conscience des animaux, au-delà du modèle stimulus-réaction
- [[Système technicien]] : Jacques Ellul, la technique suit sa propre logique, indépendante des valeurs humaines
- [[Technicité]] : Simondon distingue effets sociaux de l'automatisation et nature technique des objets
- [[Technè, praxis et épistémè]] : chez Aristote, art de faire, action éthique et politique, savoir théorique
- [[Transduction]] : chez Simondon, capacité des machines à transformer leurs états internes pour s'adapter

**Year 2 - Probability**

- [[Combinaison (dénombrement)]] : sous-ensemble non ordonné de taille k, chacune correspondant à k! permutations
- [[Corrélation et causalité]] : une corrélation n'implique pas une relation de cause à effet
- [[Diagramme en bâtons et histogramme de probabilité]] : deux représentations de la loi d'une variable aléatoire discrète
- [[Ensemble dénombrable]] : ensemble dont on peut associer les éléments aux entiers, comme ℕ
- [[Expérience aléatoire]] : action d'issue incertaine, répétable dans des conditions identiques
- [[Indépendance d'événements]] : A et B indépendants si $P(A\cap B) = P(A)P(B)$
- [[Indépendance de variables aléatoires]] : loi jointe égale au produit des lois marginales, en discret comme en continu
- [[Loi binomiale négative]] : nombre d'essais indépendants pour obtenir r succès de probabilité p
- [[Loi hypergéométrique]] : tirage sans remise de n éléments dans une population de N avec M succès
- [[Loi uniforme]] : densité constante $\frac{1}{B-A}$ sur [A, B] et nulle ailleurs
- [[Moyenne empirique]] : $\bar X = (X_1 + \dots + X_n)/n$, combinaison linéaire « très importante » de variables aléatoires
- [[Permutation (dénombrement)]] : suite ordonnée de k objets distincts pris sans remise parmi n
- [[Quantile]] : le (100p)-ième percentile $\eta_p$ vérifie $F(\eta_p) = p$
- [[Théorème de transformation]] : densité de $Y = g(X)$ pour g strictement monotone, $f_X(h(y))$ fois la valeur absolue de $h'(y)$
- [[Équiprobabilité]] : toutes les issues ont la même probabilité, $P(A)$ valant le cardinal de A sur celui de S
- [[Événement (probabilités)]] : sous-ensemble de l'espace d'échantillonnage S, simple ou composé
- [[Événements incompatibles]] : événements disjoints sans issue commune, $P(A\cup B) = P(A) + P(B)$

**Year 2 - Projet Design**

- [[Accompagnement social]] : évaluer la situation puis mettre en place un accompagnement, selon la structure du projet Edossah
- [[Anxiété crépusculaire et agitation]] : troubles fréquents comme cris et déambulation, souvent à l'origine de prescriptions
- [[Apathie]] : trouble qui peut apparaître très tôt et précéder les déficiences cognitives, distinct de la dépression
- [[Capital d'attractivité]] : nommé dans le cours, sans définition
- [[EHPAD]] : nommé dans le cours, sans définition
- [[Grille AGGIR]] : mesure la perte d'autonomie d'une personne âgée à partir de dix activités
- [[Intelligence collective]] : le plus souvent, des moments de travail collectif, selon le brief « santé au travail »
- [[Jeu de rôle]] : atelier Edossah où les participants jouent travailleur social, bénéficiaire et représentant face à une urgence
- [[Médiation sociale]] : nommé dans le cours, sans définition
- [[Plaidoyer]] : nommé dans le cours, sans définition
- [[Travail social]] : mission d'accompagner les publics en difficulté, selon le brief Edossah
- [[Triangle d'acteurs]] : outil d'analyse plaçant résidents, personnel et famille aux pôles d'un triangle
- [[Étude d'impact]] : nommé dans le cours, sans définition

**Year 2 - SHS**

- [[AEIOU]] : grille d'observation de terrain, Activité, Environnement, Interaction, Objet, Utilisateur
- [[Anthropologie]] : étude de l'Homme en tant qu'espèce, avec l'anthropologie visuelle née fin XIXe siècle
- [[Chronophotographie]] : photos successives de Marey et Muybridge, montrant que les chevaux ont toujours des pattes en l'air
- [[Ethnographie]] : étude des groupes humains et de leur culture
- [[Ethnographie visuelle]] : étudier, écrire et représenter une culture à l'aide de supports visuels
- [[Infra-ordinaire]] : nommé dans le cours, sans définition
- [[Netnographie]] : branche de l'ethnographie consacrée au numérique, dialogique et malléable
- [[Neuf dimensions de Spradley]] : dimensions qui servent à croiser les observations, des grands tours aux détails
- [[Observation de terrain]] : observation fondée sur le réel, mot qui date de la Renaissance
- [[Observation participante]] : observation par immersion complète dans le terrain, apparue au XXe siècle
- [[Photovoice]] : donner sa caméra aux personnes observées, qui font elles-mêmes le reportage
- [[Plan de recherche 4C]] : compagnie, consommateur, catégorie et canaux de distribution
- [[Problème complexe]] : problème où entrent en jeu beaucoup de facteurs, contrairement au problème seulement compliqué
- [[Réflexivité]] : recherche d'un regard plus objectif en ethnographie, l'observateur ne pouvant être objectif à 100 %
- [[Sites et modalités d'analyse d'une image]] : une photo n'est pas objective, on analyse l'auteur, l'image et les spectateurs
- [[Tournant iconique]] : « The Iconic Turn » de Gottfried Boehm, avènement d'une culture de l'image
- [[Types d'analyse d'une image]] : huit types d'analyse, anthropologique, de discours, de contenu, compositionnelle, sémiotique…
- [[Types de suivi en observation]] : quatre manières de suivre ce qu'on observe, comme le lampadaire ou la lampe frontale
- [[Usages de l'image en ethnographie]] : usages de l'image en ethnographie, dont la note de terrain, usage principal
- [[Utilisateur extrême]] : nommé dans le cours, sans définition

**Year 3 - Affordance**

- [[Analyse de l'activité]] : nommé dans le cours, sans définition
- [[Arborescence d'une application]] : nommé dans le cours, sans définition
- [[Cahier des charges]] : nommé dans le cours, sans définition
- [[Carte d'expérience]] : nommé dans le cours, sans définition
- [[Effet Hawthorne]] : nommé dans le cours, sans définition
- [[Effet de halo]] : nommé dans le cours, sans définition
- [[Enquête qualitative et quantitative]] : deux manières d'enquêter, opposées terme à terme par le cours de SHS
- [[Focus group]] : nommé dans le cours, sans définition
- [[Grille d'observation]] : mise en pratique des hypothèses et objectifs de l'étude, préparée et testée à l'avance
- [[Interaction homme-machine]] : nommé dans le cours, sans définition
- [[Panel d'utilisateurs]] : groupe de participants d'un test, aussi proche que possible de la population cible
- [[Questionnaire]] : méthode de collecte de données quantitatives et qualitatives sur des usages existants
- [[Recherche utilisateur]] : ensemble des méthodes de recueil des besoins et des usages
- [[Scénario d'usage]] : mise en scène réaliste des tâches à tester, un seul objectif par scénario
- [[Storyboard]] : nommé dans le cours, sans définition
- [[Test utilisateur]] : des utilisateurs cibles testent individuellement le produit sur des scénarios représentatifs
- [[Tri de cartes]] : nommé dans le cours, sans définition
- [[Utilisabilité]] : qualité évaluée par le test utilisateur selon l'efficacité, l'efficience et la satisfaction
- [[Échelles UX]] : nommé dans le cours, sans définition
- [[Évaluation experte]] : nommé dans le cours, sans définition

**Year 3 - Computer Network**

- [[BGP]] : nommé dans le cours, sans définition
- [[Boucle de routage]] : nommé dans le cours, sans définition
- [[Commutateur]] : switch qui relie les terminaux au LAN, des Cisco 2960 en cours
- [[Convergence d'un protocole de routage]] : nommé dans le cours, sans définition
- [[Domaine de diffusion]] : domaine de broadcast, unique par défaut sur un switch Cisco, que les VLAN divisent
- [[EIGRP]] : exemple d'IGP utilisé à l'intérieur d'un système autonome, non détaillé par le cours
- [[Encapsulation 802.1Q]] : commande encapsulation dot1q, qui associe une sous-interface à son VLAN
- [[IANA]] : organisme qui attribuait les réseaux selon la taille des entreprises, au temps des classes
- [[ICMP]] : nommé dans le cours, sans définition
- [[IETF]] : nommé dans le cours, sans définition
- [[Multicast]] : nommé dans le cours, sans définition
- [[Numéro de port]] : identifiant de couche 4, utilisé par le PAT et par les listes de contrôle d'accès
- [[OSPF]] : nommé dans le cours, sans définition
- [[Octet]] : groupe de 8 bits, une adresse IPv4 comptant quatre octets
- [[Pare-feu]] : nommé dans le cours, sans définition
- [[Passerelle par défaut]] : nommé dans le cours, sans définition
- [[Routage IP]] : acheminement des paquets IP d'un réseau source à un réseau destination, via des routeurs
- [[Routage classful et classless]] : RIPv1 classful sans masques dans ses mises à jour, RIPv2 classless
- [[Routeur]] : équipement qui relie des réseaux différents et choisit le chemin des paquets par sa table de routage
- [[Réseau local]] : nommé dans le cours, sans définition
- [[Résumé automatique de routes]] : résumé des routes à la frontière de leur classe, désactivé par no auto-summary
- [[Sous-interface]] : une sous-interface par VLAN sur l'interface du routeur reliée au trunk, pour le routage inter-VLAN
- [[Système autonome]] : réseau d'une organisation, où servent les IGP, les EGP reliant les systèmes autonomes
- [[VLSM]] : nommé dans le cours, sans définition

**Year 3 - Culture du vivant**

- [[Accord de Kunming-Montréal]] : accord de 2022 sur la biodiversité fixant 23 cibles, cité dans une chronologie
- [[Accord de Paris]] : nommé dans le cours, sans définition
- [[Biocapacité]] : capacité de production biologique de la planète en hectares globaux, de 3,2 à 1,5 par personne
- [[Bioremédiation]] : nommé dans le cours, sans définition
- [[Biosphère]] : la Nature et le Vivant comme écosystème, modèle d'interdépendance dont l'homme fait partie
- [[Bioéconomie]] : nommé dans le cours, sans définition
- [[Bombes climatiques]] : 425 sites d'extraction fossile représentant chacun plus d'une gigatonne de CO2
- [[Boussole des possibles]] : nommé dans le cours, sans définition
- [[CSRD]] : nommé dans le cours, sans définition
- [[Cartésianisme]] : en séparant l'homme de la nature, il lui a donné la raison de l'exploiter, selon le manifeste
- [[Coûts cachés]] : coût économique et social caché des achats du quotidien, comme déforestation ou travail des enfants
- [[Cradle to cradle]] : premier pilier de l'économie circulaire, « fermer le cycle de vie des produits »
- [[Cycle de vie d'un produit]] : cycle décomposé en cinq étapes, chacune avec les questions que posent les clients
- [[Design social]] : nommé dans le cours, sans définition
- [[Devoir de vigilance]] : nommé dans le cours, sans définition
- [[Effet de serre]] : nommé dans le cours, sans définition
- [[Empreinte écologique]] : concept de Mathis Wackernagel, comparé à la biocapacité sur un graphique de 1961 à 2024
- [[Entreprise à mission]] : nommé dans le cours, sans définition
- [[Finance durable]] : nommé dans le cours, sans définition
- [[GIEC]] : nommé dans le cours, sans définition
- [[Habitabilité]] : selon Alain Findeli, le but du design est d'améliorer ou maintenir l'habitabilité du monde
- [[IPBES]] : nommé dans le cours, sans définition
- [[Jour du dépassement]] : date calculée par le Global Footprint Network, biocapacité sur empreinte écologique fois 365
- [[Manifeste pour le vivant]] : manifeste de CY École de design, fondé notamment sur l'inséparabilité de l'homme et de la nature
- [[Objectifs de développement durable]] : nommé dans le cours, sans définition
- [[Permaculture]] : nommé dans le cours, sans définition
- [[Protocole de Kyoto]] : nommé dans le cours, sans définition
- [[Pyramide des besoins]] : nommé dans le cours, sans définition
- [[Radical design]] : mouvement de 1966-1968, Sottsass, Mendini, Branzi, opposé au « good design »
- [[Rapport Meadows]] : « The Limits to Growth » (1972), commandé par le Club de Rome, trois scénarios du MIT
- [[Réemploi, recyclage et reconditionnement]] : trois façons de prolonger la vie des objets, distinguées par le dossier ReYOU
- [[Sixième extinction]] : nommé dans le cours, sans définition
- [[Sobriété]] : deuxième solution du dernier cours, chasse au gaspillage, réduction des impacts, renoncements
- [[Sommet de la Terre de Rio]] : nommé dans le cours, sans définition
- [[Taxonomie européenne]] : nommé dans le cours, sans définition
- [[Théorie du Donut]] : Kate Raworth ajoute des fondations sociales aux frontières planétaires, pour un espace sûr et juste
- [[Tournant relationnel]] : nommé dans le cours, sans définition
- [[Transhumanisme]] : nommé dans le cours, sans définition
- [[Valeur socio-écologique]] : valeur dont la reconnaissance est visée pour intégrer le vivant dans les décisions économiques
- [[Warming stripes]] : visualisation d'Ed Hawkins (2018), montrée pour illustrer l'humain comme force géologique
- [[Zone critique]] : fine « peau » d'environ 20 km à la surface du globe, où nous sommes confinés
- [[Zéro artificialisation nette]] : objectif ZAN en 2050 de la loi Climat et Résilience (2021)
- [[Écologie industrielle et territoriale]] : pilier de l'économie circulaire, illustré par le port de Kalundborg
- [[Économie de la fonctionnalité]] : pilier de l'économie circulaire, « économie de la fonctionnalité et de la coopération »
- [[Érosion de la biodiversité]] : perte de biodiversité, dont le cours donne cinq causes, à commencer par la destruction des habitats

**Year 3 - Data analysis (Thanos)**

- [[Approximation normale]] : le théorème central limite justifie d'approcher binomiale, Poisson et autres lois par une normale
- [[Bibliothèque ggplot2]] : nommé dans le cours, sans définition
- [[Carré moyen]] : somme des carrés divisée par son nombre de degrés de liberté, en ANOVA
- [[Centrage et réduction]] : centrer en soustrayant la moyenne, mettre à l'échelle en divisant par l'écart-type
- [[Cercle des corrélations]] : graphe des variables d'une ACP, lu par les angles entre variables
- [[Coefficient de corrélation de Spearman]] : corrélation de rang non paramétrique, qui mesure une relation monotone
- [[Coefficient de détermination]] : $R^2$, proportion de la variation de Y expliquée par X, entre 0 et 1
- [[Coefficient de variation]] : $CV = s / \bar X \times 100\,\%$, pertinent pour les données de ratio
- [[Data frame]] : structure rectangulaire de R, liste de vecteurs de même longueur à types mélangés
- [[Diagramme tige et feuilles]] : graphique des données quantitatives, la tige portant ici les dizaines
- [[Erreur d'échantillonnage]] : erreur venant du processus d'échantillonnage lui-même, par exemple un échantillon trop petit
- [[Erreur de type I et de type II]] : rejeter $H_0$ vraie, ou ne pas rejeter $H_0$ fausse
- [[Erreur standard de la régression]] : écart-type des erreurs d'une régression linéaire simple, $s = \sqrt{SSE/(n-2)}$
- [[Extremum local d'une fonction de deux variables]] : recherche des points critiques de f(b, m) pour la droite des moindres carrés
- [[Facteur (variable catégorielle)]] : variable catégorielle, à déclarer en R, contrairement au régresseur continu
- [[Fonction Gamma]] : $\Gamma(x) = \int_0^\infty t^{x-1}e^{-t}\,dt$, présente dans la densité de la loi du χ²
- [[Fonction de répartition empirique]] : nommé dans le cours, sans définition
- [[Forme d'une distribution]] : distribution symétrique unimodale, bimodale, ou à asymétrie positive ou négative
- [[Formule de modèle en R]] : opérateurs d'une formule de modèle en R, qui ajoutent ou retirent des termes
- [[Histogramme]] : graphique en classes d'égale largeur, la hauteur de chaque barre proportionnelle à sa fréquence
- [[Homoscédasticité]] : variance constante de l'erreur, condition de la régression linéaire vérifiée sur les résidus
- [[Langage R]] : langage où tout passe par des fonctions et où tout est un objet
- [[Loadings et scores (ACP)]] : poids des variables dans une composante principale, et coordonnées des échantillons dans le système tourné
- [[Matrice de covariance]] : matrice des variances sur la diagonale et des covariances ailleurs
- [[Mesures de tendance centrale]] : mode, médiane et moyenne d'une série de données
- [[Module, paquet, bibliothèque et framework]] : du plus petit morceau de logiciel réutilisable aux ensembles plus vastes
- [[Modèle déterministe et probabiliste]] : relation exacte comme F = ma, ou relation à laquelle s'ajoute une erreur aléatoire
- [[P-value]] : probabilité d'obtenir des résultats au moins aussi extrêmes si $H_0$ est vraie
- [[Paramètre et statistique]] : caractéristique numérique de la population, ou fonction des observations de l'échantillon
- [[Population et échantillon]] : ensemble des sujets étudiés, et partie effectivement testée
- [[Quatuor d'Anscombe]] : quatre jeux de données (1973) aux mêmes statistiques mais aux formes différentes
- [[Réduction de dimension]] : passer de nombreuses variables à deux ou trois composantes pour visualiser les données
- [[Résidu (régression)]] : écart $e_i = Y_i - \hat Y_i$ entre observation et prédiction
- [[Seuil de signification]] : $\alpha$, probabilité de rejeter $H_0$ vraie, en général 0,05 ou 0,01
- [[Somme des carrés (SST, SSR, SSE)]] : variation totale, expliquée par la régression et résiduelle
- [[Statistique de test]] : variable aléatoire calculée sur l'échantillon, comparant les données à l'attendu sous $H_0$
- [[Statistique descriptive]] : branche de la statistique qui collecte, présente et caractérise les données
- [[Statistique inférentielle]] : conclure sur les paramètres de la population à partir de statistiques d'échantillon
- [[Surapprentissage]] : un modèle à trop de variables mémorise le bruit du jeu de données
- [[Tableau de contingence]] : tableau croisé de deux variables catégorielles, support du test du χ²
- [[Tau de Kendall]] : coefficient de corrélation non paramétrique fondé sur les rangs, alternative à Pearson
- [[Test Z]] : test utilisé quand $\sigma$ est connu ou que les échantillons sont grands
- [[Test binomial]] : nommé dans le cours, sans définition
- [[Test d'hypothèse]] : démarche pour décider sur un paramètre de la population à partir d'un échantillon
- [[Test de Kolmogorov-Smirnov]] : nommé dans le cours, sans définition
- [[Test de Mann-Whitney]] : nommé dans le cours, sans définition
- [[Test de McNemar]] : nommé dans le cours, sans définition
- [[Test de Wilcoxon]] : nommé dans le cours, sans définition
- [[Test de la médiane]] : nommé dans le cours, sans définition
- [[Test de la pente]] : test de $H_0 : \beta_1 = 0$, absence de relation linéaire, en régression simple
- [[Test des runs]] : nommé dans le cours, sans définition
- [[Test du signe]] : nommé dans le cours, sans définition
- [[Test paramétrique et non paramétrique]] : test disposant d'une information sur un paramètre de la population, ou non
- [[Test t]] : remplace le test Z quand $\sigma$ est inconnu et l'échantillon petit, loi de Student
- [[Test unilatéral et bilatéral]] : $\alpha$ partagé entre les deux queues, ou placé dans une seule
- [[Trace d'une matrice]] : somme des coefficients diagonaux, variance totale pour une matrice de covariance
- [[Type de variable statistique]] : variable qualitative, nominale ou ordinale, ou quantitative
- [[Valeur critique]] : seuil à partir duquel on rejette $H_0$ dans un test
- [[Variable indicatrice]] : nommé dans le cours, sans définition
- [[Vraisemblance]] : va des données vers les paramètres, à l'inverse de la probabilité
- [[Échantillons appariés et indépendants]] : mesures répétées sur les mêmes sujets, ou sur des groupes distincts

**Year 3 - Data base**

- [[Architecture n-tiers]] : architectures d'accès à une base de données, client-serveur 2 tiers, web 3 tiers…
- [[Dictionnaire de données]] : première étape de MERISE, liste des données non décomposables avec nom et type
- [[Gestion des droits SQL]] : GRANT donne un droit, REVOKE le retire
- [[Système de gestion de base de données]] : logiciel qui gère une base de données, le SGBDR étant relationnel
- [[Table de correspondance]] : table qui traduit une association N-N, son couple d'attributs formant la clé primaire
- [[Type d'association]] : traduction d'une association dans le schéma relationnel selon ses cardinalités
- [[Types de données SQL]] : types de colonnes texte, nombres et dates, comme VARCHAR, INT, DECIMAL ou DATE
- [[UML]] : nommé dans le cours, sans définition
- [[Valeur NULL]] : colonne NULL si elle peut être vide, NOT NULL si elle est obligatoire

**Year 3 - IA**

- [[AlphaGo Zero]] : nommé dans le cours, sans définition
- [[Apprentissage automatique]] : selon Mitchell (1997), un système apprend d'une expérience E à réaliser une tâche
- [[Apprentissage non supervisé]] : nommé dans le cours, sans définition
- [[Apprentissage par renforcement]] : nommé dans le cours, sans définition
- [[Apprentissage profond]] : nommé dans le cours, sans définition
- [[Apprentissage supervisé]] : apprentissage où chaque instance a des variables prédictives et une variable cible à prédire
- [[Biais politique des IA]] : boussole politique des modèles d'IA en 2025, présentée par le cours
- [[Conférence de Dartmouth]] : nommé dans le cours, sans définition
- [[Consommation énergétique de l'IA]] : chiffres de 2025 sur l'énergie d'entraînement des modèles, comme DeepSeek-V3
- [[Deep Blue]] : nommé dans le cours, sans définition
- [[Deepfake]] : nommé dans le cours, sans définition
- [[Domaine public]] : nommé dans le cours, sans définition
- [[ELIZA]] : nommé dans le cours, sans définition
- [[Entraînement et inférence]] : nommé dans le cours, sans définition
- [[IA hybride]] : nommé dans le cours, sans définition
- [[IA malveillante]] : nommé dans le cours, sans définition
- [[Intelligence artificielle]] : terme proposé à la conférence de Dartmouth en 1956, histoire en quatre temps
- [[Logic Theorist]] : nommé dans le cours, sans définition
- [[Modèle d'IA propriétaire ou ouvert]] : modèles fermés comme OpenAI ou Midjourney, ouverts comme DeepSeek ou Mistral
- [[Modèle de diffusion]] : nommé dans le cours, sans définition
- [[Neurone de McCulloch-Pitts]] : nommé dans le cours, sans définition
- [[Perceptron]] : nommé dans le cours, sans définition
- [[Petit réacteur modulaire]] : nommé dans le cours, sans définition
- [[Prompt (IA)]] : trois types de prompts pour la génération d'images, dont le prompt de texte détaillé
- [[Réseau de neurones convolutif]] : nommé dans le cours, sans définition
- [[Réseau de neurones récurrent]] : nommé dans le cours, sans définition
- [[Système expert]] : nommé dans le cours, sans définition
- [[TPU]] : nommé dans le cours, sans définition
- [[Test de Turing]] : nommé dans le cours, sans définition
- [[Token (IA)]] : une IA d'image répartit un nombre fixe de tokens entre les éléments de l'image
- [[Transformer (IA)]] : nommé dans le cours, sans définition

**Year 3 - Java**

- [[Associativité et ordre d'évaluation]] : ordre des opérations de même précédence, à gauche pour les binaires en Java
- [[Compilation et bytecode]] : javac compile le source en fichier .class de bytecode, que java exécute
- [[Constante (programmation)]] : en Java, déclarée avec final et écrite en majuscules, non modifiable
- [[Effet de bord]] : nommé dans le cours, sans définition
- [[Langage Java]] : langage sensible à la casse, avec méthode main, compilé en bytecode
- [[Méthode main]] : méthode exécutée en premier, obligatoire dans toute application Java
- [[Opérateur conditionnel]] : opérateur ternaire condition ? vrai : faux de Java
- [[Opérateur d'incrémentation]] : ++ et -- ajoutent ou retirent 1, et leur position compte
- [[Unicode]] : nommé dans le cours, sans définition
- [[Variable (programmation)]] : en Java, déclarée par type et nom, avec des règles de nommage

**Year 3 - Projet courts**

- [[Bienveillance organisationnelle]] : nommé dans le cours, sans définition
- [[Bullshit jobs]] : nommé dans le cours, sans définition
- [[Burn-out]] : terme central de la fiche ressources « santé au travail », ou épuisement professionnel
- [[Conception centrée utilisateur]] : nommé dans le cours, sans définition
- [[Design des politiques publiques]] : nommé dans le cours, sans définition
- [[Fordisme]] : nommé dans le cours, sans définition
- [[Harcèlement moral]] : nommé dans le cours, sans définition
- [[Jury citoyen]] : démarche de démocratie participative au Taillan-Médoc, citée en exemple par le brief
- [[Postvention]] : nommé dans le cours, sans définition
- [[Preuve de concept]] : nommé dans le cours, sans définition
- [[Prévention primaire, secondaire et tertiaire]] : nommé dans le cours, sans définition
- [[Qualité de vie au travail]] : nommé dans le cours, sans définition
- [[Risques psychosociaux]] : nommé dans le cours, sans définition
- [[Santé au travail]] : nommé dans le cours, sans définition

**Year 3 - SHS**

- [[Anthropomorphisme]] : voitures dotées de visages ou de caractère, relevé dans deux textes de lecture sur l'automobile
- [[Caractérologie des véhicules]] : selon Boltanski, la forme de la voiture reflète la caractérologie sociale du conducteur
- [[Concurrence pour l'espace]] : selon Boltanski, la rareté de l'espace de circulation remplace celle des véhicules
- [[Corps projectile]] : expression de Paul Virilio, la voiture comme corps projectile dont s'équipe le sujet autonome
- [[Cyborg]] : nommé dans le cours, sans définition
- [[Design fiction]] : créer un artefact du futur, objet tangible, livrable possible du cours sur l'imaginaire automobile
- [[Ethos de classe]] : nommé dans le cours, sans définition
- [[Extension du schéma corporel]] : selon Boltanski, l'automobile prolonge le corps au-delà de ses frontières biologiques
- [[Fantastique (Todorov)]] : nommé dans le cours, sans définition
- [[Futurisme]] : manifeste de Marinetti (1909), qui préfère la voiture de course à la Victoire de Samothrace
- [[Histoire visuelle]] : identifier des sources visuelles et narratives sur la façon dont le passé imaginait le futur
- [[Moi blindé]] : image de Meyer-Drawe, la voiture reflète les rêves de corps de l'humain
- [[Paréidolie]] : voir des visages dans des objets, comme sur l'avant des voitures
- [[Voiture autonome]] : selon Kröger, son histoire est autant une histoire d'images que de techniques

**Year 3 - Statistics**

- [[Convergence en probabilité]] : estimateur consistant en moyenne quadratique ou en probabilité
- [[Diagramme en barres et diagramme circulaire]] : graphiques des données catégorielles, opposés à l'histogramme
- [[Diagramme en points]] : nommé dans le cours, sans définition
- [[Fréquence relative]] : nombre d'occurrences divisé par la taille de l'échantillon
- [[Loi des valeurs extrêmes]] : exemple de loi à paramètres de position et d'échelle, sans étude propre
- [[Paramètre de position et d'échelle]] : paramètres dont dépend la fonction de répartition par $(x - \theta_1)/\theta_2$
- [[Stabilité des lois par somme]] : loi de la somme de variables aléatoires indépendantes, pour quelques familles de lois
- [[Tirage avec et sans remise]] : le vrai tirage aléatoire est avec remise, presque équivalent sans remise en pratique
- [[Transformation puissance]] : famille $Y = (X^p - 1)/p$ pour $p > 0$, et $Y = \ln X$ pour $p = 0$
- [[Étendue (statistique)]] : mesure de dispersion la plus simple, max moins min
- [[Évaluation critique d'une étude statistique]] : liste des pièges à repérer dans une étude statistique, comme l'échantillon biaisé

**Year 3 - Sémiotique**

- [[Analyse de corpus]] : analyse d'un ensemble de documents collectés, sélectionnés et triés selon une problématique
- [[Assemblages préfabriqués]] : « petites formes » standardisées des interfaces, comme le menu hamburger ou la barre de recherche
- [[Corps communicant]] : tout ce que l'informatique permet en communication est ancré dans des postures corporelles
- [[Design centré vivant]] : thème 2026, pistes sémiotiques à partir des applications de reconnaissance de la nature
- [[Dispositif (communication)]] : « ensemble des substrats matériels de la communication », selon Jeanneret
- [[Désenfouissement du code]] : rendre visible le code des architextes qui formatent nos gestes numériques
- [[Efficacité symbolique]] : les dispositifs produisent une relation par une double proximité, corporelle et imaginaire
- [[Entrepreneur de soi]] : nommé dans le cours, sans définition
- [[Externalisation des facultés]] : les outils numériques externalisent nos facultés, stocker, retrouver et partager les connaissances
- [[Genre communicationnel]] : genres culturels convoqués par un écran, comme encyclopédie ou jeu, qui impliquent une posture
- [[Hypomnémata]] : selon Stiegler, supports techniques qui extériorisent la mémoire
- [[Images opératives]] : icônes, cartes, visualisations de données, images qui orientent l'action
- [[Impératif de productivité]] : les écrans rendent l'action nécessaire et instituent l'utilisateur en producteur de contenu
- [[Littératie numérique]] : nommé dans le cours, sans définition
- [[Logique du marché]] : choisir une application, c'est adhérer à un écosystème et s'inscrire dans une économie
- [[Machine textuelle]] : les dispositifs numériques transforment nos choix et pratiques en instructions techniques
- [[Médiation]] : selon Jeanneret, activité productive et créative qui intervient sur le cours de la communication
- [[Non-neutralité des objets techniques]] : selon Akrich, les objets techniques définissent une partition du monde physique et social
- [[Novlangue du digital]] : les mots du numérique ne sont jamais neutres, chacun porte une vision du monde
- [[Numérique comme écriture]] : l'informatique de communication repose sur des processus de lecture et d'écriture
- [[Quatre cadres de l'écrit d'écran]] : selon Marc Jahjah, l'écriture à l'écran est enchâssée dans quatre cadres
- [[Saillance et normalisation]] : continuum du rapport au corps, entre émergence de pratiques nouvelles et leur effacement routinier
- [[Savoirs situés]] : nommé dans le cours, sans définition
- [[Sémiologie]] : explique comment le signe fonctionne dans un système de communication, opposée à la sémiotique
- [[Techniques du corps]] : selon Mauss, façons dont les hommes, société par société, savent se servir de leur corps
- [[Temps des écrans]] : trois temps des écrans, dont le temps informatique mesuré et prédictible
- [[Traces numériques]] : clics, recherches, likes et partages, qui construisent un profil de l'utilisateur
- [[Travail invisible des utilisateurs]] : les corps deviennent des lieux de production d'attention et de données
- [[Économie des données]] : la plateforme collecte, profile, classifie, prédit et monétise ce que fait l'utilisateur

**Year 3 - Séries**

- [[Comparaison série-intégrale]] : pour f continue, positive et décroissante, série et intégrale ont la même nature
- [[Condition nécessaire de convergence]] : si $\sum a_n$ converge, alors $a_n \to 0$, la réciproque étant fausse
- [[Convergence conditionnelle]] : série convergente sans être absolument convergente, comme la série harmonique alternée
- [[Critère de comparaison]] : pour des séries positives, la convergence de la plus grande entraîne celle de la plus petite
- [[Critère des séries alternées]] : $\sum (-1)^n b_n$ converge si $(b_n)$ décroît vers 0
- [[Fonction continue par morceaux]] : continue sur un nombre fini de morceaux, avec des limites finies aux bornes
- [[Fonction périodique]] : f est 2π-périodique si $f(x + 2\pi) = f(x)$ pour tout x
- [[Interversion de limites]] : échanges de limites, d'intégrales ou de dérivées sous convergence uniforme
- [[Point limite]] : point dont tout voisinage $]a - \epsilon, a + \epsilon[$ rencontre X
- [[Reste d'une série]] : $R_n = S - S_n$, somme des termes après le rang n, qui tend vers 0
- [[Reste de Taylor]] : $R_n = f - T_n$, f étant somme de sa série de Taylor si $R_n \to 0$

**Year 3 - ligue football**

- [[Association ternaire]] : association entre trois entités, comme le sponsoring entre Équipe, Sponsor et Saison
- [[Clé auto-incrémentée]] : nommé dans le cours, sans définition
- [[Contrainte d'intégrité]] : règles que la base impose aux données, comme CHECK dans le DDL du projet
- [[Diagramme de Gantt]] : nommé dans le cours, sans définition
- [[Expression CASE]] : nommé dans le cours, sans définition
- [[Fonction d'agrégation]] : fonctions comme SUM, utilisées avec GROUP BY pour les requêtes d'agrégats
- [[Jointure externe]] : nommé dans le cours, sans définition
- [[ODBC et JDBC]] : nommé dans le cours, sans définition
- [[PostgreSQL]] : nommé dans le cours, sans définition
- [[Sous-requête]] : requête imbriquée dans une autre, imposée par le sujet database

**Year 3 - workshop**

- [[Circulatique]] : art de penser les flux humains, notion reprise par les étudiants d'un site professionnel
- [[Classification de Strahler]] : hiérarchisation des réseaux hydrographiques par Arthur Newell Strahler
- [[Coworking]] : organisation du travail autour d'un espace partagé, selon le dossier étudiant ReYOU
- [[Salon professionnel]] : foire qui réunit en un lieu l'offre et la demande d'un secteur, exposants et visiteurs
- [[Top of mind]] : terme du dossier étudiant ReYOU, chaque visiteur ayant un « top of mind » selon son profil
- [[Éco-organisme]] : structure souvent liée à l'État qui organise la fin de vie des déchets, selon les étudiants

**Year 4 - C++**

- [[Allocation dynamique]] : malloc réserve des octets sur le tas et renvoie un pointeur vers la zone
- [[Arithmétique des pointeurs]] : ajouter 1 à une adresse la décale de la taille du type pointé
- [[Complément à deux]] : nommé dans le cours, sans définition
- [[Erreur de compilation]] : messages types du compilateur et leurs causes, comme le point-virgule oublié
- [[Erreur de segmentation]] : nommé dans le cours, sans définition
- [[Fonctions printf et scanf]] : printf affiche, scanf lit, avec des séquences de contrôle commençant par %
- [[Instruction vide]] : un ; juste après if ou while termine l'instruction, piège classique du cours
- [[Langage C]] : objet réel des trois chapitres de la matière C++, mots réservés, printf, scanf et malloc
- [[Mot réservé]] : mots prédéfinis du C, qu'on ne peut pas réutiliser comme identifiants
- [[Norme IEEE 754]] : norme appliquée pour lire des octets comme un float, en séparant signe, exposant et mantisse
- [[Notation hexadécimale]] : écriture des adresses mémoire avec le préfixe 0x, un octet sur deux chiffres
- [[Opérateur flèche]] : accès au champ d'une structure par un pointeur, p->valeur équivalant à (*p).valeur
- [[Passage par valeur]] : en C, les arguments d'une fonction sont passés par copie
- [[Pointeur NULL]] : pointeur du dernier élément d'une liste chaînée, ou premier pointeur d'une liste vide
- [[Typage statique]] : en C, toutes les vérifications de type sont faites à la compilation
- [[Variable non initialisée]] : en C, sa lecture affiche une « valeur aléatoire » selon le cours

**Year 4 - Culture du vivant**

- [[Dimension politique du design]] : « tout design est politique », se demander à qui il profite et qui est exploité
- [[IA générative]] : IA probabiliste qui devine le mot suivant, avec un risque d'hallucination
- [[IA sémantique]] : nommé dans le cours, sans définition
- [[Main invisible]] : idée d'Adam Smith, l'égoïsme individuel génère la prospérité collective
- [[World Wide Web]] : inventé par Tim Berners-Lee, anarchiste à l'origine puis devenu capitaliste selon les notes

**Year 4 - Gestion financière**

- [[Balance commerciale]] : importations et exportations de produits, seule explication de la note
- [[Balance des paiements]] : l'argent qui entre et l'argent qui sort, seule explication de la note
- [[Coût et prix]] : somme nécessaire pour obtenir quelque chose, et somme à payer pour l'acquérir
- [[Marché financier]] : nommé dans le cours, sans définition
- [[Opérations de haut de bilan]] : nommé dans le cours, sans définition
- [[Produit intérieur brut]] : PIB, qui a remplacé le PNB et compte aussi les entreprises étrangères en France
- [[Tableau économique d'ensemble]] : nommé dans le cours, sans définition
- [[Types de banque]] : nommé dans le cours, sans définition

**Year 4 - SHS**

- [[Copyleft]] : nommé dans le cours, sans définition
- [[Creative Commons]] : nommé dans le cours, sans définition
- [[Demande de fusion]] : pull request, façon de proposer une modification au dépôt d'un autre sur GitHub
- [[Design contributif]] : design où une communauté façonne collectivement la forme finale de l'objet
- [[Design des règles]] : dans OpenFisca, design de l'information dicté par la loi, en stricte conformité au droit
- [[Dictature bienveillante]] : direction artistique verticale acceptée par la communauté pour qu'un objet soit utilisable
- [[Fichier README]] : « un fondamental » selon une étudiante interrogée, écrit pour les autres et non pour soi
- [[Financement participatif]] : financement communautaire, qui a libéré Blender, et sa forme conditionnelle chez Poly Haven
- [[Freemium]] : modèle qui garde les vrais fichiers de design derrière un mur payant, chez Figma ou Blush
- [[Git]] : contrôle de version décentralisé de Linus Torvalds (2005), présenté comme innovation de procédé
- [[Gouvernance par l'expertise]] : contribuer aux communs exige des compétences techniques, d'où une « oligarchie de l'expertise »
- [[Hallucination (IA)]] : risque de l'IA générative probabiliste, intolérable pour calculer un impôt ou le RSA
- [[IA slop]] : projets bâclés produits par l'IA, terme employé par l'étudiante interrogée
- [[Intérêt général]] : nommé dans le cours, sans définition
- [[Licence anti-IA]] : licences restrictives imaginées pour protéger les communs du pillage par l'IA générative
- [[Produit d'appel]] : service gratuit d'entreprise privée sans gouvernance communautaire, comme Google Fonts ou Behance
- [[Écosystème fermé]] : dépendance aux outils d'une grande entreprise, que l'interviewée refuse au profit de la communauté

**Year 4 - culture du soin**

- [[Charge cognitive]] : nommé dans le cours, sans définition
- [[Conception centrée sur l'humain]] : approche de conception qui demande « que vit la personne ? », besoins, usages, perception
- [[Defuturing]] : nommé dans le cours, sans définition
- [[Dispositif de normalisation]] : lecture foucaldienne du design, le pouvoir organise, règle et normalise les conduites
- [[Fonctionnalisme]] : approche qui demande « que fait l'objet ? », fonction, efficacité, robustesse, performance
- [[Ouverture d'un monde (Heidegger)]] : quelles possibilités d'agir et d'exister un objet ou un espace ouvre-t-il, ou ferme-t-il
- [[Responsabilité élargie du designer]] : soutenabilité allant du choix de conception à ses conséquences écologiques, sociales et intergénérationnelles
- [[Structuration de l'expérience (Merleau-Ponty)]] : comment le monde configuré par le design est vécu dans le corps
- [[Vulnérabilité]] : voir les vulnérabilités, y compris celles que les dispositifs produisent

**Year 4 - data mining**

- [[Algorithme C4.5]] : algorithme d'arbre de décision descendant d'ID3, avec variables continues et normalisation du gain
- [[Algorithme CART]] : Classification and Regression Tree (1984), arbre de décision binaire
- [[Algorithme ID3]] : construction récursive d'un arbre de décision, choisissant à chaque nœud le test de plus grand gain
- [[Bagging]] : méthode d'ensemble qui apprend des modèles sur des échantillons tirés avec remise
- [[Boosting]] : méthode d'ensemble à exemples pondérés et modèles construits l'un après l'autre, comme AdaBoost.M1
- [[Centroïde]] : exemple synthétique dont chaque attribut est la moyenne des valeurs de l'ensemble
- [[Classification hiérarchique ascendante]] : clustering qui part d'un groupe par exemple et fusionne jusqu'à n'en avoir qu'un
- [[Classifieur]] : fonction qui prend des caractéristiques en entrée et attribue une classe discrète
- [[Clustering]] : partitionner des exemples sans étiquette en k groupes de données semblables
- [[Ensemble d'entraînement et de test]] : erreur d'un classifieur, taux de réussite, et erreur d'entraînement ou de test
- [[Entropie (théorie de l'information)]] : quantité d'information $\log_2(N/n)$, et entropie d'une partition
- [[F-mesure]] : nommé dans le cours, sans définition
- [[Forêt aléatoire]] : bagging d'arbres de décision, tirant à chaque nœud q variables parmi p
- [[Fouille de données]] : découverte de connaissances dans les données, « comment faire parler les données ? »
- [[Gain d'information]] : critère de choix du test dans ID3, baisse d'entropie apportée par un test
- [[Indice de Gini]] : critère d'impureté d'un nœud utilisé par CART, $1 - \sum p_i^2$
- [[Inertie (clustering)]] : moyenne des carrés des distances au centroïde, intra-classe et inter-classe
- [[K plus proches voisins]] : classer un point selon les classes de ses k voisins
- [[Machine à vecteurs de support]] : nommé dans le cours, sans définition
- [[Méthode de Ward]] : fusionner les deux groupes qui font perdre le moins d'inertie intra-classe
- [[Prétraitement des données]] : étape du data mining qui suit la sélection et l'exploration des données
- [[Rapport de gain]] : normalisation du gain d'information dans C4.5, par le SplitInfo
- [[Règle d'association]] : nommé dans le cours, sans définition
- [[Réseau de neurones]] : nommé dans le cours, sans définition
- [[Série temporelle]] : nommé dans le cours, sans définition
- [[Valeur manquante]] : valeurs nettoyées au prétraitement, et traitées à part par l'algorithme C4.5
- [[Variable cible et variable explicative]] : variables explicatives obtenues par observation, variable cible à prédire
- [[Élagage]] : dans CART, élaguer l'arbre entier successivement puis garder le meilleur arbre élagué

**Year 4 - graph theory**

- [[Algorithme de Kruskal]] : algorithme glouton d'arbre couvrant minimal, ajoutant la plus petite arête sans cycle
- [[Algorithme de Tarjan]] : calcule les composantes fortement connexes, cité sans description de l'algorithme
- [[Chaîne (graphe)]] : suite alternant sommets et arêtes dans un graphe non orienté, de longueur p
- [[Composante fortement connexe]] : sous-graphe orienté maximal où deux sommets sont toujours reliés dans les deux sens
- [[Degré d'un sommet]] : nombre d'arêtes incidentes à un sommet
- [[Dictionnaire (Python)]] : structure Python d'associations clé-valeur, accessibles par la clé
- [[Forêt (graphe)]] : graphe non orienté sans cycle, dont chaque composante connexe est un arbre
- [[Graphe biparti]] : graphe dont chaque arête relie les deux parties d'une partition des sommets
- [[Graphe complet]] : graphe simple où toute paire de sommets est adjacente
- [[Graphe connexe]] : graphe où deux sommets quelconques sont reliés par une chaîne
- [[Graphe planaire]] : graphe que l'on peut dessiner sans croisement d'arêtes
- [[Graphe pondéré]] : graphe muni d'une fonction de poids sur les arêtes
- [[Graphe régulier]] : graphe k-régulier, dont tout sommet est de degré k
- [[Graphe simple]] : graphe sans boucle ni arête multiple
- [[Graphe sous-jacent]] : graphe simple obtenu en supprimant boucles et arêtes multiples
- [[Isomorphisme de graphes]] : couple de bijections sur sommets et arêtes qui respecte les extrémités
- [[Matrice d'adjacence]] : matrice dont le coefficient i, j est le nombre d'arêtes entre deux sommets
- [[Parcours en largeur]] : parcours d'un graphe à l'aide d'une file, sommets marqués à leur entrée
- [[Parcours en profondeur]] : parcours récursif, marquer et afficher le sommet puis visiter chaque fils non visité
- [[Pont (graphe)]] : arête dont la suppression ajoute une composante connexe au graphe
- [[Recherche séquentielle]] : parcourir le tableau élément par élément, en $O(n)$ au pire cas
- [[Sommet et arête]] : vocabulaire de base, sommets adjacents, sommet isolé, boucle
- [[Tri par insertion]] : nommé dans le cours, sans définition
- [[Tri par sélection]] : algorithme de tri en $O(n^2)$ au pire cas
- [[Union-Find]] : structure de l'implémentation de Kruskal, find_parent cherchant récursivement la racine d'un sommet

**Year 4 - management de l'innovationb**

- [[Analyse fonctionnelle]] : nommé dans le cours, sans définition
- [[Buy now pay later]] : paiement en plusieurs fois sans frais, exemple d'innovation de business model
- [[Entreprise sans usine]] : « fabless », innovation d'organisation où la production est sous-traitée
- [[Innovation de rupture]] : nommé dans le cours, sans définition
- [[Partie prenante]] : acteurs avec qui travaille la méthode, utilisateurs, distributeurs, société, fournisseurs
- [[Tuile vectorielle]] : innovation de procédé, charger seulement les petites tuiles vectorielles de la zone affichée

**Year 4 - projet court**

- [[Charge mentale]] : nommé dans le cours, sans définition
- [[Masculinité hégémonique]] : nommé dans le cours, sans définition
- [[Mentorat]] : programme d'accompagnement comme « Tech pour toutes », six mois, gratuit et à distance
- [[Parité femmes-hommes]] : la loi du 2 mars 2022 impose dès 2024 la parité dans les instances dirigeantes du sport
- [[Sexisme ordinaire]] : identité des dirigeantes ramenée à leur corps plutôt qu'à leur fonction, selon Barbusse
- [[Tokénisme]] : concept de Kanter (1977), un groupe minoritaire sous 15 à 20 % altère la dynamique

**Autres**

- [[Linéarisation trigonométrique]] : nommé dans le cours, sans définition
- [[Nombre d'Armstrong]] : nommé dans le cours, sans définition
- [[Nombre parfait]] : nommé dans le cours, sans définition
- [[Opérateurs de recherche booléens]] : opérateurs AND, OR et autres présentés par la BU pour une recherche Google
- [[Transistor]] : nommé dans le cours, sans définition

## Résumés de sources (223)

### Documents PDF et PPTX (59)

- **Year 1, Algo Maths** : [[AlgoID1 (résumé)]]
- **Year 1, Analyse Maths** : [[AnalyseID1 (résumé)]], [[Chap0-Rappels-etc (résumé)]], [[Chap1-reels (résumé)]], [[TD0-Rappel (résumé)]], [[td0slides (résumé)]], [[TD1-numbres-reels (résumé)]], [[td1slides (résumé)]], [[TDSuites (résumé)]], [[TD5-AnalAsympt (résumé)]], [[TD5-AnalyseAsymptotiqueCorrection (1) (résumé)]], [[DS1-Analyse-2022-corrigé (résumé)]], [[DS1-correction-2021 (résumé)]]
- **Year 1, contrôles** : [[Contrôles (résumé)]]
- **Year 1, Outil Maths** : [[Chapitre2-Ensemble (4) (résumé)]], [[Chapitre3-Relation binaire (résumé)]], [[Chapitre4-Fonctions (1) (résumé)]], [[CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022 (résumé)]], [[Exo-Chapitre 2 (résumé)]], [[Exo_Chapitre1_Logique (résumé)]], [[TD4Applications (résumé)]], [[TD4Applications-Solutions (résumé)]], [[TDEnsembles (1) (résumé)]], [[TDRelations (résumé)]]
- **Year 2, Algo** : [[ARBRE AVL (résumé)]], [[Chapitre3-Arbres (résumé)]], [[Chapitre4-Preing2ID (résumé)]], [[Chapitre5-ABR (résumé)]], [[Projet-Arbre-AVL-ID2 (résumé)]]
- **Year 2, Analyse** : [[Chp9-intégrales multiples (résumé)]], [[TD7-integration (1) (résumé)]]
- **Year 2, Operating System** : [[OS - chp 4 (résumé)]], [[Copy of TP2-Commands (résumé)]], [[TP3-Commands (2) (résumé)]], [[TP4-Unix Commands (résumé)]], [[TP5-AWK Command (résumé)]], [[TP6-Assignment (résumé)]]
- **Year 2, Projet Design** : [[Projet Etudiants CYDesign 2025 (résumé)]]
- **Year 2, SHS** : [[Ethnographie visuelle (résumé)]]
- **Year 3, Affordance** : [[Présentation Tests Utilisateurs ID3 (résumé)]], [[UX Research - Observation - 2026 (résumé)]]
- **Year 3, Computer Network** : [[02 IP Addressing (résumé)]]
- **Year 3, Culture du vivant** : [[VIVANT1 DBrowaeys (résumé)]]
- **Year 3, ligue football** : [[sujet database (résumé)]], [[Rapport du projet Ligue Football (résumé)]]
- **Year 3, Projet courts** : [[Santé au travail - brief du projet (résumé)]], [[Santé au travail - fiche ressources (résumé)]]
- **Year 3, SHS** : [[imaginaire_automobile_futur_smaller (résumé)]], [[TD_preparation_entretiens25.9.25 (résumé)]], [[text1 (résumé)]], [[text2 (résumé)]], [[text3 (résumé)]]
- **Year 3, Sémiotique** : [[Séance 1 (PPTX) (résumé)]], [[Séance 2 (PPTX) (résumé)]], [[Séance 3 (PPTX) (résumé)]], [[Séance 4 (PPTX) (résumé)]]
- **Year 4, culture du soin** : [[Culture du soin Seance 1 (résumé)]]
- **Year 4, data mining** : [[séance data mining du prof (résumé)]]
- **Year 4, management de l'innovation** : [[CY école de design 4e - Management de l'innovation - 2026 09 30 (résumé)]]

Classés par matière. Le nombre entre parenthèses est celui des points à vérifier, pour les premières matières intégrées. Pour les autres, chaque résumé les liste, et la page de matière donne les priorités.

### Autres matières de Year 1

- **Algo Maths** : [[Séance 1 - Algo Maths (résumé)|Cours 1]], [[Python (résumé)]], [[explications DM d'algo (résumé)]]
- **Communication orale** : [[Communication orale - discours (résumé)]], [[Debats (résumé)]]
- **Corps à l'oeuvre** : [[corps à l'oeuvre - séance (résumé)]]
- **Dessein au cube** : [[Compte rendu (résumé)]], [[Inégalités alimentaires (résumé)]], [[Pistes entrevue (résumé)]], [[Synthèse (résumé)]], [[Untitled document (résumé)]], [[retranscription (résumé)]]
- **HDA** : [[Séance HDA (résumé)]]
- **Outil Maths** : [[Chapitre 1 logique (résumé)]], [[Chapitre 2 ensembles (résumé)]], [[Chapitre 3 - Relation binaire (résumé)]], [[Chapitre 5 - Complexes (résumé)]]
- **Peinture** : [[Séance 1 - Peinture (résumé)|Cours 1]], [[Séance 2 (résumé)]], [[Séance 3 (résumé)]]
- **Philosophie** : [[L'état (résumé)]], [[liberté et moralité (résumé)]]
- **Projet design** : [[Informations villeneuve (Brief Intro) (résumé)]], [[Prise parole Rendu final (résumé)]], [[Projet BLR (résumé)]], [[Topo ELBA (résumé)]], [[exposé melvita (résumé)]], [[idées solutions (résumé)]]

### Autres matières de Year 2

- **Algo** : [[AVL momo (résumé)]], [[Chp1 - récursivité et complexité (résumé)]], [[TD_Algo (résumé)]], [[chp2 - piles listes file (résumé)]], [[qui dit quoi AVL (résumé)]]
- **Anglais** : [[Global Exam Vocab (résumé)]], [[stars.html (résumé)]], [[world in 2075 (résumé)]]
- **Corps à l'oeuvre** : [[Dernière séance (résumé)]]
- **Operating System** : [[Commandes Shell + explications (résumé)]], [[Copy of 08 Processes-TP (résumé)]], [[Séance TP2 (résumé)]], [[Séance TP3 (résumé)]], [[Séance TP4 (résumé)]], [[Séance TP5 (résumé)]], [[DM Shell Scripting (résumé)]], [[OS - chp 1 (résumé)]], [[OS - chp 2 (résumé)]], [[OS - chp 3 (résumé)]], [[OS - chp 5 (résumé)]], [[OS - chp7 (résumé)]], [[Operating Systems - Semester report (résumé)]], [[TP1 (résumé)]], [[TP2 (résumé)]], [[TP3 (résumé)]], [[TP4 (résumé)]], [[TP5 (résumé)]], [[UNIX Commands - Semester report (résumé)]], [[séance TP1 (résumé)]], [[log (résumé)]]
- **Philosophie** : [[philo 1 (résumé)]], [[philo 2 (résumé)]], [[philo 3 (résumé)]], [[philo 4 (résumé)]], [[philo 5 (résumé)]]
- **Probability** : [[Chp 1 - Sample space,events, proba (résumé)]], [[Chp 2 - Conditional proba and independence (résumé)]], [[Chp 3 - Combinatorics (résumé)]], [[Chp 3 - Important discrete distributions (résumé)]], [[Chp 4 - Discrete random variables (résumé)]], [[Chp 5 - Continuous random variable (résumé)]], [[Chp 6 - Joint probability distributions (résumé)]]
- **Projet Design** : [[EDOSSAH (résumé)]], [[Helloartup (résumé)]], [[Qui dit quoi (résumé)]]
- **écriture narrative** : [[écriture narrative (résumé)]]

### Year 3

- **Hors matière** : [[Séance BU - Savoir rechercher sur Google (résumé)]]
- **Computer Network** : [[Chp2 - Static Routing (résumé)]], [[Chp3 - Dynamic Routing (résumé)]], [[Chp4 - VLAN ／ IVR Commands (résumé)]], [[Chp5 - NAT ／ PAT (résumé)]], [[Formation CISCO Packet Tracer (résumé)]], [[chp1 - Computer Networks (résumé)]], [[chp6 - Access Control List (résumé)]]
- **Culture du vivant** : [[Culture Vivant SÉANCE 2 EXPLICATION (résumé)]], [[Culture du vivant (résumé)]], [[Culture du vivant Dernière séance (résumé)]]
- **Data analysis** : [[Séance 1 - Data analysis (Thanos) (résumé)|Cours 1]], [[Séance 2 - Introduction statistics (résumé)]], [[Séance 3 - Paradoxe de Simpson (résumé)]], [[Séance 4 - Estimation (résumé)]], [[Séance 5 - Hypothesis Testing (résumé)]], [[Séance 6 - T-Test (résumé)]], [[Séance 7 - Z-Test (résumé)]], [[Séance 8 - Chi²-Test (résumé)]], [[Séance 9 - Covariance and Correlation (résumé)]], [[Séance 10 - linear regression (résumé)]], [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]], [[Séance 12 - ANOVA and F-statistic (résumé)]], [[Séance 13 - Principal Components Analysis (résumé)]], [[Séance 13 - PCA in R (résumé)]], [[Summary functions in RStudio (résumé)]]
- **Data base** : [[Séances 1 et 2 - Database (résumé)]], [[Séance 3 - opérateurs et SQL (résumé)]]
- **IA** : [[Séance 1 - IA (résumé)|Cours 1]]
- **Java** : [[Chp1 - Intro Java (résumé)]]
- **SHS** : [[Synthese SHS GPT (résumé)]], [[Synthèse des entretiens (résumé)]], [[Transcriptions des entretiens (résumé)]]
- **Statistics** : [[Chp1 - Intro to statistics (résumé)]], [[Chp2 - Descriptive statistics (résumé)]], [[Chp3 - More on probability (résumé)]], [[Chp4 Part 1 - Inferential statistics (résumé)]], [[Chp4 Part2 - Inferential statistics (résumé)]], [[Chp4 Part3 - Inferential statistics (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
- **Séries** : [[Chp0 - Revision chapter (résumé)]], [[Chp1 - Convergent, divergent and positive terms SERIES (résumé)]], [[Chp2 - Alternating and absolutly convergent series (résumé)]], [[Chp3 - Sequence of function (résumé)]], [[Chp4 - Series of functions (résumé)]], [[Chp5 - power series (résumé)]], [[Chp6 - Fourier Series (résumé)]]
- **ligue football** : [[readme (résumé)]]
- **workshop** : [[Reyou (résumé)]]

### Year 4

- **Gestion financière** : [[Gestion financière (résumé)]]
- **C++** : [[Chp1 - basiques (résumé)]], [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]], [[chp2 - structures code (résumé)]]
- **Culture du vivant** : [[Culture du vivant - prise de note (résumé)]]
- **SHS** : [[Prise de note SHS (résumé)]], [[Recherches SHS (résumé)]], [[Entretien sur l'open source (résumé)]]
- **data mining** : [[Chp1 - intro to data mining (résumé)]]
- **graph theory** : [[Chp 1 - Undirected graph (résumé)]], [[Chp2 - tree (résumé)]], [[Graph - Python (résumé)]], [[chp3 - complexité (résumé)]], [[chp4 - oriented graphs (résumé)]]
- **management de l'innovation** : [[Analyse d'innovations (résumé)]], [[Douze innovations (résumé)]]
- **projet court** : [[recherches femmes et foot (résumé)]]

### Year 1 - Analyse Maths

- [[Chp4 - dérivabilité (résumé)]] : dérivation, classe $\mathcal{C}^n$, Rolle, accroissements finis (4)
- [[chp5 - Analyse Maths (résumé)|chp5 (résumé, Analyse)]] : équivalents et développements limités (4)

### Year 2 - Analyse

- [[Chap7-Integration (résumé)]] : le cours d'intégration (2)
- [[démonstrations - integration (résumé)]] : les preuves du cours (5)
- [[Intégration UTILITAIRE (résumé)]] : fiche pratique (0)

### Year 1 - Algèbre Linéaire

- [[chp1 (résumé)|chp1 (résumé)]] : espaces vectoriels, familles, bases (2)
- [[chp2 (résumé)|chp2 (résumé)]] : applications linéaires, morphismes, rang (4)
- [[chp3 (résumé)|chp3 (résumé)]] : pivot de Gauss, systèmes (3)
- [[chp4 (résumé)|chp4 (résumé)]] : matrices, matrice d'une application (2)
- [[chp5 - Algèbre linéaire (résumé)|chp5 (résumé)]] : changement de base, déterminant (2)
- [[chp6 (résumé)|chp6 (résumé)]] : déterminant, caractérisation des bases (3)
- [[chp7 (résumé)|chp7 (résumé)]] : éléments propres, somme directe (2)

### Year 2 - Analyse dans Rn

- [[Chp 2 - éléments de topologie dans Rn (résumé)]] : normes, boules, ouverts, intérieur et adhérence (5)
- [[Chp 3 - Limite et continuité d’applications (résumé)]] : limites, continuité, applications lipschitziennes (5)
- [[Chp 4 - Calcul différentiel du premier ordre (résumé)]] : différentielle, gradient, EDP d'ordre 1, difféomorphismes (6)
- [[Chp 5 - Calcul différentiel d'ordre supérieur (résumé)]] : classe $\mathcal{C}^k$, Schwarz, systèmes et EDP d'ordre 2 (3)

### Year 2 - Bilinear Algebra

- [[Chp 0a - Linear combination (résumé)]] : systèmes, Span, indépendance, transformations (4)
- [[Chp 0b - Matrix algebra (résumé)]] : produit, transposée, inverse (1)
- [[Chp 0c - Determinants (résumé)]] : déterminant, Cramer, formule de l'inverse (1)
- [[Chp 0d - Vector Space (résumé)]] : sous-espaces, base, dimension, rang (1)
- [[Chp 0e - Eigenvalues and eigenvectors (résumé)]] : valeurs propres, diagonalisation (3)
- [[chp 1 - Orthogonality (résumé)]] : projection orthogonale, Gram-Schmidt, QR et moindres carrés (5)
- [[Chp2 - Symmetric matrices and quadratic forms (résumé)]] : théorème spectral, formes quadratiques, SVD (5)
- [[Invertible matrix theorem (résumé)]] : les 20 énoncés équivalents (0)

## Matières (41)

Chaque matière a son dossier `Matières/<Matière>/`, qui contient sa carte `<Matière> (matière)` et ses résumés. Une matière suivie sur plusieurs années a une seule carte, avec une section par année.

- **Year 1** : [[Algèbre linéaire (matière)]], [[Algo Maths (matière)]], [[Analyse Maths (matière)]], [[Communication orale (matière)]], [[Corps à l'oeuvre (matière)]] (aussi Year 2), [[Dessein au cube (matière)]], [[HDA (matière)]], [[Outil Maths (matière)]], [[Peinture (matière)]], [[Philosophie (matière)]] (aussi Year 2), [[Projet design (Year 1) (matière)]], [[Contrôles (résumé)]] (sans carte)
- **Year 2** : [[Algo (matière)]], [[Analyse (matière)]], [[Analyse dans Rn (matière)]], [[Anglais (matière)]], [[Bilinear Algebra (matière)]], [[Écriture narrative (matière)]], [[Operating System (matière)]], [[Probability (matière)]], [[Projet design (Year 2) (matière)]], [[SHS (matière)]] (aussi Year 3 et 4)
- **Year 3** : [[Affordance (matière)]], [[Computer Network (matière)]], [[Culture du vivant (matière)]] (aussi Year 4), [[Data analysis (Thanos) (matière)]], [[Data base (matière)]], [[IA (matière)]], [[Java (matière)]], [[Ligue football (matière)]], [[Projet courts (Year 3) (matière)]], [[Sémiotique (matière)]], [[Séries (matière)]], [[Statistics (matière)]], [[Workshop (matière)]], [[Séance BU - Savoir rechercher sur Google (résumé)]] (sans carte)
- **Year 4** : [[C++ (matière)]], [[Culture du soin (matière)]], [[Data mining (matière)]], [[Gestion financière (matière)]], [[Graph theory (matière)]], [[Management de l'innovation (matière)]], [[Projet court (Year 4) (matière)]]

Matières connues par leurs seuls documents PDF ou PPTX : [[Affordance (matière)]], [[Projet courts (Year 3) (matière)]], [[Sémiotique (matière)]], [[Culture du soin (matière)]], et la partie Year 2 de [[SHS (matière)]].

## Synthèses (0)

Aucune pour l'instant.

## Sources disponibles

Notes présentes dans `Cours/` (163), par matière. Le nombre entre parenthèses est le nombre de notes.

### Year 1

Algo Maths (3), Algèbre Linéaire (7), Analyse Maths (2), Communication orale (2), Corps à l'oeuvre (1), Dessein au cube (7), HDA (1), Outil Maths (4), Peinture (3), Philosophie (2), Projet design (6)

### Year 2

Algo (5), Analyse (3), Analyse dans Rn (4), Anglais (3), Bilinear Algebra (8), Corps à l'oeuvre (1), Operating System (21), Philosophie (5), Probability (7), Projet Design (4), écriture narrative (1)

### Year 3

Computer Network (7), Culture du vivant (3), Data analysis (Thanos) (15), Data base (2), IA (1), Java (1), SHS (3), Statistics (7), Séries (7), ligue football (1), workshop (1), plus 1 note à la racine de `Year 3`

### Year 4

C++ (3), Culture du vivant (1), SHS (3), data mining (1), graph theory (5), management de l'innovationb (2), projet court (1), plus 1 note à la racine de `Year 4` (Gestion financière)
