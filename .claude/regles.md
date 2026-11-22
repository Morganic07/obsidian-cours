# Règles annexes du wiki de cours

Procédures moins courantes, renvoyées depuis `CLAUDE.md`.

## Images

Toutes dans `Cours/<Domaine>/<Matière>/images/`, intégrées par le seul nom (`![[6 - T-Test - image3.png]]`), nom unique dans le coffre et sans nom de personne.
- Word : `<Nom de la fiche> - imageN.png`, copiée depuis le lot (`conversions/NN/nouveau/`) ou via `convertir.py … --images <dossier temporaire>`. Les anciens noms (`Chp1 - Intro Java - image3.png`) restent tels quels.
- PDF ou PPTX : `<Nom court> - p<N>.jpg`, 110 dpi, JPEG qualité 80, recadré si utile ; image d'un PPTX : son nom d'origine après le nom court.
- Les images ne suivent pas Drive : recopier une image modifiée. Les images des rendus de l'utilisatrice s'intègrent normalement ; une image montrant le nom ou le logo nominatif d'un tiers se décrit en une ligne.
- Un dessin Google Docs arrive en images suivies d'une ligne « Texte du dessin : … », sans disposition ni flèches.

## Transcriptions

`.transcriptions/<empreinte>.md` : transcription d'une image, identifiée par son contenu ; un fichier vide marque une image sans contenu. Seule partie des sources que tu peux compléter, ou corriger sur demande après avoir vu l'image. La correction reproduit l'image, coquilles comprises : une mention « À vérifier » levée devient « Vérifié sur l'image : … » ; pour une erreur du cours, garder le texte et ajouter « À vérifier : … (erreur probable du cours, l'image écrit bien …) ». Ne jamais supprimer `.transcriptions/`.

## Cartes et notes anciennes

- Une carte se lie avec `\|` dans un tableau : `[[Cours/Informatique/OS/_index\|OS]]`.
- Notes anciennes sans `type`, `tags` ou `maj` : compléter l'en-tête à leur prochaine modification.
- Créer les dossiers à la première page qui en a besoin.

## Outils

- `/maj-cours` lance `bash .outils/maj.sh` puis intègre le lot. `maj.sh` n'écrit jamais dans le wiki : il synchronise `Raw/`, convertit et transcrit (50 images au plus sans accord) dans `~/.cache/obsidian-cours/maj/`, puis écrit `lot/BILAN.md` et un fichier par document. Options : `--reprendre`, `--clore` (une fois le wiki à jour), `--sans-transcrire`. Un lot non clos bloque la synchronisation suivante.
- Transcrire un lot : `python3 .outils/transcrire.py [--matiere "Year 2/Probability"] [--limite N]`, puis `bash .outils/maj.sh --reprendre`.
- Noms de dossiers des scripts : uniquement dans `.outils/chemins.py`, jamais en dur. Pour en renommer un : disque, puis `chemins.py`, puis `CLAUDE.md`.
- `log.md`, dernières entrées : `grep "^## \[" log.md | tail -5`.

## Renommer, supprimer

- Renommer une page : depuis Obsidian (liens mis à jour). Ailleurs, réécrire soi-même liens et chemins en texte, puis contrôler. Le lien `sources` d'une fiche change si son document est déplacé.
- Supprimer une page : Obsidian laisse les liens vers elle ; les corriger (carte, `Accueil.md` compris).
- Un fichier de `Raw/` supprimé revient : le supprimer sur Drive ou l'ajouter à `.outils/exclusions.local` et l'ôter de `Raw/`, puis traiter sa fiche avec l'utilisatrice.

## Chantiers par agents

Lots d'une cinquantaine de pages, consigne de reprise (marqueur de fin, journal) ; fusionner les propositions avant d'écrire.
