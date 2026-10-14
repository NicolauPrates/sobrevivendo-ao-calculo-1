# ✅ Gabarito — Revisão da Unidade 1

> **Corrija com honestidade.** Pergunte-se "eu teria escrito isso?", e não "ah, eu sabia". Para cada questão errada, classifique a causa: não sabia a teoria, sabia e errei a montagem, montei certo e errei a conta, ou acabou o tempo. Cada uma pede um remédio diferente.

➡️ [Voltar para a Revisão](../exercicios/revisao-unidade-1.md)

---

# ✅ Parte 1 — Respostas finais

| Questão | Resposta |
| :---: | --- |
| 1 (a) | $(-\infty,\thinspace -4] \cup (3,\thinspace +\infty)$ |
| 1 (b) | $[-1,\thinspace 7]$ |
| 1 (c) | $(-\infty,\thinspace -3] \cup [0,\thinspace 3]$ |
| 2 | $(3,\thinspace 4) \cup (4,\thinspace 5)$ |
| 3 (a) | $[-5,\thinspace -2) \cup (-2,\thinspace 2) \cup (2,\thinspace +\infty)$ |
| 3 (b) | $(-\infty,\thinspace 0] \cup [3,\thinspace +\infty)$ |
| 3 (c) | $(-\infty,\thinspace 5)$ |
| 4 (a) | $2x + h - 2$ |
| 4 (b) | $[-1,\thinspace +\infty)$ |
| 5 (a) | $(f \circ g)(x) = \lvert x \rvert$, com $D = \mathbb{R}$ |
| 5 (b) | $(g \circ f)(x) = x$, com $D = [1,\thinspace +\infty)$ |
| 5 (c) | Não — veja a Parte 2 |
| 6 (a) | par |
| 6 (b) | par |
| 6 (c) | ímpar |
| 7 | Vértice $(-1,\thinspace 2)$; $\mathrm{Im} = (-\infty,\thinspace 2]$; cortes em $(0,1)$, $(-1-\sqrt2,\thinspace 0)$ e $(-1+\sqrt2,\thinspace 0)$ |
| 8 | $\mathrm{Im} = [2,\thinspace 6]$, período $\dfrac{2\pi}{3}$ |
| 9 (b) | $f^{-1}(x) = \dfrac{x+2}{x-3}$, $D = \mathbb{R}\setminus\lbrace 3 \rbrace$ |
| 10 (b) | Com $f : [-2,+\infty) \to [-1,+\infty)$: $f^{-1}(x) = -2 + \sqrt{x+1}$, $D = [-1,+\infty)$ |
| 11 (a) | $\dfrac{3\pi}{4}$ |
| 11 (b) | $-\dfrac{\pi}{3}$ |
| 11 (c) | $5$ |
| 12 (a) | $D = [-2,\thinspace 2]$, $\mathrm{Im} = [0,\thinspace 2]$ |
| 12 (b) | par |
| 12 (c) | não é injetora |
| 12 (d) | $f^{-1}(x) = \sqrt{4-x^2}$, $D = [0,\thinspace 2]$ — a função restrita é a **própria inversa** |

---
---

# 🧠 Parte 2 — Resoluções completas

### Questão 1

**(a)** O lado direito não é zero: passe tudo para a esquerda.

$$\frac{2x+1}{x-3} - 1 \geqslant 0 \ \Longrightarrow \ \frac{(2x+1) - (x-3)}{x-3} \geqslant 0 \ \Longrightarrow \ \frac{x+4}{x-3} \geqslant 0$$

Zeros: $-4$ (numerador, **entra**) e $3$ (denominador, **sai**).

| | $x<-4$ | $-4<x<3$ | $x>3$ |
| --- | :---: | :---: | :---: |
| $x+4$ | $-$ | $+$ | $+$ |
| $x-3$ | $-$ | $-$ | $+$ |
| quociente | $+$ | $-$ | $+$ |

$$S = (-\infty,\thinspace -4] \cup (3,\thinspace +\infty)$$

**(b)** "Módulo menor ou igual" vira dupla desigualdade:

$$-4 \leqslant 3-x \leqslant 4 \ \Longrightarrow \ -7 \leqslant -x \leqslant 1$$

Multiplicando por $-1$ — **inverte tudo**:

$$7 \geqslant x \geqslant -1 \ \Longrightarrow \ S = [-1,\thinspace 7]$$

*Leitura geométrica:* $\lvert 3-x \rvert = \lvert x-3 \rvert$ é a distância de $x$ até $3$; a condição pede distância $\leqslant 4$, ou seja, o intervalo de centro $3$ e raio $4$ ✔.

**(c)** Fatorando: $x^3-9x = x(x-3)(x+3)$. Zeros: $-3$, $0$, $3$ — todos entram.

| | $x<-3$ | $-3<x<0$ | $0<x<3$ | $x>3$ |
| --- | :---: | :---: | :---: | :---: |
| $x$ | $-$ | $-$ | $+$ | $+$ |
| $x-3$ | $-$ | $-$ | $-$ | $+$ |
| $x+3$ | $-$ | $+$ | $+$ | $+$ |
| produto | $-$ | $+$ | $-$ | $+$ |

$$S = (-\infty,\thinspace -3] \cup [0,\thinspace 3]$$

---

### Questão 2

A condição tem duas partes:

- $\lvert x-4 \rvert < 1$ dá $3 < x < 5$;
- $0 < \lvert x-4 \rvert$ obriga $\lvert x-4\rvert \neq 0$, isto é, $x \neq 4$.

$$S = (3,\thinspace 4) \cup (4,\thinspace 5)$$

**O papel do $0 <$:** ele **remove o centro** do intervalo. O conjunto descreve os pontos que estão a menos de $1$ de distância de $4$, **mas que não são o próprio $4$**.

> 💡 Essa é, literalmente, a condição que aparece na definição de limite: *"$x$ se aproxima de $4$ sem assumir o valor $4$"*. Você vai reencontrá-la na primeira página da [Unidade 2](../../02-limites-e-continuidade/README.md).

---

### Questão 3

**(a)** Duas exigências: $x+5 \geqslant 0 \Rightarrow x \geqslant -5$; e $x^2-4 \neq 0 \Rightarrow x \neq \pm 2$.

$$D(f) = [-5,\thinspace -2) \cup (-2,\thinspace 2) \cup (2,\thinspace +\infty)$$

**(b)** $x^2 - 3x \geqslant 0 \Rightarrow x(x-3) \geqslant 0$, com raízes $0$ e $3$ e concavidade para cima — positivo **fora** das raízes.

$$D(g) = (-\infty,\thinspace 0] \cup [3,\thinspace +\infty)$$

**(c)** Raiz **no denominador**: radicando estritamente positivo. $5 - x > 0 \Rightarrow x < 5$.

$$D(h) = (-\infty,\thinspace 5)$$

---

### Questão 4

**(a)**

$$f(x+h) = (x+h)^2 - 2(x+h) = x^2 + 2xh + h^2 - 2x - 2h$$

Subtraindo $f(x) = x^2-2x$:

$$f(x+h) - f(x) = 2xh + h^2 - 2h = h(2x + h - 2)$$

$$\frac{f(x+h)-f(x)}{h} = 2x + h - 2$$

*(Com $h \to 0$: $f'(x) = 2x-2$.)*

**(b)** Completando o quadrado: $f(x) = (x-1)^2 - 1$. Como $(x-1)^2 \geqslant 0$, o mínimo é $-1$, atingido em $x=1$.

$$\mathrm{Im}(f) = [-1,\thinspace +\infty)$$

---

### Questão 5

**(a)**

$$(f \circ g)(x) = f(x^2+1) = \sqrt{(x^2+1)-1} = \sqrt{x^2} = \lvert x \rvert$$

Domínio: é preciso ter $x \in D(g) = \mathbb{R}$ e $g(x) \in D(f) = [1,+\infty)$. Como $x^2+1 \geqslant 1$ sempre, nenhuma restrição aparece:

$$D(f \circ g) = \mathbb{R}$$

> ⚠️ Repare que $\sqrt{x^2} = \lvert x \rvert$, e **não** $x$. Responder $x$ aqui é o erro mais comum da questão.

**(b)**

$$(g \circ f)(x) = g\big(\sqrt{x-1}\big) = \big(\sqrt{x-1}\big)^2 + 1 = (x-1) + 1 = x$$

Domínio: é preciso que $f$ exista, ou seja, $x \geqslant 1$.

$$D(g \circ f) = [1,\thinspace +\infty)$$

**(c) Não são inversas.** Duas razões, qualquer uma já bastando:

1. A identidade $(g \circ f)(x) = x$ vale apenas em $[1,+\infty)$, e não em todo o domínio de $f$... na verdade, nem sequer a **outra** composta dá a identidade: $(f\circ g)(x) = \lvert x \rvert \neq x$ para $x<0$.
2. $g$ não é injetora em $\mathbb{R}$ ($g(-1) = g(1) = 2$), logo nem tem inversa nesse domínio.

> 💡 **A lição da questão:** uma composta dar $x$ **não** basta. É preciso que **as duas** compostas deem a identidade, cada uma no seu domínio. Aqui, $g$ restrita a $[0,+\infty)$ seria inversa de $f$ — mas $g$ em $\mathbb{R}$, não.

---

### Questão 6

**(a)** $f(-x) = (-x)^4 - \cos(-x) = x^4 - \cos x = f(x)$ → **par**.
(Usou-se que o cosseno é par.)

**(b)** $g(-x) = (-x)^3\mathrm{sen}(-x) = (-x^3)(-\mathrm{sen}\thinspace x) = x^3\mathrm{sen}\thinspace x = g(x)$ → **par**.

> 💡 Produto de duas ímpares dá **par** — os dois sinais negativos se cancelam. É a linha mais esquecida da tabela de propriedades.

**(c)** $h(-x) = e^{-x} - e^{x} = -(e^x - e^{-x}) = -h(x)$ → **ímpar**.
(É $2\mathrm{senh}\thinspace x$, o seno hiperbólico vezes $2$.)

---

### Questão 7

**(a)** Partindo de $y=x^2$:

| Passo | Expressão | Efeito |
| :---: | :---: | --- |
| 1 | $(x+1)^2$ | desloca $1$ para a **esquerda** |
| 2 | $-(x+1)^2$ | reflete no eixo $x$ — concavidade passa a ser para baixo |
| 3 | $2-(x+1)^2$ | sobe $2$ |

**(b)** Parábola com concavidade para baixo e **vértice em $(-1,\thinspace 2)$**.

**(c)** **Imagem:** como $-(x+1)^2 \leqslant 0$, tem-se $y \leqslant 2$:

$$\mathrm{Im} = (-\infty,\thinspace 2]$$

**Interseção com o eixo $y$** ($x=0$): $y = 2 - 1 = 1$, ponto $(0,\thinspace 1)$.

**Interseção com o eixo $x$** ($y=0$):

$$2 - (x+1)^2 = 0 \ \Longrightarrow \ (x+1)^2 = 2 \ \Longrightarrow \ x+1 = \pm\sqrt2 \ \Longrightarrow \ x = -1 \pm \sqrt2$$

Pontos $\big(-1-\sqrt2,\thinspace 0\big) \approx (-2{,}41;\thinspace 0)$ e $\big(-1+\sqrt2,\thinspace 0\big) \approx (0{,}41;\thinspace 0)$.

---

### Questão 8

**Imagem.** Partindo de $-1 \leqslant \mathrm{sen}(3x) \leqslant 1$:

$$-2 \leqslant 2\mathrm{sen}(3x) \leqslant 2$$
$$2 \geqslant -2\mathrm{sen}(3x) \geqslant -2 \qquad \text{(multiplicou por } -1\text{: inverteu)}$$
$$6 \geqslant 4 - 2\mathrm{sen}(3x) \geqslant 2$$

$$\mathrm{Im} = [2,\thinspace 6]$$

**Período.** Só o coeficiente **dentro** do seno conta:

$$T = \frac{2\pi}{3}$$

---

### Questão 9

**(a) Injetividade.** Suponha $f(x_1) = f(x_2)$:

$$\frac{3x_1+2}{x_1-1} = \frac{3x_2+2}{x_2-1}$$

Multiplicando em cruz (igualdade, denominadores não nulos):

$$(3x_1+2)(x_2-1) = (3x_2+2)(x_1-1)$$
$$3x_1x_2 - 3x_1 + 2x_2 - 2 = 3x_1x_2 - 3x_2 + 2x_1 - 2$$

Cancelando $3x_1x_2$ e $-2$:

$$-3x_1 + 2x_2 = -3x_2 + 2x_1 \ \Longrightarrow \ 5x_2 = 5x_1 \ \Longrightarrow \ x_1 = x_2 \quad \blacksquare$$

**(b) Inversa.**

$$y = \frac{3x+2}{x-1} \ \Longrightarrow \ y(x-1) = 3x+2 \ \Longrightarrow \ yx - y = 3x+2$$
$$x(y-3) = y+2 \ \Longrightarrow \ x = \frac{y+2}{y-3}$$

$$f^{-1}(x) = \frac{x+2}{x-3}, \qquad D(f^{-1}) = \mathbb{R}\setminus\lbrace 3 \rbrace$$

*Conferência:* $f(0) = -2$ e $f^{-1}(-2) = \frac{0}{-5} = 0$ ✔.

---

### Questão 10

**(a) Por que não é invertível.** Completando o quadrado: $f(x) = (x+2)^2 - 1$.

- **Não é injetora:** $f(-1) = 0 = f(-3)$, com $-1 \neq -3$ (o gráfico é simétrico em relação a $x=-2$).
- **Não é sobrejetora** em $\mathbb{R}$: $\mathrm{Im}(f) = [-1,+\infty)$, e nenhum $x$ produz, por exemplo, $y=-5$.

**(b) Restringindo.** Tome o ramo crescente, à direita do vértice, e ajuste o contradomínio:

$$f : [-2,\thinspace +\infty) \longrightarrow [-1,\thinspace +\infty)$$

$$y = (x+2)^2 - 1 \ \Longrightarrow \ (x+2)^2 = y+1 \ \Longrightarrow \ x+2 = +\sqrt{y+1}$$

(sinal positivo porque $x \geqslant -2$)

$$f^{-1}(x) = -2 + \sqrt{x+1}, \qquad D(f^{-1}) = [-1,\thinspace +\infty)$$

> 💡 O ramo esquerdo, $(-\infty,-2]$, daria $f^{-1}(x) = -2 - \sqrt{x+1}$. Qualquer um dos dois está certo, **desde que declarado**.

---

### Questão 11

**(a)** $\dfrac{5\pi}{4}$ está no terceiro quadrante, onde o cosseno é negativo:

$$\cos\frac{5\pi}{4} = -\frac{\sqrt2}{2}$$

O arco-cosseno devolve valores em $[0,\pi]$:

$$\arccos\left(-\frac{\sqrt2}{2}\right) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$$

> ⚠️ A resposta $\frac{5\pi}{4}$ está errada: ela não pertence a $[0,\pi]$, que é a imagem do arco-cosseno.

**(b)** Aqui $-\dfrac{\pi}{3}$ **pertence** a $\left[-\frac\pi2,\frac\pi2\right]$, que é o domínio restrito do seno. Então a identidade vale diretamente:

$$\mathrm{arcsen}\left(\mathrm{sen}\left(-\frac{\pi}{3}\right)\right) = -\frac{\pi}{3}$$

**(c)** $\mathrm{tg}\big(\mathrm{arctg}\thinspace u\big) = u$ para **todo** $u$ real, pois o domínio do arco-tangente é $\mathbb{R}$:

$$\mathrm{tg}\big(\mathrm{arctg}\thinspace 5\big) = 5$$

> 💡 Compare (a), (b) e (c): a composição "de fora para dentro" ($\mathrm{tg}\thinspace\circ\mathrm{arctg}$) sempre devolve o argumento; a composição "de dentro para fora" ($\mathrm{arccos}\thinspace\circ\cos$) só devolve se o ângulo estiver dentro da restrição.

---

### Questão 12 — síntese

**(a) Domínio e imagem.**

Radicando não negativo: $4 - x^2 \geqslant 0 \Rightarrow x^2 \leqslant 4 \Rightarrow \lvert x \rvert \leqslant 2$.

$$D(f) = [-2,\thinspace 2]$$

Para a imagem: $4-x^2$ varia de $0$ (em $x=\pm2$) a $4$ (em $x=0$), logo a raiz varia de $0$ a $2$.

$$\mathrm{Im}(f) = [0,\thinspace 2]$$

**(b) Paridade.** O domínio $[-2,2]$ é simétrico, e

$$f(-x) = \sqrt{4-(-x)^2} = \sqrt{4-x^2} = f(x)$$

**$f$ é par.** (Geometricamente, o gráfico é a semicircunferência superior de raio $2$ — simétrica em relação ao eixo $y$.)

**(c) Injetividade.** **Não é injetora:** $f(-1) = \sqrt3 = f(1)$, com $-1 \neq 1$. Aliás, **toda função par com domínio contendo algum $x \neq 0$ deixa de ser injetora** — é consequência imediata de $f(-x)=f(x)$.

**(d) Restringindo e invertendo.** Em $[0,2]$, a função é estritamente decrescente (logo injetora), com imagem $[0,2]$:

$$f : [0,\thinspace 2] \longrightarrow [0,\thinspace 2]$$

Invertendo:

$$y = \sqrt{4-x^2} \ \Longrightarrow \ y^2 = 4-x^2 \ \Longrightarrow \ x^2 = 4-y^2 \ \Longrightarrow \ x = +\sqrt{4-y^2}$$

(sinal positivo porque restringimos a $x \geqslant 0$)

$$f^{-1}(x) = \sqrt{4-x^2}, \qquad D(f^{-1}) = [0,\thinspace 2]$$

**Comentário.** A inversa tem **exatamente a mesma expressão** que $f$: a função restrita é a sua **própria inversa** — uma involução, como as do [Exercício 22 da Lista 1.4](../exercicios/lista-1.4-propostos.md).

Geometricamente isso é visível: o quarto de circunferência no primeiro quadrante é simétrico em relação à reta $y=x$. Refleti-lo nessa reta não muda nada — e refletir na reta $y=x$ é justamente o que inverter faz.

---

## 🎓 Fim da Unidade 1

Se você chegou até aqui resolvendo, está pronto para limites. A base que a Unidade 2 vai cobrar de você é exatamente esta:

- resolver inequação com quadro de sinais (todo cálculo de domínio e de sinal depende disso);
- ler $\lvert x - a \rvert < \delta$ como distância;
- saber que uma função pode ter limite onde **não** está definida (Questão 5, e o furo de $\frac{x^2-1}{x-1}$);
- reconhecer os gráficos elementares sem pensar.

➡️ **[Unidade 2 · Limites e Continuidade](../../02-limites-e-continuidade/README.md)**

---

| ← Revisão | 🏠 Índice | Próxima unidade → |
| :--- | :---: | ---: |
| [Revisão da Unidade 1](../exercicios/revisao-unidade-1.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [Unidade 2](../../02-limites-e-continuidade/README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
