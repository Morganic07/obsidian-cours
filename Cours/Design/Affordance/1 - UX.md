---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Affordance/Présentation Tests Utilisateurs ID3.pptx|Présentation Tests Utilisateurs ID3.pptx]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du diaporama « Introduction + Test utilisateurs » (8 janvier 2026, 25 diapositives), dans [[Cours/Design/Affordance/_index|Affordance]]. Suite : [[2 - UX|UX Research - Observation]]. Les noms d'étudiants (groupes du projet), les noms des intervenants du planning et l'adresse de contact de l'intervenant ne sont pas repris.

Le diaporama compte trois parties : ergonomie et UX, organisation des cours, test utilisateur (protocole, passation, analyse).

## 1. Ergonomie et UX

### Exemples d'objets

La diapositive « Ergonomie / Expérience utilisateur » présente, sans légende, une série de produits qui relèvent de ces deux disciplines :

![[Présentation Tests Utilisateurs ID3 - image30.png]]

*Figure : borne ou poste d'accueil avec écran, sur un bureau.*

![[Présentation Tests Utilisateurs ID3 - image31.png]]

*Figure : robot de cuisine à écran tactile.*

![[Présentation Tests Utilisateurs ID3 - image27.png]]

*Figure : défroisseur vertical à vapeur.*

![[Présentation Tests Utilisateurs ID3 - image25.png]]

*Figure : appareil à écran circulaire monté sur un bras articulé.*

![[Présentation Tests Utilisateurs ID3 - image38.png]]

*Figure : salle de contrôle avec postes de travail et mur d'écrans.*

![[Présentation Tests Utilisateurs ID3 - image26.png]]

*Figure : écran d'application mobile « Pilotez alarme et caméras avec l'appli ».*

![[Présentation Tests Utilisateurs ID3 - image33.png]]

*Figure : terminal portable de saisie (scanner et tablette durcie) tenu en main.*

Le cours ne commente pas ces objets : ils montrent la diversité des terrains de l'ergonomie et de l'UX (mobilier, électroménager, poste de supervision, application, outil professionnel).

### Définition de l'ergonomie

> « C'est la mise en œuvre de connaissances scientifiques relatives à l'homme et de méthodes pour concevoir des systèmes utilisables par le plus grand nombre avec le maximum de confort, de sécurité et d'efficacité. »
> SELF (Société d'ergonomie de langue française)

Voir [[Ergonomie]] et [[Expérience utilisateur]].

L'Association internationale d'ergonomie (IEA) distingue trois domaines de spécialisation : l'ergonomie **physique** (postures, gestes, efforts, aménagement du poste), l'ergonomie **cognitive** (perception, mémoire, raisonnement, [[Charge cognitive|charge cognitive]], interaction avec les interfaces) et l'ergonomie **organisationnelle** (organisation du travail, horaires, communication, travail d'équipe). L'UX relève surtout de l'ergonomie cognitive. [[Complément hors du cours|ⓘ]]

On oppose aussi l'**ergonomie de correction**, qui intervient sur un produit ou un poste existant pour en corriger les défauts, et l'**ergonomie de conception**, qui intervient dès le projet ; la seconde coûte moins cher et évite les problèmes au lieu de les réparer, d'où l'intérêt de tester tôt, sur maquettes et prototypes. [[Complément hors du cours|ⓘ]]

**Ergonomie et UX.** La norme ISO 9241-210 définit l'expérience utilisateur comme les « perceptions et réactions d'une personne qui résultent de l'utilisation effective et/ou anticipée d'un produit, système ou service ». Là où l'ergonomie vise d'abord l'[[Utilisabilité|utilisabilité]] (un produit utilisable, sûr, confortable), l'UX y ajoute les émotions, le plaisir, l'esthétique et le sens que l'utilisateur donne à son expérience, avant, pendant et après l'usage. [[Complément hors du cours|ⓘ]]

L'ergonomie combine deux ensembles :

| Connaissances scientifiques relatives à l'humain | + | Méthodes d'étude et de conception |
|---|---|---|
| Biomécanique | | Ethnographie |
| Physiologie | | Sociologie |
| Sciences cognitives | | Psychologie (« psychologue » sur la diapositive) |
| | | Design |

Les deux colonnes sont illustrées par des photos décoratives (un squelette aux articulations en surbrillance, une paire de jumelles), non reprises.

### Le système étudié

Schéma adapté de Brangier et Barcenilla (2003), fait de formes PowerPoint : un grand cercle découpé en quatre carrés, **produits** (en haut à gauche), **environnement** (en haut à droite), **tâches** (en bas à gauche) et **utilisateur** (en bas à droite), autour d'un cercle central, sans flèche entre eux ; sous le cercle, une frise de cinq points porte l'étiquette **temps**. L'ergonomie étudie l'utilisateur en interaction avec les tâches, les produits et l'environnement, et l'évolution de ces relations dans le temps.

## 2. Organisation des cours

### Planning (janvier à mars 2026)

| Date | Séance |
|---|---|
| 9 janvier 2026 | Tests utilisateurs |
| 14 janvier 2026 | Psychologie cognitive |
| 28 janvier 2026 | User research |
| 4 février 2026 | Conception IHM |
| 11 février 2026 | Conception IHM |
| 18 février 2026 | Conception IHM |
| 4 mars 2026 | Projet |

Chaque séance associe l'intervenant principal et un ou plusieurs intervenants spécialistes ; la dernière en réunit quatre.

### Projet fil rouge

**Conception d'une application mobile pour un groupement de musées** :

- utilisable pour plusieurs musées ;
- qui gère l'avant-visite, la visite et l'après-visite.

Étapes du projet :

1. recueil des besoins et des comportements utilisateurs ([[Recherche utilisateur]]) ;
2. construction des *user journeys* ([[Parcours utilisateur]]) ;
3. construction des [[Scénario d'usage|scénarios d'usage]] envisagés ;
4. focus sur un moment du parcours ;
5. construction de l'[[Arborescence d'une application|arborescence de l'application]] ;
6. conception des écrans et maquettage ([[Maquette (design)]]).

Groupes de trois ou quatre étudiants, quatre groupes dans chacune des deux classes (ID3-A et ID3-B).

## 3. Le test utilisateur

### Définition

Le [[Test utilisateur|test utilisateur]] est une méthode d'évaluation de l'[[Utilisabilité|utilisabilité]] d'un produit, qu'on fait tester **individuellement** par des **utilisateurs cibles**.

- En temps réel, les utilisateurs manipulent le produit pour réaliser des scénarios d'usage représentatifs des usages futurs.
- L'évaluation consiste à observer comment ils interagissent avec le produit, à mesurer des indicateurs de performance et à recueillir leurs réactions et avis.
- Les scénarios sont rédigés comme des **objectifs à atteindre**, un objectif par scénario. Ils sont remis **par écrit**, pour éviter les biais et interférer le moins possible avec l'utilisateur.

![[Présentation Tests Utilisateurs ID3 - image49.png]]

*Figure : séance de test en salle, un participant devant un ordinateur portable, une animatrice à ses côtés, caméra sur pied.*

Le test utilisateur se distingue de l'[[Évaluation experte|évaluation experte]] (inspection de l'interface par un spécialiste, sans utilisateurs, par exemple à l'aide d'heuristiques) : l'experte est rapide et peu coûteuse, mais seul le test montre ce que font de vrais utilisateurs. Les deux se combinent souvent, l'évaluation experte corrigeant les défauts évidents avant le test. [[Complément hors du cours|ⓘ]]

### Trois axes d'évaluation

Ces trois axes viennent de la définition de l'utilisabilité dans la norme ISO 9241-11 : le « degré selon lequel un produit peut être utilisé, par des utilisateurs identifiés, pour atteindre des buts définis avec efficacité, efficience et satisfaction, dans un contexte d'utilisation spécifié ». L'utilisabilité n'est donc pas une qualité absolue du produit : elle dépend des utilisateurs, de leurs buts et du contexte. [[Complément hors du cours|ⓘ]]

| Axe | Questions |
|---|---|
| **Efficacité** | L'utilisateur réussit-il à atteindre ses objectifs ? Parvient-il à achever la tâche ? |
| **Efficience** | Atteint-il ses objectifs rapidement et sans erreur ? En dépensant un minimum de ressources ? |
| **Satisfaction** | L'interface lui plaît-elle ? Est-il satisfait ? |

Chaque axe se mesure par des indicateurs habituels : l'efficacité par le **taux de réussite** des scénarios ; l'efficience par le **temps** de réalisation, le **nombre d'erreurs** ou d'actions (clics, pages visitées) par rapport au chemin optimal ; la satisfaction par un **questionnaire standardisé** et les verbatims. Les deux premiers sont des mesures objectives, le troisième une mesure subjective. [[Complément hors du cours|ⓘ]]

### Déroulement d'un test

| Phase | Étapes |
|---|---|
| **Protocole** | cadrer les objectifs du test ; construire des hypothèses ; définir le panel ; définir le déroulement du test ; recruter le panel ; dispositif et matériel ; pré-test |
| **Passation** | sessions de test |
| **Analyse** | diagnostic ; recommandations |

Le **pré-test** est une session à blanc, avec un participant proche de la cible ou un collègue, pour vérifier que les scénarios sont compris, que la durée tient et que le matériel d'enregistrement fonctionne ; on corrige le protocole avant les vraies sessions. [[Complément hors du cours|ⓘ]]

Le dispositif comprend en général l'enregistrement de l'écran, de la voix et parfois du visage : il suppose le [[Consentement éclairé|consentement éclairé]] écrit du participant (objet de l'étude, enregistrement, usage et durée de conservation des données), qu'impose en Europe le RGPD pour les données personnelles. [[Complément hors du cours|ⓘ]]

### Types de tests

![[Présentation Tests Utilisateurs ID3 - image43.png]]

*Figure : quatre modalités de test, en userlab, en environnement réel, synchrone à distance, asynchrone à distance.*

La diapositive ne fait que nommer ces quatre modalités, sans les décrire.

Ce que recouvre chaque modalité : [[Complément hors du cours|ⓘ]]

- **en userlab** (laboratoire d'utilisabilité) : salle équipée, souvent doublée d'une salle d'observation derrière une vitre sans tain ; conditions maîtrisées et enregistrement complet, mais contexte artificiel. [[Complément hors du cours|ⓘ]]
- **en environnement réel** (*in situ*) : chez l'utilisateur, sur son lieu de travail ou dans le lieu d'usage (ici, le musée) ; contexte, bruit et interruptions réels, au prix d'une logistique plus lourde. [[Complément hors du cours|ⓘ]]
- **synchrone à distance** : l'animateur et le participant sont en visioconférence, avec partage d'écran ; l'animateur peut relancer et poser des questions, sans déplacement. [[Complément hors du cours|ⓘ]]
- **asynchrone à distance** (non modéré) : le participant réalise seul les scénarios sur une plateforme qui enregistre ses actions et ses réponses ; on obtient vite beaucoup de participants, mais sans pouvoir relancer ni comprendre un blocage. [[Complément hors du cours|ⓘ]]

## 4. Protocole

### Objectifs et hypothèses : exemple d'un site de vente en ligne

**Objectifs** : obtenir des recommandations opérationnelles pour :

1. améliorer la recherche d'un produit ;
2. augmenter les performances de vente en ligne ;
3. détecter les aménagements graphiques à envisager pour garantir une bonne perception de la marque à travers le site ;
4. identifier les évolutions de la terminologie et des pictogrammes qui faciliteraient la compréhension du site.

**Hypothèses** (à confirmer ou infirmer par le test) :

1. l'efficacité du moteur de recherche facilite la recherche de produit ;
2. la catégorisation des produits dans la navigation oriente efficacement les utilisateurs ;
3. les pages produits sont trop complexes, et leur structure ne facilite pas la décision d'achat ;
4. le tunnel d'achat (formulaires et navigation) n'est pas optimisé et engendre erreurs et abandons ;
5. le graphisme du site contribue à l'attrait esthétique et véhicule les valeurs de la marque ;
6. la terminologie et l'iconographie sont compréhensibles par les différentes cibles.

Le **tunnel d'achat** (ou tunnel de conversion) est la suite d'étapes entre l'ajout au panier et la confirmation de la commande (panier, identification, livraison, paiement) ; on le dit « tunnel » parce que le site y retire en général les éléments de navigation qui feraient sortir l'acheteur. Chaque hypothèse est formulée de façon à pouvoir être vérifiée par un scénario et un indicateur : l'hypothèse 4, par exemple, se teste par un scénario d'achat complet, en relevant erreurs de saisie et abandons. [[Complément hors du cours|ⓘ]]

### Panel utilisateur

Voir [[Panel d'utilisateurs]].

**Quelles caractéristiques ?** Un panel le plus proche possible de la population cible :

- profil socio-professionnel (âge, sexe…) ;
- taux d'équipement et appétence pour les nouvelles technologies ;
- niveau novice ou expert sur les problématiques du service ;
- …

Attention à la **fréquence de participation** de certains participants (testeurs trop habitués).

**Combien de participants ?**

- 5 utilisateurs détectent **80 %** des problèmes d'utilisabilité ;
- 8 à 12 utilisateurs sont conseillés ;
- plus de 30 si l'on veut un traitement statistique.

![[Présentation Tests Utilisateurs ID3 - image48.png]]

*Figure : courbe « 5 participants uncover 80% of usability issues » : part des problèmes d'utilisabilité trouvés (0 à 100 %) en fonction du nombre de participants (0 à 15), forte hausse puis plateau.*

**D'où vient cette courbe.** Elle vient du modèle de Nielsen et Landauer (1993) : si chaque participant découvre en moyenne une proportion $L$ des problèmes, la part des problèmes trouvés avec $n$ participants vaut $1-(1-L)^n$. Avec la valeur moyenne mesurée par les auteurs, $L \approx 0{,}31$, on obtient $1-0{,}69^5 \approx 0{,}84$ pour cinq participants, d'où les 80 à 85 % souvent cités ; chaque participant supplémentaire apporte de moins en moins de problèmes nouveaux, d'où le plateau. [[Complément hors du cours|ⓘ]]

La règle des cinq utilisateurs vaut pour un **test qualitatif**, avec un groupe d'utilisateurs homogène : s'il y a plusieurs profils très différents (novices et experts, visiteurs et personnel du musée), il faut quelques participants par profil. La recommandation qui l'accompagne est de faire **plusieurs petits tests itératifs** (tester, corriger, retester) plutôt qu'un seul grand. Le seuil d'une trentaine de participants correspond, lui, à un **test quantitatif**, où l'on veut comparer des moyennes (temps, taux de réussite) avec des statistiques. [[Complément hors du cours|ⓘ]]

### Scénarios

Mettre en place des scénarios adaptés aux objectifs et aux hypothèses :

- définir les tâches représentatives des différents objectifs utilisateurs ;
- mettre en scène ces tâches dans des scénarios d'usage réalistes.

Règles de rédaction :

- **un seul objectif par scénario** ;
- rédaction **immersive** ;
- fournir les informations complémentaires si nécessaire ;
- attention particulière au **premier scénario** (exploratoire, ou simple).

Exemple de la différence entre un objectif et une consigne : « Vous comptez venir au musée samedi avec deux enfants de 8 et 10 ans ; trouvez une visite qui leur convient et réservez-la » donne un but et laisse l'utilisateur chercher son chemin, alors que « Cliquez sur Agenda puis sur Réserver » lui dicte le parcours et ne teste plus rien. On évite aussi de reprendre dans le scénario les mots exacts des menus, qui guideraient l'utilisateur. [[Complément hors du cours|ⓘ]]

## 5. Passation : déroulement d'une session

| Étape | Contenu |
|---|---|
| Accueil et entretien introductif | accueil ; présentation de l'étude et du déroulement ; recueil des données de profil |
| Recueil des usages actuels | informations sur les usages actuels |
| Tests scénarisés | réalisation des scénarios d'usage ; évaluation de l'utilisabilité de l'interface |
| Évaluation subjective | recueil des points bloquants et difficultés ; perception globale du service avec un **outil standardisé** |

L'outil standardisé n'est pas nommé dans le diaporama. Voir aussi [[Entretien semi-directif]], [[Questionnaire]].

Le plus répandu est le [[System Usability Scale|SUS]] (*System Usability Scale*, conçu par Brooke en 1986, publié en 1996) : dix affirmations notées de 1 (pas du tout d'accord) à 5 (tout à fait d'accord), alternativement positives et négatives. Pour les items impairs (positifs), on compte la note moins 1 ; pour les items pairs (négatifs), 5 moins la note ; la somme, multipliée par 2,5, donne un score de 0 à 100. Ce score n'est pas un pourcentage : un score moyen se situe autour de 68. Voir aussi [[Échelles UX]]. [[Complément hors du cours|ⓘ]]

**[[Penser à voix haute]]** (*think aloud*). Pendant les tests scénarisés, on demande en général au participant de verbaliser ce qu'il cherche, ce qu'il pense et ce qui le surprend, au fil de ses actions. C'est la principale source des verbatims, et elle explique les erreurs que la seule observation montre sans les expliquer. Ses limites : elle ralentit le participant (les temps mesurés sont moins fiables) et certains se taisent dès que la tâche devient difficile ; l'animateur relance alors par des questions neutres (« Qu'est-ce que vous cherchez ? »). [[Complément hors du cours|ⓘ]]

**Posture de l'animateur.** Il n'aide pas et ne commente pas : on teste l'interface, pas le participant, ce qu'il faut lui dire en accueil pour le mettre à l'aise. Il reste neutre (pas d'approbation qui orienterait), renvoie les questions (« Que feriez-vous si vous étiez seul ? ») et note le moment où il intervient, d'où la catégorie « réussite avec aide » de l'analyse. Le participant, qui se sait observé, tend à modifier son comportement ([[Effet Hawthorne|effet Hawthorne]]) et à donner les réponses qu'il croit attendues ([[Biais de désirabilité sociale|biais de désirabilité sociale]]), ce qui conduit à relativiser les avis très positifs. [[Complément hors du cours|ⓘ]]

## 6. Analyse

Ce qu'on tire des sessions :

- répartition **succès / réussite avec aide / échec / abandon** ;
- **parcours types** (répartition des points d'entrée, de l'usage du menu…) ;
- principales **erreurs** commises ;
- **temps moyen** (si pertinent) ;
- évaluation de la **simplicité perçue** du scénario ;
- **verbatims** des utilisateurs.

Pour passer du diagnostic aux recommandations, on classe chaque problème par **gravité**, en croisant sa fréquence (combien de participants l'ont rencontré), son impact (simple gêne, perte de temps, échec de la tâche) et sa persistance (le problème revient-il à chaque usage ?). Les recommandations se priorisent ensuite selon la gravité et le coût de la correction : on traite d'abord les problèmes bloquants qui touchent beaucoup d'utilisateurs. [[Complément hors du cours|ⓘ]]

Liens : [[Persona]], [[Entretien semi-directif]].
