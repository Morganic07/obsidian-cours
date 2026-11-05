---
type: source
sources: ["[[OS - chp 3]]"]
maj: 2026-11-05
---

Résumé de [[OS - chp 3]], dans [[Year 2 - Operating System]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été rouvertes.

## Idée générale

Linux, ses distributions, Ubuntu et l'installation d'un système.

## Contenu, dans l'ordre du cours

- **Linux** : famille de systèmes libres fondés sur le [[Noyau]] Linux, qui n'est pas un système complet.
- **Distribution** : [[Distribution Linux]] (Ubuntu, Fedora, Arch, Debian, CentOS, openSUSE).
- **Ubuntu** : versions Desktop et Server, publications LTS et interim.
- **Installation** : image ISO, partitions nécessaires (swap, racine, EFI, zone BIOS, /home) ; voir [[Système de fichiers]].
- **Arbre de décision** : sur PC, obtenir l'ISO, créer une clé USB bootable avec Rufus, démarrer dessus, installer. Sur machine virtuelle, choisir le logiciel selon l'hôte (VirtualBox pour Windows, KVM pour Ubuntu), créer la machine, obtenir l'ISO, installer ; la clé n'est pas nécessaire. KVM = Kernel Virtual Machine. Voir [[Machine virtuelle]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Mac OS est construit sur le noyau Linux »** : texte lu dans la note. C'est faux (macOS a un noyau d'origine BSD/Mach), complément. **À corriger avant un examen.**
2. **Durée du support LTS** : « 3-4 ans » ; le cours Ubuntu officiel parle plutôt de 5 ans (complément, non établi par la note).
3. **Interim release** : support de 9 mois selon la note ; à comparer avec le cours.
