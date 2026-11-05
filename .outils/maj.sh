#!/usr/bin/env bash
# Récupère les cours depuis Drive (lecture seule), puis régénère les notes.
# Si rclone échoue, on s'arrête : aucune note n'est touchée.
set -euo pipefail

ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MIROIR="$ICI/../raw"
mkdir -p "$MIROIR"

# --bind 0.0.0.0 force l'IPv4 : l'IPv6 ne joint pas les serveurs Google sur cette machine.
rclone sync "gdrive:CY Tech" "$MIROIR" \
  --drive-export-formats docx,pptx \
  --filter "- Year 2/Administration/**" \
  --filter "+ *.{docx,pdf,pptx}" --filter "- *" --ignore-case \
  --bind 0.0.0.0

python3 "$ICI/convertir.py" --miroir "$MIROIR" "$@"
