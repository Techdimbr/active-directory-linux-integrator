<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
## O que muda

<!-- descreva a mudança em 1-2 frases -->

## Checklist do contribuidor

- [ ] `./iniciar_testes.sh --cobertura` verde e cobertura >= meta
- [ ] `python3 00_AUDITORIA/AUDITORIA_COMPLETA_runner.py` APROVADO
- [ ] `python3 00_AUDITORIA/validador_checklist.py .` sem FAIL novo
- [ ] `techdim_core/` continua stdlib-only (se toquei nele)
- [ ] Novo `.md`/script com cabecalho + `ID-TECHDIM`
- [ ] Decisao arquitetural? adicionei um ADR em `08_arquitetura/adr/`
- [ ] Commit via `05_VERSOES/auto_commit.py` (Conventional Commits)
