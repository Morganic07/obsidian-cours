---
type: source
sources: ["[[cours TP1]]"]
maj: 2026-11-05
---

Résumé de [[cours TP1]], dans [[Year 2 - Operating System]]. Note de cours sur les bases de l'administration, images lues par transcription seulement.

## Contenu, dans l'ordre du cours

- **Aide** : `man`, `--help`, `info`.
- **sudo** : exécute avec les droits de root sans se connecter en root. Sans mot de passe : ajouter `username ALL=(ALL) NOPASSWD:ALL` avec `sudo visudo`. Délai de mot de passe : `Defaults timestamp_timeout=15`.
- **Mot de passe** : `sudo passwd`. Les mots de passe sont stockés hachés dans `/etc/shadow` et on ne peut pas les relire.
- **Clavier** : `setxkbmap us` (temporaire) ou `XKBLAYOUT` dans `/etc/default/keyboard` (permanent).
- **Nom de machine** : `sudo hostname nouveau` ; rôle (identification, adresse lisible, résolution DNS).
- **Arborescences** : `touch test{1..3}.txt`, `mkdir -p semester/{first/{os,uc},...}`, `tree`.
- **Divers** : `echo "first" | cat > fichier`, `chmod -R` (récursif), `whoami` (utilisateur) vs `hostname` (machine), `cd ..`, `cd ~`, `cd -`, `./`, `shutdown now` / `poweroff`, `uname -r` (version du noyau), `apt upgrade` (n'installe ni ne supprime) vs `apt full-upgrade`. Voir [[Shell et Bash]], [[Permissions Unix]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Délai sudo** : le texte dit 15 minutes mais l'explication entre parenthèses dit 30. La transcription le signale et l'incohérence est bien dans l'image d'origine (vrai signalement, image non rouverte). `timestamp_timeout=15` correspond à 15 minutes (complément).
2. **`sudo chmod -R 444 semester/`** : retire aussi le droit `x` des dossiers, qui ne peuvent alors plus être traversés (complément).
3. **`sudo hostname`** : le changement ne dure que jusqu'au redémarrage ; le fichier `/etc/hostname` rend le changement permanent (complément).
4. **Question 1 « chmod -R »** et renvoi à l'ordre des questions : la numérotation de la note repart à 1 plusieurs fois, ce qui ne permet pas de relier chaque réponse à son énoncé.
