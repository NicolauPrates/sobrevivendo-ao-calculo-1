# ✅ Gabarito — Lista 2.2

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 2.2](../exercicios/lista-2.2-propostos.md) · [Teoria 2.2](../2.2-limites-laterais.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 | $\lim_{x\to2^{-}} = 5$; $\lim_{x\to2^{+}} = 5$; $\lim_{x\to2} = 5$; $f(2) = 5$ |
| 2 | $\lim_{x\to1^{-}} = 1$; $\lim_{x\to1^{+}} = 2$; o limite **não existe** |
| 3 (a) | $-1$ |
| 3 (b) | $1$ |
| 3 (c) | $1$ |
| 3 (d) | $-1$ |
| 4 (a) | $2$ |
| 4 (b) | $3$ |
| 4 (c) | $2$ |
| 4 (d) | $3$ |
| 5 (a) | $0$ |
| 5 (b) | $0$ |
| 5 (c) | não existe (a função não está definida à esquerda de $2$) |
| 5 (d) | não existe |
| 6 | $k = 0$ |
| 7 | (a) F · (b) V · (c) F · (d) F |
| 8 | $\lim_{x\to0^{-}} = 0$; $\lim_{x\to0^{+}} = 1$; o limite **não existe** |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $-2$ pela esquerda, $2$ pela direita; o limite não existe |
| 10 | $2$ pela esquerda, $0$ pela direita; o limite não existe |
| 11 | $a = -5$ |
| 12 | Em $x=2$: os dois laterais valem $0$, o limite existe e vale $0$. Em $x=-2$: só existe o lateral à direita, que vale $0$ |
| 13 | $-1$ pela esquerda, $1$ pela direita; o limite não existe |
| 14 | Em $x=0$ **não existe**; em $x=3$ existe e vale $3$ |
| 15 | $a = 0$ e $b = 0$ |
| 16 | $0$ pela direita; pela esquerda não existe (tende a $-\infty$) |
| 17 | $1$ pela esquerda, $0$ pela direita; o limite não existe |
| 18 | Em todos os **números inteiros** |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | $\lim_{x\to1} f(x) = 2$ e $\lim_{x\to3} f(x) = 2$ |
| 20 | $a = 0$ e $b = 3$ |
| 21 | Demonstração — veja a Parte 2 |
| 22 | $D(f) = (0,+\infty)$; $\lim_{x\to0^{+}} f(x) = \dfrac12$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**Pela esquerda** ($x<2$, vale $3x-1$): $\lim_{x\to2^{-}} (3x-1) = 5$.

**Pela direita** ($x \geqslant 2$, vale $x+3$): $\lim_{x\to2^{+}} (x+3) = 5$.

Como os dois coincidem, $\lim_{x\to2} f(x) = 5$.

**No ponto:** $f(2) = 2+3 = 5$.

> 💡 Aqui as três quantidades coincidem — e é exatamente isso que significa a função ser **contínua** em $x=2$ ([2.5](../2.5-continuidade-e-tipos-de-descontinuidade.md)).

---

### Exercício 2

**Pela esquerda** ($x \leqslant 1$, vale $x^2$): $\lim_{x\to1^{-}} x^2 = 1$.

**Pela direita** ($x>1$, vale $2x$): $\lim_{x\to1^{+}} 2x = 2$.

Como $1 \neq 2$, **o limite não existe**. Há um salto de altura $1$ em $x=1$.

---

### Exercício 3

**(a)** Para $x<0$: $\lvert x \rvert = -x$, logo $\dfrac{-x}{x} = -1$. Limite: $-1$.

**(b)** Para $x>0$: $\lvert x \rvert = x$, logo $\dfrac{x}{x} = 1$. Limite: $1$.

**(c)** Para $x>5$: $x-5>0$, logo $\lvert x-5\rvert = x-5$ e a razão vale $1$. Limite: $1$.

**(d)** Para $x<5$: $x-5<0$, logo $\lvert x-5\rvert = -(x-5)$ e a razão vale $-1$. Limite: $-1$.

---

### Exercício 4

**(a)** À esquerda de $3$ (por exemplo, $x = 2{,}99$), o maior inteiro que não ultrapassa $x$ é $2$. Limite: $2$.

**(b)** À direita de $3$ ($x = 3{,}01$), o maior inteiro é $3$. Limite: $3$.

**(c)** Em torno de $2{,}5$ a função é **constante** igual a $2$ (nenhum inteiro é cruzado por perto). Limite: $2$.

**(d)** $\lfloor 3 \rfloor = 3$ — este é o **valor**, não um limite.

> ⚠️ Compare (a) com (d): o limite pela esquerda é $2$, e o valor no ponto é $3$. Um não tem nada a ver com o outro.

---

### Exercício 5

**(a)** $\lim_{x\to0^{+}} \sqrt{x} = 0$.

**(b)** $\lim_{x\to2^{+}} \sqrt{x-2} = 0$.

**(c)** **Não existe:** para $x<2$ o radicando $x-2$ é negativo, e a função nem está definida ali.

**(d)** **Não existe**, porque falta um dos laterais (Teorema 2.2.1).

---

### Exercício 6

$$\lim_{x\to2^{-}} (x+k) = 2+k \qquad \lim_{x\to2^{+}} (3x-4) = 2$$

Igualando: $2+k = 2 \Rightarrow k = 0$. Nesse caso, $\lim_{x\to2} f(x) = 2$.

---

### Exercício 7

**(a) Falso.** Eles precisam, além de existir, ser **iguais**. Contraexemplo: o Exercício 2.

**(b) Verdadeiro.** É o Teorema 2.2.1, lido da esquerda para a direita.

**(c) Falso.** $x \to a^{+}$ significa $x > a$ — valores **maiores**.

**(d) Falso.** No Exercício 2, $g(1) = 1$ existe e o limite não.

---

### Exercício 8

**Pela esquerda** ($x<0$, vale $x^2$): $\lim_{x\to0^{-}} x^2 = 0$.

**Pela direita** ($x \geqslant 0$, vale $x+1$): $\lim_{x\to0^{+}} (x+1) = 1$.

O limite **não existe**. O gráfico é o ramo esquerdo da parábola até a origem (com furo em $(0,0)$) e, a partir de $x=0$, a reta $y=x+1$ começando no ponto cheio $(0,1)$.

---

## Bloco B · Consolidação

### Exercício 9

Fatore: $x^2-1 = (x-1)(x+1)$.

**Pela esquerda** ($x<1$, logo $\lvert x-1\rvert = -(x-1)$):

$$\frac{(x-1)(x+1)}{-(x-1)} = -(x+1) \ \longrightarrow \ -2$$

**Pela direita** ($x>1$, logo $\lvert x-1\rvert = x-1$):

$$\frac{(x-1)(x+1)}{x-1} = x+1 \ \longrightarrow \ 2$$

O limite **não existe**.

---

### Exercício 10

**Pela esquerda** ($x<0$, $\lvert x\rvert = -x$):

$$\frac{x - (-x)}{x} = \frac{2x}{x} = 2 \ \longrightarrow \ 2$$

**Pela direita** ($x>0$, $\lvert x \rvert = x$):

$$\frac{x-x}{x} = \frac{0}{x} = 0 \ \longrightarrow \ 0$$

O limite **não existe**.

> ⚠️ Repare que $\frac{0}{x}$ é legítimo e vale $0$ para todo $x \neq 0$ — não é indeterminação. Indeterminação seria $\frac00$, com o denominador **também** tendendo a zero junto.

---

### Exercício 11

$$\lim_{x\to-1^{-}} \big(ax^2+1\big) = a+1 \qquad \lim_{x\to-1^{+}} (x-3) = -4$$

Igualando: $a+1 = -4 \Rightarrow a = -5$.

---

### Exercício 12

**Em $x=2$:**

- **Pela esquerda** ($-2 \leqslant x \leqslant 2$): $\lim_{x\to2^{-}} \sqrt{4-x^2} = \sqrt{0} = 0$.
- **Pela direita** ($x>2$): $\lim_{x\to2^{+}} (x-2) = 0$.

Os dois coincidem: $\lim_{x\to2} f(x) = 0$.

**Em $x=-2$:** à esquerda de $-2$ a função **não está definida** (o domínio começa em $-2$). Logo só existe

$$\lim_{x\to-2^{+}} \sqrt{4-x^2} = 0$$

e o limite bilateral não existe.

---

### Exercício 13

Fatore o denominador: $x^2-5x+6 = (x-2)(x-3)$.

**Pela esquerda** ($x<3$, $\lvert x-3\rvert = -(x-3)$):

$$\frac{-(x-3)}{(x-2)(x-3)} = \frac{-1}{x-2} \ \longrightarrow \ \frac{-1}{1} = -1$$

**Pela direita** ($x>3$):

$$\frac{x-3}{(x-2)(x-3)} = \frac{1}{x-2} \ \longrightarrow \ 1$$

O limite **não existe**.

---

### Exercício 14

**Em $x=0$:**

$$\lim_{x\to0^{-}} \big(x^2-4\big) = -4 \qquad \lim_{x\to0^{+}} \lvert x \rvert = 0$$

Diferentes: **não existe**.

**Em $x=3$:**

$$\lim_{x\to3^{-}} \lvert x \rvert = 3 \qquad \lim_{x\to3^{+}} (12-3x) = 12-9 = 3$$

Iguais: $\lim_{x\to3} f(x) = 3$.

---

### Exercício 15

**Em $x=0$:**

$$\lim_{x\to0^{-}}(x+a) = a \qquad \lim_{x\to0^{+}}\big(x^2+b\big) = b$$

Logo $a = b$.

**Em $x=2$:**

$$\lim_{x\to2^{-}}\big(x^2+b\big) = 4+b \qquad \lim_{x\to2^{+}} 2x = 4$$

Logo $4+b = 4$, ou seja, $b = 0$ — e, portanto, $a = 0$.

**Resposta.** $a = b = 0$.

---

### Exercício 16

**Pela direita** ($x>0$, $\lvert x\rvert = x$):

$$\frac1x - \frac1x = 0 \ \longrightarrow \ 0$$

**Pela esquerda** ($x<0$, $\lvert x\rvert = -x$):

$$\frac1x - \frac{1}{-x} = \frac1x + \frac1x = \frac2x$$

Quando $x \to 0^{-}$, o denominador tende a zero **por valores negativos**, e a fração cresce em módulo sem limitação, com sinal negativo:

$$\lim_{x\to0^{-}} \frac2x = -\infty$$

Isto é: o limite **não existe** como número — ele tende a $-\infty$. O tratamento sistemático desse caso é o assunto de [2.4](../2.4-limites-infinitos-no-infinito-e-assintotas.md).

---

### Exercício 17

A parte fracionária $x - \lfloor x \rfloor$ devolve "o que vem depois da vírgula".

**Pela esquerda de $2$** (por exemplo $x=1{,}99$): $\lfloor x\rfloor = 1$, logo $f(x) = x-1 \to 1$.

**Pela direita de $2$** ($x = 2{,}01$): $\lfloor x\rfloor = 2$, logo $f(x) = x-2 \to 0$.

O limite **não existe**.

**O gráfico** em $[0,3]$ é uma sequência de "rampas": em cada intervalo $[k,\thinspace k+1)$ a função sobe de $0$ (ponto cheio) até $1$ (sem atingir, ponto vazio), e despenca para $0$ no inteiro seguinte. É uma função **serra**.

---

### Exercício 18

Seja $n$ um inteiro qualquer. À esquerda de $n$, o maior inteiro é $n-1$; à direita (e em $n$), é $n$:

$$\lim_{x\to n^{-}} \lfloor x \rfloor = n-1 \qquad \lim_{x\to n^{+}} \lfloor x \rfloor = n$$

Como $n-1 \neq n$, o limite **não existe em nenhum inteiro**.

Em qualquer ponto **não inteiro** $c$, existe um intervalo em torno de $c$ onde $\lfloor x \rfloor$ é **constante**; logo o limite existe e vale $\lfloor c \rfloor$.

**Resposta.** O limite não existe exatamente nos pontos de $\mathbb{Z}$.

---

## Bloco C · Desafio

### Exercício 19

Os módulos trocam de expressão em $x=1$ e $x=3$. Escreva $f$ por partes:

$$
f(x) = \begin{cases}
(1-x)+(3-x) = 4-2x, & \text{se } x < 1 \\
(x-1)+(3-x) = 2, & \text{se } 1 \leqslant x < 3 \\
(x-1)+(x-3) = 2x-4, & \text{se } x \geqslant 3
\end{cases}
$$

**Em $x=1$:**

$$\lim_{x\to1^{-}}(4-2x) = 2 \qquad \lim_{x\to1^{+}} 2 = 2 \ \Longrightarrow \ \lim_{x\to1} f(x) = 2$$

**Em $x=3$:**

$$\lim_{x\to3^{-}} 2 = 2 \qquad \lim_{x\to3^{+}} (2x-4) = 2 \ \Longrightarrow \ \lim_{x\to3} f(x) = 2$$

> 💡 **Soma de módulos não salta.** Cada $\lvert x-a \rvert$ é contínua (vale $0$ no ponto de troca, pelos dois lados), e somas de funções contínuas são contínuas. O "bico" do gráfico é um problema para a **derivada**, não para o limite.

---

### Exercício 20

**Existência do limite.** Os dois laterais precisam coincidir:

$$\lim_{x\to1^{-}}(ax+b) = a+b \qquad \lim_{x\to1^{+}}\big(bx^2-a\big) = b-a$$

$$a+b = b-a \ \Longrightarrow \ 2a = 0 \ \Longrightarrow \ a = 0$$

**Igualdade com $f(1)$.** Com $a=0$, o limite comum vale $b$. Exigindo que seja igual a $f(1) = 3$:

$$b = 3$$

**Resposta.** $a = 0$ e $b = 3$.

*Conferência:* a função vira $f(x) = 3$ para $x<1$, $f(1)=3$ e $f(x) = 3x^2$ para $x>1$. Em $x=1$: laterais $3$ e $3$ ✔, valor $3$ ✔.

---

### Exercício 21

**Nenhuma tem limite nos inteiros.** Para $\lfloor x \rfloor$, isso é o Exercício 18. Para $g(x) = x - \lfloor x \rfloor$, em um inteiro $n$:

$$\lim_{x\to n^{-}} g(x) = \lim_{x\to n^{-}} \big(x - (n-1)\big) = 1 \qquad \lim_{x\to n^{+}} g(x) = \lim_{x\to n^{+}} (x - n) = 0$$

Como $1 \neq 0$, $g$ também não tem limite em inteiro nenhum.

**Mas a soma tem.** Para **todo** $x$ real,

$$f(x) + g(x) = \lfloor x \rfloor + \big(x - \lfloor x \rfloor\big) = x$$

A soma é a função identidade, que tem limite em todo ponto: $\lim_{x\to a}\big(f(x)+g(x)\big) = a$. $\blacksquare$

> 💡 **A moral é a mesma do Exercício Resolvido 4 da teoria:** a propriedade "limite da soma é a soma dos limites" exige que as parcelas tenham limite. Quando não têm, a soma ainda pode ter — os saltos se cancelam. A propriedade é uma via de mão única.

---

### Exercício 22

**Domínio.** O denominador é $\lvert x \rvert + x$:

- para $x > 0$: $\lvert x\rvert + x = x + x = 2x \neq 0$ ✔;
- para $x < 0$: $\lvert x\rvert + x = -x + x = 0$ ✘ — o denominador **zera para todo $x$ negativo**;
- para $x = 0$: também dá $0$ ✘.

$$D(f) = (0,\thinspace +\infty)$$

**Limites laterais em $0$.** Só o da direita faz sentido. Para $x>0$:

$$f(x) = \frac{x}{2x} = \frac12 \ \Longrightarrow \ \lim_{x\to0^{+}} f(x) = \frac12$$

O limite pela esquerda **não existe** — e nem poderia ser calculado, já que a função não está definida em nenhum ponto à esquerda de $0$.

> 💡 **A pegadinha está no domínio, não na conta.** Quem tentou "abrir o módulo" direto obteve $\frac{x}{0}$ à esquerda e concluiu "infinito". Mas não há sequer um ponto do domínio ali para se aproximar: a questão é de existência, não de valor.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 2.2](../exercicios/lista-2.2-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [2.2 · Teoria](../2.2-limites-laterais.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
