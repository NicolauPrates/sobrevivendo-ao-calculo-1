# ✅ Gabarito — Lista 2.4

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 2.4](../exercicios/lista-2.4-propostos.md) · [Teoria 2.4](../2.4-limites-infinitos-no-infinito-e-assintotas.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $+\infty$ |
| 1 (b) | $-\infty$ |
| 1 (c) | $+\infty$ |
| 1 (d) | $+\infty$ |
| 2 (a) | $0$ |
| 2 (b) | $0$ |
| 2 (c) | $2$ |
| 2 (d) | $-3$ |
| 3 (a) | $\dfrac23$ |
| 3 (b) | $0$ |
| 3 (c) | $+\infty$ |
| 3 (d) | $2$ |
| 4 (a) | determinada: $+\infty$ |
| 4 (b) | **indeterminada** |
| 4 (c) | **indeterminada** |
| 4 (d) | determinada: $0$ |
| 4 (e) | **indeterminada** |
| 4 (f) | **indeterminada** |
| 5 (a) | $x=3$ e $x=-3$ |
| 5 (b) | só $x=-1$ (em $x=1$ há um furo) |
| 5 (c) | nenhuma |
| 6 (a) | $y=3$ |
| 6 (b) | $y=0$ |
| 6 (c) | nenhuma |
| 7 | $1$ e $-1$ |
| 8 | (a) F · (b) V · (c) V · (d) F |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $\dfrac32$ |
| 10 | $+\infty$ |
| 11 | $-\infty$ pela esquerda, $+\infty$ pela direita |
| 12 | $3$ |
| 13 | Verticais $x=2$ e $x=-2$; horizontal $y=1$ |
| 14 | Vertical $x=1$; oblíqua $y=x+3$ |
| 15 | $-1$ |
| 16 | $-\infty$ e $+\infty$; assíntota vertical $x=0$ |
| 17 | $0$ |
| 18 | $\dfrac14$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | $\dfrac12$ |
| 20 | $1$ |
| 21 | $a=1$ e $b=-1$ |
| 22 | A reta $y=x$ é assíntota oblíqua; a curva fica **abaixo** dela quando $x\to+\infty$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** Para $x>1$, o denominador $x-1$ é positivo pequeno ($0^{+}$), e o numerador é $1>0$:

$$\frac{1}{0^{+}} = +\infty$$

**(b)** Para $x<1$, o denominador é $0^{-}$:

$$\frac{1}{0^{-}} = -\infty$$

**(c)** $x^2$ é sempre positivo, logo é $0^{+}$ pelos **dois** lados: $\dfrac{1}{0^{+}} = +\infty$. Aqui o limite bilateral pode ser escrito, porque os dois lados concordam.

**(d)** Mesmo raciocínio: $(x+2)^2 \to 0^{+}$ pelos dois lados, e o numerador é $3>0$. Logo $+\infty$.

---

### Exercício 2

Todos saem do Teorema 2.4.1 ($\frac{1}{x^n} \to 0$):

**(a)** $0$ &nbsp;&nbsp; **(b)** $0$ &nbsp;&nbsp; **(c)** $2 + 0 = 2$ &nbsp;&nbsp; **(d)** $0 - 3 = -3$

---

### Exercício 3

**(a)** Graus iguais. Dividindo por $x$:

$$\frac{2+\frac1x}{3-\frac5x} \ \longrightarrow \ \frac{2}{3}$$

**(b)** Grau de cima ($2$) menor que o de baixo ($3$). Dividindo por $x^3$:

$$\frac{\frac1x + \frac{1}{x^3}}{1+\frac{2}{x^3}} \ \longrightarrow \ \frac{0}{1} = 0$$

**(c)** Grau de cima maior. Dividindo por $x^2$:

$$\frac{x - \frac{1}{x^2}}{1+\frac{1}{x^2}} \ \longrightarrow \ \frac{+\infty}{1} = +\infty$$

**(d)** Graus iguais, razão dos líderes $\frac42 = 2$. (O resultado é o mesmo em $-\infty$, já que ambos os graus são pares.)

---

### Exercício 4

| | Classificação | Resultado |
| :---: | --- | :---: |
| (a) $\infty+\infty$ | determinada | $+\infty$ |
| (b) $\infty-\infty$ | **indeterminada** | — |
| (c) $0\cdot\infty$ | **indeterminada** | — |
| (d) $\frac{k}{\infty}$ | determinada | $0$ |
| (e) $\frac{\infty}{\infty}$ | **indeterminada** | — |
| (f) $1^{\infty}$ | **indeterminada** | — |

> 💡 Em (f), a intuição "$1$ elevado a qualquer coisa é $1$" falha porque a base **não é exatamente** $1$ — ela apenas tende a $1$, enquanto o expoente explode. O exemplo clássico é $\left(1+\frac1x\right)^x \to e$.

---

### Exercício 5

**(a)** $x^2-9 = (x-3)(x+3)$ zera em $\pm3$, e o numerador ($1$) nunca zera. **Assíntotas: $x=3$ e $x=-3$.**

**(b)** Simplifique primeiro:

$$\frac{x-1}{x^2-1} = \frac{x-1}{(x-1)(x+1)} = \frac{1}{x+1} \qquad (x\neq1)$$

Só $x=-1$ é assíntota. Em $x=1$ há um **furo**: o limite ali vale $\frac{1}{2}$.

**(c)** $x^2+1$ nunca zera em $\mathbb{R}$. **Não há assíntota vertical.**

---

### Exercício 6

**(a)** Graus iguais: $\lim_{x\to\pm\infty}\frac{3x}{x+2} = 3$. **Assíntota: $y=3$.**

**(b)** Grau de cima menor: limite $0$. **Assíntota: $y=0$.**

**(c)** Grau de cima maior: o limite é $\pm\infty$. **Não há assíntota horizontal** (há oblíqua — veja o Exercício 14).

---

### Exercício 7

$$\lim_{x\to+\infty}\frac{\sqrt{x^2+1}}{x} = 1 \qquad \lim_{x\to-\infty}\frac{\sqrt{x^2+1}}{x} = -1$$

**Por quê.** Pondo $x^2$ em evidência dentro da raiz:

$$\sqrt{x^2+1} = \lvert x\rvert\sqrt{1+\frac{1}{x^2}}$$

Para $x\to+\infty$, $\lvert x\rvert = x$ e a razão tende a $+1$. Para $x\to-\infty$, $\lvert x \rvert = -x$ e a razão tende a $-1$.

**Confirmação sem conta:** a raiz é sempre **positiva**; o denominador é positivo à direita e negativo à esquerda. Logo as respostas **têm** de ter sinais opostos.

---

### Exercício 8

**(a) Falso.** $+\infty$ não é número real: a notação diz que o limite **não existe**, e descreve como ele falha.

**(b) Verdadeiro.** O Exercício 7 é um exemplo: $y=1$ e $y=-1$.

**(c) Verdadeiro.** A função $\operatorname{tg} x$ tem uma assíntota em cada $\frac{\pi}{2}+k\pi$ — infinitas.

**(d) Falso.** Pode haver cancelamento, e aí o ponto é apenas um furo (Exercício 5(b)).

---

## Bloco B · Consolidação

### Exercício 9

Forma $\infty-\infty$: multiplique pelo conjugado.

$$\sqrt{x^2+3x}-x = \frac{(x^2+3x)-x^2}{\sqrt{x^2+3x}+x} = \frac{3x}{\sqrt{x^2+3x}+x}$$

Dividindo por $x>0$ (e, dentro da raiz, por $x^2$):

$$= \frac{3}{\sqrt{1+\frac3x}+1} \ \longrightarrow \ \frac{3}{2}$$

---

### Exercício 10

Agora $x\to-\infty$, e **não há indeterminação**: o $-x$ é positivo e grande, então a expressão é soma de duas quantidades positivas grandes.

Em detalhe, com $\sqrt{x^2+3x} = \lvert x\rvert\sqrt{1+\frac3x} = -x\sqrt{1+\frac3x}$:

$$\sqrt{x^2+3x}-x = -x\sqrt{1+\frac3x} - x = -x\left(\sqrt{1+\frac3x}+1\right)$$

Quando $x\to-\infty$: $-x \to +\infty$ e o parêntese tende a $2$. Logo

$$\lim_{x\to-\infty}\left(\sqrt{x^2+3x}-x\right) = +\infty$$

> 💡 **A comparação com o Exercício 9 é a lição da questão.** A **mesma expressão** dá $\frac32$ em um extremo e $+\infty$ no outro. Nunca presuma que o comportamento nos dois infinitos é igual.

---

### Exercício 11

Em $x=2$, o numerador vale $4 \neq 0$ e o denominador zera.

- **Pela esquerda** ($x<2$): $x-2 = 0^{-}$, e $\frac{4}{0^{-}} = -\infty$.
- **Pela direita** ($x>2$): $x-2 = 0^{+}$, e $\frac{4}{0^{+}} = +\infty$.

A reta $x=2$ é assíntota vertical.

---

### Exercício 12

Dentro da raiz, a maior potência é $x^4$, cuja raiz é $x^2$ (positivo, qualquer que seja o sinal de $x$):

$$\sqrt{x^4+1} = x^2\sqrt{1+\frac{1}{x^4}}$$

Logo

$$\frac{3x^2-2x}{\sqrt{x^4+1}} = \frac{3x^2-2x}{x^2\sqrt{1+\frac{1}{x^4}}} = \frac{3-\frac2x}{\sqrt{1+\frac{1}{x^4}}} \ \longrightarrow \ \frac{3}{1} = 3$$

> 💡 Aqui **não** houve problema de sinal, porque $\sqrt{x^4} = x^2$ já é positivo. O cuidado com o módulo é específico de $\sqrt{x^2}$ (e, em geral, de raízes de potências **ímpares** depois de fatoradas).

---

### Exercício 13

**Verticais.** $x^2-4 = (x-2)(x+2)$ zera em $\pm2$; o numerador $x^2-1$ vale $3$ em $x=2$ e $3$ em $x=-2$ — não zera. **Assíntotas: $x=2$ e $x=-2$.**

**Horizontal.** Graus iguais, razão dos líderes $\frac11 = 1$:

$$\lim_{x\to\pm\infty}\frac{x^2-1}{x^2-4} = 1$$

**Assíntota: $y=1$**, nos dois extremos.

**Oblíqua.** Não há, pois já existe horizontal.

---

### Exercício 14

**Vertical.** O denominador zera em $x=1$, e o numerador vale $1+2 = 3 \neq 0$. **Assíntota: $x=1$.**

**Horizontal.** Grau de cima ($2$) maior que o de baixo ($1$): não há.

**Oblíqua.** Divida:

$$\frac{x^2+2x}{x-1} = x+3+\frac{3}{x-1}$$

*(Conferindo: $(x-1)(x+3) = x^2+2x-3$; somando $3$, volta a $x^2+2x$ ✔.)*

Como $\frac{3}{x-1}\to0$, **a assíntota oblíqua é $y = x+3$**, nos dois extremos.

---

### Exercício 15

A exponencial dominante é $3^x$. Dividindo tudo por ela:

$$\frac{2^x-3^x}{3^x+1} = \frac{\left(\frac23\right)^x - 1}{1 + \left(\frac13\right)^x} \ \longrightarrow \ \frac{0-1}{1+0} = -1$$

---

### Exercício 16

$$\lim_{x\to0^{+}}\ln x = -\infty \qquad \lim_{x\to+\infty}\ln x = +\infty$$

O gráfico tem **assíntota vertical $x=0$** (o eixo $y$). Não há assíntota horizontal: embora $\ln x$ cresça devagar, ele cresce **sem limitação**.

> ⚠️ Note que só faz sentido o limite **lateral à direita** em $0$: o domínio de $\ln$ é $(0,+\infty)$.

---

### Exercício 17

Use o teorema do anulamento ([2.3](../2.3-teorema-do-sanduiche.md)), que também vale no infinito: $\operatorname{sen} x$ é **limitado** e $\frac1x \to 0$.

Formalmente, para $x>0$:

$$-\frac1x \ \leqslant \ \frac{\operatorname{sen} x}{x} \ \leqslant \ \frac1x$$

e as duas pontas tendem a $0$. Logo

$$\lim_{x\to+\infty}\frac{\operatorname{sen} x}{x} = 0$$

> ⚠️ **Não confunda com o limite fundamental.** Em $x\to0$, essa mesma expressão tende a $1$; em $x\to+\infty$, tende a $0$. O que muda é que, no infinito, não há indeterminação alguma: é "limitado dividido por algo que explode".

---

### Exercício 18

Conjugado:

$$\sqrt{4x^2+x}-2x = \frac{(4x^2+x)-4x^2}{\sqrt{4x^2+x}+2x} = \frac{x}{\sqrt{4x^2+x}+2x}$$

Com $x>0$, tem-se $\sqrt{4x^2+x} = 2x\sqrt{1+\frac{1}{4x}}$. Dividindo numerador e denominador por $x$:

$$= \frac{1}{2\sqrt{1+\frac{1}{4x}}+2} \ \longrightarrow \ \frac{1}{2+2} = \frac14$$

---

## Bloco C · Desafio

### Exercício 19

A forma é $\infty \cdot 0$ — indeterminada. Comece pelo conjugado do parêntese:

$$\sqrt{x^2+1}-x = \frac{1}{\sqrt{x^2+1}+x}$$

Logo

$$x\left(\sqrt{x^2+1}-x\right) = \frac{x}{\sqrt{x^2+1}+x}$$

Dividindo por $x>0$:

$$= \frac{1}{\sqrt{1+\frac{1}{x^2}}+1} \ \longrightarrow \ \frac{1}{1+1} = \frac12$$

**Resposta.** $\dfrac12$

---

### Exercício 20

Separe o fator que você já sabe tratar:

$$\frac{x^2\operatorname{sen}\frac1x}{x+1} = \underbrace{\left(x\operatorname{sen}\frac1x\right)}_{\to\,1}\cdot\underbrace{\frac{x}{x+1}}_{\to\,1}$$

**Por que o primeiro fator tende a $1$:** faça $u = \frac1x$. Quando $x\to+\infty$, tem-se $u\to0^{+}$, e

$$x\operatorname{sen}\frac1x = \frac{\operatorname{sen} u}{u} \ \longrightarrow \ 1$$

que é o limite fundamental de [2.3](../2.3-teorema-do-sanduiche.md).

**Resposta.** $1 \cdot 1 = 1$

---

### Exercício 21

Divida $x^2+1$ por $x+1$:

$$\frac{x^2+1}{x+1} = x - 1 + \frac{2}{x+1}$$

*(Conferindo: $(x+1)(x-1) = x^2-1$; somando $2$, volta a $x^2+1$ ✔.)*

Então

$$\frac{x^2+1}{x+1} - ax - b = (1-a)x - (1+b) + \frac{2}{x+1}$$

Para que isso tenda a $0$, é preciso que o termo em $x$ e o termo constante **desapareçam**:

$$1-a = 0 \ \Longrightarrow \ a = 1 \qquad\qquad -(1+b) = 0 \ \Longrightarrow \ b = -1$$

**Resposta.** $a = 1$ e $b = -1$.

**Interpretação geométrica.** A condição $\lim\big[f(x) - (ax+b)\big] = 0$ é **exatamente a definição** de assíntota oblíqua. Portanto a reta $y = x-1$ é a assíntota oblíqua de $f(x) = \frac{x^2+1}{x+1}$.

---

### Exercício 22

**A assíntota.** Calcule a diferença entre a função e a reta candidata:

$$f(x) - x = \frac{x^3}{x^2+1} - x = \frac{x^3 - x\big(x^2+1\big)}{x^2+1} = \frac{-x}{x^2+1}$$

Quando $x\to\pm\infty$, essa diferença tende a $0$ (grau de cima menor que o de baixo). Logo **$y=x$ é assíntota oblíqua** nos dois extremos. $\blacksquare$

**Acima ou abaixo?** Basta olhar o **sinal** da diferença:

$$f(x) - x = \frac{-x}{x^2+1}$$

Para $x>0$, essa expressão é **negativa**: $f(x) < x$, isto é, a curva está **abaixo** da reta.

*(E, por simetria, para $x<0$ a diferença é positiva: a curva fica **acima** da reta quando $x\to-\infty$. Coerente com $f$ ser uma função ímpar.)*

> 💡 **Esse cálculo do sinal é o que a assíntota não conta.** Saber que a curva se aproxima da reta é uma coisa; saber **de que lado** ela se aproxima é outra — e é essa segunda informação que faz o esboço ficar correto em [4.4](../../04-aplicacoes-das-derivadas/4.4-crescimento-concavidade-e-esboco-de-graficos.md).

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 2.4](../exercicios/lista-2.4-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [2.4 · Teoria](../2.4-limites-infinitos-no-infinito-e-assintotas.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
