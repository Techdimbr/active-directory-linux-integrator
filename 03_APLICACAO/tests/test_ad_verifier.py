#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o verificador do Active Directory Linux Integrator.
"""

import unittest
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from ad_verifier import ADPrerequisitesVerifier

class TestADPrerequisitesVerifier(unittest.TestCase):
    def test_validacao_fqdn(self):
        self.assertTrue(ADPrerequisitesVerifier.validar_fqdn("corp.techdim.local"))
        self.assertTrue(ADPrerequisitesVerifier.validar_fqdn("ad.empresa.com.br"))
        self.assertFalse(ADPrerequisitesVerifier.validar_fqdn("invalido_sem_ponto"))

    def test_registros_srv(self):
        srvs = ADPrerequisitesVerifier.gerar_registros_srv_obrigatorios("corp.local")
        self.assertEqual(len(srvs), 4)
        self.assertIn("_ldap._tcp.dc._msdcs.corp.local", srvs)
        self.assertIn("_kerberos._tcp.corp.local", srvs)

    def test_validacao_config_sssd(self):
        conf = """
        [domain/CORP]
        id_provider = ad
        cache_credentials = True
        use_fully_qualified_names = False
        """
        resultado = ADPrerequisitesVerifier.validar_config_sssd(conf)
        self.assertTrue(resultado["auth_provider = krb5"])
        self.assertTrue(resultado["cache_credentials = true"])

if __name__ == "__main__":
    unittest.main()
