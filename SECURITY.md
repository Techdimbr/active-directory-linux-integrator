<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Política de Segurança — Protocolo TECHDIM

## Versões suportadas

| Versão do organismo | Suporte de segurança |
|---------------------|----------------------|
| 2.2.x               | ✅ ativa              |
| 2.1.x               | ✅ correções críticas |
| < 2.1               | ❌ sem suporte        |

A versão vigente está em `VERSION` e no topo de `05_VERSOES/CHANGELOG.md`.

## Divulgação responsável

Encontrou uma vulnerabilidade? **Não abra issue pública nem PR.**

1. Envie e-mail para **security@techdim.com.br** com o assunto `[VULN] Protocolo TECHDIM`.
2. Inclua: descrição, impacto, passos de reprodução, versão (`VERSION`), SO/arquitetura
   (saída de `./diagnostico.sh` ajuda), e um PoC mínimo se houver.
3. Se possível, cifre o relatório com a chave PGP publicada em `https://www.techdim.com.br/.well-known/security.txt`.

### Prazos (SLA de divulgação)

| Etapa | Prazo |
|-------|-------|
| Confirmação de recebimento | 48 h úteis |
| Triagem e classificação de severidade (CVSS 3.1) | 5 dias úteis |
| Correção de severidade **crítica/alta** | 30 dias corridos |
| Correção de severidade **média/baixa** | próximo ciclo de release |
| Divulgação coordenada | após correção publicada, ou 90 dias (o que ocorrer antes) |

Reconhecemos publicamente quem reporta (opt-in) em `05_VERSOES/CHANGELOG.md`.

## Escopo

**No escopo:** `techdim_core/`, lançadores, scripts de `00_AUDITORIA/` e `05_VERSOES/`,
`03_APLICACAO/src/`, o gate de confinamento, o baixador de dependências.

**Fora do escopo:** ferramentas de terceiros vendorizadas (reportar ao upstream;
ver `03_APLICACAO/dependencias/sbom.json`); engenharia social; ataques que exijam
acesso físico já privilegiado à máquina; a ausência de sandbox quando o host não
tem `bwrap`/`firejail` (comportamento documentado e degradação intencional).

## Modelo de segurança do organismo

- **Confinamento:** toda escrita passa por `techdim_core.confinamento.exigir_dentro_da_raiz()`.
- **Sem rede no caminho de execução:** único ponto autorizado é
  `03_APLICACAO/dependencias/baixar_dependencias.py`, declarado em
  `confinamento.REDE_DECLARADA` e com verificação SHA-256 obrigatória.
- **Sem credenciais:** varredura estática a cada arranque (`auditoria_seguranca.py`)
  + `.secrets.baseline` + `gitleaks.toml`.
- **Isolamento real:** subprocessos via `bwrap`/`firejail` quando disponíveis.
- **Auditoria imutável:** `00_AUDITORIA/` roda a cada inicialização.

## Reporte de dados pessoais / LGPD

Questões de privacidade e tratamento de dados: **dpo@techdim.com.br**.
Ver `02_COMO_USAR/03_seguranca_e_privacidade.md`.
