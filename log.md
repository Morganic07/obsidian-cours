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
