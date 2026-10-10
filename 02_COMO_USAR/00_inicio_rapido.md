<!-- TECHDIM INOVA SIMPLES (I.S.) - ME 61.933.926/0001-24 | www.techdim.com.br -->
<!-- ID-TECHDIM: TECHDIM-PROJ-PROTOCOLO-v2.1.0 -->
# Início Rápido — do zero ao painel em 5 minutos

## 1. Requisito

**Python 3.9+.** Nada mais.
`python3 --version` (Linux/macOS) ou `python --version` (Windows).

## 2. Colocar a pasta na máquina

Copie `PROTOCOLO_TECHDIM_v2.1.0/` inteira (pendrive, HD, nuvem, `scp`, `git clone`).
No Linux/macOS, uma vez: `chmod +x iniciar.sh diagnostico.sh iniciar_testes.sh`.

## 3. Abrir o painel

| SO | Comando |
|----|---------|
| Linux/macOS | `./iniciar.sh` |
| Windows | duplo-clique em `INICIAR.bat` |
| Qualquer | `python3 INICIAR_UNIVERSAL.py` |

O organismo se apresenta (máquina, Git, saúde) e abre o Painel Interativo.

## 4. Primeiros comandos no painel

- **[1]** Rodar auditoria completa → deve dar **APROVADO**.
- **[11]** Validar Checklist Oficial (Fases 0–9) → grade **A/A+**.
- **[12]** Ver saúde → `/health: pass`, `/ready: true`.

## 5. Sem o painel

```bash
make help              # todos os atalhos
make auditoria         # 7 auditorias
make testes            # suíte unittest
./diagnostico.sh       # retrato da máquina + auditoria
python3 INICIAR_UNIVERSAL.py --health   # só /health /ready (JSON)
```

## 6. Gerar o domínio de exemplo

```bash
python3 02_COMO_USAR/NOVO_DOMINIO.py android_hardening \
  --descricao "Hardening + Performance + Privacidade + Modo Gamer para Android via ADB"
```
Cria `03_APLICACAO/src/dominios/android_hardening/` **e faz o commit inicial**.

## Problemas comuns

| Problema | Solução |
|----------|---------|
| `python3: command not found` | `sudo apt install python3` (o `iniciar.sh` também tenta `python`) |
| Painel sem cores | esperado fora de TTY / com `NO_COLOR`; use `--sem-cor` para forçar |
| Auditoria AMARELA logo após gerar algo | há mudanças não commitadas → ação **[3]** |
| `git` ausente | organismo funciona; só o Git Vivo fica inativo até haver `git` |

Próximo: [`08_passo_a_passo.md`](08_passo_a_passo.md) para o fluxo completo.
