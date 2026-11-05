# Index du wiki

Catalogue de toutes les pages du wiki. À lire en premier pour répondre à une question.

État au 2026-11-05 : 186 concepts, 163 résumés, 40 matières, aucune synthèse. Toutes les notes de `Cours/` sont intégrées. Les PDF et les PPTX ne le sont pas.

## Concepts (186)

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

## Résumés de sources (163)

Classés par matière. Le nombre entre parenthèses est celui des points à vérifier, pour les premières matières intégrées. Pour les autres, chaque résumé les liste, et la page de matière donne les priorités.

### Autres matières de Year 1

- **Algo Maths** : [[Sources/Year 1/Algo Maths/Cours 1 (résumé)|Cours 1]], [[Python (résumé)]], [[explications DM d'algo (résumé)]]
- **Communication orale** : [[Communication orale - discours (résumé)]], [[Debats (résumé)]]
- **Corps à l'oeuvre** : [[corps à l'oeuvre - cours (résumé)]]
- **Dessein au cube** : [[Compte rendu (résumé)]], [[Inégalités alimentaires (résumé)]], [[Pistes entrevue (résumé)]], [[Synthèse (résumé)]], [[Untitled document (résumé)]], [[retranscription (résumé)]]
- **HDA** : [[Cours HDA (résumé)]]
- **Outil Maths** : [[Chapitre 1 logique (résumé)]], [[Chapitre 2 ensembles (résumé)]], [[Chapitre 3 - Relation binaire (résumé)]], [[Chapitre 5 - Complexes (résumé)]]
- **Peinture** : [[Sources/Year 1/Peinture/Cours 1 (résumé)|Cours 1]], [[Cours 2 (résumé)]], [[Cours 3 (résumé)]]
- **Philosophie** : [[L'état (résumé)]], [[liberté et moralité (résumé)]]
- **Projet design** : [[Informations villeneuve (Brief Intro) (résumé)]], [[Prise parole Rendu final (résumé)]], [[Projet BLR (résumé)]], [[Topo ELBA (résumé)]], [[exposé melvita (résumé)]], [[idées solutions (résumé)]]

### Autres matières de Year 2

- **Algo** : [[AVL momo (résumé)]], [[Chp1 - récursivité et complexité (résumé)]], [[TD_Algo (résumé)]], [[chp2 - piles listes file (résumé)]], [[qui dit quoi AVL (résumé)]]
- **Anglais** : [[Global Exam Vocab (résumé)]], [[stars.html (résumé)]], [[world in 2075 (résumé)]]
- **Corps à l'oeuvre** : [[Dernier cours (résumé)]]
- **Operating System** : [[Commandes Shell + explications (résumé)]], [[Copy of 08 Processes-TP (résumé)]], [[Cours TP2 (résumé)]], [[Cours TP3 (résumé)]], [[Cours TP4 (résumé)]], [[Cours TP5 (résumé)]], [[DM Shell Scripting (résumé)]], [[OS - chp 1 (résumé)]], [[OS - chp 2 (résumé)]], [[OS - chp 3 (résumé)]], [[OS - chp 5 (résumé)]], [[OS - chp7 (résumé)]], [[Operating Systems - Semester report (résumé)]], [[TP1 (résumé)]], [[TP2 (résumé)]], [[TP3 (résumé)]], [[TP4 (résumé)]], [[TP5 (résumé)]], [[UNIX Commands - Semester report (résumé)]], [[cours TP1 (résumé)]], [[log (résumé)]]
- **Philosophie** : [[philo 1 (résumé)]], [[philo 2 (résumé)]], [[philo 3 (résumé)]], [[philo 4 (résumé)]], [[philo 5 (résumé)]]
- **Probability** : [[Chp 1 - Sample space,events, proba (résumé)]], [[Chp 2 - Conditional proba and independence (résumé)]], [[Chp 3 - Combinatorics (résumé)]], [[Chp 3 - Important discrete distributions (résumé)]], [[Chp 4 - Discrete random variables (résumé)]], [[Chp 5 - Continuous random variable (résumé)]], [[Chp 6 - Joint probability distributions (résumé)]]
- **Projet Design** : [[EDOSSAH (résumé)]], [[Helloartup (résumé)]], [[Qui dit quoi (résumé)]]
- **écriture narrative** : [[écriture narrative (résumé)]]

### Year 3

- **Hors matière** : [[Cours BU - Savoir rechercher sur Google (résumé)]]
- **Computer Network** : [[Chp2 - Static Routing (résumé)]], [[Chp3 - Dynamic Routing (résumé)]], [[Chp4 - VLAN ／ IVR Commands (résumé)]], [[Chp5 - NAT ／ PAT (résumé)]], [[Formation CISCO Packet Tracer (résumé)]], [[chp1 - Computer Networks (résumé)]], [[chp6 - Access Control List (résumé)]]
- **Culture du vivant** : [[Culture Vivant COURS 2 EXPLICATION (résumé)]], [[Culture du vivant (résumé)]], [[Culture du vivant Dernier cours (résumé)]]
- **Data analysis** : [[Sources/Year 3/Data analysis (Thanos)/Cours 1 (résumé)|Cours 1]], [[Cours 2 - Introduction statistics (résumé)]], [[Cours 3 - Paradoxe de Simpson (résumé)]], [[Cours 4 - Estimation (résumé)]], [[Cours 5 - Hypothesis Testing (résumé)]], [[Cours 6 - T-Test (résumé)]], [[Cours 7 - Z-Test (résumé)]], [[Cours 8 - Chi²-Test (résumé)]], [[Cours 9 - Covariance and Correlation (résumé)]], [[Cours 10 - linear regression (résumé)]], [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)]], [[Cours 12 - ANOVA and F-statistic (résumé)]], [[Cours 13 - Principal Components Analysis (résumé)]], [[Cours 13 - PCA in R (résumé)]], [[Summary functions in RStudio (résumé)]]
- **Data base** : [[Cours 1 et 2 - Database (résumé)]], [[Cours 3 - opérateurs et SQL (résumé)]]
- **IA** : [[Sources/Year 3/IA/Cours 1 (résumé)|Cours 1]]
- **Java** : [[Chp1 - Intro Java (résumé)]]
- **SHS** : [[Synthese SHS GPT (résumé)]], [[Synthèse des entretiens (résumé)]], [[Transcriptions des entretiens (résumé)]]
- **Statistics** : [[Chp1 - Intro to statistics (résumé)]], [[Chp2 - Descriptive statistics (résumé)]], [[Chp3 - More on probability (résumé)]], [[Chp4 Part 1 - Inferential statistics (résumé)]], [[Chp4 Part2 - Inferential statistics (résumé)]], [[Chp4 Part3 - Inferential statistics (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
- **Séries** : [[Chp0 - Revision chapter (résumé)]], [[Chp1 - Convergent, divergent and positive terms SERIES (résumé)]], [[Chp2 - Alternating and absolutly convergent series (résumé)]], [[Chp3 - Sequence of function (résumé)]], [[Chp4 - Series of functions (résumé)]], [[Chp5 - power series (résumé)]], [[Chp6 - Fourier Series (résumé)]]
- **ligue football** : [[readme (résumé)]]
- **workshop** : [[Reyou (résumé)]]

### Year 4

- **C++** : [[Chp1 - basiques (résumé)]], [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]], [[chp2 - structures code (résumé)]]
- **Culture du vivant** : [[Culture du vivant - prise de note (résumé)]]
- **SHS** : [[Prise de note SHS (résumé)]], [[Recherches SHS (résumé)]], [[Entretien sur l'open source (résumé)]]
- **data mining** : [[Chp1 - intro to data mining (résumé)]]
- **graph theory** : [[Chp 1 - Undirected graph (résumé)]], [[Chp2 - tree (résumé)]], [[Graph - Python (résumé)]], [[chp3 - complexité (résumé)]], [[chp4 - oriented graphs (résumé)]]
- **management de l'innovation** : [[Analyse d'innovations (résumé)]], [[Douze innovations (résumé)]]
- **projet court** : [[recherches femmes et foot (résumé)]]

### Year 1 - Analyse Maths

- [[Chp4 - dérivabilité (résumé)]] : dérivation, classe $\mathcal{C}^n$, Rolle, accroissements finis (4)
- [[Sources/Year 1/Analyse Maths/chp5 (résumé)|chp5 (résumé, Analyse)]] : équivalents et développements limités (4)

### Year 2 - Analyse

- [[Chap7-Integration (résumé)]] : le cours d'intégration (2)
- [[démonstrations - integration (résumé)]] : les preuves du cours (5)
- [[Intégration UTILITAIRE (résumé)]] : fiche pratique (0)

### Year 1 - Algèbre Linéaire

- [[Sources/Year 1/Algèbre Linéaire/chp1 (résumé)|chp1 (résumé)]] : espaces vectoriels, familles, bases (2)
- [[Sources/Year 1/Algèbre Linéaire/chp2 (résumé)|chp2 (résumé)]] : applications linéaires, morphismes, rang (4)
- [[Sources/Year 1/Algèbre Linéaire/chp3 (résumé)|chp3 (résumé)]] : pivot de Gauss, systèmes (3)
- [[Sources/Year 1/Algèbre Linéaire/chp4 (résumé)|chp4 (résumé)]] : matrices, matrice d'une application (2)
- [[Sources/Year 1/Algèbre Linéaire/chp5 (résumé)|chp5 (résumé)]] : changement de base, déterminant (2)
- [[Sources/Year 1/Algèbre Linéaire/chp6 (résumé)|chp6 (résumé)]] : déterminant, caractérisation des bases (3)
- [[Sources/Year 1/Algèbre Linéaire/chp7 (résumé)|chp7 (résumé)]] : éléments propres, somme directe (2)

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

## Matières (40)

- **Year 1, autres** : [[Year 1 - Algo Maths]], [[Year 1 - Communication orale]], [[Year 1 - Corps à l'oeuvre]], [[Year 1 - Dessein au cube]], [[Year 1 - HDA]], [[Year 1 - Outil Maths]], [[Year 1 - Peinture]], [[Year 1 - Philosophie]], [[Year 1 - Projet design]]
- **Year 2, autres** : [[Year 2 - Algo]], [[Year 2 - Anglais]], [[Year 2 - Corps à l'oeuvre]], [[Year 2 - Operating System]], [[Year 2 - Philosophie]], [[Year 2 - Probability]], [[Year 2 - Projet Design]], [[Year 2 - écriture narrative]]
- **Year 3** : [[Year 3 - Computer Network]], [[Year 3 - Culture du vivant]], [[Year 3 - Data analysis (Thanos)]], [[Year 3 - Data base]], [[Year 3 - IA]], [[Year 3 - Java]], [[Year 3 - SHS]], [[Year 3 - Statistics]], [[Year 3 - Séries]], [[Year 3 - ligue football]], [[Year 3 - workshop]]
- **Year 4** : [[Year 4 - C++]], [[Year 4 - Culture du vivant]], [[Year 4 - SHS]], [[Year 4 - data mining]], [[Year 4 - graph theory]], [[Year 4 - management de l'innovationb]], [[Year 4 - projet court]]

- [[Year 1 - Analyse Maths]] : 2 notes sur 2, une grande partie reste en PDF
- [[Year 2 - Analyse]] : 3 notes sur 3 pour le chapitre 7, le reste est en PDF
- [[Year 2 - Analyse dans Rn]] : 4 notes intégrées sur 4, et ce qu'il faut revoir en priorité
- [[Year 1 - Algèbre Linéaire]] : 7 notes intégrées sur 7, vocabulaire français et anglais, et ce qu'il faut revoir en priorité
- [[Year 2 - Bilinear Algebra]] : 8 notes intégrées sur 8, et ce qu'il faut revoir en priorité

## Synthèses (0)

Aucune pour l'instant.

## Sources disponibles

Notes présentes dans `Cours/` (165), par matière. Le nombre entre parenthèses est le nombre de notes.

### Year 1

Algo Maths (3), Algèbre Linéaire (7), Analyse Maths (2), Communication orale (2), Corps à l'oeuvre (1), Dessein au cube (7), HDA (1), Outil Maths (4), Peinture (3), Philosophie (2), Projet design (6)

### Year 2

Algo (5), Analyse (3), Analyse dans Rn (4), Anglais (3), Bilinear Algebra (8), Corps à l'oeuvre (1), Operating System (21), Philosophie (5), Probability (7), Projet Design (4), écriture narrative (1)

### Year 3

Computer Network (7), Culture du vivant (3), Data analysis (Thanos) (15), Data base (2), IA (1), Java (1), SHS (3), Statistics (7), Séries (7), ligue football (1), workshop (1), plus 1 note à la racine de `Year 3`

### Year 4

C++ (3), Culture du vivant (1), SHS (3), data mining (1), graph theory (5), management de l'innovationb (2), projet court (1)
