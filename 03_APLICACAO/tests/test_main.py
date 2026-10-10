import unittest
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "03_APLICACAO" / "src"))

from main import carregar_manifesto, main


class TestMain(unittest.TestCase):
    def test_carregar_manifesto(self):
        m = carregar_manifesto()
        self.assertIsInstance(m, dict)
        self.assertEqual(m.get("doutrina"), "KETHER_1")

    def test_main_status(self):
        code = main([])
        self.assertEqual(code, 0)

    def test_main_version(self):
        code = main(["--version"])
        self.assertEqual(code, 0)

    def test_main_json(self):
        code = main(["--json"])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
