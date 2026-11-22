---
description: Récupère les cours depuis Google Drive et met le wiki à jour
---

Mets le coffre à jour depuis Google Drive, puis intègre au wiki ce qui a changé. Suis `CLAUDE.md`.

## 1. Récupérer et préparer le lot

Lance `bash .outils/maj.sh` depuis la racine du coffre. Il synchronise `Raw/` avec Drive, puis prépare le lot hors du coffre, sans rien écrire dans le wiki.

- **Code 0** : le lot est prêt, ou « Aucun changement sur Drive » : dans ce cas, dis-le en une phrase et arrête-toi.
- **Code 3 (lot non clos)** : un lot précédent n'a pas été intégré. Dis-le à l'utilisatrice et demande-lui s'il faut l'intégrer d'abord (`bash .outils/maj.sh --reprendre`, puis la suite de cette commande) ou l'abandonner (`bash .outils/maj.sh --clore`, ce qui perd les anciennes versions gardées). Ne choisis pas à sa place.
- **Code 4 (plus de 50 images à transcrire)** : annonce leur nombre et demande l'accord, car la transcription consomme beaucoup d'usage. Avec l'accord : `python3 .outils/transcrire.py`, puis `bash .outils/maj.sh --reprendre`. Sans l'accord : `bash .outils/maj.sh --reprendre --sans-transcrire`.
- **Erreur d'authentification de rclone** (jeton expiré ou refusé) : arrête-toi et demande à l'utilisatrice de lancer `! rclone config reconnect gdrive: --bind 0.0.0.0`, puis de relancer `/maj-cours`.
- **« Sans extension sur Drive »** dans la sortie : un document déposé sur Drive sans extension dans son nom a été repris d'après son type, sous son nom suivi de l'extension (lien et fiche utilisent ce nom). « ignoré » signale un tel document écarté parce que Drive porte déjà un fichier du même nom avec l'extension, « écarté par exclusions.local » un document que les filtres refusent : cite les deux dans le compte rendu (le second peut être voulu, ou trahir un nom mal lu).
- **Code 1 avec un lot écrit** : certains documents n'ont pas pu être convertis ; le bilan les marque « échec de conversion ». Continue avec les autres et signale-les.
- Toute autre erreur : montre-la et arrête-toi.

## 2. Lire le bilan

Lis `lot/BILAN.md` (le chemin est affiché à la fin de la sortie). Il liste les documents ajoutés, modifiés, déplacés et supprimés, avec leur fiche existante. Chaque document a son fichier dans `lot/` : état, chemin dans `Raw/`, année, fiche existante ou dossier de fiches probable, concepts existants repérés, changements du texte (pour un document modifié), texte converti avec les transcriptions des images, et dossier de ses images.

Si une matière a plus de 5 documents changés, ou si plus de 15 documents ont changé en tout, présente d'abord la liste à l'utilisatrice et demande-lui par quoi commencer.

## 3. Mettre le wiki à jour

Pour chaque fichier du lot :

- **Sans fiche, mais le lot liste des « fiches qui citent son dossier sans le lier »** : regarde d'abord si l'une d'elles est la sienne (document dont le nom porte celui d'un tiers). Si oui, traite-le comme un document modifié de cette fiche, sans écrire de doublon ; dans le doute, demande.
- **Tri et nommage, avant toute fiche** : applique les règles de `CLAUDE.md` (section Wiki : rangement des dossiers, nom `<N> - <Titre>`, documents sans fiche). Un document sans fiche selon ces règles (TD, exercices, contrôles, rendus, entretiens, anglais…) n'en reçoit pas : signale-le dans le compte rendu. Un document modifié qui n'avait pas de fiche le 2026-11-07 reste sans fiche. En cas de doute sur la catégorie ou le numéro, demande à l'utilisatrice.
- **Ajouté** : écris sa fiche selon « Intégrer une source » de `CLAUDE.md`, sous le nom donné par les règles de nommage, dans le dossier de fiches indiqué (ou celui de sa matière, `Cours/<Domaine>/<Matière>/` ; une matière nouvelle va dans le domaine de son contenu, voir `CLAUDE.md`), avec le tag de l'année du lot et le lien du document dans `sources` (ligne « Lien à mettre dans la fiche »). Copie les figures depuis le dossier d'images du lot vers `Cours/<Domaine>/<Matière>/images/<Nom de la fiche> - imageN.png`. Un PDF : lis le texte du lot, et n'ouvre une page en image que si le texte est illisible. Un PPTX : lis le fichier directement.
- **Modifié** : corrige la fiche existante **d'après les changements du lot seulement**. Ne la réécris pas : elle contient des corrections faites à la main. Garde les corrections d'erreurs du cours déjà faites dans la fiche (voir `log.md`) : le nouveau texte ne doit pas réintroduire une erreur corrigée. Corrige directement toute nouvelle erreur, avec la marque ✎ (ancrée sur la puce de la page dans `Erreurs du cours.md`, à créer ou compléter) (voir « Fiabilité » dans `CLAUDE.md`). Dans les changements, une image est désignée par l'empreinte de son contenu (`![[image <empreinte>]]`) : Google renumérote les images à chaque export, une image dont seul le numéro change n'est pas un changement. Pour une image nouvelle ou remplacée : copie-la depuis le dossier d'images du lot dans `images/` sous un nom **libre** (`<Nom de la fiche> - imageN.png`, en ajoutant un suffixe si le nom est déjà pris : les copies existantes portent les numéros d'un ancien export, et en écraser une casserait une autre figure). La ligne « Images retirées ou remplacées » donne la copie de la fiche qui montrait l'ancien contenu : remplace son intégration par la nouvelle copie, ou retire-la si l'image a disparu du document. Ne supprime pas l'ancienne copie sans le dire. Mets à jour `maj` dans l'en-tête.
- **Déplacé** : même contenu, nouveau chemin. Remplace l'ancien lien `[[Raw/…]]` par le nouveau dans `sources` de la fiche et dans les pages listées par le lot. Si le document a changé de matière, demande avant de déplacer la fiche.
- **Supprimé** : ne supprime rien. Signale à l'utilisatrice sa fiche et les pages listées qui la lient ou citent le document, et demande quoi en faire.
- **Enrichir, pour chaque document ajouté ou modifié** (priorité de `CLAUDE.md`, section « Priorité : enrichir le cours ») : une fois le cours repris, relis la fiche en te demandant ce qu'il faut savoir sur ce sujet que la note n'a pas noté, et complète-la directement dans le texte, là où l'ajout sert, chaque passage ajouté finissant par `[[Complément hors du cours|ⓘ]]` (pas d'encadré) ; puis mets `enrichi:` à la date du jour. Pour un document modifié, enrichis au moins les parties nouvelles. Sans objet pour les documents sans fiche, les projets de design et les notes de travail de groupe (seulement leurs concepts).
- Pour chaque document ajouté ou modifié : crée ou complète les concepts concernés, en partant de la liste des concepts repérés (pas de doublon sous un autre nom), **et ceux qu'appellent les compléments**, puis la carte de la matière. Lier **densément**, selon la règle « Concepts, densément » de `CLAUDE.md` : chaque notion nommée dans la fiche (cours ou complément, personnes exceptées) est liée et a sa page, au moins 50 concepts distincts pour une fiche d'une centaine de lignes. L'utilisatrice a dû le redemander plusieurs fois : c'est une condition pour rendre la fiche, pas une option. Si l'écriture est confiée à des agents, recopie-leur cette règle et le seuil, et compte les liens distincts de chaque fiche à leur retour.
- Si le lot signale un tableau resté en HTML ou un échec de conversion, ouvre le document lui-même pour cette partie.
- **Matière nouvelle** (dossier de `Raw/` qu'aucun concept ne cite encore dans `matieres`) : les concepts dont `matieres` est limité ne sont pas cherchés dans ses documents. Cherche dans le texte de ces documents les noms et les `aliases` de ces concepts, lis chaque passage trouvé, et propose à l'utilisatrice d'ajouter la nouvelle matière à `matieres` pour ceux qui y sont employés dans le même sens. N'élargis rien sans son accord.

## 4. Conclure

- Mets à jour `Accueil.md` (pages créées, nombre de documents de `Raw/` dans « Sources disponibles »), puis ajoute à `log.md` une entrée `## [AAAA-MM-JJ] import | Mise à jour depuis Drive`.
- Donne à l'utilisatrice un compte rendu : documents changés, fiches écrites ou mises à jour, ce que l'enrichissement a ajouté, concepts créés ou complétés, documents supprimés à décider, nouveaux points à vérifier dans ses cours, et ce qui reste à faire.
- Une fois qu'elle a validé le résultat, propose de clore le lot (`bash .outils/maj.sh --clore`). Tant qu'il n'est pas clos, la mise à jour suivante est bloquée.
- Ne commite pas et n'envoie rien : propose le commit, sans le faire. L'utilisatrice valide avant tout commit.
