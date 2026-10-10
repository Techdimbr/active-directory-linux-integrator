#!/bin/bash
# TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br
# ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0
# Suite de testes do organismo (unittest puro; sem pytest).
set -e
cd "$(dirname "$0")"
PY="$(command -v python3 || command -v python)"
exec "$PY" 03_APLICACAO/tests/executar_testes.py "$@"
