---
type: source
tags: [year2]
sources: ["[[Commandes Shell + explications]]"]
maj: 2026-11-05
---

Résumé de [[Commandes Shell + explications]], dans [[Operating System (matière)]]. Fiche de référence de l'étudiant, sans images à ouvrir sauf une capture de `shuf` (transcription seule lue).

## Contenu, dans l'ordre de la fiche

- **Tableau de commandes** : `cat /etc/shells`, `which`, `rm`, `rmdir` (dossier vide), `ls`, `cd`, `nano`, `sh fichier.sh` (exécute avec l'interpréteur de `sh`), `./fichier.sh` (respecte le shebang, exige la permission d'exécution), `apt update` / `upgrade`, `date`, `pwd`, `whoami`, `mkdir`, `echo`, `sudo su`, `touch` (crée ou met à jour l'horodatage), `read`, `grep`, `wc`, `sort -g`, `uniq`, `jobs`, `ping`, `free -h`, `df -h`, `lscpu`, `lshw`. Voir [[Shell et Bash]].
- **`cat`** et **`chmod`** : tableaux d'usages, voir [[Permissions Unix]].
- **Langage Bash** : substitution `$(...)`, variables, `read -p` / `-s` / `-a`, `if`, `elif`, `while`, `for`, ET / OU, tests d'entiers et de chaînes ; voir [[Script Bash]]. Attention aux espaces autour de `=` (interdits) et de `[ ]` (obligatoires). `[ ]` pour les chaînes et fichiers, `(( ))` pour l'arithmétique.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`sh testfile.sh` « avec l'interpréteur bash »** : sous Debian et Ubuntu, `sh` pointe en général vers `dash`, pas Bash (complément). **À corriger avant un examen.**
2. **Exemple des tableaux** : `read -a names` puis `${name[0]}` : le nom de la variable est différent (`names` / `name`), l'affichage serait vide (complément).
3. **Exemple `Name="… est la bonne orthographe`** : guillemet non fermé, cité comme contre-exemple de syntaxe ; la phrase est mal formulée.
4. **Exemples écrits avec des guillemets typographiques** (`“`, `”`) : ils ne fonctionnent pas dans un vrai script.
5. **Ligne `0` isolée** dans l'explication de `$(...)`, probablement un reste de mise en page.
