<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Configuração

O organismo funciona **sem nenhuma configuração**. Os ajustes abaixo são todos opcionais.

## Variáveis de ambiente

| Variável | Efeito | Padrão |
|----------|--------|--------|
| `TECHDIM_OPERADOR` | nome do operador no Estado do Operador / memória episódica | usuário do SO |
| `TECHDIM_GIT_NAME` / `TECHDIM_GIT_EMAIL` | identidade dos commits do Git Vivo | `TECHDIM Brasil` / `techdimbrasil@gmail.com` |
| `TECHDIM_LOCALE` | idioma do painel (`pt-BR` · `en-US` · `es-ES`) | locale do SO → `pt-BR` |
| `TECHDIM_A11Y` | modo acessível (sem box-drawing, marcadores textuais) | desligado |
| `NO_COLOR` | desliga cores ANSI | — |
| `TECHDIM_LOG_NIVEL` | `DEBUG`/`INFO`/`WARN`/`ERROR`/`FATAL` no log JSON | `INFO` |
| `TECHDIM_SEM_ESTADO` | audita em memória, não grava estado/memória (direito de oposição LGPD) | desligado |

## Arquivo `03_APLICACAO/config/config.json` (opcional)

Copie de `config.exemplo.json`. Chaves reconhecidas:

```json
{
  "locale": "pt-BR",
  "perfil_padrao": "hardening",
  "adb_timeout_s": 8,
  "operador": "${TECHDIM_OPERADOR}"
}
```

Nunca coloque segredo em texto puro — use `${VARIAVEL}` e resolva em runtime.
`config.json` e `perfil_ativo.json` são gitignored.

## Perfis

`03_APLICACAO/config/perfil_ativo.json` guarda o perfil aplicado pela ação **[5]** do
painel (`hardening` / `performance` / `privacidade` / `gamer`). Domínios leem esse valor.

## Flags de linha de comando

`./iniciar.sh [--sem-painel] [--auditoria] [--diagnostico] [--health] [--a11y] [--sem-cor] [--locale xx-YY]`
