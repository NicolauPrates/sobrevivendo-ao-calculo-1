# ✅ Gabarito — Lista 4.3

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 4.3](../exercicios/lista-4.3-propostos.md) · [Teoria 4.3](../4.3-regra-de-lhospital.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $1$ |
| 1 (b) | $1$ |
| 1 (c) | $1$ |
| 1 (d) | $0$ |
| 2 (a) | $0$ |
| 2 (b) | $0$ |
| 2 (c) | $\dfrac32$ |
| 3 (a) | **Não** se aplica; o limite é $2$ |
| 3 (b) | Aplica-se; o limite é $4$ |
| 3 (c) | Aplica-se uma vez; o limite é $+\infty$ |
| 4 (a) | $\dfrac12$ |
| 4 (b) | $\dfrac16$ |
| 5 (a) | $0$ |
| 5 (b) | $0$ |
| 5 (c) | $0$ |
| 6 | $\dfrac12$ |
| 7 | $e^2$ |
| 8 | (a) F · (b) V · (c) F · (d) F |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $\dfrac13$ |
| 10 | $0$ |
| 11 | $0$ |
| 12 | $\dfrac12$ |
| 13 | $e^{-3}$ |
| 14 | $e^{-1/2}$ |
| 15 | $1$ |
| 16 | $a=2$; o limite vale $-\dfrac43$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 17 | Demonstração — veja a Parte 2 |
| 18 | $1$ |
| 19 | Explicação — veja a Parte 2; o limite é $1$ |
| 20 | Demonstração — veja a Parte 2 |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** $\frac00$ ✔ → $\lim\dfrac{\cos x}{1} = 1$

**(b)** $\frac00$ ✔ → $\lim\dfrac{e^x}{1} = 1$

**(c)** $\frac00$ ✔ → $\lim\dfrac{1/x}{1} = 1$

**(d)** $\frac00$ ✔ → $\lim\dfrac{\mathrm{sen}\thinspace x}{1} = 0$

---

### Exercício 2

**(a)** $\frac{\infty}{\infty}$ ✔ → $\lim\dfrac{1/x}{2x} = \lim\dfrac{1}{2x^2} = 0$

**(b)** $\frac{\infty}{\infty}$ ✔ → $\lim\dfrac{1}{e^x} = 0$

**(c)** $\frac{\infty}{\infty}$ ✔ → $\lim\dfrac{6x}{4x-1}$, ainda $\frac\infty\infty$ → $\lim\dfrac{6}{4} = \dfrac32$

*(O atalho de [2.4](../../02-limites-e-continuidade/2.4-limites-infinitos-no-infinito-e-assintotas.md) — razão dos coeficientes líderes — dá o mesmo direto.)*

---

### Exercício 3

**(a)** Substituindo: $\dfrac{0+2}{0+1} = 2$. **Não há indeterminação**, logo L&#39;Hôspital **não se aplica**. (Aplicá-la daria $\frac11 = 1$ — errado.)

**(b)** Substituindo: $\frac00$ ✔ aplica-se:

$$\lim_{x\to2}\frac{2x}{1} = 4$$

*(Fatorando daria $x+2 \to 4$ ✔)*

**(c)** Substituindo: $\frac00$ ✔ aplica-se:

$$\lim_{x\to0^{+}}\frac{\cos x}{2x} = \frac{1}{0^{+}} = +\infty$$

Agora **não** há mais indeterminação: a resposta é $+\infty$, e aplicar a regra de novo seria erro.

---

### Exercício 4

**(a)** $\frac00$ ✔

$$\lim_{x\to0}\frac{e^x-1}{2x} \ \longrightarrow \ \frac00 \ \overset{\text{L'H}}{=} \ \lim_{x\to0}\frac{e^x}{2} = \frac12$$

**(b)** $\frac00$ ✔

$$\lim_{x\to0}\frac{1-\cos x}{3x^2} \ \longrightarrow \ \frac00 \ \overset{\text{L'H}}{=} \ \lim_{x\to0}\frac{\mathrm{sen}\thinspace x}{6x} = \frac16$$

*(Na última passagem usou-se $\frac{\mathrm{sen}\thinspace x}{x}\to1$; aplicar L&#39;Hôspital mais uma vez daria $\frac{\cos x}{6}\to\frac16$ igualmente.)*

---

### Exercício 5

**(a)** $0\cdot(-\infty)$. Reescreva:

$$x\ln x = \frac{\ln x}{1/x} \ \longrightarrow \ \frac{-\infty}{+\infty} \ \overset{\text{L'H}}{=} \ \lim_{x\to0^{+}}\frac{1/x}{-1/x^2} = \lim_{x\to0^{+}}(-x) = 0$$

**(b)** $\infty\cdot0$. Reescreva como $\dfrac{x}{e^x}$, que é o Exercício 2(b): limite $0$.

**(c)** Mesma técnica de (a):

$$\frac{\ln x}{1/x^2} \ \overset{\text{L'H}}{=} \ \lim_{x\to0^{+}}\frac{1/x}{-2/x^3} = \lim_{x\to0^{+}}\left(-\frac{x^2}{2}\right) = 0$$

---

### Exercício 6

Some as frações:

$$\frac{1}{\ln x} - \frac{1}{x-1} = \frac{(x-1) - \ln x}{(x-1)\ln x} \ \longrightarrow \ \frac00 \quad \checkmark$$

$$\overset{\text{L'H}}{=} \lim_{x\to1}\frac{1-\frac1x}{\ln x + \frac{x-1}{x}} = \lim_{x\to1}\frac{\frac{x-1}{x}}{\frac{x\ln x + x-1}{x}} = \lim_{x\to1}\frac{x-1}{x\ln x + x - 1}$$

Ainda $\frac00$ ✔

$$\overset{\text{L'H}}{=} \lim_{x\to1}\frac{1}{\ln x + 1 + 1} = \frac{1}{0+2} = \frac12$$

---

### Exercício 7

Forma $1^\infty$. Com $y = \left(1+\frac2x\right)^x$:

$$\ln y = x\ln\left(1+\frac2x\right) = \frac{\ln\left(1+\frac2x\right)}{1/x} \ \longrightarrow \ \frac00 \quad \checkmark$$

$$\overset{\text{L'H}}{=} \lim_{x\to+\infty}\frac{\dfrac{1}{1+\frac2x}\cdot\left(-\dfrac{2}{x^2}\right)}{-\dfrac{1}{x^2}} = \lim_{x\to+\infty}\frac{2}{1+\frac2x} = 2$$

**Voltando:** $y = e^{\ln y} \to e^2$.

---

### Exercício 8

**(a) Falso.** Só vale nas formas $\frac00$ e $\frac\infty\infty$.

**(b) Verdadeiro.**

**(c) Falso.** A regra é **condicional**: se o limite da direita não existe, ela nada afirma. O Exercício 19 é o contraexemplo.

**(d) Falso.** $0^0$ é **indeterminado**. O [Exercício Resolvido 3 da teoria](../4.3-regra-de-lhospital.md) mostra um caso em que dá $1$, mas outras combinações dão outros valores.

---

## Bloco B · Consolidação

### Exercício 9

$\frac00$ ✔

$$\overset{\text{L'H}}{=} \lim_{x\to0}\frac{\sec^2 x - 1}{3x^2} = \lim_{x\to0}\frac{\mathrm{tg}^2\thinspace x}{3x^2} = \frac13\lim_{x\to0}\left(\frac{\mathrm{tg}\thinspace x}{x}\right)^2 = \frac13\cdot1 = \frac13$$

*(usou-se $\sec^2 x - 1 = \mathrm{tg}^2\thinspace x$ e o limite de [2.3](../../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md))*

---

### Exercício 10

$\frac{\infty}{\infty}$ ✔

$$\overset{\text{L'H}}{=} \lim_{x\to+\infty}\frac{2\ln x\cdot\frac1x}{1} = \lim_{x\to+\infty}\frac{2\ln x}{x} \ \longrightarrow \ \frac{\infty}{\infty} \ \overset{\text{L'H}}{=} \ \lim_{x\to+\infty}\frac{2/x}{1} = 0$$

---

### Exercício 11

Forma $0\cdot(-\infty)$. Reescreva com o **logaritmo em cima** (ele é o fator difícil):

$$\mathrm{sen}\thinspace x\cdot\ln x = \frac{\ln x}{\mathrm{cossec}\thinspace x} \ \longrightarrow \ \frac{-\infty}{+\infty} \quad \checkmark$$

$$\overset{\text{L'H}}{=} \lim_{x\to0^{+}}\frac{1/x}{-\mathrm{cossec}\thinspace x\mathrm{cotg}\thinspace x} = \lim_{x\to0^{+}}\frac{-\mathrm{sen}^2\thinspace x}{x\cos x} = \lim_{x\to0^{+}}\left(-\frac{\mathrm{sen}\thinspace x}{x}\cdot\frac{\mathrm{sen}\thinspace x}{\cos x}\right) = -1\cdot 0 = 0$$

---

### Exercício 12

$$\frac1x - \frac{1}{e^x-1} = \frac{e^x-1-x}{x\big(e^x-1\big)} \ \longrightarrow \ \frac00 \quad \checkmark$$

$$\overset{\text{L'H}}{=} \lim_{x\to0}\frac{e^x-1}{\big(e^x-1\big)+xe^x} \ \longrightarrow \ \frac00 \ \overset{\text{L'H}}{=} \ \lim_{x\to0}\frac{e^x}{e^x+e^x+xe^x} = \frac{1}{2} $$

---

### Exercício 13

Forma $1^\infty$. Com $y = \left(1-\frac3x\right)^x$:

$$\ln y = \frac{\ln\left(1-\frac3x\right)}{1/x} \ \overset{\text{L'H}}{=} \ \lim_{x\to+\infty}\frac{\dfrac{1}{1-\frac3x}\cdot\dfrac{3}{x^2}}{-\dfrac{1}{x^2}} = \lim_{x\to+\infty}\frac{-3}{1-\frac3x} = -3$$

**Voltando:** $y \to e^{-3}$.

> 💡 **O padrão geral:** $\lim_{x\to+\infty}\left(1+\frac kx\right)^x = e^k$. Vale decorar — ele aparece em juros compostos, decaimento radioativo e crescimento populacional.

---

### Exercício 14

Forma $1^\infty$. Com $y = (\cos x)^{1/x^2}$:

$$\ln y = \frac{\ln(\cos x)}{x^2} \ \longrightarrow \ \frac00 \quad \checkmark$$

$$\overset{\text{L'H}}{=} \lim_{x\to0}\frac{\dfrac{-\mathrm{sen}\thinspace x}{\cos x}}{2x} = \lim_{x\to0}\frac{-\mathrm{tg}\thinspace x}{2x} = -\frac12$$

**Voltando:** $y \to e^{-1/2} = \dfrac{1}{\sqrt e} \approx 0{,}607$.

---

### Exercício 15

Forma $\infty\cdot0$. **Mudança de variável** é o caminho mais limpo: seja $t = \frac1x$, com $t\to0^{+}$ quando $x\to+\infty$:

$$x\left(e^{1/x}-1\right) = \frac{e^t-1}{t} \ \longrightarrow \ 1$$

pelo Exercício 1(b).

---

### Exercício 16

**Primeira aplicação** (forma $\frac00$ ✔):

$$\lim_{x\to0}\frac{a\cos(ax) - 2}{3x^2}$$

O denominador tende a $0$. Para o limite ser **finito**, o numerador precisa tender a $0$ também:

$$a\cos 0 - 2 = a - 2 = 0 \ \Longrightarrow \ a = 2$$

**Com $a=2$**, a forma volta a ser $\frac00$:

$$\lim_{x\to0}\frac{2\cos(2x)-2}{3x^2} \ \overset{\text{L'H}}{=} \ \lim_{x\to0}\frac{-4\mathrm{sen}(2x)}{6x} = -\frac46\cdot\lim_{x\to0}\frac{\mathrm{sen}(2x)}{x} = -\frac23\cdot2 = -\frac43$$

**Resposta.** $a=2$ e o limite vale $-\dfrac43$.

---

## Bloco C · Desafio

### Exercício 17

Cada aplicação da regra **baixa em um** o grau do numerador, e deixa o denominador inalterado:

$$\lim_{x\to+\infty}\frac{x^n}{e^x} \ \overset{\text{L'H}}{=} \ \lim\frac{n\thinspace x^{n-1}}{e^x} \ \overset{\text{L'H}}{=} \ \lim\frac{n(n-1)x^{n-2}}{e^x} \ \overset{\text{L'H}}{=} \ \cdots$$

A cada passo a forma continua sendo $\frac{\infty}{\infty}$, de modo que a regra pode ser reaplicada. Após **$n$ aplicações**, o numerador vira a constante $n!$:

$$\lim_{x\to+\infty}\frac{n!}{e^x} = 0$$

pois o denominador cresce sem limitação e o numerador é fixo. $\blacksquare$

> 💡 **É a hierarquia do infinito demonstrada:** a exponencial vence **qualquer** potência, por maior que seja o expoente.

---

### Exercício 18

Forma $\infty^0$. Com $y = \left(\dfrac1x\right)^{\mathrm{sen}\thinspace x}$:

$$\ln y = \mathrm{sen}\thinspace x\cdot\ln\frac1x = -\mathrm{sen}\thinspace x\cdot\ln x$$

Pelo Exercício 11, $\mathrm{sen}\thinspace x\ln x \to 0$, logo $\ln y \to 0$.

**Voltando:** $y \to e^0 = 1$.

---

### Exercício 19

**Por que a regra não conclui nada.** A forma é $\frac{\infty}{\infty}$, então a regra **pode** ser tentada:

$$\lim_{x\to+\infty}\frac{1+\cos x}{1}$$

Mas esse limite **não existe** — $\cos x$ oscila entre $-1$ e $1$ indefinidamente. E o teorema é **condicional**: ele afirma a igualdade "**desde que o limite da direita exista**". Como não existe, a regra simplesmente não diz nada. Em particular, **não** se pode concluir que o limite original não existe.

**Calculando por outro método.** Separe a fração:

$$\frac{x+\mathrm{sen}\thinspace x}{x} = 1 + \frac{\mathrm{sen}\thinspace x}{x}$$

E $\frac{\mathrm{sen}\thinspace x}{x}\to0$ quando $x\to+\infty$ (teorema do anulamento, [2.3](../../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md)). Logo

$$\lim_{x\to+\infty}\frac{x+\mathrm{sen}\thinspace x}{x} = 1 + 0 = 1$$

> 💡 **A moral:** L&#39;Hôspital pode **falhar em concluir** mesmo quando o limite existe. É uma ferramenta poderosa, não universal — e é por isso que as técnicas da Unidade 2 continuam valendo.

---

### Exercício 20

Forma $0\cdot(-\infty)$. Reescreva com o logaritmo no numerador:

$$x^{\alpha}\ln x = \frac{\ln x}{x^{-\alpha}} \ \longrightarrow \ \frac{-\infty}{+\infty} \quad \checkmark$$

$$\overset{\text{L'H}}{=} \lim_{x\to0^{+}}\frac{1/x}{-\alpha\thinspace x^{-\alpha-1}} = \lim_{x\to0^{+}}\frac{x^{\alpha+1}}{-\alpha\thinspace x} = \lim_{x\to0^{+}}\left(-\frac{x^{\alpha}}{\alpha}\right) = 0$$

pois $\alpha>0$ garante $x^\alpha \to 0$. $\blacksquare$

> 💡 **Em palavras:** qualquer potência positiva de $x$, por menor que seja o expoente, **domina** o $\ln x$ perto de zero. É a versão "no zero" da hierarquia do infinito — e explica por que gráficos como $y = x\ln x$ chegam mansamente à origem, apesar de o logaritmo explodir.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 4.3](../exercicios/lista-4.3-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [4.3 · Teoria](../4.3-regra-de-lhospital.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
