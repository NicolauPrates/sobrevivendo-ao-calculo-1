"""
Extrai toda a matemática dos arquivos .md já com o pré-processamento do GitHub aplicado.

Por que isso é necessário
-------------------------
O GitHub aplica os escapes do Markdown **antes** de entregar a fórmula ao KaTeX.
Dentro de ``$...$`` — e de um ``$$...$$`` escrito em uma linha só — toda barra
invertida seguida de pontuação ASCII é simplesmente apagada. Então ``\\{`` vira
``{``, ``\\,`` vira ``,`` e ``\\left\\{`` vira ``\\left{``, que é um erro fatal:
ele derruba **todas** as fórmulas da página, não só a defeituosa.

Num bloco ``$$`` escrito em várias linhas, com os delimitadores sozinhos, nada
disso acontece: o conteúdo chega intacto. (A regra completa está na §5.1 de
CONVENCOES.md.)

Este script reproduz esse comportamento e grava, em ``formulas.json``, exatamente
o que o KaTeX receberia. O arquivo é lido por ``verifica.html``.

Uso
---
    python extrai_formulas.py            # usa a raiz do repositório
    python extrai_formulas.py <caminho>  # usa outra pasta

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

#: Pontuação ASCII — o conjunto que o Markdown aceita escapar com barra invertida.
PONTUACAO = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

RE_FENCE = re.compile(r"^\s*(```|~~~)")
RE_CODIGO_INLINE = re.compile(r"`[^`\n]*`")
RE_PREFIXO_CITACAO = re.compile(r"^(\s*>\s?)+")
RE_DISPLAY_LINHA = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
RE_INLINE = re.compile(r"(?<!\$)\$(?!\s)([^\$\n]+?)(?<!\s)\$(?!\$)")

RAIZ_PADRAO = Path(__file__).resolve().parents[2]


def aplicar_escapes(texto: str) -> str:
    """Reproduz o que o Markdown faz: barra invertida antes de pontuação some."""
    saida: list[str] = []
    i = 0
    while i < len(texto):
        if texto[i] == "\\" and i + 1 < len(texto) and texto[i + 1] in PONTUACAO:
            saida.append(texto[i + 1])
            i += 2
        else:
            saida.append(texto[i])
            i += 1
    return "".join(saida)


def extrair(md: str, arquivo: str) -> list[dict]:
    """Devolve a lista de fórmulas de um arquivo, já como o KaTeX as receberia."""
    itens: list[dict] = []
    em_fence = False
    em_bloco = False
    buffer: list[str] = []
    restante: list[str] = []

    for linha in md.split("\n"):
        if RE_FENCE.match(linha):
            em_fence = not em_fence
            continue
        if em_fence:
            continue

        nua = RE_PREFIXO_CITACAO.sub("", linha).strip()

        if em_bloco:
            if nua == "$$":
                itens.append({
                    "arquivo": arquivo,
                    "estilo": "display",
                    "contexto": "bloco $$ em varias linhas",
                    "tex": "\n".join(buffer),
                })
                buffer, em_bloco = [], False
            else:
                buffer.append(RE_PREFIXO_CITACAO.sub("", linha))
            continue

        if nua == "$$":
            em_bloco = True
            continue

        restante.append(linha)

    texto = RE_CODIGO_INLINE.sub(" ", "\n".join(restante))

    for m in RE_DISPLAY_LINHA.finditer(texto):
        itens.append({
            "arquivo": arquivo,
            "estilo": "display",
            "contexto": "$$ em uma linha so",
            "tex": aplicar_escapes(m.group(1)),
        })

    for m in RE_INLINE.finditer(RE_DISPLAY_LINHA.sub(" ", texto)):
        itens.append({
            "arquivo": arquivo,
            "estilo": "inline",
            "contexto": "inline",
            "tex": aplicar_escapes(m.group(1)),
        })

    return itens


def main() -> None:
    raiz = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ_PADRAO
    todos: list[dict] = []

    for p in sorted(raiz.rglob("*.md")):
        if ".git" in p.parts:
            continue
        md = p.read_text(encoding="utf-8")
        if "$" not in md:
            continue
        rel = str(p.relative_to(raiz)).replace("\\", "/")
        achados = extrair(md, rel)
        todos.extend(achados)
        print(f"  {rel}: {len(achados)} formulas")

    destino = Path(__file__).with_name("formulas.json")
    destino.write_text(json.dumps(todos, ensure_ascii=False), encoding="utf-8")
    print(f"\n{len(todos)} formulas gravadas em {destino.name}")
    print("Agora abra verifica.html (veja o README desta pasta).")


if __name__ == "__main__":
    main()
