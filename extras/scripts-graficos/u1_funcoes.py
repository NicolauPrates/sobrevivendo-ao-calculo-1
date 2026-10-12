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

FIGURAS = [
    reta_real,
    tipos_de_intervalo,
    solucao_quociente,
    modulo_como_distancia,
    modulo_grafico,
]


def main() -> None:
    ec.configurar()
    print("Gerando as figuras da Unidade 1...")
    for figura in FIGURAS:
        figura()
    print(f"Pronto: {len(FIGURAS)} figuras.")


if __name__ == "__main__":
    main()
