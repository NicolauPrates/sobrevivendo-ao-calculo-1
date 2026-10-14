# A2 · Tabela de integrais

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A1 · Tabela de derivadas](A1-tabela-de-derivadas.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A3 · Identidades trigonométricas](A3-identidades-trigonometricas.md) |

> **Teoria correspondente:** [5.1](../05-integrais/5.1-primitivas-e-o-conceito-de-integral.md) e [5.2](../05-integrais/5.2-tecnicas-de-integracao.md).

> **Em todas as linhas, some $+\thinspace C$.** Omitido por economia de espaço, obrigatório na sua prova.

---

## 1. Imediatas

| Integral | Resultado |
| --- | --- |
| $\displaystyle\int k\thinspace dx$ | $kx$ |
| $\displaystyle\int x^{n}dx$ &nbsp;($n\neq-1$) | $\dfrac{x^{n+1}}{n+1}$ |
| $\displaystyle\int\frac{dx}{x}$ | $\ln\lvert x\rvert$ |
| $\displaystyle\int e^{x}dx$ | $e^{x}$ |
| $\displaystyle\int a^{x}dx$ | $\dfrac{a^{x}}{\ln a}$ |
| $\displaystyle\int\ln x\thinspace dx$ | $x\ln x - x$ |

> ⚠️ **$n=-1$ é o único caso fora da regra da potência**, e sua resposta é de outra natureza: o logaritmo. É o buraco mais cobrado da tabela.

---

## 2. Trigonométricas

| Integral | Resultado |
| --- | --- |
| $\displaystyle\int\mathrm{sen}\thinspace x\thinspace dx$ | $-\cos x$ |
| $\displaystyle\int\cos x\thinspace dx$ | $\mathrm{sen}\thinspace x$ |
| $\displaystyle\int\mathrm{sec}^2\thinspace x\thinspace dx$ | $\mathrm{tg}\thinspace x$ |
| $\displaystyle\int\mathrm{cossec}^2\thinspace x\thinspace dx$ | $-\mathrm{cotg}\thinspace x$ |
| $\displaystyle\int\mathrm{sec}\thinspace x\mathrm{tg}\thinspace x\thinspace dx$ | $\mathrm{sec}\thinspace x$ |
| $\displaystyle\int\mathrm{cossec}\thinspace x\mathrm{cotg}\thinspace x\thinspace dx$ | $-\mathrm{cossec}\thinspace x$ |

### As quatro que exigem truque

| Integral | Resultado | Como sai |
| --- | --- | --- |
| $\displaystyle\int\mathrm{tg}\thinspace x\thinspace dx$ | $-\ln\lvert\cos x\rvert = \ln\lvert\mathrm{sec}\thinspace x\rvert$ | $u=\cos x$ |
| $\displaystyle\int\mathrm{cotg}\thinspace x\thinspace dx$ | $\ln\lvert\mathrm{sen}\thinspace x\rvert$ | $u=\mathrm{sen}\thinspace x$ |
| $\displaystyle\int\mathrm{sec}\thinspace x\thinspace dx$ | $\ln\lvert\mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x\rvert$ | multiplique por $\frac{\mathrm{sec}+\mathrm{tg}}{\mathrm{sec}+\mathrm{tg}}$ |
| $\displaystyle\int\mathrm{cossec}\thinspace x\thinspace dx$ | $-\ln\lvert\mathrm{cossec}\thinspace x+\mathrm{cotg}\thinspace x\rvert$ | truque análogo |

> 💡 **A integral da secante é a única da tabela que ninguém redescobre em prova.** Memorize-a: ela aparece sempre que você calcular comprimento de arco.

### Potências de seno e cosseno

| Integral | Resultado |
| --- | --- |
| $\displaystyle\int\mathrm{sen}^2\thinspace x\thinspace dx$ | $\dfrac{x}{2}-\dfrac{\mathrm{sen}\thinspace 2x}{4}$ |
| $\displaystyle\int\cos^2 x\thinspace dx$ | $\dfrac{x}{2}+\dfrac{\mathrm{sen}\thinspace 2x}{4}$ |
| $\displaystyle\int\mathrm{tg}^2\thinspace x\thinspace dx$ | $\mathrm{tg}\thinspace x - x$ |
| $\displaystyle\int\mathrm{cotg}^2\thinspace x\thinspace dx$ | $-\mathrm{cotg}\thinspace x - x$ |

> 💡 **A estratégia geral das potências:** expoente **ímpar** → separe um fator e substitua; expoente **par** → use o arco duplo ([A3](A3-identidades-trigonometricas.md)).

---

## 3. Formas com $a$ — as que produzem arco e logaritmo

| Integral | Resultado |
| --- | --- |
| $\displaystyle\int\frac{dx}{a^2+x^2}$ | $\dfrac1a\mathrm{arctg}\thinspace\dfrac{x}{a}$ |
| $\displaystyle\int\frac{dx}{\sqrt{a^2-x^2}}$ | $\mathrm{arcsen}\thinspace\dfrac{x}{a}$ |
| $\displaystyle\int\frac{dx}{x\sqrt{x^2-a^2}}$ | $\dfrac1a\mathrm{arcsec}\left\lvert\dfrac{x}{a}\right\rvert$ |
| $\displaystyle\int\frac{dx}{a^2-x^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{a+x}{a-x}\right\rvert$ |
| $\displaystyle\int\frac{dx}{x^2-a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert$ |
| $\displaystyle\int\frac{dx}{\sqrt{x^2\pm a^2}}$ | $\ln\left\lvert x+\sqrt{x^2\pm a^2}\right\rvert$ |
| $\displaystyle\int\sqrt{a^2-x^2}\thinspace dx$ | $\dfrac{x\sqrt{a^2-x^2}}{2}+\dfrac{a^2}{2}\mathrm{arcsen}\thinspace\dfrac{x}{a}$ |

> [!TIP]
> **O radical decide o destino.** Denominador com **radical** de soma/diferença de quadrados → **arco** (seno ou secante). Denominador **sem** radical, com diferença de quadrados → **logaritmo** (frações parciais). Soma de quadrados sem radical → **arco-tangente**.
>
> Note o contraste entre a segunda e a quarta linha: o mesmo $a^2-x^2$, com e sem raiz, produz funções de famílias completamente diferentes.

---

## 4. As quatro técnicas, em uma página

| Técnica | Quando usar | Fórmula |
| --- | --- | --- |
| **Substituição** | há uma função **e a derivada dela** | $\displaystyle\int f\big(g\big)g'dx = \int f(u)du$ |
| **Por partes** | produto de tipos diferentes | $\displaystyle\int u\thinspace dv = uv-\int v\thinspace du$ |
| **Frações parciais** | quociente de polinômios | some $\frac{A}{x-a}$, uma parcela por fator |
| **Trigonométrica** | radical de soma/diferença de quadrados | veja a tabela abaixo |

### LIATE — quem vai no $u$ da integração por partes

**L**ogarítmica · **I**nversa trigonométrica · **A**lgébrica · **T**rigonométrica · **E**xponencial

A **primeira** da lista que aparecer no integrando vira $u$; o resto vira $dv$.

### Substituição trigonométrica

| Se aparece | Substitua | O radical vira |
| :---: | :---: | :---: |
| $\sqrt{a^2-x^2}$ | $x = a\mathrm{sen}\thinspace\theta$ | $a\cos\theta$ |
| $\sqrt{a^2+x^2}$ | $x = a\mathrm{tg}\thinspace\theta$ | $a\mathrm{sec}\thinspace\theta$ |
| $\sqrt{x^2-a^2}$ | $x = a\mathrm{sec}\thinspace\theta$ | $a\mathrm{tg}\thinspace\theta$ |

**Mnemônico dos sinais:** menos **primeiro** → seno · **mais** → tangente · menos **depois** → secante.

### Frações parciais — o que cada fator gera

| Fator no denominador | Parcelas |
| --- | --- |
| $(x-a)$ | $\dfrac{A}{x-a}$ |
| $(x-a)^n$ | $\dfrac{A_1}{x-a}+\dfrac{A_2}{(x-a)^2}+\cdots+\dfrac{A_n}{(x-a)^n}$ |
| $x^2+bx+c$ irredutível | $\dfrac{Ax+B}{x^2+bx+c}$ |

> ⚠️ **Antes de decompor:** o grau do numerador tem de ser **menor** que o do denominador. Se não for, **divida os polinômios primeiro**.

---

## 5. Padrões que valem mais que a tabela

| Padrão | Resultado | Por quê |
| --- | --- | --- |
| $\displaystyle\int\frac{g'(x)}{g(x)}dx$ | $\ln\lvert g(x)\rvert$ | **o mais frequente de todos** |
| $\displaystyle\int g'(x)\thinspace e^{g(x)}dx$ | $e^{g(x)}$ | cadeia ao contrário |
| $\displaystyle\int g'(x)\big[g(x)\big]^{n}dx$ | $\dfrac{\big[g(x)\big]^{n+1}}{n+1}$ | potência com cadeia |
| $\displaystyle\int f(ax+b)\thinspace dx$ | $\dfrac1a F(ax+b)$ | argumento linear |

> 💡 **Reconhecer o primeiro padrão de olho economiza minutos por prova.** Sempre que o numerador for (múltiplo de) a derivada do denominador, a resposta é logarítmica — sem escrever o $u$.

---

## 6. Integral definida

$$\int_a^b f(x)\thinspace dx = F(b)-F(a) = \Big[F(x)\Big]_a^b \qquad\text{(TFC, parte 2)}$$

$$\frac{d}{dx}\int_a^{g(x)} f(t)\thinspace dt = f\big(g(x)\big)\thinspace g'(x) \qquad\text{(TFC, parte 1)}$$

| Propriedade | |
| --- | --- |
| $\displaystyle\int_a^a f = 0$ | intervalo nulo |
| $\displaystyle\int_b^a f = -\int_a^b f$ | inversão |
| $\displaystyle\int_a^c f = \int_a^b f + \int_b^c f$ | aditividade |
| $f$ **par**: $\displaystyle\int_{-a}^{a} f = 2\int_0^a f$ | simetria |
| $f$ **ímpar**: $\displaystyle\int_{-a}^{a} f = 0$ | simetria |

> ⚠️ **Integral definida não leva $+\thinspace C$** — a constante se cancela em $F(b)-F(a)$.
>
> E **integral não é área**: $\text{área} = \int\lvert f\rvert$, quebrando onde $f$ troca de sinal.

---

## 7. Aplicações

| | Fórmula |
| --- | --- |
| **Área entre curvas** | $\displaystyle A = \int_a^b\big[f-g\big]dx$ &nbsp;(de cima menos de baixo) |
| **Volume — disco** | $\displaystyle V = \pi\int_a^b\big[f(x)\big]^2 dx$ |
| **Volume — anel** | $\displaystyle V = \pi\int_a^b\big(R^2-r^2\big)dx$ |
| **Volume — casca** | $\displaystyle V = 2\pi\int_a^b x\thinspace h(x)\thinspace dx$ |
| **Comprimento de arco** | $\displaystyle L = \int_a^b\sqrt{1+\big(f'\big)^2}\thinspace dx$ |
| **Área de superfície** | $\displaystyle S = 2\pi\int_a^b f\sqrt{1+\big(f'\big)^2}\thinspace dx$ |
| **Valor médio** | $\displaystyle f_{\text{méd}} = \frac{1}{b-a}\int_a^b f$ |

---

## 8. Integrais impróprias — o teste da $p$-integral

| Integral | Converge se |
| --- | :---: |
| $\displaystyle\int_1^{\infty}\frac{dx}{x^{p}}$ | $p>1$ &nbsp;(e vale $\frac{1}{p-1}$) |
| $\displaystyle\int_0^{1}\frac{dx}{x^{p}}$ | $p<1$ &nbsp;(e vale $\frac{1}{1-p}$) |

**Comparação:** teto que converge segura; piso que diverge empurra.

---

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A1 · Tabela de derivadas](A1-tabela-de-derivadas.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A3 · Identidades trigonométricas](A3-identidades-trigonometricas.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
