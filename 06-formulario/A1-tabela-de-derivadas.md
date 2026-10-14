# A1 · Tabela de derivadas

| ← Índice | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [Formulário](README.md) | [Página inicial](../README.md) | [A2 · Tabela de integrais](A2-tabela-de-integrais.md) |

> **Teoria correspondente:** [3.1](../03-derivadas/3.1-conceito-interpretacao-geometrica-e-regras-basicas.md) a [3.4](../03-derivadas/3.4-derivadas-das-funcoes-trigonometricas-inversas.md).

---

## 1. As regras

| Regra | Fórmula |
| --- | --- |
| **Constante** | $\big(k\big)' = 0$ |
| **Potência** | $\big(x^{n}\big)' = n\thinspace x^{n-1}$ &nbsp; (vale para todo $n$ real) |
| **Constante vezes função** | $\big(k\thinspace f\big)' = k\thinspace f'$ |
| **Soma** | $\big(f \pm g\big)' = f' \pm g'$ |
| **Produto** | $\big(f\thinspace g\big)' = f'g + fg'$ |
| **Quociente** | $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$ |
| **Cadeia** | $\Big(f\big(g(x)\big)\Big)' = f'\big(g(x)\big)\cdot g'(x)$ |
| **Inversa** | $\big(f^{-1}\big)'(y) = \dfrac{1}{f'(x)}$, &nbsp;com $y=f(x)$ |

> 💡 **A regra do quociente em palavras:** *"derivada de cima vezes baixo, menos cima vezes derivada de baixo, tudo sobre baixo ao quadrado."* A ordem importa — o sinal de menos não é simétrico.

---

## 2. Funções elementares

| $f(x)$ | $f'(x)$ |
| :---: | :---: |
| $k$ | $0$ |
| $x$ | $1$ |
| $x^{n}$ | $n\thinspace x^{n-1}$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ |
| $\dfrac1x$ | $-\dfrac{1}{x^2}$ |
| $e^{x}$ | $e^{x}$ |
| $a^{x}$ | $a^{x}\ln a$ |
| $\ln x$ | $\dfrac1x$ |
| $\ln\lvert x\rvert$ | $\dfrac1x$ |
| $\log_a x$ | $\dfrac{1}{x\ln a}$ |

---

## 3. Trigonométricas

| $f(x)$ | $f'(x)$ |
| :---: | :---: |
| $\mathrm{sen}\thinspace x$ | $\cos x$ |
| $\cos x$ | $-\mathrm{sen}\thinspace x$ |
| $\mathrm{tg}\thinspace x$ | $\mathrm{sec}^2\thinspace x$ |
| $\mathrm{cotg}\thinspace x$ | $-\mathrm{cossec}^2\thinspace x$ |
| $\mathrm{sec}\thinspace x$ | $\mathrm{sec}\thinspace x\mathrm{tg}\thinspace x$ |
| $\mathrm{cossec}\thinspace x$ | $-\mathrm{cossec}\thinspace x\mathrm{cotg}\thinspace x$ |

> 💡 **O padrão do sinal:** as três **co**-funções (**co**sseno, **co**tangente, **co**ssecante) são as que ganham **menos**. Lembrar disso dispensa decorar seis linhas — bastam três mais a regra.

---

## 4. Trigonométricas inversas

| $f(x)$ | $f'(x)$ | Domínio de $f'$ |
| :---: | :---: | :---: |
| $\mathrm{arcsen}\thinspace x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | $-1<x<1$ |
| $\mathrm{arccos}\thinspace x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ | $-1<x<1$ |
| $\mathrm{arctg}\thinspace x$ | $\dfrac{1}{1+x^2}$ | $\mathbb{R}$ |
| $\mathrm{arccotg}\thinspace x$ | $-\dfrac{1}{1+x^2}$ | $\mathbb{R}$ |
| $\mathrm{arcsec}\thinspace x$ | $\dfrac{1}{\lvert x\rvert\sqrt{x^2-1}}$ | $\lvert x\rvert>1$ |
| $\mathrm{arccossec}\thinspace x$ | $-\dfrac{1}{\lvert x\rvert\sqrt{x^2-1}}$ | $\lvert x\rvert>1$ |

> 💡 **Mesmo padrão:** as **co**-inversas são as negativas das outras. E note que $\mathrm{arcsen}\thinspace x + \mathrm{arccos}\thinspace x = \frac{\pi}{2}$ é constante — por isso as derivadas são opostas.

---

## 5. Tudo de novo, com a cadeia

Na prática, o argumento quase nunca é $x$ puro. Com $u = u(x)$:

| $f$ | $f'$ |
| :---: | :---: |
| $u^{n}$ | $n\thinspace u^{n-1}\thinspace u'$ |
| $e^{u}$ | $e^{u}\thinspace u'$ |
| $a^{u}$ | $a^{u}\ln a\cdot u'$ |
| $\ln\lvert u\rvert$ | $\dfrac{u'}{u}$ |
| $\mathrm{sen}\thinspace u$ | $\cos u\cdot u'$ |
| $\cos u$ | $-\mathrm{sen}\thinspace u\cdot u'$ |
| $\mathrm{tg}\thinspace u$ | $\mathrm{sec}^2\thinspace u\cdot u'$ |
| $\mathrm{sec}\thinspace u$ | $\mathrm{sec}\thinspace u\mathrm{tg}\thinspace u\cdot u'$ |
| $\mathrm{arcsen}\thinspace u$ | $\dfrac{u'}{\sqrt{1-u^2}}$ |
| $\mathrm{arctg}\thinspace u$ | $\dfrac{u'}{1+u^2}$ |
| $\sqrt{u}$ | $\dfrac{u'}{2\sqrt{u}}$ |

> [!TIP]
> **Esta é a tabela que você realmente usa.** A da seção 2 é o caso particular $u=x$, em que $u'=1$. Treine com a versão $u$ desde o começo e a regra da cadeia deixa de ser um passo extra — vira parte da derivada.

---

## 6. Técnicas especiais

### Derivação implícita

Quando $y$ não está isolado, derive **os dois lados** em relação a $x$, tratando $y$ como função de $x$ (ou seja, cada $y$ derivado produz um $y'$), e **isole $y'$** no fim.

$$x^2+y^2 = 25 \ \Longrightarrow \ 2x + 2y\thinspace y' = 0 \ \Longrightarrow \ y' = -\frac{x}{y}$$

### Derivação logarítmica

Para produtos/quocientes longos, ou expoente variável: aplique $\ln$ dos dois lados, derive implicitamente e isole.

$$y = x^{x} \ \Longrightarrow \ \ln y = x\ln x \ \Longrightarrow \ \frac{y'}{y} = \ln x + 1 \ \Longrightarrow \ y' = x^{x}\big(\ln x+1\big)$$

> ⚠️ **$x^x$ não é nem potência nem exponencial** — a base e o expoente variam juntos. Nem $\big(x^x\big)' = x\thinspace x^{x-1}$, nem $x^x\ln x$. Só a derivação logarítmica resolve.

### Derivadas de ordem superior

$$f'' = \big(f'\big)' \qquad f''' = \big(f''\big)' \qquad f^{(n)} = \big(f^{(n-1)}\big)'$$

**Notações equivalentes:** $f'(x) = \dfrac{dy}{dx} = D_x y$ &nbsp;·&nbsp; $f''(x) = \dfrac{d^2y}{dx^2}$.

---

## 7. Os erros que a tabela não evita

| O erro | O certo |
| --- | --- |
| $\big(f\thinspace g\big)' = f'g'$ | $f'g + fg'$ |
| $\left(\frac{f}{g}\right)' = \frac{f'}{g'}$ | $\frac{f'g-fg'}{g^2}$ |
| $\big(\mathrm{sen}(x^2)\big)' = \cos(x^2)$ | falta o $\cdot\thinspace 2x$ da cadeia |
| $\big(e^{3x}\big)' = e^{3x}$ | $3e^{3x}$ |
| $\big(\ln(5x)\big)' = \frac{1}{5x}$ | $\frac{5}{5x} = \frac1x$ |
| $\big(2^{x}\big)' = x\thinspace 2^{x-1}$ | $2^{x}\ln 2$ — é exponencial, não potência |
| $\big(x^{x}\big)' = x\thinspace x^{x-1}$ | derivação logarítmica |

---

| ← Índice | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [Formulário](README.md) | [Página inicial](../README.md) | [A2 · Tabela de integrais](A2-tabela-de-integrais.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
