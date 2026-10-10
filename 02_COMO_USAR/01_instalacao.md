<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Instalação (não há instalação)

## Requisito único

**Python 3.9 ou superior.** Nada mais é obrigatório.

| SO | Como obter Python |
|---|---|
| Debian 12+/Ubuntu 22.04+ | `sudo apt install python3` (quase sempre já vem) |
| Windows 10/11 | https://www.python.org/downloads/ — marque "Add python.exe to PATH" |
| macOS | `brew install python` ou o instalador oficial |

## Colocar o organismo na máquina

1. Copie a pasta `PROTOCOLO_TECHDIM_v2.1.0/` inteira (pendrive, HD externo, nuvem, `scp`).
2. No Linux/macOS, garanta permissão de execução uma vez:
   `chmod +x iniciar.sh diagnostico.sh INICIAR_NOVO_PROJETO.sh`
3. Rode:
   - Linux/macOS: `./iniciar.sh`
   - Windows: duplo-clique em `INICIAR.bat`
   - Qualquer: `python3 INICIAR_UNIVERSAL.py`

Na primeira execução o organismo cria `05_VERSOES/.git`, escreve `ESTADO_ATUAL.json`
e abre o painel. Nenhum arquivo é criado fora da pasta.

## Ferramentas opcionais (modo offline após 1º download)

| Ferramenta | Para quê | Fallback se ausente |
|---|---|---|
| `git` | Git Vivo em `05_VERSOES/` | organismo funciona; versionamento fica inativo |
| `adb` / `scrcpy` / `fastboot` | domínio Android | domínio roda em dry-run e reporta "adb ausente" |
| `bubblewrap` (`bwrap`) ou `firejail` | isolamento real de subprocessos | roda direto, registra "isolamento indisponível" |

Para vendorizar ferramentas portáteis dentro do organismo:
`python3 03_APLICACAO/dependencias/baixar_dependencias.py` (ver `MANIFESTO.md`).
Depois disso, `checksums.txt` é regenerado e a auditoria de integridade passa a cobri-las.

## Verificar que está tudo são

```bash
./diagnostico.sh            # retrato da máquina + auditoria completa
```
Saída esperada: **veredito APROVADO** e Estado Quântico **VERDE** (ou AMARELO só por
"mudanças não commitadas" logo após gerar algo).
