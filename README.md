# 🏛️ Active Directory Linux Integrator (`PRJ-TECHDIM-PUBLIC-v1.0.0`)

<p align="center">
  <img src="icone.svg" width="80" alt="TECHDIM Logo" />
</p>

<p align="center">
  <a href="https://www.debian.org"><img src="https://img.shields.io/badge/OS-Debian%2013%20(Trixie%2FSid)-A81D33?style=flat-square&logo=debian&logoColor=white" alt="Debian 13" /></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.11%2B%20(Stdlib)-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+" /></a>
  <a href="04_INTELIGENCIA_DE_DESENVOLVIMENTO/adrs/ADR-0001-arquitetura-atomica.md"><img src="https://img.shields.io/badge/Architecture-Atomic%20Box-0052CC?style=flat-square" alt="Architecture" /></a>
  <a href="05_VERSOES/git_templates/hooks/pre-commit"><img src="https://img.shields.io/badge/Zero%20Leaks-Verified-2ea44f?style=flat-square&logo=shield" alt="Zero Leaks" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License MIT" /></a>
  <a href="https://cloud.google.com"><img src="https://img.shields.io/badge/Google%20Cloud-Ready-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="Google Cloud Ready" /></a>
  <a href="https://techdimbr.github.io/techdimbr/"><img src="https://img.shields.io/badge/GitHub%20Pages-Live%20Showcase-0969DA?style=flat-square&logo=github&logoColor=white" alt="GitHub Pages" /></a>
</p>

<p align="center">
  <img src="06_MIDIA/banner_oficial.png" width="100%" alt="TECHDIM Banner" />
</p>

> **Propriedade:** TECHDIM INOVA SIMPLES (I.S.) · CNPJ: 61.933.926/0001-24  
> **Doutrina:** Kether_1 · Central de Engenharia, Ciberdefesa e Governança Soberana  
> **Identificador Canônico:** `PRJ-TECHDIM-PUBLIC-v1.0.0`

---

## 🇧🇷 Visão Geral (Português)

O **Padrão Canônico TECHDIM GitHub Público** é o template de arquitetura corporativa para desenvolvimento open-source e B2B da TECHDIM. Ele estrutura sistemas como uma **Caixa-Preta Atômica** (organismo autocontido, offline-first e determinístico), garantindo que qualquer desenvolvedor ou auditor possa clonar, verificar a integridade matemática e executar a aplicação instantaneamente.

### Destaques da Engenharia
- **Filosofia de Caixa-Preta Atômica:** Ciclo de vida previsível em 7 diretórios numéricos canônicos (`00` a `06`).
- **Prova Matemática de Integridade (AIDE/Tripwire):** Verificação SHA-256 nativa de scripts e manifestos via `00_AUDITORIA/verificar_integridade.sh`.
- **Barreira Zero Leaks:** Hook pré-commit nativo que bloqueia envio acidental de arquivos `.env`, chaves privadas e tokens de nuvem.
- **Prontidão Nativa para Agentes de IA:** Diretrizes universais em `AGENTS.md`, `GEMINI.md`, `CLAUDE.md` e `.agents/skills/`.
- **Bootstrap Inteligente:** Inicialização instantânea (< 1s) para módulos em Python puro (stdlib) e isolamento automático em `.venv` quando dependências externas forem requeridas.

---

## 🇺🇸 Executive Summary (English)

The **TECHDIM Canonical Standard for Public GitHub Repositories** is an enterprise-grade architectural blueprint designed to build software as an **Atomic Black Box** (self-contained, offline-first, and deterministic). Engineered for mission-critical reliability, it enforces a strict 7-tier decimal directory lifecycle (`00` through `06`) with native mathematical integrity checks and multi-agent AI orchestration.

---

## 📐 Arquitetura Canônica / Directory Architecture

```text
active-directory-linux-integrator/
├── 00_AUDITORIA/                       # Rastreabilidade, checksums.sha256 e verificação AIDE
├── 01_SOBRE_O_PROJETO/                 # Visão de negócio, dores resolvidas e diagramas
├── 02_COMO_USAR/                       # Guias de instalação, manuais e scripts operacionais
├── 03_APLICACAO/                       # Código-fonte executável (src/), testes (tests/) e assets
├── 04_INTELIGENCIA_DE_DESENVOLVIMENTO/ # ADRs (Architecture Decision Records) e referências
├── 05_VERSOES/                         # Histórico de releases, CHANGELOG e git templates/hooks
├── 06_MIDIA/                           # Ativos visuais essenciais (banner_oficial.png)
│
├── .agents/skills/                     # Skills embutidas para agentes de IA
├── .github/workflows/                  # CI/CD (testes automatizados e auditoria de segurança)
├── .env.example                        # Template seguro de variáveis de ambiente
├── project.json                        # Manifesto estruturado de metadados corporativos
├── LEIA-ME.md                          # Manual técnico operacional (Uso Interno)
├── README.md                           # Vitrine pública executiva bilíngue (GitHub)
├── iniciar.sh / INICIAR.bat            # Lançadores multiplataforma com bootstrap automático
└── LICENSE                             # Licença MIT aberta com termos institucionais
```

---

## 🚀 Como Executar / Quick Start

```bash
# 1. Clonar o repositório
git clone https://github.com/Techdimbr/<nome-do-repositorio>.git
cd <nome-do-repositorio>

# 2. Verificar a integridade matemática dos arquivos críticos (AIDE/SHA-256)
./00_AUDITORIA/verificar_integridade.sh

# 3. Inicializar a aplicação (bootstrap inteligente automático)
./iniciar.sh
```

---

## 🛡️ Segurança e Governança

- **Verificação de Integridade:** Execute `./00_AUDITORIA/verificar_integridade.sh` para auditoria matemática via SHA-256.
- **Zero Leaks:** Nunca versione o arquivo `.env`. Copie `.env.example` para `.env` e configure suas variáveis locais.
- **Git Hooks:** Ative a barreira pré-commit executando `./05_VERSOES/git_templates/configurar_git.sh`.

---

## 💼 Implantação Corporativa & Parcerias Estratégicas

A **TECHDIM Inova Simples** fornece blueprints de código aberto e atua na implantação de arquiteturas avançadas de ciberdefesa, nuvem soberana e governança corporativa:

- 🛡️ **Hardening & Ciberdefesa:** Blindagem de servidores Linux Debian, regras avançadas de nftables e contenção de endpoints.
- ☁️ **Arquitetura Google Cloud (GCP):** Landing Zones soberanas, conectividade privada (VPC/IAP), Cloud Armor e CMEK.
- 🤖 **IA Privada & RAG Corporativo:** Sistemas corporativos com Vertex AI e Gemini sem vazamento de dados confidenciais.
- ⚖️ **Governança LGPD:** Auditorias automatizadas de bancos de dados, varredura de PII e emissão de relatórios de conformidade.

### Contato Comercial & Canais Oficiais
- 🌐 **Website Oficial:** [https://www.techdim.com.br](https://www.techdim.com.br)
- 🚀 **Vitrine Interativa (GitHub Pages):** [https://techdimbr.github.io/techdimbr/](https://techdimbr.github.io/techdimbr/)
- 📩 **Atendimento Corporativo:** `contato@techdim.com.br` / `reparafacilcampinas@gmail.com`
- 🏢 **CNPJ:** `61.933.926/0001-24` — TECHDIM INOVA SIMPLES (I.S.) · Campinas/SP
