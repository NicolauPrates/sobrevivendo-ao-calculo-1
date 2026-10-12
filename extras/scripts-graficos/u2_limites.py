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

FIGURAS = [
    ideia_de_limite,
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
