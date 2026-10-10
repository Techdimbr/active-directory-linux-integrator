import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


class TestFumacaEstrutura(unittest.TestCase):
    def test_pastas_canonicas_existem(self):
        pastas = [
            "00_AUDITORIA",
            "01_SOBRE_O_PROJETO",
            "02_COMO_USAR",
            "03_APLICACAO",
            "04_INTELIGENCIA_DE_DESENVOLVIMENTO",
            "05_VERSOES",
            "06_MIDIA",
        ]
        for p in pastas:
            self.assertTrue((RAIZ / p).is_dir(), f"Pasta canônica ausente: {p}")

    def test_arquivos_essenciais_raiz(self):
        arquivos = [
            "README.md",
            "LEIA-ME.md",
            "LICENSE",
            "SECURITY.md",
            "CONTRIBUTING.md",
            ".gitignore",
            ".env.example",
            "project.json",
            "iniciar.sh",
        ]
        for a in arquivos:
            self.assertTrue((RAIZ / a).is_file(), f"Arquivo essencial ausente: {a}")

    def test_zero_leaks_env_real_nao_existe(self):
        self.assertFalse((RAIZ / ".env").is_file(), "Arquivo .env real não pode estar versionado!")


if __name__ == "__main__":
    unittest.main()
