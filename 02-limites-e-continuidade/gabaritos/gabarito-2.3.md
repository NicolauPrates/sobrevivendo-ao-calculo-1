# ✅ Gabarito — Lista 2.3

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 2.3](../exercicios/lista-2.3-propostos.md) · [Teoria 2.3](../2.3-teorema-do-sanduiche.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $4$ |
| 1 (b) | $\dfrac13$ |
| 1 (c) | $\dfrac25$ |
| 1 (d) | $3$ |
| 2 (a) | $0$ |
| 2 (b) | $0$ |
| 2 (c) | $0$ |
| 3 | $5$ |
| 4 (a) | $0$ |
| 4 (b) | $\dfrac12$ |
| 4 (c) | $1$ |
| 5 | (a) V · (b) F · (c) F · (d) V |
| 6 (a) | $0$ |
| 6 (b) | $1$ |
| 6 (c) | $1$ |
| 7 (a) | $0$ |
| 7 (b) | $\dfrac{2}{\pi}$ |
| 8 | $\dfrac35$ |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $-\dfrac12$ |
| 10 | $2$ |
| 11 | $0$ |
| 12 | $\dfrac12$ |
| 13 | $0$ |
| 14 | Demonstração — veja a Parte 2 |
| 15 | $-\mathrm{sen}\thinspace a$ |
| 16 | $2$ |
| 17 | Demonstração — veja a Parte 2 |
| 18 | $2$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | $1$ |
| 20 | $1$ |
| 21 | Demonstração — veja a Parte 2 |
| 22 | $\dfrac12$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** Multiplique e divida por $4$, para o denominador casar com o argumento:

$$\frac{\mathrm{sen}\thinspace 4x}{x} = 4\cdot\frac{\mathrm{sen}\thinspace 4x}{4x} \ \longrightarrow \ 4 \cdot 1 = 4$$

**(b)** $\dfrac{\mathrm{sen}\thinspace x}{3x} = \dfrac13 \cdot \dfrac{\mathrm{sen}\thinspace x}{x} \longrightarrow \dfrac13$

**(c)** Prepare as duas frações:

$$\frac{\mathrm{sen}\thinspace 2x}{\mathrm{sen}\thinspace 5x} = \frac{\mathrm{sen}\thinspace 2x}{2x}\cdot\frac{5x}{\mathrm{sen}\thinspace 5x}\cdot\frac{2}{5} \ \longrightarrow \ 1 \cdot 1 \cdot \frac25 = \frac25$$

**(d)** $\dfrac{\mathrm{tg}\thinspace 3x}{x} = \dfrac{\mathrm{sen}\thinspace 3x}{x\cos 3x} = 3\cdot\dfrac{\mathrm{sen}\thinspace 3x}{3x}\cdot\dfrac{1}{\cos 3x} \longrightarrow 3 \cdot 1 \cdot 1 = 3$

---

### Exercício 2

Em todos, o segundo fator é **limitado** (seno e cosseno vivem em $[-1,1]$) e o primeiro tende a zero.

**(a)** $\lvert x \rvert \to 0$ e $\left\lvert\mathrm{sen}\thinspace\frac1x\right\rvert \leqslant 1$ ⟹ limite $0$.

**(b)** $x^2 \to 0$ e $\left\lvert\cos\frac1x\right\rvert \leqslant 1$ ⟹ limite $0$.

**(c)** $x^4 \to 0$ e $\left\lvert\mathrm{sen}\thinspace\frac{1}{x^3}\right\rvert \leqslant 1$ ⟹ limite $0$.

> 💡 Note que não importa **quão rápido** o fator oscilante varia: $\mathrm{sen}\thinspace\frac{1}{x^3}$ oscila muito mais do que $\mathrm{sen}\thinspace\frac1x$, e o resultado é o mesmo. O que importa é só ele ser **limitado**.

---

### Exercício 3

$$\lim_{x\to2}(3x-1) = 5 \qquad \lim_{x\to2}\big(x^2+1\big) = 5$$

As duas pontas tendem a $5$, logo, pelo confronto, $\lim_{x\to2} f(x) = 5$.

---

### Exercício 4

**(a)** Multiplicando pelo conjugado:

$$\frac{1-\cos x}{x} = \frac{\mathrm{sen}^2\thinspace x}{x(1+\cos x)} = \frac{\mathrm{sen}\thinspace x}{x}\cdot\frac{\mathrm{sen}\thinspace x}{1+\cos x} \ \longrightarrow \ 1 \cdot \frac{0}{2} = 0$$

**(b)** Mesmo truque, com $x^2$ embaixo:

$$\frac{1-\cos x}{x^2} = \left(\frac{\mathrm{sen}\thinspace x}{x}\right)^2\cdot\frac{1}{1+\cos x} \ \longrightarrow \ 1 \cdot \frac12 = \frac12$$

**(c)** É o inverso do limite fundamental: $\dfrac{x}{\mathrm{sen}\thinspace x} = \left(\dfrac{\mathrm{sen}\thinspace x}{x}\right)^{-1} \longrightarrow \dfrac11 = 1$.

---

### Exercício 5

**(a) Verdadeiro.** É exatamente o Teorema do Confronto.

**(b) Falso.** As pontas precisam ter o **mesmo** limite. Contraexemplo: $g(x) = 1$, $h(x) = 3$ e

$$
f(x) = \begin{cases}
1, & \text{se } x < 0 \\
3, & \text{se } x \geqslant 0
\end{cases}
$$

satisfaz $g \leqslant f \leqslant h$, e $\lim_{x\to0} f(x)$ não existe.

**(c) Falso.** A demonstração usa a área do setor circular, $\frac12 r^2 x$, que só vale em radianos. Em graus, o limite seria $\frac{\pi}{180}$.

**(d) Verdadeiro.** É o teorema do anulamento (2.3.2).

---

### Exercício 6

**(a)** $\dfrac{\mathrm{sen}(x^2)}{x} = \dfrac{\mathrm{sen}(x^2)}{x^2}\cdot x \longrightarrow 1 \cdot 0 = 0$

**(b)** $\dfrac{\mathrm{sen}^2\thinspace x}{x^2} = \left(\dfrac{\mathrm{sen}\thinspace x}{x}\right)^2 \longrightarrow 1^2 = 1$

**(c)** $\dfrac{x}{\mathrm{tg}\thinspace x} = \dfrac{x\cos x}{\mathrm{sen}\thinspace x} = \dfrac{x}{\mathrm{sen}\thinspace x}\cdot\cos x \longrightarrow 1 \cdot 1 = 1$

---

### Exercício 7

**(a)** Substituindo: $\dfrac{\mathrm{sen}\thinspace\pi}{\pi} = \dfrac{0}{\pi} = 0$. Não há indeterminação nenhuma — o denominador não zera.

**(b)** $\dfrac{\mathrm{sen}(\pi/2)}{\pi/2} = \dfrac{1}{\pi/2} = \dfrac{2}{\pi} \approx 0{,}637$.

> ⚠️ **A armadilha da questão:** responder $1$ nos dois, por reflexo. O limite fundamental vale **só** quando $x \to 0$, porque é só aí que aparece a indeterminação $\frac00$. Em qualquer outro ponto, substitua.

---

### Exercício 8

$$\frac{\mathrm{sen}\thinspace 3x}{5x} = \frac{3}{5}\cdot\frac{\mathrm{sen}\thinspace 3x}{3x} \ \longrightarrow \ \frac35$$

---

## Bloco B · Consolidação

### Exercício 9

$$\frac{\cos x - 1}{x^2} = -\frac{1-\cos x}{x^2} \ \longrightarrow \ -\frac12$$

(usando o resultado do Exercício 4(b)).

---

### Exercício 10

Ponha $x$ em evidência no denominador:

$$\frac{\mathrm{sen}\thinspace 2x}{x+x^2} = \frac{\mathrm{sen}\thinspace 2x}{x(1+x)} = 2\cdot\frac{\mathrm{sen}\thinspace 2x}{2x}\cdot\frac{1}{1+x} \ \longrightarrow \ 2 \cdot 1 \cdot 1 = 2$$

---

### Exercício 11

Separe a fração:

$$\frac{x-\mathrm{sen}\thinspace x}{x} = \frac{x}{x} - \frac{\mathrm{sen}\thinspace x}{x} = 1 - \frac{\mathrm{sen}\thinspace x}{x} \ \longrightarrow \ 1 - 1 = 0$$

---

### Exercício 12

**Estratégia.** Fatorar $\mathrm{sen}\thinspace x$ e fazer aparecer os dois limites conhecidos.

$$\mathrm{tg}\thinspace x - \mathrm{sen}\thinspace x = \frac{\mathrm{sen}\thinspace x}{\cos x} - \mathrm{sen}\thinspace x = \mathrm{sen}\thinspace x\left(\frac{1}{\cos x} - 1\right) = \mathrm{sen}\thinspace x \cdot \frac{1-\cos x}{\cos x}$$

Dividindo por $x^3$ e separando em três fatores:

$$\frac{\mathrm{tg}\thinspace x - \mathrm{sen}\thinspace x}{x^3} = \frac{\mathrm{sen}\thinspace x}{x}\cdot\frac{1-\cos x}{x^2}\cdot\frac{1}{\cos x}$$

$$\longrightarrow \ 1 \cdot \frac12 \cdot 1 = \frac12$$

---

### Exercício 13

$\mathrm{sen}\thinspace x \to 0$ e $\cos\frac1x$ é **limitado**. Pelo anulamento, o limite é $0$.

---

### Exercício 14

Da sugestão, com $u = \dfrac1x$ (note que $x>0$, logo $u>0$):

$$\frac1x - 1 < \left\lfloor \frac1x \right\rfloor \leqslant \frac1x$$

Multiplicando os três membros por $x$, que é **positivo** (o sentido se mantém):

$$1 - x < x\left\lfloor\frac1x\right\rfloor \leqslant 1$$

Como $\lim_{x\to0^{+}}(1-x) = 1$ e $\lim_{x\to0^{+}} 1 = 1$, o Teorema do Confronto dá

$$\lim_{x\to0^{+}} x\left\lfloor\frac1x\right\rfloor = 1 \qquad \blacksquare$$

> 💡 Um resultado surpreendente: $\lfloor 1/x \rfloor$ dá saltos infinitos perto de $0$, e mesmo assim o produto converge mansamente para $1$.

---

### Exercício 15

Abra o cosseno da soma: $\cos(a+h) = \cos a\cos h - \mathrm{sen}\thinspace a \mathrm{sen}\thinspace h$.

$$
\begin{aligned}
\frac{\cos(a+h)-\cos a}{h}
&= \frac{\cos a\cos h - \mathrm{sen}\thinspace a\mathrm{sen}\thinspace h - \cos a}{h} \\
&= \frac{\cos a\thinspace (\cos h - 1) - \mathrm{sen}\thinspace a\mathrm{sen}\thinspace h}{h} \\
&= -\cos a \cdot \frac{1-\cos h}{h} - \mathrm{sen}\thinspace a\cdot\frac{\mathrm{sen}\thinspace h}{h}
\end{aligned}
$$

No limite: $-\cos a \cdot 0 - \mathrm{sen}\thinspace a \cdot 1 = -\mathrm{sen}\thinspace a$.

**Resposta.** $-\mathrm{sen}\thinspace a$ — que é a derivada do cosseno, obtida pela definição.

---

### Exercício 16

Separe em duas frações:

$$\frac{\mathrm{sen}\thinspace 5x - \mathrm{sen}\thinspace 3x}{x} = \frac{\mathrm{sen}\thinspace 5x}{x} - \frac{\mathrm{sen}\thinspace 3x}{x} = 5\cdot\frac{\mathrm{sen}\thinspace 5x}{5x} - 3\cdot\frac{\mathrm{sen}\thinspace 3x}{3x}$$

$$\longrightarrow \ 5 - 3 = 2$$

---

### Exercício 17

A hipótese $\lvert f(x)-3\rvert \leqslant 2\lvert x-1\rvert$ é equivalente (pela Propriedade 1.1.3) a

$$-2\lvert x-1\rvert \ \leqslant \ f(x) - 3 \ \leqslant \ 2\lvert x-1\rvert$$

Quando $x \to 1$, as duas pontas tendem a $0$. Pelo confronto,

$$\lim_{x\to1}\big(f(x)-3\big) = 0 \ \Longrightarrow \ \lim_{x\to1} f(x) = 3 \qquad \blacksquare$$

> 💡 **Esse é o formato da própria definição de limite.** A desigualdade dada é, essencialmente, "$\delta = \varepsilon/2$ funciona".

---

### Exercício 18

**Caminho 1 — pela identidade.** Como $1 - \cos 2x = 2\mathrm{sen}^2\thinspace x$:

$$\frac{1-\cos 2x}{x^2} = \frac{2\mathrm{sen}^2\thinspace x}{x^2} = 2\left(\frac{\mathrm{sen}\thinspace x}{x}\right)^2 \ \longrightarrow \ 2$$

**Caminho 2 — ajustando o argumento.** Multiplicando e dividindo por $4$:

$$\frac{1-\cos 2x}{x^2} = 4\cdot\frac{1-\cos 2x}{(2x)^2} \ \longrightarrow \ 4\cdot\frac12 = 2$$

Os dois caminhos dão $2$.

---

## Bloco C · Desafio

### Exercício 19

Multiplique e divida por $\mathrm{sen}\thinspace x$ — legítimo porque $\mathrm{sen}\thinspace x \neq 0$ para $x$ perto de $0$ (mas $x \neq 0$):

$$\frac{\mathrm{sen}(\mathrm{sen}\thinspace x)}{x} = \frac{\mathrm{sen}(\mathrm{sen}\thinspace x)}{\mathrm{sen}\thinspace x}\cdot\frac{\mathrm{sen}\thinspace x}{x}$$

No primeiro fator, faça $u = \mathrm{sen}\thinspace x$. Quando $x \to 0$, tem-se $u \to 0$, e o fator vira $\frac{\mathrm{sen}\thinspace u}{u} \to 1$. O segundo fator também tende a $1$.

$$\lim_{x\to0}\frac{\mathrm{sen}(\mathrm{sen}\thinspace x)}{x} = 1 \cdot 1 = 1$$

---

### Exercício 20

Racionalize o numerador:

$$
\begin{aligned}
\frac{\sqrt{1+\mathrm{sen}\thinspace x}-\sqrt{1-\mathrm{sen}\thinspace x}}{x}
&= \frac{(1+\mathrm{sen}\thinspace x)-(1-\mathrm{sen}\thinspace x)}{x\big(\sqrt{1+\mathrm{sen}\thinspace x}+\sqrt{1-\mathrm{sen}\thinspace x}\big)} \\
&= \frac{2\mathrm{sen}\thinspace x}{x\big(\sqrt{1+\mathrm{sen}\thinspace x}+\sqrt{1-\mathrm{sen}\thinspace x}\big)} \\
&= \frac{\mathrm{sen}\thinspace x}{x}\cdot\frac{2}{\sqrt{1+\mathrm{sen}\thinspace x}+\sqrt{1-\mathrm{sen}\thinspace x}}
\end{aligned}
$$

No limite: $1 \cdot \dfrac{2}{1+1} = 1$.

---

### Exercício 21

**Hipóteses.** Existe $M>0$ com $\lvert f(x)\rvert \leqslant M$ para todo $x$ perto de $a$, e $\lim_{x\to a} g(x) = 0$.

**Demonstração.** Para esses $x$,

$$\big\lvert f(x)g(x) \big\rvert = \lvert f(x)\rvert \cdot \lvert g(x)\rvert \leqslant M\thinspace \lvert g(x) \rvert$$

e, portanto,

$$-M\thinspace \lvert g(x)\rvert \ \leqslant \ f(x)g(x) \ \leqslant \ M\thinspace \lvert g(x)\rvert$$

Como $g(x) \to 0$, também $\lvert g(x)\rvert \to 0$ e, por L2, $\pm M\lvert g(x)\rvert \to 0$. As duas pontas do sanduíche tendem a $0$; pelo Teorema do Confronto,

$$\lim_{x\to a} f(x)g(x) = 0 \qquad \blacksquare$$

> 💡 Note onde a hipótese "limitada" entrou: ela permitiu **trocar $f$ por uma constante** $M$ na desigualdade. Sem isso, não haveria sanduíche — e o resultado seria falso: $\frac1x \cdot x \to 1$, não $0$.

---

### Exercício 22

Faça $u = x-1$, de modo que $x = u+1$ e $u \to 0$ quando $x \to 1$. O denominador vira

$$x^2 - 1 = (u+1)^2 - 1 = u^2 + 2u = u(u+2)$$

Então

$$\frac{\mathrm{sen}(x-1)}{x^2-1} = \frac{\mathrm{sen}\thinspace u}{u(u+2)} = \frac{\mathrm{sen}\thinspace u}{u}\cdot\frac{1}{u+2} \ \longrightarrow \ 1 \cdot \frac12 = \frac12$$

**Resposta.** $\dfrac12$

> 💡 **Alternativa sem mudança de variável:** fatore $x^2-1 = (x-1)(x+1)$ e escreva
> $$\frac{\mathrm{sen}(x-1)}{(x-1)(x+1)} = \frac{\mathrm{sen}(x-1)}{x-1}\cdot\frac{1}{x+1}$$
> O primeiro fator tem a forma $\frac{\mathrm{sen}\thinspace u}{u}$ com $u = x-1 \to 0$, e o segundo tende a $\frac12$.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 2.3](../exercicios/lista-2.3-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [2.3 · Teoria](../2.3-teorema-do-sanduiche.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
