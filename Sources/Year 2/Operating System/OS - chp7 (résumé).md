---
type: source
sources: ["[[OS - chp7]]"]
maj: 2026-11-05
---

Résumé de [[OS - chp7]], dans [[Year 2 - Operating System]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été rouvertes.

## Idée générale

Les processus : ce qu'ils sont, leur mémoire, leurs états, leur ordonnancement, leur création et leur fin.

## Contenu, dans l'ordre du cours

- **Concept** : un [[Processus]] est un programme en exécution. Un seul flux d'instructions par processus.
- **Mémoire** : text, data, heap, stack, avec l'exemple d'un programme C (`int x;`, `int y = 15;`, `malloc`). Voir [[Processus]].
- **États** : new, ready, running, waiting, terminated ; voir [[États d'un processus]]. Les processus I/O bound passent leur temps en attente, les CPU bound en exécution. Le dispatcher réalise le passage ready vers running.
- **PCB** : [[Bloc de contrôle de processus]].
- **Ordonnancement** : files d'attente et trois ordonnanceurs (LTS, STS, MTS) ; voir [[Ordonnancement des processus]].
- **Changement de contexte** : [[Changement de contexte]].
- **Mobile** : iOS (un seul processus au premier plan à l'origine) et Android (services en arrière-plan).
- **Opérations** : création avec `fork()`, `exec()`, `wait()`, terminaison avec `exit()` et `abort()`, terminaison en cascade ; voir [[Création et terminaison de processus]]. Zombie et orphelin : [[Processus zombie et orphelin]]. Un programme C exemple fait `fork`, `execlp("/bin/ls")` dans le fils, `wait(NULL)` dans le parent. Arbre de processus A, B, C, D, E, F, G, H, I.
- **Chrome multiprocessus** : browser, renderer, plug-in.

## Annotations de l'étudiant

Annotations du dessin sur la mémoire : taille allouée dans la RAM, mémoire dynamique (peut grandir ou rétrécir), zones fixes ou dynamiques. Annotation sur les états : « Storage ; RAM ; RAM ; CPU ; LT scheduler », mots sans leurs flèches, donc sans doute le trajet disque vers RAM vers CPU de l'ordonnanceur à long terme. Sur les files : une tranche de temps expirée renvoie le processus en ready queue ; il emprunte l'une des quatre files.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Surlignage du dispatcher** : trois phrases en surbrillance dans la note ; elles sont cohérentes avec le reste.
2. **« Zombie occupe la mémoire »** : plus exactement, une entrée de la table des processus (complément).
3. **Orphelin** : le rattachement à `init` est donné comme général (« généralement »), c'est exact.
4. **Fausse alerte de la transcription** : « argc, agrv » sur le schéma de mémoire est bien une faute dans l'image, qui n'a pas de conséquence ; le code utilise `argv`.
5. **Exemple C** : il appelle `wait` sans inclure `<sys/wait.h>` (complément) ; sans conséquence pour le cours.
