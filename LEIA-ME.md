# 🛠️ MANUAL TÉCNICO DE BANCADA (USO INTERNO / OPERADOR LOCAL)
> **AVISO DE ESCOPO:** Este arquivo é destinado estritamente ao operador, engenheiro ou agente local da TECHDIM.
> Para a vitrine pública e apresentação comercial, consulte o arquivo **`README.md`**.

# 🚀 Techdim — Padrão de Criação de Projetos

> **Propriedade:** TECHDIM INOVA (I.S.) · CNPJ: 61.933.926/0001-24  
> **Vitrine GitHub Pages:** https://techdimbr.github.io/techdimbr/  
> **Identificador Único:** `PRJ-TECHDIM-PADRAO-v9.9.9`  
> **Categoria:** Governança & Engenharia de Software  
> **Versão:** 9.9.9 | **Status:** 🟢 Pronto para Venda (Debian 13 Trixie/Sid)  

---

## 📋 Descrição do que faz:
1. **Ciclo de Início de Projeto Mandatório:**
   - **Compreensão & Diálogo:** Entendimento profundo da solicitação. Havendo ambiguidades, questionar o usuário antes de codificar.
   - **Planejamento de Possibilidades:** Elaborar o plano detalhado apresentando todas as opções e arquiteturas possíveis para decisão do usuário.
   - **Pesquisa & Forja de Skill Específica:** Buscar conhecimentos atualizados na internet e na base de inteligência para gerar e implantar uma Skill específica em `.agents/skills/<nome_projeto>/SKILL.md`.
   - **Agentes e Sub-agentes:** Planejamento e orquestração de agentes especializados para otimizar cada fase do ciclo de desenvolvimento.
   - **Git com Atalho & Ícone:** Inicialização do Git Vivo, commits atômicos e ícone padronizado para navegação imediata.
   - **Documentação Contínua (Living Docs):** Atualização contínua das notas, mapas mentais e registros históricos.
2. **Duas Pastas de Mídia Dedicadas:**
   - **`MIDIA_1_ANUNCIO/`:** Ativos para divulgação comercial, incluindo anúncios com hashtags para LinkedIn/Instagram/X, campanha completa Google Ads (RSA), prompts para geração de vídeo com IA no Google Flow / Gemini Omni Flash, tabela de preços estruturada e canais estratégicos de venda.
   - **`MIDIA_2_APRESENTACAO/`:** Apresentação de facílimo entendimento para qualquer público, com o PDF oficial (`TECHDIM_EXPLICACAO_SIMPLES_PUBLICO.pdf`), duas imagens conceituais ilustrativas e visualizador web.
3. **Hub Universal de Agentes de IA (`hub_agentes.py`):** Descobre automaticamente ambientes do Claude Code, Antigravity CLI, Antigravity IDE e Antigravity 2.0, sincronizando skills e instruções principais com um clique.
4. **Organismo Unificado de Governança (Kether v2.3.0):** 
   - A raiz deste projeto é o próprio organismo vivo integrado, sem redundância de pastas.
   - Contém o núcleo executável (`techdim_core/`), suíte de 99 testes automatizados (`03_APLICACAO/tests/`), auto-auditoria em 7 eixos (`00_AUDITORIA/`) e observabilidade com métricas Prometheus.
5. **Geração e Instalação Automatizada:**
   - `scripts/criar_estrutura.py` e `.ps1`: geração da árvore oficial com frontmatter YAML, SHA-256, Git local e ponto de entrada funcional.
   - Instaladores universais (`instalador_linux.sh` / `INSTALADOR_AUTOMATICO.bat`) com verificação de runtime, permissões, dependências vendorizadas e autoteste.
6. **Painel Local Completo (`painel.py` + `painel.html`):** Servidor HTTP local (100% stdlib) com interface rica para governança, diagnósticos de máquina, implantação de skills, auditoria e execução de testes.
7. **Atalho Desktop Multiplataforma (`instalar_atalho.sh`):** Instala o atalho com ícone na Área de Trabalho, menu de aplicativos e pasta central TECHDIM.

---

## 🎯 Para que serve (Objetivo Estratégico & Valor Agregado):
Garantir total confidencialidade corporativa nos processamentos cognitivos, eliminar custos por token de nuvens proprietárias e manter disponibilidade total mesmo sem conexão com a internet.

---

## ⚙️ Como funciona (Arquitetura e Engenharia):
Todas as funcionalidades do protocolo estão unificadas e diretamente acessíveis na raiz deste projeto:
- `00_AUDITORIA/`: Motor de auto-auditoria em 7 eixos.
- `01_SOBRE_O_PROJETO/`: Visão geral, mapas conceituais e inteligência de negócios.
- `02_COMO_USAR/`: Guias de instalação, tutoriais passo a passo e FAQ.
- `03_APLICACAO/`: Código-fonte, testes de fumaça, dependências e assets.
- `04_INTELIGENCIA_DE_DESENVOLVIMENTO/`: Registros de sessões, decisões técnicas (ADR) e lições aprendidas.
- `05_VERSOES/`: Histórico de versões, CHANGELOG e Git vivo.
- `06_MIDIA/`: Kit comercial original e manifesto de integridade.
- `MIDIA_1_ANUNCIO/`: Anúncios prontos, Google Ads, prompts de vídeo IA e precificação.
- `MIDIA_2_APRESENTACAO/`: PDF simples para público geral e ilustrações conceituais.
- `techdim_core/`: Biblioteca central de governança e integridade.
- `INICIO_START/`: Lançador universal portátil cross-platform.

---

## ⚡ Como executar:
1. **Pelo Terminal / CLI:**
   ```bash
   cd "#PROJETO_PADRAO_PROJETO_TECHDIM (SCAFFOLD OFICIAL DO PADRAO TECHDIM KETHER1)"
   python3 src/main.py
   ```
2. **Pelo Catálogo Central TECHDIM:**
   Abra o painel central de projetos e clique em "Abrir Pasta" ou "Detalhes".


---

## 📚 Documentação Técnica Original:

<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PADRAO-v2.3.0 -->
# TECHDIM — Padrão de Criação de Projetos (v2.3.0)

> ID-TECHDIM: TECHDIM-PROJ-PADRAO-v2.3.0 | Central de Governança, Hub de Agentes de IA e Padrão Mestre Techdim.  
> **Catálogo de Funcionalidades:** 48 itens homologados (ver [03_funcionalidades.md](01_SOBRE_O_PROJETO/03_funcionalidades.md)).

## Por onde começar?

| Objetivo | Onde ir |
|---|---|
| **Usar o painel visual** (Hub de Agentes, implantar, auditoria, testes, checklist) | Duplo-clique no atalho de Área de Trabalho, ou `./iniciar.sh` (Linux/Mac) / `iniciar_painel_windows.bat` (Windows) |
| **Implantar nos agentes de IA** (Claude Code, Antigravity CLI, IDE e 2.0) | Aba **🤖 Agentes de IA** no painel visual, ou `python3 hub_agentes.py sincronizar` |
| **Campanhas de Anúncio & Vendas** (Redes sociais, Google Ads, prompts de vídeo IA, precificação e canais) | [`MIDIA_1_ANUNCIO/`](MIDIA_1_ANUNCIO/LEIA-ME.md) |
| **Apresentação Didática para o Público** (PDF simples, 2 imagens conceituais e versão web) | [`MIDIA_2_APRESENTACAO/`](MIDIA_2_APRESENTACAO/LEIA-ME.md) |
| **Entender o padrão completo** (fases, fluxo de início, regras de ouro) | [`SKILL.md`](SKILL.md) |
| Ver a árvore de pastas detalhada | [`references/estrutura_padrao.md`](references/estrutura_padrao.md) |
| Conferir checklist executável ou manual | Aba **🛡️ Auditoria & Testes** no painel ou [`references/checklist_qualidade.md`](references/checklist_qualidade.md) |
| Padrão de metadados YAML (Obsidian/RAG) | [`references/00_padrao_metadados_yaml_kether.md`](references/00_padrao_metadados_yaml_kether.md) |
| Blindagem de Propriedade Intelectual (ZWC + SHA-256) | `python3 scripts/blindar_propriedade_intelectual.py` (Linux/Mac/Win) |
| Conferir uma entrega contra o certificado emitido | `python3 scripts/blindar_propriedade_intelectual.py --verificar` (sai com código 1 se divergir) |
| Provar autoria lendo a assinatura invisível de um arquivo | `python3 scripts/blindar_propriedade_intelectual.py --extrair caminho/do/arquivo.py` |
| Gerar um projeto novo pelo terminal (sem o painel) | `python3 scripts/criar_estrutura.py "NomeDoProjeto" --tipo python --destino /caminho --descricao "o que faz" --problema "a dor que resolve"` |
| Instalar um projeto já gerado numa máquina nova | `./instalador_linux.sh` (Linux/Mac) ou `INSTALADOR_AUTOMATICO.bat` (Windows), dentro da pasta do projeto |
| Sincronizar / Verificar Prontidão para o Catálogo Comercial | `python3 06_MIDIA/sincronizar_catalogo.py` ou aba **💎 Catálogo & Vitrine** no painel |
| Bootstrap de Git em qualquer projeto | [`techdim-git-padrao/LEIA-ME.md`](techdim-git-padrao/LEIA-ME.md) |

## O que esta pasta faz, resumido

1. **Ciclo de Início de Projeto Mandatório:**
   - **Compreensão & Diálogo:** Entendimento profundo da solicitação. Havendo ambiguidades, questionar o usuário antes de codificar.
   - **Planejamento de Possibilidades:** Elaborar o plano detalhado apresentando todas as opções e arquiteturas possíveis para decisão do usuário.
   - **Pesquisa & Forja de Skill Específica:** Buscar conhecimentos atualizados na internet e na base de inteligência para gerar e implantar uma Skill específica em `.agents/skills/<nome_projeto>/SKILL.md`.
   - **Agentes e Sub-agentes:** Planejamento e orquestração de agentes especializados para otimizar cada fase do ciclo de desenvolvimento.
   - **Git com Atalho & Ícone:** Inicialização do Git Vivo, commits atômicos e ícone padronizado para navegação imediata.
   - **Documentação Contínua (Living Docs):** Atualização contínua das notas, mapas mentais e registros históricos.
2. **Duas Pastas de Mídia Dedicadas:**
   - **`MIDIA_1_ANUNCIO/`:** Ativos para divulgação comercial, incluindo anúncios com hashtags para LinkedIn/Instagram/X, campanha completa Google Ads (RSA), prompts para geração de vídeo com IA no Google Flow / Gemini Omni Flash, tabela de preços estruturada e canais estratégicos de venda.
   - **`MIDIA_2_APRESENTACAO/`:** Apresentação de facílimo entendimento para qualquer público, com o PDF oficial (`TECHDIM_EXPLICACAO_SIMPLES_PUBLICO.pdf`), duas imagens conceituais ilustrativas e visualizador web.
3. **Hub Universal de Agentes de IA (`hub_agentes.py`):** Descobre automaticamente ambientes do Claude Code, Antigravity CLI, Antigravity IDE e Antigravity 2.0, sincronizando skills e instruções principais com um clique.
4. **Organismo Unificado de Governança (Kether v2.3.0):** 
   - A raiz deste projeto é o próprio organismo vivo integrado, sem redundância de pastas.
   - Contém o núcleo executável (`techdim_core/`), suíte de 99 testes automatizados (`03_APLICACAO/tests/`), auto-auditoria em 7 eixos (`00_AUDITORIA/`) e observabilidade com métricas Prometheus.
5. **Geração e Instalação Automatizada:**
   - `scripts/criar_estrutura.py` e `.ps1`: geração da árvore oficial com frontmatter YAML, SHA-256, Git local e ponto de entrada funcional.
   - Instaladores universais (`instalador_linux.sh` / `INSTALADOR_AUTOMATICO.bat`) com verificação de runtime, permissões, dependências vendorizadas e autoteste.
6. **Painel Local Completo (`painel.py` + `painel.html`):** Servidor HTTP local (100% stdlib) com interface rica para governança, diagnósticos de máquina, implantação de skills, auditoria e execução de testes.
7. **Atalho Desktop Multiplataforma (`instalar_atalho.sh`):** Instala o atalho com ícone na Área de Trabalho, menu de aplicativos e pasta central TECHDIM.

## Como isto se comporta numa máquina nova (do zero)

Copie a pasta `techdim-projeto-padrao/` inteira (pendrive, HD, nuvem) para o computador novo e rode `./iniciar.sh` (ou o `.bat`/`.command` equivalente). O sistema detecta automaticamente o primeiro uso, configura permissões, diagnostica o ambiente e oferece a instalação do atalho de área de trabalho com ícone.

## Arquitetura Unificada (Kether v2.3.0)

Todas as funcionalidades do protocolo estão unificadas e diretamente acessíveis na raiz deste projeto:
- `00_AUDITORIA/`: Motor de auto-auditoria em 7 eixos.
- `01_SOBRE_O_PROJETO/`: Visão geral, mapas conceituais e inteligência de negócios.
- `02_COMO_USAR/`: Guias de instalação, tutoriais passo a passo e FAQ.
- `03_APLICACAO/`: Código-fonte, testes de fumaça, dependências e assets.
- `04_INTELIGENCIA_DE_DESENVOLVIMENTO/`: Registros de sessões, decisões técnicas (ADR) e lições aprendidas.
- `05_VERSOES/`: Histórico de versões, CHANGELOG e Git vivo.
- `06_MIDIA/`: Kit comercial original e manifesto de integridade.
- `MIDIA_1_ANUNCIO/`: Anúncios prontos, Google Ads, prompts de vídeo IA e precificação.
- `MIDIA_2_APRESENTACAO/`: PDF simples para público geral e ilustrações conceituais.
- `techdim_core/`: Biblioteca central de governança e integridade.
- `INICIO_START/`: Lançador universal portátil cross-platform.

## Regra de ouro

Esta skill nunca modifica nada fora da pasta de um projeto explicitamente indicado por você. Nenhuma ação varre ou apaga pastas do sistema além dessa. A remoção recusa qualquer caminho que passe por links simbólicos, garantindo segurança total de execução.

