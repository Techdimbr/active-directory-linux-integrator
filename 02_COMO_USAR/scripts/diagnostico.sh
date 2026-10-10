#!/bin/bash
# TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br
# ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0
# Diagnóstico completo de ambiente + auditoria, sem abrir o painel.
set -e
cd "$(dirname "$0")"
PY="$(command -v python3 || command -v python)"
"$PY" INICIAR_UNIVERSAL.py --diagnostico
"$PY" INICIAR_UNIVERSAL.py --auditoria
echo
echo "Relatórios em 00_AUDITORIA/"
