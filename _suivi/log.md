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

Deux fichiers changés sur Drive, aucune image à transcrire. Nouvelle note `Year 4/Gestion financière`, rangée à la racine de l'année : résumé et page de matière Gestion financière (matière) créés, sans concept (définitions d'une ligne), trois points à vérifier dont la définition du PNB. Note modifiée `Chp1 - intro to data mining` : seul ajout repéré, la phrase reliant le classifieur à la matrice de confusion, reportée dans le résumé. L'index compte désormais 163 notes (le décompte de 165 n'avait pas suivi le retrait de trois notes isolées).

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

`Entretien sur l'open source` : transcription lue en entier, le résumé ajoute la façon de juger un dépôt (mises à jour, communauté, étoiles), la diffusion par le bouche-à-oreille et les réseaux sociaux, l'absence de licence, et la contribution par demande de fusion. Nouveau concept [[Demande de fusion]]. `Global Exam Vocab` : les quelque 285 entrées sont classées par chapitre ; sept définitions discutables relevées (hue, tertiary colours, golden ratio, aspect ratio, die cut, tolerance, anti-ornate), la définition d'aspect ratio aussi signalée sur [[Compression vidéo]].

## [2026-11-06] ingest | Résumés complets, avec figures

Les 216 résumés des notes de `Cours/` et des documents de `.raw/` deviennent des fiches complètes (`complet: true`), pour réviser sans ouvrir la source : définitions, théorèmes, formules, méthodes, code, exemples et exercices corrigés quand le document le permet. Ils passent d'environ 100 000 à 376 000 mots. Sont écartés : les résumés des trois notes supprimées par l'utilisatrice, les deux résumés d'entretiens SHS de Year 3 dont la note n'existe plus, et l'entretien sur l'open source, déjà complet. 841 images intégrées : 498 reprises des notes de `Cours/` sans copie, 343 créées depuis les PDF et PPTX dans 17 dossiers `Matières/<Matière>/images/` (47 Mo). Les PDF scannés (Contrôles, AnalyseID1, Chap1-reels, exercices de logique, Chp9) sont lus sur l'image ; `Contrôles.pdf` donne enfin les définitions de [[Nombre d'Armstrong]] et [[Nombre parfait]], complétées. Les schémas de formes PowerPoint, non extractibles faute de LibreOffice, sont décrits en texte.

Nouvelles erreurs de cours relevées et notées, sans correction, dont : majoration de $\sum 1/k^2$ (AnalyseID1), terme d'ordre 4 du corrigé du TD5 (ex. 18c), formules trigonométriques de td0slides, calcul d'âge et date d'Al-Khowarizmi (AlgoID1), réseau de l'ACL (Computer Network), conjugué des complexes (Outil Maths). Textes signalés comme générés ou traduits par un outil : Synthese SHS GPT, Recherches SHS, encadrés de la séance 13 d'ACP, fiche ressources Santé au travail, text1 (DeepL), recherches femmes et foot. Restent à trancher avec l'utilisatrice : les images de ses rendus dont le chemin porte son nom (écartées pour TP3, intégrées pour Douze innovations), trois images d'IA portant le logo nominatif d'une intervenante, et trois faux liens automatiques (gamma distribution, sample median, matrice composée).

## [2026-11-07] schema | Images des fiches copiées dans Matières/

Décisions de l'utilisatrice : les images de ses rendus s'intègrent même si leur chemin porte son nom (19 captures ajoutées au TP3) ; trois images de la séance 1 d'IA portant le logo nominatif d'une intervenante sont remplacées par une description ; les PNG lourds restent tels quels. Pour pouvoir cacher `Cours/` plus tard, les 514 images que les fiches intégraient depuis `Cours/…/medias/` sont copiées dans `Matières/<Matière>/images/`, nommées d'après leur fiche (`AVL momo - image3.png`), sans nom de personne ; 87 fiches réécrites. Les images du wiki pèsent désormais 123 Mo. Les noms de dossiers utilisés par les scripts sont centralisés dans `.outils/chemins.py`, et `maj.sh` refuse un nom de miroir vide ou suspect avant `rclone sync`.

## [2026-11-07] transcription | Vérification des 1 838 transcriptions sur l'image

Chaque transcription non vide dont l'image existe encore est comparée à son image, en 12 lots. 39 erreurs de lecture corrigées, dont 10 qui changent le sens : les adresses `127.0.1.1` du TP3 (deux captures), l'`exit(0)` du processus F (TP 08), trois limites en polaires d'Analyse dans Rn (deux images portent $(0,\theta)$, une $(0,0)$), la médiane $\tilde{x} = 92{,}17$ de Statistics (et non la moyenne), le troisième couple de la validation croisée en data mining, un code couleur et un prompt en IA, un facteur d'équilibre d'arbre AVL. Les 29 autres sont des mots mal lus, des descriptions de figure et des coquilles du cours que la transcription corrigeait sans le dire ; elle reproduit désormais l'image, la coquille signalée. Les corrections sont reportées dans les fiches et les concepts qui les avaient recopiées ; trois pages reprochaient à tort une erreur au cours de Statistics. Une image (« Critical Evaluation », Statistics Chp1) reste à vérifier à la main : le filtre de contenu bloquait sa vérification. La reconversion des notes de `Cours/` n'a pas été lancée.
