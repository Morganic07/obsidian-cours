---
type: source
tags: [year3]
sources: ["[[chp6 - Access Control List]]"]
maj: 2026-11-05
---

Résumé de [[chp6 - Access Control List]], dans [[Computer Network (matière)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Voir [[Liste de contrôle d'accès]].

## Contenu, dans l'ordre du cours

- **Wildcard mask** : masque de sous-réseau inversé (les 1 deviennent 0 et inversement). Raccourci : retrancher chaque octet du masque à 255. Exemples : /24 donne 0.0.0.255, /28 donne 0.0.0.15, /25 donne 0.0.0.127. Un 0 signifie « doit correspondre », un 1 « peu importe ». L'hôte 192.168.2.1/32 a pour wildcard 0.0.0.0.
- **Entrant et sortant** : le sens est vu depuis le routeur, par interface.
- **ACL** : filtre de paquets, séquence ordonnée d'ACE (Access Control Entries), configurée en mode de configuration globale. Elle peut filtrer sur les adresses source et destination et sur les ports de couche 4. Elle ne prend effet qu'une fois appliquée à une interface, en entrée ou en sortie.
- **Parcours** : le routeur lit les ACE de haut en bas et s'arrête à la première qui correspond. Au plus une ACL par interface et par direction : une seconde remplace la première.
- **Refus implicite** : un `deny` implicite termine toute ACL. Le cours compare trois ACL qui ne diffèrent que par la dernière ligne (aucune, `deny any`, `permit any`).
- **Types** : standard (source seulement, numérotée 1 à 99 et 1300 à 1999, ou nommée), étendue (source, destination, ports, numérotée ou nommée).
- **Syntaxe** : `access-list <numéro> {deny | permit} <ip> <wildcard-mask>` puis, sur l'interface, `ip access-group <numéro> {in | out}`.
- **Où placer une ACL standard** : près de la destination, puisqu'elle ne filtre que la source.
- **TP (cinq exigences)** : 192.168.1.0/24 ne peut pas joindre 10.0.2.0/24, PC3 ne peut pas joindre 10.0.1.0/24, les autres PC du 192.168.2.0/24 le peuvent, PC1 le peut, les autres du 192.168.1.0/24 non. Réponse : sur R2, ACL 10 en sortie de G0/2 et ACL 20 en sortie de G0/1. Méthode : choisir l'équipement, l'interface et le sens pour chaque exigence, puis regrouper dans une même ACL ce qui a les mêmes paramètres.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les images sont lues par leur transcription, aucune ouverte.

1. **Solution du TP, exigence 4** (complément). **À corriger avant un examen.** Le cours place l'exigence 4 (PC1 vers 10.0.1.0/24) sur « R2 : G0/2-out ACL 10 ». Le réseau 10.0.1.0/24 est derrière G0/1, et G0/2 dessert 10.0.2.0/24. Elle devrait donc relever de « R2 : G0/1-out ACL 20 », comme les exigences 2, 3 et 5. L'exigence 1 est bien sur G0/2 en sortie.
2. **« Router R2 » et commandes `R1`** : dans l'image de configuration, le titre « Router R2 » ne correspond pas aux commandes préfixées `R1`. Alerte de la transcription confirmée par le texte, non tranchée sur l'image.
3. **Contenu manquant** : le cours ne donne pas les lignes des ACL 10 et 20 du TP, seulement leur emplacement. Comme l'ACL 20 mélange un hôte (PC3, wildcard 0.0.0.0) et des réseaux, l'ordre des ACE y compte (complément).
4. **Étiquette coupée** : « 192.168.2.0/24 » est coupée par la barre d'outils de la visionneuse sur une image, sans effet sur le contenu.
5. **ICMP** : seule la définition (« Internet Control Message Protocol ») apparaît, sans exemple.
