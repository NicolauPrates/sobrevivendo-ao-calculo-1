"""
Gráficos da Unidade 3 — Derivadas: conceito e regras.

Rode a partir desta pasta:

    python u3_derivadas.py

As figuras são gravadas em assets/img/03-derivadas/.

Autor: Nicolau Prates — CC BY-SA 4.0
"""

from __future__ import annotations

import numpy as np

import estilo_calculo as ec

UNIDADE = "03-derivadas"


# ======================================================================================
# 3.1 — Conceito, interpretação geométrica e regras básicas
# ======================================================================================

def secantes_para_tangente() -> None:
    """Retas secantes se aproximando da tangente conforme h diminui."""
    fig, ax = ec.novo_plano(xlim=(-0.6, 3.4), ylim=(-1.5, 7), figsize=(6.6, 4.8),
                            passo_y=1)

    f = lambda x: x**2
    a = 1.0

    ec.plotar(ax, f, (-0.6, 2.6), rotulo="$f(x)=x^2$")

    # Secantes para h cada vez menor.
    cores_h = [(1.4, 0.30), (0.9, 0.45), (0.45, 0.62)]
    for h, alpha in cores_h:
        m = (f(a + h) - f(a)) / h
        reta = lambda x, m=m: f(a) + m * (x - a)
        ax.plot([-0.6, 3.4], [reta(-0.6), reta(3.4)], color=ec.CORES["curva2"],
                linewidth=1.5, alpha=alpha, zorder=2)
        ec.ponto_fechado(ax, a + h, f(a + h), cor=ec.CORES["curva2"], tamanho=5)

    # Tangente (h -> 0): inclinação 2a.
    m_t = 2 * a
    ax.plot([-0.6, 3.4], [f(a) + m_t * (-0.6 - a), f(a) + m_t * (3.4 - a)],
            color=ec.CORES["destaque"], linewidth=2.2, zorder=4)
    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["destaque"], tamanho=7)

    ax.annotate("secantes", xy=(2.6, 4.6), color=ec.CORES["curva2"], fontsize=10)
    ax.annotate("tangente\n(limite das secantes)", xy=(2.3, 1.0),
                color=ec.CORES["destaque"], fontsize=10)
    ax.annotate("$a$", xy=(a, 0), xytext=(-4, -20), textcoords="offset points",
                fontsize=11)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "3.1-secantes-para-tangente")


def quociente_de_newton() -> None:
    """A figura que define o quociente: cateto horizontal h, cateto vertical a variação."""
    fig, ax = ec.novo_plano(xlim=(-0.4, 3.4), ylim=(-0.8, 6.5), figsize=(6.4, 4.6),
                            passo_y=1)

    f = lambda x: 0.8 * x**2
    a, h = 1.0, 1.5

    ec.plotar(ax, f, (-0.4, 2.9), rotulo="$y=f(x)$")

    P = (a, f(a))
    Q = (a + h, f(a + h))

    # Secante por P e Q.
    m = (Q[1] - P[1]) / h
    ax.plot([-0.2, 3.2], [P[1] + m * (-0.2 - a), P[1] + m * (3.2 - a)],
            color=ec.CORES["destaque"], linewidth=1.8, zorder=3)

    # Triângulo dos catetos.
    ax.plot([P[0], Q[0]], [P[1], P[1]], color=ec.CORES["curva3"], linewidth=2.0,
            zorder=3)
    ax.plot([Q[0], Q[0]], [P[1], Q[1]], color=ec.CORES["curva2"], linewidth=2.0,
            zorder=3)

    ec.ponto_fechado(ax, *P, cor=ec.CORES["destaque"], tamanho=6)
    ec.ponto_fechado(ax, *Q, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("$P\\,(a,\\,f(a))$", xy=P, xytext=(-70, -16),
                textcoords="offset points", fontsize=10)
    ax.annotate("$Q\\,(a+h,\\,f(a+h))$", xy=Q, xytext=(-30, 12),
                textcoords="offset points", fontsize=10)
    ax.annotate("$h$", xy=((P[0] + Q[0]) / 2, P[1]), xytext=(0, -20),
                textcoords="offset points", ha="center", color=ec.CORES["curva3"],
                fontsize=12)
    ax.annotate("$f(a+h)-f(a)$", xy=(Q[0], (P[1] + Q[1]) / 2), xytext=(8, -6),
                textcoords="offset points", color=ec.CORES["curva2"], fontsize=10)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "3.1-quociente-de-newton")


def tangente_e_normal() -> None:
    """Reta tangente e reta normal a uma curva em um ponto."""
    fig, ax = ec.novo_plano(xlim=(-1, 4), ylim=(-2, 5), figsize=(5.8, 4.4),
                            aspecto_igual=True)

    f = lambda x: 0.5 * x**2
    a = 2.0
    m = 2 * 0.5 * a  # f'(x) = x

    ec.plotar(ax, f, (-1, 3), rotulo="$y=f(x)$")

    xs = np.array([-1, 4])
    ax.plot(xs, f(a) + m * (xs - a), color=ec.CORES["curva2"], linewidth=2.0,
            zorder=3, label="tangente")
    ax.plot(xs, f(a) - (1 / m) * (xs - a), color=ec.CORES["curva3"], linewidth=2.0,
            zorder=3, label="normal")
    ec.ponto_fechado(ax, a, f(a), cor=ec.CORES["destaque"], tamanho=7)

    ax.annotate("$90^\\circ$", xy=(a + 0.25, f(a) + 0.2), color=ec.CORES["destaque"],
                fontsize=9)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "3.1-tangente-e-normal")


def _plano_nao_derivavel(titulo: str):
    return ec.novo_plano(xlim=(-2.2, 2.2), ylim=(-2.2, 2.6), figsize=(3.6, 3.2),
                         titulo=titulo, passo_x=1, passo_y=1)


def nao_derivavel_bico() -> None:
    """Bico: as derivadas laterais existem e são diferentes."""
    fig, ax = _plano_nao_derivavel("bico")
    ec.plotar(ax, np.abs, (-2.2, 2.2))
    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["destaque"], tamanho=6)
    ec.salvar(fig, UNIDADE, "3.1-nao-derivavel-bico")


def nao_derivavel_tangente_vertical() -> None:
    """Tangente vertical: o quociente de Newton tende a infinito."""
    fig, ax = _plano_nao_derivavel("tangente vertical")
    ec.plotar(ax, np.cbrt, (-2.2, 2.2))
    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["destaque"], tamanho=6)
    ec.assintota_vertical(ax, 0)
    ec.salvar(fig, UNIDADE, "3.1-nao-derivavel-tangente-vertical")


def nao_derivavel_salto() -> None:
    """Descontinuidade: nem contínua, logo nem derivável."""
    fig, ax = _plano_nao_derivavel("salto")
    ec.plotar(ax, lambda x: x + 1, (-2.2, 0), cor=ec.CORES["curva"])
    ec.plotar(ax, lambda x: x - 1, (0, 2.2), cor=ec.CORES["curva2"])
    ec.ponto_fechado(ax, 0, 1, cor=ec.CORES["curva"])
    ec.ponto_aberto(ax, 0, -1, cor=ec.CORES["curva2"])
    ec.salvar(fig, UNIDADE, "3.1-nao-derivavel-salto")


def funcao_e_derivada() -> None:
    """f(x) = x^3 - 3x e a sua derivada, lado a lado no mesmo plano."""
    fig, ax = ec.novo_plano(xlim=(-2.6, 2.6), ylim=(-4.5, 4.5), figsize=(6.4, 4.6),
                            passo_y=1)

    f = lambda x: x**3 - 3 * x
    d = lambda x: 3 * x**2 - 3

    ec.plotar(ax, f, (-2.3, 2.3), cor=ec.CORES["curva"], rotulo="$f(x)=x^3-3x$")
    ec.plotar(ax, d, (-2.0, 2.0), cor=ec.CORES["curva2"],
              rotulo="$f'(x)=3x^2-3$")

    for x0 in (-1, 1):
        ec.ponto_fechado(ax, x0, f(x0), cor=ec.CORES["destaque"], tamanho=6)
        ec.ponto_fechado(ax, x0, 0, cor=ec.CORES["destaque"], tamanho=6)
        ec.linha_guia(ax, x=x0)

    ax.annotate("onde $f$ tem pico ou vale,\n$f'$ corta o eixo $x$",
                xy=(1, 0), xytext=(-2.5, 2.6), color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower right")
    ec.salvar(fig, UNIDADE, "3.1-funcao-e-derivada")


# ======================================================================================
# 3.2 — Derivadas das funções elementares
# ======================================================================================

def _eixo_em_pi(ax, de=-1, ate=2) -> None:
    nomes = {-1: r"$-\pi$", -0.5: r"$-\frac{\pi}{2}$", 0.5: r"$\frac{\pi}{2}$",
             1: r"$\pi$", 1.5: r"$\frac{3\pi}{2}$", 2: r"$2\pi$"}
    marcas, rotulos = [], []
    k = de
    while k <= ate + 1e-9:
        if abs(k) > 1e-9 and k in nomes:
            marcas.append(k * np.pi)
            rotulos.append(nomes[k])
        k += 0.5
    ax.set_xticks(marcas)
    ax.set_xticklabels(rotulos)


def seno_e_sua_derivada() -> None:
    """sen e cos no mesmo plano: onde um tem pico, o outro cruza o eixo."""
    fig, ax = ec.novo_plano(xlim=(-0.6, 2 * np.pi + 0.5), ylim=(-1.8, 1.8),
                            figsize=(7.2, 3.6), passo_x=None, passo_y=1)
    _eixo_em_pi(ax, de=0.5, ate=2)

    ec.plotar(ax, np.sin, (0, 2 * np.pi), cor=ec.CORES["curva"],
              rotulo=r"$f(x)=\mathrm{sen}\,x$")
    ec.plotar(ax, np.cos, (0, 2 * np.pi), cor=ec.CORES["curva2"],
              rotulo=r"$f'(x)=\cos x$")

    for x0 in (np.pi / 2, 3 * np.pi / 2):
        ec.ponto_fechado(ax, x0, np.sin(x0), cor=ec.CORES["destaque"], tamanho=6)
        ec.ponto_fechado(ax, x0, 0, cor=ec.CORES["destaque"], tamanho=6)
        ec.linha_guia(ax, x=x0)

    ax.annotate("pico de $f$  ⇔  $f'$ zera", xy=(np.pi / 2, 1), xytext=(2.0, 1.45),
                color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="lower left")
    ec.salvar(fig, UNIDADE, "3.2-seno-e-sua-derivada")


def exponencial_inclinacao() -> None:
    """Em e^x, a inclinação da tangente é igual à altura do ponto."""
    fig, ax = ec.novo_plano(xlim=(-2.2, 2.2), ylim=(-1, 7), figsize=(6.0, 4.6),
                            passo_y=1)

    ec.plotar(ax, np.exp, (-2.2, 1.9), rotulo="$y=e^x$")

    for a in (0.0, 1.0):
        h = np.exp(a)
        xs = np.array([a - 1.1, a + 1.1])
        ax.plot(xs, h + h * (xs - a), color=ec.CORES["curva2"], linewidth=1.8,
                zorder=3)
        ec.ponto_fechado(ax, a, h, cor=ec.CORES["destaque"], tamanho=6)
        ax.annotate(f"altura {h:.2f}\ninclinação {h:.2f}".replace(".", ","),
                    xy=(a, h), xytext=(10, -34), textcoords="offset points",
                    color=ec.CORES["destaque"], fontsize=9)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "3.2-exponencial-inclinacao")


# ======================================================================================
# 3.3 — Regra da cadeia e derivada da função inversa
# ======================================================================================

def cadeia_compressao() -> None:
    """sen(3x) sobe três vezes mais rápido que sen(x): é o fator de dentro."""
    fig, ax = ec.novo_plano(xlim=(-0.5, 2 * np.pi + 0.4), ylim=(-1.8, 1.8),
                            figsize=(7.2, 3.8), passo_x=None, passo_y=1)
    _eixo_em_pi(ax, de=0.5, ate=2)

    ec.plotar(ax, np.sin, (0, 2 * np.pi), cor=ec.CORES["curva"],
              rotulo=r"$y=\mathrm{sen}\,x$")
    ec.plotar(ax, lambda x: np.sin(3 * x), (0, 2 * np.pi), cor=ec.CORES["curva2"],
              rotulo=r"$y=\mathrm{sen}\,3x$")

    # Tangentes na origem: inclinações 1 e 3.
    xs = np.array([-0.35, 0.55])
    ax.plot(xs, xs, color=ec.CORES["curva"], linestyle="--", linewidth=1.5, zorder=4)
    ax.plot(np.array([-0.2, 0.42]), 3 * np.array([-0.2, 0.42]),
            color=ec.CORES["curva2"], linestyle="--", linewidth=1.5, zorder=4)
    ec.ponto_fechado(ax, 0, 0, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("inclinação 1", xy=(0.6, 0.6), color=ec.CORES["curva"], fontsize=9)
    ax.annotate("inclinação 3", xy=(0.45, 1.45), color=ec.CORES["curva2"], fontsize=9)

    ec.legenda(ax, local="lower left")
    ec.salvar(fig, UNIDADE, "3.3-cadeia-compressao")


def inversa_inclinacoes() -> None:
    """As inclinações de f e de f^-1 em pontos correspondentes são inversas."""
    fig, ax = ec.novo_plano(xlim=(-0.5, 4.5), ylim=(-0.5, 4.5), figsize=(5.4, 5.0),
                            aspecto_igual=True)

    f = lambda x: x**2
    a = 1.5
    b = f(a)  # 2.25

    ec.plotar(ax, f, (0, 2.1), cor=ec.CORES["curva"], rotulo="$y=x^2$")
    ec.plotar(ax, np.sqrt, (0, 4.5), cor=ec.CORES["curva2"],
              rotulo=r"$y=\sqrt{x}$")
    ax.plot([-0.4, 4.4], [-0.4, 4.4], color=ec.CORES["tracejado"], linestyle="--",
            linewidth=1.2, zorder=2)

    # Tangente a f em (a, b): inclinação 2a = 3.
    m = 2 * a
    xs = np.array([a - 0.8, a + 0.8])
    ax.plot(xs, b + m * (xs - a), color=ec.CORES["curva"], linewidth=1.6, zorder=3)
    # Tangente à inversa em (b, a): inclinação 1/(2a) = 1/3.
    ys = np.array([b - 1.6, b + 1.6])
    ax.plot(ys, a + (1 / m) * (ys - b), color=ec.CORES["curva2"], linewidth=1.6,
            zorder=3)

    ec.ponto_fechado(ax, a, b, cor=ec.CORES["destaque"], tamanho=6)
    ec.ponto_fechado(ax, b, a, cor=ec.CORES["destaque"], tamanho=6)

    ax.annotate("inclinação 3", xy=(a, b), xytext=(-18, 26),
                textcoords="offset points", color=ec.CORES["curva"], fontsize=9)
    ax.annotate(r"inclinação $1/3$", xy=(b, a), xytext=(14, -26),
                textcoords="offset points", color=ec.CORES["curva2"], fontsize=9)

    ec.legenda(ax, local="upper left")
    ec.salvar(fig, UNIDADE, "3.3-inversa-inclinacoes")


# ======================================================================================

FIGURAS = [
    secantes_para_tangente,
    quociente_de_newton,
    tangente_e_normal,
    nao_derivavel_bico,
    nao_derivavel_tangente_vertical,
    nao_derivavel_salto,
    funcao_e_derivada,
    seno_e_sua_derivada,
    exponencial_inclinacao,
    cadeia_compressao,
    inversa_inclinacoes,
]


def main() -> None:
    ec.configurar()
    print("Gerando as figuras da Unidade 3...")
    for figura in FIGURAS:
        figura()
    print(f"Pronto: {len(FIGURAS)} figuras.")


if __name__ == "__main__":
    main()
