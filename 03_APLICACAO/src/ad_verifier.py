#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Active Directory Linux Integrator - Validador de Pré-Requisitos e SSSD
Python 3 stdlib puro
"""

import sys
import re
from typing import Dict, Any, List

class ADPrerequisitesVerifier:
    @staticmethod
    def validar_fqdn(dominio: str) -> bool:
        """Verifica se o nome de domínio possui formato FQDN corporativo válido."""
        padrao = r"^(?=.{4,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})+$"
        return bool(re.match(padrao, dominio))

    @staticmethod
    def gerar_registros_srv_obrigatorios(dominio: str) -> List[str]:
        """Retorna a lista de registros DNS SRV mandatórios para ingresso no AD."""
        return [
            f"_ldap._tcp.dc._msdcs.{dominio}",
            f"_kerberos._tcp.dc._msdcs.{dominio}",
            f"_ldap._tcp.{dominio}",
            f"_kerberos._tcp.{dominio}"
        ]

    @staticmethod
    def validar_config_sssd(conteudo_sssd: str) -> Dict[str, bool]:
        """Valida se parâmetros críticos de segurança estão presentes no sssd.conf."""
        requisitos = {
            "auth_provider = krb5": "auth_provider = krb5" in conteudo_sssd or "id_provider = ad" in conteudo_sssd,
            "cache_credentials = true": "cache_credentials = true" in conteudo_sssd.lower(),
            "use_fully_qualified_names = false": "use_fully_qualified_names = false" in conteudo_sssd.lower(),
        }
        return requisitos

def main():
    print("=" * 65)
    print("🏛️  TECHDIM ACTIVE DIRECTORY LINUX INTEGRATOR - PRÉ-REQUISITOS")
    print("=" * 65)
    
    dominio_exemplo = "corp.techdim.local"
    fqdn_valido = ADPrerequisitesVerifier.validar_fqdn(dominio_exemplo)
    srvs = ADPrerequisitesVerifier.gerar_registros_srv_obrigatorios(dominio_exemplo)
    
    print(f"🏢 Domínio Alvo               : {dominio_exemplo}")
    print(f"✅ Formato FQDN Válido         : {'SIM' if fqdn_valido else 'NÃO'}")
    print(f"📋 Registros DNS SRV Exigidos  :")
    for s in srvs:
        print(f"   - {s}")
        
    print("-" * 65)
    print("✓ Validador de conformidade Active Directory pronto para orquestração.")

if __name__ == "__main__":
    main()
