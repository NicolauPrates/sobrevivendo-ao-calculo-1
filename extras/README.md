# Extras — 100% opcional

> [!IMPORTANT]
> **Você NÃO precisa instalar nada para estudar por este material.**
> Toda a teoria, todos os exercícios, todos os gabaritos e todos os gráficos já estão
> prontos e abrem direto no navegador. Esta pasta é um **bônus** para quem tem
> curiosidade de ver como os gráficos foram feitos — e, de quebra, aprender a plotar
> funções por conta própria. Se você fechar esta página agora, não perde absolutamente nada.

---

## O que tem aqui

```text
extras/
├── README.md                         você está aqui
└── scripts-graficos/
    ├── estilo_calculo.py             o estilo visual único de todos os gráficos
    ├── u1_funcoes.py                 gráficos da Unidade 1
    ├── u2_limites.py                 gráficos da Unidade 2
    ├── u3_derivadas.py               gráficos da Unidade 3
    ├── u4_aplicacoes.py              gráficos da Unidade 4
    └── u5_integrais.py               gráficos da Unidade 5
```

Cada script gera os arquivos `.svg` de [`assets/img/`](../assets/img) usados nas páginas de teoria. A regra do repositório é simples: **nenhuma imagem entra aqui sem o script que a produz.** Isso garante que todo gráfico possa ser corrigido, ajustado e refeito anos depois.

---

## Por que isso vale o seu tempo (se você quiser)

Plotar uma função é a forma mais rápida de **conferir se você entendeu**. Você calculou que $f(x) = \frac{x^2-1}{x-1}$ tem um "buraco" em $x = 1$? Plote e veja. Achou que a derivada troca de sinal em $x = -2$? Plote a função e a derivada no mesmo gráfico e confira.

Além disso, saber usar `numpy` e `matplotlib` é útil em praticamente toda disciplina de engenharia e de ciências exatas que vem depois — Física Experimental, Cálculo Numérico, Estatística, laboratórios em geral.

> [!TIP]
> **Atenção ao usar o computador para estudar Cálculo.** O gráfico serve para **conferir** e para **criar intuição**, nunca para substituir a conta. Em prova você não terá Python. Faça à mão primeiro, plote depois.

---

## Como rodar

### 1. Instale o Python

Qualquer uma das opções abaixo serve:

- **[Anaconda](https://www.anaconda.com/download)** — mais pesado, mas já vem com tudo (`numpy`, `matplotlib`, Jupyter). É o caminho mais simples para quem nunca instalou Python.
- **[Python.org](https://www.python.org/downloads/)** — instalação enxuta. No Windows, marque a caixa **"Add Python to PATH"** durante a instalação.

### 2. Instale as duas bibliotecas

Quem instalou o Anaconda pode pular esta etapa.

```bash
pip install numpy matplotlib
```

### 3. Rode o script da unidade que quiser

A partir da pasta `extras/scripts-graficos`:

```bash
python u1_funcoes.py
```

As figuras são gravadas (ou sobrescritas) em `assets/img/<unidade>/`. O script imprime o caminho de cada arquivo gerado.

Para gerar os gráficos de todas as unidades de uma vez:

```bash
python u1_funcoes.py && python u2_limites.py && python u3_derivadas.py && python u4_aplicacoes.py && python u5_integrais.py
```

---

## Como fazer o seu próprio gráfico

O arquivo `estilo_calculo.py` cuida de toda a parte chata — eixos cruzando na origem, setas nas pontas, cores, grade, fundo branco — e deixa você escrever apenas a matemática:

```python
import numpy as np
import estilo_calculo as ec

ec.configurar()

# Plano cartesiano de -3 a 3 no eixo x, -2 a 8 no eixo y
fig, ax = ec.novo_plano(xlim=(-3, 3), ylim=(-2, 8))

# A função
ec.plotar(ax, lambda x: x**2, (-3, 3), rotulo="$f(x) = x^2$")

# Um ponto que pertence ao gráfico, e uma seta apontando para ele
ec.ponto_fechado(ax, 2, 4)
ec.anotar(ax, "$(2, 4)$", xy=(2, 4), xytext=(2.3, 6))

ec.legenda(ax)
ec.salvar(fig, "01-funcoes", "meu-primeiro-grafico")
```

### As funções que você tem à disposição

| Função | O que faz |
| --- | --- |
| `configurar()` | Aplica o estilo do repositório. Chame uma vez, no início |
| `novo_plano(xlim, ylim, ...)` | Plano cartesiano com eixos na origem e setas |
| `nova_reta_real(xlim, ...)` | Reta real isolada — para intervalos e conjuntos-solução |
| `plotar(ax, f, (a, b), ...)` | Desenha a curva de `f` no intervalo dado |
| `ponto_fechado(ax, x, y)` | Bolinha cheia: o ponto pertence ao gráfico |
| `ponto_aberto(ax, x, y)` | Bolinha vazia: o ponto não pertence |
| `intervalo(ax, a, b, ...)` | Destaca um intervalo sobre a reta real, com bolinha cheia ou vazia |
| `assintota_vertical(ax, x)` | Reta vertical tracejada |
| `assintota_horizontal(ax, y)` | Reta horizontal tracejada |
| `linha_guia(ax, x=..., y=...)` | Linha pontilhada de projeção de coordenada |
| `area_sob(ax, f, a, b)` | Preenche a área entre a curva e o eixo $x$ |
| `anotar(ax, texto, xy, xytext)` | Texto com seta, para dizer o que olhar |
| `legenda(ax)` | Legenda no padrão do material |
| `salvar(fig, unidade, nome)` | Grava o `.svg` em `assets/img/<unidade>/` |

> [!NOTE]
> **Função com assíntota ou com quebra:** plote **um trecho por vez**. Se você pedir
> `plotar(ax, lambda x: 1/x, (-3, 3))`, o matplotlib liga os dois ramos com um segmento
> vertical que não existe na função. O correto é chamar `plotar` duas vezes, em
> `(-3, -0.05)` e em `(0.05, 3)`.

---

## Convenções visuais (para quem for contribuir)

Antes de enviar um gráfico novo, leia a [§8 das convenções](../CONVENCOES.md#8-gráficos). Em resumo:

- **SVG**, sempre — nunca PNG.
- Cores **somente** do dicionário `CORES` de `estilo_calculo.py`.
- **Fundo branco explícito** (já é o padrão): o GitHub tem tema escuro.
- Nome do arquivo: `<N.M>-<descricao-curta>.svg`, por exemplo `1.3-paridade-x3-3x.svg`.
- Comite **o script e a imagem juntos**, no mesmo commit.

---

| 🏠 Índice |
| :---: |
| [Página inicial](../README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
