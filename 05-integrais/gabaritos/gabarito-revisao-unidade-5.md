# ✅ Gabarito — Revisão da Unidade 5

> **Como usar.** Parte 1: só as respostas, para você conferir e se pontuar. Parte 2: as resoluções completas.

➡️ [Voltar para a Revisão](../exercicios/revisao-unidade-5.md) · [Unidade 5](../README.md)

---

# ✅ Parte 1 — Respostas finais

| Q. | Resposta |
| :---: | --- |
| 1 (a) | $x^3 - 2\ln\lvert x\rvert + \dfrac23 x^{3/2} + C$ |
| 1 (b) | $-2\cos x - \mathrm{tg}\thinspace x + C$ |
| 1 (c) | $\dfrac{x^3}{3}+2x-\dfrac1x + C$ |
| 2 | $-\dfrac{1}{9\big(x^3+5\big)^{3}} + C$ |
| 3 | $\dfrac{x^3}{3}\ln x - \dfrac{x^3}{9} + C$ |
| 4 | $\dfrac73\ln\lvert x-2\rvert - \dfrac13\ln\lvert x+1\rvert + C$ |
| 5 | $-\dfrac{\sqrt{x^2+9}}{9x} + C$ |
| 6 | (a) $v=4t-3t^2$ · (b) $s=2t^2-t^3+2$ · (c) $t=\frac23$ s, com $v=\frac43$ m/s |
| 7 (a) | $\sqrt{1+x^4}$ |
| 7 (b) | $2x\thinspace e^{-x^2}$ |
| 8 | $\dfrac13$ |
| 9 | $8$ |
| 10 | $\dfrac{16\pi}{3}$ — é a **semiesfera** de raio $2$ |
| 11 | $\dfrac53$ |
| 12 | (a) $p>1$ · (b) $p>\frac12$ · (c) sim, qualquer $p$ com $\frac12<p\leqslant1$ |

---

# 📖 Parte 2 — Resoluções completas

## Questão 1

**(a)** Reescreva a raiz como potência e integre termo a termo:

$$\int\left(3x^2-\frac2x+x^{1/2}\right)dx = 3\cdot\frac{x^3}{3} - 2\ln\lvert x\rvert + \frac{x^{3/2}}{3/2} + C$$

$$= x^3 - 2\ln\lvert x\rvert + \frac23 x^{3/2} + C$$

**(b)**

$$\int\big(2\mathrm{sen}\thinspace x - \mathrm{sec}^2\thinspace x\big)dx = -2\cos x - \mathrm{tg}\thinspace x + C$$

> ⚠️ O sinal: $\int\mathrm{sen} = -\cos$. Na dúvida, derive de volta.

**(c)** **Expanda e divida antes de integrar:**

$$\frac{\big(x^2+1\big)^2}{x^2} = \frac{x^4+2x^2+1}{x^2} = x^2+2+x^{-2}$$

$$\int\big(x^2+2+x^{-2}\big)dx = \frac{x^3}{3}+2x-\frac1x + C$$

---

## Questão 2

A função "de dentro" é $x^3+5$, e sua derivada $3x^2$ está (a menos do fator $3$) no numerador:

$$u = x^3+5 \ \Longrightarrow \ du = 3x^2 dx \ \Longrightarrow \ x^2 dx = \frac{du}{3}$$

$$\int\frac{x^2 dx}{\big(x^3+5\big)^4} = \frac13\int u^{-4}du = \frac13\cdot\frac{u^{-3}}{-3} = -\frac{1}{9u^3} = -\frac{1}{9\big(x^3+5\big)^3}+C$$

**Conferindo:** $\dfrac{d}{dx}\left[-\dfrac19\big(x^3+5\big)^{-3}\right] = -\dfrac19\cdot(-3)\big(x^3+5\big)^{-4}\cdot 3x^2 = \dfrac{x^2}{\big(x^3+5\big)^4}$ ✔

---

## Questão 3

Por LIATE, o **logaritmo** vai no $u$:

$$u = \ln x,\quad dv = x^2 dx \ \Longrightarrow \ du = \frac{dx}{x},\quad v = \frac{x^3}{3}$$

$$\int x^2\ln x\thinspace dx = \frac{x^3}{3}\ln x - \int\frac{x^3}{3}\cdot\frac1x dx = \frac{x^3}{3}\ln x - \frac13\int x^2 dx$$

$$= \frac{x^3}{3}\ln x - \frac{x^3}{9} + C$$

**Conferindo:**

$$\left[\frac{x^3}{3}\ln x - \frac{x^3}{9}\right]' = x^2\ln x + \frac{x^3}{3}\cdot\frac1x - \frac{3x^2}{9} = x^2\ln x + \frac{x^2}{3} - \frac{x^2}{3} = x^2\ln x \ \checkmark$$

---

## Questão 4

**Grau $1 < 2$** ✔ e o denominador fatora:

$$x^2-x-2 = (x-2)(x+1)$$

$$\frac{2x+3}{(x-2)(x+1)} = \frac{A}{x-2}+\frac{B}{x+1} \ \Longrightarrow \ 2x+3 = A(x+1)+B(x-2)$$

**Substituindo as raízes:**

- $x=2$: $\ 7 = 3A \Rightarrow A = \dfrac73$
- $x=-1$: $\ 1 = -3B \Rightarrow B = -\dfrac13$

$$\int\frac{2x+3}{x^2-x-2}dx = \frac73\ln\lvert x-2\rvert - \frac13\ln\lvert x+1\rvert + C$$

---

## Questão 5

Radical da forma $\sqrt{a^2+x^2}$ com $a=3$ ⟹ **tangente**:

$$x = 3\mathrm{tg}\thinspace\theta \ \Longrightarrow \ dx = 3\mathrm{sec}^2\thinspace\theta\thinspace d\theta, \qquad \sqrt{x^2+9} = 3\mathrm{sec}\thinspace\theta, \qquad x^2 = 9\mathrm{tg}^2\thinspace\theta$$

**Substituindo:**

$$\int\frac{dx}{x^2\sqrt{x^2+9}} = \int\frac{3\mathrm{sec}^2\thinspace\theta\thinspace d\theta}{9\mathrm{tg}^2\thinspace\theta\cdot 3\mathrm{sec}\thinspace\theta} = \frac19\int\frac{\mathrm{sec}\thinspace\theta}{\mathrm{tg}^2\thinspace\theta}d\theta$$

**Reescreva em seno e cosseno** — é sempre o movimento que destrava integrais trigonométricas estranhas:

$$\frac{\mathrm{sec}\thinspace\theta}{\mathrm{tg}^2\thinspace\theta} = \frac{1}{\cos\theta}\cdot\frac{\cos^2\theta}{\mathrm{sen}^2\thinspace\theta} = \frac{\cos\theta}{\mathrm{sen}^2\thinspace\theta}$$

Com $w = \mathrm{sen}\thinspace\theta$ e $dw = \cos\theta\thinspace d\theta$:

$$\frac19\int\frac{dw}{w^2} = -\frac{1}{9w} = -\frac{1}{9\mathrm{sen}\thinspace\theta}$$

**Voltando ao triângulo.** De $\mathrm{tg}\thinspace\theta = \frac{x}{3}$: cateto oposto $x$, adjacente $3$, hipotenusa $\sqrt{x^2+9}$. Logo

$$\mathrm{sen}\thinspace\theta = \frac{x}{\sqrt{x^2+9}}$$

$$\int\frac{dx}{x^2\sqrt{x^2+9}} = -\frac{1}{9}\cdot\frac{\sqrt{x^2+9}}{x} = -\frac{\sqrt{x^2+9}}{9x}+C$$

**Conferindo** (regra do quociente, com $h = \frac{\sqrt{x^2+9}}{x}$):

$$h' = \frac{\frac{x}{\sqrt{x^2+9}}\cdot x - \sqrt{x^2+9}}{x^2} = \frac{x^2-\big(x^2+9\big)}{x^2\sqrt{x^2+9}} = \frac{-9}{x^2\sqrt{x^2+9}}$$

logo $\left(-\frac{h}{9}\right)' = \dfrac{1}{x^2\sqrt{x^2+9}}$ ✔

---

## Questão 6

**(a)** Integrando a aceleração, com $v(0)=0$:

$$v(t) = \int(4-6t)dt = 4t-3t^2+C_1 \qquad v(0)=C_1 = 0$$

$$v(t) = 4t-3t^2$$

**(b)** Integrando a velocidade, com $s(0)=2$:

$$s(t) = \int\big(4t-3t^2\big)dt = 2t^2-t^3+C_2 \qquad s(0)=C_2 = 2$$

$$s(t) = 2t^2-t^3+2$$

**(c)** A velocidade é máxima onde $v'(t)=0$ — e $v' = a$:

$$a(t) = 4-6t = 0 \ \Longrightarrow \ t = \frac23\ \text{s}$$

**Confirmando que é máximo:** $a$ passa de **positiva** (acelerando) para **negativa** (freando) em $t=\frac23$, logo $v$ sobe e depois desce ✔

$$v\left(\frac23\right) = 4\cdot\frac23 - 3\cdot\frac49 = \frac83-\frac43 = \frac43\ \text{m/s}$$

> 💡 **A questão usa as duas unidades ao mesmo tempo:** a integral construiu $v$ e $s$ a partir de $a$ (Unidade 5), e a derivada localizou o máximo de $v$ (Unidade 4). É o padrão de toda aplicação física — e o motivo de as duas unidades serem ensinadas em sequência.

---

## Questão 7

**(a)** TFC parte 1 direto — troque $t$ por $x$:

$$F'(x) = \sqrt{1+x^4}$$

> 💡 Sem precisar calcular a integral — o que é ótimo, porque $\int\sqrt{1+t^4}\thinspace dt$ não tem primitiva elementar.

**(b)** Limite superior composto, $g(x)=x^2$, logo entra a regra da cadeia:

$$G'(x) = e^{-x^2}\cdot 2x = 2x\thinspace e^{-x^2}$$

---

## Questão 8

$$u = \cos x \ \Longrightarrow \ du = -\mathrm{sen}\thinspace x\thinspace dx \ \Longrightarrow \ \mathrm{sen}\thinspace x\thinspace dx = -du$$

**Convertendo os limites:**

| $x$ | $u = \cos x$ |
| :---: | :---: |
| $0$ | $1$ |
| $\frac{\pi}{2}$ | $0$ |

$$\int_0^{\pi/2}\mathrm{sen}\thinspace x\cos^2 x\thinspace dx = \int_{1}^{0}u^2(-du) = \int_0^{1}u^2 du = \left[\frac{u^3}{3}\right]_0^1 = \frac13$$

> 💡 **O sinal negativo inverteu os limites** — e inverter os limites cancela o sinal. Quem se perde nessa troca pode usar o Caminho 2: ache a primitiva $-\frac{\cos^3 x}{3}$, volte para $x$ e avalie em $0$ e $\frac{\pi}{2}$:
>
> $$\left[-\frac{\cos^3 x}{3}\right]_0^{\pi/2} = 0 + \frac13 = \frac13 \ \checkmark$$

---

## Questão 9

$$y = x^3-4x = x\big(x^2-4\big) = x(x-2)(x+2)$$

**Raízes:** $-2$, $0$ e $2$. A de dentro do intervalo que importa é $x=0$.

| | $-2<x<0$ | $0<x<2$ |
| --- | :---: | :---: |
| $x$ | $-$ | $+$ |
| $x^2-4$ | $-$ | $-$ |
| $y$ | $+$ | $-$ |

**Quebre em $x=0$**, com primitiva $\dfrac{x^4}{4}-2x^2$:

$$\int_{-2}^{0}\big(x^3-4x\big)dx = 0-\big(4-8\big) = 4$$

$$\int_{0}^{2}\big(x^3-4x\big)dx = \big(4-8\big)-0 = -4$$

$$\text{Área} = \lvert 4\rvert + \lvert -4\rvert = 8$$

> ⚠️ **A integral direta daria $0$** — porque $x^3-4x$ é **ímpar** e o intervalo é simétrico. Quem responder $0$ a uma pergunta sobre **área** perde a questão inteira, mesmo tendo feito a conta certa. **Leia o enunciado:** "integral" e "área" são perguntas diferentes.

---

## Questão 10

**(a)** Método do disco, com raio $\sqrt{4-x^2}$:

$$V = \pi\int_0^{2}\left(\sqrt{4-x^2}\right)^2 dx = \pi\int_0^2\big(4-x^2\big)dx$$

$$= \pi\left[4x-\frac{x^3}{3}\right]_0^2 = \pi\left(8-\frac83\right) = \frac{16\pi}{3}$$

**(b)** A curva $y=\sqrt{4-x^2}$ é o **quarto de circunferência** de raio $2$ no primeiro quadrante. Girando em torno do eixo $x$, ele varre uma **semiesfera** de raio $2$.

**Pela fórmula da geometria:**

$$V_{\text{semiesfera}} = \frac12\cdot\frac43\pi r^3 = \frac12\cdot\frac43\pi\cdot 8 = \frac{16\pi}{3} \ \checkmark$$

> 💡 **Identificar o sólido é o melhor controle de qualidade que existe** nesse tipo de questão. Quando a região girada é um pedaço de circunferência, de reta ou de retângulo, o resultado tem de bater com a fórmula da geometria elementar — e bate.

---

## Questão 11

$$y = \frac23\big(x^2+1\big)^{3/2} \ \Longrightarrow \ y' = \frac23\cdot\frac32\big(x^2+1\big)^{1/2}\cdot 2x = 2x\sqrt{x^2+1}$$

$$\big(y'\big)^2 = 4x^2\big(x^2+1\big) = 4x^4+4x^2$$

**Somando $1$:**

$$1+\big(y'\big)^2 = 4x^4+4x^2+1 = \big(2x^2+1\big)^2$$

**Quadrado perfeito** ✔ — como sempre acontece nos exercícios de comprimento de arco. A raiz sai limpa (e $2x^2+1>0$, então não precisa de módulo):

$$L = \int_0^1\big(2x^2+1\big)dx = \left[\frac{2x^3}{3}+x\right]_0^1 = \frac23+1 = \frac53$$

**Conferindo a ordem de grandeza.** Os extremos são $\left(0,\thinspace\frac23\right)$ e $\left(1,\thinspace\frac{4\sqrt2}{3}\right)\approx(1;\thinspace 1{,}89)$. A distância em linha reta é

$$\sqrt{1^2 + \left(1{,}89-0{,}67\right)^2} \approx \sqrt{1+1{,}49} \approx 1{,}58$$

e $L = \frac53 \approx 1{,}67$ — **um pouco maior** que a reta, como tem de ser ✔

---

## Questão 12 — síntese

**(a) A área.**

$$A = \int_1^{\infty}\frac{dx}{x^{p}}$$

Pelo Teorema 5.5.1, converge se, e só se,

$$\boxed{\ p>1\ }$$

**(b) O volume.** Pelo método do disco, com raio $\frac{1}{x^p}$:

$$V = \pi\int_1^{\infty}\left(\frac{1}{x^{p}}\right)^2 dx = \pi\int_1^{\infty}\frac{dx}{x^{2p}}$$

É de novo uma $p$-integral — mas agora com expoente $2p$. Converge se, e só se, $2p>1$, isto é,

$$\boxed{\ p>\frac12\ }$$

**(c) Sim, existe — e é toda uma faixa de valores.**

Comparando as duas condições:

| | converge quando |
| --- | :---: |
| **área** | $p>1$ |
| **volume** | $p>\frac12$ |

A condição do volume é **mais fraca**. Logo, para qualquer $p$ com

$$\frac12 < p \leqslant 1$$

o **volume é finito** e a **área é infinita**.

**O exemplo canônico é $p=1$**, a **trombeta de Gabriel** (exercício 21 das Listas [5.4](../exercicios/lista-5.4-propostos.md) e [5.5](../exercicios/lista-5.5-propostos.md)):

$$A = \int_1^{\infty}\frac{dx}{x} = \infty \qquad\qquad V = \pi\int_1^{\infty}\frac{dx}{x^2} = \pi$$

**Por que isso é possível.** O método do disco **eleva o raio ao quadrado**, o que **dobra o expoente**: a área integra $x^{-p}$, mas o volume integra $x^{-2p}$. Dobrar o expoente empurra a integral para o lado convergente da fronteira $p=1$ — e, para todo $p$ entre $\frac12$ e $1$, o expoente $p$ fica abaixo dela enquanto $2p$ fica acima.

Geometricamente: a região é larga o bastante para acumular área infinita, mas, ao girar, cada secção vira um disco de área $\pi r^2$, e **elevar ao quadrado um raio que já é pequeno o torna pequeno muito mais depressa**. O sólido afina rápido demais para acumular volume.

> 💡 **Esta questão é o fecho do curso, e não por acaso.**
>
> Ela usa a definição de integral imprópria (5.5), o teste da $p$-integral (5.5), o método do disco (5.4) e a noção de área sob curva (5.3) — e o que amarra tudo é um raciocínio sobre **velocidade de decaimento**, que vem lá da hierarquia do infinito da Unidade 4.
>
> Mais do que isso: ela mostra que a intuição geométrica, treinada em figuras limitadas, **não sobrevive ao infinito** sem o Cálculo. Nenhum desenho convence alguém de que um sólido infinitamente longo tem volume $\pi$. A integral convence — e é exatamente para isso que ela existe.

---

## 🏁 Fim da Unidade 5 — e do conteúdo

| Se você acertou | Faça agora |
| --- | --- |
| 11 ou 12 | Vá para os [simulados](../../07-simulados/README.md) |
| 8 a 10 | Refaça as questões que errou, depois os simulados |
| 5 a 7 | Refaça as [listas da unidade](../exercicios/README.md) dos tópicos que falharam |
| 0 a 4 | Volte a [5.1](../5.1-primitivas-e-o-conceito-de-integral.md) e releia a unidade |

> [!TIP]
> **Você chegou ao fim do conteúdo.** O que falta agora não é aprender coisa nova — é **treinar em condições de prova**. Use o [formulário](../../06-formulario/README.md) para revisar e os [simulados](../../07-simulados/README.md) para ensaiar com cronômetro.

---

| ← Revisão | 🏠 Índice | Próximo → |
| :--- | :---: | ---: |
| [Revisão da Unidade 5](../exercicios/revisao-unidade-5.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [Formulário](../../06-formulario/README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
