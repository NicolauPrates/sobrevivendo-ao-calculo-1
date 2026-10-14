# 📝 Lista 5.5 — Integrais impróprias

> **Antes de começar:** leia a [teoria 5.5](../5.5-integrais-improprias.md).

**O primeiro passo é sempre o mesmo:** olhe o integrando e descubra **por que** a integral é imprópria. Depois disso, é limite.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 9 | Todos |
| **B · Consolidação** | 10 a 18 | Todos |
| **C · Desafio** | 19 a 22 | Os que der |

---

## Bloco A · Fixação

**1.** Para cada integral, diga **se é imprópria** e, em caso afirmativo, de **qual tipo** e **onde** está o problema. Não calcule.

&nbsp;&nbsp;**(a)** $\displaystyle\int_0^{\infty}e^{-x}dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_0^{1}\frac{dx}{x-2}$ &nbsp;&nbsp;&nbsp; **(c)** $\displaystyle\int_0^{2}\frac{dx}{x-1}$

&nbsp;&nbsp;**(d)** $\displaystyle\int_1^{2}\ln(x-1)\thinspace dx$ &nbsp;&nbsp;&nbsp; **(e)** $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ &nbsp;&nbsp;&nbsp; **(f)** $\displaystyle\int_0^{\pi}\mathrm{tg}\thinspace x\thinspace dx$

**2.** Decida a convergência **pelo teste da $p$-integral** (sem calcular):

&nbsp;&nbsp;**(a)** $\displaystyle\int_1^{\infty}\frac{dx}{x^{3}}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$

&nbsp;&nbsp;**(c)** $\displaystyle\int_0^{1}\frac{dx}{x^{3}}$ &nbsp;&nbsp;&nbsp; **(d)** $\displaystyle\int_0^{1}\frac{dx}{\sqrt[3]{x}}$

**3.** Calcule, se convergirem:

&nbsp;&nbsp;**(a)** $\displaystyle\int_0^{\infty}e^{-2x}dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_1^{\infty}\frac{dx}{x^{4}}$ &nbsp;&nbsp;&nbsp; **(c)** $\displaystyle\int_{-\infty}^{0}e^{x}dx$

**4.** Calcule, se convergirem:

&nbsp;&nbsp;**(a)** $\displaystyle\int_0^{4}\frac{dx}{\sqrt{x}}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_0^{1}\ln x\thinspace dx$ &nbsp;&nbsp;&nbsp; **(c)** $\displaystyle\int_1^{2}\frac{dx}{x-1}$

**5.** Calcule $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$.

**6.** Mostre que $\displaystyle\int_0^{2}\frac{dx}{(x-1)^{2}}$ **diverge**, e explique por que a conta

$$\left[-\frac{1}{x-1}\right]_0^{2} = -1-1 = -2$$

&nbsp;&nbsp;está errada.

**7.** Determine para quais valores de $p$ cada integral converge:

&nbsp;&nbsp;**(a)** $\displaystyle\int_2^{\infty}\frac{dx}{x^{p}}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_0^{3}\frac{dx}{x^{p}}$

**8.** Use o **teste da comparação** para decidir:

&nbsp;&nbsp;**(a)** $\displaystyle\int_1^{\infty}\frac{dx}{x^3+1}$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_1^{\infty}\frac{2+\mathrm{sen}\thinspace x}{x}\thinspace dx$

**9.** Verdadeiro ou falso? Justifique.

&nbsp;&nbsp;**(a)** Se $\displaystyle\lim_{x\to\infty}f(x) = 0$, então $\displaystyle\int_1^{\infty}f$ converge.

&nbsp;&nbsp;**(b)** Se $\displaystyle\int_1^{\infty}f$ converge e $0\leqslant g\leqslant f$, então $\displaystyle\int_1^{\infty}g$ converge.

&nbsp;&nbsp;**(c)** $\displaystyle\int_{-\infty}^{\infty}x\thinspace dx = 0$, por simetria.

&nbsp;&nbsp;**(d)** Toda integral imprópria de uma função positiva ou converge, ou "vale $+\infty$".

---

## Bloco B · Consolidação

**10.** $\displaystyle\int_0^{\infty}x\thinspace e^{-x^2}dx$

**11.** $\displaystyle\int_2^{\infty}\frac{dx}{x\ln x}$

**12.** $\displaystyle\int_2^{\infty}\frac{dx}{x\big(\ln x\big)^{2}}$

**13.** $\displaystyle\int_0^{\infty}\frac{dx}{(1+x)^{3}}$

**14.** $\displaystyle\int_0^{1}\frac{dx}{\sqrt{1-x^2}}$

**15.** $\displaystyle\int_0^{\infty}\frac{x\thinspace dx}{1+x^2}$

**16.** $\displaystyle\int_{-1}^{1}\frac{dx}{\sqrt[3]{x}}$

&nbsp;&nbsp;*(Cuidado: a singularidade está no meio.)*

**17.** $\displaystyle\int_0^{\infty}e^{-x}\mathrm{sen}\thinspace x\thinspace dx$

**18.** Decida, por comparação:

&nbsp;&nbsp;**(a)** $\displaystyle\int_1^{\infty}\frac{\ln x}{x}\thinspace dx$ &nbsp;&nbsp;&nbsp; **(b)** $\displaystyle\int_1^{\infty}e^{-x^2}dx$

&nbsp;&nbsp;*(Em (b), compare com $e^{-x}$ para $x\geqslant1$.)*

---

## Bloco C · Desafio

**19.** Determine todos os $p$ para os quais $\displaystyle\int_0^{\infty}\frac{dx}{x^{p}}$ converge.

&nbsp;&nbsp;*(Sugestão: quebre em $x=1$ e use os dois teoremas.)*

**20.** Mostre que $\displaystyle\int_0^{1}x^{n}\ln x\thinspace dx = -\frac{1}{(n+1)^{2}}$ para todo inteiro $n\geqslant0$.

**21.** **A área e o volume da trombeta.** Reveja o exercício 21 da [Lista 5.4](lista-5.4-propostos.md) e reescreva os itens (a)–(c) como **integrais impróprias**, resolvendo-as com a notação desta seção.

**22.** Para quais valores de $a>0$ a integral

$$\int_0^{\infty}\frac{dx}{x^{a}+x^{2a}}$$

&nbsp;&nbsp;converge?

&nbsp;&nbsp;*(Analise separadamente o comportamento perto de $0$ e perto de $\infty$.)*

---

## ✅ Conferir

➡️ **[Gabarito da Lista 5.5](../gabaritos/gabarito-5.5.md)**

---

| ← Lista anterior | 🏠 Índice | Próximo → |
| :--- | :---: | ---: |
| [Lista 5.4](lista-5.4-propostos.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Revisão da Unidade 5](revisao-unidade-5.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
