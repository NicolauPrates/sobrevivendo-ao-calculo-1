# ✅ Gabarito — Lista 4.2

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 4.2](../exercicios/lista-4.2-propostos.md) · [Teoria 4.2](../4.2-teoremas-de-rolle-e-do-valor-medio.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $c = 2$ |
| 1 (b) | $c = 1$ |
| 1 (c) | $c = \dfrac{\pi}{2}$ |
| 2 (a) | $c = 1$ |
| 2 (b) | $c = \pm\dfrac{\sqrt3}{3}$ |
| 2 (c) | $c = \sqrt2$ |
| 3 (a) | falha a **derivabilidade** (bico em $x=0$) |
| 3 (b) | falha a **continuidade** (nem está definida em $x=0$) |
| 3 (c) | falha $f(a)=f(b)$ |
| 4 | (a) V · (b) F · (c) F · (d) V |
| 5 | $f(6) = 17$ |
| 6 | $3 \leqslant f(2) \leqslant 7$ |
| 7 | Demonstração — veja a Parte 2 |
| 8 | Explicação — veja a Parte 2 |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $c = 1$; não impede (derivabilidade só é exigida no **aberto**) |
| 10 | Demonstração — veja a Parte 2 |
| 11 | Demonstração — veja a Parte 2 |
| 12 | Demonstração — veja a Parte 2 |
| 13 | Demonstração — veja a Parte 2 |
| 14 | $c = \pm\dfrac{2\sqrt3}{3} \approx \pm1{,}155$ |
| 15 | Raiz única, entre $1$ e $2$ |
| 16 | Demonstração — veja a Parte 2 |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 17 | Demonstração — veja a Parte 2 |
| 18 | Demonstração — veja a Parte 2 |
| 19 | Demonstração — veja a Parte 2 |
| 20 | $c = \dfrac{14}{9} \approx 1{,}556$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** Polinômio: contínua em $[1,3]$ e derivável em $(1,3)$ ✔ ; $f(1)=0=f(3)$ ✔

$$f'(x) = 2x-4 = 0 \ \Longrightarrow \ c = 2 \in (1,3)$$

**(b)** Polinômio ✔ ; $f(0)=0$ e $f(2) = 4-4 = 0$ ✔

$$f'(x) = 2x-2 = 0 \ \Longrightarrow \ c = 1$$

**(c)** $\operatorname{sen}$ é contínua e derivável em $\mathbb{R}$ ✔ ; $\operatorname{sen} 0 = 0 = \operatorname{sen}\pi$ ✔

$$f'(x) = \cos x = 0 \ \Longrightarrow \ c = \frac{\pi}{2} \in (0,\pi)$$

---

### Exercício 2

**(a)** Taxa média $= \dfrac{4-0}{2} = 2$. Então $2c = 2 \Rightarrow c=1$ ✔

**(b)** Taxa média $= \dfrac{1-(-1)}{2} = 1$. Então $3c^2 = 1 \Rightarrow c = \pm\dfrac{1}{\sqrt3} = \pm\dfrac{\sqrt3}{3}$ — **os dois** estão em $(-1,1)$.

**(c)** Em $[1,2]$ a função $\frac1x$ é contínua e derivável ✔ Taxa média:

$$\frac{\frac12-1}{2-1} = -\frac12$$

$$f'(x) = -\frac{1}{x^2} = -\frac12 \ \Longrightarrow \ x^2 = 2 \ \Longrightarrow \ c = \sqrt2 \approx 1{,}414 \in (1,2)$$

---

### Exercício 3

**(a)** $f(-2)=f(2)=2$ ✔, mas $f$ **não é derivável** em $x=0$. Falha a hipótese 2 — e, de fato, $f'$ nunca é zero.

**(b)** $\frac1x$ **não está definida** em $x=0 \in [-1,1]$: falha a continuidade (e nem domínio há). Sem isso, o TVM não se aplica — note que a "taxa média" daria $\frac{-1-1}{2} = -1$, enquanto $f' = -\frac{1}{x^2}$ é sempre negativa, mas nunca vale $-1$ em... na verdade vale em $x=\pm1$, que são as bordas. O ponto é que o teorema simplesmente **não se aplica**.

**(c)** $f(0)=0$ e $f(2)=2$: falha $f(a)=f(b)$. E $f'=1\neq0$ sempre.

---

### Exercício 4

**(a) Verdadeiro.** Com $f(a)=f(b)$, a taxa média do TVM é zero.

**(b) Falso.** Ele garante **pelo menos um**; o Exercício 2(b) tem dois.

**(c) Falso.** O domínio precisa ser um **intervalo**. Contraexemplo: $\frac{\lvert x\rvert}{x}$.

**(d) Verdadeiro.** É o Corolário 3.

---

### Exercício 5

Pelo TVM em $[2,6]$ (ou simplesmente porque $f$ é afim):

$$f(6)-f(2) = f'(c)\cdot(6-2) = 3\cdot 4 = 12 \ \Longrightarrow \ f(6) = 5+12 = 17$$

---

### Exercício 6

Pelo TVM em $[0,2]$: $f(2)-f(0) = f'(c)\cdot2$, com $1 \leqslant f'(c)\leqslant 3$:

$$2 \leqslant f(2)-1 \leqslant 6 \ \Longrightarrow \ 3 \leqslant f(2) \leqslant 7$$

---

### Exercício 7

**Existência.** $f(-1) = -1-2+1 = -2 < 0$ e $f(0) = 1 > 0$. Como $f$ é polinomial (contínua), Bolzano garante uma raiz em $(-1,0)$.

**Unicidade.** Se houvesse duas raízes $r_1<r_2$, Rolle daria um $c$ com $f'(c)=0$. Mas

$$f'(x) = 5x^4+2 \geqslant 2 > 0 \quad \text{para todo } x$$

nunca se anula. Contradição. **A raiz é única.** $\blacksquare$

---

### Exercício 8

As funções $x^2$, $x^2+1$, $x^2-7$ **todas** têm derivada $2x$. Pelo **Corolário 2**, duas funções com a mesma derivada num intervalo diferem por uma constante — e nenhuma informação adicional distingue uma da outra.

Logo o conjunto **completo** das primitivas de $2x$ é $\lbrace x^2 + C : C\in\mathbb{R}\rbrace$, e escrever apenas $x^2$ seria dar **uma** resposta onde existem infinitas. É essa a origem do "$+\thinspace C$" da [Unidade 5](../../05-integrais/README.md).

---

## Bloco B · Consolidação

### Exercício 9

**Hipóteses:** $\sqrt x$ é contínua em $[0,4]$ ✔ e derivável em $(0,4)$ ✔ — a não derivabilidade em $x=0$ **não impede nada**, porque o teorema exige derivabilidade apenas no intervalo **aberto**.

**Taxa média:** $\dfrac{2-0}{4-0} = \dfrac12$.

$$f'(x) = \frac{1}{2\sqrt x} = \frac12 \ \Longrightarrow \ \sqrt x = 1 \ \Longrightarrow \ c = 1 \in (0,4) \quad \checkmark$$

> 💡 **Essa assimetria entre $[a,b]$ e $(a,b)$ é proposital no enunciado do teorema.** Ela permite aplicá-lo a funções com tangente vertical nas pontas, como esta.

---

### Exercício 10

Seja $g(x) = x - \ln(1+x)$, definida para $x>-1$, com $g(0)=0$.

$$g'(x) = 1 - \frac{1}{1+x} = \frac{(1+x)-1}{1+x} = \frac{x}{1+x}$$

Para $x>0$, numerador e denominador são positivos, logo $g'(x)>0$ e $g$ é **crescente** em $[0,+\infty)$.

Como $g(0)=0$ e $g$ cresce, $g(x)>0$ para $x>0$, isto é,

$$x - \ln(1+x) > 0 \ \Longrightarrow \ \ln(1+x) < x \qquad \blacksquare$$

---

### Exercício 11

Se $a=b$, a desigualdade é trivial. Se $a \neq b$, aplique o TVM a $f(x)=\operatorname{sen} x$ no intervalo de extremos $a$ e $b$: existe $c$ entre eles com

$$\operatorname{sen} a - \operatorname{sen} b = \cos c\thinspace (a-b)$$

Tomando módulos e usando $\lvert\cos c\rvert \leqslant 1$:

$$\big\lvert \operatorname{sen} a - \operatorname{sen} b\big\rvert = \lvert\cos c\rvert\cdot\lvert a-b\rvert \leqslant \lvert a-b\rvert \qquad \blacksquare$$

> 💡 Em palavras: **o seno nunca "estica" distâncias.** É um caso particular do Exercício 18.

---

### Exercício 12

Suponha, por absurdo, que $f$ tenha **duas** raízes $r_1<r_2$ em $(a,b)$. Então $f(r_1)=f(r_2)=0$, e $f$ é contínua em $[r_1,r_2]$ e derivável em $(r_1,r_2)$ (pois esses intervalos estão dentro de $(a,b)$).

Pelo Teorema de Rolle, existiria $c\in(r_1,r_2)$ com $f'(c)=0$ — contrariando a hipótese de que $f'$ nunca se anula.

Logo $f$ tem **no máximo uma** raiz em $(a,b)$. $\blacksquare$

---

### Exercício 13

Sejam $f(t)$ e $g(t)$ as posições dos dois corredores, com largada em $t=a$ e chegada em $t=b$:

$$f(a) = g(a) \qquad \text{(partem juntos)}$$
$$f(b) = g(b) \qquad \text{(chegam empatados)}$$

Defina $h = f-g$, contínua em $[a,b]$ e derivável em $(a,b)$ (supondo movimentos suaves). Então

$$h(a) = 0 = h(b)$$

Pelo **Teorema de Rolle**, existe $c\in(a,b)$ com $h'(c) = 0$, ou seja,

$$f'(c) = g'(c)$$

— no instante $c$, os dois tinham a **mesma velocidade**. $\blacksquare$

---

### Exercício 14

$$f(2) = 8-6+2 = 4 \qquad f(-2) = -8+6+2 = 0$$

**Taxa média:** $\dfrac{4-0}{2-(-2)} = 1$.

$$f'(x) = 3x^2-3 = 1 \ \Longrightarrow \ 3x^2 = 4 \ \Longrightarrow \ x = \pm\frac{2}{\sqrt3} = \pm\frac{2\sqrt3}{3} \approx \pm1{,}155$$

Os **dois** valores estão em $(-2,2)$.

---

### Exercício 15

**Existência.** $f(1) = 1+1-4 = -2 < 0$ e $f(2) = 8+2-4 = 6 > 0$. Por Bolzano, há raiz em $(1,\thinspace 2)$.

**Unicidade.** $f'(x) = 3x^2+1 \geqslant 1 > 0$ nunca se anula; pelo Exercício 12, há no máximo uma raiz.

**Resposta.** Raiz única, localizada entre $1$ e $2$.

---

### Exercício 16

Pelo TVM em $[0,2]$, existe $c\in(0,2)$ com

$$f(2) - f(0) = f'(c)\cdot(2-0) = 2f'(c)$$

Como $f(0)=0$ e $f'(c) \leqslant 2$:

$$f(2) = 2f'(c) \leqslant 2\cdot 2 = 4 \qquad \blacksquare$$

---

## Bloco C · Desafio

### Exercício 17

**Construção.** A reta secante que passa por $\big(a,f(a)\big)$ e $\big(b,f(b)\big)$ é

$$r(x) = f(a) + \frac{f(b)-f(a)}{b-a}(x-a)$$

Defina $g(x) = f(x) - r(x)$.

**Verificando as hipóteses de Rolle para $g$:**

1. $g$ é **contínua** em $[a,b]$: diferença de funções contínuas ✔
2. $g$ é **derivável** em $(a,b)$: diferença de deriváveis ✔
3. Nas pontas:
   $$g(a) = f(a)-r(a) = f(a)-f(a) = 0$$
   $$g(b) = f(b)-r(b) = f(b)-f(b) = 0$$
   logo $g(a)=g(b)$ ✔

**Aplicando Rolle:** existe $c\in(a,b)$ com $g'(c)=0$. Mas

$$g'(x) = f'(x) - \frac{f(b)-f(a)}{b-a}$$

(a derivada de $r$ é a sua inclinação, constante). Então $g'(c)=0$ significa

$$f'(c) = \frac{f(b)-f(a)}{b-a} \qquad \blacksquare$$

> 💡 **A ideia é "inclinar o gráfico até ele ficar horizontal".** Subtrair a secante transforma o problema geral no caso particular de Rolle — um truque que reaparece em várias demonstrações do Cálculo.

---

### Exercício 18

Sejam $x,y \in I$. Se $x=y$, a desigualdade é trivial ($0 \leqslant 0$).

Se $x\neq y$, aplique o TVM no intervalo de extremos $x$ e $y$ (que está contido em $I$): existe $c$ entre eles com

$$f(x)-f(y) = f'(c)\thinspace (x-y)$$

Tomando módulos:

$$\big\lvert f(x)-f(y)\big\rvert = \lvert f'(c)\rvert\cdot\lvert x-y\rvert \leqslant M\thinspace \lvert x-y\rvert \qquad \blacksquare$$

> 💡 **Interpretação:** uma função lipschitziana não pode "esticar" distâncias mais do que o fator $M$. O Exercício 11 é o caso $M=1$ para o seno. Essa propriedade é central em equações diferenciais, onde ela garante que a solução é única.

---

### Exercício 19

Seja $g(x) = x - f(x)$, com $g(0) = 0 - 0 = 0$.

$$g'(x) = 1 - f'(x) \geqslant 1 - 1 = 0$$

Logo $g$ é **não decrescente** em $[0,+\infty)$ (Corolário 3, na versão com $\geqslant$).

Como $g(0)=0$ e $g$ não decresce, tem-se $g(x) \geqslant 0$ para todo $x\geqslant0$, ou seja,

$$x - f(x) \geqslant 0 \ \Longrightarrow \ f(x) \leqslant x \qquad \blacksquare$$

---

### Exercício 20

**Verificando as hipóteses** em $[1,2]$: $f(x)=x^2$ e $g(x)=x^3$ são polinômios — contínuas e deriváveis ✔ E $g'(x) = 3x^2 \neq 0$ em $(1,2)$ ✔

**Lado esquerdo:**

$$\frac{f(2)-f(1)}{g(2)-g(1)} = \frac{4-1}{8-1} = \frac{3}{7}$$

**Lado direito:**

$$\frac{f'(c)}{g'(c)} = \frac{2c}{3c^2} = \frac{2}{3c}$$

**Igualando:**

$$\frac{2}{3c} = \frac37 \ \Longrightarrow \ 14 = 9c \ \Longrightarrow \ c = \frac{14}{9} \approx 1{,}556 \in (1,2) \quad \checkmark$$

> 💡 **Por que esse teorema existe.** Ele é a ferramenta usada para **demonstrar a Regra de L'Hôspital**, que é o assunto da [próxima seção](../4.3-regra-de-lhospital.md). Note que o TVM comum é o caso particular $g(x)=x$.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 4.2](../exercicios/lista-4.2-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [4.2 · Teoria](../4.2-teoremas-de-rolle-e-do-valor-medio.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
