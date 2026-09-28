#!/bin/bash
# Conta selos de verificação na biblioteca canônica MAIS NOVA desta pasta (vN automático).
# Local deste script: <mecanismo>/ferramentas_geracao/auditoria/  -> mecanismo = 2 níveis acima
DIR="$(cd "$(dirname "$0")/../.." && pwd)"
f=$(ls "$DIR"/Biblioteca_*_CANONICA.md 2>/dev/null | sort -t_ -k2 -V | tail -1)
if [ -z "$f" ]; then echo "Nenhuma biblioteca canônica em $DIR"; exit 0; fi
echo "Biblioteca ativa: $(basename "$f")"
echo "=== selos de verification_status na PROSA ==="
for s in "[VERIFICADO]" "[PRÉ-CLÍNICO]" "[EXTRAPOLADO: animal/célula→humano]" "[EMERGENTE]" "[CONTROVERSO]" "[APENAS PRÉ-CLÍNICO]"; do
  echo "  '$s': $(grep -F -c -- "$s" "$f")"
done
