# 📝 Lista 5.2 — Técnicas de integração

> **Antes de começar:** leia a [teoria 5.2](../5.2-tecnicas-de-integracao.md).

Esta é a lista mais longa do material — e com razão: integrar se aprende por volume. No **Bloco A** a técnica está indicada; a partir do **Bloco B**, você decide.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 10 | Todos |
| **B · Consolidação** | 11 a 22 | Todos |
| **C · Desafio** | 23 a 27 | Os que der |

---

## Bloco A · Fixação

### Substituição

**1.** Calcule:

&nbsp;&nbsp;**(a)** $\displaystyle\int \big(3x+5\big)^{7}dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int 2x\big(x^2-4\big)^{5}dx$

&nbsp;&nbsp;**(c)** $\displaystyle\int \frac{x\thinspace dx}{\sqrt{x^2+9}}$ &nbsp;&nbsp;&nbsp; **(d)** $\displaystyle\int \mathrm{sen}\big(5x\big)dx$

**2.** Calcule:

&nbsp;&nbsp;**(a)** $\displaystyle\int \frac{dx}{3x-1}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int \frac{2x+3}{x^2+3x+1}\thinspace dx$

&nbsp;&nbsp;**(c)** $\displaystyle\int \frac{\ln x}{x}\thinspace dx$ &nbsp;&nbsp;&nbsp; **(d)** $\displaystyle\int \mathrm{cotg}\thinspace x\thinspace dx$

**3.** Calcule:

&nbsp;&nbsp;**(a)** $\displaystyle\int \cos^3 x\mathrm{sen}\thinspace x\thinspace dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int x\thinspace e^{-x^2}dx$ &nbsp;&nbsp;&nbsp; **(c)** $\displaystyle\int \frac{e^{\sqrt{x}}}{\sqrt{x}}\thinspace dx$

### Integração por partes

**4.** Calcule:

&nbsp;&nbsp;**(a)** $\displaystyle\int x\mathrm{sen}\thinspace x\thinspace dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int x\thinspace e^{3x}dx$ &nbsp;&nbsp;&nbsp; **(c)** $\displaystyle\int x\ln x\thinspace dx$

**5.** Calcule (precisa de **duas** aplicações):

&nbsp;&nbsp;**(a)** $\displaystyle\int x^2 e^{x}dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int x^2\cos x\thinspace dx$

**6.** Calcule, usando o truque $dv = dx$:

&nbsp;&nbsp;**(a)** $\displaystyle\int \mathrm{arctg}\thinspace x\thinspace dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int \mathrm{arcsen}\thinspace x\thinspace dx$

### Frações parciais

**7.** Decomponha em frações parciais (**não** integre):

&nbsp;&nbsp;**(a)** $\dfrac{1}{x^2-1}$ &nbsp;&nbsp;&nbsp; **(b)** $\dfrac{5x-4}{x^2-x-6}$ &nbsp;&nbsp;&nbsp; **(c)** $\dfrac{2}{x(x+1)^2}$

**8.** Calcule:

&nbsp;&nbsp;**(a)** $\displaystyle\int\frac{dx}{x^2-1}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int\frac{5x-4}{x^2-x-6}\thinspace dx$

### Substituição trigonométrica

**9.** Indique a substituição adequada (**não** calcule):

&nbsp;&nbsp;**(a)** $\displaystyle\int\frac{dx}{\sqrt{25-x^2}}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int\frac{dx}{x^2\sqrt{x^2+4}}$ &nbsp;&nbsp;&nbsp; **(c)** $\displaystyle\int\sqrt{x^2-16}\thinspace dx$

**10.** Calcule $\displaystyle\int\frac{dx}{\sqrt{4-x^2}}$ de **duas** maneiras: pela tabela e por substituição trigonométrica. Confirme que dá o mesmo.

---

## Bloco B · Consolidação

> A partir daqui **a técnica não é indicada**. Olhe o integrando e decida.

**11.** $\displaystyle\int \frac{x^2}{\sqrt{x^3+1}}\thinspace dx$

**12.** $\displaystyle\int x\sqrt{x-1}\thinspace dx$

&nbsp;&nbsp;*(Sugestão: $u = x-1$, e então $x = u+1$.)*

**13.** $\displaystyle\int e^{x}\cos x\thinspace dx$

**14.** $\displaystyle\int \frac{x+5}{x^2+x-6}\thinspace dx$

**15.** $\displaystyle\int \frac{x^3}{x-2}\thinspace dx$

**16.** $\displaystyle\int \mathrm{sen}^2\thinspace x\thinspace dx$

**17.** $\displaystyle\int \mathrm{sen}^3\thinspace x\thinspace dx$

&nbsp;&nbsp;*(Sugestão: separe um $\mathrm{sen}\thinspace x$ e use $\mathrm{sen}^2 = 1-\cos^2$.)*

**18.** $\displaystyle\int \frac{dx}{x^2+6x+13}$

&nbsp;&nbsp;*(Sugestão: complete o quadrado.)*

**19.** $\displaystyle\int \frac{\sqrt{4-x^2}}{x^2}\thinspace dx$

**20.** $\displaystyle\int \ln\big(x^2\big)dx$

**21.** $\displaystyle\int \frac{3x^2+2x-1}{x^3+x}\thinspace dx$

**22.** $\displaystyle\int x^3 e^{x^2}dx$

&nbsp;&nbsp;*(Sugestão: comece com $u=x^2$ e depois use partes.)*

---

## Bloco C · Desafio

**23.** Mostre que

$$\int \mathrm{sec}\thinspace x\thinspace dx = \ln\lvert\mathrm{sec}\thinspace x + \mathrm{tg}\thinspace x\rvert + C$$

&nbsp;&nbsp;*(Sugestão: multiplique e divida por $\mathrm{sec}\thinspace x + \mathrm{tg}\thinspace x$.)*

**24.** Deduza a **fórmula de redução**

$$\int \mathrm{sen}^n\thinspace x\thinspace dx = -\frac{\mathrm{sen}^{n-1}\thinspace x\cos x}{n} + \frac{n-1}{n}\int \mathrm{sen}^{n-2}\thinspace x\thinspace dx$$

&nbsp;&nbsp;e use-a para calcular $\displaystyle\int\mathrm{sen}^4\thinspace x\thinspace dx$.

**25.** $\displaystyle\int \frac{dx}{1+e^{x}}$

**26.** Calcule $\displaystyle\int \mathrm{sen}\thinspace x\cos x\thinspace dx$ de **três** maneiras:

&nbsp;&nbsp;**(a)** com $u=\mathrm{sen}\thinspace x$; &nbsp;&nbsp;**(b)** com $u=\cos x$; &nbsp;&nbsp;**(c)** usando $\mathrm{sen}\thinspace 2x = 2\mathrm{sen}\thinspace x\cos x$.

&nbsp;&nbsp;As três respostas parecem diferentes. Mostre que todas estão corretas.

**27.** $\displaystyle\int \frac{dx}{x\sqrt{x^2-1}}$

---

## ✅ Conferir

➡️ **[Gabarito da Lista 5.2](../gabaritos/gabarito-5.2.md)**

---

| ← Lista anterior | 🏠 Índice | Próxima lista → |
| :--- | :---: | ---: |
| [Lista 5.1](lista-5.1-propostos.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Lista 5.3](lista-5.3-propostos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
