"""
Gráficos da Unidade 5 — Integral.

Rode a partir desta pasta:

    python u5_integrais.py

As figuras são gravadas em assets/img/05-integrais/.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

import estilo_calculo as ec

UNIDADE = "05-integrais"


# ======================================================================================
# 5.1 · Primitivas e o conceito de integral
# ======================================================================================

def familia_de_primitivas() -> None:
    """Todas as primitivas de 2x são x^2 + C: a mesma curva, transladada."""
    fig, ax = ec.novo_plano(xlim=(-2.9, 3.9), ylim=(-4.2, 10.2), figsize=(6.8, 5.0),
                            passo_y=2)

    borda = 2.4
    constantes = (-3, -1.5, 0, 1.5, 3)

    for c in constantes:
        ec.plotar(ax, lambda x, c=c: x**2 + c, (-borda, borda),
                  cor=ec.CORES["curva"], largura=2.0)
        ax.text(borda + 0.12, borda**2 + c, f"$C={c:g}$".replace("-", "−"),
                color=ec.CORES["curva"], fontsize=9.5, ha="left", va="center")

    # As tangentes em x = 1 sao todas paralelas: a inclinacao nao depende de C.
    for c in constantes:
        ax.plot([0.35, 1.65], [2 * 0.35 - 1 + c, 2 * 1.65 - 1 + c],
                color=ec.CORES["destaque"], linewidth=1.3, zorder=4)

    ec.anotar(ax, "em $x=1$ todas as tangentes\nsão paralelas: inclinação $2$",
              xy=(1.7, -0.75), xytext=(1.15, -3.6), fontsize=10)

    ec.salvar(fig, UNIDADE, "5.1-familia-de-primitivas")


def primitiva_pela_condicao() -> None:
    """Uma condição inicial escolhe uma única curva da família."""
    fig, ax = ec.novo_plano(xlim=(-2.6, 2.6), ylim=(-2.4, 6.4), figsize=(6.4, 4.4),
                            passo_y=1)

    for c in (-2, -1, 0, 1, 2, 3):
        ec.plotar(ax, lambda x, c=c: x**2 + c, (-2.45, 2.45),
                  cor=ec.CORES["tracejado"], largura=1.0, estilo="--")

    ec.plotar(ax, lambda x: x**2 + 1, (-2.45, 2.45), cor=ec.CORES["curva"],
              largura=2.6, rotulo="$y = x^2 + 1$")
    ec.ponto_fechado(ax, 0, 1, cor=ec.CORES["destaque"], tamanho=9)

    ec.anotar(ax, "$F(0) = 1$\nescolhe uma só", xy=(0, 1), xytext=(0.7, -1.7),
              fontsize=10)
    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "5.1-primitiva-pela-condicao")


# ======================================================================================
# 5.2 · Técnicas de integração
# ======================================================================================

def triangulos_substituicao() -> None:
    """Os três triângulos de referência da substituição trigonométrica."""
    casos = [
        # (radical, hipotenusa, cateto oposto, cateto adjacente, substituicao)
        ("$\\sqrt{a^2-x^2}$", "$a$", "$x$", "$\\sqrt{a^2-x^2}$",
         "$x = a\\operatorname{sen}\\theta$"),
        ("$\\sqrt{a^2+x^2}$", "$\\sqrt{a^2+x^2}$", "$x$", "$a$",
         "$x = a\\operatorname{tg}\\theta$"),
        ("$\\sqrt{x^2-a^2}$", "$x$", "$\\sqrt{x^2-a^2}$", "$a$",
         "$x = a\\operatorname{sec}\\theta$"),
    ]

    fig, eixos = plt.subplots(1, 3, figsize=(9.8, 3.6))
    for ax, (radical, hip, oposto, adjacente, subst) in zip(eixos, casos):
        ax.set_xlim(-0.35, 4.1)
        ax.set_ylim(-1.15, 2.6)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Triangulo retangulo com o angulo theta no vertice da esquerda.
        base, altura = 2.6, 1.7
        ax.plot([0, base, base, 0], [0, 0, altura, 0],
                color=ec.CORES["curva"], linewidth=2.0)

        # Marca do angulo reto.
        m = 0.22
        ax.plot([base - m, base - m, base], [0, m, m],
                color=ec.CORES["eixo"], linewidth=1.1)

        # Marca do angulo theta.
        t = np.linspace(0, np.arctan2(altura, base), 40)
        ax.plot(0.55 * np.cos(t), 0.55 * np.sin(t),
                color=ec.CORES["destaque"], linewidth=1.2)
        ax.text(0.76, 0.17, "$\\theta$", color=ec.CORES["destaque"], fontsize=12)

        ax.text(base / 2 - 0.3, altura / 2 + 0.42, hip, fontsize=11.5,
                color=ec.CORES["texto"], ha="center", rotation=33)
        ax.text(base + 0.1, altura / 2, oposto, fontsize=11.5,
                color=ec.CORES["texto"], ha="left", va="center")
        ax.text(base / 2, -0.38, adjacente, fontsize=11.5,
                color=ec.CORES["texto"], ha="center", va="top")

        ax.set_title(f"para {radical}", fontsize=11.5, color=ec.CORES["texto"], pad=6)
        ax.text(base / 2, -0.95, subst, fontsize=12,
                color=ec.CORES["destaque"], ha="center", va="center")

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.2-triangulos-substituicao")


# ======================================================================================
# 5.3 · Integral definida e o Teorema Fundamental
# ======================================================================================

def _retangulos(ax, funcao, a, b, n, *, lado="esquerda", cor=None):
    """Desenha n retângulos de aproximação sob a curva."""
    bordas = np.linspace(a, b, n + 1)
    largura = (b - a) / n
    for i in range(n):
        x = bordas[i] if lado == "esquerda" else bordas[i + 1]
        altura = funcao(x)
        ax.add_patch(Rectangle(
            (bordas[i], 0), largura, altura,
            facecolor=cor or ec.CORES["area"], alpha=0.25,
            edgecolor=cor or ec.CORES["curva"], linewidth=1.0, zorder=2))


def somas_de_riemann() -> None:
    """A mesma área aproximada com 4, 8 e 16 retângulos."""


    f = lambda x: 0.4 * x**2 + 0.4
    a, b = 0.0, 3.0
    exata = 0.4 * b**3 / 3 + 0.4 * b  # = 4.8

    fig, eixos = plt.subplots(1, 3, figsize=(9.6, 3.3))
    for ax, n in zip(eixos, (4, 8, 16)):
        ax.set_xlim(-0.35, 3.45)
        ax.set_ylim(-0.5, 4.6)
        for lado in ("right", "top"):
            ax.spines[lado].set_visible(False)
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.set_xticks([0, 1, 2, 3])
        ax.set_yticks([])
        ax.tick_params(labelsize=9)

        _retangulos(ax, f, a, b, n)
        x = np.linspace(a - 0.2, b + 0.3, 300)
        ax.plot(x, f(x), color=ec.CORES["curva"], linewidth=2.2, zorder=4)

        # Soma pela esquerda — subestima, porque a funcao e crescente aqui.
        bordas = np.linspace(a, b, n + 1)[:-1]
        soma = float(np.sum(f(bordas)) * (b - a) / n)
        ax.set_title(f"$n={n}$   soma $= {soma:.2f}$".replace(".", "{,}"),
                     fontsize=10.5, color=ec.CORES["texto"], pad=7)

    eixos[2].text(0.15, 4.25, f"área exata $= {exata:.1f}$".replace(".", "{,}"),
                  fontsize=10.5, color=ec.CORES["destaque"], ha="left", va="top")

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.3-somas-de-riemann")


def area_com_sinal() -> None:
    """A integral soma áreas com sinal: no período inteiro, o saldo é zero."""
    fig, ax = ec.novo_plano(xlim=(-0.7, 7.3), ylim=(-1.9, 1.9), figsize=(7.0, 4.0),
                            passo_y=1)

    f = np.sin
    ec.plotar(ax, f, (-0.5, 7.1), rotulo="$y = \\operatorname{sen} x$")

    x1 = np.linspace(0, np.pi, 300)
    ax.fill_between(x1, f(x1), color=ec.CORES["curva"], alpha=0.25, linewidth=0,
                    zorder=1)
    x2 = np.linspace(np.pi, 2 * np.pi, 300)
    ax.fill_between(x2, f(x2), color=ec.CORES["destaque"], alpha=0.25, linewidth=0,
                    zorder=1)

    ax.text(np.pi / 2, 0.38, "$+2$", fontsize=14, ha="center",
            color=ec.CORES["curva"])
    ax.text(3 * np.pi / 2, -0.52, "$-2$", fontsize=14, ha="center",
            color=ec.CORES["destaque"])

    ax.text(np.pi, 1.55,
            "integral $= +2-2 = 0$,   mas área $= 4$",
            fontsize=11, ha="center", color=ec.CORES["texto"])

    ax.set_xticks([0, np.pi, 2 * np.pi])
    ax.set_xticklabels(["$0$", "$\\pi$", "$2\\pi$"])
    ec.legenda(ax, local="lower left")
    ec.salvar(fig, UNIDADE, "5.3-area-com-sinal")


def funcao_area_acumulada() -> None:
    """O TFC parte 1: A(x) acumula área, e A'(x) = f(x)."""


    f = lambda x: 0.25 * x**2 + 0.5
    a = 0.5

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True)

    for ax in (ax1, ax2):
        ax.set_xlim(-0.2, 3.6)
        for lado in ("right", "top"):
            ax.spines[lado].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.tick_params(labelsize=9)

    # Painel de cima: f e a area acumulada ate x = 2.5.
    ax1.set_ylim(-0.2, 2.9)
    x = np.linspace(-0.1, 3.5, 300)
    ax1.plot(x, f(x), color=ec.CORES["curva"], linewidth=2.3, zorder=3)
    xs = np.linspace(a, 2.5, 300)
    ax1.fill_between(xs, f(xs), color=ec.CORES["area"], alpha=0.25, linewidth=0)
    ax1.plot([a, a], [0, f(a)], color=ec.CORES["tracejado"], linewidth=1.1)
    ax1.plot([2.5, 2.5], [0, f(2.5)], color=ec.CORES["destaque"], linewidth=1.4)
    ax1.text(1.4, 0.42, "$A(x)$", fontsize=13, color=ec.CORES["curva"], ha="center")
    ax1.text(3.3, 2.5, "$y=f(t)$", fontsize=11, color=ec.CORES["curva"], ha="right")
    ax1.set_xticks([a, 2.5])
    ax1.set_xticklabels(["$a$", "$x$"])
    ax1.set_yticks([])

    # Painel de baixo: a propria funcao area.
    ax2.set_ylim(-0.3, 3.4)
    xa = np.linspace(a, 3.5, 300)
    area = 0.25 * (xa**3 - a**3) / 3 + 0.5 * (xa - a)
    ax2.plot(xa, area, color=ec.CORES["curva3"], linewidth=2.3, zorder=3)
    ax2.plot([2.5, 2.5],
             [0, 0.25 * (2.5**3 - a**3) / 3 + 0.5 * (2.5 - a)],
             color=ec.CORES["destaque"], linewidth=1.4)
    ec.ponto_fechado(ax2, a, 0, cor=ec.CORES["curva3"], tamanho=7)
    ax2.text(3.3, 2.9, "$y=A(x)$", fontsize=11, color=ec.CORES["curva3"], ha="right")

    # A tangente a A em x tem inclinacao f(x) — e isso e o TFC.
    altura = 0.25 * (2.5**3 - a**3) / 3 + 0.5 * (2.5 - a)
    inclinacao = f(2.5)
    xt = np.array([1.8, 3.0])
    ax2.plot(xt, altura + inclinacao * (xt - 2.5), color=ec.CORES["auxiliar"],
             linewidth=1.6, zorder=4)
    ax2.annotate("a inclinação de $A$ aqui\nvale exatamente $f(x)$",
                 xy=(2.15, altura + inclinacao * (2.15 - 2.5)), xytext=(0.6, 2.45),
                 color=ec.CORES["auxiliar"], fontsize=9.5, zorder=6,
                 arrowprops=dict(arrowstyle="->", color=ec.CORES["auxiliar"],
                                 linewidth=1.3, shrinkA=0, shrinkB=4))
    ax2.set_xticks([a, 2.5])
    ax2.set_xticklabels(["$a$", "$x$"])
    ax2.set_yticks([])
    ax2.set_xlabel("$x$", fontsize=11)

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.3-funcao-area-acumulada")


def valor_medio_integral() -> None:
    """O retângulo de altura média tem a mesma área que a região sob a curva."""
    fig, ax = ec.novo_plano(xlim=(-0.5, 4.2), ylim=(-0.6, 4.2), figsize=(6.6, 4.2),
                            passo_y=1)

    k = 0.3
    f = lambda x: k * x**2 + 0.5
    a, b = 0.5, 3.0
    media = (k * (b**3 - a**3) / 3 + 0.5 * (b - a)) / (b - a)

    ec.area_sob(ax, f, a, b)
    ec.plotar(ax, f, (-0.3, 3.5))
    ax.text(3.55, f(3.5), "$y=f(x)$", fontsize=11, color=ec.CORES["curva"],
            va="center")

    ax.plot([a, b], [media, media], color=ec.CORES["destaque"], linewidth=1.8,
            zorder=4)
    ax.plot([a, a], [0, media], color=ec.CORES["destaque"], linewidth=1.2)
    ax.plot([b, b], [0, media], color=ec.CORES["destaque"], linewidth=1.2)

    # O c garantido pelo teorema: onde f cruza a altura media.
    c = float(np.sqrt((media - 0.5) / k))
    ec.ponto_fechado(ax, c, media, cor=ec.CORES["destaque"], tamanho=8)

    ax.text(1.75, 3.3,
            "o retângulo de altura média\ntem a mesma área que a região",
            fontsize=10, ha="center", color=ec.CORES["destaque"])
    ax.text(b + 0.1, media, "$f(c)$", fontsize=11, color=ec.CORES["destaque"],
            va="center")
    ax.set_xticks([a, c, b])
    ax.set_xticklabels(["$a$", "$c$", "$b$"])
    ec.salvar(fig, UNIDADE, "5.3-valor-medio-integral")


# ======================================================================================
# 5.4 · Aplicações da integral definida
# ======================================================================================

def area_entre_curvas() -> None:
    """A região entre duas curvas e o retângulo representativo de altura f - g."""
    fig, ax = ec.novo_plano(xlim=(-1.2, 3.4), ylim=(-1.9, 4.6), figsize=(6.6, 4.6),
                            passo_y=1)

    f = lambda x: x + 2          # reta, a curva "de cima"
    g = lambda x: x**2           # parábola, a curva "de baixo"
    a, b = -1.0, 2.0             # interseções: x + 2 = x^2

    x = np.linspace(a, b, 300)
    ax.fill_between(x, g(x), f(x), color=ec.CORES["area"], alpha=0.22, linewidth=0,
                    zorder=1)

    ec.plotar(ax, f, (-1.15, 3.1), cor=ec.CORES["curva"], rotulo="$y = f(x)$")
    ec.plotar(ax, g, (-1.15, 2.1), cor=ec.CORES["curva2"], rotulo="$y = g(x)$")

    # Retangulo representativo: e dele que sai o integrando.
    xr = 0.7
    ax.plot([xr, xr], [g(xr), f(xr)], color=ec.CORES["destaque"], linewidth=2.2,
            zorder=5)
    ax.add_patch(Rectangle((xr - 0.07, g(xr)), 0.14, f(xr) - g(xr),
                           facecolor=ec.CORES["destaque"], alpha=0.3,
                           edgecolor=ec.CORES["destaque"], linewidth=1.0, zorder=4))

    ax.annotate("altura $= f(x)-g(x)$\nlargura $= dx$",
                xy=(xr, g(xr) - 0.04), xytext=(0.75, -1.15), ha="center",
                color=ec.CORES["destaque"], fontsize=10, zorder=6,
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"],
                                linewidth=1.3, shrinkA=0, shrinkB=4))

    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["eixo"], tamanho=6)
    ec.ponto_fechado(ax, b, f(b), cor=ec.CORES["eixo"], tamanho=6)
    ax.set_xticks([a, b])
    ax.set_xticklabels(["$a$", "$b$"])
    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "5.4-area-entre-curvas")


def metodo_do_disco() -> None:
    """A região girada em torno do eixo x, e o disco que o retângulo varre."""
    fig = plt.figure(figsize=(9.4, 4.0))
    f = lambda x: np.sqrt(x)
    a, b, xr = 0.0, 4.0, 2.3

    # --- Painel esquerdo: a regiao plana -------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlim(-0.6, 4.8)
    ax1.set_ylim(-0.8, 2.9)
    for lado in ("right", "top"):
        ax1.spines[lado].set_visible(False)
    ax1.spines["left"].set_position("zero")
    ax1.spines["bottom"].set_position("zero")
    ax1.set_yticks([])
    ax1.set_xticks([a, b])
    ax1.set_xticklabels(["$a$", "$b$"])
    ax1.tick_params(labelsize=9)

    x = np.linspace(a, b, 300)
    ax1.fill_between(x, 0, f(x), color=ec.CORES["area"], alpha=0.22, linewidth=0)
    ax1.plot(x, f(x), color=ec.CORES["curva"], linewidth=2.3, zorder=3)
    ax1.text(4.3, 2.3, "$y=f(x)$", fontsize=11, color=ec.CORES["curva"], ha="right")

    ax1.add_patch(Rectangle((xr - 0.09, 0), 0.18, f(xr),
                            facecolor=ec.CORES["destaque"], alpha=0.35,
                            edgecolor=ec.CORES["destaque"], linewidth=1.0, zorder=4))
    ax1.annotate("raio $= f(x)$", xy=(xr + 0.1, f(xr) / 2), xytext=(0.5, -0.55),
                 color=ec.CORES["destaque"], fontsize=10,
                 arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"],
                                 linewidth=1.3, shrinkA=0, shrinkB=4))
    ax1.set_title("a região", fontsize=11, color=ec.CORES["texto"], pad=4)

    # --- Painel direito: o solido de revolucao -------------------------------------
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    u = np.linspace(a, b, 60)
    t = np.linspace(0, 2 * np.pi, 60)
    U, T = np.meshgrid(u, t)
    # shade=False mantem a cor chapada; com sombreamento, o azul vira cinza.
    ax2.plot_surface(U, f(U) * np.cos(T), f(U) * np.sin(T),
                     color=ec.CORES["curva"], alpha=0.22, linewidth=0,
                     antialiased=True, shade=False)

    # O disco varrido pelo retangulo destacado.
    r = np.linspace(0, f(xr), 20)
    R, T2 = np.meshgrid(r, t)
    ax2.plot_surface(np.full_like(R, xr), R * np.cos(T2), R * np.sin(T2),
                     color=ec.CORES["destaque"], alpha=0.95, linewidth=0,
                     shade=False, zorder=10)

    ax2.set_box_aspect((2.2, 1, 1))
    ax2.view_init(elev=16, azim=-62)
    ax2.set_axis_off()
    ax2.set_title("o sólido, com um disco destacado", fontsize=11,
                  color=ec.CORES["texto"], pad=0)
    ax2.text2D(0.5, 0.02, "$dV = \\pi\\,[f(x)]^2\\,dx$", transform=ax2.transAxes,
               fontsize=12, color=ec.CORES["destaque"], ha="center")

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.4-metodo-do-disco")


def metodo_do_anel() -> None:
    """Região entre duas curvas girada: a secção é um anel, não um disco."""
    fig, eixos = plt.subplots(1, 2, figsize=(9.0, 3.8))

    f = lambda x: np.sqrt(x) + 1.0   # borda externa
    g = lambda x: 0.45 * x           # borda interna
    a, b, xr = 0.0, 4.0, 2.4

    # --- A regiao -------------------------------------------------------------------
    ax = eixos[0]
    ax.set_xlim(-0.6, 4.8)
    ax.set_ylim(-0.5, 3.4)
    for lado in ("right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_yticks([])
    ax.set_xticks([a, b])
    ax.set_xticklabels(["$a$", "$b$"])
    ax.tick_params(labelsize=9)

    x = np.linspace(a, b, 300)
    ax.fill_between(x, g(x), f(x), color=ec.CORES["area"], alpha=0.22, linewidth=0)
    ax.plot(x, f(x), color=ec.CORES["curva"], linewidth=2.2, zorder=3)
    ax.plot(x, g(x), color=ec.CORES["curva2"], linewidth=2.2, zorder=3)
    ax.text(4.2, f(4.0), "$f$", fontsize=12, color=ec.CORES["curva"], va="center")
    ax.text(4.2, g(4.0), "$g$", fontsize=12, color=ec.CORES["curva2"], va="center")

    ax.plot([xr, xr], [g(xr), f(xr)], color=ec.CORES["destaque"], linewidth=2.4,
            zorder=5)
    ax.set_title("a região (não encosta no eixo)", fontsize=11,
                 color=ec.CORES["texto"], pad=4)

    # --- O anel ---------------------------------------------------------------------
    ax = eixos[1]
    ax.set_xlim(-3.1, 3.1)
    ax.set_ylim(-3.5, 2.8)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    R, rr = f(xr), g(xr)
    t = np.linspace(0, 2 * np.pi, 200)
    ax.fill(R * np.cos(t), R * np.sin(t), color=ec.CORES["curva"], alpha=0.28,
            linewidth=0)
    ax.fill(rr * np.cos(t), rr * np.sin(t), color=ec.CORES["fundo"], linewidth=0)
    ax.plot(R * np.cos(t), R * np.sin(t), color=ec.CORES["curva"], linewidth=2.0)
    ax.plot(rr * np.cos(t), rr * np.sin(t), color=ec.CORES["curva2"], linewidth=2.0)

    ax.plot([0, R], [0, 0], color=ec.CORES["curva"], linewidth=1.6)
    ax.plot([0, 0], [0, -rr], color=ec.CORES["curva2"], linewidth=1.6)
    ax.text(R / 2, 0.18, "$R$", fontsize=12, color=ec.CORES["curva"], ha="center")
    ax.text(0.16, -rr / 2, "$r$", fontsize=12, color=ec.CORES["curva2"],
            ha="left", va="center")

    ax.set_title("a secção: um anel", fontsize=11, color=ec.CORES["texto"], pad=4)
    ax.text(0, -2.95, "$R=f(x)$,   $r=g(x)$", fontsize=10.5,
            color=ec.CORES["texto"], ha="center")
    ax.text(0, -3.35, "$dV = \\pi\\left(R^2-r^2\\right)dx$", fontsize=12,
            color=ec.CORES["destaque"], ha="center")

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.4-metodo-do-anel")


def casca_cilindrica() -> None:
    """A casca desenrolada vira um retângulo: 2(pi)x de largura por h de altura."""
    fig, eixos = plt.subplots(1, 2, figsize=(9.2, 3.8))

    h = lambda x: 2.4 - 0.45 * x**2
    a, b, xr = 0.0, 2.1, 1.25

    # --- A regiao e a casca ---------------------------------------------------------
    ax = eixos[0]
    ax.set_xlim(-2.6, 2.8)
    ax.set_ylim(-0.7, 4.1)
    for lado in ("right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_yticks([])
    ax.set_xticks([xr])
    ax.set_xticklabels(["$x$"])
    ax.tick_params(labelsize=9)

    x = np.linspace(a, b, 300)
    ax.fill_between(x, 0, h(x), color=ec.CORES["area"], alpha=0.22, linewidth=0)
    ax.plot(x, h(x), color=ec.CORES["curva"], linewidth=2.2, zorder=3)
    ax.add_patch(Rectangle((xr - 0.08, 0), 0.16, h(xr),
                           facecolor=ec.CORES["destaque"], alpha=0.4,
                           edgecolor=ec.CORES["destaque"], linewidth=1.0, zorder=4))
    # A imagem espelhada mostra para onde o retangulo vai ao girar.
    ax.add_patch(Rectangle((-xr - 0.08, 0), 0.16, h(xr),
                           facecolor=ec.CORES["destaque"], alpha=0.18,
                           edgecolor=ec.CORES["destaque"], linewidth=1.0,
                           linestyle="--", zorder=4))
    ax.annotate("", xy=(-xr, 2.85), xytext=(xr, 2.85),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"],
                                linewidth=1.3, connectionstyle="arc3,rad=0.35"))
    ax.text(0, 3.55, "gira em torno do eixo $y$", fontsize=9.5,
            color=ec.CORES["destaque"], ha="center")
    ax.set_title("o retângulo gira e vira uma casca", fontsize=11,
                 color=ec.CORES["texto"], pad=4)

    # --- A casca desenrolada --------------------------------------------------------
    ax = eixos[1]
    ax.set_xlim(-0.9, 8.2)
    ax.set_ylim(-0.9, 3.2)
    ax.axis("off")

    larg = 7.0
    ax.add_patch(Rectangle((0, 0), larg, h(xr), facecolor=ec.CORES["destaque"],
                           alpha=0.3, edgecolor=ec.CORES["destaque"], linewidth=1.6))
    ax.annotate("", xy=(larg, -0.35), xytext=(0, -0.35),
                arrowprops=dict(arrowstyle="<->", color=ec.CORES["texto"],
                                linewidth=1.2))
    ax.text(larg / 2, -0.72, "$2\\pi x$  (a circunferência)", fontsize=10.5,
            color=ec.CORES["texto"], ha="center")
    ax.annotate("", xy=(-0.4, h(xr)), xytext=(-0.4, 0),
                arrowprops=dict(arrowstyle="<->", color=ec.CORES["texto"],
                                linewidth=1.2))
    ax.text(-0.55, h(xr) / 2, "$h(x)$", fontsize=10.5, color=ec.CORES["texto"],
            ha="right", va="center", rotation=90)

    ax.set_title("desenrolada, é um retângulo", fontsize=11,
                 color=ec.CORES["texto"], pad=4)
    ax.text(larg / 2, 2.72, "$dV = 2\\pi x\\,h(x)\\,dx$", fontsize=12,
            color=ec.CORES["destaque"], ha="center")

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.4-casca-cilindrica")


def comprimento_de_arco() -> None:
    """O arco aproximado por segmentos, e o triângulo que dá a fórmula."""
    fig, eixos = plt.subplots(1, 2, figsize=(9.0, 3.7))

    f = lambda x: 0.35 * x**2 + 0.4

    # --- O arco e a poligonal -------------------------------------------------------
    ax = eixos[0]
    ax.set_xlim(-0.4, 3.4)
    ax.set_ylim(-0.4, 4.0)
    for lado in ("right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_yticks([])
    ax.set_xticks([0.3, 3.0])
    ax.set_xticklabels(["$a$", "$b$"])
    ax.tick_params(labelsize=9)

    x = np.linspace(0.3, 3.0, 300)
    ax.plot(x, f(x), color=ec.CORES["curva"], linewidth=2.4, zorder=3)
    nos = np.linspace(0.3, 3.0, 4)
    ax.plot(nos, f(nos), color=ec.CORES["destaque"], linewidth=1.6,
            marker="o", markersize=5, zorder=4)
    ax.annotate("cada corda\n\"corta\" a curva", xy=(1.9, f(1.65) + 0.08),
                xytext=(0.45, 3.1), color=ec.CORES["destaque"], fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"],
                                linewidth=1.2, shrinkA=0, shrinkB=4))
    ax.set_title("o arco, aproximado por segmentos", fontsize=11,
                 color=ec.CORES["texto"], pad=4)

    # --- O triangulo infinitesimal --------------------------------------------------
    ax = eixos[1]
    ax.set_xlim(-0.5, 4.4)
    ax.set_ylim(-0.8, 3.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    ax.plot([0, 3.2, 3.2, 0], [0, 0, 2.0, 0], color=ec.CORES["eixo"], linewidth=1.6)
    ax.plot([0, 3.2], [0, 2.0], color=ec.CORES["destaque"], linewidth=2.4)
    m = 0.22
    ax.plot([3.2 - m, 3.2 - m, 3.2], [0, m, m], color=ec.CORES["eixo"], linewidth=1.0)

    ax.text(1.6, -0.42, "$dx$", fontsize=13, color=ec.CORES["texto"], ha="center")
    ax.text(3.35, 1.0, "$dy$", fontsize=13, color=ec.CORES["texto"], va="center")
    ax.text(1.35, 1.35, "$ds$", fontsize=13, color=ec.CORES["destaque"], ha="center")

    ax.text(1.8, 2.6, "$ds=\\sqrt{dx^2+dy^2}=\\sqrt{1+(y')^2}\\;dx$", fontsize=11.5,
            color=ec.CORES["destaque"], ha="center")
    ax.set_title("cada segmento é a hipotenusa", fontsize=11,
                 color=ec.CORES["texto"], pad=4)

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.4-comprimento-de-arco")


# ======================================================================================
# 5.5 · Integrais impróprias
# ======================================================================================

def dois_tipos_de_impropria() -> None:
    """Tipo 1: o intervalo é infinito. Tipo 2: o integrando explode."""
    fig, eixos = plt.subplots(1, 2, figsize=(9.2, 3.6))

    # --- Tipo 1: intervalo infinito -------------------------------------------------
    ax = eixos[0]
    ax.set_xlim(-0.5, 6.4)
    ax.set_ylim(-0.35, 1.5)
    for lado in ("right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_yticks([])
    ax.set_xticks([1])
    ax.set_xticklabels(["$a$"])
    ax.tick_params(labelsize=10)

    f = lambda x: np.exp(-0.55 * (x - 1))
    x = np.linspace(1, 6.2, 300)
    ax.fill_between(x, f(x), color=ec.CORES["area"], alpha=0.25, linewidth=0)
    ax.plot(x, f(x), color=ec.CORES["curva"], linewidth=2.3, zorder=3)
    ax.plot([1, 1], [0, f(1)], color=ec.CORES["curva"], linewidth=1.4)
    ax.annotate("", xy=(6.3, 0), xytext=(5.4, 0),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"],
                                linewidth=1.6))
    ax.text(4.3, 0.75, "o intervalo\nnão termina", fontsize=10,
            color=ec.CORES["destaque"], ha="center")
    ax.set_title("Tipo 1 — intervalo infinito", fontsize=11.5,
                 color=ec.CORES["texto"], pad=6)

    # --- Tipo 2: integrando ilimitado -----------------------------------------------
    ax = eixos[1]
    ax.set_xlim(-0.5, 4.4)
    ax.set_ylim(-0.35, 4.4)
    for lado in ("right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_yticks([])
    ax.set_xticks([1, 4])
    ax.set_xticklabels(["$a$", "$b$"])
    ax.tick_params(labelsize=10)

    g = lambda x: 1.1 / np.sqrt(x - 1)
    x = np.linspace(1.08, 4.0, 300)
    ax.fill_between(x, g(x), color=ec.CORES["area"], alpha=0.25, linewidth=0)
    ax.plot(x, g(x), color=ec.CORES["curva"], linewidth=2.3, zorder=3)
    ax.plot([1, 1], [0, 4.3], color=ec.CORES["tracejado"], linewidth=1.4,
            linestyle="--", zorder=2)
    ax.plot([4, 4], [0, g(4.0)], color=ec.CORES["curva"], linewidth=1.4)
    ax.annotate("", xy=(1.06, 4.25), xytext=(1.06, 3.1),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"],
                                linewidth=1.6))
    ax.text(2.6, 3.3, "a função\nnão é limitada", fontsize=10,
            color=ec.CORES["destaque"], ha="center")
    ax.set_title("Tipo 2 — integrando ilimitado", fontsize=11.5,
                 color=ec.CORES["texto"], pad=6)

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.5-dois-tipos")


def convergencia_1x_versus_1x2() -> None:
    """Mesma aparência, destinos opostos: 1/x diverge, 1/x^2 converge."""
    fig, eixos = plt.subplots(1, 2, figsize=(9.2, 3.8), sharey=True)

    casos = [
        (lambda x: 1 / x, "$y = \\dfrac{1}{x}$",
         "área até $b$: $\\ln b \\to \\infty$", "DIVERGE", ec.CORES["destaque"]),
        (lambda x: 1 / x**2, "$y = \\dfrac{1}{x^2}$",
         "área até $b$: $1-\\dfrac{1}{b} \\to 1$", "CONVERGE para $1$",
         ec.CORES["curva3"]),
    ]

    for ax, (f, nome, conta, veredito, cor) in zip(eixos, casos):
        ax.set_xlim(-0.4, 6.6)
        ax.set_ylim(-0.3, 1.75)
        for lado in ("right", "top"):
            ax.spines[lado].set_visible(False)
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.set_yticks([1])
        ax.set_xticks([1])
        ax.tick_params(labelsize=10)

        x = np.linspace(1, 6.4, 400)
        ax.fill_between(x, f(x), color=cor, alpha=0.22, linewidth=0)
        xc = np.linspace(0.62, 6.4, 400)
        ax.plot(xc, f(xc), color=ec.CORES["curva"], linewidth=2.3, zorder=3)
        ax.plot([1, 1], [0, 1], color=ec.CORES["curva"], linewidth=1.4)

        ax.text(4.3, 1.42, nome, fontsize=13, color=ec.CORES["curva"], ha="center")
        ax.text(4.3, 1.02, conta, fontsize=10, color=ec.CORES["texto"], ha="center")
        ax.text(3.3, -0.22, veredito, fontsize=11.5, color=cor, ha="center",
                fontweight="bold")

    fig.tight_layout()
    ec.salvar(fig, UNIDADE, "5.5-convergencia-comparada")


# ======================================================================================

FIGURAS = [
    familia_de_primitivas,
    primitiva_pela_condicao,
    triangulos_substituicao,
    somas_de_riemann,
    area_com_sinal,
    funcao_area_acumulada,
    valor_medio_integral,
    area_entre_curvas,
    metodo_do_disco,
    metodo_do_anel,
    casca_cilindrica,
    comprimento_de_arco,
    dois_tipos_de_impropria,
    convergencia_1x_versus_1x2,
]


def main() -> None:
    ec.configurar()
    print("Gerando as figuras da Unidade 5...")
    for figura in FIGURAS:
        figura()
    print(f"Pronto: {len(FIGURAS)} figuras.")


if __name__ == "__main__":
    main()
