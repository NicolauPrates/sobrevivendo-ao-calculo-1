"""
Gráficos da Unidade 1 — Funções reais de uma variável real.

Rode a partir desta pasta:

    python u1_funcoes.py

As figuras são gravadas em assets/img/01-funcoes/.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import numpy as np

import estilo_calculo as ec

UNIDADE = "01-funcoes"


# ======================================================================================
# 1.1 — Números reais, intervalos, valor absoluto e desigualdades
# ======================================================================================

def reta_real() -> None:
    """A reta real com alguns números notáveis localizados."""
    fig, ax = ec.nova_reta_real(xlim=(-4, 4), figsize=(7.2, 1.9))

    pontos = [
        (-3.0, "$-3$", ec.CORES["curva"]),
        (-5 / 2, r"$-\frac{5}{2}$", ec.CORES["curva"]),
        (np.sqrt(2), r"$\sqrt{2}$", ec.CORES["destaque"]),
        (np.pi, r"$\pi$", ec.CORES["destaque"]),
    ]
    for x, rotulo, cor in pontos:
        ec.ponto_fechado(ax, x, 0, cor=cor, tamanho=7)
        ax.annotate(rotulo, xy=(x, 0), xytext=(0, 14), textcoords="offset points",
                    ha="center", color=cor, fontsize=12)

    ax.annotate("racionais", xy=(-2.75, 0), xytext=(-2.75, -0.85), ha="center",
                color=ec.CORES["curva"], fontsize=10)
    ax.annotate("irracionais", xy=(2.3, 0), xytext=(2.3, -0.85), ha="center",
                color=ec.CORES["destaque"], fontsize=10)

    ec.salvar(fig, UNIDADE, "1.1-reta-real")


def tipos_de_intervalo() -> None:
    """Os quatro tipos de intervalo, com a = -2 e b = 3."""
    a, b = -2, 3
    rotulos = [
        r"$[a,\,b]$   fechado",
        r"$(a,\,b)$   aberto",
        r"$[a,\,b)$   semiaberto",
        r"$(-\infty,\,b]$   ilimitado",
    ]
    fig, eixos = ec.novo_painel_retas(rotulos, xlim=(-5, 5), altura_linha=1.05)

    ec.intervalo(eixos[0], a, b, fechado_a=True, fechado_b=True)
    ec.intervalo(eixos[1], a, b, fechado_a=False, fechado_b=False)
    ec.intervalo(eixos[2], a, b, fechado_a=True, fechado_b=False)
    ec.intervalo(eixos[3], -np.inf, b, fechado_b=True)

    # Aqui a e b são genéricos: os valores numéricos dos eixos só atrapalhariam.
    for i, ax in enumerate(eixos):
        ax.set_xticklabels([])
        if i < 3:
            ax.annotate("$a$", xy=(a, 0), xytext=(0, -20), textcoords="offset points",
                        ha="center", fontsize=12)
        ax.annotate("$b$", xy=(b, 0), xytext=(0, -20), textcoords="offset points",
                    ha="center", fontsize=12)

    ec.salvar(fig, UNIDADE, "1.1-tipos-de-intervalo")


def solucao_quociente() -> None:
    """Conjunto-solução de (x-1)/(x+2) >= 0."""
    fig, ax = ec.nova_reta_real(xlim=(-5, 4), figsize=(7.2, 1.9))

    ec.intervalo(ax, -np.inf, -2, fechado_b=False)
    ec.intervalo(ax, 1, np.inf, fechado_a=True)

    ax.annotate("excluído", xy=(-2, 0), xytext=(0, -34), textcoords="offset points",
                ha="center", fontsize=9, color=ec.CORES["destaque"])
    ax.annotate("incluído", xy=(1, 0), xytext=(0, -34), textcoords="offset points",
                ha="center", fontsize=9, color=ec.CORES["destaque"])
    ax.annotate(r"$(-\infty,\,-2)\ \cup\ [1,\,+\infty)$", xy=(0, 0), xytext=(-0.5, 0.55),
                ha="center", color=ec.CORES["destaque"], fontsize=12)

    ec.salvar(fig, UNIDADE, "1.1-solucao-quociente")


def modulo_como_distancia() -> None:
    """|x - 3| < 2 lido como distância: todos os pontos a menos de 2 unidades de 3."""
    fig, ax = ec.nova_reta_real(xlim=(-1, 7), figsize=(7.2, 2.1))

    ec.intervalo(ax, 1, 5, fechado_a=False, fechado_b=False)
    ec.ponto_fechado(ax, 3, 0, cor=ec.CORES["curva"], tamanho=8)

    ax.annotate("centro", xy=(3, 0), xytext=(0, -34), textcoords="offset points",
                ha="center", color=ec.CORES["curva"], fontsize=10)

    # Setas indicando o raio 2 para cada lado.
    for x0, x1, meio in [(3, 1, 2), (3, 5, 4)]:
        ax.annotate("", xy=(x1, 0.42), xytext=(x0, 0.42),
                    arrowprops=dict(arrowstyle="->", color=ec.CORES["auxiliar"],
                                    linewidth=1.3))
        ax.annotate("$2$", xy=(meio, 0.5), ha="center", color=ec.CORES["auxiliar"],
                    fontsize=11)

    ec.salvar(fig, UNIDADE, "1.1-modulo-como-distancia")


def modulo_grafico() -> None:
    """A mesma inequação |x - 3| < 2 vista no gráfico de y = |x - 3|."""
    fig, ax = ec.novo_plano(xlim=(-1, 7), ylim=(-1, 5), figsize=(6.6, 4.4))

    # Nos rótulos use "|", e não \lvert: o mathtext do matplotlib não conhece esse comando.
    ec.plotar(ax, lambda x: np.abs(x - 3), (-1, 7), rotulo="$y = |x-3|$")
    ax.axhline(2, color=ec.CORES["curva2"], linewidth=2.0, zorder=3)
    ax.annotate("$y = 2$", xy=(6.1, 2), xytext=(0, 8), textcoords="offset points",
                color=ec.CORES["curva2"], fontsize=11)

    ec.linha_guia(ax, x=1)
    ec.linha_guia(ax, x=5)
    ec.intervalo(ax, 1, 5, fechado_a=False, fechado_b=False, altura=0)

    ax.annotate("o gráfico fica abaixo da reta\nexatamente para $1 < x < 5$",
                xy=(3, 0.05), xytext=(3, -0.95), ha="center",
                color=ec.CORES["destaque"], fontsize=10)

    ec.legenda(ax, local="upper center")
    ec.salvar(fig, UNIDADE, "1.1-modulo-grafico-inequacao")


# ======================================================================================
# 1.2 — Funções: domínio, contradomínio e imagem
# ======================================================================================

def teste_reta_vertical_sim() -> None:
    """Uma parábola passa no teste da reta vertical: é função."""
    fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-1, 6), figsize=(4.6, 3.8),
                            titulo="é função")

    ec.plotar(ax, lambda x: x**2, (-2.45, 2.45))
    for x0 in (-1.5, 0.8):
        ax.axvline(x0, color=ec.CORES["destaque"], linestyle="--", linewidth=1.4,
                   zorder=2)
        ec.ponto_fechado(ax, x0, x0**2, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("cada reta vertical\ncorta uma vez só", xy=(0.8, 0.64),
                xytext=(-2.9, 4.6), color=ec.CORES["destaque"], fontsize=9)

    ec.salvar(fig, UNIDADE, "1.2-teste-reta-vertical-sim")


def teste_reta_vertical_nao() -> None:
    """A circunferência falha no teste: não é função."""
    fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-3.2, 3.2), figsize=(4.6, 3.8),
                            titulo="não é função", aspecto_igual=True)

    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(2.5 * np.cos(t), 2.5 * np.sin(t), color=ec.CORES["curva"],
            linewidth=2.2, zorder=3)

    x0 = 1.2
    y0 = np.sqrt(2.5**2 - x0**2)
    ax.axvline(x0, color=ec.CORES["destaque"], linestyle="--", linewidth=1.4, zorder=2)
    ec.ponto_fechado(ax, x0, y0, cor=ec.CORES["destaque"], tamanho=6)
    ec.ponto_fechado(ax, x0, -y0, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("dois valores de $y$\npara o mesmo $x$", xy=(x0, y0),
                xytext=(-2.9, 2.6), color=ec.CORES["destaque"], fontsize=9)

    ec.salvar(fig, UNIDADE, "1.2-teste-reta-vertical-nao")


def dominio_e_imagem() -> None:
    """Domínio no eixo x, imagem no eixo y, para f(x) = raiz de (4 - x^2)."""
    fig, ax = ec.novo_plano(xlim=(-3.4, 3.4), ylim=(-1.2, 3.2), figsize=(6.6, 4.0),
                            aspecto_igual=True)

    f = lambda x: np.sqrt(np.clip(4 - x**2, 0, None))
    ec.plotar(ax, f, (-2, 2), rotulo=r"$f(x)=\sqrt{4-x^2}$")

    # Domínio sobre o eixo x; imagem sobre o eixo y.
    ax.plot([-2, 2], [0, 0], color=ec.CORES["curva2"], linewidth=5,
            solid_capstyle="butt", zorder=4)
    ax.plot([0, 0], [0, 2], color=ec.CORES["curva3"], linewidth=5,
            solid_capstyle="butt", zorder=4)

    ax.annotate(r"domínio $[-2,2]$", xy=(0, 0), xytext=(-1.0, -0.85),
                color=ec.CORES["curva2"], fontsize=11)
    ax.annotate(r"imagem" "\n" r"$[0,2]$", xy=(0, 1), xytext=(0.22, 1.9),
                color=ec.CORES["curva3"], fontsize=11)

    ec.linha_guia(ax, x=-2)
    ec.linha_guia(ax, x=2)
    ec.legenda(ax, local="upper right")
    ec.salvar(fig, UNIDADE, "1.2-dominio-e-imagem")


def funcao_por_partes() -> None:
    """Gráfico da função definida por partes usada nos exemplos de 1.2."""
    fig, ax = ec.novo_plano(xlim=(-4.5, 5.5), ylim=(-2.5, 5.5), figsize=(6.8, 4.6))

    ec.plotar(ax, lambda x: x + 3, (-4.5, -1), rotulo="$x+3$")
    ec.plotar(ax, lambda x: x**2, (-1, 2), cor=ec.CORES["curva2"], rotulo="$x^2$")
    ec.plotar(ax, lambda x: 5 - x, (2, 5.5), cor=ec.CORES["curva3"], rotulo="$5-x$")

    ec.ponto_aberto(ax, -1, 2, cor=ec.CORES["curva"])
    ec.ponto_fechado(ax, -1, 1, cor=ec.CORES["curva2"])
    ec.ponto_fechado(ax, 2, 4, cor=ec.CORES["curva2"])
    ec.ponto_aberto(ax, 2, 3, cor=ec.CORES["curva3"])

    ax.annotate("salto em $x=-1$", xy=(-1, 1.5), xytext=(-4.4, 3.4),
                color=ec.CORES["destaque"], fontsize=9)
    ax.annotate("salto em $x=2$", xy=(2, 3.5), xytext=(2.9, 4.6),
                color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower left")
    ec.salvar(fig, UNIDADE, "1.2-funcao-por-partes")


# ======================================================================================
# 1.3 — Funções elementares, paridade e gráficos
# ======================================================================================

def potencias() -> None:
    """As quatro primeiras potências de x no mesmo plano."""
    fig, ax = ec.novo_plano(xlim=(-2.2, 2.2), ylim=(-3, 4.2), figsize=(6.2, 4.6),
                            passo_y=1)

    ec.plotar(ax, lambda x: x, (-2.2, 2.2), cor=ec.CORES["curva"], rotulo="$y=x$")
    ec.plotar(ax, lambda x: x**2, (-2.05, 2.05), cor=ec.CORES["curva2"],
              rotulo="$y=x^2$")
    ec.plotar(ax, lambda x: x**3, (-1.5, 1.6), cor=ec.CORES["curva3"],
              rotulo="$y=x^3$")
    ec.plotar(ax, lambda x: x**4, (-1.44, 1.44), cor=ec.CORES["auxiliar"],
              rotulo="$y=x^4$")

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "1.3-potencias")


def raizes() -> None:
    """Raiz quadrada e raiz cúbica."""
    fig, ax = ec.novo_plano(xlim=(-4.5, 4.5), ylim=(-2.5, 2.5), figsize=(6.4, 3.8))

    ec.plotar(ax, np.sqrt, (0, 4.5), cor=ec.CORES["curva"], rotulo=r"$y=\sqrt{x}$")
    ec.plotar(ax, lambda x: np.cbrt(x), (-4.5, 4.5), cor=ec.CORES["curva2"],
              rotulo=r"$y=\sqrt[3]{x}$")
    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["curva"], tamanho=6)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "1.3-raizes")


def racionais() -> None:
    """As hipérboles 1/x e 1/x^2, com as assíntotas."""
    fig, ax = ec.novo_plano(xlim=(-4, 4), ylim=(-4, 4), figsize=(6.0, 4.6),
                            aspecto_igual=True)

    for trecho in [(-4, -0.26), (0.26, 4)]:
        ec.plotar(ax, lambda x: 1 / x, trecho, cor=ec.CORES["curva"],
                  rotulo="$y=1/x$" if trecho[0] > 0 else None)
    for trecho in [(-4, -0.51), (0.51, 4)]:
        ec.plotar(ax, lambda x: 1 / x**2, trecho, cor=ec.CORES["curva2"],
                  rotulo="$y=1/x^2$" if trecho[0] > 0 else None)

    ec.legenda(ax, local="lower left")
    ec.salvar(fig, UNIDADE, "1.3-racionais")


def modular() -> None:
    """A função modular."""
    fig, ax = ec.novo_plano(xlim=(-4, 4), ylim=(-1.5, 4), figsize=(5.6, 3.6))
    ec.plotar(ax, np.abs, (-4, 4), rotulo="$y=|x|$")
    ec.anotar(ax, "bico em $x=0$:\nnão há reta tangente", xy=(0, 0), xytext=(0.5, 2.4),
              fontsize=9)
    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "1.3-modular")


def exp_e_log() -> None:
    """Exponencial e logaritmo natural, simétricos em relação à reta y = x."""
    fig, ax = ec.novo_plano(xlim=(-3, 6), ylim=(-3, 6), figsize=(5.8, 5.2),
                            aspecto_igual=True)

    ec.plotar(ax, np.exp, (-3, 1.8), cor=ec.CORES["curva"], rotulo="$y=e^x$")
    ec.plotar(ax, np.log, (0.02, 6), cor=ec.CORES["curva2"], rotulo=r"$y=\ln x$")
    ax.plot([-3, 6], [-3, 6], color=ec.CORES["tracejado"], linestyle="--",
            linewidth=1.3, zorder=2)
    ax.annotate("$y=x$", xy=(4.4, 4.4), xytext=(6, -10), textcoords="offset points",
                color=ec.CORES["tracejado"], fontsize=10)

    ec.ponto_fechado(ax, 0, 1, cor=ec.CORES["curva"], tamanho=6)
    ec.ponto_fechado(ax, 1, 0, cor=ec.CORES["curva2"], tamanho=6)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "1.3-exp-e-log")


def _eixo_em_pi(ax, de=-2, ate=2) -> None:
    """Marca o eixo x em múltiplos de pi/2, com rótulos em LaTeX."""
    marcas, rotulos = [], []
    nomes = {-2: r"$-2\pi$", -1.5: r"$-\frac{3\pi}{2}$", -1: r"$-\pi$",
             -0.5: r"$-\frac{\pi}{2}$", 0.5: r"$\frac{\pi}{2}$", 1: r"$\pi$",
             1.5: r"$\frac{3\pi}{2}$", 2: r"$2\pi$"}
    k = de
    while k <= ate + 1e-9:
        if abs(k) > 1e-9 and k in nomes:
            marcas.append(k * np.pi)
            rotulos.append(nomes[k])
        k += 0.5
    ax.set_xticks(marcas)
    ax.set_xticklabels(rotulos)


def seno_e_cosseno() -> None:
    """Seno e cosseno em um período completo de cada lado."""
    fig, ax = ec.novo_plano(xlim=(-2 * np.pi - 0.4, 2 * np.pi + 0.4), ylim=(-1.8, 1.8),
                            figsize=(7.4, 3.6), passo_x=None, passo_y=1)
    _eixo_em_pi(ax)

    ec.plotar(ax, np.sin, (-2 * np.pi, 2 * np.pi), cor=ec.CORES["curva"],
              rotulo=r"$y=\mathrm{sen}\,x$")
    ec.plotar(ax, np.cos, (-2 * np.pi, 2 * np.pi), cor=ec.CORES["curva2"],
              rotulo=r"$y=\cos x$")

    ec.legenda(ax, local="upper right")
    ec.salvar(fig, UNIDADE, "1.3-seno-e-cosseno")


def tangente() -> None:
    """A tangente e suas assíntotas verticais."""
    fig, ax = ec.novo_plano(xlim=(-2 * np.pi - 0.3, 2 * np.pi + 0.3), ylim=(-4, 4),
                            figsize=(7.4, 4.0), passo_x=None, passo_y=1)
    _eixo_em_pi(ax)

    for k in (-2, -1, 0, 1):
        centro = k * np.pi
        ec.plotar(ax, np.tan, (centro - np.pi / 2 + 0.12, centro + np.pi / 2 - 0.12),
                  cor=ec.CORES["curva"],
                  rotulo=r"$y=\mathrm{tg}\,x$" if k == 0 else None)
    for k in (-3, -1, 1, 3):
        ec.assintota_vertical(ax, k * np.pi / 2)

    ec.legenda(ax, local="upper right")
    ec.salvar(fig, UNIDADE, "1.3-tangente")


def translacoes() -> None:
    """Translações vertical e horizontal a partir de y = x^2."""
    fig, ax = ec.novo_plano(xlim=(-4, 6), ylim=(-1.5, 7), figsize=(6.4, 4.4))

    ec.plotar(ax, lambda x: x**2, (-2.7, 2.7), cor=ec.CORES["curva"],
              rotulo="$y=x^2$")
    ec.plotar(ax, lambda x: x**2 + 2, (-2.3, 2.3), cor=ec.CORES["curva2"],
              rotulo="$y=x^2+2$")
    ec.plotar(ax, lambda x: (x - 3) ** 2, (0.3, 5.7), cor=ec.CORES["curva3"],
              rotulo="$y=(x-3)^2$")

    ax.annotate("", xy=(0, 2), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["curva2"], lw=1.4))
    ax.annotate("sobe 2", xy=(0.1, 1.0), color=ec.CORES["curva2"], fontsize=9)
    ax.annotate("", xy=(3, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=ec.CORES["curva3"], lw=1.4))
    ax.annotate("anda 3 para a direita", xy=(0.5, -0.9), color=ec.CORES["curva3"],
                fontsize=9)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "1.3-translacoes")


def reflexoes() -> None:
    """Reflexões em relação aos dois eixos, a partir da raiz quadrada."""
    fig, ax = ec.novo_plano(xlim=(-4.5, 4.5), ylim=(-2.6, 2.6), figsize=(6.4, 3.8))

    ec.plotar(ax, np.sqrt, (0, 4.5), cor=ec.CORES["curva"], rotulo=r"$y=\sqrt{x}$")
    ec.plotar(ax, lambda x: -np.sqrt(x), (0, 4.5), cor=ec.CORES["curva2"],
              rotulo=r"$y=-\sqrt{x}$")
    ec.plotar(ax, lambda x: np.sqrt(-x), (-4.5, 0), cor=ec.CORES["curva3"],
              rotulo=r"$y=\sqrt{-x}$")

    ax.annotate("espelho no eixo $x$", xy=(3.2, -1.78), color=ec.CORES["curva2"],
                fontsize=9, ha="center")
    ax.annotate("espelho no eixo $y$", xy=(-3.2, 2.1), color=ec.CORES["curva3"],
                fontsize=9, ha="center")

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "1.3-reflexoes")


def dilatacoes() -> None:
    """Dilatação vertical e horizontal a partir do seno."""
    fig, ax = ec.novo_plano(xlim=(-0.6, 2 * np.pi + 0.4), ylim=(-2.6, 2.6),
                            figsize=(7.2, 3.6), passo_x=None, passo_y=1)
    _eixo_em_pi(ax, de=0.5, ate=2)

    ec.plotar(ax, np.sin, (0, 2 * np.pi), cor=ec.CORES["curva"],
              rotulo=r"$y=\mathrm{sen}\,x$")
    ec.plotar(ax, lambda x: 2 * np.sin(x), (0, 2 * np.pi), cor=ec.CORES["curva2"],
              rotulo=r"$y=2\,\mathrm{sen}\,x$")
    ec.plotar(ax, lambda x: np.sin(2 * x), (0, 2 * np.pi), cor=ec.CORES["curva3"],
              rotulo=r"$y=\mathrm{sen}\,2x$")

    ec.legenda(ax, local="upper right")
    ec.salvar(fig, UNIDADE, "1.3-dilatacoes")


def paridade_par() -> None:
    """Função par: simetria em relação ao eixo y."""
    fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-1.5, 5), figsize=(4.6, 3.6),
                            titulo="par: $f(-x) = f(x)$")

    f = lambda x: x**4 - 3 * x**2 + 2
    ec.plotar(ax, f, (-2.2, 2.2))
    for x0 in (1.6,):
        ec.ponto_fechado(ax, x0, f(x0), cor=ec.CORES["destaque"], tamanho=6)
        ec.ponto_fechado(ax, -x0, f(-x0), cor=ec.CORES["destaque"], tamanho=6)
        ax.plot([-x0, x0], [f(x0), f(x0)], color=ec.CORES["destaque"],
                linestyle=":", linewidth=1.2)
    ec.salvar(fig, UNIDADE, "1.3-paridade-par")


def paridade_impar() -> None:
    """Função ímpar: simetria em relação à origem."""
    fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-4, 4), figsize=(4.6, 3.6),
                            titulo="ímpar: $f(-x) = -f(x)$")

    f = lambda x: x**3 - 3 * x
    ec.plotar(ax, f, (-2.2, 2.2))
    x0 = 1.6
    ec.ponto_fechado(ax, x0, f(x0), cor=ec.CORES["destaque"], tamanho=6)
    ec.ponto_fechado(ax, -x0, f(-x0), cor=ec.CORES["destaque"], tamanho=6)
    ax.plot([-x0, x0], [f(-x0), f(x0)], color=ec.CORES["destaque"],
            linestyle=":", linewidth=1.2)
    ec.salvar(fig, UNIDADE, "1.3-paridade-impar")


# ======================================================================================
# 1.4 — Injetoras, sobrejetoras, bijetoras e inversas
# ======================================================================================

def reta_horizontal_sim() -> None:
    """x^3 passa no teste da reta horizontal: é injetora."""
    fig, ax = ec.novo_plano(xlim=(-2.4, 2.4), ylim=(-4.5, 4.5), figsize=(4.6, 3.8),
                            titulo="injetora")

    ec.plotar(ax, lambda x: x**3, (-1.62, 1.62))
    for y0 in (2.0, -2.0):
        ax.axhline(y0, color=ec.CORES["destaque"], linestyle="--", linewidth=1.4,
                   zorder=2)
        ec.ponto_fechado(ax, np.cbrt(y0), y0, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("toda horizontal\ncorta uma vez só", xy=(0, 0), xytext=(-2.3, 3.0),
                color=ec.CORES["destaque"], fontsize=9)

    ec.salvar(fig, UNIDADE, "1.4-reta-horizontal-sim")


def reta_horizontal_nao() -> None:
    """x^2 falha no teste da reta horizontal: não é injetora."""
    fig, ax = ec.novo_plano(xlim=(-2.4, 2.4), ylim=(-1, 5), figsize=(4.6, 3.8),
                            titulo="não é injetora")

    ec.plotar(ax, lambda x: x**2, (-2.2, 2.2))
    y0 = 2.25
    ax.axhline(y0, color=ec.CORES["destaque"], linestyle="--", linewidth=1.4, zorder=2)
    ec.ponto_fechado(ax, 1.5, y0, cor=ec.CORES["destaque"], tamanho=6)
    ec.ponto_fechado(ax, -1.5, y0, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("$f(-1{,}5) = f(1{,}5)$", xy=(0, y0), xytext=(-1.1, 3.4),
                color=ec.CORES["destaque"], fontsize=9)

    ec.salvar(fig, UNIDADE, "1.4-reta-horizontal-nao")


def inversa_reflexao() -> None:
    """f(x) = x^3 e sua inversa, simétricas em relação à reta y = x."""
    fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-3, 3), figsize=(5.2, 4.8),
                            aspecto_igual=True)

    ec.plotar(ax, lambda x: x**3, (-1.45, 1.45), cor=ec.CORES["curva"],
              rotulo="$y=x^3$")
    ec.plotar(ax, np.cbrt, (-3, 3), cor=ec.CORES["curva2"],
              rotulo=r"$y=\sqrt[3]{x}$")
    ax.plot([-3, 3], [-3, 3], color=ec.CORES["tracejado"], linestyle="--",
            linewidth=1.3, zorder=2)
    ax.annotate("$y=x$", xy=(2.3, 2.3), xytext=(4, -14), textcoords="offset points",
                color=ec.CORES["tracejado"], fontsize=10)

    # Um par de pontos simétricos, para mostrar a troca de coordenadas.
    ec.ponto_fechado(ax, 1.2, 1.728, cor=ec.CORES["destaque"], tamanho=6)
    ec.ponto_fechado(ax, 1.728, 1.2, cor=ec.CORES["destaque"], tamanho=6)
    ax.plot([1.2, 1.728], [1.728, 1.2], color=ec.CORES["destaque"], linestyle=":",
            linewidth=1.2, zorder=4)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "1.4-inversa-reflexao")


def restricao_do_seno() -> None:
    """O seno restrito a [-pi/2, pi/2] e o arco seno."""
    fig, ax = ec.novo_plano(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2), figsize=(5.2, 4.8),
                            aspecto_igual=True, passo_x=1, passo_y=1)

    ec.plotar(ax, np.sin, (-np.pi / 2, np.pi / 2), cor=ec.CORES["curva"],
              rotulo=r"$y=\mathrm{sen}\,x$,  $-\frac{\pi}{2}\leq x \leq \frac{\pi}{2}$")
    ec.plotar(ax, np.arcsin, (-1, 1), cor=ec.CORES["curva2"],
              rotulo=r"$y=\mathrm{arcsen}\,x$")
    ax.plot([-2.1, 2.1], [-2.1, 2.1], color=ec.CORES["tracejado"], linestyle="--",
            linewidth=1.3, zorder=2)

    for x0 in (-np.pi / 2, np.pi / 2):
        ec.ponto_fechado(ax, x0, np.sin(x0), cor=ec.CORES["curva"], tamanho=5)
    for x0 in (-1, 1):
        ec.ponto_fechado(ax, x0, np.arcsin(x0), cor=ec.CORES["curva2"], tamanho=5)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "1.4-restricao-do-seno")


# ======================================================================================

FIGURAS = [
    reta_real,
    tipos_de_intervalo,
    solucao_quociente,
    modulo_como_distancia,
    modulo_grafico,
    teste_reta_vertical_sim,
    teste_reta_vertical_nao,
    dominio_e_imagem,
    funcao_por_partes,
    potencias,
    raizes,
    racionais,
    modular,
    exp_e_log,
    seno_e_cosseno,
    tangente,
    translacoes,
    reflexoes,
    dilatacoes,
    paridade_par,
    paridade_impar,
    reta_horizontal_sim,
    reta_horizontal_nao,
    inversa_reflexao,
    restricao_do_seno,
]


def main() -> None:
    ec.configurar()
    print("Gerando as figuras da Unidade 1...")
    for figura in FIGURAS:
        figura()
    print(f"Pronto: {len(FIGURAS)} figuras.")


if __name__ == "__main__":
    main()
