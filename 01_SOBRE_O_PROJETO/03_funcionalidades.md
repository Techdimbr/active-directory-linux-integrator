<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Funcionalidades (48) — o que cada uma faz e por que importa

> **Inventário Oficial Completo:** Para a listagem exaustiva de todas as 70 capacidades numeradas do organismo, consulte o [CHECKLIST MESTRE DE FUNCIONALIDADES](CHECKLIST_FUNCIONALIDADES_MESTRE.md).

| # | Funcionalidade | Onde vive | Utilidade prática |
|---|---|---|---|
| 1 | Lançador universal | `INICIAR_UNIVERSAL.py` | Um ponto de entrada para Windows/Linux/macOS — o usuário não precisa saber qual script chamar. |
| 2 | Zero instalação | raiz | Copiar a pasta e rodar. Nada é instalado no sistema. |
| 3 | Offline-first | `techdim_core/` | Biblioteca-tronco só com stdlib; funciona sem internet. |
| 4 | Descoberta da RAIZ | `raiz.py` | O organismo acha a si mesmo mesmo se a pasta for renomeada/movida. |
| 5 | Atalhos cross-platform | `INICIO_START/` | `.desktop` (Linux), `.bat` (Windows), `.command` (macOS) para o painel. |
| 6 | Fingerprint da máquina | `maquina.py` | Hash SHA-256 estável para rastreabilidade sem expor MAC/serial. |
| 7 | Física × virtual | `maquina.py` | Detecta VirtualBox/VMware/KVM/Hyper-V por DMI. |
| 8 | Inventário Android | `maquina.py` | Localiza `adb`/`scrcpy`/`fastboot` (PATH ou vendorizado) + versão. |
| 9 | Diagnóstico de ambiente | `diagnostico.sh` → `00_AUDITORIA/DIAGNOSTICO_AMBIENTE.md` | Retrato completo da máquina para anexar a um chamado. |
| 10 | Gate de gravação | `confinamento.py` | Bloqueia qualquer escrita fora da RAIZ, com exceção explícita. |
| 11 | Varredura red-team | `confinamento.varredura_estatica` | Acha `rm -rf /`, fork bombs, tokens, chamadas de rede não declaradas. |
| 12 | Isolamento real | `confinamento.montar_comando_isolado` | Roda subprocessos dentro de `bwrap`/`firejail` quando disponível. |
| 13 | Auditoria de segurança no arranque | `INICIAR_UNIVERSAL.py` | Toda vez que liga, verifica se algo perigoso entrou. |
| 14 | Anti caminho-hardcoded | `auditoria_caminhos.py` | Garante portabilidade: só `$HOME` / `%USERPROFILE%` / `Path.home()`. |
| 15 | Auditoria de estrutura | `auditoria_estrutura.py` | 8 pastas + arquivos-raiz + placeholders esquecidos. |
| 16 | Auditoria de checksums | `auditoria_checksums.py` | Confere SHA-256 de cada dependência vendorizada. |
| 17 | Auditorias de caminhos/segurança/git | `00_AUDITORIA/*.py` | Cada eixo tem um script rodável isolado. |
| 18 | Relatório consolidado | `00_AUDITORIA/AUDITORIA_COMPLETA.md` | Uma tabela + detalhes, gerada a cada auditoria. |
| 19 | Git dentro de 05_VERSOES/ | `05_VERSOES/.git` | Histórico contido numa pasta oficial; worktree = organismo. |
| 20 | auto_commit.py | `05_VERSOES/auto_commit.py` | add + commit convencional + tag + CHANGELOG + VERSION num comando. |
| 21 | CHANGELOG como fonte da verdade | `05_VERSOES/CHANGELOG.md` | Um só lugar define a versão; `VERSION` é derivado. |
| 22 | Estado Quântico | `04_INTELIGENCIA.../ESTADO_ATUAL.json` | Colapso de todos os sinais num veredito 🟢/🟡/🔴 + hash estrutural. |
| 23 | Neural Core | `04_INTELIGENCIA.../06_neural_core/` | Grafo vivo + `memoria_episodica.jsonl` das ações. |
| 24 | Estado do Operador | `07_estado_operador/operador.json` | Foco declarado, sincronia humano-máquina, histórico de intenções. |
| 25 | Painel Interativo | `techdim_core/painel.py` | Centro de comando: saúde, checklist, histórico, 10 ações numeradas. |
| 26 | NOVO_DOMINIO.py | `02_COMO_USAR/NOVO_DOMINIO.py` | Gera um domínio completo já com commit inicial e perfil. |
| 27 | Módulo Comercial + Prova de Integridade | `06_MIDIA/` | Pitch, precificação, Google Ads, roteiro de vídeo, `PROVA_DE_INTEGRIDADE.json`. |
| 28 | i18n do próprio tooling | `techdim_core/i18n.py` + `03_APLICACAO/i18n/` | Painel em pt-BR / en-US / es-ES; `pt-BR` é a fonte da verdade e a paridade de chaves é testada. |
| 29 | Acessibilidade de CLI (WCAG 2.1 AA) | `--a11y` · `--sem-cor` · `02_COMO_USAR/04_acessibilidade.md` | Marcadores textuais, sem box-drawing, `NO_COLOR`; nenhuma informação depende só de cor. |
| 30 | SBOM CycloneDX 1.5 | `techdim_core/sbom.py` → `dependencias/sbom.json` | Inventário assinável de componentes — requisito de contrato B2B e do EU CRA. |
| 31 | Gate de licenças de dependências | `licencas_compativeis.txt` + `sbom.gate_licencas()` | Bloqueia copyleft forte (GPL/AGPL/SSPL) que contaminaria a distribuição proprietária. |
| 32 | Prevenção proativa de segredos | `.secrets.baseline` + `gitleaks.toml` | Complementa a varredura reativa: baseline detect-secrets e regras gitleaks com allowlist. |
| 33 | Documentação LGPD/GDPR | `02_COMO_USAR/03_seguranca_e_privacidade.md` | Dados tratados, base legal, retenção, direitos do titular, `TECHDIM_SEM_ESTADO=1`. |
| 34 | Suíte de testes automatizados | `03_APLICACAO/tests/{unitarios,integracao,e2e,performance,seguranca}/` | 99 testes em `unittest` puro — sem pytest no caminho de execução. |
| 35 | Cobertura de testes stdlib | `executar_testes.py --cobertura` | Usa `coverage` se houver; senão um tracer `sys.settrace`. Meta e resultado em `cobertura_de_testes.md`. |
| 36 | Runner one-click de testes | `iniciar_testes.sh` / `INICIAR_TESTES.bat` | Roda toda a suíte em máquina limpa, sem instalar nada. |
| 37 | Logging estruturado JSON | `techdim_core/registro.py` → `03_APLICACAO/logs/` | JSON lines com rotação 5×1 MB e mascaramento LGPD de `$HOME`/usuário. |
| 38 | Métricas + export Prometheus | `registro.metrica()` → `03_APLICACAO/metricas/` | `metricas.jsonl` + `organismo.prom` para o textfile collector. |
| 39 | Healthcheck /health e /ready | `techdim_core/saude.py` · `healthcheck.py` · `--health` | Liveness e readiness com exit code — usável em orquestrador e CI. |
| 40 | Diagramas C4 + ADRs em arquivo | `04_.../08_arquitetura/` (c4/ + adr/) | 14 ADRs no formato MADR e os 3 níveis C4 em Mermaid (offline) e PlantUML. |
| 41 | Runbooks de incidente | `04_.../09_runbooks/` | 7 procedimentos: auditoria reprovada, checksums, estado vermelho, Git, vazamento, release, CI. |
| 42 | CI/CD stdlib-first | `.github/workflows/ci.yml` · `release.yml` | Matriz Linux/Windows/macOS × Python 3.9–3.12 sem nenhum `pip install`; release empacota e anexa a prova. |
| 43 | Pre-commit local e offline | `.pre-commit-config.yaml` + `05_VERSOES/scripts/` | Auditorias rápidas + testes de segurança antes de cada commit; e `version-bump.sh`. |
| 44 | CHECKLIST OFICIAL executável | `techdim_core/checklist.py` + `00_AUDITORIA/validador_checklist.py` | Fases 0–9 com verificadores reais (`file`/`dir`/`glob`/`grep`/`audit`/`py`/`cmd`); vira a 7ª auditoria e dá score + grade. |
| 45 | Manual Consolidado | `01_SOBRE_O_PROJETO/00_MANUAL_CONSOLIDADO.md` | Documento único: identidade, arquitetura, operação, onboarding < 15 min, qualidade, incidentes. |
| 46 | DX: Makefile, devcontainer, compose | `Makefile` · `.devcontainer/` · `docker-compose.yml` | `make help` lista tudo; container é opcional e nunca requisito. |
| 47 | Kit jurídico-comercial | `06_MIDIA/03_contrato_modelo/` · `04_case_studies/` · `05_materiais_de_vendas/` · `06_comparativo_concorrencia.md` | MSA, DPA e SLA modelo, 2 case studies, one-pager/deck/objeções/preços e matriz concorrencial. |
| 48 | Exportação como Agente de IA | `02_COMO_USAR/EXPORTAR_AGENTE.py` (ações [13] e [14]) | Aplica o organismo como Agente Claude (`.claude/` + `AGENTS.md`) e Antigravity CLI/IDE/2.0 (`.agents/`). |

## Perfis aplicáveis (ação [5] do painel)

| Perfil | Foco | Efeito no domínio Android de exemplo |
|---|---|---|
| **Hardening** | superfície de ataque | desativa depuração USB, revoga autorizações ADB, checa criptografia. |
| **Performance** | fluidez | limpa caches, congela apps de background, ajusta `animator_duration_scale`. |
| **Privacidade** | telemetria | desativa anúncios personalizados, restringe sensores em background. |
| **Gamer** | latência | modo avião seletivo, prioridade de CPU, bloqueio de notificações. |

O perfil ativo fica em `03_APLICACAO/config/perfil_ativo.json`.
