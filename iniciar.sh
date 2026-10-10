#!/usr/bin/env bash
# ==============================================================================
# TECHDIM INOVA SIMPLES (I.S.) · CNPJ: 61.933.926/0001-24
# Lançador Portátil Universal & Bootstrap Inteligente (Debian 13 Trixie/Sid)
# Padrão Canônico: PRJ-TECHDIM-PADRAO-v9.9.9
# ==============================================================================
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

REQ_FILE="$DIR/03_APLICACAO/requirements.txt"
VENV_DIR="$DIR/03_APLICACAO/.venv"
if [[ ! -d "$VENV_DIR" && -d "$DIR/.venv" ]]; then
    VENV_DIR="$DIR/.venv"
fi

# Bootstrap condicional de dependências
if [[ -f "$REQ_FILE" ]]; then
    # Projeto requer bibliotecas externas
    if [[ ! -d "$VENV_DIR" ]]; then
        echo "📦 [BOOTSTRAP]: Ambiente virtual não detectado. Criando ambiente isolado em $VENV_DIR..."
        python3 -m venv "$VENV_DIR"
        echo "📥 [BOOTSTRAP]: Instalando dependências de $REQ_FILE..."
        "$VENV_DIR/bin/pip" install --quiet --upgrade pip
        "$VENV_DIR/bin/pip" install --quiet -r "$REQ_FILE"
        echo "✓ [BOOTSTRAP]: Dependências instaladas com sucesso."
    fi
    PYTHON_EXEC="$VENV_DIR/bin/python"
else
    # Projeto em Python puro (stdlib) - boot instantâneo (< 1s)
    PYTHON_EXEC="/usr/bin/python3"
    if [[ ! -x "$PYTHON_EXEC" ]]; then
        PYTHON_EXEC="$(command -v python3 || command -v python)"
    fi
fi

# Executa ponto de entrada universal da TECHDIM
if [[ -f "$DIR/INICIAR_UNIVERSAL.py" ]]; then
    exec "$PYTHON_EXEC" "$DIR/INICIAR_UNIVERSAL.py" "$@"
elif [[ -f "$DIR/03_APLICACAO/src/main.py" ]]; then
    exec "$PYTHON_EXEC" "$DIR/03_APLICACAO/src/main.py" "$@"
else
    echo "⚠️ Nenhum ponto de entrada padrão encontrado (INICIAR_UNIVERSAL.py ou src/main.py)." >&2
    exit 1
fi
