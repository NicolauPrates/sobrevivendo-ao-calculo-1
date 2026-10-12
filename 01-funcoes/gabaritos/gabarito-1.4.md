# ✅ Gabarito — Lista 1.4

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 1.4](../exercicios/lista-1.4-propostos.md) · [Teoria 1.4](../1.4-injetoras-sobrejetoras-bijetoras-e-inversas.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | injetora |
| 1 (b) | não é injetora |
| 1 (c) | injetora |
| 1 (d) | não é injetora |
| 1 (e) | injetora |
| 2 (a) | sobrejetora |
| 2 (b) | não é sobrejetora |
| 2 (c) | sobrejetora |
| 2 (d) | não é sobrejetora |
| 3 (a) | $f^{-1}(x) = x-7$, $D=\mathbb{R}$ |
| 3 (b) | $f^{-1}(x) = \dfrac{x+1}{4}$, $D=\mathbb{R}$ |
| 3 (c) | $f^{-1}(x) = \sqrt[3]{x}$, $D=\mathbb{R}$ |
| 3 (d) | $f^{-1}(x) = \dfrac1x$, $D=\mathbb{R}\setminus\lbrace 0 \rbrace$ |
| 3 (e) | $f^{-1}(x) = \sqrt[5]{x-2}$, $D=\mathbb{R}$ |
| 4 (a) | $2$ |
| 4 (b) | $3$ |
| 4 (c) | $10$ |
| 5 (a) | sim |
| 5 (b) | sim |
| 5 (c) | sim |
| 5 (d) | não |
| 6 (a) | $\dfrac{\pi}{2}$ |
| 6 (b) | $-\dfrac{\pi}{6}$ |
| 6 (c) | $\dfrac{\pi}{2}$ |
| 6 (d) | $\dfrac{\pi}{4}$ |
| 6 (e) | $\pi$ |
| 7 (a) | crescente → injetora |
| 7 (b) | crescente → injetora |
| 7 (c) | não é monótona → não é injetora |
| 7 (d) | decrescente → injetora |
| 8 | (a) F · (b) V · (c) V · (d) F · (e) V |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $f^{-1}(x) = \dfrac{x+3}{2-x}$, $D = \mathbb{R}\setminus\lbrace 2 \rbrace$ |
| 10 | Com $f : [3,+\infty) \to [-4,+\infty)$: $f^{-1}(x) = 3 + \sqrt{x+4}$, $D=[-4,+\infty)$ |
| 11 | $f^{-1}(x) = \dfrac{(x-4)^2+1}{2}$; $D(f) = \left[\frac12,+\infty\right)$, $D(f^{-1}) = [4,+\infty)$ |
| 12 | $f^{-1}(x) = 2 + \ln x$; $D(f)=\mathbb{R}$, $D(f^{-1}) = (0,+\infty)$ |
| 13 | $f^{-1}(x) = e^{x+1} - 3$; $D(f) = (-3,+\infty)$, $D(f^{-1}) = \mathbb{R}$ |
| 14 (a) | $\dfrac{\pi}{3}$ |
| 14 (b) | $\dfrac{5\pi}{6}$ |
| 14 (c) | $-\dfrac{\pi}{4}$ |
| 14 (d) | $0{,}3$ |
| 15 | Demonstração — veja a Parte 2 |
| 16 | $(f\circ g)^{-1}(x) = \dfrac{x-2}{3} = \big(g^{-1}\circ f^{-1}\big)(x)$ |
| 17 | $f^{-1}(1)=3$; $f^{-1}(3)=1$; $f^{-1}(5)=2$; $f^{-1}(f(2))=2$ |
| 18 | $k \geqslant -2$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | Demonstração — veja a Parte 2 |
| 20 | $\operatorname{Im}(f) = (-1,\thinspace 1)$ e $f^{-1}(x) = \dfrac{x}{1-\lvert x \rvert}$, $D = (-1,1)$ |
| 21 | Demonstração — veja a Parte 2 |
| 22 | $f = f^{-1}$; o gráfico é simétrico em relação à reta $y=x$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** Suponha $f(x_1)=f(x_2)$: $5x_1+2 = 5x_2+2 \Rightarrow x_1 = x_2$. **Injetora.**

**(b)** Contraexemplo: $f(1) = 0 = f(-1)$, com $1 \neq -1$. **Não é injetora.**

**(c)** Suponha $x_1^3 + 1 = x_2^3 + 1 \Rightarrow x_1^3 = x_2^3 \Rightarrow x_1 = x_2$ (a raiz cúbica é única em $\mathbb{R}$). **Injetora.**

**(d)** Contraexemplo: $f(-3) = 3 = f(3)$. **Não é injetora.**

**(e)** Suponha $\dfrac{1}{x_1} = \dfrac{1}{x_2}$. Como nenhum dos dois é zero, pode-se inverter: $x_1 = x_2$. **Injetora.**

---

### Exercício 2

**(a)** $\operatorname{Im} = \mathbb{R}$: dado qualquer $y$, basta tomar $x = \frac{y+6}{2}$. **Sobrejetora.**

**(b)** $\operatorname{Im} = [1,+\infty) \neq \mathbb{R}$: nenhum $x$ produz $y=0$. **Não é sobrejetora.**

**(c)** $\operatorname{Im} = \mathbb{R}$: dado $y$, tome $x = \sqrt[3]{y}$. **Sobrejetora.**

**(d)** $\operatorname{Im} = (0,+\infty) \neq \mathbb{R}$: a exponencial nunca é negativa nem zero. **Não é sobrejetora.**

---

### Exercício 3

**(a)** $y = x+7 \Rightarrow x = y-7$. $f^{-1}(x) = x-7$, $D=\mathbb{R}$.

**(b)** $y = 4x-1 \Rightarrow x = \dfrac{y+1}{4}$. $f^{-1}(x) = \dfrac{x+1}{4}$, $D=\mathbb{R}$.

**(c)** $y = x^3 \Rightarrow x = \sqrt[3]{y}$. $f^{-1}(x) = \sqrt[3]{x}$, $D=\mathbb{R}$.

**(d)** $y = \dfrac1x \Rightarrow x = \dfrac1y$. $f^{-1}(x) = \dfrac1x$, $D=\mathbb{R}\setminus\lbrace 0 \rbrace$ — a função é **a sua própria inversa**.

**(e)** $y = x^5+2 \Rightarrow x = \sqrt[5]{y-2}$. $f^{-1}(x) = \sqrt[5]{x-2}$, $D=\mathbb{R}$.

---

### Exercício 4

**(a)** $f(2)=7$ significa que $f$ leva $2$ em $7$; a inversa faz o caminho de volta: $f^{-1}(7) = 2$.

**(b)** $f^{-1}(3) = -1$ significa que $f(-1) = 3$.

**(c)** $f^{-1}\big(f(10)\big) = 10$, pela identidade fundamental.

---

### Exercício 5

**(a)** $f(g(x)) = 3 \cdot \frac{x}{3} = x$ e $g(f(x)) = \frac{3x}{3} = x$. **São inversas.**

**(b)** $f(g(x)) = (x-4)+4 = x$ e $g(f(x)) = (x+4)-4 = x$. **São inversas.**

**(c)** Em $[0,+\infty)$: $f(g(x)) = (\sqrt{x})^2 = x$ e $g(f(x)) = \sqrt{x^2} = \lvert x \rvert = x$ (pois $x \geqslant 0$). **São inversas.**

> ⚠️ A restrição é essencial: em $\mathbb{R}$ teríamos $\sqrt{x^2} = \lvert x \rvert \neq x$ para $x<0$, e a identidade falharia.

**(d)** $f(g(x)) = 2 \cdot \dfrac{1}{2x+1} + 1 = \dfrac{2}{2x+1} + 1 \neq x$. **Não são inversas** — $g$ é o *inverso multiplicativo* de $f$, e não a função inversa.

---

### Exercício 6

**(a)** $\operatorname{arcsen} 1 = \dfrac{\pi}{2}$ &nbsp;&nbsp; **(b)** $\operatorname{arcsen}\left(-\frac12\right) = -\dfrac{\pi}{6}$ &nbsp;&nbsp; **(c)** $\arccos 0 = \dfrac{\pi}{2}$

**(d)** $\operatorname{arctg} 1 = \dfrac{\pi}{4}$ &nbsp;&nbsp; **(e)** $\arccos(-1) = \pi$

> 💡 Em (b), a resposta é negativa porque o arco-seno devolve valores em $\left[-\frac\pi2,\frac\pi2\right]$ — e nesse intervalo o ângulo com seno $-\frac12$ é $-\frac{\pi}{6}$. Já em (e), o arco-cosseno vive em $[0,\pi]$, e por isso a resposta é $\pi$, e não $-\pi$.

---

### Exercício 7

**(a)** $e^x$ é estritamente crescente em $\mathbb{R}$ → **injetora**.

**(b)** $\ln x$ é estritamente crescente em $(0,+\infty)$ → **injetora**.

**(c)** $\cos x$ sobe e desce indefinidamente — não é monótona. E de fato não é injetora: $\cos 0 = \cos 2\pi = 1$.

**(d)** $-3x+5$ é estritamente decrescente → **injetora**.

> [!NOTE]
> A implicação vale em um só sentido: **monótona ⟹ injetora**, mas não o contrário. A função $f(x) = \frac1x$ é injetora em $\mathbb{R}\setminus\lbrace 0 \rbrace$ e **não** é monótona nesse conjunto (ela decresce em cada ramo, mas $f(-1) = -1 < 1 = f(1)$ com $-1 < 1$).

---

### Exercício 8

**(a) Falso.** $f : \mathbb{R} \to \mathbb{R}$, $f(x) = e^x$, é injetora mas não é sobrejetora.

**(b) Verdadeiro.** A inversa "desfaz" a correspondência um-a-um, que continua um-a-um no sentido contrário.

**(c) Verdadeiro.** É a Propriedade 1.4.2.

**(d) Falso.** $f^{-1}$ é a função inversa, não o inverso multiplicativo. Para $f(x)=x+3$: $f^{-1}(x) = x-3$, enquanto $\frac{1}{f(x)} = \frac{1}{x+3}$.

**(e) Verdadeiro.** Refletir um gráfico crescente na reta $y=x$ produz outro gráfico crescente.

---

## Bloco B · Consolidação

### Exercício 9

**Injetividade.** Suponha $f(x_1) = f(x_2)$:

$$\frac{2x_1-3}{x_1+1} = \frac{2x_2-3}{x_2+1}$$

Multiplicando em cruz (é uma igualdade, e os denominadores não são nulos):

$$(2x_1-3)(x_2+1) = (2x_2-3)(x_1+1)$$
$$2x_1x_2 + 2x_1 - 3x_2 - 3 = 2x_1x_2 + 2x_2 - 3x_1 - 3$$

Cancelando $2x_1x_2$ e $-3$ dos dois lados:

$$2x_1 - 3x_2 = 2x_2 - 3x_1 \ \Longrightarrow \ 5x_1 = 5x_2 \ \Longrightarrow \ x_1 = x_2$$

**Injetora.** $\blacksquare$

**Inversa.**

$$y = \frac{2x-3}{x+1} \ \Longrightarrow \ y(x+1) = 2x-3 \ \Longrightarrow \ yx + y = 2x - 3$$
$$x(y-2) = -3 - y \ \Longrightarrow \ x = \frac{-3-y}{y-2} = \frac{y+3}{2-y}$$

$$f^{-1}(x) = \frac{x+3}{2-x}, \qquad D(f^{-1}) = \mathbb{R}\setminus\lbrace 2 \rbrace$$

*Conferência:* $f(0) = -3$ e $f^{-1}(-3) = \frac{0}{5} = 0$ ✔.

---

### Exercício 10

Completando o quadrado:

$$f(x) = x^2-6x+5 = (x-3)^2 - 4$$

O vértice está em $(3,\thinspace -4)$. Restringindo ao ramo **direito**, onde a função cresce:

$$f : [3,\thinspace +\infty) \longrightarrow [-4,\thinspace +\infty)$$

Agora é bijetora. Invertendo:

$$y = (x-3)^2 - 4 \ \Longrightarrow \ (x-3)^2 = y+4 \ \Longrightarrow \ x - 3 = +\sqrt{y+4}$$

(sinal positivo, pois restringimos a $x \geqslant 3$)

$$f^{-1}(x) = 3 + \sqrt{x+4}, \qquad D(f^{-1}) = [-4,\thinspace +\infty)$$

> 💡 A restrição ao ramo esquerdo, $(-\infty,3]$, também seria válida — e daria $f^{-1}(x) = 3 - \sqrt{x+4}$. O que não se pode é deixar de **declarar** a escolha.

---

### Exercício 11

**Domínio e imagem de $f$:** $2x-1 \geqslant 0 \Rightarrow D(f) = \left[\frac12,+\infty\right)$. Como $\sqrt{2x-1} \geqslant 0$, tem-se $f(x) \geqslant 4$, logo $\operatorname{Im}(f) = [4,+\infty)$.

**Invertendo:**

$$y - 4 = \sqrt{2x-1}$$

Elevando ao quadrado (legítimo porque $y-4 \geqslant 0$):

$$(y-4)^2 = 2x - 1 \ \Longrightarrow \ x = \frac{(y-4)^2+1}{2}$$

$$f^{-1}(x) = \frac{(x-4)^2+1}{2}, \qquad D(f^{-1}) = [4,\thinspace +\infty), \qquad \operatorname{Im}(f^{-1}) = \left[\tfrac12,\thinspace +\infty\right)$$

---

### Exercício 12

$D(f) = \mathbb{R}$ e $\operatorname{Im}(f) = (0,+\infty)$, pois a exponencial é sempre positiva.

$$y = e^{x-2} \ \Longrightarrow \ \ln y = x - 2 \ \Longrightarrow \ x = 2 + \ln y$$

$$f^{-1}(x) = 2 + \ln x, \qquad D(f^{-1}) = (0,\thinspace +\infty)$$

---

### Exercício 13

$D(f)$: o logaritmando precisa ser positivo, $x + 3 > 0 \Rightarrow D(f) = (-3,+\infty)$. Como $\ln$ percorre todo $\mathbb{R}$, $\operatorname{Im}(f) = \mathbb{R}$.

$$y = \ln(x+3) - 1 \ \Longrightarrow \ y + 1 = \ln(x+3) \ \Longrightarrow \ e^{y+1} = x+3 \ \Longrightarrow \ x = e^{y+1} - 3$$

$$f^{-1}(x) = e^{x+1} - 3, \qquad D(f^{-1}) = \mathbb{R}, \qquad \operatorname{Im}(f^{-1}) = (-3,\thinspace +\infty)$$

> 💡 Note a troca completa: o domínio de $f$ virou a imagem de $f^{-1}$, e vice-versa. Isso é um bom teste de consistência da sua resposta.

---

### Exercício 14

**(a)** $\operatorname{sen}\dfrac{2\pi}{3} = \dfrac{\sqrt3}{2}$. Como $\dfrac{2\pi}{3} \notin \left[-\frac\pi2,\frac\pi2\right]$, **não** se pode cancelar direto. O arco-seno devolve o ângulo da restrição com esse seno:

$$\operatorname{arcsen}\frac{\sqrt3}{2} = \frac{\pi}{3}$$

**(b)** $\cos\dfrac{7\pi}{6} = -\dfrac{\sqrt3}{2}$. O arco-cosseno devolve valores em $[0,\pi]$:

$$\arccos\left(-\frac{\sqrt3}{2}\right) = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$$

**(c)** $\operatorname{tg}\dfrac{3\pi}{4} = -1$, e o arco-tangente devolve valores em $\left(-\frac\pi2,\frac\pi2\right)$:

$$\operatorname{arctg}(-1) = -\frac{\pi}{4}$$

**(d)** Aqui a ordem é a outra: $0{,}3 \in [-1,1]$, que é o domínio do arco-seno. Então vale $\operatorname{sen}\big(\operatorname{arcsen} u\big) = u$ diretamente:

$$\operatorname{sen}\big(\operatorname{arcsen} 0{,}3\big) = 0{,}3$$

> [!IMPORTANT]
> **A ordem das composições não é simétrica.** $\operatorname{sen}(\operatorname{arcsen} u) = u$ vale para **todo** $u \in [-1,1]$. Já $\operatorname{arcsen}(\operatorname{sen} x) = x$ vale só para $x \in \left[-\frac\pi2,\frac\pi2\right]$. A razão: a restrição foi feita no domínio do seno, não no do arco-seno.

---

### Exercício 15

**Hipótese.** $f$ é estritamente crescente em um intervalo $I$: se $a < b$ em $I$, então $f(a) < f(b)$.

**Tese.** $f$ é injetora em $I$.

**Demonstração.** Sejam $x_1, x_2 \in I$ com $x_1 \neq x_2$. Há duas possibilidades:

- se $x_1 < x_2$, a hipótese dá $f(x_1) < f(x_2)$;
- se $x_2 < x_1$, a hipótese dá $f(x_2) < f(x_1)$.

Em ambos os casos $f(x_1) \neq f(x_2)$. Logo $f$ é injetora. $\blacksquare$

> 💡 A demonstração para funções decrescentes é idêntica, trocando os sinais.

---

### Exercício 16

$$(f \circ g)(x) = f(3x) = 3x + 2$$

Invertendo: $y = 3x+2 \Rightarrow x = \dfrac{y-2}{3}$, ou seja,

$$(f \circ g)^{-1}(x) = \frac{x-2}{3}$$

Por outro lado, $f^{-1}(x) = x - 2$ e $g^{-1}(x) = \dfrac{x}{3}$. Então

$$\big(g^{-1} \circ f^{-1}\big)(x) = g^{-1}(x-2) = \frac{x-2}{3} \quad \checkmark$$

As duas coincidem, confirmando $(f\circ g)^{-1} = g^{-1} \circ f^{-1}$.

> ⚠️ Repare que $f^{-1} \circ g^{-1}$ daria $\frac{x}{3} - 2$, que é **outra** função. A ordem inverte — não é detalhe.

---

### Exercício 17

$$f^{-1}(1) = 3 \quad (\text{pois } f(3)=1) \qquad f^{-1}(3) = 1 \quad (\text{pois } f(1)=3)$$
$$f^{-1}(5) = 2 \quad (\text{pois } f(2)=5) \qquad f^{-1}\big(f(2)\big) = 2$$

---

### Exercício 18

A parábola $f(x) = x^2 + kx + 1$ tem vértice em

$$x_v = -\frac{k}{2}$$

e é crescente à direita do vértice. Para que $f$ seja injetora em $[1,+\infty)$, basta que esse intervalo esteja **inteiramente** na parte crescente:

$$-\frac{k}{2} \leqslant 1 \ \Longrightarrow \ -k \leqslant 2 \ \Longrightarrow \ k \geqslant -2$$

**Resposta.** $k \geqslant -2$.

*Conferência:* com $k = -2$, o vértice fica em $x=1$, exatamente na borda do intervalo — e a função é crescente em todo $[1,+\infty)$ ✔. Com $k = -4$, o vértice iria para $x=2$, e teríamos $f(1) = f(3)$, quebrando a injetividade ✘.

---

## Bloco C · Desafio

### Exercício 19

**Tese.** $f(x) = x^3 + x$ é injetora.

**Demonstração.** Suponha $f(a) = f(b)$, isto é, $a^3 + a = b^3 + b$. Então

$$a^3 - b^3 + a - b = 0$$

Fatorando a diferença de cubos, $a^3-b^3 = (a-b)(a^2+ab+b^2)$, e pondo $(a-b)$ em evidência:

$$(a-b)\big(a^2+ab+b^2\big) + (a-b) = 0 \ \Longrightarrow \ (a-b)\big(a^2+ab+b^2+1\big) = 0$$

Resta mostrar que o segundo fator **nunca** é zero. Completando o quadrado:

$$a^2 + ab + b^2 = \left(a + \frac{b}{2}\right)^2 + \frac{3b^2}{4} \geqslant 0$$

Logo $a^2+ab+b^2+1 \geqslant 1 > 0$. Como o produto é zero e o segundo fator não é, necessariamente $a - b = 0$, ou seja, $a = b$.

Portanto $f$ é injetora. $\blacksquare$

> 💡 Na Unidade 4 isso sai em uma linha: $f'(x) = 3x^2+1 > 0$ para todo $x$, logo $f$ é estritamente crescente e, portanto, injetora. Guarde a comparação — ela mostra bem o que a derivada compra.

---

### Exercício 20

Como $\lvert x \rvert$ muda de expressão em $x=0$, convém escrever $f$ por partes:

$$
f(x) = \begin{cases}
\dfrac{x}{1+x}, & \text{se } x \geqslant 0 \\[6pt]
\dfrac{x}{1-x}, & \text{se } x < 0
\end{cases}
$$

**Imagem.** Para $x \geqslant 0$:

$$\frac{x}{1+x} = \frac{(1+x) - 1}{1+x} = 1 - \frac{1}{1+x}$$

que cresce de $0$ (em $x=0$) e se aproxima de $1$ sem atingi-lo. Esse ramo cobre $[0,\thinspace 1)$.

Como $f$ é **ímpar** — pois $f(-x) = \dfrac{-x}{1+\lvert x \rvert} = -f(x)$ — o ramo negativo cobre $(-1,\thinspace 0]$ por simetria.

$$\operatorname{Im}(f) = (-1,\thinspace 1)$$

**Injetividade.** Cada ramo é estritamente crescente, e eles ocupam faixas disjuntas da imagem ($[0,1)$ e $(-1,0]$, com interseção só no $0$, atingido uma única vez, em $x=0$). Logo $f$ é injetora em $\mathbb{R}$.

**Inversa.** Para $y \geqslant 0$, resolvendo $y = \dfrac{x}{1+x}$:

$$y(1+x) = x \ \Longrightarrow \ y = x(1-y) \ \Longrightarrow \ x = \frac{y}{1-y}$$

Para $y < 0$, resolvendo $y = \dfrac{x}{1-x}$, obtém-se analogamente $x = \dfrac{y}{1+y}$. As duas expressões se reúnem em uma só:

$$f^{-1}(x) = \frac{x}{1 - \lvert x \rvert}, \qquad D(f^{-1}) = (-1,\thinspace 1)$$

*Conferência:* $f(1) = \frac{1}{2}$ e $f^{-1}\left(\frac12\right) = \frac{1/2}{1 - 1/2} = 1$ ✔.

> 💡 Esta função é um "compressor": ela espreme a reta inteira dentro do intervalo $(-1,1)$, de forma reversível. Funções com esse perfil aparecem em estatística e em redes neurais, com o nome de funções de ativação.

---

### Exercício 21

**Hipótese.** $f : A \to B$ é bijetora, e $f^{-1} : B \to A$ é a sua inversa.

**(i) $f^{-1}$ é injetora.** Suponha $f^{-1}(y_1) = f^{-1}(y_2)$. Aplicando $f$ aos dois lados e usando $f(f^{-1}(y)) = y$:

$$y_1 = f\big(f^{-1}(y_1)\big) = f\big(f^{-1}(y_2)\big) = y_2$$

**(ii) $f^{-1}$ é sobrejetora.** Dado qualquer $a \in A$, tome $y = f(a) \in B$. Então

$$f^{-1}(y) = f^{-1}\big(f(a)\big) = a$$

ou seja, todo elemento de $A$ é atingido por $f^{-1}$.

De (i) e (ii), $f^{-1}$ é bijetora.

**(iii) $\big(f^{-1}\big)^{-1} = f$.** Pela definição de inversa, $\big(f^{-1}\big)^{-1}$ é a única função que desfaz $f^{-1}$. Mas $f$ já faz isso: $f\big(f^{-1}(y)\big) = y$ e $f^{-1}\big(f(x)\big) = x$. Pela unicidade da inversa, $\big(f^{-1}\big)^{-1} = f$. $\blacksquare$

---

### Exercício 22

Já se sabe que $f\big(f(x)\big) = x$ para todo $x \neq 1$.

Essa identidade diz exatamente que $f$ **desfaz** $f$ — e, pela definição de inversa, a função que desfaz $f$ é $f^{-1}$. Pela unicidade da inversa:

$$f = f^{-1}$$

**Verificação direta.** Invertendo pela receita:

$$y = \frac{x+1}{x-1} \ \Longrightarrow \ y(x-1) = x+1 \ \Longrightarrow \ x(y-1) = y+1 \ \Longrightarrow \ x = \frac{y+1}{y-1}$$

que é a mesma expressão de $f$ ✔.

**Interpretação geométrica.** Como o gráfico de $f^{-1}$ é o reflexo do de $f$ na reta $y = x$, e aqui os dois gráficos **coincidem**, o gráfico de $f$ é **simétrico em relação à reta $y=x$**.

> 💡 Funções que são a própria inversa chamam-se **involuções**. Outros exemplos: $f(x) = \frac1x$, $f(x) = -x$, $f(x) = c - x$. Todas têm gráfico simétrico em relação a $y=x$ — e todas desfazem a si mesmas quando aplicadas duas vezes.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 1.4](../exercicios/lista-1.4-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [1.4 · Teoria](../1.4-injetoras-sobrejetoras-bijetoras-e-inversas.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
