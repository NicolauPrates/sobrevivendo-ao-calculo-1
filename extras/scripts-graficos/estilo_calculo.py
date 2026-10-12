"""
Estilo visual único de todos os gráficos de "Sobrevivendo ao Cálculo 1 (UENF)".

Este módulo centraliza cores, fontes, eixos e o modo de salvar as figuras, para que
todo gráfico do repositório tenha exatamente a mesma aparência. Nenhum script de
gráfico deve definir cor, fonte ou tamanho por conta própria: tudo sai daqui.

Por que SVG com `svg.fonttype = "path"`
---------------------------------------
Os textos da figura são convertidos em curvas, e não em elementos de texto. Assim a
imagem renderiza igual no GitHub, no celular e no papel, sem depender de o leitor
ter a fonte instalada.

Por que fundo branco explícito
------------------------------
O GitHub tem tema escuro. Uma figura de fundo transparente com eixos escuros
desaparece para metade dos leitores.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sem janela: só gera arquivo

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter, MultipleLocator  # noqa: E402

# --------------------------------------------------------------------------------------
# Caminhos
# --------------------------------------------------------------------------------------

#: Raiz do repositório (este arquivo vive em extras/scripts-graficos/).
RAIZ = Path(__file__).resolve().parents[2]

#: Pasta onde as imagens do material são gravadas.
PASTA_IMG = RAIZ / "assets" / "img"


# --------------------------------------------------------------------------------------
# Paleta
# --------------------------------------------------------------------------------------

CORES = {
    "curva": "#1a5fb4",       # azul — a função principal do gráfico
    "curva2": "#e66100",      # laranja — a segunda função, a inversa, a comparação
    "curva3": "#26734d",      # verde — a terceira função
    "destaque": "#a51d2d",    # vermelho — o que o aluno precisa olhar primeiro
    "auxiliar": "#7b2d8e",    # roxo — reta tangente, secante, construção auxiliar
    "tracejado": "#8a8a8a",   # cinza — assíntotas, retas de referência
    "area": "#1a5fb4",        # preenchimento de área (usado com alpha)
    "eixo": "#2b2b2b",
    "grade": "#dfe3e8",
    "fundo": "#ffffff",
    "texto": "#1a1a1a",
}

#: Ordem de uso das cores quando há várias curvas no mesmo gráfico.
CICLO = [CORES["curva"], CORES["curva2"], CORES["curva3"], CORES["auxiliar"]]


# --------------------------------------------------------------------------------------
# Configuração global
# --------------------------------------------------------------------------------------

def configurar() -> None:
    """Aplica o estilo do repositório ao matplotlib. Chame uma vez, no topo do script."""
    plt.rcParams.update(
        {
            "figure.facecolor": CORES["fundo"],
            "axes.facecolor": CORES["fundo"],
            "savefig.facecolor": CORES["fundo"],
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.12,
            "svg.fonttype": "path",
            "font.family": "DejaVu Sans",
            "font.size": 12,
            "axes.titlesize": 13,
            "axes.labelsize": 12,
            "axes.labelcolor": CORES["texto"],
            "axes.edgecolor": CORES["eixo"],
            "axes.linewidth": 1.1,
            "axes.grid": True,
            "grid.color": CORES["grade"],
            "grid.linewidth": 0.8,
            "lines.linewidth": 2.2,
            "lines.solid_capstyle": "round",
            "text.color": CORES["texto"],
            "xtick.color": CORES["texto"],
            "ytick.color": CORES["texto"],
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.frameon": True,
            "legend.framealpha": 0.95,
            "legend.edgecolor": CORES["grade"],
            "legend.fontsize": 10,
            "mathtext.fontset": "dejavusans",
        }
    )


def _sem_zero(valor: float, _pos: int) -> str:
    """Formatador de eixo que esconde o rótulo 0 (ele polui o cruzamento dos eixos)."""
    if abs(valor) < 1e-9:
        return ""
    if abs(valor - round(valor)) < 1e-9:
        return f"{round(valor):d}"
    return f"{valor:g}".replace(".", ",")


# --------------------------------------------------------------------------------------
# Planos cartesianos
# --------------------------------------------------------------------------------------

def novo_plano(
    xlim: tuple[float, float] = (-5, 5),
    ylim: tuple[float, float] = (-5, 5),
    *,
    figsize: tuple[float, float] = (6.4, 4.6),
    passo_x: float | None = 1,
    passo_y: float | None = 1,
    titulo: str | None = None,
    rotulo_x: str = "$x$",
    rotulo_y: str = "$y$",
    aspecto_igual: bool = False,
):
    """Cria um plano cartesiano no padrão do material: eixos cruzando na origem e setas nas pontas.

    Retorna o par ``(fig, ax)``.
    """
    fig, ax = plt.subplots(figsize=figsize)

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if aspecto_igual:
        ax.set_aspect("equal", adjustable="box")

    # Eixos cruzando na origem, sem a moldura da direita e de cima.
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    if passo_x:
        ax.xaxis.set_major_locator(MultipleLocator(passo_x))
    if passo_y:
        ax.yaxis.set_major_locator(MultipleLocator(passo_y))
    ax.xaxis.set_major_formatter(FuncFormatter(_sem_zero))
    ax.yaxis.set_major_formatter(FuncFormatter(_sem_zero))
    ax.tick_params(direction="inout", length=5, width=1.0)

    # Setas nas extremidades dos eixos.
    ax.plot(1, 0, ">", color=CORES["eixo"], markersize=6,
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^", color=CORES["eixo"], markersize=6,
            transform=ax.get_xaxis_transform(), clip_on=False)

    # Nomes dos eixos junto às setas.
    ax.annotate(rotulo_x, xy=(1, 0), xycoords=ax.get_yaxis_transform(),
                xytext=(6, -16), textcoords="offset points", fontsize=12)
    ax.annotate(rotulo_y, xy=(0, 1), xycoords=ax.get_xaxis_transform(),
                xytext=(8, -4), textcoords="offset points", fontsize=12)

    if titulo:
        ax.set_title(titulo, pad=12)

    ax.set_axisbelow(True)
    return fig, ax


def nova_reta_real(
    xlim: tuple[float, float] = (-5, 5),
    *,
    figsize: tuple[float, float] = (6.8, 1.5),
    passo: float = 1,
    titulo: str | None = None,
):
    """Cria uma reta real isolada — usada para intervalos, módulo e conjuntos-solução."""
    fig, ax = plt.subplots(figsize=figsize)

    ax.set_xlim(*xlim)
    ax.set_ylim(-1, 1)
    ax.grid(False)
    for lado in ("left", "right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_position("zero")
    ax.get_yaxis().set_visible(False)

    ax.xaxis.set_major_locator(MultipleLocator(passo))
    ax.xaxis.set_major_formatter(FuncFormatter(_sem_zero))
    ax.tick_params(direction="inout", length=6, width=1.0)

    ax.plot(1, 0, ">", color=CORES["eixo"], markersize=6,
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.annotate("$x$", xy=(1, 0), xycoords=ax.get_yaxis_transform(),
                xytext=(6, -14), textcoords="offset points", fontsize=12)
    ax.annotate("$0$", xy=(0, 0), xytext=(-3, -16), textcoords="offset points",
                fontsize=10)

    if titulo:
        ax.set_title(titulo, pad=10)
    return fig, ax


# --------------------------------------------------------------------------------------
# Elementos de desenho
# --------------------------------------------------------------------------------------

def plotar(ax, funcao, dominio, *, cor: str | None = None, rotulo: str | None = None,
           estilo: str = "-", largura: float | None = None, n: int = 800):
    """Desenha ``funcao`` sobre ``dominio = (a, b)`` com amostragem densa.

    Use um ``dominio`` por trecho quando a função tiver quebra ou assíntota: assim a
    curva não é ligada por um segmento vertical que não existe.
    """
    a, b = dominio
    x = np.linspace(a, b, n)
    y = funcao(x)
    return ax.plot(x, y, estilo, color=cor or CORES["curva"], label=rotulo,
                   linewidth=largura or plt.rcParams["lines.linewidth"], zorder=3)


def ponto_fechado(ax, x: float, y: float, *, cor: str | None = None, tamanho: float = 7):
    """Bolinha cheia: o ponto **pertence** ao gráfico."""
    return ax.plot([x], [y], "o", color=cor or CORES["curva"], markersize=tamanho,
                   zorder=5, clip_on=False)


def ponto_aberto(ax, x: float, y: float, *, cor: str | None = None, tamanho: float = 7):
    """Bolinha vazia: o ponto **não** pertence ao gráfico."""
    return ax.plot([x], [y], "o", markerfacecolor=CORES["fundo"],
                   markeredgecolor=cor or CORES["curva"], markeredgewidth=1.8,
                   markersize=tamanho, zorder=5, clip_on=False)


def intervalo(ax, a: float, b: float, *, fechado_a: bool = True, fechado_b: bool = True,
              cor: str | None = None, altura: float = 0.0, rotulo: str | None = None):
    """Destaca o intervalo de extremos ``a`` e ``b`` sobre uma reta real.

    Bolinha cheia marca extremo incluído; bolinha vazia, extremo excluído. Use
    ``a = -np.inf`` ou ``b = np.inf`` para intervalos ilimitados (o traço vai até a
    borda da figura e o extremo infinito nunca recebe bolinha).
    """
    cor = cor or CORES["destaque"]
    x_min, x_max = ax.get_xlim()
    inicio = x_min if a == -np.inf else a
    fim = x_max if b == np.inf else b

    ax.plot([inicio, fim], [altura, altura], color=cor, linewidth=4.5,
            solid_capstyle="butt", zorder=4, label=rotulo)
    if a != -np.inf:
        (ponto_fechado if fechado_a else ponto_aberto)(ax, a, altura, cor=cor)
    if b != np.inf:
        (ponto_fechado if fechado_b else ponto_aberto)(ax, b, altura, cor=cor)


def assintota_vertical(ax, x: float, *, rotulo: str | None = None):
    """Reta vertical tracejada, no padrão de assíntota."""
    linha = ax.axvline(x, color=CORES["tracejado"], linestyle="--", linewidth=1.5,
                       zorder=2)
    if rotulo:
        ax.annotate(rotulo, xy=(x, ax.get_ylim()[1]), xytext=(4, -14),
                    textcoords="offset points", color=CORES["tracejado"], fontsize=10)
    return linha


def assintota_horizontal(ax, y: float, *, rotulo: str | None = None):
    """Reta horizontal tracejada, no padrão de assíntota."""
    linha = ax.axhline(y, color=CORES["tracejado"], linestyle="--", linewidth=1.5,
                       zorder=2)
    if rotulo:
        ax.annotate(rotulo, xy=(ax.get_xlim()[1], y), xytext=(-42, 6),
                    textcoords="offset points", color=CORES["tracejado"], fontsize=10)
    return linha


def linha_guia(ax, *, x: float | None = None, y: float | None = None):
    """Linha pontilhada fina de projeção, para indicar coordenada de um ponto."""
    if x is not None:
        ax.axvline(x, color=CORES["tracejado"], linestyle=":", linewidth=1.1, zorder=1)
    if y is not None:
        ax.axhline(y, color=CORES["tracejado"], linestyle=":", linewidth=1.1, zorder=1)


def area_sob(ax, funcao, a: float, b: float, *, cor: str | None = None,
             alpha: float = 0.22, n: int = 400, rotulo: str | None = None):
    """Preenche a região entre o gráfico e o eixo $x$ no intervalo $[a,b]$."""
    x = np.linspace(a, b, n)
    return ax.fill_between(x, funcao(x), color=cor or CORES["area"], alpha=alpha,
                           linewidth=0, label=rotulo, zorder=1)


def anotar(ax, texto: str, xy, xytext, *, cor: str | None = None, seta: bool = True,
           fontsize: int = 11):
    """Anotação com seta — use para dizer ao aluno o que olhar na figura."""
    props = dict(
        arrowprops=dict(arrowstyle="->", color=cor or CORES["destaque"], linewidth=1.3,
                        shrinkA=0, shrinkB=4)
    ) if seta else {}
    return ax.annotate(texto, xy=xy, xytext=xytext, color=cor or CORES["destaque"],
                       fontsize=fontsize, zorder=6, **props)


def legenda(ax, *, local: str = "best"):
    """Legenda no padrão do material (só aparece se houver curvas rotuladas)."""
    if ax.get_legend_handles_labels()[1]:
        return ax.legend(loc=local)
    return None


# --------------------------------------------------------------------------------------
# Gravação
# --------------------------------------------------------------------------------------

def salvar(fig, unidade: str, nome: str) -> Path:
    """Grava a figura em ``assets/img/<unidade>/<nome>.svg`` e devolve o caminho.

    Exemplo:
        >>> salvar(fig, "01-funcoes", "1.3-paridade-x3-3x")
    """
    destino = PASTA_IMG / unidade / f"{nome}.svg"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, format="svg")
    plt.close(fig)
    print(f"  ✓ assets/img/{unidade}/{nome}.svg")
    return destino
