# 📝 Lista 2.1 — Conceito de limite e teoremas operatórios

> **Antes de começar:** leia a [teoria 2.1](../2.1-conceito-e-nocao-intuitiva-de-limite.md).

**Lembrete que vale ponto:** o símbolo $\lim$ acompanha **toda** linha da resolução, até você finalmente calculá-lo.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 8 | Todos |
| **B · Consolidação** | 9 a 18 | Todos |
| **C · Desafio** | 19 a 22 | Os que der |

---

## Bloco A · Fixação

**1.** Calcule por substituição direta:

&nbsp;&nbsp;**(a)** $\lim\limits_{x \to 2} (3x-7)$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x \to -1} (x^2+4x-5)$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x \to 0} 5$

&nbsp;&nbsp;**(d)** $\lim\limits_{x \to 3} \dfrac{x^3-2x}{x+1}$ &nbsp;&nbsp;&nbsp; **(e)** $\lim\limits_{x \to 4} \sqrt{x+5}$

**2.** Calcule, fatorando:

&nbsp;&nbsp;**(a)** $\lim\limits_{x \to 2} \dfrac{x^2-4}{x-2}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x \to -3} \dfrac{x^2+5x+6}{x+3}$

&nbsp;&nbsp;**(c)** $\lim\limits_{x \to 1} \dfrac{x^2-3x+2}{x-1}$ &nbsp;&nbsp;&nbsp; **(d)** $\lim\limits_{x \to 0} \dfrac{x^2+3x}{x}$

**3.** Calcule, racionalizando:

&nbsp;&nbsp;**(a)** $\lim\limits_{x \to 0} \dfrac{\sqrt{x+4}-2}{x}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x \to 9} \dfrac{x-9}{\sqrt{x}-3}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x \to 1} \dfrac{\sqrt{x}-1}{x-1}$

**4.** Calcule, somando as frações primeiro:

&nbsp;&nbsp;**(a)** $\lim\limits_{x \to 0} \dfrac{\frac{1}{x+3} - \frac{1}{3}}{x}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x \to 2} \dfrac{\frac{1}{x} - \frac{1}{2}}{x-2}$

**5.** Seja

$$
f(x) = \begin{cases}
x+1, & \text{se } x \neq 2 \\
5, & \text{se } x = 2
\end{cases}
$$

&nbsp;&nbsp;**(a)** Calcule $\lim\limits_{x \to 2} f(x)$. &nbsp;&nbsp;&nbsp; **(b)** Calcule $f(2)$. &nbsp;&nbsp;&nbsp; **(c)** Os dois coincidem? Explique o que isso diz sobre a função.

**6.** Calcule os quocientes de Newton:

&nbsp;&nbsp;**(a)** $\lim\limits_{h \to 0} \dfrac{(1+h)^2-1}{h}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{h \to 0} \dfrac{(3+h)^2-9}{h}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{h \to 0} \dfrac{\sqrt{4+h}-2}{h}$

**7.** Verdadeiro ou falso? Justifique.

&nbsp;&nbsp;**(a)** Se $f(a)$ não existe, então $\lim\limits_{x\to a} f(x)$ não existe.

&nbsp;&nbsp;**(b)** Se $\lim\limits_{x\to a} f(x) = L$, então $f(a) = L$.

&nbsp;&nbsp;**(c)** A indeterminação $\frac00$ sempre resulta em $1$.

&nbsp;&nbsp;**(d)** Se o limite existe, ele é único.

&nbsp;&nbsp;**(e)** $\lim\limits_{x\to a}\big[f(x)+g(x)\big] = \lim\limits_{x\to a} f(x) + \lim\limits_{x\to a} g(x)$, quaisquer que sejam $f$ e $g$.

**8.** Calcule:

&nbsp;&nbsp;**(a)** $\lim\limits_{x \to 0} \dfrac{\sqrt[3]{1+x}-1}{x}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x \to 16} \dfrac{\sqrt{x}-4}{x-16}$

---

## Bloco B · Consolidação

**9.** $\lim\limits_{x \to 1} \dfrac{x^3-3x+2}{x^2-1}$

**10.** $\lim\limits_{x \to 2} \dfrac{x^4-16}{x-2}$

**11.** $\lim\limits_{x \to 0} \dfrac{\sqrt{4+x}-\sqrt{4-x}}{x}$

**12.** $\lim\limits_{x \to 3} \dfrac{\frac{1}{x}-\frac{1}{3}}{x-3}$

**13.** $\lim\limits_{h \to 0} \dfrac{(x+h)^3 - x^3}{h}$ &nbsp;&nbsp;*(aqui $x$ é fixo e $h$ é a variável)*

**14.** $\lim\limits_{x \to -2} \dfrac{x^3+8}{x+2}$

**15.** $\lim\limits_{x \to 4} \dfrac{3-\sqrt{x+5}}{x-4}$

**16.** $\lim\limits_{x \to 1} \dfrac{\sqrt{x+3}-2}{x-1}$

**17.** Seja $a$ uma constante. Calcule $\lim\limits_{x \to a} \dfrac{x^2-a^2}{x-a}$ e interprete o resultado.

**18.** Demonstre, pela definição, que $\lim\limits_{x \to -1} (3x+2) = -1$.

---

## Bloco C · Desafio

**19.** $\lim\limits_{x \to 0} \dfrac{\sqrt[3]{1+x} - \sqrt[3]{1-x}}{x}$

&nbsp;&nbsp;*(Sugestão: use $a^3-b^3 = (a-b)(a^2+ab+b^2)$ para isolar $a-b$.)*

**20.** Mostre que, para todo inteiro $n \geqslant 1$,

$$\lim_{x \to 1} \frac{x^n-1}{x-1} = n$$

**21.** Mostre que $\lim\limits_{x \to 0} \operatorname{sen}\dfrac{1}{x}$ **não existe**, exibindo duas maneiras de $x$ se aproximar de $0$ que produzem valores diferentes.

**22.** $\lim\limits_{x \to 2} \dfrac{\sqrt{x+2}-2}{\sqrt[3]{x+6}-2}$

---

## ✅ Conferir

➡️ **[Gabarito da Lista 2.1](../gabaritos/gabarito-2.1.md)**

---

| ← Teoria | 🏠 Índice | Próxima lista → |
| :--- | :---: | ---: |
| [2.1 · Teoria](../2.1-conceito-e-nocao-intuitiva-de-limite.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Lista 2.2](lista-2.2-propostos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
