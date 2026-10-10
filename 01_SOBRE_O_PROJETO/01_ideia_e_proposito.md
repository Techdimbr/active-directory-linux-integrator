<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Ideia e Propósito

## A dor

Times e criadores solo acumulam dezenas de "projetinhos": scripts, automações, apps.
Seis meses depois ninguém lembra o que cada pasta faz, se roda em outra máquina, qual era
a versão boa, ou por que uma decisão foi tomada. Entregar isso a um cliente ou a outro dev
custa horas de arqueologia. E copiar a pasta para outro computador quase nunca "só funciona".

## A solução

O **Protocolo TECHDIM v2.1.0** trata cada projeto como um **organismo vivo e portátil**:

- **Identidade** — `LEIA-ME.md`, `VERSION`, `ID-TECHDIM`, ícone.
- **Corpo** — `03_APLICACAO/` com o código e as dependências vendorizadas.
- **Cérebro** — `04_INTELIGENCIA_DE_DESENVOLVIMENTO/` com decisões, lições, grafo neural e estado.
- **DNA** — `05_VERSOES/` com o histórico Git completo e o CHANGELOG como única fonte de versão.
- **Projeção** — `06_MIDIA/` com o material comercial e a prova de integridade.
- **Sistema imunológico** — `00_AUDITORIA/` que se auto-verifica a cada arranque.

Você copia a pasta para qualquer máquina limpa (Windows, Debian/Ubuntu, macOS), roda um
comando, e o organismo se apresenta: diz onde está instalado, em que máquina, se está
saudável, e abre um painel onde tudo é feito por ações numeradas.

## Público-alvo

- **Desenvolvedores solo / freelancers** que precisam entregar projetos auto-explicáveis.
- **Pequenas software houses** que querem um padrão único para todo o portfólio.
- **Consultores de segurança / hardening** que entregam ferramentas para rodar em campo, offline.
- **Educadores** que distribuem material prático que "roda no laboratório sem internet".

## Domínio de referência embutido

App **Android de Hardening + Performance + Privacidade + Modo Gamer**: um caso real,
sensível a segurança e a portabilidade (precisa de `adb`/`scrcpy`, roda em campo, não
pode vazar credenciais), que exercita todas as camadas do protocolo.

## Critério de "pronto"

O `00_AUDITORIA/AUDITORIA_COMPLETA.md` com **veredito APROVADO** e o Estado Quântico
**VERDE** — ver [[04_mapa_de_funcionamento]] e [[03_funcionalidades]].
