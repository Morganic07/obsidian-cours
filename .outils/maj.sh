#!/usr/bin/env bash
# Récupère les cours depuis Drive (lecture seule), puis régénère les notes.
# Si rclone échoue, on s'arrête : aucune note n'est touchée.
set -euo pipefail

ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MIROIR="$ICI/../raw"
mkdir -p "$MIROIR"
JOURNAL="$(mktemp)"
trap 'rm -f "$JOURNAL"' EXIT

# --bind 0.0.0.0 force l'IPv4 : l'IPv6 ne joint pas les serveurs Google sur cette machine.
if ! rclone sync "gdrive:CY Tech" "$MIROIR" \
  --drive-export-formats docx,pptx \
  --filter-from "$ICI/exclusions.local" --ignore-case \
  --bind 0.0.0.0 \
  -v --stats-log-level DEBUG >"$JOURNAL" 2>&1; then
  cat "$JOURNAL" >&2
  echo "erreur : rclone a échoué, aucune note n'est touchée" >&2
  exit 1
fi

# Fichiers de Drive ajoutés, remplacés ou supprimés, y compris les PDF et PPTX.
grep -E ': (Copied|Updated|Deleted)' "$JOURNAL" | sed -E 's/^.*INFO *: */drive : /' || true

python3 "$ICI/convertir.py" --miroir "$MIROIR" "$@"
