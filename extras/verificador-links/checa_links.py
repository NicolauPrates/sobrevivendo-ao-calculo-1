"""
Confere se todo link relativo do repositório aponta para um arquivo que existe.

O material tem mais de mil links internos entre páginas, listas, gabaritos e
figuras. Renomear um arquivo quebra todos os que apontavam para ele, e o GitHub
não avisa: o link simplesmente leva a um 404.

Rode a partir da raiz do repositório:

    python extras/verificador-links/checa_links.py

Sai com código 1 se houver algum link quebrado, para poder ser usado em CI.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

#: Links em markdown: [texto](alvo)
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

#: Abertura ou fechamento de bloco de código cercado (``` ou ~~~).
CERCA = re.compile(r"^\s*(```|~~~)")

#: Pastas que não contêm material do repositório.
IGNORAR = {".git", "node_modules", ".venv", "__pycache__"}

#: Alvos que não são arquivos: o GitHub os resolve no servidor dele.
NAO_SAO_ARQUIVOS = ("issues/new", "/commits/", "/pulls", "/discussions")

PREFIXOS_EXTERNOS = ("http://", "https://", "mailto:", "#")


def links_do_arquivo(texto: str):
    """Devolve os alvos dos links, pulando o que está dentro de bloco de código.

    Blocos cercados contêm exemplos e modelos — os links ali são ilustração, e o
    GitHub os mostra como texto literal.
    """
    dentro_de_bloco = False
    for linha in texto.splitlines():
        if CERCA.match(linha):
            dentro_de_bloco = not dentro_de_bloco
            continue
        if dentro_de_bloco:
            continue
        # Trecho de código em linha (`assim`) também é ilustração.
        linha_sem_codigo = re.sub(r"`[^`]*`", "", linha)
        yield from LINK.findall(linha_sem_codigo)


def main() -> int:
    raiz = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

    quebrados: list[tuple[str, str]] = []
    total = 0

    for md in sorted(raiz.rglob("*.md")):
        if any(parte in IGNORAR for parte in md.parts):
            continue

        for alvo in links_do_arquivo(md.read_text(encoding="utf-8")):
            if alvo.startswith(PREFIXOS_EXTERNOS):
                continue
            if any(marca in alvo for marca in NAO_SAO_ARQUIVOS):
                continue

            caminho = unquote(alvo.split("#")[0])
            if not caminho:
                continue

            total += 1
            if not (md.parent / caminho).resolve().exists():
                quebrados.append((str(md.relative_to(raiz)), alvo))

    print(f"{total} links relativos verificados em {raiz}.")

    if quebrados:
        print(f"\n{len(quebrados)} QUEBRADOS:\n")
        for arquivo, alvo in quebrados:
            print(f"  {arquivo}")
            print(f"      -> {alvo}")
        return 1

    print("Nenhum quebrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
