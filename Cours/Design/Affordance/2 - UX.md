---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Affordance/UX Research - Observation - 2026.pptx|UX Research - Observation - 2026.pptx]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du diaporama « UX Research » (41 diapositives, janvier 2026), dans [[Cours/Design/Affordance/_index|Affordance]]. Il couvre les méthodes de recherche utilisateurs (entretien, questionnaire) puis l'observation. Il se complète avec [[1 - UX|la présentation sur les tests utilisateurs]]. Ne pas confondre avec le concept [[Affordance]] : ici, Affordance désigne le nom de la matière.

Sommaire du diaporama : 1. Les méthodes de recherche utilisateurs (p. 5) ; 2. L'observation (p. 16).

## Projet fil rouge

**Conception d'une application mobile pour un groupement de musées**, utilisable pour plusieurs musées, qui gère l'avant-visite, la visite et l'après-visite.

Étapes : recueil des besoins et comportements utilisateurs ; construction des *user journeys* ([[Parcours utilisateur]]) ; construction des [[Scénario d'usage|scénarios d'usage]] envisagés ; focus sur un moment du parcours ; construction de l'[[Arborescence d'une application|arborescence]] ; conception des écrans et maquettage.

## 1. Les méthodes de recherche utilisateurs

### Panorama des méthodes UX design

Le diaporama place autour de « votre besoin » seize méthodes, puis met en avant, sur la diapositive suivante, celles qui servent au **recueil des besoins et des usages** : sur cette diapositive, six méthodes gardent leur couleur et les autres passent en gris, soit l'entretien, le focus group, le questionnaire, l'observation, le persona et l'analyse de l'activité.

| | | | |
|---|---|---|---|
| Entretien | [[Focus group]] | [[Idéation]] | [[Questionnaire]] |
| [[Évaluation experte]] | [[Maquette (design)\|Maquette]] | Observation | [[Persona]] |
| [[Tri de cartes]] | Maquettage | [[Prototype]] | [[Test utilisateur\|Tests utilisateurs]] |
| [[Échelles UX]] | Outils digitaux | [[Analyse de l'activité]] | Papier crayon |

D'après la suite du cours, les méthodes de recueil détaillées sont l'entretien, le questionnaire et l'observation.

Ces méthodes se rangent souvent selon deux axes : **déclaratif ou comportemental** (ce que les gens disent, dans un entretien ou un questionnaire, ou ce qu'ils font, observé directement) et **qualitatif ou quantitatif** (comprendre le pourquoi sur peu de personnes, ou mesurer l'ampleur sur beaucoup). Les gens ne font pas toujours ce qu'ils disent : on surestime ses bonnes pratiques, on oublie les gestes devenus automatiques. D'où l'intérêt de croiser plusieurs méthodes sur une même question, ce qu'on appelle la **triangulation**. Voir [[Enquête qualitative et quantitative]]. [[Complément hors du cours|ⓘ]]

### L'entretien

Voir [[Entretien semi-directif]].

On distingue trois formes d'entretien selon la liberté laissée à la personne : l'entretien **directif** (questions fixées dans un ordre fixe, proche d'un questionnaire oral), l'entretien **semi-directif** (un guide de thèmes et de questions, suivi avec souplesse, avec des relances : la forme la plus courante en UX) et l'entretien **non directif** ou libre (un thème de départ, la personne déroule son propos). Plus l'entretien est libre, plus il fait émerger de l'imprévu, et plus il est difficile à comparer et à analyser. [[Complément hors du cours|ⓘ]]

**Buts multiples** :

- collecte de données qualitatives et quantitatives ;
- analyse de l'existant ;
- enquête exploratoire.

**Collecter des informations pour** : étudier l'utilisateur ; étudier ses usages et le contexte d'usage ; étudier ce que l'utilisateur « pense de… » ; obtenir du retour d'expérience ; réaliser des entretiens exploratoires.

| Avantages (+) | Limites (−) |
|---|---|
| Les objectifs de l'utilisateur | Uniquement déclaratif |
| Le ressenti de l'utilisateur | Absence directe du contexte d'usage |
| Flexibilité | Pas adapté aux grands échantillons |
| Peut être combiné à d'autres méthodes | Biais ([[Effet de halo\|effet de halo]], [[Biais de confirmation\|biais de confirmation]], rapport interviewer-interviewé…) |
| Facilité de mise en place | |

Les deux biais du tableau : l'[[Effet de halo|effet de halo]] est la contamination du jugement par une impression générale (un enquêté sympathique paraît plus crédible, une interface jolie paraît plus facile) ; le [[Biais de confirmation|biais de confirmation]] pousse l'enquêteur à retenir ce qui confirme ses hypothèses et à poser des questions qui les appellent. S'y ajoute le [[Biais de désirabilité sociale|biais de désirabilité sociale]] : l'enquêté donne la réponse qu'il juge valorisante ou attendue (« oui, je prépare toujours ma visite »). On les limite par des questions ouvertes et neutres, et en faisant raconter des situations précises et récentes (« la dernière fois que… ») plutôt que des habitudes générales. [[Complément hors du cours|ⓘ]]

**L'entretien par rapport à…**

| Comparé à | + | − |
|---|---|---|
| l'observation | perception utilisateur ; terrains inaccessibles ; peut évoquer des situations passées | déclaratif ; contexte ; limite la compréhension et l'appropriation par l'enquêteur |
| le questionnaire | qualitatif ; flexible | peu adapté à l'étude quantitative ; coûts |

### Le questionnaire

Voir [[Questionnaire]].

**Buts multiples** :

- collecte de données quantitatives et qualitatives sur des usages existants ;
- enquête exploratoire ;
- traitements statistiques.

**Collecter des informations pour** :

- décrire et comprendre les utilisateurs et leurs comportements vis-à-vis d'un produit, d'un système, d'un service, d'un concept ;
- décrire et comprendre le contexte d'utilisation ;
- explorer et comprendre les besoins et attentes des utilisateurs (potentiels) ;
- détecter les comportements et attitudes qui ressortent, comprendre leur répartition (caractère générique ou spécifique d'un problème ou d'un usage) et leur importance relative dans la population cible.

| Avantages (+) | Limites (−) |
|---|---|
| Accès à un grand nombre d'utilisateurs, même dispersés, rapidement et à faible coût | Difficile de recueillir émotions et ressentis |
| Administration en ligne simplifiée | Biais dus à la formulation des questions et au panel de répondants |
| Beaucoup de données, traitements statistiques possibles | Impossible de clarifier certaines réponses ou de vérifier que toutes ont été fournies |
| Méthode uniforme, donc relativement fiable (pas de variantes dans les questions, pas d'influence d'un interviewer) | Panel de répondants sachant lire et écrire |

**Par rapport à l'entretien et à l'observation** : + adapté à l'étude quantitative et aux grands échantillons, coûts ; − qualitatif, flexibilité.

**Types de questions** : les questions **fermées** (oui/non, choix unique, choix multiples) se dépouillent facilement et se prêtent aux statistiques ; les questions **à échelle**, comme l'échelle de Likert (de « pas du tout d'accord » à « tout à fait d'accord », en 5 ou 7 points), mesurent une opinion ou une intensité ; les questions **ouvertes** recueillent du qualitatif mais demandent un codage à l'analyse. [[Complément hors du cours|ⓘ]]

**Règles de rédaction**, pour limiter le biais de formulation : une seule idée par question (« Le site est-il clair et rapide ? » en contient deux) ; pas de question orientée (« Ne trouvez-vous pas que… ») ; pas de double négation ni de jargon ; des modalités de réponse exhaustives et sans recouvrement (prévoir « autre » et « ne sait pas ») ; les questions personnelles en fin de questionnaire. On le teste sur quelques personnes avant la diffusion. [[Complément hors du cours|ⓘ]]

Pour que les résultats valent pour la population cible, l'échantillon doit lui ressembler : un questionnaire diffusé seulement sur les réseaux du musée ne touche que des visiteurs déjà fidèles. Voir [[Échantillonnage]]. [[Complément hors du cours|ⓘ]]

## 2. L'observation

Voir [[Observation de terrain]], [[Observation participante]], [[Types de suivi en observation]].

### Principes

**Buts multiples** : analyser l'activité réelle ; analyser l'environnement ; confronter des hypothèses.

**Collecter des informations sur** : buts et besoins ; contextes ; pratiques ; interactions ; ressources et contraintes.

**Sous plusieurs formes** : grilles d'observation ; transcriptions d'observations ; notes de terrain ; journal de bord ; photos ; vidéos ; documents ; artefacts ; verbatims…

| Avantages (+) | Limites (−) |
|---|---|
| Objectivité | Ressenti de l'utilisateur |
| Vision globale, contextuelle | Risque de sur-interprétation |
| Capter ce qui ne s'énonce pas | Difficulté d'accès à certains terrains |
| Peut être combinée à d'autres méthodes | Biais (effet de halo, biais de confirmation, [[Effet Hawthorne\|effet Hawthorne]]…) |
| Illustrer un discours | |

L'[[Effet Hawthorne|effet Hawthorne]] désigne la modification du comportement des personnes du seul fait qu'elles se savent observées ; on le réduit en restant discret, en observant assez longtemps pour que les personnes s'habituent à la présence de l'observateur, ou par une observation indirecte. Le **risque de sur-interprétation** vient de ce que l'observateur voit un geste sans en connaître la raison : un entretien juste après l'observation permet de vérifier son interprétation. [[Complément hors du cours|ⓘ]]

**L'observation par rapport à…**

| Comparée à | + | − |
|---|---|---|
| l'entretien | contourner le déclaratif ; observer des pratiques ; contexte | accès à la subjectivité |
| le questionnaire | qualitatif et quantitatif ; flexibilité | peu adaptée à l'étude quantitative à grande échelle ; coût |

### Exemples de mise en œuvre

Deux diapositives montrent, sans commentaire, des terrains d'observation :

![[UX Research - Observation - 2026 - image40.png]]

*Figure : postes de travail de bureau, plusieurs écrans, téléphone et documents.*

![[UX Research - Observation - 2026 - image37.png]]

*Figure : intérieur d'une boutique très fréquentée, clients entre les rayons.*

### Les étapes de l'observation

| Préparation | Réalisation | Analyse |
|---|---|---|
| Reformulation de la demande | Percevoir | Besoins utilisateurs |
| Recherche en amont et formulation d'hypothèses | Coder | Usages et contexte d'usage |
| Choix d'une ou plusieurs méthodes d'observation | | Modélisation de comportements utilisateurs |
| Planification de l'observation | | |
| Définition d'une grille d'observation | | |

**Coder** une observation, c'est traduire ce qu'on voit en catégories définies à l'avance dans la grille (type d'action, lieu, durée, interlocuteur…) pour pouvoir compter et comparer d'une session à l'autre. Le codage peut aussi être ouvert : on note librement, puis on crée les catégories à l'analyse. [[Complément hors du cours|ⓘ]]

## 3. Préparer l'observation

### Choisir les méthodes

Le choix se fait en fonction **des buts**, **des hypothèses**, **des terrains** et **des moyens** de l'étude. Il n'est **pas exclusif** : on peut combiner plusieurs méthodes.

Deux familles :

- **observations directes** : avantage de la flexibilité, mais elles peuvent être influencées par la présence de l'observateur ;
- **observations indirectes** : une certaine neutralité des observés, au prix d'une grande préparation et d'un manque de flexibilité.

Modalités :

| Modalité | Alternative |
|---|---|
| Participante | Non participante |
| In situ | Contexte artificiel |
| Ponctuelle | Récurrente |
| À couvert | À découvert |
| Appareillée | Non appareillée |

Ce que recouvrent ces modalités : [[Complément hors du cours|ⓘ]]

- **participante** : l'observateur prend part à l'activité (il travaille avec l'équipe, fait la visite comme un visiteur) ; **non participante** : il reste en retrait. Voir [[Observation participante]]. [[Complément hors du cours|ⓘ]]
- **in situ** : sur le lieu réel de l'activité ; **contexte artificiel** : dans une situation reconstituée, par exemple en laboratoire. [[Complément hors du cours|ⓘ]]
- **ponctuelle** : une seule séance ; **récurrente** : plusieurs séances, pour saisir les variations (jours de forte affluence, saisons). [[Complément hors du cours|ⓘ]]
- **à couvert** : les personnes ne savent pas qu'elles sont observées ; **à découvert** : l'observateur se présente et explique sa démarche. L'observation à couvert évite l'effet Hawthorne mais pose un problème éthique, et la captation d'images de personnes identifiables suppose leur [[Consentement éclairé|consentement]]. [[Complément hors du cours|ⓘ]]
- **appareillée** : avec un dispositif d'enregistrement (caméra, capteurs, *eye tracking* qui suit le regard, journaux d'usage d'une application) ; **non appareillée** : à l'œil, avec la grille et des notes. [[Complément hors du cours|ⓘ]]

L'**auto-observation** (illustrée plus bas) confie le recueil à l'utilisateur lui-même, par exemple au moyen d'un journal de bord ou d'une **étude de journal** (*diary study*) : il note ou photographie ses usages pendant plusieurs jours, ce qui donne accès à des moments où l'observateur ne peut pas être présent. [[Complément hors du cours|ⓘ]]

Méthode classique de l'UX qui combine observation et entretien : l'[[Enquête contextuelle|enquête contextuelle]] (*contextual inquiry*), où l'on observe la personne dans son contexte réel, pendant qu'elle fait son activité, en lui demandant d'expliquer ce qu'elle fait, dans une relation de type maître-apprenti. [[Complément hors du cours|ⓘ]]

### Exemples de méthodes couramment utilisées

![[UX Research - Observation - 2026 - image36.jpg]]

*Figure : observation directe non participante, illustrée par un chantier où des ouvriers manipulent des matériaux.*

![[UX Research - Observation - 2026 - image43.png]]

*Figure : observation indirecte appareillée, illustrée par des caméras de surveillance.*

![[UX Research - Observation - 2026 - image38.jpg]]

*Figure : observation participante et auto-observation, illustrée par une équipe en tee-shirts « Crew » au travail.*

### Exercice fil rouge (1)

Définir en groupe, pour le projet :

- les **problématiques, hypothèses** et besoins en données de l'étude ;
- les **thèmes** de l'étude, par exemple : usages ; déplacements dans un espace ; séquences ; interactions entre utilisateurs ; manipulation d'objets… ;
- le **cadre** : le moment ; qui ou quoi observer ; le terrain ; la complémentarité avec d'autres méthodes ;
- en fonction de ce qui précède, les **méthodes d'observation** les plus adaptées.

Pas de correction dans le diaporama (travail de groupe).

### Construire la grille d'observation

Voir [[Grille d'observation]].

La grille d'observation :

- est la **mise en pratique des hypothèses et objectifs** de l'étude ;
- est **préparée à l'avance** et pensée pour être utilisée pendant l'observation ;
- peut être testée et affinée par une **observation préliminaire** : les observables, le protocole, le point de vue, le matériel nécessaire…

Contenu habituel :

1. **Informations génériques** : nom du lieu, date, heure ou durée de l'observation.
2. **Contexte** de la situation observée :
   - les acteurs (qui, caractéristiques, seul ou en groupe) ;
   - le lieu (disposition, équipements, particularités).
3. **Usages et actions** :
   - l'activité générale, les besoins, les buts (« ! ») des participants ;
   - l'activité fine : modes opératoires, parcours utilisateurs, actions, erreurs et messages du système (*feedbacks*) ;
   - les comportements, gestuelles, postures, déplacements, positions stationnaires ;
   - les verbalisations, prises d'informations, réactions.
4. **Commentaires libres** de l'observateur et prises de vues.

### Exemple 1 : grille d'un service d'accueil des usagers

**1. Organisation du lieu**

- extérieure : accès à la structure, signalétique externe, infrastructures (parking…), accessibilité PMR… ;
- intérieure : signalétique intérieure, sens de circulation, accessibilité PMR… ;
- locaux de réception : agencement spatial, salles et matériel, postes d'accueil, salle d'attente, mesures spécifiques Covid…

**2. Organisation du flux**

- si multiservices : zone multiservice ou zones dédiées ;
- entrée (accessibilité PMR…) ; zone d'accueil ; zone d'attente ;
- zone d'entretien (salle dédiée ou open space, espace de confidentialité à qualifier…) ;
- sortie (différenciée de l'entrée, accessibilité PMR…).

**3. Fonctionnement de l'équipe**

- nombre d'agents présents le jour de l'observation ;
- échanges entre agents (nature, durée, points formels ou informels…) ;
- supports de transmission d'informations (papier, mail, oral…) ;
- organisation de l'activité entre agents (ordre d'arrivée, disponibilité, spécialité…).

**4. Entretien entre agent et usager**

- profil de l'usager (caractéristiques, âge, langue, niveau digital…) ;
- (1) expression de la demande (compréhension, connaissance du partenaire, objectif, attentes…) ;
- (2) reformulation et précision du besoin : informations ou documents demandés, nature de la demande, partenaire concerné et type d'accès ;
- (3) résolution de la demande : réponse du partenaire (immédiate, différée, prise de RDV…), nature des échanges avec le partenaire, accompagnement ou substitution, actions réalisées par l'agent, actions réalisées par l'usager, prise de notes de l'agent, partage d'information avec l'usager (double écran…) ;
- (4) suites et clôture du RDV : prochaines étapes (entretien terminé, action autonome de l'usager, nouveau RDV, RDV avec un partenaire…), documents fournis à l'usager (traces : ce qui a été fait, ce qui va se passer, ce qu'il doit faire, informations de connexion…), devenir des notes (conservation, destruction…).

### Exemple 2 : grille de transcription de dialogue

Colonnes : **qui parle ?** (A = agent, U = usager) ; **étape du rendez-vous** ; **phrases clés**, tournures typiques ou non conventionnelles ; **intention, émotion**.

| Qui | Étape | Phrase clé | Intention, émotion |
|---|---|---|---|
| A | Récapitulatif des informations disponibles pour déterminer la demande (personne déjà venue) | — | Dialogue |
| U | Donne des informations de contexte sur le ton de la conversation avec l'agent | « D'habitude, je le fais sur l'ordinateur à l'accueil mais là ils me l'ont envoyé par la poste mais comme je ne peux pas écrire » | Dialogue |
| A | Signature document | « Je vous fais signer tout de suite comme ça ce sera fait » | Consigne |
| A | Signature document | « Ce document dit que vous êtes d'accord pour le dépassement d'honoraire » | Explication, consigne |
| U | Signature document | « Je n'ai pas le choix », et signe | Humour, réalisation d'action |
| A | Signature document | « Vous avez bien la complémentaire santé ou la CMU ? » | Explication, discussion, prise d'information |

### Exercice fil rouge (2)

Définir en groupe une **ébauche de grille d'observation** pour le projet, à partir de la liste d'observables ci-dessus (informations génériques, contexte, usages et actions, comportements, verbalisations, commentaires et prises de vues). Pas de correction.

## 4. Réaliser l'observation

| Moment | À faire |
|---|---|
| **Avant** | tester le matériel de recueil ; s'assurer de la présence des contacts, avoir les autorisations sur soi ; s'assurer de la présence des participants |
| **Pendant** | percevoir, mémoriser, coder ; rester concentré ; limiter l'impact de sa présence ; prendre des photos, collecter des artefacts ; vérifier l'état des moyens de recueil |
| **Après** | faire un débriefing ; demander des contacts ; commencer à organiser ses notes, faire ressortir les points importants |

## 5. Analyser l'observation

### Objectifs et démarche

L'analyse cherche à identifier : des besoins et buts utilisateurs ; des pratiques et usages ; des contextes d'activité.

Démarche :

1. catégoriser les données ;
2. identifier des moments « typiques » ;
3. identifier et quantifier les convergences et divergences de comportements à ces moments ;
4. expliquer les similitudes et convergences (origine, impact) ;
5. comparer avec l'existant (représentativité, variations).

Pour l'étape 1, l'outil le plus courant est le [[Diagramme d'affinités|diagramme d'affinités]] : chaque observation ou verbatim est écrit sur un post-it, puis l'équipe regroupe les post-its qui se ressemblent et donne un titre à chaque groupe ; les catégories naissent des données au lieu d'être fixées d'avance. [[Complément hors du cours|ⓘ]]

### Exemples de formalisation des données

**Rapport d'activité** (tableau de la diapositive) :

| Activité | Description | Fréquence | Durée cumulée |
|---|---|---|---|
| Édite | Change le code source du programme | 12 | 31 min |
| Note | Prend des notes, ou consulte d'anciennes notes | 3 | 5 min |
| Documentation | Consulte la documentation | 8 | 24 min |

**Graphe temporel d'activité** :

![[UX Research - Observation - 2026 - image35.png]]

*Figure : niveau de charge d'une batterie (en %) de vendredi à mercredi ; deux recharges surlignées, samedi (lieu : domicile, raison : batterie faible, moyen : recharge sur secteur) et lundi (domicile, synchronisation, recharge par port USB).*

**Modélisation de l'activité** :

![[UX Research - Observation - 2026 - image34.png]]

*Figure : « arbre complet des tâches et de leurs relations » pour « manger des crêpes » : acheter les ingrédients, préparer la pâte, faire cuire, déguster ; sous-tâches (mélanger, tamiser, battre au fouet ou au batteur électrique, verser une louche, retourner ou faire sauter), tâche optionnelle en pointillés (sucre vanillé si crêpes sucrées), condition « si la pâte a reposé 2 h ».*

Ce type d'arbre relève de l'[[Analyse hiérarchique des tâches|analyse hiérarchique des tâches]] : on décompose un but général en sous-buts, puis en actions élémentaires, et l'on précise les relations entre elles (séquence, alternative, option, condition). L'arbre sert à repérer les étapes longues, les choix difficiles ou les points d'erreur, que l'interface devra simplifier. [[Complément hors du cours|ⓘ]]

L'ergonomie de langue française distingue la **tâche prescrite** (ce qui est demandé, la procédure prévue) et l'**activité réelle** (ce que la personne fait vraiment pour y parvenir, avec ses raccourcis, contournements et imprévus). L'observation sert précisément à saisir cet écart, qui explique beaucoup d'erreurs et de détournements d'un produit. Voir [[Analyse de l'activité]]. [[Complément hors du cours|ⓘ]]

### Utiliser les analyses

Les conclusions peuvent alimenter :

- des recommandations, la conception ;
- la conception de [[Persona|personas]] ;
- des *experience maps* ([[Carte d'expérience]]), des *user journeys* ;
- des scénarios d'usage, de parcours ;
- un [[Cahier des charges|cahier des charges]] ;
- des [[Storyboard|storyboards]]…

Une **experience map** décrit l'expérience d'une personne autour d'un besoin (voyager, visiter un musée) dans son ensemble, au-delà d'un seul service ; un **user journey** suit le parcours d'un utilisateur dans un service ou un produit précis. Les deux font figurer, étape par étape, les actions, les pensées et les émotions, et font apparaître les points de friction, qui deviennent des opportunités de conception. [[Complément hors du cours|ⓘ]]

![[UX Research - Observation - 2026 - image42.png]]

*Figure : exemple d'experience map (Rail Europe, Adaptive Path, 2011) : principes directeurs, parcours en six étapes (recherche et planification, achat, réservation, après réservation, voyage, après voyage) avec lignes « doing », « thinking », « feeling », « experience », puis opportunités.*

## Prochaines échéances

- Prochain cours : mercredi 4 février, conception, avec les deux groupes.
- Pour le projet : avoir initié la partie *user research*.

Liens : [[Analyse thématique d'entretien]], [[Cours/Sciences humaines/SHS/_index|SHS]] (observation de terrain en ethnographie), [[Recherche utilisateur]].
