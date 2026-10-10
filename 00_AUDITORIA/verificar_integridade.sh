#!/usr/bin/env bash
# ==============================================================================
# TECHDIM INOVA SIMPLES (I.S.) · CNPJ: 61.933.926/0001-24
# Verificador Matemático de Integridade (AIDE / Tripwire Nativo)
# Padrão Canônico: PRJ-TECHDIM-PUBLIC-v1.0.0
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(cd "$SCRIPT_DIR/.." && pwd)"
CHECKSUM_FILE="$SCRIPT_DIR/checksums.sha256"

cd "$RAIZ"

if [[ "${1:-}" == "--gerar" || "${1:-}" == "--update" ]]; then
    echo "🔐 Gerando assinaturas criptográficas SHA-256 para o projeto público..."
    rm -f "$CHECKSUM_FILE"
    
    ARQUIVOS_CRITICOS=(
        "iniciar.sh"
        "03_APLICACAO/src/main.py"
        "project.json"
        "00_AUDITORIA/verificar_integridade.sh"
        "05_VERSOES/git_templates/hooks/pre-commit"
    )
    
    for f in "${ARQUIVOS_CRITICOS[@]}"; do
        if [[ -f "$f" ]]; then
            sha256sum "$f" >> "$CHECKSUM_FILE"
        fi
    done
    
    echo "✓ Assinaturas geradas com sucesso em: $CHECKSUM_FILE"
    exit 0
fi

if [[ ! -f "$CHECKSUM_FILE" ]]; then
    echo "⚠️ Arquivo de assinaturas não encontrado: $CHECKSUM_FILE"
    echo "Execute '$0 --gerar' para criar o arquivo base de integridade."
    exit 1
fi

echo "=============================================================================="
echo "  TECHDIM — Verificação Matemática de Integridade SHA-256 (Repositório Público)"
echo "=============================================================================="

FALHAS=0
while read -r HASH ARQUIVO; do
    if [[ -z "$HASH" || -z "$ARQUIVO" ]]; then
        continue
    fi
    if [[ ! -f "$ARQUIVO" ]]; then
        echo "❌ [FALTA]: Arquivo ausente -> $ARQUIVO"
        FALHAS=$((FALHAS + 1))
        continue
    fi
    
    CALCULADO=$(sha256sum "$ARQUIVO" | awk '{print $1}')
    if [[ "$CALCULADO" == "$HASH" ]]; then
        echo "✅ [OK]: $ARQUIVO"
    else
        echo "🚨 [VIOLAÇÃO]: Integridade violada em -> $ARQUIVO"
        echo "   Esperado : $HASH"
        echo "   Calculado: $CALCULADO"
        FALHAS=$((FALHAS + 1))
    fi
done < "$CHECKSUM_FILE"

echo "------------------------------------------------------------------------------"
if [[ $FALHAS -eq 0 ]]; then
    echo "🛡️  SUCESSO: Todos os arquivos críticos do projeto público estão 100% íntegros."
    exit 0
else
    echo "❌ FALHA CRÍTICA: $FALHAS arquivo(s) apresentaram anomalia de integridade!"
    exit 1
fi
