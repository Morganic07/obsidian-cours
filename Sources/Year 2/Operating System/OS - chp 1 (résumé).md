---
type: source
sources: ["[[OS - chp 1]]"]
maj: 2026-11-05
---

Résumé de [[OS - chp 1]], dans [[Year 2 - Operating System]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été rouvertes : tout repose sur les transcriptions.

## Idée générale

Introduction : matériel d'un ordinateur, rôle du [[Système d'exploitation]], communication CPU / mémoire / périphériques, démarrage, stockage et architectures de systèmes.

## Contenu, dans l'ordre du cours

- **Matériel** : tous les ordinateurs ont le même squelette. Carte mère : socket du CPU, emplacements RAM, slots d'extension (PCIe pour carte graphique ou Wi-Fi), stockage SATA ou M.2, alimentation du processeur (2×8 broches) et de la carte. Un serveur a deux alimentations : si l'une tombe, l'autre prend le relais.
- **Processeur** : cycle recherche de l'instruction, interprétation, exécution, écriture du résultat. Un cœur fait une tâche à la fois ; l'hyperthreading simule plusieurs cœurs virtuels (utile pour jeux ou montage vidéo, pas pour un navigateur).
- **Structure** : utilisateur, applications, système, matériel (voir [[Système d'exploitation]]).
- **Bus système** : trois bus. Données (bidirectionnel), adresses (CPU vers mémoire, unidirectionnel), contrôle (signaux d'horloge, demandes d'interruption, bidirectionnel). La RAM reçoit les données que traite le CPU ; le CPU consulte son cache avant la RAM, et le système charge depuis le SSD vers la RAM ce qui manque.
- **Fonctionnement** : chaque périphérique a un contrôleur, un pilote (*driver*) et un tampon (*buffer*). Le contrôleur signale la fin d'une opération par une [[Interruption]]. Exemple du clavier : un petit processeur local convertit la touche en ASCII puis en binaire. Une opération d'E/S suit trois temps : requête, transfert de données, interruption ; le **DMA** permet d'accéder à la RAM sans interrompre le CPU.
- **Démarrage** : le BIOS (en ROM) fait le POST puis charge le système en RAM, voir [[BIOS et UEFI]]. L'appel système est un moyen logiciel de déclencher une interruption ([[Appel système]]).
- **Hiérarchie de stockage** : registres, cache, mémoire principale, mémoire non volatile, disques, optique, bandes ; voir [[Hiérarchie de stockage]].
- **Architectures** : monoprocesseur ; multiprocesseur, symétrique (chaque CPU traite un travail) ou asymétrique (un maître distribue aux esclaves) ; clusters (plusieurs machines, stockage partagé via un SAN, haute disponibilité : en mode asymétrique un nœud *hot-standby* attend une panne, en mode symétrique tous travaillent et se surveillent ; HPC pour le calcul parallèle ; DLM pour verrouiller les ressources partagées).
- **Environnements** : traditionnel, mobile (GPS, gyroscope, iOS et Android), virtuel ([[Machine virtuelle]]), client-serveur (serveur de calcul, serveur de fichiers), cloud, systèmes distribués (réseau de machines hétérogènes donnant l'illusion d'un seul système).

## Annotations de l'étudiant

Le dessin de la section « Computer system operation » ne donne que des mots (RAM, Device controller, Buffer, CPU) : la disposition et les flèches sont perdues. Sur la diapositive des systèmes distribués, l'étudiant écrit qu'il doit encore comprendre l'explication et le schéma. La section « Working of an I/O operation » est marquée « A COMPRENDRE ».

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Texte du dessin « Located in the CPU »** : la note s'arrête là, sans phrase complète. Elle semble désigner les registres et le cache de la hiérarchie de stockage.
2. **« Le buffer se vide dès que la tâche est accomplie »** et « un programme ne peut pas être chargé sur le SSD directement » : formulations approximatives (complément). Un programme est stocké sur le SSD et copié en RAM pour s'exécuter.
3. **Définition du clavier** : « le CPU converti en binary » est simplifiée ; le code ASCII vient du contrôleur du clavier.
4. **À vérifier de la transcription** (trait noir dépassant à gauche du schéma des machines virtuelles) : sans conséquence, fausse alerte pour le contenu.
