# ✅ Gabarito — Lista 2.1

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 2.1](../exercicios/lista-2.1-propostos.md) · [Teoria 2.1](../2.1-conceito-e-nocao-intuitiva-de-limite.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $-1$ |
| 1 (b) | $-8$ |
| 1 (c) | $5$ |
| 1 (d) | $\dfrac{21}{4}$ |
| 1 (e) | $3$ |
| 2 (a) | $4$ |
| 2 (b) | $-1$ |
| 2 (c) | $-1$ |
| 2 (d) | $3$ |
| 3 (a) | $\dfrac14$ |
| 3 (b) | $6$ |
| 3 (c) | $\dfrac12$ |
| 4 (a) | $-\dfrac19$ |
| 4 (b) | $-\dfrac14$ |
| 5 (a) | $3$ |
| 5 (b) | $5$ |
| 5 (c) | Não coincidem — veja a Parte 2 |
| 6 (a) | $2$ |
| 6 (b) | $6$ |
| 6 (c) | $\dfrac14$ |
| 7 | (a) F · (b) F · (c) F · (d) V · (e) F |
| 8 (a) | $\dfrac13$ |
| 8 (b) | $\dfrac18$ |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $0$ |
| 10 | $32$ |
| 11 | $\dfrac12$ |
| 12 | $-\dfrac19$ |
| 13 | $3x^2$ |
| 14 | $12$ |
| 15 | $-\dfrac16$ |
| 16 | $\dfrac14$ |
| 17 | $2a$ |
| 18 | $\delta = \dfrac{\varepsilon}{3}$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | $\dfrac23$ |
| 20 | Demonstração — veja a Parte 2 |
| 21 | Não existe — veja a Parte 2 |
| 22 | $3$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

Todos são polinômios ou racionais com denominador não nulo no ponto: vale a **substituição direta**.

**(a)** $3(2)-7 = -1$

**(b)** $(-1)^2 + 4(-1) - 5 = 1 - 4 - 5 = -8$

**(c)** O limite de uma constante é a própria constante: $5$.

**(d)** $\dfrac{3^3 - 2 \cdot 3}{3+1} = \dfrac{27-6}{4} = \dfrac{21}{4}$

**(e)** $\sqrt{4+5} = \sqrt9 = 3$ (propriedade L6).

---

### Exercício 2

**(a)** $\dfrac{(x-2)(x+2)}{x-2} = x+2 \to 4$

**(b)** $\dfrac{(x+3)(x+2)}{x+3} = x+2 \to -3+2 = -1$

**(c)** $\dfrac{(x-1)(x-2)}{x-1} = x-2 \to 1-2 = -1$

**(d)** $\dfrac{x(x+3)}{x} = x+3 \to 3$

---

### Exercício 3

**(a)** Multiplicando pelo conjugado:

$$\frac{\sqrt{x+4}-2}{x} \cdot \frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \frac{(x+4)-4}{x\big(\sqrt{x+4}+2\big)} = \frac{1}{\sqrt{x+4}+2} \to \frac{1}{2+2} = \frac14$$

**(b)** Aqui a raiz está no **denominador**: multiplique pelo conjugado dele.

$$\frac{x-9}{\sqrt{x}-3} \cdot \frac{\sqrt{x}+3}{\sqrt{x}+3} = \frac{(x-9)\big(\sqrt{x}+3\big)}{x-9} = \sqrt{x}+3 \to 3+3 = 6$$

**(c)** $\dfrac{\sqrt{x}-1}{x-1} \cdot \dfrac{\sqrt{x}+1}{\sqrt{x}+1} = \dfrac{x-1}{(x-1)\big(\sqrt x + 1\big)} = \dfrac{1}{\sqrt x + 1} \to \dfrac12$

---

### Exercício 4

**(a)** Some as frações do numerador:

$$\frac{1}{x+3} - \frac13 = \frac{3 - (x+3)}{3(x+3)} = \frac{-x}{3(x+3)}$$

$$\frac{\frac{1}{x+3}-\frac13}{x} = \frac{-x}{3(x+3)} \cdot \frac1x = \frac{-1}{3(x+3)} \to \frac{-1}{9}$$

**(b)**

$$\frac1x - \frac12 = \frac{2-x}{2x} \ \Longrightarrow \ \frac{\frac1x-\frac12}{x-2} = \frac{2-x}{2x(x-2)} = \frac{-(x-2)}{2x(x-2)} = \frac{-1}{2x} \to -\frac14$$

> 💡 O sinal vem de $2-x = -(x-2)$. É o deslize mais comum deste exercício.

---

### Exercício 5

**(a)** Para **todo** $x \neq 2$ — que é o que o limite enxerga — vale $f(x) = x+1$. Logo

$$\lim_{x\to2} f(x) = \lim_{x\to2}(x+1) = 3$$

**(b)** $f(2) = 5$, por definição da função.

**(c)** **Não coincidem:** o limite é $3$ e o valor é $5$. A função tem um **ponto deslocado** em $x=2$ — o gráfico é a reta $y=x+1$ com um furo em $(2,3)$ e um ponto solto em $(2,5)$.

Isso significa que $f$ **não é contínua** em $x=2$. E a descontinuidade é **removível**: bastaria redefinir $f(2) = 3$ para consertá-la. O assunto é de [2.5](../2.5-continuidade-e-tipos-de-descontinuidade.md).

---

### Exercício 6

**(a)** $\dfrac{(1+h)^2-1}{h} = \dfrac{1+2h+h^2-1}{h} = \dfrac{h(2+h)}{h} = 2+h \to 2$

**(b)** $\dfrac{(3+h)^2-9}{h} = \dfrac{9+6h+h^2-9}{h} = 6+h \to 6$

**(c)** $\dfrac{\sqrt{4+h}-2}{h} \cdot \dfrac{\sqrt{4+h}+2}{\sqrt{4+h}+2} = \dfrac{h}{h\big(\sqrt{4+h}+2\big)} = \dfrac{1}{\sqrt{4+h}+2} \to \dfrac14$

> 💡 Os três são derivadas disfarçadas: $(x^2)' = 2x$ em $x=1$ e em $x=3$; $(\sqrt{x})' = \frac{1}{2\sqrt x}$ em $x=4$.

---

### Exercício 7

**(a) Falso.** O exemplo central da seção: $\frac{x^2-1}{x-1}$ não existe em $x=1$ e tem limite $2$ ali.

**(b) Falso.** No Exercício 5, o limite é $3$ e $f(2)=5$. (Quando os dois coincidem, a função é **contínua** no ponto — e aí sim vale a igualdade.)

**(c) Falso.** $\frac00$ é indeterminação: $\lim_{x\to0}\frac{x}{x}=1$, $\lim_{x\to0}\frac{x^2}{x}=0$, e $\lim_{x\to0}\frac{x}{x^2}$ nem existe. Todos dão $\frac00$ na substituição.

**(d) Verdadeiro.** É o Teorema da unicidade (2.1.1).

**(e) Falso.** A propriedade exige que **os dois limites existam**. Com $f(x) = \frac1x$ e $g(x) = -\frac1x$ em $a=0$, a soma é constante igual a $0$ (para $x\neq0$) e tem limite $0$, mas nenhuma das duas parcelas tem limite.

---

### Exercício 8

**(a)** Mudança de variável: $u = \sqrt[3]{1+x}$, logo $x = u^3 - 1$. Quando $x \to 0$, $u \to 1$.

$$\frac{\sqrt[3]{1+x}-1}{x} = \frac{u-1}{u^3-1} = \frac{u-1}{(u-1)(u^2+u+1)} = \frac{1}{u^2+u+1} \to \frac13$$

**(b)** $\dfrac{\sqrt x - 4}{x-16} \cdot \dfrac{\sqrt x + 4}{\sqrt x + 4} = \dfrac{x-16}{(x-16)\big(\sqrt x + 4\big)} = \dfrac{1}{\sqrt x + 4} \to \dfrac18$

---

## Bloco B · Consolidação

### Exercício 9

Substituindo dá $\frac00$. Fatore o numerador — note que $x=1$ é raiz **dupla**:

$$x^3-3x+2 = (x-1)(x^2+x-2) = (x-1)(x-1)(x+2) = (x-1)^2(x+2)$$

$$\frac{x^3-3x+2}{x^2-1} = \frac{(x-1)^2(x+2)}{(x-1)(x+1)} = \frac{(x-1)(x+2)}{x+1}$$

$$\lim_{x\to1}\frac{(x-1)(x+2)}{x+1} = \frac{0 \cdot 3}{2} = 0$$

> 💡 Depois do cancelamento ainda sobrou um fator $(x-1)$ no numerador — por isso a resposta é **zero**, e não um número não nulo. Quando a raiz é múltipla, o cancelamento não "zera" a indeterminação de uma vez.

---

### Exercício 10

$$x^4 - 16 = (x^2-4)(x^2+4) = (x-2)(x+2)(x^2+4)$$

$$\frac{x^4-16}{x-2} = (x+2)(x^2+4) \to 4 \cdot 8 = 32$$

---

### Exercício 11

$$
\begin{aligned}
\frac{\sqrt{4+x}-\sqrt{4-x}}{x}
&= \frac{\sqrt{4+x}-\sqrt{4-x}}{x} \cdot \frac{\sqrt{4+x}+\sqrt{4-x}}{\sqrt{4+x}+\sqrt{4-x}} \\
&= \frac{(4+x)-(4-x)}{x\big(\sqrt{4+x}+\sqrt{4-x}\big)} \\
&= \frac{2x}{x\big(\sqrt{4+x}+\sqrt{4-x}\big)} \\
&= \frac{2}{\sqrt{4+x}+\sqrt{4-x}}
\end{aligned}
$$

$$\lim_{x\to0}\frac{2}{\sqrt{4+x}+\sqrt{4-x}} = \frac{2}{2+2} = \frac12$$

---

### Exercício 12

$$\frac1x - \frac13 = \frac{3-x}{3x} \ \Longrightarrow \ \frac{\frac1x-\frac13}{x-3} = \frac{3-x}{3x(x-3)} = \frac{-(x-3)}{3x(x-3)} = \frac{-1}{3x}$$

$$\lim_{x\to3}\frac{-1}{3x} = -\frac19$$

---

### Exercício 13

Desenvolva o cubo, lembrando que aqui a variável é $h$:

$$(x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$$

$$\frac{(x+h)^3-x^3}{h} = \frac{3x^2h + 3xh^2 + h^3}{h} = \frac{h\big(3x^2+3xh+h^2\big)}{h} = 3x^2+3xh+h^2$$

$$\lim_{h\to0}\big(3x^2+3xh+h^2\big) = 3x^2$$

> 💡 Você acabou de deduzir que $(x^3)' = 3x^2$ — pela definição, sem usar regra nenhuma.

---

### Exercício 14

Soma de cubos: $x^3 + 8 = (x+2)(x^2-2x+4)$.

$$\frac{x^3+8}{x+2} = x^2-2x+4 \to 4+4+4 = 12$$

---

### Exercício 15

$$
\begin{aligned}
\frac{3-\sqrt{x+5}}{x-4}
&= \frac{3-\sqrt{x+5}}{x-4} \cdot \frac{3+\sqrt{x+5}}{3+\sqrt{x+5}} \\
&= \frac{9 - (x+5)}{(x-4)\big(3+\sqrt{x+5}\big)} \\
&= \frac{4-x}{(x-4)\big(3+\sqrt{x+5}\big)} \\
&= \frac{-1}{3+\sqrt{x+5}}
\end{aligned}
$$

$$\lim_{x\to4}\frac{-1}{3+\sqrt{x+5}} = \frac{-1}{3+3} = -\frac16$$

> ⚠️ O sinal negativo nasce de $4-x = -(x-4)$. Perdê-lo é o erro padrão desta questão.

---

### Exercício 16

$$\frac{\sqrt{x+3}-2}{x-1} \cdot \frac{\sqrt{x+3}+2}{\sqrt{x+3}+2} = \frac{(x+3)-4}{(x-1)\big(\sqrt{x+3}+2\big)} = \frac{x-1}{(x-1)\big(\sqrt{x+3}+2\big)} = \frac{1}{\sqrt{x+3}+2}$$

$$\lim_{x\to1}\frac{1}{\sqrt{x+3}+2} = \frac{1}{2+2} = \frac14$$

---

### Exercício 17

$$\frac{x^2-a^2}{x-a} = \frac{(x-a)(x+a)}{x-a} = x+a \qquad (x \neq a)$$

$$\lim_{x\to a}(x+a) = 2a$$

**Interpretação.** Este é o quociente de Newton de $f(x)=x^2$ no ponto $a$. O resultado $2a$ é a inclinação da reta tangente à parábola em $x=a$ — ou seja, $f'(a) = 2a$, que é a regra $(x^2)' = 2x$ aparecendo pela definição.

---

### Exercício 18

Seja $\varepsilon > 0$ dado. Analisando a quantidade que se quer tornar pequena:

$$\big\lvert (3x+2) - (-1) \big\rvert = \lvert 3x+3 \rvert = 3\,\lvert x+1 \rvert$$

Queremos $3\lvert x+1\rvert < \varepsilon$, isto é, $\lvert x+1 \rvert < \dfrac{\varepsilon}{3}$.

**Escolha** $\delta = \dfrac{\varepsilon}{3}$. Então, se $0 < \lvert x - (-1)\rvert < \delta$:

$$\big\lvert (3x+2)-(-1) \big\rvert = 3\lvert x+1 \rvert < 3\delta = \varepsilon$$

Como $\varepsilon > 0$ era arbitrário, $\lim_{x\to-1}(3x+2) = -1$. $\blacksquare$

---

## Bloco C · Desafio

### Exercício 19

Sejam $a = \sqrt[3]{1+x}$ e $b = \sqrt[3]{1-x}$. Da identidade $a^3-b^3 = (a-b)(a^2+ab+b^2)$, isolando a diferença:

$$a - b = \frac{a^3-b^3}{a^2+ab+b^2}$$

Como $a^3 = 1+x$ e $b^3 = 1-x$, temos $a^3-b^3 = 2x$. Logo

$$\frac{\sqrt[3]{1+x}-\sqrt[3]{1-x}}{x} = \frac{2x}{x\big(a^2+ab+b^2\big)} = \frac{2}{a^2+ab+b^2}$$

Quando $x \to 0$: $a \to 1$ e $b \to 1$, de modo que $a^2+ab+b^2 \to 3$.

$$\lim_{x\to0}\frac{\sqrt[3]{1+x}-\sqrt[3]{1-x}}{x} = \frac{2}{3}$$

> 💡 **Essa é a "racionalização" das raízes cúbicas.** O papel do conjugado $(\sqrt A + \sqrt B)$ no caso quadrático é feito aqui por $(a^2+ab+b^2)$. Vale a pena guardar a identidade.

---

### Exercício 20

**Tese.** $\lim\limits_{x\to1}\dfrac{x^n-1}{x-1} = n$, para todo inteiro $n \geqslant 1$.

**Demonstração.** Use a fatoração (que é a soma de uma progressão geométrica):

$$x^n - 1 = (x-1)\big(x^{n-1} + x^{n-2} + \cdots + x + 1\big)$$

Para verificar, basta distribuir: todos os termos se cancelam em cascata, sobrando $x^n - 1$.

Então, para $x \neq 1$:

$$\frac{x^n-1}{x-1} = x^{n-1} + x^{n-2} + \cdots + x + 1$$

É um polinômio, e vale a substituição direta. Em $x=1$, cada uma das $n$ parcelas vale $1$:

$$\lim_{x\to1}\frac{x^n-1}{x-1} = \underbrace{1 + 1 + \cdots + 1}_{n \text{ parcelas}} = n \qquad \blacksquare$$

> 💡 Este é o quociente de Newton de $f(x) = x^n$ em $x=1$: o resultado $n$ é a **regra da potência**, $(x^n)' = n x^{n-1}$, avaliada em $x=1$.

---

### Exercício 21

A função $\operatorname{sen}\frac1x$ oscila cada vez mais rápido conforme $x \to 0$. Para mostrar que o limite não existe, basta exibir **duas** aproximações de $0$ que levem a valores diferentes.

**Primeira aproximação.** Tome os pontos $x_k = \dfrac{1}{k\pi}$, com $k = 1, 2, 3, \ldots$ Eles tendem a $0$, e

$$\operatorname{sen}\frac{1}{x_k} = \operatorname{sen}(k\pi) = 0 \quad \text{para todo } k$$

Por esse caminho, os valores da função são **sempre $0$**.

**Segunda aproximação.** Tome $y_k = \dfrac{1}{\frac{\pi}{2} + 2k\pi}$. Eles também tendem a $0$, e

$$\operatorname{sen}\frac{1}{y_k} = \operatorname{sen}\left(\frac{\pi}{2} + 2k\pi\right) = 1 \quad \text{para todo } k$$

Por esse caminho, os valores são **sempre $1$**.

Se o limite existisse, ele teria de ser único (Teorema 2.1.1) — e todos os caminhos de aproximação levariam ao mesmo valor. Como um caminho dá $0$ e outro dá $1$, o limite **não existe**. $\blacksquare$

> 💡 **Guarde a técnica:** para provar que um limite **não** existe, exiba dois caminhos com destinos diferentes. É o mesmo raciocínio dos limites laterais de [2.2](../2.2-limites-laterais.md), só que com caminhos mais criativos.

---

### Exercício 22

Numerador e denominador zeram em $x=2$. Trate cada um separadamente, fazendo aparecer o fator $(x-2)$.

**Numerador** (conjugado):

$$\sqrt{x+2}-2 = \frac{(x+2)-4}{\sqrt{x+2}+2} = \frac{x-2}{\sqrt{x+2}+2}$$

**Denominador** (identidade do cubo, com $a = \sqrt[3]{x+6}$ e $b=2$):

$$\sqrt[3]{x+6}-2 = \frac{(x+6)-8}{\big(\sqrt[3]{x+6}\big)^2 + 2\sqrt[3]{x+6} + 4} = \frac{x-2}{\big(\sqrt[3]{x+6}\big)^2 + 2\sqrt[3]{x+6} + 4}$$

Dividindo um pelo outro, o fator $(x-2)$ cancela:

$$\frac{\sqrt{x+2}-2}{\sqrt[3]{x+6}-2} = \frac{\big(\sqrt[3]{x+6}\big)^2 + 2\sqrt[3]{x+6} + 4}{\sqrt{x+2}+2}$$

Agora substitua $x=2$ — numerador: $4 + 4 + 4 = 12$; denominador: $2+2 = 4$.

$$\lim_{x\to2}\frac{\sqrt{x+2}-2}{\sqrt[3]{x+6}-2} = \frac{12}{4} = 3$$

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 2.1](../exercicios/lista-2.1-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [2.1 · Teoria](../2.1-conceito-e-nocao-intuitiva-de-limite.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
