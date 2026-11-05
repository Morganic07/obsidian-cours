---
type: source
sources: ["[[OS - chp 5]]"]
maj: 2026-11-05
---

Résumé de [[OS - chp 5]], dans [[Year 2 - Operating System]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été rouvertes.

## Idée générale

Premières commandes Linux : le shell, `cat`, les permissions, les éditeurs, APT et les scripts Bash.

## Contenu, dans l'ordre du cours

- **Shell** : programme d'interface qui interprète les commandes ; Bash par défaut sur Debian/Ubuntu. Voir [[Shell et Bash]]. La sortie de `cat /etc/shells` est reproduite, avec la remarque que `/bin` contient l'essentiel au démarrage.
- **`cat`** : afficher (`cat f`, `-n` pour numéroter), créer (`cat > f`, fin par Ctrl+D), concaténer (`cat f1 f2 > f3`). `rm` supprime.
- **Permissions** : lecture de `ls -l`, valeurs octales, `chmod` ; voir [[Permissions Unix]]. `sudo nano fichier.sh` crée ou ouvre un fichier ; Ctrl+O sauvegarde, Ctrl+X quitte.
- **Éditeurs** : nano, Vim, Gedit.
- **APT** : `apt update` récupère les listes de paquets, `apt upgrade` installe les nouvelles versions.
- **Script Bash** : commence par le shebang `#!/bin/bash` ; voir [[Script Bash]]. Un lien vers un guide des options est donné.

## Annotations de l'étudiant

Il note que `chmod +w` n'ajoute l'écriture qu'au propriétaire sur sa machine, et suppose un défaut de son Debian.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Nombre de liens : liens symboliques »** : la colonne de `ls -l` compte les liens physiques (*hard links*), pas les liens symboliques (complément).
2. **`chmod +w` « visiblement pas les autres »** : comportement normal dû au masque `umask`, pas à un défaut de Debian (complément).
3. **Exemple 703** : « droit d'exécuter et d'écrire aux autres membres » est juste (3 = w+x).
