# 📝 Lista 2.5 — Continuidade e tipos de descontinuidade

> **Antes de começar:** leia a [teoria 2.5](../2.5-continuidade-e-tipos-de-descontinuidade.md).

**Em toda questão de continuidade, escreva os três testes separadamente:** $f(a)$ existe? o limite existe? são iguais? Responder só "é contínua" costuma valer metade da nota.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 8 | Todos |
| **B · Consolidação** | 9 a 18 | Todos |
| **C · Desafio** | 19 a 22 | Os que der |

---

## Bloco A · Fixação

**1.** Verifique, pelos três testes, se cada função é contínua em $x=1$:

**(a)**

$$
f(x) = \begin{cases}
x^2, & \text{se } x \neq 1 \\
1, & \text{se } x = 1
\end{cases}
$$

**(b)**

$$
g(x) = \begin{cases}
x+2, & \text{se } x \neq 1 \\
5, & \text{se } x = 1
\end{cases}
$$

**(c)**

$$
h(x) = \begin{cases}
x+1, & \text{se } x < 1 \\
2x, & \text{se } x \geqslant 1
\end{cases}
$$

**2.** Determine **onde** cada função é contínua:

&nbsp;&nbsp;**(a)** $f(x) = x^3-2x+1$ &nbsp;&nbsp;&nbsp; **(b)** $f(x) = \dfrac{x+1}{x-4}$ &nbsp;&nbsp;&nbsp; **(c)** $f(x) = \sqrt{x-2}$

&nbsp;&nbsp;**(d)** $f(x) = \ln(x+3)$ &nbsp;&nbsp;&nbsp; **(e)** $f(x) = \operatorname{tg} x$

**3.** Classifique a descontinuidade no ponto indicado:

&nbsp;&nbsp;**(a)** $\dfrac{x^2-1}{x-1}$ em $x=1$ &nbsp;&nbsp;&nbsp; **(b)** $\dfrac{1}{x-2}$ em $x=2$

&nbsp;&nbsp;**(c)** $\dfrac{\lvert x-3 \rvert}{x-3}$ em $x=3$ &nbsp;&nbsp;&nbsp; **(d)** $\operatorname{sen}\dfrac1x$ em $x=0$

**4.** Determine $k$ para que a função seja contínua:

**(a)**

$$
f(x) = \begin{cases}
\dfrac{x^2-25}{x-5}, & \text{se } x \neq 5 \\
k, & \text{se } x = 5
\end{cases}
$$

**(b)**

$$
f(x) = \begin{cases}
3x+k, & \text{se } x < 1 \\
x^2, & \text{se } x \geqslant 1
\end{cases}
$$

**5.** Calcule, justificando pela continuidade:

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to3}\sqrt{x^2+7}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to0} e^{\cos x}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x\to2}\ln\big(x^2+1\big)$ &nbsp;&nbsp;&nbsp; **(d)** $\lim\limits_{x\to\pi}\cos\dfrac{x}{2}$

**6.** Use o Teorema do Valor Intermediário para mostrar que $x^3+x-3=0$ tem uma raiz em $(1,\thinspace 2)$.

**7.** Verdadeiro ou falso? Justifique.

&nbsp;&nbsp;**(a)** Se $f$ é contínua em $a$, então $\lim\limits_{x\to a} f(x)$ existe.

&nbsp;&nbsp;**(b)** Se $\lim\limits_{x\to a} f(x)$ existe, então $f$ é contínua em $a$.

&nbsp;&nbsp;**(c)** Toda função polinomial é contínua em $\mathbb{R}$.

&nbsp;&nbsp;**(d)** Se $f$ é contínua em $[a,b]$ e $f(a)\cdot f(b) < 0$, a raiz em $(a,b)$ é única.

&nbsp;&nbsp;**(e)** Toda descontinuidade pode ser removida redefinindo-se $f(a)$.

**8.** Dê um exemplo (fórmula ou esboço) de uma função que seja:

&nbsp;&nbsp;**(a)** descontínua em $x=2$, com descontinuidade **removível**;

&nbsp;&nbsp;**(b)** descontínua em $x=0$, com **salto**;

&nbsp;&nbsp;**(c)** contínua em $\mathbb{R}$, mas com um "bico".

---

## Bloco B · Consolidação

**9.** Determine todos os pontos de descontinuidade de $f(x) = \dfrac{x^2-4}{x^2-5x+6}$ e classifique cada um.

**10.** Determine $a$ e $b$ para que $f$ seja contínua em $\mathbb{R}$:

$$
f(x) = \begin{cases}
x^2, & \text{se } x \leqslant 2 \\
ax+b, & \text{se } 2 < x < 5 \\
10, & \text{se } x \geqslant 5
\end{cases}
$$

**11.** Determine $k$ para que $f$ seja contínua em $x=0$:

$$
f(x) = \begin{cases}
\dfrac{\operatorname{sen} 3x}{x}, & \text{se } x \neq 0 \\
k, & \text{se } x = 0
\end{cases}
$$

**12.** Determine $k$ para que $f$ seja contínua em $x=0$:

$$
f(x) = \begin{cases}
\dfrac{\sqrt{x+4}-2}{x}, & \text{se } x \neq 0 \\
k, & \text{se } x = 0
\end{cases}
$$

**13.** Mostre que $x^4-3x+1=0$ tem **pelo menos duas** raízes reais.

**14.** Seja $f$ contínua em $[1,4]$, com $f(1)=3$ e $f(4)=-2$. Mostre que $f$ tem uma raiz em $(1,4)$ e que também assume o valor $1$ nesse intervalo.

**15.** A função abaixo é contínua em $x=0$? Classifique a descontinuidade, se houver.

$$
f(x) = \begin{cases}
x+1, & \text{se } x \leqslant 0 \\[2pt]
\dfrac1x, & \text{se } x > 0
\end{cases}
$$

**16.** Calcule $\lim\limits_{x\to0} \operatorname{sen}\left(\dfrac{\pi}{2}\cos x\right)$, justificando a passagem do limite para dentro do seno.

**17.** A função $f(x) = \lvert x^2-4 \rvert$ é contínua em $\mathbb{R}$? Em quais pontos o seu gráfico tem "bico"?

**18.** Analise a continuidade em $x=0$ de cada uma:

$$
f(x) = \begin{cases} x\operatorname{sen}\dfrac1x, & x \neq 0 \\ 0, & x=0 \end{cases}
\qquad\qquad
g(x) = \begin{cases} \operatorname{sen}\dfrac1x, & x \neq 0 \\ 0, & x=0 \end{cases}
$$

---

## Bloco C · Desafio

**19.** Mostre que **todo polinômio de grau ímpar** tem pelo menos uma raiz real.

**20.** Seja $f$ contínua em $[0,2]$ com $f(0) = f(2)$. Mostre que existe $c \in [0,1]$ tal que $f(c) = f(c+1)$.

**21.** A função

$$
f(x) = \begin{cases}
1, & \text{se } x \geqslant 0 \\
-1, & \text{se } x < 0
\end{cases}
$$

&nbsp;&nbsp;satisfaz $f(-1) = -1 < 0$ e $f(1) = 1 > 0$, mas **não tem raiz** em $(-1,\thinspace 1)$. Isso contradiz o Teorema do Valor Intermediário? Explique.

**22.** Determine $a$ e $b$ para que $f$ seja contínua em todo o seu domínio:

$$
f(x) = \begin{cases}
\dfrac{x^2-1}{x-1}, & \text{se } x < 1 \\[6pt]
ax+b, & \text{se } 1 \leqslant x \leqslant 3 \\[6pt]
\dfrac{\sqrt{x+1}-2}{x-3}, & \text{se } x > 3
\end{cases}
$$

---

## ✅ Conferir

➡️ **[Gabarito da Lista 2.5](../gabaritos/gabarito-2.5.md)**

Terminou? Feche a unidade com a ➡️ **[Revisão da Unidade 2](revisao-unidade-2.md)**.

---

| ← Lista anterior | 🏠 Índice | Revisão → |
| :--- | :---: | ---: |
| [Lista 2.4](lista-2.4-propostos.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Revisão da Unidade 2](revisao-unidade-2.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
