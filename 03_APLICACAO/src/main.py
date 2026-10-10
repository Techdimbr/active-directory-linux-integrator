#!/usr/bin/env python3
# ==============================================================================
# TECHDIM INOVA SIMPLES (I.S.) · CNPJ: 61.933.926/0001-24
# Padrão Canônico para Repositórios Públicos GitHub (PRJ-TECHDIM-PUBLIC-v1.0.0)
# ==============================================================================
"""
Ponto de entrada do Projeto Padrão TECHDIM.
Demonstra a arquitetura atômica de software: offline-first, seguro e determinístico.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def carregar_manifesto() -> dict:
    p = RAIZ / "project.json"
    if p.is_file():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


def exibir_status() -> int:
    manifesto = carregar_manifesto()
    nome = manifesto.get("nome_comercial", "TECHDIM Projeto Padrão Público")
    versao = manifesto.get("versao", "1.0.0")
    cid = manifesto.get("canonical_id", "PRJ-TECHDIM-PUBLIC-v1.0.0")
    doutrina = manifesto.get("doutrina", "KETHER_1")

    print("=" * 72)
    print(f"  🏛️  {nome}")
    print(f"  📌 ID Canônico : {cid}")
    print(f"  🚀 Versão      : {versao} | Doutrina: {doutrina}")
    print(f"  🛡️  Segurança   : Zero Leaks · Padrão Debian 13 (Trixie/Sid)")
    print("=" * 72)
    print("✓ Organismo atômico operacional e validado.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="TECHDIM — Padrão Canônico para Repositórios Públicos GitHub"
    )
    parser.add_argument(
        "--status", action="store_true", help="Exibe o status consolidado do projeto"
    )
    parser.add_argument(
        "--version", "-v", action="store_true", help="Exibe a versão canônica"
    )
    parser.add_argument(
        "--json", action="store_true", help="Retorna o manifesto do projeto em JSON"
    )

    args = parser.parse_args(argv)

    if args.version:
        manifesto = carregar_manifesto()
        print(manifesto.get("versao", "1.0.0"))
        return 0

    if args.json:
        print(json.dumps(carregar_manifesto(), ensure_ascii=False, indent=2))
        return 0

    return exibir_status()


if __name__ == "__main__":
    raise SystemExit(main())
