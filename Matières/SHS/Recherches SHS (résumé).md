---
type: source
tags: [year4]
sources: ["Note d'origine dans Cours/Year 4/SHS"]
maj: 2026-11-06
complet: true
---

Résumé d'une note de `Cours/Year 4/SHS`, dans [[SHS (matière)]]. Recherches d'un étudiant pour l'enquête sur le [[Open design|design libre et en commun]], reprises dans [[Prise de note SHS (résumé)|la note de travail du groupe]]. Les deux images en tête ne contiennent que du texte (les définitions recopiées ci-dessous) : aucune n'est intégrée. Les transcriptions sont lisibles.

**Origine du texte** : plusieurs passages s'adressent au lecteur (« votre groupe », « votre syllabus ») et se commentent eux-mêmes (« c'est ici que l'analyse d'OpenFisca devient intellectuellement brillante ») : une bonne part de la note semble être un **texte produit par un outil de génération de texte** et recopié, puis annoté par l'étudiant. Les affirmations sur les projets cités ne sont pas sourcées.

## Définitions de départ

- **Design libre et en commun** : le design lui-même comme commun — typographies libres, [[Design system|design systems]] et bibliothèques ouvertes, ressources et productions sous [[Licences libres|licences libres]], [[Design contributif|design contributif]].
- **[[Communs numériques|Commun numérique]]** : une ressource produite ou entretenue collectivement par une communauté d'acteurs hétérogènes, et gouvernée par des règles qui lui assurent son caractère collectif et partagé. Elle peut être numérique : logiciel, base de données, contenu (texte, image, vidéo, son).

## Pistes non sélectionnées

| Piste | Pourquoi elle est écartée |
|---|---|
| Catalogue d'outils gratuits (Google Fonts, communauté Figma, banques d'icônes) | ce ne sont pas des communs régis par une communauté, mais des [[Produit d'appel\|produits d'appel]] d'entreprises privées pour capter des parts de marché |
| Behance, communauté Figma, ArtStation | plateformes propriétaires : accès gratuit aux fichiers, mais aucune gouvernance communautaire ; partager son interface gratuitement n'en fait pas un commun |
| Freesound | la mutualisation s'arrête au téléchargement : le vrai travail de [[Design sonore\|design sonore]] (nettoyer, couper, mixer) se fait seul, hors de la communauté ; pas de curation artistique, seulement des règles légales — on ne « designe rien ensemble » |

**Piste gardée : Hugging Face**. Entreprise privée, mais terrain pertinent, voire obligatoire, pour traiter l'impact de l'[[Intelligence artificielle]] sur la fabrication des communs, critère d'évaluation du syllabus.

## Blender (studio, add-ons)

- Le Blender Studio produit des courts-métrages d'animation de qualité industrielle (*Spring*, *Charge*) et **libère tous les assets** (*rigs* des personnages, textures, modèles 3D, environnements), en général sous licence [[Creative Commons]] Attribution.
- La communauté peut télécharger, décortiquer, modifier et réutiliser ces objets. Mais la **gouvernance de la création initiale reste très verticale** : un réalisateur et un directeur artistique décident de l'esthétique. Le commun n'existe qu'**a posteriori**, une fois le design validé et publié. « Le design par consensus total n'existe pas, même chez Blender. »
- **Il faut être très compétent pour contribuer** : créer des *Geometry Nodes* réutilisables, automatiser un shader ou développer un add-on demande de coder en Python ou de maîtriser des mathématiques vectorielles. L'inclusion vantée par le logiciel libre bute sur une barrière d'ingénierie ; le pouvoir de modifier le commun appartient à une élite hybride, les *Technical Artists*, qui exclut les profils purement visuels.

## OpenFisca

### Pas de design « visuel »

- Dans la typographie libre ou les *Open Movies*, le commun produit une forme visuelle discutable par la communauté ; dans OpenFisca, **l'interface n'existe pas** en soi (c'est une API).
- Le design contributif est amputé de sa dimension créative : une *pull request* (voir [[Demande de fusion]]) ne relève pas d'un choix subjectif mais d'une **stricte conformité au droit** (le Journal officiel). La règle légale et mathématique écrase tout choix formel.

### Il faut être très compétent pour contribuer

- Plus un commun est critique et utile (calculer les aides sociales), plus il **expulse le designer visuel** au profit du binôme développeur et juriste. Le design de l'information y est dicté par la loi.

### La gouvernance par l'expertise

- La communauté d'OpenFisca : agents de l'État, économistes, développeurs civiques. Contribuer au [[Design des règles|design des règles]] exige [[Git]], Python et la lecture des textes de loi.
- Conclusion de la note : la gouvernance ouverte n'est pas synonyme d'inclusion, c'est une **[[Gouvernance par l'expertise|oligarchie de l'expertise]]**. Angle d'enquête proposé : un designer, censé être l'avocat de l'utilisateur final, peut-il trouver sa place dans une gouvernance aussi technique ?

### Et l'IA ?

- OpenFisca est un **[[Système expert|système expert]] déterministe** (si la loi dit A, le code fait exactement A) ; l'[[IA générative]] (LLM) est **probabiliste** (elle prédit le mot suivant, avec un risque d'[[Hallucination (IA)|hallucination]]). Voir [[Modèle déterministe et probabiliste]].
- L'État ne peut pas tolérer qu'une IA « hallucine » le calcul du RSA d'un citoyen : le cœur d'OpenFisca est donc, par nature, **protégé du remplacement direct** par une IA générative.

## Trois insights

### 1. L'illusion de l'inclusion

- Contribuer à Blender exige de coder en Python ; à OpenFisca, de manipuler du droit et des scripts.
- **Le design libre et en commun n'est pas démocratique, il est technocratique.** L'outil ouvert force le designer à devenir ingénieur ; la gouvernance crée une nouvelle fracture qui exclut les profils graphiques ou ergonomiques au profit des profils techniques.

### 2. Le mythe du consensus esthétique (la verticalité indispensable)

- Dans les *Open Movies*, la direction artistique reste contrôlée par un réalisateur avant la libération des fichiers.
- La subjectivité d'un design de qualité ne survit pas à la gouvernance horizontale : le design contributif intégral mène au **chaos visuel**. Il faut d'abord accepter une [[Dictature bienveillante|dictature bienveillante]] (direction artistique verticale en amont) ; le commun n'intervient qu'en aval, pour la distribution et la modification individuelle.
- Réalité économique : une typographie libre ou un design system demandent des centaines d'heures de travail qualifié. **Si la ressource est gratuite, qui finance le temps de conception ?** S'appuyer sur le travail gratuit ou l'auto-exploitation des designers n'est pas soutenable.

### 3. L'IA (le syllabus demande d'en parler)

- Les designers s'auto-exploitent pour maintenir typographies et modèles, tandis que les IA génératives (accessibles via Hugging Face) s'entraînent sur ces données.
- Les licences libres (Creative Commons, GPL, voir [[Copyleft]]) deviennent **obsolètes et agissent comme des failles économiques** : pensées pour le partage entre humains, elles ne protègent pas de l'entraînement des IA (voir [[Licence anti-IA]], [[Droit d'auteur et IA]]).
- Certains domaines, comme celui de l'État, ne tolèrent pas les hallucinations probabilistes pour calculer des impôts : ils ont besoin du déterminisme d'OpenFisca.
- Contrairement à la création visuelle, précarisée par l'IA, le design des règles (design d'information, *legal design*) est **protégé par sa propre complexité**. Le danger pour OpenFisca n'est pas que l'IA remplace le commun, mais que les contributeurs utilisent des LLM pour traduire les lois en code et **perdent la capacité humaine d'auditer** leur propre système.

## Points à signaler

- Les affirmations sur le fonctionnement de ces projets viennent de l'étudiant et ne sont pas sourcées dans la note ; l'idée de « dictature bienveillante » est une thèse du groupe.
- Une partie du texte semble produite par un outil de génération de texte (adresse au lecteur, autocommentaire) : à vérifier avant toute citation dans le dossier.

Aucun point à vérifier.
