"""
Gráficos da Unidade 2 — Limites e continuidade.

Rode a partir desta pasta:

    python u2_limites.py

As figuras são gravadas em assets/img/02-limites-e-continuidade/.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import numpy as np

import estilo_calculo as ec

UNIDADE = "02-limites-e-continuidade"


# ======================================================================================
# 2.1 — Conceito e noção intuitiva de limite
# ======================================================================================

def ideia_de_limite() -> None:
    """A reta y = x+1 com um furo em x = 1: o limite existe, o valor não."""
    fig, ax = ec.novo_plano(xlim=(-1, 3.5), ylim=(-1, 4.5), figsize=(6.4, 4.4))

    ec.plotar(ax, lambda x: x + 1, (-1, 3.5),
              rotulo=r"$f(x)=\dfrac{x^2-1}{x-1}$")
    ec.ponto_aberto(ax, 1, 2, cor=ec.CORES["curva"], tamanho=8)

    ec.linha_guia(ax, x=1)
    ec.linha_guia(ax, y=2)

    # Setas de aproximação pela esquerda e pela direita.
    ax.annotate("", xy=(0.93, 1.93), xytext=(0.25, 1.25),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"], lw=1.6))
    ax.annotate("", xy=(1.07, 2.07), xytext=(1.75, 2.75),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"], lw=1.6))
    ax.annotate(r"$L=2$", xy=(1, 2), xytext=(-0.92, 2.25),
                color=ec.CORES["destaque"], fontsize=11)
    ax.annotate("o furo não atrapalha:\no limite é 2", xy=(1, 2), xytext=(1.5, 0.6),
                color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "2.1-ideia-de-limite")


def _plano_pequeno(titulo: str):
    return ec.novo_plano(xlim=(-0.6, 2.6), ylim=(-0.6, 3.6), figsize=(3.5, 3.1),
                         titulo=titulo, passo_x=1, passo_y=1)


def valor_nao_importa_a() -> None:
    """Caso 1: f(1) não existe."""
    fig, ax = _plano_pequeno("$f(1)$ não existe")
    ec.plotar(ax, lambda x: x + 1, (-0.6, 2.6))
    ec.ponto_aberto(ax, 1, 2, cor=ec.CORES["curva"])
    ec.salvar(fig, UNIDADE, "2.1-valor-nao-importa-a")


def valor_nao_importa_b() -> None:
    """Caso 2: f(1) = 2, igual ao limite."""
    fig, ax = _plano_pequeno("$f(1)=2$")
    ec.plotar(ax, lambda x: x + 1, (-0.6, 2.6))
    ec.ponto_fechado(ax, 1, 2, cor=ec.CORES["curva"])
    ec.salvar(fig, UNIDADE, "2.1-valor-nao-importa-b")


def valor_nao_importa_c() -> None:
    """Caso 3: f(1) = 3, diferente do limite."""
    fig, ax = _plano_pequeno("$f(1)=3$")
    ec.plotar(ax, lambda x: x + 1, (-0.6, 2.6))
    ec.ponto_aberto(ax, 1, 2, cor=ec.CORES["curva"])
    ec.ponto_fechado(ax, 1, 3, cor=ec.CORES["destaque"])
    ec.salvar(fig, UNIDADE, "2.1-valor-nao-importa-c")


def nao_existe_salto() -> None:
    """Limite não existe por salto: os dois lados discordam."""
    fig, ax = ec.novo_plano(xlim=(-2.6, 2.6), ylim=(-2.6, 3.2), figsize=(3.9, 3.3),
                            titulo="salto")
    ec.plotar(ax, lambda x: x + 1, (-2.6, 0), cor=ec.CORES["curva"])
    ec.plotar(ax, lambda x: x - 2, (0, 2.6), cor=ec.CORES["curva2"])
    ec.ponto_fechado(ax, 0, 1, cor=ec.CORES["curva"])
    ec.ponto_aberto(ax, 0, -2, cor=ec.CORES["curva2"])
    ec.salvar(fig, UNIDADE, "2.1-nao-existe-salto")


def nao_existe_oscilacao() -> None:
    """Limite não existe por oscilação: sen(1/x) perto de zero."""
    fig, ax = ec.novo_plano(xlim=(-0.35, 0.35), ylim=(-1.6, 1.6), figsize=(3.9, 3.3),
                            titulo="oscilação", passo_x=None, passo_y=1)
    ax.set_xticks([-0.3, -0.1, 0.1, 0.3])
    ax.set_xticklabels(["-0,3", "-0,1", "0,1", "0,3"])

    x1 = np.linspace(-0.35, -0.0015, 6000)
    x2 = np.linspace(0.0015, 0.35, 6000)
    for x in (x1, x2):
        ax.plot(x, np.sin(1 / x), color=ec.CORES["curva"], linewidth=1.1, zorder=3)
    ec.salvar(fig, UNIDADE, "2.1-nao-existe-oscilacao")


def nao_existe_infinito() -> None:
    """Limite não existe por explosão: 1/x^2 perto de zero."""
    fig, ax = ec.novo_plano(xlim=(-2.6, 2.6), ylim=(-1, 8), figsize=(3.9, 3.3),
                            titulo="explosão", passo_y=2)
    for trecho in [(-2.6, -0.36), (0.36, 2.6)]:
        ec.plotar(ax, lambda x: 1 / x**2, trecho, cor=ec.CORES["curva"])
    ec.assintota_vertical(ax, 0)
    ec.salvar(fig, UNIDADE, "2.1-nao-existe-infinito")


def epsilon_delta() -> None:
    """A figura da definição formal, para f(x) = 2x+1 em a = 2, L = 5."""
    fig, ax = ec.novo_plano(xlim=(0, 4), ylim=(0, 9), figsize=(6.4, 4.8),
                            passo_x=1, passo_y=1)

    a, L, eps = 2.0, 5.0, 1.2
    delta = eps / 2

    # Faixas horizontal (epsilon) e vertical (delta).
    ax.axhspan(L - eps, L + eps, color=ec.CORES["curva2"], alpha=0.16, zorder=1)
    ax.axvspan(a - delta, a + delta, color=ec.CORES["curva3"], alpha=0.16, zorder=1)

    ec.plotar(ax, lambda x: 2 * x + 1, (0, 4), rotulo="$f(x)=2x+1$")
    ec.ponto_fechado(ax, a, L, cor=ec.CORES["destaque"], tamanho=7)

    for y in (L - eps, L + eps):
        ax.axhline(y, color=ec.CORES["curva2"], linestyle="--", linewidth=1.2, zorder=2)
    for x in (a - delta, a + delta):
        ax.axvline(x, color=ec.CORES["curva3"], linestyle="--", linewidth=1.2, zorder=2)

    # Caixa branca atrás do rótulo: sem ela, a linha tracejada corta o texto e
    # o sinal de menos passa a parecer um sinal de mais.
    caixa = dict(boxstyle="round,pad=0.15", facecolor=ec.CORES["fundo"], edgecolor="none")
    ax.annotate(r"$L+\varepsilon$", xy=(0.06, L + eps + 0.15), color=ec.CORES["curva2"],
                fontsize=10, bbox=caixa)
    ax.annotate(r"$L-\varepsilon$", xy=(0.06, L - eps + 0.15), color=ec.CORES["curva2"],
                fontsize=10, bbox=caixa)
    ax.annotate(r"$a-\delta$", xy=(a - delta, 0.12), ha="center",
                color=ec.CORES["curva3"], fontsize=10, bbox=caixa)
    ax.annotate(r"$a+\delta$", xy=(a + delta, 0.12), ha="center",
                color=ec.CORES["curva3"], fontsize=10, bbox=caixa)
    ax.annotate(r"$L$", xy=(a, L), xytext=(10, 6), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=11)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "2.1-epsilon-delta")


# ======================================================================================
# 2.2 — Limites laterais
# ======================================================================================

def laterais_iguais() -> None:
    """Os dois lados vão para o mesmo valor: o limite bilateral existe."""
    fig, ax = ec.novo_plano(xlim=(-1.5, 4.5), ylim=(-1.5, 4.5), figsize=(6.4, 4.4))

    ec.plotar(ax, lambda x: x + 1, (-1.5, 2), cor=ec.CORES["curva"],
              rotulo="$x+1$, para $x < 2$")
    ec.plotar(ax, lambda x: 5 - x, (2, 4.5), cor=ec.CORES["curva2"],
              rotulo="$5-x$, para $x > 2$")
    ec.ponto_aberto(ax, 2, 3, cor=ec.CORES["destaque"])

    ec.linha_guia(ax, x=2)
    ax.annotate(r"$\lim_{x \to 2^-} f(x) = 3$", xy=(2, 3), xytext=(-1.4, 3.9),
                color=ec.CORES["curva"], fontsize=10)
    ax.annotate(r"$\lim_{x \to 2^+} f(x) = 3$", xy=(2, 3), xytext=(2.35, 3.9),
                color=ec.CORES["curva2"], fontsize=10)
    ax.annotate("os dois lados concordam:\no limite existe e vale 3",
                xy=(2, 3), xytext=(0.1, 0.25), color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.2-laterais-iguais")


def laterais_com_salto() -> None:
    """Salto: os laterais existem, são diferentes, e o limite não existe."""
    fig, ax = ec.novo_plano(xlim=(-1.5, 4.5), ylim=(-2.5, 4.5), figsize=(6.4, 4.4))

    ec.plotar(ax, lambda x: x + 1, (-1.5, 2), cor=ec.CORES["curva"],
              rotulo="$x+1$, para $x < 2$")
    ec.plotar(ax, lambda x: x - 3, (2, 4.5), cor=ec.CORES["curva2"],
              rotulo="$x-3$, para $x \\geq 2$")

    ec.ponto_aberto(ax, 2, 3, cor=ec.CORES["curva"])
    ec.ponto_fechado(ax, 2, -1, cor=ec.CORES["curva2"])

    ax.annotate(r"$\lim_{x \to 2^-} f(x) = 3$", xy=(2, 3), xytext=(-1.4, 3.7),
                color=ec.CORES["curva"], fontsize=10)
    ax.annotate(r"$\lim_{x \to 2^+} f(x) = -1$", xy=(2, -1), xytext=(2.4, -2.1),
                color=ec.CORES["curva2"], fontsize=10)
    ax.annotate("salto de\naltura 4", xy=(2, 1), xytext=(2.6, 1.3),
                color=ec.CORES["destaque"], fontsize=9)
    ax.annotate("", xy=(2, 3), xytext=(2, -1),
                arrowprops=dict(arrowstyle="<->", color=ec.CORES["destaque"], lw=1.3))

    ec.legenda(ax, local="upper right")
    ec.salvar(fig, UNIDADE, "2.2-laterais-com-salto")


def modulo_sobre_x() -> None:
    """y = |x|/x: vale -1 à esquerda e +1 à direita."""
    fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-2, 2), figsize=(5.6, 3.2), passo_y=1)

    ax.plot([-3, 0], [-1, -1], color=ec.CORES["curva"], linewidth=2.2, zorder=3)
    ax.plot([0, 3], [1, 1], color=ec.CORES["curva2"], linewidth=2.2, zorder=3)
    ec.ponto_aberto(ax, 0, -1, cor=ec.CORES["curva"])
    ec.ponto_aberto(ax, 0, 1, cor=ec.CORES["curva2"])

    ax.annotate(r"$-1$", xy=(-2.2, -1), xytext=(0, 10), textcoords="offset points",
                color=ec.CORES["curva"], fontsize=11)
    ax.annotate(r"$+1$", xy=(2.0, 1), xytext=(0, -22), textcoords="offset points",
                color=ec.CORES["curva2"], fontsize=11)

    ec.salvar(fig, UNIDADE, "2.2-modulo-sobre-x")


def maior_inteiro() -> None:
    """A função maior inteiro: um salto em cada número inteiro."""
    fig, ax = ec.novo_plano(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2), figsize=(5.6, 4.0),
                            aspecto_igual=True)

    for k in range(-3, 3):
        ax.plot([k, k + 1], [k, k], color=ec.CORES["curva"], linewidth=2.2, zorder=3)
        ec.ponto_fechado(ax, k, k, cor=ec.CORES["curva"], tamanho=6)
        ec.ponto_aberto(ax, k + 1, k, cor=ec.CORES["curva"], tamanho=6)

    ec.salvar(fig, UNIDADE, "2.2-maior-inteiro")


def raiz_lateral() -> None:
    """Em x = 0 só existe o limite pela direita: à esquerda a função nem existe."""
    fig, ax = ec.novo_plano(xlim=(-2, 4), ylim=(-1, 2.6), figsize=(5.8, 3.4))

    ec.plotar(ax, np.sqrt, (0, 4), rotulo=r"$y=\sqrt{x}$")
    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["curva"], tamanho=6)

    ax.annotate("aqui a função\nnão existe", xy=(-1.0, 0.1), xytext=(-1.95, 1.3),
                color=ec.CORES["destaque"], fontsize=9)
    ax.annotate("", xy=(-0.1, 0.06), xytext=(-1.0, 1.15),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["destaque"], lw=1.3))

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.2-raiz-lateral")


# ======================================================================================
# 2.3 — Teorema do Confronto
# ======================================================================================

def confronto() -> None:
    """A ideia do confronto: f espremida entre g e h, que se encontram em L."""
    fig, ax = ec.novo_plano(xlim=(-1.2, 3.2), ylim=(-0.6, 3.4), figsize=(6.4, 4.4))

    g = lambda x: 2 - 0.5 * (x - 1) ** 2
    h = lambda x: 2 + 0.5 * (x - 1) ** 2
    f = lambda x: 2 + 0.35 * (x - 1) ** 2 * np.sin(6 * (x - 1))

    ec.plotar(ax, h, (-1.0, 3.0), cor=ec.CORES["curva2"], rotulo="$h(x)$")
    ec.plotar(ax, g, (-1.0, 3.0), cor=ec.CORES["curva3"], rotulo="$g(x)$")
    ec.plotar(ax, f, (-1.0, 3.0), cor=ec.CORES["curva"], rotulo="$f(x)$", largura=2.6)

    ec.ponto_fechado(ax, 1, 2, cor=ec.CORES["destaque"], tamanho=7)
    ec.linha_guia(ax, x=1)
    ax.annotate("$L$", xy=(1, 2), xytext=(-14, 8), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=12)
    ax.annotate("$a$", xy=(1, 0), xytext=(0, -20), textcoords="offset points",
                ha="center", color=ec.CORES["destaque"], fontsize=12)
    ax.annotate("as duas pontas se encontram:\n$f$ não tem para onde fugir",
                xy=(1, 2), xytext=(1.35, 0.35), color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "2.3-confronto")


def x2_sen_um_sobre_x() -> None:
    """x^2 sen(1/x) espremida entre -x^2 e x^2."""
    fig, ax = ec.novo_plano(xlim=(-0.55, 0.55), ylim=(-0.3, 0.3), figsize=(6.2, 4.0),
                            passo_x=None, passo_y=None)
    ax.set_xticks([-0.4, -0.2, 0.2, 0.4])
    ax.set_xticklabels(["-0,4", "-0,2", "0,2", "0,4"])
    ax.set_yticks([-0.2, -0.1, 0.1, 0.2])
    ax.set_yticklabels(["-0,2", "-0,1", "0,1", "0,2"])

    ec.plotar(ax, lambda x: x**2, (-0.55, 0.55), cor=ec.CORES["curva2"],
              rotulo="$y=x^2$")
    ec.plotar(ax, lambda x: -x**2, (-0.55, 0.55), cor=ec.CORES["curva3"],
              rotulo="$y=-x^2$")

    for trecho in [(-0.55, -0.0008), (0.0008, 0.55)]:
        x = np.linspace(*trecho, 9000)
        ax.plot(x, x**2 * np.sin(1 / x), color=ec.CORES["curva"], linewidth=1.3,
                zorder=4,
                label=r"$y=x^2\,\mathrm{sen}\,\frac{1}{x}$" if trecho[0] > 0 else None)

    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["destaque"], tamanho=6)
    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "2.3-x2-sen-um-sobre-x")


def circulo_trigonometrico() -> None:
    """A construção geométrica que prova sen(x)/x -> 1."""
    fig, ax = ec.novo_plano(xlim=(-0.35, 1.9), ylim=(-0.35, 1.5), figsize=(6.0, 4.4),
                            aspecto_igual=True, passo_x=None, passo_y=None)
    ax.set_xticks([1])
    ax.set_yticks([1])
    ax.grid(False)

    t = np.linspace(0, np.pi / 2.2, 300)
    ax.plot(np.cos(t), np.sin(t), color=ec.CORES["tracejado"], linewidth=1.4, zorder=2)

    ang = 0.9
    P = (np.cos(ang), np.sin(ang))
    T = (1.0, np.tan(ang))

    # Setor circular (área x/2).
    ts = np.linspace(0, ang, 120)
    ax.fill(np.concatenate([[0], np.cos(ts), [0]]),
            np.concatenate([[0], np.sin(ts), [0]]),
            color=ec.CORES["curva3"], alpha=0.22, zorder=1)

    # Triângulo menor OAP (área sen x / 2) e maior OAT (área tg x / 2).
    ax.plot([0, 1, P[0], 0], [0, 0, P[1], 0], color=ec.CORES["curva"], linewidth=2.0,
            zorder=3)
    ax.plot([0, 1, T[0], 0], [0, 0, T[1], 0], color=ec.CORES["curva2"], linewidth=2.0,
            zorder=3)
    ax.plot([1, 1], [0, T[1]], color=ec.CORES["curva2"], linewidth=2.0, zorder=3)
    ax.plot([P[0], P[0]], [0, P[1]], color=ec.CORES["curva"], linestyle=":",
            linewidth=1.4, zorder=3)

    ec.ponto_fechado(ax, 1, 0, cor=ec.CORES["eixo"], tamanho=5)
    ec.ponto_fechado(ax, *P, cor=ec.CORES["curva"], tamanho=5)
    ec.ponto_fechado(ax, *T, cor=ec.CORES["curva2"], tamanho=5)

    ax.annotate("$O$", xy=(0, 0), xytext=(-16, -14), textcoords="offset points",
                fontsize=11)
    ax.annotate("$A$", xy=(1, 0), xytext=(10, -16), textcoords="offset points",
                fontsize=11)
    ax.annotate("$P$", xy=P, xytext=(-16, 6), textcoords="offset points",
                color=ec.CORES["curva"], fontsize=11)
    ax.annotate("$T$", xy=T, xytext=(6, 2), textcoords="offset points",
                color=ec.CORES["curva2"], fontsize=11)
    ax.annotate(r"$\mathrm{sen}\,x$", xy=(P[0], P[1] / 2), xytext=(-58, -4),
                textcoords="offset points", color=ec.CORES["curva"], fontsize=10)
    ax.annotate(r"$\mathrm{tg}\,x$", xy=(1, T[1] / 2), xytext=(8, -4),
                textcoords="offset points", color=ec.CORES["curva2"], fontsize=10)
    ax.annotate("$x$", xy=(0.22, 0.09), color=ec.CORES["curva3"], fontsize=11)

    ec.salvar(fig, UNIDADE, "2.3-circulo-trigonometrico")


def sen_x_sobre_x() -> None:
    """O gráfico de sen(x)/x, com o furo em x = 0."""
    fig, ax = ec.novo_plano(xlim=(-3 * np.pi, 3 * np.pi), ylim=(-0.5, 1.4),
                            figsize=(7.0, 3.4), passo_x=None, passo_y=None)
    marcas = [-2 * np.pi, -np.pi, np.pi, 2 * np.pi]
    ax.set_xticks(marcas)
    ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", r"$\pi$", r"$2\pi$"])
    ax.set_yticks([0.5, 1])
    ax.set_yticklabels(["0,5", "1"])

    for trecho in [(-3 * np.pi, -0.01), (0.01, 3 * np.pi)]:
        ec.plotar(ax, lambda x: np.sin(x) / x, trecho, cor=ec.CORES["curva"],
                  rotulo=r"$y=\frac{\mathrm{sen}\,x}{x}$" if trecho[0] > 0 else None)
    ec.ponto_aberto(ax, 0, 1, cor=ec.CORES["curva"])
    ec.linha_guia(ax, y=1)

    ax.annotate("o limite é 1,\nmas a função\nnão existe em 0", xy=(0, 1),
                xytext=(1.2, 0.35), color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.3-sen-x-sobre-x")


# ======================================================================================
# 2.4 — Limites infinitos, limites no infinito e assíntotas
# ======================================================================================

def assintota_vertical_fig() -> None:
    """1/(x-2): os dois lados fogem para infinitos de sinais opostos."""
    fig, ax = ec.novo_plano(xlim=(-1.5, 5.5), ylim=(-6, 6), figsize=(6.2, 4.6),
                            passo_y=2)

    for trecho in [(-1.5, 1.83), (2.17, 5.5)]:
        ec.plotar(ax, lambda x: 1 / (x - 2), trecho, cor=ec.CORES["curva"],
                  rotulo=r"$y=\frac{1}{x-2}$" if trecho[0] > 0 else None)
    ec.assintota_vertical(ax, 2)
    ec.assintota_horizontal(ax, 0)

    ax.annotate(r"$x \to 2^-$:  $-\infty$", xy=(2, -4), xytext=(-1.4, -4.6),
                color=ec.CORES["destaque"], fontsize=10)
    ax.annotate(r"$x \to 2^+$:  $+\infty$", xy=(2, 4), xytext=(2.5, 4.6),
                color=ec.CORES["destaque"], fontsize=10)
    ax.annotate(r"$x=2$", xy=(2, 0), xytext=(-34, -26), textcoords="offset points",
                color=ec.CORES["tracejado"], fontsize=10)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "2.4-assintota-vertical")


def assintota_horizontal_fig() -> None:
    """(3x^2+1)/(x^2+2): a curva se aproxima da reta y = 3 nos dois extremos."""
    fig, ax = ec.novo_plano(xlim=(-9, 9), ylim=(-0.8, 4.2), figsize=(6.6, 3.8),
                            passo_x=2, passo_y=1)

    ec.plotar(ax, lambda x: (3 * x**2 + 1) / (x**2 + 2), (-9, 9),
              rotulo=r"$y=\frac{3x^2+1}{x^2+2}$")
    ec.assintota_horizontal(ax, 3, rotulo="$y=3$")

    ax.annotate("quando $x$ cresce, a curva\ngruda na reta $y=3$", xy=(7, 2.9),
                xytext=(1.2, 1.1), color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.4-assintota-horizontal")


def raiz_no_infinito() -> None:
    """sqrt(x^2+1)/x: tende a 1 à direita e a -1 à esquerda."""
    fig, ax = ec.novo_plano(xlim=(-9, 9), ylim=(-2.2, 2.2), figsize=(6.6, 3.6),
                            passo_x=2, passo_y=1)

    f = lambda x: np.sqrt(x**2 + 1) / x
    for trecho in [(-9, -0.35), (0.35, 9)]:
        ec.plotar(ax, f, trecho, cor=ec.CORES["curva"],
                  rotulo=r"$y=\frac{\sqrt{x^2+1}}{x}$" if trecho[0] > 0 else None)

    ec.assintota_horizontal(ax, 1, rotulo="$y=1$")
    ec.assintota_horizontal(ax, -1, rotulo="$y=-1$")

    ax.annotate("duas assíntotas horizontais:\no sinal muda porque\n"
                r"$\sqrt{x^2}=|x|$", xy=(-6, -1), xytext=(-8.6, 0.8),
                va="top", color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.4-raiz-no-infinito")


def assintota_obliqua() -> None:
    """(x^2+1)/x = x + 1/x: a curva se aproxima da reta y = x."""
    fig, ax = ec.novo_plano(xlim=(-6, 6), ylim=(-7, 7), figsize=(5.8, 4.8),
                            passo_y=2)

    for trecho in [(-6, -0.17), (0.17, 6)]:
        ec.plotar(ax, lambda x: (x**2 + 1) / x, trecho, cor=ec.CORES["curva"],
                  rotulo=r"$y=\frac{x^2+1}{x}$" if trecho[0] > 0 else None)

    ax.plot([-6, 6], [-6, 6], color=ec.CORES["tracejado"], linestyle="--",
            linewidth=1.4, zorder=2)
    ax.annotate("$y=x$", xy=(4.4, 4.4), xytext=(8, -14), textcoords="offset points",
                color=ec.CORES["tracejado"], fontsize=10)
    ec.assintota_vertical(ax, 0)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.4-assintota-obliqua")


# ======================================================================================
# 2.5 — Continuidade e tipos de descontinuidade
# ======================================================================================

def _plano_descontinuidade(titulo: str):
    return ec.novo_plano(xlim=(-0.6, 3.6), ylim=(-1.2, 4.2), figsize=(3.6, 3.2),
                         titulo=titulo, passo_x=1, passo_y=1)


def descontinuidade_removivel() -> None:
    """Furo: o limite existe, mas não é o valor (ou o valor não existe)."""
    fig, ax = _plano_descontinuidade("removível")
    ec.plotar(ax, lambda x: x + 1, (-0.6, 3.6))
    ec.ponto_aberto(ax, 1, 2, cor=ec.CORES["curva"])
    ec.ponto_fechado(ax, 1, 3.4, cor=ec.CORES["destaque"])
    ec.salvar(fig, UNIDADE, "2.5-descontinuidade-removivel")


def descontinuidade_salto() -> None:
    """Salto: os laterais existem e discordam."""
    fig, ax = _plano_descontinuidade("de salto")
    ec.plotar(ax, lambda x: x + 1, (-0.6, 1.5), cor=ec.CORES["curva"])
    ec.plotar(ax, lambda x: x - 0.5, (1.5, 3.6), cor=ec.CORES["curva2"])
    ec.ponto_aberto(ax, 1.5, 2.5, cor=ec.CORES["curva"])
    ec.ponto_fechado(ax, 1.5, 1.0, cor=ec.CORES["curva2"])
    ec.salvar(fig, UNIDADE, "2.5-descontinuidade-salto")


def descontinuidade_infinita() -> None:
    """Infinita: pelo menos um lateral explode."""
    fig, ax = _plano_descontinuidade("infinita")
    for trecho in [(-0.6, 1.25), (1.75, 3.6)]:
        ec.plotar(ax, lambda x: 1 / (x - 1.5) + 1.5, trecho, cor=ec.CORES["curva"])
    ec.assintota_vertical(ax, 1.5)
    ec.salvar(fig, UNIDADE, "2.5-descontinuidade-infinita")


def teorema_valor_intermediario() -> None:
    """O TVI: função contínua assume todo valor entre f(a) e f(b)."""
    fig, ax = ec.novo_plano(xlim=(-0.5, 6), ylim=(-3.5, 5), figsize=(6.4, 4.4),
                            passo_y=1)

    f = lambda x: 0.35 * (x - 1) ** 3 - 1.6 * (x - 1) + 0.4 * (x - 1) ** 2 - 2
    a, b = 1.0, 5.0
    N = 1.0

    ec.plotar(ax, f, (a, b), rotulo="$f$ contínua em $[a,b]$")
    ec.assintota_horizontal(ax, N, rotulo="$y=N$")

    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["destaque"], tamanho=7)
    ec.ponto_fechado(ax, b, f(b), cor=ec.CORES["destaque"], tamanho=7)

    # Localiza numericamente um c com f(c) = N.
    xs = np.linspace(a, b, 4000)
    ys = f(xs)
    c = xs[np.argmin(np.abs(ys - N))]
    ec.ponto_fechado(ax, c, N, cor=ec.CORES["curva2"], tamanho=7)
    ec.linha_guia(ax, x=c)

    ax.annotate("$a$", xy=(a, 0), xytext=(-4, -22), textcoords="offset points",
                fontsize=11)
    ax.annotate("$b$", xy=(b, 0), xytext=(-4, -22), textcoords="offset points",
                fontsize=11)
    ax.annotate("$c$", xy=(c, 0), xytext=(-4, -22), textcoords="offset points",
                color=ec.CORES["curva2"], fontsize=11)
    ax.annotate("$f(a)$", xy=(a, f(a)), xytext=(6, -14), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=10)
    ax.annotate("$f(b)$", xy=(b, f(b)), xytext=(-40, 4), textcoords="offset points",
                color=ec.CORES["destaque"], fontsize=10)
    ax.annotate("existe $c$ com $f(c)=N$", xy=(c, N), xytext=(c + 0.25, 2.9),
                color=ec.CORES["curva2"], fontsize=9)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "2.5-teorema-do-valor-intermediario")


# ======================================================================================

FIGURAS = [
    ideia_de_limite,
    laterais_iguais,
    laterais_com_salto,
    modulo_sobre_x,
    maior_inteiro,
    raiz_lateral,
    confronto,
    x2_sen_um_sobre_x,
    circulo_trigonometrico,
    sen_x_sobre_x,
    assintota_vertical_fig,
    assintota_horizontal_fig,
    raiz_no_infinito,
    assintota_obliqua,
    descontinuidade_removivel,
    descontinuidade_salto,
    descontinuidade_infinita,
    teorema_valor_intermediario,
    valor_nao_importa_a,
    valor_nao_importa_b,
    valor_nao_importa_c,
    nao_existe_salto,
    nao_existe_oscilacao,
    nao_existe_infinito,
    epsilon_delta,
]


def main() -> None:
    ec.configurar()
    print("Gerando as figuras da Unidade 2...")
    for figura in FIGURAS:
        figura()
    print(f"Pronto: {len(FIGURAS)} figuras.")


if __name__ == "__main__":
    main()
