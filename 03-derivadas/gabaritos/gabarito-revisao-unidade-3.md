# ✅ Gabarito — Revisão da Unidade 3

> **Corrija com honestidade.** Para cada questão errada, classifique a causa: não sabia a regra, sabia e errei a aplicação, montei certo e errei a conta, ou acabou o tempo.

➡️ [Voltar para a Revisão](../exercicios/revisao-unidade-3.md)

---

# ✅ Parte 1 — Respostas finais

| Questão | Resposta |
| :---: | --- |
| 1 | $f'(x) = 4x-1$ |
| 2 | Tangente $y = 4x-7$; normal $y = -\dfrac{x}{4}+\dfrac32$ |
| 3 (a) | $3e^x - \dfrac2x + \cos x$ |
| 3 (b) | $2x\cos x - x^2\operatorname{sen} x$ |
| 3 (c) | $\dfrac{1-2\ln x}{x^3}$ |
| 4 (a) | $2x\cos\big(x^2+1\big)$ |
| 4 (b) | $e^{3x}\big[3\cos(2x) - 2\operatorname{sen}(2x)\big]$ |
| 4 (c) | $\dfrac{1}{2x\sqrt{1+\ln x}}$ |
| 5 (a) | $\dfrac{dy}{dx} = \dfrac{2y-x^2}{y^2-2x}$ |
| 5 (b) | $y = -x+6$ |
| 6 | $\dfrac15$ |
| 7 (a) | $\dfrac{2}{1+4x^2}$ |
| 7 (b) | $\arccos x - \dfrac{x}{\sqrt{1-x^2}}$ |
| 7 (c) | $\dfrac{3\big(\operatorname{arctg} x\big)^2}{1+x^2}$ |
| 8 | $x^{2x}\big(2\ln x + 2\big)$ |
| 9 | Sim, é derivável; $f'(2) = 4$ |
| 10 | $\dfrac{1}{\pi} \approx 0{,}32$ cm/s |
| 11 (a) | $v = 6t^2-18t+12$; $a = 12t-18$ |
| 11 (b) | $t=1$ s e $t=2$ s |
| 11 (c) | acelerando em $(1;\thinspace 1{,}5)$ e em $(2,\thinspace +\infty)$ |
| 12 (a) | $f'(x) = e^{-x}(1-x)$ |
| 12 (b) | $\left(1,\thinspace \dfrac1e\right)$ |
| 12 (c) | $f''(x) = e^{-x}(x-2)$ |
| 12 (d) | Verificação — veja a Parte 2 |

---
---

# 🧠 Parte 2 — Resoluções completas

### Questão 1

$$f(x+h) = 2(x+h)^2-(x+h) = 2x^2+4xh+2h^2-x-h$$

Subtraindo $f(x) = 2x^2-x$:

$$f(x+h)-f(x) = 4xh+2h^2-h = h(4x+2h-1)$$

$$f'(x) = \lim_{h\to0}(4x+2h-1) = 4x-1$$

---

### Questão 2

**Ponto:** $f(2) = 8-8+1 = 1$, logo $P = (2,\thinspace 1)$.

**Inclinação:** $f'(x) = 3x^2-4x$, logo $f'(2) = 12-8 = 4$.

**Tangente:** $y - 1 = 4(x-2) \Rightarrow y = 4x-7$

**Normal:** inclinação $-\dfrac14$:

$$y - 1 = -\frac14(x-2) \ \Longrightarrow \ y = -\frac{x}{4}+\frac32$$

---

### Questão 3

**(a)** $f'(x) = 3e^x - \dfrac2x + \cos x$

**(b)** $f'(x) = 2x\cos x + x^2(-\operatorname{sen} x) = 2x\cos x - x^2\operatorname{sen} x$

**(c)** Pela regra do quociente:

$$f'(x) = \frac{\frac1x\cdot x^2 - \ln x\cdot 2x}{x^4} = \frac{x - 2x\ln x}{x^4} = \frac{x(1-2\ln x)}{x^4} = \frac{1-2\ln x}{x^3}$$

---

### Questão 4

**(a)** $f'(x) = \cos\big(x^2+1\big)\cdot 2x = 2x\cos\big(x^2+1\big)$

**(b)** Regra do produto, com cadeia nos dois fatores:

$$f'(x) = 3e^{3x}\cos(2x) + e^{3x}\big(-2\operatorname{sen}(2x)\big) = e^{3x}\big[3\cos(2x)-2\operatorname{sen}(2x)\big]$$

**(c)**

$$f'(x) = \frac{1}{2\sqrt{1+\ln x}}\cdot\frac1x = \frac{1}{2x\sqrt{1+\ln x}}$$

---

### Questão 5

**(a)** Derivando implicitamente, com a regra do **produto** no lado direito:

$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$

Agrupando:

$$\frac{dy}{dx}\big(3y^2-6x\big) = 6y-3x^2 \ \Longrightarrow \ \frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x} = \frac{2y-x^2}{y^2-2x}$$

**(b)** *Confirmando o ponto:* $27+27 = 54$ e $6(3)(3) = 54$ ✔

$$\left.\frac{dy}{dx}\right|_{(3,3)} = \frac{6-9}{9-6} = \frac{-3}{3} = -1$$

$$y - 3 = -1(x-3) \ \Longrightarrow \ y = -x+6$$

---

### Questão 6

$$f'(x) = 3x^2+2 \ \Longrightarrow \ f'(1) = 5$$

Como $f(1)=4$, tem-se $f^{-1}(4) = 1$ e

$$\big(f^{-1}\big)'(4) = \frac{1}{f'(1)} = \frac15$$

---

### Questão 7

**(a)** $f'(x) = \dfrac{2}{1+(2x)^2} = \dfrac{2}{1+4x^2}$

**(b)** $f'(x) = 1\cdot\arccos x + x\cdot\left(-\dfrac{1}{\sqrt{1-x^2}}\right) = \arccos x - \dfrac{x}{\sqrt{1-x^2}}$

**(c)** $f'(x) = 3\big(\operatorname{arctg} x\big)^2\cdot\dfrac{1}{1+x^2} = \dfrac{3\big(\operatorname{arctg} x\big)^2}{1+x^2}$

---

### Questão 8

$$\ln y = 2x\ln x$$

Derivando (produto à direita):

$$\frac{y'}{y} = 2\ln x + 2x\cdot\frac1x = 2\ln x + 2$$

$$y' = x^{2x}\big(2\ln x + 2\big) = 2x^{2x}\big(\ln x + 1\big)$$

---

### Questão 9

**1. Continuidade** (pré-requisito):

$$\lim_{x\to2^{-}}\big(x^2+1\big) = 5 \qquad f(2) = 4(2)-3 = 5 \quad \checkmark$$

**2. Derivadas laterais:**

$$f'_{-}(2) = \big(x^2+1\big)'\big|_{x=2} = 2(2) = 4$$
$$f'_{+}(2) = (4x-3)'\big|_{x=2} = 4$$

As duas coincidem.

**Resposta.** $f$ é derivável em $x=2$, com $f'(2) = 4$.

> 💡 Geometricamente: a parábola e a reta se encontram em $(2,5)$ **com a mesma inclinação** — a reta é justamente a tangente à parábola ali. Por isso a emenda é lisa, sem bico.

---

### Questão 10

$$A = \pi r^2 \ \Longrightarrow \ \frac{dA}{dt} = 2\pi r\frac{dr}{dt}$$

Quando $A = 9\pi$: $\pi r^2 = 9\pi \Rightarrow r = 3$ cm. Substituindo:

$$6 = 2\pi(3)\frac{dr}{dt} = 6\pi\frac{dr}{dt} \ \Longrightarrow \ \frac{dr}{dt} = \frac{1}{\pi} \approx 0{,}32 \ \text{cm/s}$$

---

### Questão 11

**(a)**

$$v(t) = 6t^2-18t+12 = 6\big(t^2-3t+2\big) = 6(t-1)(t-2)$$
$$a(t) = 12t-18 = 6(2t-3)$$

**(b)** $v=0$ em $t=1$ s e $t=2$ s.

**(c)** Quadro de sinais (com $a=0$ em $t=1{,}5$):

| | $0<t<1$ | $1<t<1{,}5$ | $1{,}5<t<2$ | $t>2$ |
| --- | :---: | :---: | :---: | :---: |
| $v$ | $+$ | $-$ | $-$ | $+$ |
| $a$ | $-$ | $-$ | $+$ | $+$ |
| mesmo sinal? | não | **sim** | não | **sim** |

**Resposta.** Acelerando em $(1;\thinspace 1{,}5)$ e em $(2,\thinspace +\infty)$; freando em $(0,\thinspace 1)$ e em $(1{,}5;\thinspace 2)$.

---

### Questão 12 — síntese

**(a)** Regra do produto, com cadeia em $e^{-x}$:

$$f'(x) = 1\cdot e^{-x} + x\cdot\big(-e^{-x}\big) = e^{-x}(1-x)$$

**(b)** Tangente horizontal exige $f'(x)=0$. Como $e^{-x} > 0$ sempre:

$$1-x = 0 \ \Longrightarrow \ x = 1$$

A ordenada é $f(1) = 1\cdot e^{-1} = \dfrac1e \approx 0{,}368$. **Ponto:** $\left(1,\thinspace \dfrac1e\right)$.

**(c)** Derivando $f'(x) = e^{-x}(1-x)$, de novo pelo produto:

$$f''(x) = -e^{-x}(1-x) + e^{-x}(-1) = e^{-x}\big[-(1-x)-1\big] = e^{-x}(x-2)$$

**(d)** Substituindo:

$$
\begin{aligned}
f''+2f'+f &= e^{-x}(x-2) + 2e^{-x}(1-x) + x\thinspace e^{-x} \\
&= e^{-x}\big[(x-2) + (2-2x) + x\big] \\
&= e^{-x}\cdot 0 = 0 \quad \checkmark
\end{aligned}
$$

> 💡 **A função $xe^{-x}$ descreve um sistema criticamente amortecido** — um amortecedor de carro bem regulado, que volta ao repouso o mais rápido possível sem oscilar. O ponto $\left(1,\frac1e\right)$ é o pico do deslocamento, e é exatamente o tipo de informação que a [Unidade 4](../../04-aplicacoes-das-derivadas/README.md) vai sistematizar.

---

## 🎓 Fim da Unidade 3

Você agora deriva qualquer função do curso. A Unidade 4 usa isso para **responder perguntas**:

- onde a função atinge o **maior** e o **menor** valor ([4.1](../../04-aplicacoes-das-derivadas/4.1-maximos-e-minimos.md));
- que teorema garante que "derivada positiva implica crescente" ([4.2](../../04-aplicacoes-das-derivadas/4.2-teoremas-de-rolle-e-do-valor-medio.md));
- como a derivada resolve limites indeterminados ([4.3](../../04-aplicacoes-das-derivadas/4.3-regra-de-lhospital.md));
- como esboçar o gráfico completo de uma função ([4.4](../../04-aplicacoes-das-derivadas/4.4-crescimento-concavidade-e-esboco-de-graficos.md)).

Tudo isso depende de uma única habilidade, que você acabou de treinar: **derivar sem pensar, para poder pensar no resto.**

➡️ **[Unidade 4 · Derivadas: aplicações](../../04-aplicacoes-das-derivadas/README.md)**

---

| ← Revisão | 🏠 Índice | Próxima unidade → |
| :--- | :---: | ---: |
| [Revisão da Unidade 3](../exercicios/revisao-unidade-3.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [Unidade 4](../../04-aplicacoes-das-derivadas/README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
