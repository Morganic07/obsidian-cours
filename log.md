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

Le miroir de Drive passe dans `raw/`, exclu de git. La conversion ignorait les dessins groupés de Google Docs : 82 groupes dans 176 documents, soit 97 images et le texte de 45 encadrés absents des notes. Le script les remplace désormais par leurs images et une ligne « Texte du dessin ». La disposition et les flèches restent perdues. Les 97 images sont transcrites, ce qui porte le total à 1 978.

## [2026-11-05] ingest | Year 1/Algèbre Linéaire

7 notes intégrées. Créés : 7 résumés, 1 page de matière et 3 concepts (Morphisme, Changement de base, Somme directe). 18 concepts communs complétés, sans doublon. 18 points à vérifier dans le cours. Des formules manquent dans chp4, chp5 et chp6 : l'export de Google est vide à ces endroits, à vérifier dans les Google Docs.

## [2026-11-05] ingest | Reprise de Bilinear Algebra après récupération des dessins

26 images récupérées et les textes des dessins relus. Deux remarques du wiki étaient fausses et sont retirées : la formule de la décomposition spectrale figure bien dans le cours (image non importée jusqu'ici), et un dessin de chp4 corrige la borne de la somme de $c_{ij}$. Ajouts : $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$, $\text{proj}_W\,\mathbf{y} = UU^T\mathbf{y}$ et le développement colonnes-lignes.

## [2026-11-05] import | Retrait d'un dossier administratif

Un dossier de documents administratifs est retiré de `raw/`, de `Cours/` et de `.transcriptions/`, et exclu des prochaines mises à jour depuis Drive. Il reste 175 notes, 53 PDF et 1 976 transcriptions.

## [2026-11-05] ingest | Year 2/Analyse dans Rn

4 notes intégrées. Créés : 4 résumés, 1 page de matière et 12 concepts, de Boule et voisinage à Difféomorphisme. Norme complétée. 19 points à vérifier dans le cours, dont cinq prioritaires, notamment « lipschitzien ⇔ uniformément continue » et le test en coordonnées polaires, qui ne suffit pas à prouver une limite.

## [2026-11-05] ingest | Year 1/Analyse Maths et Year 2/Analyse

5 notes intégrées. Créés : 5 résumés, 2 pages de matière et 5 concepts (Dérivabilité, Comparaison asymptotique, Développement limité, Intégrale, Primitive). 15 points à vérifier dans le cours. Deux mentions « À vérifier » de transcriptions sont de fausses alertes, signalées dans le résumé de chp5. 14 PDF de ces deux matières (réels, rappels, TD, contrôles, intégrales multiples) restent absents du wiki.

## [2026-11-05] ingest | Toutes les autres matières, par lots

151 notes intégrées en 7 lots parallèles : Probability, Statistics, Data analysis, data mining, IA, Outil Maths, Algo Maths, Séries, graph theory, Operating System, Algo, Java, C++, Data base, Computer Network, Philosophie, SHS, HDA, Communication orale, Anglais, écriture narrative, Culture du vivant, Corps à l'oeuvre, Dessein au cube, Peinture, Projets design, workshop, ligue football, management de l'innovation, projet court. Créés : 149 résumés, 35 pages de matière et 128 concepts. Les notes en double sont regroupées dans un seul résumé. Fusion : deux concepts écrits en même temps (Économie circulaire, Complexité algorithmique) sont réunis, et les variantes `process` et `top of mind` sont retirées car elles créaient de faux liens. Contrôle : 285 nouveaux liens échantillonnés par concept. La plupart des images n'ont pas été rouvertes dans ces lots. Deux notes ne sont lues qu'en partie : l'entretien de SHS en Year 4 et Global Exam Vocab.

## [2026-11-05] import | Retrait de notes personnelles

10 notes personnelles sont retirées de `raw/`, de `Cours/`, de `.transcriptions/` et du wiki, et exclues des prochaines mises à jour depuis Drive : un dossier de Dessein au cube, une fiche, les devoirs de Peinture et une note d'instructions. Six résumés sont renommés pour ne plus porter de nom de personne. Il reste 165 notes et 163 résumés.

## [2026-11-06] import | Retrait de trois notes isolées

Trois notes sans lien entrant, dont deux portaient un nom de personne, sont retirées de `raw/` et de `Cours/` et exclues des mises à jour. Leurs résumés restent. Il reste 162 notes.

## [2026-11-06] ingest | Documents PDF et PPTX

Les 53 PDF et 6 PPTX de `raw/` sont résumés en 4 lots, soit 1 515 pages : 59 résumés, 15 concepts et 5 nouvelles pages de matière (Year 2 - SHS, Year 3 - Affordance, Year 3 - Projet courts, Year 3 - Sémiotique, Year 4 - culture du soin). Les documents sont lus par leur texte extrait, et une page n'est ouverte en image que si le texte est illisible ou douteux. Lectures partielles : les gros documents de diapositives (AlgoID1, AnalyseID1, td0slides, td1slides, TDSuites), text2 et text3 de SHS. Les liens vers trois fichiers dont le nom pose problème sont écrits en texte simple.
