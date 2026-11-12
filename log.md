# Journal du wiki

Historique chronologique. On ajoute à la fin, sans réécrire les entrées passées.

Dernières entrées : `grep "^## \[" log.md | tail -5`

## [2026-11-04] import | Premier import depuis Drive

176 documents de `gdrive:CY Tech` convertis dans `Cours/`. Les PDF et PPTX ne sont pas encore traités.

## [2026-11-04] transcription | Bilinear Algebra

169 images de `Year 2/Bilinear Algebra` transcrites. Deux passages marqués « À vérifier » : `det A = (adj A)A` dans `Chp 0c - Determinants`, et le tableau des symétries dans `Chp 0a - Linear combination`.

## [2026-11-04] ingest | Concepts de Bilinear Algebra

26 notes créées dans `Concepts/`. Pas de résumés de sources. Ingestion partielle, antérieure au schéma actuel.

## [2026-11-04] transcription | Lancement du script par lots

`.outils/transcrire.py` traite les autres matières. Le lancement était en cours à l'écriture de cette entrée : 1 452 transcriptions enregistrées, dont 7 refaites après le problème des captures de terminal.

## [2026-11-04] schema | Passage à une organisation en wiki

Consignes du coffre réécrites autour de trois couches (sources, wiki, schéma) et de trois opérations (ingest, query, lint). Création de `index.md` et de ce journal.

## [2026-11-05] transcription | Fin des transcriptions

Les 1 881 images des documents importés sont traitées : 3 fichiers vides, 367 transcriptions avec une mention « À vérifier ». Quatre images bloquées par le filtre de l'API ont été écrites à la main, dont 2 sous forme de résumé. Les PDF et PPTX restent à traiter.

## [2026-11-05] import | Reconversion après correctif

9 images de `Year 1/Outil Maths/Cours/Chapitre 5 - Complexes` ne s'affichaient pas à cause d'un `]` dans leur texte alternatif : le filtre retire désormais ce texte. Contrôle : 2 078 images insérées, aucune cassée.

## [2026-11-05] ingest | chp 1 - Orthogonality (test)

Première intégration, pour valider le niveau de détail. Créés : 1 résumé, 1 page de matière et 6 concepts (Norme, Complément orthogonal, Famille orthogonale, Projection orthogonale, Matrice orthogonale, Régression linéaire). Complétés : Moindres carrés, Orthogonalité, Produit scalaire, Procédé de Gram-Schmidt, Factorisation QR. 5 points à vérifier dans le cours, dont un écart entre le texte et la figure sur le projeté de $\mathbf{b}$.

## [2026-11-05] ingest | Fin de Year 2/Bilinear Algebra

Niveau de détail validé sur le test. 7 notes intégrées, soit 8 sur 8 pour cette matière. Créés : 7 résumés et 6 concepts (Système linéaire, Espace engendré, Injectivité et surjectivité, Produit matriciel, Sous-espaces fondamentaux, Espace propre). Les 21 concepts restants de l'import d'origine sont complétés et ont désormais un en-tête complet. 16 nouveaux points à vérifier dans le cours, dont deux prioritaires : la définition de « negative definite » et l'usage de la forme échelonnée pour trouver les valeurs propres.

## [2026-11-05] import | Dossier raw et dessins récupérés

Le miroir de Drive passe dans `.raw/`, exclu de git. La conversion ignorait les dessins groupés de Google Docs : 82 groupes dans 176 documents, soit 97 images et le texte de 45 encadrés absents des notes. Le script les remplace désormais par leurs images et une ligne « Texte du dessin ». La disposition et les flèches restent perdues. Les 97 images sont transcrites, ce qui porte le total à 1 978.

## [2026-11-05] ingest | Year 1/Algèbre Linéaire

7 notes intégrées. Créés : 7 résumés, 1 page de matière et 3 concepts (Morphisme, Changement de base, Somme directe). 18 concepts communs complétés, sans doublon. 18 points à vérifier dans le cours. Des formules manquent dans chp4, chp5 et chp6 : l'export de Google est vide à ces endroits, à vérifier dans les Google Docs.

## [2026-11-05] ingest | Reprise de Bilinear Algebra après récupération des dessins

26 images récupérées et les textes des dessins relus. Deux remarques du wiki étaient fausses et sont retirées : la formule de la décomposition spectrale figure bien dans le cours (image non importée jusqu'ici), et un dessin de chp4 corrige la borne de la somme de $c_{ij}$. Ajouts : $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$, $\text{proj}_W\,\mathbf{y} = UU^T\mathbf{y}$ et le développement colonnes-lignes.

## [2026-11-05] import | Retrait d'un dossier administratif

Un dossier de documents administratifs est retiré de `.raw/`, de `Cours/` et de `.transcriptions/`, et exclu des prochaines mises à jour depuis Drive. Il reste 175 notes, 53 PDF et 1 976 transcriptions.

## [2026-11-05] ingest | Year 2/Analyse dans Rn

4 notes intégrées. Créés : 4 résumés, 1 page de matière et 12 concepts, de Boule et voisinage à Difféomorphisme. Norme complétée. 19 points à vérifier dans le cours, dont cinq prioritaires, notamment « lipschitzien ⇔ uniformément continue » et le test en coordonnées polaires, qui ne suffit pas à prouver une limite.

## [2026-11-05] ingest | Year 1/Analyse Maths et Year 2/Analyse

5 notes intégrées. Créés : 5 résumés, 2 pages de matière et 5 concepts (Dérivabilité, Comparaison asymptotique, Développement limité, Intégrale, Primitive). 15 points à vérifier dans le cours. Deux mentions « À vérifier » de transcriptions sont de fausses alertes, signalées dans le résumé de chp5. 14 PDF de ces deux matières (réels, rappels, TD, contrôles, intégrales multiples) restent absents du wiki.

## [2026-11-05] ingest | Toutes les autres matières, par lots

151 notes intégrées en 7 lots parallèles : Probability, Statistics, Data analysis, data mining, IA, Outil Maths, Algo Maths, Séries, graph theory, Operating System, Algo, Java, C++, Data base, Computer Network, Philosophie, SHS, HDA, Communication orale, Anglais, écriture narrative, Culture du vivant, Corps à l'oeuvre, Dessein au cube, Peinture, Projets design, workshop, ligue football, management de l'innovation, projet court. Créés : 149 résumés, 35 pages de matière et 128 concepts. Les notes en double sont regroupées dans un seul résumé. Fusion : deux concepts écrits en même temps (Économie circulaire, Complexité algorithmique) sont réunis, et les variantes `process` et `top of mind` sont retirées car elles créaient de faux liens. Contrôle : 285 nouveaux liens échantillonnés par concept. La plupart des images n'ont pas été rouvertes dans ces lots. Deux notes ne sont lues qu'en partie : l'entretien de SHS en Year 4 et Global Exam Vocab.

## [2026-11-05] import | Retrait de notes personnelles

10 notes personnelles sont retirées de `.raw/`, de `Cours/`, de `.transcriptions/` et du wiki, et exclues des prochaines mises à jour depuis Drive : un dossier de Dessein au cube, une fiche, les devoirs de Peinture et une note d'instructions. Six résumés sont renommés pour ne plus porter de nom de personne. Il reste 165 notes et 163 résumés.

## [2026-11-06] import | Retrait de trois notes isolées

Trois notes sans lien entrant, dont deux portaient un nom de personne, sont retirées de `.raw/` et de `Cours/` et exclues des mises à jour. Leurs résumés restent. Il reste 162 notes.

## [2026-11-06] ingest | Documents PDF et PPTX

Les 53 PDF et 6 PPTX de `.raw/` sont résumés en 4 lots, soit 1 515 pages : 59 résumés, 15 concepts et 5 nouvelles pages de matière (Year 2 - SHS, Year 3 - Affordance, Year 3 - Projet courts, Year 3 - Sémiotique, Year 4 - culture du soin). Les documents sont lus par leur texte extrait, et une page n'est ouverte en image que si le texte est illisible ou douteux. Lectures partielles : les gros documents de diapositives (AlgoID1, AnalyseID1, td0slides, td1slides, TDSuites), text2 et text3 de SHS. Les liens vers trois fichiers dont le nom pose problème sont écrits en texte simple.

## [2026-11-06] ingest | Compléments des concepts

44 concepts existants complétés à partir des propositions des lots, surtout grâce aux documents PDF : Limite et continuité (version à une variable), Injectivité et surjectivité (applications ensemblistes), Arbre de décision (ID3, C4.5, CART), Limites planétaires (Rockström, Donut), etc. Portée élargie pour Injectivité et surjectivité (Outil Maths), Comparaison asymptotique (Séries), Récursivité (Algo Maths), Affordance (Sémiotique, Affordance) et Entretien semi-directif (SHS, Affordance). Un seul nouveau lien automatique dans les cours, vérifié.

## [2026-11-06] import | Mise à jour depuis Drive

Deux fichiers changés sur Drive, aucune image à transcrire. Nouvelle note `Year 4/Gestion financière`, rangée à la racine de l'année : résumé et page de matière Gestion financière (index) créés, sans concept (définitions d'une ligne), trois points à vérifier dont la définition du PNB. Note modifiée `Chp1 - intro to data mining` : seul ajout repéré, la phrase reliant le classifieur à la matrice de confusion, reportée dans le résumé. L'index compte désormais 163 notes (le décompte de 165 n'avait pas suivi le retrait de trois notes isolées).

## [2026-11-06] ingest | Une page par notion nommée dans les cours

Règle choisie : toute notion nommée dans un cours a sa page, pour apparaître dans le graphe. Les 223 résumés (docx, PDF, PPTX) sont repassés en 8 lots, avec vérification dans la note de `Cours/` ou le document de `.raw/` : 1 443 notions relevées, fusionnées en 1 064 pages nouvelles (65 regroupent plusieurs relevés, Weka écarté) et 302 compléments de pages existantes. `Concepts/` passe de 201 à 1 265 pages. Les sous-notions qui n'étaient qu'un alias d'une page plus large ont leur page, et l'alias quitte la page parente, qui renvoie désormais vers elles (Arbre de décision vers Indice de Gini, ID3, CART ; Graphe non orienté vers 12 pages ; Logique propositionnelle, Sémiotique vers Sémiologie, etc.). « noyau » reste sur Espace nul : ses matières ne recoupent pas celles de Noyau.

Les erreurs apparentes des cours sont recopiées dans les sections « À vérifier » sans être corrigées (C : `if (a=3)`, `^`, taille d'un `int` ; OS : `/etc/passwd` et `/etc/shadow`, `ls -l`, crontab ; Outil Maths : De Morgan, antisymétrie ; Bauhaus, Hegel, etc.), ainsi que les désaccords entre sources (hauteur d'un arbre, seuil de l'approximation normale, nombre de limites planétaires dépassées). Les pages tirées d'un travail d'étudiant, d'un entretien ou d'un texte généré le disent. Les sources dont le nom de fichier porte un nom de personne sont citées en texte simple.

Reconversion : 1 271 nouveaux liens automatiques dans `Cours/`, vers 750 concepts, aucune alerte de collision. Échantillon de 70 liens relu ; deux faux liens corrigés en limitant `matieres` (« opérations élémentaires » en graph theory, « bande magnétique » d'une carte bancaire). Pages de `Matières/` et `index.md` mis à jour.

Restent ouverts : les liens vers `.raw/Year 1/Contrôles.pdf` et le PDF de management de l'innovation, dont le nom est en Unicode décomposé sur le disque, à vérifier dans Obsidian ; les noms de page à valider (Comatrice, Compact élémentaire, Littératie numérique) ; le doublon entre Matrice inversible et Théorème de la matrice inversible ; Nombre d'Armstrong et Nombre parfait sans définition, faute d'avoir lu les pages scannées de `Contrôles.pdf`.

## [2026-11-06] schema | Nouvelle arborescence : matières sans année, concepts par domaine

Le dossier `Sources/` disparaît : chaque matière a son dossier `Matières/<Matière>/`, avec sa carte `<Matière> (matière)` et ses résumés. Plus d'année dans les noms : Philosophie, SHS, Corps à l'oeuvre et Culture du vivant ont une seule carte, avec une section par année (46 cartes deviennent 41) ; Projet design garde deux dossiers, qualifiés par l'année, comme Projet courts (Year 3) et Projet court (Year 4). Les six résumés aux noms en double sont renommés avec leur matière (`Cours 1 - Peinture (résumé)`, `chp5 - Analyse Maths (résumé)`…). Les 1 265 concepts sont rangés en six domaines (Mathématiques 297, Informatique 395, Données et IA 154, Design 232, SHS et philosophie 114, Écologie et société 73), selon la matière où chaque notion apparaît en premier. Chaque résumé, carte et concept porte des tags `year1` à `year4`. `index.md` devient `Accueil.md` ; `log.md` et `À faire.md` passent dans `_suivi/`. `CLAUDE.md` et `/maj-cours` suivent.

Migration par script : 15 272 liens du wiki, aucun cassé ni ambigu avant comme après. Les tests passent, et une reconversion ne change aucune note de `Cours/`.

## [2026-11-06] schema | Miroir caché dans .raw/, résumés de séances renommés

Le miroir Drive passe de `raw/` à `.raw/`, qu'Obsidian n'affiche pas ; `maj.sh` et `convertir.py` suivent. Obsidian ne résout pas les liens vers un dossier caché : les 775 liens vers ses documents sont devenus du texte, chemin entre accents graves. Dans le nom des 37 résumés concernés, « cours » devient « séance » (`Séance 6 - T-Test (résumé)`, `Dernière séance (résumé)`), et `Matières/Cours BU/` devient `Matières/Séance BU/` ; les notes de `Cours/` gardent leur nom de Drive. Trois notes de `Cours/` (Prise parole Rendu final, Projet BLR, UNIX Commands - Semester report) ont été supprimées par l'utilisatrice, qui fera le tri plus tard ; leurs résumés restent, et 27 liens vers elles sont cassés en attendant.

## [2026-11-06] ingest | Fin de deux résumés incomplets

`Entretien sur l'open source` : transcription lue en entier, le résumé ajoute la façon de juger un dépôt (mises à jour, communauté, étoiles), la diffusion par le bouche-à-oreille et les réseaux sociaux, l'absence de licence, et la contribution par demande de fusion. Nouveau concept . `Global Exam Vocab` : les quelque 285 entrées sont classées par chapitre ; sept définitions discutables relevées (hue, tertiary colours, golden ratio, aspect ratio, die cut, tolerance, anti-ornate), la définition d'aspect ratio aussi signalée sur 

## [2026-11-06] ingest | Résumés complets, avec figures

Les 216 résumés des notes de `Cours/` et des documents de `.raw/` deviennent des fiches complètes (`complet: true`), pour réviser sans ouvrir la source : définitions, théorèmes, formules, méthodes, code, exemples et exercices corrigés quand le document le permet. Ils passent d'environ 100 000 à 376 000 mots. Sont écartés : les résumés des trois notes supprimées par l'utilisatrice, les deux résumés d'entretiens SHS de Year 3 dont la note n'existe plus, et l'entretien sur l'open source, déjà complet. 841 images intégrées : 498 reprises des notes de `Cours/` sans copie, 343 créées depuis les PDF et PPTX dans 17 dossiers `Matières/<Matière>/images/` (47 Mo). Les PDF scannés (Contrôles, AnalyseID1, Chap1-reels, exercices de logique, Chp9) sont lus sur l'image ; `Co complétées. Les schémas de formes PowerPoint, non extractibles faute de LibreOffice, sont décrits en texte.

Nouvelles erreurs de cours relevées et notées, sans correction, dont : majoration de $\sum 1/k^2$ (AnalyseID1), terme d'ordre 4 du corrigé du TD5 (ex. 18c), formules trigonométriques de td0slides, calcul d'âge et date d'Al-Khowarizmi (AlgoID1), réseau de l'ACL (Computer Network), conjugué des complexes (Outil Maths). Textes signalés comme générés ou traduits par un outil : Synthese SHS GPT, Recherches SHS, encadrés de la séance 13 d'ACP, fiche ressources Santé au travail, text1 (DeepL), recherches femmes et foot. Restent à trancher avec l'utilisatrice : les images de ses rendus dont le chemin porte son nom (écartées pour TP3, intégrées pour Douze innovations), trois images d'IA portant le logo nominatif d'une intervenante, et trois faux liens automatiques (gamma distribution, sample median, matrice composée).

## [2026-11-07] schema | Images des fiches copiées dans Matières/

Décisions de l'utilisatrice : les images de ses rendus s'intègrent même si leur chemin porte son nom (19 captures ajoutées au TP3) ; trois images de la séance 1 d'IA portant le logo nominatif d'une intervenante sont remplacées par une description ; les PNG lourds restent tels quels. Pour pouvoir cacher `Cours/` plus tard, les 514 images que les fiches intégraient depuis `Cours/…/medias/` sont copiées dans `Matières/<Matière>/images/`, nommées d'après leur fiche (`AVL momo - image3.png`), sans nom de personne ; 87 fiches réécrites. Les images du wiki pèsent désormais 123 Mo. Les noms de dossiers utilisés par les scripts sont centralisés dans `.outils/chemins.py`, et `maj.sh` refuse un nom de miroir vide ou suspect avant `rclone sync`.

## [2026-11-07] transcription | Vérification des 1 838 transcriptions sur l'image

Chaque transcription non vide dont l'image existe encore est comparée à son image, en 12 lots. 39 erreurs de lecture corrigées, dont 10 qui changent le sens : les adresses `127.0.1.1` du TP3 (deux captures), l'`exit(0)` du processus F (TP 08), trois limites en polaires d'Analyse dans Rn (deux images portent $(0,\theta)$, une $(0,0)$), la médiane $\tilde{x} = 92{,}17$ de Statistics (et non la moyenne), le troisième couple de la validation croisée en data mining, un code couleur et un prompt en IA, un facteur d'équilibre d'arbre AVL. Les 29 autres sont des mots mal lus, des descriptions de figure et des coquilles du cours que la transcription corrigeait sans le dire ; elle reproduit désormais l'image, la coquille signalée. Les corrections sont reportées dans les fiches et les concepts qui les avaient recopiées ; trois pages reprochaient à tort une erreur au cours de Statistics. Une image (« Critical Evaluation », Statistics Chp1) reste à vérifier à la main : le filtre de contenu bloquait sa vérification. La reconversion des notes de `Cours/` n'a pas été lancée.

## [2026-11-07] schema | Plus de notes converties : les fiches lient le miroir Raw/

Le miroir de Drive redevient visible sous `Raw/`, et Obsidian affiche ses docx et pptx (`showUnsupportedFiles`). Les liens du wiki vers les notes de `Cours/` mènent désormais à leur fiche, avec le même texte affiché (2 000 liens) ; dans une fiche, le lien vers sa propre note devient le lien de son document dans `Raw/` (308), et `sources` des six fiches sans lien reçoit celui de son document. Les 778 mentions `.raw/…` d'un fichier sont devenues des liens aw/ ; les mentions d'un dossier, et le PDF dont le nom contient des crochets, restent en texte. Mesure après migration : aucun lien vers `Cours/`, aucun cassé ni ambigu, 1 092 liens vers `Raw/`. Ce journal garde ses mentions `.raw/` d'origine.

Décision de l'utilisatrice : `Prise parole Rendu final`, `Projet BLR` et `UNIX Commands - Semester report` sont exclus du miroir (`exclusions.local`) ; les 21 liens vers ces notes mènent à leur fiche. Les deux fiches d'entretiens SHS de Year 3 citent leur document comme exclu du miroir.

Nouvelle chaîne de mise à jour : `maj.sh` synchronise `Raw/` en gardant les anciennes versions, compare le miroir avant et après, convertit les documents changés et transcrit leurs images hors du coffre, puis écrit un lot que `/maj-cours` intègre au wiki (fiche corrigée d'après les changements d'un document modifié, jamais réécrite). `convertir.py "Raw/…docx"` permet de relire un document Word. Les liens automatiques vers les concepts disparaissent avec `Cours/` ; `aliases` et `matieres` servent à repérer les concepts présents dans un document changé. `CLAUDE.md` et `/maj-cours` suivent. `Cours/` reste sur le disque jusqu'à sa suppression.

## [2026-11-07] import | Mise à jour depuis Drive

Premier essai de la nouvelle chaîne, sur un document modifié par l'utilisatrice : `Year 4/data mining/Chp1 - intro to data mining`. Seul changement : « maiste exacte. Google avait renuméroté les 55 images du document sans en changer le contenu : le lot désigne désormais les images par l'empreinte de leur contenu dans les changements, pour ne montrer que les vraies modifications.

## [2026-11-07] schema | Suppression de Cours/

Après vérification qu'aucun lien ni aucune image du wiki n'y menait, l'utilisatrice a retiré `Cours/` du coffre (173 Mo, 2 046 fichiers). Mesure sans lui : aucun lien cassé ni ambigu, les 857 images intégrées sont toutes daui disait intégrer une image depuis `Cours/`, est corrigée.

## [2026-11-07] schema | Fusion de deux domaines de concepts

À la demande de l'utilisatrice, `Concepts/SHS et philosophie` (115 concepts) et `Concepts/Écologie et société` (73) fusionnent en `Concepts/Sciences humaines` (188), sans doublon de nom. Les liens visant les concepts par leur nom, aucun n'est touché. `CLAUDE.md` passe à cinq domaines ; les deux groupes de couleur du graphe sont à réunir en un seul dans Obsidian.

## [2026-11-07] schema | Concepts rangés par discipline

La frontière entre `Données et IA` et `Informatique` n'était pas claire, et la règle « matière de première apparition » séparait les probabilités de Year 2 (dans `Mathématiques`) des statistiques de Year 3 (dans `Données et IA`). Sur décision de l'utilisatrice, les concepts sont désormais rangés par discipline, et `Données et IA` disparaît :

- `Probabilités et statistiques` (nouveau, 107) : les 77 concepts de statistique de `Données et IA`, plus 30 de `Mathématiques` (probabilités et dénombrement) ;
- `Informatique` (461) : 66 concepts de technique de l'IA, d'apprentissage automatique et d'outils R ;
- `Sciences humaines` (196) : 8 concepts sur les enjeux de l'IA (deepfake, droit d'auteur, consommation énergétique…) ; `Hallucination (IA)` et `IA générative` y restent ;
- `Mathématiques` (270) : `Trace d'une matrice`, `Fonction Gamma`, `Extremum local d'une fonction de deux variables`.

Aucun lien touché : ils visent les concepts par leur nom. La règle de `CLAUDE.md` est réécrite. Les groupes de couleur du graphe sont à refaire dans Obsidian.

## [2026-11-07] schema | Fin du tag nomme : définitions des concepts nommés

Sur demande de l'utilisatrice, le tag `nomme` disparaît. Chacun des 162 concepts qui le portaient commence désormais par une définition, suivie de `## Dans le cours`, qui garde le texte d'avant intact. Pour 161 d'entre eux, aucune fiche ne définit la notion : la définition est marquée « complément, hors du cours ». Pour Problème indécidable, le cours (AlgoID1) donne bien la définition : elle est reprise d'après la fiche, et la phrase « nommé sans définition » est corrigée. Format validé sur quatre pages (IPv6, Réseau de neurones, Santé au travail, Cahier des charges), puis appliqué en trois lots. `CLAUDE.md` décrit la nouvelle règle.

Compléments à relire, faute de définition établie ou de vérification sur un texte officiel : Gestelligence (interprétation du mot), Capital d'attractivité, IA sémantique, Tournant relationnel, Boussole des possibles, CSRD (calendrier), Qualité de vie au travail et Harcèlement moral (références juridiques), Ethos de classe, Système nerveux sympathique et parasympathique.

Manques repérés, non traités : Effet de bord (aussi en Year 1, AlgoID1), Suite arithmétique (aussi en Year 4, Graph theory), Diagramme de Gantt (fiche de Management de l'innovation), Savoirs situés et Interaction homme-machine (fiche Ethnographie visuelle), Design des politiques publiques, Fordisme, Stigmatisation : des fiches y renvoient sans que la page les cite en retour.

## [2026-11-07] lint | Relecture des 162 définitions et liens retour

Manques corrigés : les neuf pages ci-dessus citent désormais les fiches qui renvoient vers elles (« Dans le cours », `Résumés`, `sources`), avec les années manquantes ; `matieres` élargi pour Diagramme de Gantt, Fordisme, Stigmatisation et Conception centrée utilisateur, qui sinon ne seraient pas repérés dans les documents de ces matières.

Relecture critique des 162 définitions, avec vérification sur le web pour les points douteux. Quatorze définitions corrigées :
- Informatique : NFS, Lien symbolique et Secteur défectueux signalent désormais l'écart avec le sens que leur donne le cours ; Erreur de segmentation ne laisse plus croire que tout débordement de tableau la déclenche.
- Design : Bullshit jobs (traduction française « jobs à la con »), Fauvisme (le mot de Vauxcelles, « Donatello chez les fauves »), Santé au travail (« travailleurs », comme l'article L. 4121-1), Responsabilité sociétale des entreprises (définitions de 2001 et de 2011 distinguées), Système nerveux sympathique et parasympathique (anatomie du nerf vague distinguée de la lecture polyvagale), Capital d'attractivité (mis au conditionnel).
- Sciences humaines : CSRD (report en 2025, puis périmètre réduit en 2026 par la directive Omnibus I), Pont aux ânes, Boussole des possibles (les huit vents nommés), Masculinité hégémonique (formulée dans les années 1980).

Restent incertains : Gestelligence (aucune occurrence hors du cours), ReFS (rapport à NTFS selon les versions de Windows), les seuils de Devoir de vigilance (simplifiés), le numéro de la directive Omnibus I (non vérifié sur EUR-Lex, et non cité dans la page).

## [2026-11-07] schema | Matières rangées par domaine

Les 43 dossiers de `Matières/` sont rangés dans les cinq domaines de `Concepts/` : `Matières/<Domaine>/<Matière>/`.
- Mathématiques (9) : Algèbre linéaire, Algo Maths, Analyse, Analyse dans Rn, Analyse Maths, Bilinear Algebra, Contrôles, Outil Maths, Séries.
- Probabilités et statistiques (3) : Data analysis (Thanos), Probability, Statistics.
- Informatique (10) : Algo, C++, Computer Network, Data base, Data mining, Graph theory, IA, Java, Ligue football, Operating System.
- Design (11) : Affordance, Corps à l'oeuvre, Culture du soin, Dessein au cube, HDA, Peinture, Projet courts (Year 3), Projet design (Year 1), Projet design (Year 2), Sémiotique, Workshop.
- Sciences humaines (10) : Anglais, Communication orale, Culture du vivant, Écriture narrative, Gestion financière, Management de l'innovation, Philosophie, Projet court (Year 4), SHS, Séance BU.

Aucun lien ne passait par le chemin d'une matière : rien de cassé (contrôle de tous les liens et images du wiki). Chemins en texte corrigés dans 0 - rappels pdf (résumé) et 4 - Discrete random variables (résumé). `CLAUDE.md`, `/maj-cours` et Accueil (liste par domaine, et « cinq domaines » au lieu de six pour `Concepts/`) mis à jour. `maj.py` parcourt `Matières/` en profondeur : il retrouve les 223 fiches et oriente un document nouveau vers le dossier de sa matière.

## [2026-11-07] lint | Tags réduits aux années

Seuls `year1` à `year4` restent comme tags.
- `nomme` retiré de 31 concepts que l'entrée « Fin du tag nomme » avait manqués. Aucun n'a encore la définition prévue par `CLAUDE.md` (« **Définition (complément, hors du cours)** » puis `## Dans le cours`) : ils gardent l'ancien texte « Nommé dans … sans définition ». Ce sont AlphaGo Zero, Apprentissage non supervisé, Apprentissage par renforcement, Apprentissage profond, Conférence de Dartmouth, Deep Blue, Deepfake, Domaine public, ELIZA, Entraînement et inférence, Expressionnisme abstrait, Fonctions hyperboliques, IA hybride, IA malveillante, Impressionnisme, Logic Theorist, Modèle de diffusion, Neurone de McCulloch-Pitts, Outrenoir, Perceptron, Petit réacteur modulaire, Réseau de neurones convolutif, Réseau de neurones récurrent, Street art, Surréalisme, Système expert, Test de Turing, TPU, Transformer (IA), Transistor, Variable indicatrice.
- Les autres tags venaient de `#` du contenu des cours, lus comme des tags par Obsidian : mots-dièses de la courbe du deuil (2 - Culture du vivant (résumé)), clés étrangères du schéma relationnel (Rapport du projet Ligue Football), slogan « \#SingleNotSorry » (2 - sémiotique (résumé)), hashtag de l'histoire (1 - écriture narrative (résumé)). Échappés en `\#` : le texte affiché ne change pas.

## [2026-11-07] schema | Matières/ renommé en Cours/

Le dossier des cartes de matière et des fiches s'appelle désormais `Cours/` : `Cours/<Domaine>/<Matière>/`. À ne pas confondre avec l'ancien `Cours/` des entrées précédentes, qui contenait les notes converties et a été retiré du coffre : avant cette entrée, `Cours/` désigne ces notes, et `Matières/` le dossier actuel.

`.outils/chemins.py` (`MATIERES = "Cours"`), `CLAUDE.md`, `/maj-cours`, Accueil et les deux fiches qui citent leur dossier d'images (0 - rappels pdf (résumé), 4 - Discrete random variables (résumé)) mis à jour. Aucun lien ne passait par ce chemin ; tests verts, et `maj.py` retrouve les 223 fiches. Filtres et groupes de couleur d'Extended Graph passés de `path:Matières/…` à `path:Cours/…`.

## [2026-11-07] schema | Dossiers de domaine qualifiés par (concept) et (cours)

Les dix dossiers de domaine sont renommés pour se distinguer dans le graphe : `Concepts/<Domaine> (concept)/` et `Cours/<Domaine> (cours)/` (`Concepts/Design (concept)`, `Cours/Design (cours)`). Aucun lien ni script ne dépendait de ces noms ; tests verts, `maj.py` retrouve les 223 fiches. `CLAUDE.md`, `/maj-cours`, Accueil, les deux fiches qui citent leur dossier d'images et les groupes de couleur d'Extended Graph (requêtes désormais entre guillemets, à cause des parenthèses) mis à jour.

## [2026-11-07] schema | Noms des cartes, des dossiers de matière et des fiches

Renommages faits par l'utilisatrice dans Obsidian, complétés et répercutés dans les liens :
- cartes de matière : `<Matière> (matière)` devient `<Matière> (index)` (41 cartes) ;
- dossiers de matière : `<Matière>` devient `<Matière> (cours)`, avec le nom court de la matière (`OS (cours)`) ; les projets de design sont regroupés par année dans `Projet year N (cours)`, Workshop compris ;
- fiches : `N - Titre (résumé)`, sans « chp » ni « Séance » (`Chp1 - Intro Java` → `1 - Intro Java`, `Séance 6 - T-Test` → `6 - T-Test`, `OS - chp 1` → `1 - OS`) ; un document sans titre prend le nom de sa matière (`2 - Peinture`, `1 - Algèbre linéaire`) ; `0 - rappels pdf` reçoit le suffixe « (résumé) », sans lequel `maj.py` ne la voyait pas ;
- Algo Maths est rattachée à Algo : ses fiches passent dans `Algo (cours)` et sa carte devient la section `## Year 1` d'Algo (index).

Les liens vers les fiches et les cartes renommées sont réécrits (plusieurs milliers) ; les images gardent leur ancien nom. Règles de nommage et de rangement inscrites dans `CLAUDE.md` et `/maj-cours`.

## [2026-11-07] lint | Fiches triées, liens réparés, concepts reliés

L'utilisatrice a supprimé les fiches qui ne résument pas un support de cours : TD, exercices et corrigés, contrôles et DS, devoirs et rendus, entretiens, notes de recherche, anglais, projet de la ligue de football (64 fiches, 159 restent). Deux fiches ont été fusionnées dans une autre : la fiche ressources de Santé au travail dans Santé au travail (résumé), et `Culture Vivant SÉANCE 2 EXPLICATION` à la fin de 2 - Culture du vivant (résumé) (son document est ajouté à `sources`).

Réparations :
- 1 231 liens cassés, vers 82 fiches ou cartes disparues : retirés des listes (« Résumés », Accueil, tableaux des cartes) ; ailleurs, remplacés par le lien du document de `Raw/`, ou par son nom en texte s'il est exclu du miroir ou porte le nom d'un tiers ;
- 15 images restaurées depuis git (`AlgoID1`, `Reyou`), restées dans des dossiers supprimés ; 134 images que plus aucune page n'utilisait supprimées ;
- 4 documents de `Raw/Year 1/Dessein au cube`, supprimés par erreur dans le coffre, remis en place depuis la corbeille ;
- cartes, Accueil et décomptes mis à jour (38 matières, 159 résumés).

Concepts : 148 n'avaient plus de fiche. 128 sont reliés à une fiche, dont une partie par rapprochement, marqué « Résumés (rapprochement, complément hors du cours) » ; 20 sont supprimés à la demande de l'utilisatrice (vidéo et animation, astronomie, débats de Communication orale, gestion de projet), ce qui laisse 1 246 concepts.

Vérifié : `maj.py` indexe les 159 fiches ; tous les PDF du Drive sont dans `Raw/`, sauf les 8 du dossier `Year 2/Administration`, exclu exprès (c'était l'écart de PDF relevé à l'import).

## [2026-11-07] lint | Mentions « À vérifier » traitées et retirées

Toutes les mentions « À vérifier » du wiki (sections « À vérifier », « Points à vérifier », « Points à vérifier dans le cours », encadrés et renvois dans le texte) sont traitées puis retirées : 620 pages de `Concepts/` et de `Cours/`, 1 367 points. Critères de l'utilisatrice : on vérifie sur la source (image d'origine, document de `Raw/`) les points qui touchent une formule, une définition exacte, du code, ou une lecture incertaine ; on efface sans vérifier les points mineurs (notion citée sans définition, complément hors du cours, orthographe, date, vocabulaire).

Issues :
- 448 erreurs du cours confirmées, notées dans une nouvelle section `## Erreurs du cours` en fin de page (269 pages) ;
- 218 doutes levés (mention supprimée, page complétée au besoin) ;
- 22 erreurs du wiki corrigées, dont le schéma « droit et morale » lu à l'envers (Droit et morale, 2 - philo (résumé)) et la définition de l'ethos de classe, présente dans text3.pdf ;
- 664 points mineurs effacés ;
- 15 points non tranchés, mention retirée quand même : surtout des formules ou des sections absentes des docx eux-mêmes (Algèbre linéaire chp4 et chp6, perte probable à l'export depuis Google Docs), des images coupées (Vector Space, Orthogonality), des sources exclues du miroir (entretiens SHS) ou absentes (`00_inegalites.pdf`, `formtrig.pdf`).

Règle inscrite dans `CLAUDE.md` (section « Fiabilité ») : plus de mention « À vérifier » dans le wiki ; un doute se tranche sur la source, une erreur du cours va sous « Erreurs du cours ». Accueil : compteurs de points à vérifier retirés. Contrôlé : aucune mention restante (hors verbe ordinaire), aucun lien cassé ni page orpheline introduits.

## [2026-11-07] lint | Liens, concepts, sources, rangement et manques

Contrôle demandé sur les liens, les concepts, les sources, le rangement et les manques, sans la cohérence entre pages. 1 244 concepts, 159 fiches, 38 cartes.

Sans anomalie : aucun lien cassé (les 8 relevés sont la syntaxe Bash `[[ … ]]` dans du code), aucun lien ambigu, toutes les pages dans `Accueil.md`, en-têtes complets (type, tag d'année, sources), aucune fiche hors de sa carte, aucune image inutilisée, aucun doublon de titre.

Corrigé : trois concepts sans lien entrant, Contrainte d'intégrité, Jointure externe et Expression CASE, sont maintenant liés depuis Langage SQL.

Soumis à l'utilisatrice :
- deux fiches mal nommées, à renommer dans Obsidian : `4 - Inferential statistics 3(résumé)` (espace manquante) et `3 -Invertible matrix theorem (résumé)` ;
- 49 concepts dont la seule source est un document exclu du miroir (47 du dossier Anglais de Year 2), dont six sans lien entrant ;
- des concepts à changer de domaine (Git, Chaîne de caractères, Recherche dichotomique, Moyenne empirique, notions de santé au travail et d'économie rangées en Design…) ;
- un doublon probable : Conception centrée sur l'humain et Conception centrée utilisateur ;
- environ 100 mentions de concepts existants non liées dans les fiches.

## [2026-11-07] schema | Fiches renommées sans « (résumé) »

Les 159 fiches de `Cours/` perdent le suffixe « (résumé) » (`6 - T-Test (résumé)` → `6 - T-Test`) ; liens et textes affichés réécrits dans tout le wiki, aucun lien vers une fiche cassé. `4 - Inferential statistics 3(résumé)` devient `4 - Inferential statistics 3`. `Santé au travail (résumé)` devient `Santé au travail (Projet year 3)`, le concept Santé au travail portant déjà ce nom. `maj.py` repère désormais les fiches comme toute page d'un dossier de matière hors carte (`(index)` ou `type: matiere`) ; `CLAUDE.md`, `/maj-cours` et le suivi mis à jour. Les entrées précédentes du journal gardent les anciens noms.

## [2026-11-07] schema | Cartes de matière renommées en _index

Les cartes `<Matière> (index).md` deviennent `_index.md` dans leur dossier (37 cartes). Les noms n'étant plus uniques, tous les liens vers une carte passent par le chemin complet avec le nom de la matière affiché (`[[Algo (index)]]` → `[[Cours/Informatique/Algo/_index|Algo]]`, `\|` dans les tableaux) : 198 pages réécrites, aucun lien vers une carte cassé. La carte Workshop, seconde carte du dossier `Projet year 3`, est fusionnée dans celle de Projet design (Year 3) sous `## Workshop` ; ses liens visent cette section. `maj.py` écarte les cartes par le nom `_index.md` ; `CLAUDE.md` et Accueil mis à jour.

## [2026-11-07] ingest | Fiche ressources et brief de Santé au travail versés dans les concepts

Les deux PDF de Raw/Year 3/Projet courts restent cités en texte (leurs noms portent ceux de tiers), d'où leur absence de liens. 30 concepts créés dans `Concepts/Design/`, à côté des concepts du même projet : Souffrance psychique, Santé mentale, Stress au travail, Facteurs de risques psychosociaux, Conflit de valeurs, Sens au travail, Gouvernance partagée, Aménagement de poste, Temps partiel thérapeutique, Retour au travail et maintien en emploi, Psychologue du travail, Service de prévention et de santé au travail, Comité social et économique, Syndicat, Obligation de sécurité de l'employeur, Art-thérapie, Sophrologie, Méditation, Soins énergétiques, Cellule d'écoute, Prévention du suicide, Tabous au travail, Grande cause nationale santé mentale, Innovation sociale, Projet pilote, Anact, INRS, Catégories d'entreprises, Secteurs d'activité, Keynésianisme. Définitions en complément, hors du cours (la fiche ne définit rien), puis toutes les ressources de la fiche rattachées à leur notion. Enrichis : Burn-out (ouvrages, programmes, vidéos), Risques psychosociaux, Qualité de vie au travail, Santé au travail (table des sept thèmes ; alias « obligations de l'employeur » passé à la nouvelle page), Prévention primaire, secondaire et tertiaire, Postvention, Stigmatisation, Harcèlement moral, Bienveillance organisationnelle, Charge mentale, Ergonomie, Bullshit jobs, Fordisme. Fiche Santé au travail (Projet year 3) : champ lexical et sections reliés aux concepts, titre « Fiche ressources » à la place des lignes vides, nature du texte reformulée. Carte de Projet design (Year 3) et Accueil mis à jour.

## [2026-11-07] import | Mise à jour depuis Drive

Lot de 20 documents. Déplacés (renommés sur Drive pour ne plus porter de nom de tiers) : les deux PDF de Raw/Year 3/Projet courts deviennent `Santé au travail - brief.pdf` et `Santé au travail - fiche ressources.pdf`. Les citations en texte sont remplacées par de vrais liens : fiche Santé au travail (Projet year 3) (`sources` et introductions), 51 concepts ; Accueil ne mentionne plus l'exception. Les 17 documents « ajoutés » (Analyse Maths, Communication orale, Dessein au cube, SHS, ligue football) étaient déjà liés au même chemin dans le wiki : rien à écrire. Le document modifié `Chp1 - intro to data mining.docx` a un texte et des images identiques après conversion : fiche inchangée.

## [2026-11-07] lint | Tri de Raw : 11 documents retirés du miroir

L'utilisatrice a supprimé 11 documents de `Raw/` en local (dossier inégalités alimentaires de Dessein au cube, Debats, écriture narrative, sujet database et readme de ligue football, une synthèse et une retranscription SHS). Ils restent sur Drive : chacun est ajouté à `.outils/exclusions.local` pour que la synchronisation ne les ramène pas ; Drive filtré et `Raw/` concordent (205 documents). Fiches supprimées à sa demande : 1 - inégalités alimentaires, 2 - pistes entrevues, 3 - Compte rendu (et son image), 1 - écriture narrative ; la carte d'Écriture narrative, sans plus aucun document, est supprimée. Les concepts qui en venaient sont gardés, leur source citée en texte « …, dans Raw/… (exclu du miroir) » : biais (cognitif, de confirmation, de disponibilité, de rétrospective), Consentement éclairé, Entretien semi-directif, Analyse thématique d'entretien, Structure narrative, Consigne d'écriture, Scénario (cinéma), et neuf concepts de base de données. Carte de Dessein au cube réécrite ; cartes Communication orale et SHS, Ethnographie visuelle et Accueil (catalogue, inventaire des sources) corrigés. Aucun lien cassé.

## [2026-11-07] lint | Contrôle mécanique du wiki

1 274 concepts, 155 fiches, 36 cartes, 205 documents de `Raw/`. Rangement par domaine, en-têtes (type, tags d'année, sources, maj), présence dans Accueil : conformes partout. Aucune page orpheline, aucune image non intégrée, aucun dossier vide, aucun doublon de concept. Corrigé : fiche `3 -Invertible matrix theorem` renommée `3 - Invertible matrix theorem` (7 pages et Accueil) ; source de Bel-air citée au format « …, dans Raw/… (exclu du miroir) ». Faux positifs écartés : la syntaxe shell `[[ … ]]` dans du code (Opérateur logique, Opérateur de comparaison, Shell dash, 8 - OS commandes sh), « à vérifier » employé comme verbe, « kernel » et « noyau » partagés par Noyau et Espace nul mais séparés par `matieres`, sigles courts tous limités à leurs matières. 46 documents sans fiche, tous TD, DS, DM, rendus ou notes, sauf deux soumis à l'utilisatrice (Python.docx en Algo Maths, cours TP1.docx en Operating System). Contradictions entre pages et manques non contrôlés : demandent une relecture du contenu.

## [2026-11-07] ingest | Fiches Python (Algo Maths) et cours TP1 (Operating System)

À la demande de l'utilisatrice, les deux documents signalés par le lint reçoivent une fiche. `0 - Python` (Algo, section Year 1 ; numéro 0 comme les autres fiches de l'ancienne Algo Maths) : note du 05/10/23 sur `range`, `for _ in`, `print(..., end="")`, avec l'erreur du cours sur `range(2, 10, 5)`. `1 - TP1` (Operating System, à la suite de 2 - TP2 à 5 - TP5) : aide sur les commandes, `sudo` et sudoers, mots de passe et `/etc/shadow`, clavier, nom d'hôte, `touch` et `mkdir -p` avec accolades, `chmod -R`, réponses aux questions du TP ; une capture intégrée (`1 - TP1 - image12.png`), le reste recopié en texte ; erreur du support sur `timestamp_timeout` (15 ou 30 minutes) vérifiée sur l'image. Concepts : 27 sources passées du document à la fiche `1 - TP1`, 3 à `0 - Python` (Fonction range, Boucle, Langage Python). Cartes d'OS et d'Algo, Accueil mis à jour. Bel-air laissé sans `complet: true`, à la demande de l'utilisatrice.

## [2026-11-08] import | Mise à jour depuis Drive

Lot du 2026-11-08 : 3 documents (2 ajoutés, 1 modifié), aucune image à transcrire.

- `Year 4/C++/chp4 C++.pdf` (ajouté, 32 diapositives) : fiche `4 - C++`, premier chapitre en C++ (bases, `std::cout`, classes, public/privé, trois constructeurs, get/set, surcharge de `-`, `+` et `<<`, `friend`, exercices `Point`, `Segment` et `Maze`). Les trois dernières diapositives n'ont pas de couche texte : code lu sur l'image, sortie ASCII du labyrinthe intégrée (`4 - C++ - p30.jpg`), recadrée sans l'invite du terminal qui portait un nom. Erreurs du cours : `Rayon` pour `rayon`, accès à `p3.x` privé hors de la classe, `i % 20` pour 21 colonnes.
- `Year 4/C++/chp4 prise de note.pdf` (ajouté, 9 pages manuscrites, sans texte extractible) : fiche `4 - Prise de note`, lue sur les images ; code des captures recopié en texte, sans les invites du terminal. Erreurs : `int x = 0;` dans un constructeur (variable locale), `float f = 13,3;`, `x + y` non initialisés.
- `Year 4/SHS/Prise de note SHS.docx` (modifié) : fiche `3 - Prise de note` mise à jour d'après les changements seulement (problématique retirée et deux nouvelles propositions, définitions d'intérêt général et d'open design, partie 4 retravaillée avec Poly Haven, Velvetyne et LAION-5B, ouverture fusionnée). La piste ChatGPT, notée « rayée » dans l'ancienne fiche, n'est pas barrée dans le document : corrigé. Concepts complétés : Intérêt général, Open design, Licences libres, Communs numériques, Licence anti-IA, Creative Commons, IA générative. Travail confié à un agent, relu ensuite.

Concepts créés (11, `Informatique`) : Langage C++, Programmation orientée objet, Classe et objet, Encapsulation (programmation), Constructeur (programmation), Accesseur et mutateur, Surcharge d'opérateurs, Référence (C++), Fonction amie (friend), Flux d'entrée-sortie (C++), Espace de noms (namespace). Concepts complétés : Langage C, Structure (struct), Passage par valeur, Variable non initialisée, GCC (`g++`, matière C++ ajoutée à `matieres`), Type primitif, Méthode spéciale Python, Fonctions printf et scanf, Tableau (programmation), Distance (matière C++ ajoutée à `matieres`). Carte C++ et Accueil mis à jour ; le compteur des résumés d'Accueil, qui annonçait 159 pour 157, est corrigé (159 avec les deux nouvelles fiches).

## [2026-11-08] schema | Enrichir le cours devient une priorité

À la demande de l'utilisatrice, dont les prises de note sautent des notions : chaque fiche est désormais complétée au-delà du document (notions manquantes, mécanismes, exemples), et les notions apportées par ces compléments reçoivent leur page de concept. Format choisi par l'utilisatrice : les ajouts vont directement dans le texte du cours, sans encadré, chacun terminé par une marque discrète `[[Complément hors du cours|ⓘ]]` qui mène à la page racine `Complément hors du cours` ; un extrait CSS la rend petite et grise en mode lecture. Suivi par le champ `enrichi:` des fiches. `CLAUDE.md` (section « Priorité : enrichir le cours », ingest, lint, fiabilité) et `/maj-cours` sont mis à jour.

## [2026-11-08] ingest | Gestion financière enrichie (fiche pilote)

`1 - gestion financière` complétée : les trois types de banque détaillés, le bilan (haut et bas), les marchés primaire et secondaire, actions et obligations, marché monétaire, la structure de la balance des paiements et le taux de couverture, le TEE et ses secteurs, les trois calculs du PIB, PIB nominal et réel, le passage du PNB au RNB, la marge, les coûts fixes et variables et le seuil de rentabilité. Concepts créés (9) : Banque centrale, Politique monétaire, Inflation, Produit national brut, Valeur ajoutée, Bilan comptable, Action et obligation, Création monétaire, Seuil de rentabilité. Concepts complétés : Types de banque (l'alias banque centrale passe à sa page), Produit intérieur brut (les alias PNB passent à sa page), Balance des paiements, Balance commerciale, Marché financier, Coût et prix, Opérations de haut de bilan. Carte et Accueil mis à jour. Niveau de détail soumis à l'utilisatrice avant d'enrichir les autres matières.

## [2026-11-08] ingest | Enrichissement de toutes les fiches de cours

148 fiches examinées et enrichies par 72 lots d'agents (projets de design, note de groupe SHS et Gestion financière exclus), 439 pages de concept écrites dont 172 créées, 7 noms de concept fusionnés comme doublons.

Contrôle après le chantier : texte des fiches +68 % (surtout les notes les plus minces) ; aucun encadré, aucun « À vérifier », `Raw/` intact ; aucune ligne de cours perdue, sauf une phrase de [[4 - imaginaires de l'automobile]] (Hammond) déplacée dans un complément, remise en place. Corrigés : 5 liens vers `Raw/` réécrits en Unicode composé (NFC) alors que les noms de fichiers de Drive sont décomposés (NFD) ; un lien vers [[Degrés de liberté]], page créée ; une ligne parasite « path: » dans [[4 - C++]] ; l'entrée « Erreurs du cours » de [[0 - Revision chapter]] sur $\sqrt{1+x}$, qui affirmait à tort une erreur de signe (seul $x^n$ manque). 1 467 concepts, aucun lien cassé, tous les concepts dans Accueil. 123 doutes des agents soumis à l'utilisatrice.

## [2026-11-08] lint | Correction des erreurs du cours

Nouvelle règle : les erreurs des cours ne sont plus relevées dans une section à part, mais corrigées directement dans le texte des fiches et des concepts. Chaque passage corrigé finit par la marque `[[Erreurs du cours|✎]]`, qui mène à la page racine [[Erreurs du cours]] ; celle-ci donne, page par page, ce que disait le cours, la version juste et sa source. Une source fiable du web (documentation, norme, manuel, organisme officiel) ou un calcul refait l'emporte sur la prise de note.

297 pages corrigées (fiches et concepts), 581 corrections marquées ✎. Les sections « Erreurs du cours », les encadrés « Écart dans le cours » et les phrases « En cas d'écart, le cours fait foi » sont supprimés partout ; les rubriques « À revoir » des cartes qui renvoyaient à des erreurs sont réécrites en points à maîtriser. Faits retirés faute de source : la Suède qui aurait banni Google ([[4 - Culture du vivant]]), une traduction de Hobbes attribuée à Tricaud ([[1 - philo]]), l'espace dans `id _saison` ([[Langage SQL]]).

Détail des corrections : [[Erreurs du cours]].

## [2026-11-10] import | Mise à jour depuis Drive

Le lot du 2026-11-08, déjà intégré, n'avait pas été clos : clos avant la synchronisation. Lot du 2026-11-10 : 10 documents (7 ajoutés, 1 modifié, 2 supprimés), une image transcrite.

- **Deux faux couples supprimé/ajouté**, au contenu identique, traités comme des déplacements : `Year 4/Culture du vivant/Culture du vivant - prise de note .docx` devient `Chp 1- prise de note .docx` ; `Year 4/Gestion financière.docx` passe dans le dossier `Year 4/Gestion Financière/`. Liens `sources` et `[[Raw/…]]` mis à jour dans les fiches [[4 - Culture du vivant]] et [[1 - gestion financière]] et dans 11 concepts.
- `Year 4/SHS/Prise de note SHS.docx` (modifié) : [[6 - design libre]] mise à jour (lien de l'intérêt général avec les communs numériques ; consigne de chercher des cas d'IA ayant « pillé » l'open design). Note de groupe : pas d'enrichissement.
- `Year 4/Culture du vivant/chp 2 - prise de note.docx` (ajouté) : fiche [[5 - Culture du vivant]] (d'abord nommée `2 - Prise de note`, renumérotée ensuite, voir plus bas), enrichie (33 compléments). Image de texte recopiée en texte (principes du réensauvagement). Corrections : 73 % des populations de vertébrés et non 70 % des mammifères disparus, 1750 repère conventionnel et non invention de la machine à vapeur, DDT sans rapport avec l'agent orange, émissions mondiales en hausse, électricité et non énergie décarbonée en France, aigle de Prométhée et *technè*, Calibri.
- Nouvelle matière `Year 4/histoire du design et interactions ` → [[Cours/Design/Histoire du design/_index|Histoire du design]] (Design, distincte de HDA). Quatre fiches enrichies : [[1 - Histoire du design]] (chp1 cours.pdf ; ses pages 21 à 60 reprennent le chapitre 2, seulement résumées), [[2 - Histoire du design]] (chp2 cours.pdf), [[2 - De courrier à courriels]] (scan de 14 pages lu en images ; ouvrage attribué à Nicholas Carr, *Superbloom*, par concordance de table des matières), [[2 - Prise de note de courrier à courriel]] (synthèse du scan). Corrections : thèse de Church-Turing (1936), Whole Earth Catalog (1968), Xerox PARC (1970, Palo Alto), annuaires et moteurs de recherche, modem 56k (1997), ARPA et DARPA, HP (1939), Stanford Research Park (1951), Intel (Mountain View), sigle du CERN, guerre de Sécession, deux écarts entre la synthèse et le scan.

Concepts créés (49) : 12 pour Culture du vivant (Société de consommation, Fabrique du consentement, Révolution industrielle, Printemps silencieux, Forêt (écosystème), Droits de la nature, Perspectivisme, Réensauvagement, Cascade trophique, Écoféminisme, Mythe de Prométhée, Dédale et Icare), 37 pour Histoire du design (voir [[Accueil]]). Concepts complétés : Tournant relationnel, Grande accélération, Sixième extinction, Limites planétaires, Anthropocène, Capitalisme, Érosion de la biodiversité, Technicité, Économie circulaire, Design industriel, Cybernétique, Rétroaction (alias « homéostasie » retiré, devenu page propre), Machine de Turing, Test de Turing, Interface graphique, Apprentissage automatique, Intelligence artificielle, World Wide Web, Le médium est le message, Économie de l'attention, Réseau local, Modèle OSI, Routage IP, DNS. Travail confié à trois agents, relu ensuite.

## [2026-11-10] schema | Numérotation chronologique des matières sur plusieurs années

Dans une matière répartie sur plusieurs années, les fiches sont numérotées de façon continue dans l'ordre chronologique, de la plus ancienne année à la plus récente ; un nouveau document prend le numéro suivant. Règle ajoutée à `CLAUDE.md`. Renommage fait par l'utilisatrice dans Obsidian :

- Culture du vivant : Year 3 `1` (note du cours 1), `2` (dernier cours), `3` (PDF du premier cours) ; Year 4 `4` (chp 1, ancienne `1`), `5` (chp 2). Ancres ✎ renumérotées (`^e-2` à `^e-5-culture-du-vivant`).
- SHS : `3`, `4`, `5` pour les trois textes de Year 3 (anciennes `4`, `5`, `6`), et [[6 - design libre]] pour la note de groupe de Year 4 (ancienne `3 - Prise de note`).

Algo, Philosophie et Corps à l'oeuvre étaient déjà dans l'ordre.

## [2026-11-10] schema | Concepts liés densément

L'utilisatrice a jugé la fiche du cours 2 de Culture du vivant trop peu liée, et ce n'était pas la première fois. Nouvelle règle « Concepts, densément » dans `CLAUDE.md`, rappelée dans `/maj-cours` : chaque notion, courant, œuvre, institution, loi, événement ou technique nommé dans une fiche (cours ou complément) est lié et a sa page, personnes exceptées ; au moins 50 concepts distincts pour une fiche d'une centaine de lignes.

## [2026-11-10] ingest | Enrichissement dense des fiches du lot

Les cinq fiches nouvelles du lot reprises selon cette règle (concepts distincts liés, avant → après) : [[5 - Culture du vivant]] 28 → 151 (44 compléments ⓘ, 11 de plus), [[1 - Histoire du design]] 35 → 208 (35 ⓘ), [[2 - Histoire du design]] → 236 (25 ⓘ), [[2 - De courrier à courriels]] → 95 (12 ⓘ), [[2 - Prise de note de courrier à courriel]] → 53 (4 ⓘ). 312 concepts créés (1 828 au total), dont 275 définis hors du cours, et une centaine de pages existantes complétées. Alias en double retirés quand une notion a reçu sa propre page (DDT, animisme, hubris, obsolescence programmée, LSD, Macintosh, Xerox Alto, thèse de Church-Turing…) ; doublons CERN, DARPA et SRI International fusionnés. Correction ajoutée : [[Whole Earth Catalog]] (1965 → 1968). L'agent des fiches du chapitre 2 s'est arrêté sur une erreur de connexion après avoir fini ses fiches ; le contrôle final ne trouve aucun lien cassé. Travail confié à trois agents, relu ensuite.

## [2026-11-10] import | Mise à jour depuis Drive

Lot du 2026-11-10 (second de la journée) : 3 documents (2 ajoutés, 1 modifié). Seul le document SHS est intégré, à la demande de l'utilisatrice.

- `Year 4/SHS/Prise de note SHS.docx` (modifié) : [[6 - design libre]] mise à jour. Le groupe a retiré ses notes de recherche (Blush, crédits, Hugging Face…), la problématique « à retirer » et la plupart des consignes ; la partie 3 remplace la thèse de la « dictature bienveillante » par le constat d'interfaces faites sans designers, et gagne une sous-partie sur la captation des communs par les entreprises (Google et Kubernetes, AGPL) ; la partie 4 détaille le cas Docker Swarm (licence Apache 2.0) et retient les CC signals comme piste ; une thèse finale sur la commoditisation du complément est ajoutée. Note de groupe : pas d'enrichissement. 74 concepts distincts liés.
- Correction : Kubernetes n'est pas construit « sur le code source de Docker » mais inspiré des systèmes internes Borg et Omega de Google (kubernetes.io, 2024) ; inscrite dans [[Erreurs du cours]].
- Concepts créés (30) : Kubernetes, Orchestration de conteneurs, LAION-5B, CLIP (modèle), Jeu de données d'entraînement, Centre de données, Blender, Figma, Penpot, OpenFisca, GitHub, Forge logicielle, Logiciel propriétaire, Lucide, Licence Apache, Licence permissive, GNU Affero General Public License, Poly Haven, CocoMaterial, Collletttivo, Velvetyne, Blush (illustration), Imagerie à grande gamme dynamique, Benchmark (design), Commoditisation du complément, Monopole, Organisation non gouvernementale, Terres rares, Patreon, CC signals (sorti des alias de Creative Commons). Concepts complétés : Communs numériques, Creative Commons, Licences libres, Design contributif et Dictature bienveillante (thèse retirée de la note).
- Non intégrés, en attente : `Year 4/C++/chp4 C++ - cours super complet.pdf` et `Year 4/C++/chp5 compilation séparée .pdf` (ajoutés). Lot non clos.

## [2026-11-11] import | Mise à jour depuis Drive

Jeton rclone expiré, renouvelé par l'utilisatrice. Lot du 2026-11-11 : 1 document modifié, `Year 4/SHS/Prise de note SHS.docx`, non intégré (l'utilisatrice a demandé le seul cours de C++). Les deux PDF de C++ laissés en attente le 2026-11-10 ne figuraient plus dans le lot, l'ancien ayant été clos : ils sont intégrés depuis `Raw/` comme documents ajoutés.

- `Year 4/C++/chp4 C++ - cours super complet.pdf` (ajouté, polycopié de TP de 40 pages, 2012) : fiche [[4 - Cours complet]], 1 222 lignes, 93 compléments ⓘ, 177 concepts distincts liés. Trois parties (premier programme, structure d'un programme, programmation modulaire), les 56 questions de révision avec leur réponse et les exercices 1 à 6 avec une solution (ⓘ), tableau final de ce que le C++ moderne change au polycopié. Les noms de l'auteur et de l'auteur du fichier `aCorriger.cpp` sont retirés. Rédigée par un agent, relue ensuite.
- `Year 4/C++/chp5 compilation séparée .pdf` (ajouté, 5 diapositives) : fiche [[5 - Compilation séparée]], 21 compléments ⓘ, 70 concepts liés ; figure du schéma de compilation séparée (`5 - Compilation séparée - image1.png`). Code des diapositives compilé avec g++ 14.
- Corrections (✎) : [[5 - Compilation séparée]], `affiche()` appelée sans être déclarée dans `Point` ni `Segment` (le `main` ne compile pas), et `#include "…"` cherché dans le dossier du fichier qui inclut, pas dans le dossier courant (manuel du préprocesseur de GCC) ; [[4 - Cours complet]], neuf corrections (`string` sans `std::` ni `<string>`, `bool` présent en C depuis C99, identificateurs « 12 premiers caractères discriminants », noms réservés en `__`, `racineCarree` 7 → 49, premier programme enregistré : Manchester Baby 1948 et non EDSAC 1949, appel avant déclaration = erreur en C++, figure `carre(2)` = 4, renvoi de la question 56) ; [[Directive include]] et [[Racine carrée]], par contrecoup.
- Concepts créés (107) : 79 par l'agent pour le polycopié (Compilateur, Code machine, Langage d'assemblage, Environnement de développement intégré, Débogueur, Commentaire, Fonction main (C et C++), Lvalue et rvalue, Initialisation, Type entier, Booléen, Classe string (C++), Norme du C, EDSAC, Manchester Baby, Visual Studio, Discours de la méthode…), 28 pour le chapitre 5 (Compilation séparée, Fichier source, Déclaration et définition, Interface et implémentation, Préprocesseur, Directive include, Garde d'inclusion, Compilation conditionnelle, Unité de compilation, Fichier objet, Édition de liens, Symbole (édition de liens), Exécutable, Option de compilation, Avertissement de compilation, Make (logiciel), CMake, Ninja, Clang, Norme du C++, Organisation internationale de normalisation, Bibliothèque standard du C++, Liste d'initialisation, Opérateur de résolution de portée, Règle de la définition unique, Fonction inline, Méthode constante, Caractère de tabulation). Une trentaine de concepts existants complétés (Fichier d'en-tête, Chaîne de compilation, GCC, Programmation modulaire, Racine carrée, Langage C++, Référence (C++), Passage par valeur…).
- Alias retirés parce que la notion a sa page : « édition de liens », « linker », « préprocesseur », « fichier objet » (Chaîne de compilation), « #include », « include guard », « #pragma once » (Fichier d'en-tête), « liste d'initialisation » (Constructeur), « opérateur de résolution de portée » (Classe et objet), « undefined reference » et « avertissement du compilateur » (Erreur de compilation) ; « fonction main » passe de Méthode main (Java) à Fonction main (C et C++). Liens vers Méthode main dans les fiches C++ redirigés.
- Carte C++, Accueil (1 966 concepts, 166 résumés), Complément hors du cours et Erreurs du cours (309 pages, 626 marques) mis à jour. Aucun lien cassé dans les fichiers modifiés.

## [2026-11-12] import | Mise à jour depuis Drive

Lot du 2026-11-12 : 15 documents (5 ajoutés, 1 modifié, 5 déplacés, 4 supprimés). Seuls les documents de C et C++ sont traités, à la demande de l'utilisatrice.

- Le dossier Drive `Year 4/C++` est devenu `Year 4/C／C++` (barre oblique pleine chasse, U+FF0F). Les trois docx des chapitres 1 à 3, signalés supprimés puis ajoutés, ont un texte et des images identiques (empreintes comparées) : ce sont des déplacements, comme les quatre PDF des chapitres 4 et 5. Aucune fiche réécrite.
- Liens `[[Raw/Year 4/C++/…]]` remplacés par `[[Raw/Year 4/C／C++/…]]` dans 147 pages (les 7 fiches et 140 concepts) ; les 7 liens se résolvent. `matieres: C++` devient `C／C++` dans 18 concepts, pour que la mise à jour continue de les repérer dans les documents de ce dossier.
- Accueil (ligne de la matière, avec les fiches des chapitres 4 et 5 qui y manquaient ; Sources disponibles, 215 documents) et carte C++ mis à jour.
- Non intégrés, en attente : `Year 4/data mining/chp 2 - association rules.pdf` (ajouté), `Chp1 - intro to data mining.docx` renommé `Chp 1 - …` et `chp 1 - cours data mining du prof.pdf` déplacé, `Year 4/SHS/Prise de note SHS.docx` (modifié). Lot non clos.

## [2026-11-12] schema | Programmes C et C++ : une fiche par dossier

L'utilisatrice a déposé sur Drive deux dossiers de programmes, `Year 4/C／C++/programmes C` et `programmes C++`, dont les commentaires portent sur le cours, et veut les retrouver dans le wiki, une fiche par dossier. `CLAUDE.md` reçoit l'exception (fiche `<N> - Programmes <dossier>`, code en blocs, commentaires remis en explications). Outils : le filtre `.outils/exclusions.local` retient aussi les `.c`, `.cpp`, `.h`, `.hpp` et Makefile des seuls dossiers `programmes…` de C／C++ (les deux exécutables compilés du Drive restent exclus) ; `maj.py` recopie un fichier de code source dans un bloc de code au lieu de ne rien convertir (test ajouté, 93 tests verts).

## [2026-11-12] ingest | Programmes C et C++

Le lot du jour étant ouvert, les 78 programmes ont été copiés dans `Raw/` par `rclone copy` avec le même filtre, puis le lot refait (`maj.sh --reprendre`), où ils figurent comme ajoutés.

- Douze fiches dans [[Cours/Informatique/C++/_index|C++]], chaque programme compilé (`gcc`/`g++` 14, `-Wall -Wextra`) et exécuté : [[tp2]], [[tp3]], [[tp4]], [[tp5]], [[tp6]], [[tp7]], [[tableaux]], [[pointeurs]], [[td listes chaînées]], [[formation C++]], [[exo-prof]], [[compilation séparée (C++)]]. Concepts distincts liés : de 50 à 92 par fiche (16 et 18 pour les deux fiches d'un et deux programmes) ; 177 compléments ⓘ.
- Corrections (✎, 29 marques sur 7 fiches, inscrites dans [[Erreurs du cours]]) : programmes qui ne compilaient pas (2.5, 2.10, 3.3, 3.4, 3.11, ex1.c, `x` en trop de tous_les_exo.c), divisions entières (2.3, 7.3), variables lues sans valeur (5.3, 7.2), tests faux (nombre parfait, 1 premier, `2<=n<=5`, mauvais chaînon supprimé dans ex4.c), formules de volume, arguments inversés de `puissance`, fuites mémoire (ex3.c, ex4.c), commentaires inexacts (`char "e"`, `std::endl`, `ostream`, opérateur virgule, tableau « initialisé », double pointeur).
- Concepts créés (52) : 34 en informatique (Opérateur sizeof, Double pointeur, Alias de type (typedef), Instructions break et continue, Pointeur this, Surcharge de fonctions, Copie superficielle et copie profonde, Règle de zéro, Dépassement de tampon, Décroissance d'un tableau en pointeur, AddressSanitizer, Valgrind, POSIX, Compilation incrémentale…), 10 en mathématiques (Puissance, Exponentiation, Fonction affine, Nombre pi, Nombres de Lucas…), 7 en sciences humaines (Année bissextile, Échelle de Richter, Séisme…). 58 concepts existants complétés (« Dans le cours »), `matieres: C++` → `C／C++` sur 8 d'entre eux.
- Alias retirés parce que la notion a sa page : « compilation incrémentale » (Compilation séparée), « signal POSIX » (Signal Unix), « crible d'Ératosthène » (Nombre premier), « typedef » (Structure (struct)), « identificateur » (Variable (programmation)). [[Comportement indéfini]] : `i = i++ + 1;` est défini en C++ depuis C++17 ; [[Variable non initialisée]] : l'oubli est signalé par un avertissement, pas une erreur.
- Accueil (2 018 concepts, 178 résumés, 293 documents dans Sources disponibles), carte C++, Complément hors du cours (168 fiches, 2 991 compléments, 848 concepts) et Erreurs du cours (316 pages, 655 marques) mis à jour. Rédaction confiée à sept agents (quatre pour les fiches, trois pour les concepts), relue ensuite ; aucun lien cassé dans les pages écrites.
- Reste ouvert : [[Distance]] lie deux documents de data mining renommés sur Drive, à reprendre avec l'intégration de data mining. Lot non clos.

## [2026-11-12] schema | Fiches de programmes en sous-dossiers

À la demande de l'utilisatrice, les fiches de programmes quittent la racine de la matière : 6 à 14 (C) dans `Cours/Informatique/C++/programmesC/`, 15 à 17 (C++) dans `programmesCPP/`. Noms inchangés et uniques, aucun lien par chemin : tous les liens se résolvent. Exception notée dans `CLAUDE.md` et sur la carte C++.

## [2026-11-12] schema | Fiches de programmes renommées

À la demande de l'utilisatrice, les fiches de programmes perdent numéro et préfixe et prennent le nom de leur dossier de Drive : [[tp2]] à [[tp7]], [[tableaux]], [[pointeurs]], [[td listes chaînées]] (`programmesC/`), [[formation C++]], [[exo-prof]] et [[compilation séparée (C++)]] (`programmesCPP/` ; suffixe parce que le concept [[Compilation séparée]] porte déjà ce nom). Liens réécrits dans 125 pages, entrées précédentes de ce journal comprises, comme le ferait un renommage dans Obsidian ; ancres ✎ renommées (`^e-tp2`, `^e-td-listes-chainees`, `^e-formation-c`…) dans les fiches et [[Erreurs du cours]]. Aucun lien ni ancre cassés ; la mise à jour depuis Drive retrouve chaque fiche. Règle de nommage mise à jour dans `CLAUDE.md`.

## [2026-11-12] import | Mise à jour depuis Drive

Lot du 2026-11-12 (second de la journée) : 1 document modifié, `Year 4/SHS/Prise de note SHS.docx`. Le lot précédent ayant été clos sans que cette note soit intégrée, la fiche est comparée au texte entier, pas au seul diff du lot.

- [[6 - design libre]] mise à jour : « L'illusion de l'inclusion » passe de la partie 3 à la partie 2 ; la partie 3 devient « Financer le design en commun », avec la sous-partie « L'illusion du vol du commun » (Google et Kubernetes, AGPL) ; transitions vers les parties 3 et 4 ; partie 4 recentrée sur l'IA, avec sa question directrice ; nouvelle section « Contexte de l'enquête », recopie de l'énoncé du cours (workshop, filiation Papanek, Mari, Illich, Huyghe, l'IA comme objet transversal, restitution publiée sur un commun numérique sous licence libre). Note de groupe : pas d'enrichissement. 89 concepts distincts liés, aucun lien cassé.
- Correction : la partie 3 reprend « Google a pompé le code source de Docker Swarm » ; corrigée avec la marque ✎ existante, puce complétée dans [[Erreurs du cours]].
- Concepts créés (10) : [[Design for the Real World]], [[Autoprogettazione]], [[Workshop (design)]], [[Convivialité (Illich)]], [[Les Bases du numérique d'intérêt général]], [[Agence nationale de la cohésion des territoires]], [[Site web]], [[Wiki]], [[Éditeur de texte collaboratif]], [[Podcast]]. Complétés : [[Design industriel]], [[Design social]], [[Responsabilité élargie du designer]], [[Logiciel libre]].
- Pas de page pour Conviviel (plateforme citée par l'énoncé, introuvable dans une source fiable) ni pour le « design pensé comme prudence » de Pierre-Damien Huyghe (notion à préciser avec le cours).
- Carte SHS et Accueil (2 028 concepts, 178 résumés) mis à jour.

## [2026-11-12] import | Mise à jour depuis Drive

Lot précédent clos à la demande de l'utilisatrice. Lot du 2026-11-12 (troisième de la journée) : 4 documents (3 ajoutés, 1 modifié). Les trois PDF de Graph theory étaient déposés sur Drive sans extension : repris d'après leur type, avec l'extension `.pdf` dans `Raw/`.

- `Year 4/SHS/Prise de note SHS.docx` (modifié) : [[6 - design libre]], le groupe commence à rédiger l'introduction du rapport (sujet : le design comme commun numérique ; cours de SHS de 4e année) ; reporté dans « Contexte de l'enquête ».
- `Year 4/graph theory/Suppléments de cours (tree, algo...)/` (3 ajoutés, supports de cours) : fiches [[2 - tree revisions années précédentes]] (diaporama « Arbres » du cours d'algorithmique de 1re année de CY Tech, 2020-2021 ; 270 lignes, 30 ⓘ, 75 concepts liés), [[4 - bellman ford]] (diaporama d'Aix-Marseille Université, 2023-2024 ; 327 lignes, 26 ⓘ, 59 concepts) et [[4 - dijkstra]] (CY Tech, 2020-2021 ; 179 lignes, 18 ⓘ, 55 concepts ; les deux exercices résolus, ⓘ, vérifiés sur l'image). Numéros repris des noms des documents (`Chp2`, `chp4`), comme les fiches qu'ils complètent. Calculs des exemples refaits par script : tableaux exacts. 11 figures (`… - p<N>.jpg`), sans les noms des enseignants. Rédaction confiée à deux agents, relue ensuite.
- Corrections (✎, inscrites dans [[Erreurs du cours]]) : définition récursive circulaire de l'arbre, hauteur minimale « ⌊log_k n⌋ + 1 » avec une profondeur comptée en arcs, postcondition de `filsGauche` ; circuits négatifs (seuls les sommets atteignables via le circuit perdent leur plus court chemin), `pred` jamais mis à jour dans BELLMAN-FORD-R1 ; Dijkstra conçu en 1956, publié en 1959.
- Concepts créés (32) : Plus court chemin, Relâchement d'un arc, Circuit absorbant, Arbre des plus courts chemins, Algorithme de Floyd-Warshall, Algorithme de Johnson, Algorithme SPFA, Algorithme A étoile, Heuristique (algorithmique), Principe d'optimalité de Bellman, Problème du plus long chemin, Routage à vecteur de distances, Routage à état de liens, Comptage à l'infini, Latence (réseau), ARMAC, Numerische Mathematik, Parcours préfixe, Parcours infixe, Parcours postfixe, Sous-arbre, Arbre ordonné, Arbre numéroté, Arbre équilibré, Arbre dégénéré, Type abstrait de données, Précondition et postcondition, File de priorité, Tas de Fibonacci, Analyse amortie, Logarithme, Nombre de Catalan. Une trentaine de concepts existants complétés (Algorithme de Dijkstra, Algorithme de Bellman-Ford, Programmation dynamique, Arbre binaire, Arbre binaire de recherche, Hauteur d'un arbre, Pile et file, Tas binaire, Routage dynamique, OSPF…).
- Alias retirés parce que la notion a sa page : « parcours préfixe/infixe/postfixe » (Arbre binaire), « file de priorité », « priority queue » (Tas binaire), « vecteur de distance » (Routage dynamique).
- Carte Graph theory (section « Suppléments de cours »), Accueil (2 060 concepts, 181 résumés, 296 documents dans Sources disponibles), Complément hors du cours (171 fiches, 3 065 compléments, 882 concepts) et Erreurs du cours (319 pages, 659 marques) mis à jour. Lot non clos.
