# 📝 Lista 4.2 — Teoremas de Rolle e do Valor Médio

> **Antes de começar:** leia a [teoria 4.2](../4.2-teoremas-de-rolle-e-do-valor-medio.md).

**Em toda questão com Rolle ou TVM, verifique as hipóteses explicitamente.** É parte da resposta, e vale nota.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 8 | Todos |
| **B · Consolidação** | 9 a 16 | Todos |
| **C · Desafio** | 17 a 20 | Os que der |

---

## Bloco A · Fixação

**1.** Verifique as hipóteses do **Teorema de Rolle** e encontre todos os $c$:

&nbsp;&nbsp;**(a)** $f(x) = x^2-4x+3$ em $[1,\thinspace 3]$

&nbsp;&nbsp;**(b)** $f(x) = x^2-2x$ em $[0,\thinspace 2]$

&nbsp;&nbsp;**(c)** $f(x) = \operatorname{sen} x$ em $[0,\thinspace \pi]$

**2.** Verifique as hipóteses do **TVM** e encontre todos os $c$:

&nbsp;&nbsp;**(a)** $f(x) = x^2$ em $[0,\thinspace 2]$

&nbsp;&nbsp;**(b)** $f(x) = x^3$ em $[-1,\thinspace 1]$

&nbsp;&nbsp;**(c)** $f(x) = \dfrac1x$ em $[1,\thinspace 2]$

**3.** Em cada caso, diga **qual hipótese falha** e por quê:

&nbsp;&nbsp;**(a)** Rolle para $f(x)=\lvert x\rvert$ em $[-2,\thinspace 2]$

&nbsp;&nbsp;**(b)** TVM para $f(x)=\dfrac1x$ em $[-1,\thinspace 1]$

&nbsp;&nbsp;**(c)** Rolle para $f(x)=x$ em $[0,\thinspace 2]$

**4.** Verdadeiro ou falso? Justifique.

&nbsp;&nbsp;**(a)** O Teorema de Rolle é um caso particular do TVM.

&nbsp;&nbsp;**(b)** O TVM garante que existe **exatamente um** $c$.

&nbsp;&nbsp;**(c)** Se $f'(x)=0$ em todo o domínio de $f$, então $f$ é constante.

&nbsp;&nbsp;**(d)** Se $f'(x)>0$ em um intervalo, então $f$ é crescente nesse intervalo.

**5.** Sabe-se que $f(2) = 5$ e que $f'(x) = 3$ para todo $x$. Determine $f(6)$.

**6.** Sabe-se que $f(0) = 1$ e que $1 \leqslant f'(x) \leqslant 3$ para todo $x$. Entre que valores está $f(2)$?

**7.** Mostre que $f(x) = x^5+2x+1$ tem **exatamente uma** raiz real.

**8.** Use o Corolário 2 do TVM para explicar por que a primitiva de $2x$ é $x^2 + C$, e não simplesmente $x^2$.

---

## Bloco B · Consolidação

**9.** Verifique o TVM para $f(x) = \sqrt x$ em $[0,\thinspace 4]$ e encontre o $c$.

&nbsp;&nbsp;*(Atenção: $f$ não é derivável em $x=0$. Isso impede aplicar o teorema?)*

**10.** Mostre que $\ln(1+x) < x$ para todo $x>0$.

**11.** Mostre que $\big\lvert \operatorname{sen} a - \operatorname{sen} b\big\rvert \leqslant \lvert a-b\rvert$ para todos $a,b \in \mathbb{R}$.

**12.** Seja $f$ derivável em $(a,b)$, com $f'(x) \neq 0$ para todo $x$ nesse intervalo. Mostre que $f$ tem **no máximo uma** raiz em $(a,b)$.

**13.** Dois corredores partem juntos e chegam **empatados** ao final da prova. Mostre que em algum instante eles tiveram exatamente a **mesma velocidade**.

**14.** Encontre todos os $c$ do TVM para $f(x) = x^3-3x+2$ em $[-2,\thinspace 2]$.

**15.** Mostre que $f(x) = x^3+x-4$ tem exatamente uma raiz real e localize-a entre dois inteiros consecutivos.

**16.** Seja $f$ contínua em $[0,2]$, derivável em $(0,2)$, com $f(0)=0$ e $f'(x) \leqslant 2$ para todo $x$. Mostre que $f(2) \leqslant 4$.

---

## Bloco C · Desafio

**17.** **Demonstre o TVM a partir do Teorema de Rolle.**

&nbsp;&nbsp;*(Sugestão: aplique Rolle à função $g(x) = f(x) - r(x)$, em que $r$ é a reta secante que liga $\big(a,f(a)\big)$ a $\big(b,f(b)\big)$.)*

**18.** Seja $f$ derivável num intervalo $I$, com $\lvert f'(x)\rvert \leqslant M$ para todo $x \in I$. Mostre que

$$\big\lvert f(x)-f(y)\big\rvert \leqslant M\thinspace \lvert x-y\rvert \qquad \text{para todos } x,y \in I$$

&nbsp;&nbsp;*(Funções com essa propriedade são chamadas de **lipschitzianas**.)*

**19.** Seja $f$ derivável em $\mathbb{R}$, com $f(0)=0$ e $f'(x) \leqslant 1$ para todo $x$. Mostre que $f(x) \leqslant x$ para todo $x \geqslant 0$.

**20.** O **Teorema do Valor Médio de Cauchy** afirma: se $f$ e $g$ são contínuas em $[a,b]$, deriváveis em $(a,b)$ e $g'(x)\neq0$, então existe $c \in (a,b)$ com

$$\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}$$

&nbsp;&nbsp;Verifique-o para $f(x)=x^2$ e $g(x)=x^3$ em $[1,\thinspace 2]$, encontrando o $c$.

---

## ✅ Conferir

➡️ **[Gabarito da Lista 4.2](../gabaritos/gabarito-4.2.md)**

---

| ← Lista anterior | 🏠 Índice | Próxima lista → |
| :--- | :---: | ---: |
| [Lista 4.1](lista-4.1-propostos.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Lista 4.3](lista-4.3-propostos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
