<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Contribuindo com o Protocolo TECHDIM

Guia resumido; o detalhado vive em `02_COMO_USAR/05_contribuindo.md`.

1. Nunca escreva fora da RAIZ. Use `techdim_core.confinamento.escrever_texto()`.
2. `techdim_core/` e' **stdlib pura** — zero dependencia de terceiros no caminho de execucao.
3. Rode antes de commitar: `./iniciar_testes.sh` e `python3 00_AUDITORIA/AUDITORIA_COMPLETA_runner.py`.
4. Commits via `python3 05_VERSOES/auto_commit.py "<descricao>" --tipo <feat|fix|docs|test|build|chore>`.
5. Decisao arquitetural nao-trivial => novo ADR em `04_INTELIGENCIA_DE_DESENVOLVIMENTO/08_arquitetura/adr/`.
6. Todo `.md` e script novo começa com o cabecalho e a linha `ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0`.
