#!/usr/bin/env bash
# Récupère les cours depuis Drive (lecture seule), puis régénère les notes.
# Si rclone échoue, on s'arrête : aucune note n'est touchée.
set -euo pipefail

ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Les noms de dossiers viennent de chemins.py. rclone sync efface dans la cible tout
# ce qui n'est pas sur Drive : un nom vide ferait de la racine du coffre la cible.
NOM_MIROIR="$(python3 "$ICI/chemins.py" MIROIR)"
NOM_EXCLUSIONS="$(python3 "$ICI/chemins.py" EXCLUSIONS)"
for nom in "$NOM_MIROIR" "$NOM_EXCLUSIONS"; do
  if [[ -z "$nom" || "$nom" == "." || "$nom" == ".." || "$nom" == */* ]]; then
    echo "erreur : nom de dossier invalide dans chemins.py : « $nom »" >&2
    exit 1
  fi
done
MIROIR="$ICI/../$NOM_MIROIR"
mkdir -p "$MIROIR"
JOURNAL="$(mktemp)"
trap 'rm -f "$JOURNAL"' EXIT

# --bind 0.0.0.0 force l'IPv4 : l'IPv6 ne joint pas les serveurs Google sur cette machine.
if ! rclone sync "gdrive:CY Tech" "$MIROIR" \
  --drive-export-formats docx,pptx \
  --filter-from "$ICI/$NOM_EXCLUSIONS" --ignore-case \
  --bind 0.0.0.0 \
  -v --stats-log-level DEBUG >"$JOURNAL" 2>&1; then
  cat "$JOURNAL" >&2
  echo "erreur : rclone a échoué, aucune note n'est touchée" >&2
  exit 1
fi

# Fichiers de Drive ajoutés, remplacés ou supprimés, y compris les PDF et PPTX.
grep -E ': (Copied|Updated|Deleted)' "$JOURNAL" | sed -E 's/^.*INFO *: */drive : /' || true

python3 "$ICI/convertir.py" --miroir "$MIROIR" "$@"
