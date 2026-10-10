<!-- ID-TECHDIM: TECHDIM-PROJ-PADRAO-v9.9.9 -->
<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
# 🇧🇷 GEMINI.md — DIRETRIZES DO GOOGLE ANTIGRAVITY (MISSION CONTROL TECHDIM)

> Este arquivo é lido automaticamente pelo Google Antigravity IDE ao abrir este projeto.

## 1. O Papel do Google Antigravity
* O **Google Antigravity IDE** é o ambiente de engenharia oficial (Mission Control Supremo).
* Este projeto segue o padrão canônico de **8 Eixos Techdim (00_AUDITORIA a 06_MIDIA)** e foi forjado a partir da Central de Engenharia:
  `📁 ./309_REGRAS_DE_DESENVOLVIMENTO/`

## 2. Invariantes de Desenvolvimento
1. **Regra da Caixa-Preta:** O projeto é autossuficiente e portátil. Nunca dependa de caminhos fora da sua raiz sem fallback.
2. **Qualidade Máxima:** Sem placeholders, sem código simulado ou `eval()`.
3. **Living Documentation:** Mantenha os 8 eixos sempre sincronizados a cada nova funcionalidade.

## 3. Comandos de Sincronização Obrigatória com a Central Techdim
Ao concluir qualquer tarefa ou implementação no Antigravity:
```bash
# 1. Auditar qualidade e segurança (5 Sentinelas):
../309_REGRAS_DE_DESENVOLVIMENTO/dev auditar .

# 2. Executar suíte de testes com Devin IA:
../309_REGRAS_DE_DESENVOLVIMENTO/dev testar .

# 3. Sincronizar o projeto no Catálogo Comercial SQLite Techdim:
../309_REGRAS_DE_DESENVOLVIMENTO/dev catalogo sync
```
