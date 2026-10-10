# 🏛️ Active Directory Linux Integrator
## Automação Corporativa para Ingresso e Integração de Servidores e Estações Linux em Domínios Microsoft Active Directory

![Active Directory Linux Integrator](06_MIDIA/banner_oficial.png)

[![Padrão](https://img.shields.io/badge/Padr%C3%A3o-PRJ--TECHDIM--PUBLIC--v1.0.0-00E5FF.svg)](https://techdimbr.github.io/techdimbr/)
[![Doutrina](https://img.shields.io/badge/Doutrina-KETHER__1-7C4DFF.svg)](https://www.techdim.com.br)
[![Autenticação](https://img.shields.io/badge/Auth-Kerberos%20%7C%20SSSD-00C853.svg)](https://sssd.io)
[![Ambiente Híbrido](https://img.shields.io/badge/H%C3%ADbrido-Active%20Directory%20%2B%20Debian%20Linux-0078D7.svg)](README.md)
[![Automação](https://img.shields.io/badge/IaC-Ansible%20Playbooks-EE0000.svg)](https://www.ansible.com)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT%20Corporate-green.svg)](LICENSE)

> **Automação robusta em Ansible e Python para ingresso e governança de estações e servidores Linux Debian/Ubuntu em domínios Microsoft Active Directory. Autenticação Kerberos, Single Sign-On (SSO), autorização granular com SSSD, cache offline e controle centralizado de permissões sudoers.**

---

## 🏛️ Visão Geral & Proposta de Valor

Em corporações que possuem ecossistemas mistos (Windows Server no núcleo de identidade e Linux nos servidores de aplicação e estações de desenvolvimento), é comum ver contas locais dispersas sem expiração de senhas, sem revogação automática e sem auditoria centralizada.

O **Active Directory Linux Integrator** une o melhor dos dois mundos:
1. **Identidade Centralizada e Única (SSO):** O colaborador utiliza as mesmas credenciais do Windows / Microsoft 365 para efetuar login SSH ou na interface gráfica das máquinas Linux.
2. **Autorização Centralizada de Sudoers:** Grupos de segurança do AD (ex.: `AD-Engenharia-Admins`) recebem privilégios de `sudo` no Linux de forma declarativa e automatizada, sem necessidade de editar `/etc/sudoers` manualmente em cada nó.
3. **Resiliência com Cache Offline:** O SSSD mantém cache local criptografado de credenciais para que notebooks de desenvolvedores continuem operacionais mesmo sem conexão com o Domain Controller.

---

## 🏗️ Topologia da Autenticação Híbrida

```mermaid
graph TD
    User["Colaborador (Login SSH / Console Linux)"] -->|Solicitação de Acesso PAM| SSSD["System Security Services Daemon (SSSD)"]
    SSSD -->|1. Consulta DNS SRV (_ldap/_kerberos)| DNS["DNS Corporativo do Domínio AD"]
    SSSD -->|2. Obtenção de Ticket TGT (Porta 88)| KDC["Key Distribution Center (Active Directory KDC)"]
    KDC -->|3. Ticket Kerberos Criptografado| SSSD
    SSSD -->|4. Busca de Grupos & Atributos (LDAP Porta 389/636)| AD["Microsoft Active Directory Domain Controller"]
    SSSD -->|5. Mapeamento de Sudoers| Sudo["/etc/sudoers.d/ad_security_groups"]
    Sudo --> Shell["Sessão Linux Autorizada com Auditoria"]
```

---

## ⚡ Início Rápido

### Comandos de Operação
```bash
# 1. Clonar o repositório
git clone https://github.com/Techdimbr/active-directory-linux-integrator.git
cd active-directory-linux-integrator

# 2. Inicializar o ambiente local
./iniciar.sh

# 3. Executar o verificador de pré-requisitos e registros SRV do AD
python3 03_APLICACAO/src/ad_verifier.py --domain corp.exemplo.com
```

---

## 🛡️ Governança & Contato Corporativo
- **Autor:** Deivis Írio Mayer (Kether_1)
- **Entidade:** TECHDIM INOVA SIMPLES (I.S.) - ME · CNPJ 61.933.926/0001-24
- **Website Oficial:** [https://www.techdim.com.br](https://www.techdim.com.br)
- **Portal de Soluções:** [https://techdimbr.github.io/techdimbr/](https://techdimbr.github.io/techdimbr/)
