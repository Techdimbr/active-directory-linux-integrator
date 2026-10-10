---
name: projeto-padrao
description: Instruções de desenvolvimento e arquitetura do Projeto Padrão TECHDIM.
---

# Skill: Projeto Padrão TECHDIM (GitHub Público)

## Diretrizes de Operação:
1. Respeitar os 7 diretórios canônicos numerados (00 a 06).
2. Manter estritamente a política Zero Leaks (sem commits de `.env` ou chaves privadas).
3. Todo código principal reside em `03_APLICACAO/src/` e seus testes em `03_APLICACAO/tests/`.
4. Verificar integridade via `./00_AUDITORIA/verificar_integridade.sh` antes de qualquer entrega.
