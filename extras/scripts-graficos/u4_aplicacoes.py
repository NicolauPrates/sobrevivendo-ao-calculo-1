"""
Gráficos da Unidade 4 — Derivadas: aplicações.

Rode a partir desta pasta:

    python u4_aplicacoes.py

As figuras são gravadas em assets/img/04-aplicacoes-das-derivadas/.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import numpy as np

import estilo_calculo as ec

UNIDADE = "04-aplicacoes-das-derivadas"


def _figura_geometrica(xlim, ylim, figsize):
    """Figura sem plano cartesiano, para desenhos de enunciado."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for lado in ("left", "bottom", "right", "top"):
        ax.spines[lado].set_visible(False)
    return fig, ax


# ======================================================================================
# 4.1 — Máximos e mínimos
# ======================================================================================

def extremos_locais_e_absolutos() -> None:
    """Uma função em [a,b] com todos os tipos de extremo marcados."""
    fig, ax = ec.novo_plano(xlim=(-0.7, 5.9), ylim=(-7.5, 2.4), figsize=(7.0, 4.8),
                            passo_y=1)

    f = lambda x: 0.2 * x**4 - 2 * x**3 + 6 * x**2 - 6 * x
    a, b = 0.0, 5.0

    ec.plotar(ax, f, (a, b), rotulo="$y=f(x)$")

    # Pontos notáveis, achados numericamente.
    xs = np.linspace(a, b, 5000)
    ys = f(xs)
    i_min_abs = int(np.argmin(ys))
    i_max_abs = int(np.argmax(ys))

    # Extremos locais interiores (derivada troca de sinal).
    d = np.diff(np.sign(np.diff(ys)))
    criticos = [xs[i + 1] for i in np.nonzero(d)[0]]

    for c in criticos:
        ec.ponto_fechado(ax, c, f(c), cor=ec.CORES["curva2"], tamanho=6)
    ec.ponto_fechado(ax, xs[i_min_abs], ys[i_min_abs], cor=ec.CORES["destaque"],
                     tamanho=8)
    ec.ponto_fechado(ax, xs[i_max_abs], ys[i_max_abs], cor=ec.CORES["destaque"],
                     tamanho=8)
    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["eixo"], tamanho=6)
    ec.ponto_fechado(ax, b, f(b), cor=ec.CORES["eixo"], tamanho=6)

    ax.annotate("mín. local", xy=(criticos[0], f(criticos[0])), xytext=(-20, -26),
                textcoords="offset points", color=ec.CORES["curva2"], fontsize=9)
    ax.annotate("máx. local", xy=(criticos[1], f(criticos[1])), xytext=(-22, 14),
                textcoords="offset points", color=ec.CORES["curva2"], fontsize=9)
    ax.annotate("mín. absoluto", xy=(xs[i_min_abs], ys[i_min_abs]), xytext=(-30, -26),
                textcoords="offset points", color=ec.CORES["destaque"], fontsize=9)
    ax.annotate("máx. absoluto\n(na borda!)", xy=(xs[i_max_abs], ys[i_max_abs]),
                xytext=(10, 6), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=9)
    ax.annotate("$a$", xy=(a, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)
    ax.annotate("$b$", xy=(b, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "4.1-extremos-locais-e-absolutos")


def critico_sem_extremo() -> None:
    """x^3 tem ponto crítico em 0 que não é máximo nem mínimo."""
    fig, ax = ec.novo_plano(xlim=(-2.2, 2.2), ylim=(-4.5, 4.5), figsize=(4.6, 3.8),
                            titulo="crítico, mas não é extremo", passo_y=2)

    ec.plotar(ax, lambda x: x**3, (-1.62, 1.62))
    ax.axhline(0, color=ec.CORES["destaque"], linestyle="--", linewidth=1.4, zorder=2)
    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["destaque"], tamanho=7)
    ax.annotate(r"$f'(0)=0$", xy=(0, 0), xytext=(12, 10), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=10)

    ec.salvar(fig, UNIDADE, "4.1-critico-sem-extremo")


def teste_primeira_derivada() -> None:
    """Como o sinal de f' identifica máximo e mínimo locais."""
    fig, ax = ec.novo_plano(xlim=(-2.8, 2.8), ylim=(-3.5, 4.5), figsize=(6.6, 4.6),
                            passo_y=1)

    f = lambda x: x**3 - 3 * x
    d = lambda x: 3 * x**2 - 3

    ec.plotar(ax, f, (-2.3, 2.3), cor=ec.CORES["curva"], rotulo="$f$")
    ec.plotar(ax, d, (-2.0, 2.0), cor=ec.CORES["curva2"], rotulo="$f'$")

    ec.ponto_fechado(ax, -1, f(-1), cor=ec.CORES["destaque"], tamanho=7)
    ec.ponto_fechado(ax, 1, f(1), cor=ec.CORES["destaque"], tamanho=7)
    ec.linha_guia(ax, x=-1)
    ec.linha_guia(ax, x=1)

    ax.annotate("$f'>0$\ncresce", xy=(-2.0, 3.3), color=ec.CORES["curva3"], fontsize=9)
    ax.annotate("$f'<0$\ndecresce", xy=(-0.45, 2.6), color=ec.CORES["curva3"],
                fontsize=9)
    ax.annotate("$f'>0$\ncresce", xy=(1.5, 3.3), color=ec.CORES["curva3"], fontsize=9)
    ax.annotate("máximo local", xy=(-1, 2), xytext=(-2.75, -2.2),
                color=ec.CORES["destaque"], fontsize=9)
    ax.annotate("mínimo local", xy=(1, -2), xytext=(1.25, -3.1),
                color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower left")
    ec.salvar(fig, UNIDADE, "4.1-teste-primeira-derivada")


def caixa_otimizacao() -> None:
    """A folha quadrada com cantos recortados, que vira caixa."""
    fig, ax = _figura_geometrica((-0.6, 7.0), (-1.4, 6.4), (5.6, 4.6))

    L, x = 6.0, 1.2

    # Folha.
    ax.plot([0, L, L, 0, 0], [0, 0, L, L, 0], color=ec.CORES["eixo"], linewidth=2.0)

    # Cantos recortados.
    for cx, cy in [(0, 0), (L - x, 0), (0, L - x), (L - x, L - x)]:
        ax.fill([cx, cx + x, cx + x, cx], [cy, cy, cy + x, cy + x],
                color=ec.CORES["destaque"], alpha=0.25, zorder=1)
        ax.plot([cx, cx + x, cx + x, cx, cx], [cy, cy, cy + x, cy + x, cy],
                color=ec.CORES["destaque"], linewidth=1.4, linestyle="--", zorder=2)

    # Linhas de dobra.
    ax.plot([x, L - x, L - x, x, x], [x, x, L - x, L - x, x],
            color=ec.CORES["curva"], linewidth=1.8, linestyle=":", zorder=3)

    ax.annotate(r"$x$", xy=(x / 2, -0.45), ha="center", color=ec.CORES["destaque"],
                fontsize=12)
    ax.annotate(r"$x$", xy=(-0.35, x / 2), va="center", color=ec.CORES["destaque"],
                fontsize=12)
    ax.annotate(r"$L$", xy=(L / 2, L + 0.3), ha="center", color=ec.CORES["eixo"],
                fontsize=12)
    ax.annotate(r"$L-2x$", xy=(L / 2, x + 0.3), ha="center", color=ec.CORES["curva"],
                fontsize=11)
    ax.annotate("dobre as abas\npara cima", xy=(L + 0.1, L / 2), va="center",
                color=ec.CORES["curva"], fontsize=9)

    ec.salvar(fig, UNIDADE, "4.1-caixa-otimizacao")


# ======================================================================================
# 4.2 — Teoremas de Rolle e do Valor Médio
# ======================================================================================

def teorema_de_rolle() -> None:
    """f(a) = f(b) obriga uma tangente horizontal em algum ponto interior."""
    fig, ax = ec.novo_plano(xlim=(-0.6, 5.4), ylim=(-1.4, 3.6), figsize=(6.4, 4.2),
                            passo_y=1)

    f = lambda x: -0.5 * (x - 1) * (x - 4) + 1
    a, b = 1.0, 4.0

    ec.plotar(ax, f, (a - 0.35, b + 0.35), rotulo="$y=f(x)$")

    # f(a) = f(b): reta horizontal ligando as pontas.
    ax.plot([a, b], [f(a), f(b)], color=ec.CORES["tracejado"], linestyle="--",
            linewidth=1.4, zorder=2)
    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["eixo"], tamanho=6)
    ec.ponto_fechado(ax, b, f(b), cor=ec.CORES["eixo"], tamanho=6)

    c = 2.5  # vértice da parábola
    ax.plot([c - 1.1, c + 1.1], [f(c), f(c)], color=ec.CORES["destaque"],
            linewidth=2.0, zorder=3)
    ec.ponto_fechado(ax, c, f(c), cor=ec.CORES["destaque"], tamanho=7)

    ax.annotate("$a$", xy=(a, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)
    ax.annotate("$b$", xy=(b, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)
    ax.annotate("$c$", xy=(c, 0), xytext=(-4, -20), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=11)
    ec.linha_guia(ax, x=c)
    ax.annotate("$f(a)=f(b)$", xy=(a, f(a)), xytext=(-6, -24),
                textcoords="offset points", color=ec.CORES["tracejado"], fontsize=10)
    ax.annotate(r"$f'(c)=0$", xy=(c, f(c)), xytext=(8, 12),
                textcoords="offset points", color=ec.CORES["destaque"], fontsize=11)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "4.2-teorema-de-rolle")


def teorema_valor_medio() -> None:
    """A tangente em c é paralela à secante que liga as pontas."""
    fig, ax = ec.novo_plano(xlim=(-0.6, 5.2), ylim=(-1.4, 4.6), figsize=(6.6, 4.4),
                            passo_y=1)

    f = lambda x: 0.22 * x**3 - 1.3 * x**2 + 2.4 * x
    a, b = 0.6, 4.2

    ec.plotar(ax, f, (a - 0.5, b + 0.4), rotulo="$y=f(x)$")

    m = (f(b) - f(a)) / (b - a)
    ax.plot([a - 0.3, b + 0.3], [f(a) + m * (-0.3), f(b) + m * (0.3)],
            color=ec.CORES["curva2"], linewidth=2.0, zorder=3)
    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["eixo"], tamanho=6)
    ec.ponto_fechado(ax, b, f(b), cor=ec.CORES["eixo"], tamanho=6)

    # Onde f'(c) = m: resolve numericamente.
    xs = np.linspace(a, b, 4000)
    d = 0.66 * xs**2 - 2.6 * xs + 2.4
    c = xs[int(np.argmin(np.abs(d - m)))]

    ax.plot([c - 1.0, c + 1.0], [f(c) - m, f(c) + m], color=ec.CORES["destaque"],
            linewidth=2.0, zorder=4)
    ec.ponto_fechado(ax, c, f(c), cor=ec.CORES["destaque"], tamanho=7)
    ec.linha_guia(ax, x=c)

    ax.annotate("$a$", xy=(a, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)
    ax.annotate("$b$", xy=(b, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)
    ax.annotate("$c$", xy=(c, 0), xytext=(-4, -20), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=11)
    ax.annotate("secante", xy=(b - 0.6, f(b) - 0.55), color=ec.CORES["curva2"],
                fontsize=10)
    ax.annotate("tangente paralela", xy=(c + 0.15, f(c) + 0.75),
                color=ec.CORES["destaque"], fontsize=10)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "4.2-teorema-valor-medio")


# ======================================================================================

FIGURAS = [
    extremos_locais_e_absolutos,
    critico_sem_extremo,
    teste_primeira_derivada,
    caixa_otimizacao,
    teorema_de_rolle,
    teorema_valor_medio,
]


def main() -> None:
    ec.configurar()
    print("Gerando as figuras da Unidade 4...")
    for figura in FIGURAS:
        figura()
    print(f"Pronto: {len(FIGURAS)} figuras.")


if __name__ == "__main__":
    main()
