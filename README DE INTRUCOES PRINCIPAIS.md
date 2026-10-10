# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Active Directory Linux Integrator

**Repositório Oficial:** `https://github.com/Techdimbr/active-directory-linux-integrator`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Active Directory Linux Integrator
- **Identificador (Slug):** `active-directory-linux-integrator`
- **Categoria:** Identidade Corporativa & Integração Híbrida
- **Stack Tecnológica:** Ansible Core, SSSD, Realmd, Kerberos (`krb5-user`), Samba Winbind, OpenSSH, PAM
- **Objetivo Central:** Automatizar o processo de ingresso e governança de servidores e estações de trabalho Debian 13 em domínios Microsoft Active Directory, configurando Kerberos, SSSD e permissões sudoers de forma reprodutível e segura.

### Casos de Uso Reais
1. **Provisionamento Automatizado de VMs Linux:** Ingresso sem intervenção manual no AD via Ansible logo após o boot.
2. **Governança de Acessos Privilegiados:** Concessão de privilégios de sudoers restrita a grupos corporativos do AD.
3. **Sincronização Segura de Relógio (Kerberos):** Configuração de Chrony/NTP apontando para os Domain Controllers (essencial para evitar falhas de skew de relógio do Kerberos acima de 300 segundos).

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── ad_verifier.py                     # Validador de pré-requisitos (SRV DNS, NTP, portas KDC)
├── site.yml                           # Playbook principal do Ansible para join no domínio
├── roles/
│   ├── 01_prereqs_ntp/                # Instalação de pacotes e sincronização de horário
│   ├── 02_realm_join/                 # Execução do realm join e criação da conta de máquina
│   └── 03_sssd_sudoers/               # Configuração do sssd.conf e regras de sudoers
└── templates/
    ├── sssd.conf.j2                   # Template Jinja2 otimizado para SSSD com cache offline
    └── krb5.conf.j2                   # Template Jinja2 para Kerberos 5
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS RECURSOS DE INTEGRAÇÃO AD -->
- [x] Verificador de resolução DNS de registros SRV do Kerberos e LDAP;
- [x] Template de configuração do SSSD com encriptação e cache;
- [ ] Módulo de renovação automática do ticket da conta de máquina ($);
- [ ] Suporte a múltiplos domínios e florestas com relação de confiança (Forest Trusts).
