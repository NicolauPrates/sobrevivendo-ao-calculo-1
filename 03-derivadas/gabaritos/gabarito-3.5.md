# ✅ Gabarito — Lista 3.5

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 3.5](../exercicios/lista-3.5-propostos.md) · [Teoria 3.5](../3.5-problemas-de-taxa-de-variacao.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $v(t) = 2t-4$ m/s |
| 1 (b) | $t = 2$ s |
| 1 (c) | $a(t) = 2$ m/s² |
| 2 (a) | $v = 3t^2-3$; $a = 6t$ |
| 2 (b) | $t = 1$ s |
| 2 (c) | acelerando para $t>1$ |
| 3 | $60$ cm²/s |
| 4 | $20\pi \approx 62{,}8$ m²/s |
| 5 | $96$ cm³/min |
| 6 (a) | $\approx 3{,}0167$ |
| 6 (b) | $\approx 8{,}12$ |
| 7 | (a) V · (b) F · (c) F · (d) V |
| 8 | $\dfrac{1}{5\pi} \approx 0{,}064$ cm/s |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | O topo desce a $\dfrac56 \approx 0{,}83$ m/s |
| 10 | $130$ km/h |
| 11 | $\dfrac{4}{\pi} \approx 1{,}27$ m/min |
| 12 | $0{,}048$ rad/s |
| 13 | $\dfrac{\sqrt3}{3} \approx 0{,}58$ cm/s |
| 14 | $v(t) = \dfrac{1-t^2}{\big(t^2+1\big)^2}$; parada em $t=1$ s |
| 15 | $dV = 30$ cm³; erro relativo de $3$% |
| 16 | A pressão **cresce** a $1$ unidade por segundo |
| 17 | $\dfrac{12}{7} \approx 1{,}71$ m/s |
| 18 | O nível baixa a $\dfrac{3}{\pi} \approx 0{,}95$ m/min |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | $0{,}3$ m²/s |
| 20 | $\dfrac{dS}{dt} = \dfrac{40}{a}$ — veja a Parte 2 |
| 21 | $480$ km/h |
| 22 | Demonstração — veja a Parte 2 |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** $v(t) = s'(t) = 2t-4$ m/s

**(b)** $2t-4 = 0 \Rightarrow t = 2$ s

**(c)** $a(t) = v'(t) = 2$ m/s² — constante.

---

### Exercício 2

**(a)** $v(t) = 3t^2-3 = 3(t-1)(t+1)$ e $a(t) = 6t$.

**(b)** Para $t\geqslant0$: $v=0$ em $t=1$ s.

**(c)** Sinais, para $t>0$:

| | $0<t<1$ | $t>1$ |
| --- | :---: | :---: |
| $v$ | $-$ | $+$ |
| $a$ | $+$ | $+$ |

Mesmo sinal apenas para $t>1$: a partícula **acelera** em $(1,+\infty)$ e **freia** em $(0,1)$.

---

### Exercício 3

$$A = L^2 \ \Longrightarrow \ \frac{dA}{dt} = 2L\frac{dL}{dt} = 2(10)(3) = 60 \ \text{cm}^2/\text{s}$$

---

### Exercício 4

$$A = \pi r^2 \ \Longrightarrow \ \frac{dA}{dt} = 2\pi r\frac{dr}{dt} = 2\pi(5)(2) = 20\pi \approx 62{,}8 \ \text{m}^2/\text{s}$$

---

### Exercício 5

$$V = a^3 \ \Longrightarrow \ \frac{dV}{dt} = 3a^2\frac{da}{dt} = 3(64)(0{,}5) = 96 \ \text{cm}^3/\text{min}$$

---

### Exercício 6

**(a)** $f(x) = \sqrt x$, $x=9$, $\Delta x = 0{,}1$, $f'(9) = \dfrac{1}{6}$:

$$\sqrt{9{,}1} \approx 3 + \frac{0{,}1}{6} \approx 3{,}0167$$

**(b)** $f(x) = x^3$, $x=2$, $\Delta x = 0{,}01$, $f'(2) = 12$:

$$(2{,}01)^3 \approx 8 + 12(0{,}01) = 8{,}12$$

*(Valor exato: $8{,}120601$.)*

---

### Exercício 7

**(a) Verdadeiro.**

**(b) Falso.** Com $v$ e $a$ de **mesmo** sinal, a partícula está **acelerando** (ganhando rapidez).

**(c) Falso.** Substituir antes transforma a variável em constante, e a taxa correspondente desaparece.

**(d) Verdadeiro.**

---

### Exercício 8

$$V = \frac43\pi r^3 \ \Longrightarrow \ \frac{dV}{dt} = 4\pi r^2\frac{dr}{dt}$$

$$20 = 4\pi(25)\frac{dr}{dt} \ \Longrightarrow \ \frac{dr}{dt} = \frac{20}{100\pi} = \frac{1}{5\pi} \approx 0{,}064 \ \text{cm/s}$$

---

## Bloco B · Consolidação

### Exercício 9

$$x^2+y^2 = 169 \ \Longrightarrow \ 2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0 \ \Longrightarrow \ \frac{dy}{dt} = -\frac xy\frac{dx}{dt}$$

Quando $x=5$: $y = \sqrt{169-25} = 12$. Logo

$$\frac{dy}{dt} = -\frac{5}{12}(2) = -\frac{5}{6} \approx -0{,}83 \ \text{m/s}$$

**O topo desce a $\dfrac56$ m/s.**

---

### Exercício 10

Após $1$ h: $x = 120$ km (leste), $y = 50$ km (norte) e $z = \sqrt{120^2+50^2} = 130$ km.

$$z^2 = x^2+y^2 \ \Longrightarrow \ \frac{dz}{dt} = \frac{x\frac{dx}{dt}+y\frac{dy}{dt}}{z} = \frac{120(120)+50(50)}{130} = \frac{16900}{130} = 130 \ \text{km/h}$$

---

### Exercício 11

Semelhança: $\dfrac rh = \dfrac36 = \dfrac12$, logo $r = \dfrac h2$.

$$V = \frac13\pi r^2h = \frac13\pi\frac{h^2}{4}h = \frac{\pi h^3}{12}$$

$$\frac{dV}{dt} = \frac{\pi h^2}{4}\frac{dh}{dt} \ \Longrightarrow \ 4 = \frac{\pi(4)}{4}\frac{dh}{dt} = \pi\frac{dh}{dt}$$

$$\frac{dh}{dt} = \frac{4}{\pi} \approx 1{,}27 \ \text{m/min}$$

---

### Exercício 12

Seja $\theta$ o ângulo de elevação e $h$ a altura do balão:

$$\mathrm{tg}\thinspace\theta = \frac{h}{40}$$

Derivando:

$$\sec^2\theta\cdot\frac{d\theta}{dt} = \frac{1}{40}\frac{dh}{dt}$$

Quando $h=30$, a hipotenusa vale $\sqrt{40^2+30^2} = 50$, logo $\sec\theta = \frac{50}{40} = \frac54$ e $\sec^2\theta = \frac{25}{16}$:

$$\frac{25}{16}\cdot\frac{d\theta}{dt} = \frac{3}{40} \ \Longrightarrow \ \frac{d\theta}{dt} = \frac{3}{40}\cdot\frac{16}{25} = \frac{48}{1000} = 0{,}048 \ \text{rad/s}$$

> 💡 A resposta está em **rad/s** — a derivada da tangente só vale em radianos.

---

### Exercício 13

$$A = \frac{\sqrt3}{4}L^2 \ \Longrightarrow \ \frac{dA}{dt} = \frac{\sqrt3}{2}L\frac{dL}{dt}$$

$$10 = \frac{\sqrt3}{2}(20)\frac{dL}{dt} = 10\sqrt3\frac{dL}{dt} \ \Longrightarrow \ \frac{dL}{dt} = \frac{1}{\sqrt3} = \frac{\sqrt3}{3} \approx 0{,}58 \ \text{cm/s}$$

---

### Exercício 14

Pela regra do quociente:

$$v(t) = \frac{1\cdot\big(t^2+1\big) - t(2t)}{\big(t^2+1\big)^2} = \frac{1-t^2}{\big(t^2+1\big)^2}$$

$v(t) = 0$ quando $1-t^2=0$, isto é, $t=1$ s (para $t\geqslant0$).

---

### Exercício 15

$$V = a^3 \ \Longrightarrow \ dV = 3a^2\thinspace da = 3(100)(0{,}1) = 30 \ \text{cm}^3$$

**Erro relativo:**

$$\frac{dV}{V} = \frac{3a^2\thinspace da}{a^3} = 3\cdot\frac{da}{a} = 3\cdot\frac{0{,}1}{10} = 0{,}03$$

ou seja, **3%**.

> 💡 O erro relativo do volume é **o triplo** do erro relativo da aresta — o expoente $3$ multiplica a imprecisão.

---

### Exercício 16

Derivando $PV = C$ em relação a $t$ (regra do **produto**):

$$P\frac{dV}{dt} + V\frac{dP}{dt} = 0$$

Substituindo $P=50$, $V=100$ e $\frac{dV}{dt} = -2$ (o volume **diminui**):

$$50(-2) + 100\frac{dP}{dt} = 0 \ \Longrightarrow \ \frac{dP}{dt} = 1$$

**A pressão cresce a $1$ unidade de pressão por segundo** — coerente com a lei de Boyle: comprimir aumenta a pressão.

---

### Exercício 17

Sejam $x$ a distância da pessoa ao poste e $s$ o comprimento da sombra. Por semelhança:

$$\frac{6}{x+s} = \frac{1{,}8}{s} \ \Longrightarrow \ 6s = 1{,}8x + 1{,}8s \ \Longrightarrow \ 4{,}2\thinspace s = 1{,}8\thinspace x \ \Longrightarrow \ s = \frac{3}{7}x$$

Derivando:

$$\frac{ds}{dt} = \frac37(1{,}2) = \frac{18}{35} \approx 0{,}51 \ \text{m/s}$$

A **ponta da sombra** está a $x+s$ do poste:

$$\frac{d}{dt}(x+s) = 1{,}2 + \frac{18}{35} = \frac{42}{35}+\frac{18}{35} = \frac{60}{35} = \frac{12}{7} \approx 1{,}71 \ \text{m/s}$$

---

### Exercício 18

Semelhança: $\dfrac rh = \dfrac24 = \dfrac12$, logo $r = \dfrac h2$ e $V = \dfrac{\pi h^3}{12}$ (como no Exercício 11).

$$\frac{dV}{dt} = \frac{\pi h^2}{4}\frac{dh}{dt} \ \Longrightarrow \ -3 = \frac{\pi(4)}{4}\frac{dh}{dt} = \pi\frac{dh}{dt}$$

$$\frac{dh}{dt} = -\frac{3}{\pi} \approx -0{,}95 \ \text{m/min}$$

**O nível baixa a $\dfrac3\pi$ m/min.**

---

## Bloco C · Desafio

### Exercício 19

$$A = \frac12(4)(5)\mathrm{sen}\thinspace\theta = 10\mathrm{sen}\thinspace\theta$$

$$\frac{dA}{dt} = 10\cos\theta\cdot\frac{d\theta}{dt}$$

Em $\theta = \dfrac\pi3$, tem-se $\cos\theta = \dfrac12$:

$$\frac{dA}{dt} = 10\cdot\frac12\cdot 0{,}06 = 0{,}3 \ \text{m}^2/\text{s}$$

---

### Exercício 20

Seja $a$ a aresta. Do volume:

$$V = a^3 \ \Longrightarrow \ \frac{dV}{dt} = 3a^2\frac{da}{dt} = 10 \ \Longrightarrow \ \frac{da}{dt} = \frac{10}{3a^2}$$

Da área da superfície:

$$S = 6a^2 \ \Longrightarrow \ \frac{dS}{dt} = 12a\frac{da}{dt} = 12a\cdot\frac{10}{3a^2} = \frac{40}{a}$$

Ou seja, $\dfrac{dS}{dt}$ é **inversamente proporcional** à aresta, com constante de proporcionalidade $40$. $\blacksquare$

> 💡 **Consequência física:** mantendo a vazão constante, quanto maior o cubo, mais devagar a sua superfície cresce. É o mesmo efeito do balão do Exemplo 4 da teoria — e a razão de organismos pequenos trocarem calor com o ambiente muito mais rápido que os grandes.

---

### Exercício 21

Seja $x$ a distância horizontal do avião ao ponto acima do radar, e $z$ a distância direta:

$$z^2 = x^2 + 6^2$$

Derivando:

$$2z\frac{dz}{dt} = 2x\frac{dx}{dt} \ \Longrightarrow \ \frac{dz}{dt} = \frac{x}{z}\frac{dx}{dt}$$

Quando $z=10$: $x = \sqrt{100-36} = 8$ km. Com $\frac{dx}{dt} = 600$ km/h:

$$\frac{dz}{dt} = \frac{8}{10}(600) = 480 \ \text{km/h}$$

> 💡 **Menor que $600$ km/h, e isso faz sentido:** parte do movimento do avião é "para o lado", não "para longe" do radar. Só quando ele está muito distante é que $\frac xz \to 1$ e as duas taxas se igualam.

---

### Exercício 22

Derivando $xy = k$ em relação a $t$, pela regra do produto:

$$\frac{dx}{dt}\thinspace y + x\thinspace \frac{dy}{dt} = 0$$

Dividindo os dois lados por $xy$ (legítimo, pois $x,y>0$):

$$\frac{\frac{dx}{dt}\thinspace y}{xy} + \frac{x\frac{dy}{dt}}{xy} = 0 \ \Longrightarrow \ \frac{1}{x}\frac{dx}{dt} + \frac1y\frac{dy}{dt} = 0$$

$$\frac{1}{x}\frac{dx}{dt} = -\frac1y\frac{dy}{dt} \qquad \blacksquare$$

> 💡 **Em português:** se $x$ cresce $2$% por segundo, $y$ decresce $2$% por segundo. Em produtos constantes — pressão e volume, preço e quantidade, velocidade e tempo de percurso — as **variações percentuais** se compensam exatamente. É por isso que economistas e físicos trabalham tanto com taxas relativas.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 3.5](../exercicios/lista-3.5-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [3.5 · Teoria](../3.5-problemas-de-taxa-de-variacao.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
