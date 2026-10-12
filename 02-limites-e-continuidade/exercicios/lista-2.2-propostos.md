# 📝 Lista 2.2 — Limites laterais

> **Antes de começar:** leia a [teoria 2.2](../2.2-limites-laterais.md). Em todo exercício com módulo, o primeiro passo é **abrir o módulo** conforme o sinal do que está dentro.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 8 | Todos |
| **B · Consolidação** | 9 a 18 | Todos |
| **C · Desafio** | 19 a 22 | Os que der |

---

## Bloco A · Fixação

**1.** Seja

$$
f(x) = \begin{cases}
3x-1, & \text{se } x < 2 \\
x+3, & \text{se } x \geqslant 2
\end{cases}
$$

&nbsp;&nbsp;Calcule $\lim\limits_{x\to2^{-}} f(x)$, $\lim\limits_{x\to2^{+}} f(x)$, $\lim\limits_{x\to2} f(x)$ e $f(2)$.

**2.** Seja

$$
g(x) = \begin{cases}
x^2, & \text{se } x \leqslant 1 \\
2x, & \text{se } x > 1
\end{cases}
$$

&nbsp;&nbsp;Calcule os limites laterais em $x=1$ e decida se $\lim\limits_{x\to1} g(x)$ existe.

**3.** Calcule:

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to0^{-}} \dfrac{\lvert x \rvert}{x}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to0^{+}} \dfrac{\lvert x \rvert}{x}$

&nbsp;&nbsp;**(c)** $\lim\limits_{x\to5^{+}} \dfrac{\lvert x-5 \rvert}{x-5}$ &nbsp;&nbsp;&nbsp; **(d)** $\lim\limits_{x\to5^{-}} \dfrac{\lvert x-5 \rvert}{x-5}$

**4.** Sendo $\lfloor x \rfloor$ a função maior inteiro, calcule:

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to3^{-}} \lfloor x \rfloor$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to3^{+}} \lfloor x \rfloor$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x\to2{,}5} \lfloor x \rfloor$ &nbsp;&nbsp;&nbsp; **(d)** $\lfloor 3 \rfloor$

**5.** Calcule, se existirem:

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to0^{+}} \sqrt{x}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to2^{+}} \sqrt{x-2}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x\to2^{-}} \sqrt{x-2}$ &nbsp;&nbsp;&nbsp; **(d)** $\lim\limits_{x\to2} \sqrt{x-2}$

**6.** Determine $k$ para que $\lim\limits_{x\to2} f(x)$ exista, onde

$$
f(x) = \begin{cases}
x+k, & \text{se } x < 2 \\
3x-4, & \text{se } x \geqslant 2
\end{cases}
$$

**7.** Verdadeiro ou falso? Justifique.

&nbsp;&nbsp;**(a)** Se os dois limites laterais existem, então o limite existe.

&nbsp;&nbsp;**(b)** Se o limite existe, então os dois laterais existem e são iguais.

&nbsp;&nbsp;**(c)** $x \to a^{+}$ significa que $x$ assume valores menores que $a$.

&nbsp;&nbsp;**(d)** Se $f(a)$ existe, então $\lim\limits_{x\to a} f(x)$ existe.

**8.** Esboce o gráfico e calcule os limites laterais em $x=0$:

$$
f(x) = \begin{cases}
x^2, & \text{se } x < 0 \\
x+1, & \text{se } x \geqslant 0
\end{cases}
$$

---

## Bloco B · Consolidação

**9.** Calcule $\lim\limits_{x\to1^{-}} \dfrac{x^2-1}{\lvert x-1 \rvert}$ e $\lim\limits_{x\to1^{+}} \dfrac{x^2-1}{\lvert x-1 \rvert}$.

**10.** Calcule $\lim\limits_{x\to0^{-}} \dfrac{x - \lvert x \rvert}{x}$ e $\lim\limits_{x\to0^{+}} \dfrac{x - \lvert x \rvert}{x}$.

**11.** Determine $a$ para que $\lim\limits_{x\to-1} f(x)$ exista, onde

$$
f(x) = \begin{cases}
ax^2+1, & \text{se } x < -1 \\
x-3, & \text{se } x \geqslant -1
\end{cases}
$$

**12.** Seja

$$
f(x) = \begin{cases}
\sqrt{4-x^2}, & \text{se } -2 \leqslant x \leqslant 2 \\
x-2, & \text{se } x > 2
\end{cases}
$$

&nbsp;&nbsp;Calcule os limites laterais em $x=2$ e decida se o limite existe. E em $x=-2$?

**13.** Calcule os limites laterais de $\dfrac{\lvert x-3 \rvert}{x^2-5x+6}$ em $x=3$.

**14.** Seja

$$
f(x) = \begin{cases}
x^2-4, & \text{se } x < 0 \\
\lvert x \rvert, & \text{se } 0 \leqslant x < 3 \\
12-3x, & \text{se } x \geqslant 3
\end{cases}
$$

&nbsp;&nbsp;Determine em quais dos pontos $x=0$ e $x=3$ o limite existe.

**15.** Determine $a$ e $b$ para que o limite exista em $x=0$ **e** em $x=2$, onde

$$
f(x) = \begin{cases}
x+a, & \text{se } x < 0 \\
x^2+b, & \text{se } 0 \leqslant x < 2 \\
2x, & \text{se } x \geqslant 2
\end{cases}
$$

**16.** Calcule $\lim\limits_{x\to0^{+}} \left( \dfrac1x - \dfrac{1}{\lvert x \rvert} \right)$ e $\lim\limits_{x\to0^{-}} \left( \dfrac1x - \dfrac{1}{\lvert x \rvert} \right)$.

**17.** Seja $f(x) = x - \lfloor x \rfloor$ (a **parte fracionária** de $x$). Calcule os limites laterais em $x=2$ e esboce o gráfico em $[0,3]$.

**18.** Determine todos os pontos em que $f(x) = \lfloor x \rfloor$ **não** tem limite. Justifique.

---

## Bloco C · Desafio

**19.** Seja $f(x) = \lvert x-1 \rvert + \lvert x-3 \rvert$. Calcule os limites laterais em $x=1$ e em $x=3$, e conclua que o limite existe nos dois pontos.

**20.** Determine $a$ e $b$ para que $\lim\limits_{x\to1} f(x)$ exista **e** seja igual a $f(1)$, onde

$$
f(x) = \begin{cases}
ax+b, & \text{se } x < 1 \\
3, & \text{se } x = 1 \\
bx^2 - a, & \text{se } x > 1
\end{cases}
$$

**21.** Sejam $f(x) = \lfloor x \rfloor$ e $g(x) = x - \lfloor x \rfloor$. Mostre que **nenhuma** das duas tem limite nos inteiros, mas que $f+g$ tem limite em **todo** ponto.

**22.** Seja $f(x) = \dfrac{x}{\lvert x \rvert + x}$. Determine o domínio de $f$ e calcule os limites laterais em $x=0$ que fizerem sentido.

---

## ✅ Conferir

➡️ **[Gabarito da Lista 2.2](../gabaritos/gabarito-2.2.md)**

---

| ← Lista anterior | 🏠 Índice | Próxima lista → |
| :--- | :---: | ---: |
| [Lista 2.1](lista-2.1-propostos.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Lista 2.3](lista-2.3-propostos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
