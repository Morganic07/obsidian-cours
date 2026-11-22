# Wiki de cours

Base de connaissances sur les cours de CY Tech (modèle « LLM Wiki ») : le savoir est compilé une fois dans le wiki puis tenu à jour. L'utilisatrice choisit les sources et pose les questions ; tu écris et entretiens le wiki. Tout en français, en gardant les termes techniques du cours. Procédures moins courantes (images, transcriptions, renommer, supprimer, outils) : `.claude/regles.md`, à lire quand on en a besoin.

## Priorité : compléter et corriger le cours

Les documents de `Raw/` sont surtout des prises de note rapides, lacunaires et parfois fausses. **Un de tes rôles principaux est de compléter chaque cours** pour qu'il permette de maîtriser le sujet. Cela vaut à chaque fiche écrite ou mise à jour, sans attendre de demande, et pour les fiches existantes encore lacunaires.

- **Compléter** : dans le périmètre et au niveau du cours (année, filière), ajouter ce qui manque pour comprendre : définition d'un terme employé sans explication, notion classique absente, étape sautée, mécanisme, exemple chiffré, ordre de grandeur, contexte historique, lien avec d'autres matières. L'ajout va à l'endroit où il sert, dans le texte (pas d'encadré), en paragraphe ou élément de liste entier, terminé par `[[Complément hors du cours|ⓘ]]` (pour une liste, un tableau ou une formule ajoutés : à la fin de la phrase qui les introduit), pour que la marque dise sans ambiguïté ce qui vient d'ailleurs. Enrichir, pas noyer : tout passage sans ⓘ vient du cours. Pas d'enrichissement des projets de design ni des notes de groupe (seulement leurs concepts).
- **Corriger** : une source fiable (manuel, documentation officielle, organisme, publication, vérifiée sur le web) ou un calcul refait prime sur la note. L'erreur se corrige dans le texte même, sans section ni mention « le cours écrit… » ; le passage corrigé (phrase, élément de liste, ligne de tableau, phrase qui introduit un code ou une formule) finit par `[[Erreurs du cours#^e-<page>|✎]]`, et la correction s'ajoute à `Erreurs du cours.md` : une puce par page (ce que disait le cours, version juste, source) terminée par l'ancre `^e-<page>` (nom en minuscules sans accents, tirets ailleurs : `^e-2-tp2`), cible de toutes les marques de la page ; la noter aussi dans `log.md`. Sans source sûre, ne pas corriger : le signaler à l'utilisatrice. Ne s'applique pas aux `.transcriptions/`, qui reproduisent l'image.
- **Fiabilité des ajouts** : savoir établi de manuel. Chiffres, dates, lois, taux : citer l'organisme ou le texte et l'année, vérifier sur le web si la donnée évolue, sinon s'en passer. Ne rien inventer. Compléter est attendu : le marquage distingue le cours des ajouts, il ne sert pas à les limiter.
- **Concepts, densément** (exigence répétée de l'utilisatrice, à appliquer d'office à chaque fiche écrite ou mise à jour) : chaque notion, courant, théorie, œuvre, institution, loi, événement, technique ou objet nommé dans la fiche, qu'il vienne du cours ou d'un complément, est lié à sa page de concept à sa première occurrence dans chaque section, et la page est créée si elle manque (le PIB appelle Banque centrale, PNB, Inflation… ; une note d'écologie appelle Biodiversité, Écosystème, Bioaccumulation, Empreinte carbone…). Seules les personnes n'ont pas de page. Dans le doute, lier et créer. Ordre de grandeur : une fiche d'une centaine de lignes lie au moins 50 concepts distincts ; une fiche peu liée n'est pas finie. Avant de rendre une fiche, relire chaque paragraphe pour repérer les termes encore sans lien.
- **Suivi** : `enrichi: AAAA-MM-JJ` dans l'en-tête d'une fiche enrichie. Les deux pages racine listent les fiches complétées et les corrections.
- Les deux pages racine expliquent les marques ; `.obsidian/snippets/masquer-images.css` les rend petites et grises en mode lecture. Dans un tableau, elles s'écrivent `[[Complément hors du cours\|ⓘ]]` et `[[Erreurs du cours#^e-<page>\|✎]]`.

## Couches

| Couche | Emplacement | Règle |
|---|---|---|
| Sources | `Raw/`, `.transcriptions/` | Immuables : lire, jamais réécrire |
| Wiki | `Concepts/`, `Cours/`, `Synthèses/`, `Accueil.md`, `log.md`, `Complément hors du cours.md`, `Erreurs du cours.md` | Créer, tenir à jour, relier |
| Schéma | `CLAUDE.md`, `.claude/regles.md` | Évolue avec l'utilisatrice |

**Sources.** `Raw/` est le miroir de `gdrive:CY Tech`, hors git, remplacé à chaque mise à jour : n'y rien déposer ni modifier, renommer sur Drive. Ses noms de fichiers sont en Unicode NFD : ne pas retaper un lien `[[Raw/…]]` accentué, le copier depuis le disque. Lire un Word avec ses images transcrites : `python3 .outils/convertir.py "Raw/…docx"` (n'écrit rien) ; un PDF : `pdftotext -layout`, ou en image s'il est illisible ; un PPTX ou un programme : directement.

## Concepts

`Concepts/<Domaine>/<Concept>.md`, une notion par page, nom français (termes anglais dans `aliases`). Cinq domaines, par discipline et non par matière :
- `Mathématiques` : algèbre, analyse, séries, logique ;
- `Probabilités et statistiques` : probabilités, dénombrement, statistique, tests, régression ;
- `Informatique` : systèmes, réseaux, programmation, algorithmique, bases de données, outils (R compris), IA technique (une ACP vue en statistique va ici) ;
- `Design` ;
- `Sciences humaines` : SHS, philosophie, écologie et société, enjeux de l'IA (un deepfake va ici).

- Notion définie par un cours : « **Définition** (d'après [[<fiche>]]) : … ». Notion seulement nommée (vérifier d'abord dans les fiches) : « **Définition (complément, hors du cours)** : … », 2 à 4 phrases au moins, plus si la notion est centrale, puis `## Dans le cours`.
- `matieres` = nom du dossier de `Raw/` (`data mining`), pas de `Cours/` : la mise à jour le compare au chemin des documents. S'en servir pour les mots ambigus (`rank`, `déterminant`) ; pas d'alias trop général.
- Tag d'année, `matieres` et `sources` (son document) de la fiche qui a fait naître le concept ; un concept tiré d'un document sans fiche lie ce document dans `sources`.

## Cours

`Cours/<Domaine>/<Matière>/`, un dossier par matière, sans année, dans le domaine de son contenu principal (Graph theory en `Informatique`, Data analysis en `Probabilités et statistiques`, communication et gestion en `Sciences humaines`). Nom court (`OS` pour `Raw/Year 2/Operating System`). Une matière renommée l'année suivante est fusionnée dans la plus récente (Algo Maths → `Algo`, section `## Year 1`). Projets de design : `Projet year N`, workshop compris (section `## Workshop` de la carte). Document isolé : dossier sans carte (`Séance BU`). Fiches à plat, images dans `images/`.

- `_index.md` : la carte (chapitres, concepts, liens), une par dossier, une section `## Year N` par année. Toujours liée par son chemin complet : `[[Cours/Informatique/OS/_index|OS]]`.
- `<N> - <Titre>.md` : la fiche d'un document de `Raw/` (toute page autre que la carte).
  - **Numéro** seul : `Chp1 -`, `Cours 6 -` → `1 - `, `6 - ` (jamais « chp » ni « séance ») ; `0 - ` pour un support transversal ; un numéro peut servir deux fois (`2 - OS`, `2 - TP2`) ; parties : `4 - Inferential statistics 1`, `… 2`. Matière sur plusieurs années : numérotation continue dans l'ordre chronologique (année la plus ancienne d'abord, puis ordre des cours), quel que soit le numéro du document ; un nouveau document prend le numéro suivant.
  - **Titre** : le sujet du nom du document, dans sa langue (`6 - T-Test`) ; sans titre, le nom de la matière (`2 - Peinture`) ; PDF de l'enseignant doublant une note : `2 - pdf`, `1 - pdf du prof`. Projets de design : nom du projet ou du commanditaire, sans numéro.
  - Nom unique dans le coffre, concepts compris (sinon `(Matière)` en suffixe), sans nom de personne.
- **Documents sans fiche** : seuls les supports de cours en ont (chapitres, séances, diaporamas, polycopiés, fiches de commandes, sujets de TP de cours). Pas de fiche pour TD, exercices et corrections, contrôles et DS, rendus de l'utilisatrice (DM, comptes rendus, rapports, projets), entretiens et leurs synthèses, notes de recherche, anglais. Un document sans fiche au 2026-11-07 n'en reçoit pas, même modifié. Catégorie douteuse : demander. Exception, à la demande de l'utilisatrice : les programmes (`.c`, `.cpp`, `.h`, Makefile, dossiers `programmes …` de `Raw/Year 4/C／C++`), dont les commentaires portent sur le cours, ont **une fiche par dossier**, nommée comme le dossier de Drive, sans numéro (`tp2`, `formation C++` ; suffixe `(C++)` si le nom est pris, comme `compilation séparée (C++)`), rangée dans le sous-dossier `programmesC/` ou `programmesCPP/` de la matière (seule exception aux fiches à plat), qui liste chaque fichier dans `sources` ; elle donne chaque programme en bloc de code, remet ses commentaires en explications et le relie au chapitre qu'il illustre.
- **Contenu** : complet, pour réviser sans l'original, dans l'ordre du cours : définitions, propriétés et théorèmes (énoncés exacts), formules, méthodes, code et commandes, exemples, exercices avec leur correction si donnée ; en SHS, philosophie, design : thèses, auteurs, citations, cas. Pas de recopie mot à mot. Figures utiles intégrées avec `*Figure : …*` (nommage : `.claude/regles.md`) ; une image de texte se recopie en texte ou LaTeX. En-tête `complet: true`, puis compléter et corriger (voir « Priorité »).

**Synthèses** — `Synthèses/<Titre>.md` : comparaisons, analyses, réponses à conserver.

En-tête (tags `year1` à `year4` : l'année d'une fiche, toutes les années d'une carte ou d'un concept) :

```yaml
---
type: concept          # concept, source, matiere ou synthese
tags: [year2, year4]
aliases: [eigenvalue]                # concepts
matieres: [Bilinear Algebra]         # concepts, mot ambigu seulement
sources: ["[[Raw/Year 2/Probability/Cours 6 - T-Test.docx|Cours 6 - T-Test.docx]]"]
maj: 2026-11-04
---
```

## Liens

- Relier les pages avec `[[...]]`, chaque affirmation à sa source ; `\|` dans un tableau.
- Un document de `Raw/` se lie par son chemin complet : `[[Raw/Year 4/data mining/cours.pdf|cours.pdf]]`. Le lien `sources` d'une fiche permet à la mise à jour de la retrouver : le garder exact.
- Nom contenant `[`, `]`, `#`, `^` ou `|` : l'écrire en texte. Nom contenant celui d'un tiers : ne pas le citer, nommer son dossier (« PDF du brief, dans Raw/Year 3/Projet courts »).

## Opérations

**Intégrer une source** (sur demande ; les changements de Drive passent par `/maj-cours`). Pour une matière entière, faire valider le niveau de détail sur un ou deux documents d'abord.
1. Lire le document et ses transcriptions ; ouvrir une image non transcrite si elle compte.
2. Résumer les points essentiels et les changements prévus (sauf lot déjà validé).
3. Écrire la fiche et ses figures, puis la compléter et la corriger.
4. Créer ou mettre à jour les concepts (y compris ceux des compléments) et la carte, sans doublon.
5. Source qui contredit le wiki : ne pas écraser ; noter le désaccord avec les deux sources et le signaler.
6. Mettre à jour `Accueil.md`, puis `log.md`.

**Répondre à une question** : lire `Accueil.md` puis les pages concernées ; vérifier dans `Raw/` ce qui compte (formule, définition exacte, point absent du wiki), en cherchant les variantes françaises et anglaises (texte non indexé : `convertir.py`, sans rien écrire) ; répondre en citant les pages, sous la forme adaptée (texte, tableau, fiche, quiz), en séparant le cours des ajouts et en disant d'abord si le cours n'en dit rien ; proposer de classer une réponse utile dans `Synthèses/` (puis `Accueil.md` et `log.md`). Une question simple ne modifie aucun fichier.

**Contrôler le wiki (lint)**, sur demande : contradictions et affirmations dépassées, pages sans lien entrant, liens cassés ou ambigus, manques à combler, concepts manquants ou en double, alias trop généraux, pages sans source, sans tag, mal rangées ou absentes d'`Accueil.md`, `sources` qui ne lie rien, documents sans fiche, fiches sans `enrichi:`. Corriger le mécanique, soumettre le reste, journaliser.

## Fiabilité

- Source fiable vérifiée > image d'origine > texte du document > transcription > wiki ; en cas d'écart, le plus fiable l'emporte et l'écart se corrige dans le wiki.
- Aucune mention « À vérifier » dans le wiki : un doute (formule, définition, code, transcription coupée, scan) se tranche aussitôt sur l'image puis le document, sinon le dire à l'utilisatrice. Les remarques mineures ne s'inscrivent pas.
- Autres marques d'ajout : « **Définition (complément, hors du cours)** » en tête d'un concept, « (complément, hors du cours) » ou *Piste* ailleurs.
- Document rédigé ou traduit par un outil : « texte produit par un outil de génération de texte » (ou « traduit avec DeepL »), jamais « généré par une IA » (bloque le commit).

## `Accueil.md` et `log.md`

- `Accueil.md` : catalogue par catégorie, un lien et une ligne de résumé par page, à jour à chaque création ou suppression.
- `log.md` : ajout seul, entrées `## [AAAA-MM-JJ] type | titre` (`ingest`, `query`, `lint`, `import`, `transcription`, `schema`).

## Divers

- `/maj-cours` met à jour depuis Drive (détails dans la commande et `.claude/regles.md`). Tests : `python3 -m unittest discover -s .outils -p 'test_*.py'`. Ne lancer les outils que si la demande l'exige.
- Git versionne le wiki, ses images et les transcriptions, pas `Raw/`. Commit sur demande seulement.
- Ne pas modifier `.obsidian/graph.json` ni `app.json` pendant qu'Obsidian est ouvert ; `app.json` garde `showUnsupportedFiles: true` (sinon les liens vers docx et pptx ne se résolvent pas).
- Chantiers par agents : quatre en parallèle au plus, lots d'une cinquantaine de pages, consigne de reprise ; deux agents ne touchent jamais le même fichier.
