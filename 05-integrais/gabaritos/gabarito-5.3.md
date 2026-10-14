# ✅ Gabarito — Lista 5.3

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 5.3](../exercicios/lista-5.3-propostos.md) · [Teoria 5.3](../5.3-integral-definida-e-o-teorema-fundamental-do-calculo.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $12$ |
| 1 (b) | $\dfrac{15}{4}$ |
| 1 (c) | $\dfrac{52}{3}$ |
| 1 (d) | $e-1$ |
| 2 (a) | $2$ |
| 2 (b) | $1$ |
| 2 (c) | $\dfrac12$ |
| 3 | $2$ pelos dois caminhos |
| 4 (a) | $0$ |
| 4 (b) | $-12$ |
| 4 (c) | $-2$ |
| 4 (d) | $0$ |
| 5 (a) | $\dfrac{1}{1+x^4}$ |
| 5 (b) | $\ln\big(1+x^2\big)$ |
| 5 (c) | $3x^2\cos\big(x^3\big)$ |
| 5 (d) | $-\sqrt{x}$ |
| 6 (a) | $\dfrac{121}{5}$ |
| 6 (b) | $\dfrac{e^4-1}{2}$ |
| 6 (c) | $\dfrac12$ |
| 7 | (a) $\dfrac32$ · (b) área $=\dfrac52$ |
| 8 (a) | média $2$; $c=2$ |
| 8 (b) | média $\dfrac{13}{3}$; $c=\dfrac{\sqrt{39}}{3}$ |
| 9 | (a) V · (b) F · (c) **F** · (d) V |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 10 | $\dfrac14$ |
| 11 | $2\ln 2 - \dfrac34$ |
| 12 | $\dfrac{\pi}{2}-1$ |
| 13 | $\dfrac{\pi}{4}$ |
| 14 | $\dfrac12\ln\dfrac32$ |
| 15 | $\dfrac{23}{3}$ |
| 16 | $2$ |
| 17 | (a) $F'=x^2-4$, críticos $\pm2$ · (b) máx em $-2$, mín em $2$ · (c) $F(x)=\dfrac{x^3}{3}-4x$ |
| 18 | (a) deslocamento $\dfrac32$ m · (b) distância $\dfrac{11}{6}$ m |
| 19 | $b=4$ **ou** $b=-1$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 20 | Demonstração (substituição $u=-x$) |
| 21 | $1$ |
| 22 | $f(x)=\dfrac{1}{\sqrt{x}}$ e $a=4$ |
| 23 | $G''(x) = \dfrac{1}{1+x^2+x^4}$ |
| 24 | Demonstração (limite o integrando e compare) |

---

# 📖 Parte 2 — Resoluções completas

## Bloco A · Fixação

### 1.

**(a)** $\displaystyle\int_0^3(2x+1)dx = \Big[x^2+x\Big]_0^3 = (9+3)-(0+0) = 12$

**(b)** $\displaystyle\int_{-1}^{2}x^3 dx = \left[\frac{x^4}{4}\right]_{-1}^{2} = \frac{16}{4}-\frac{1}{4} = \frac{15}{4}$

**(c)** $\displaystyle\int_1^{9}\sqrt{x}\thinspace dx = \left[\frac23 x^{3/2}\right]_1^{9} = \frac23(27) - \frac23(1) = 18-\frac23 = \frac{52}{3}$

**(d)** $\displaystyle\int_0^{1}e^x dx = \Big[e^x\Big]_0^1 = e-1$

---

### 2.

**(a)** $\displaystyle\int_0^{\pi}\mathrm{sen}\thinspace x\thinspace dx = \Big[-\cos x\Big]_0^{\pi} = -\cos\pi + \cos 0 = 1+1 = 2$

**(b)** $\displaystyle\int_0^{\pi/4}\mathrm{sec}^2\thinspace x\thinspace dx = \Big[\mathrm{tg}\thinspace x\Big]_0^{\pi/4} = 1-0 = 1$

**(c)** $\displaystyle\int_1^{2}x^{-2}dx = \left[-\frac1x\right]_1^{2} = -\frac12 + 1 = \frac12$

---

### 3.

**Pela definição.** Com $\Delta x = \dfrac{2}{n}$ e $x_i = \dfrac{2i}{n}$ (extremos direitos):

$$S_n = \sum_{i=1}^{n}\frac{2i}{n}\cdot\frac{2}{n} = \frac{4}{n^2}\sum_{i=1}^{n} i = \frac{4}{n^2}\cdot\frac{n(n+1)}{2} = \frac{2(n+1)}{n} = 2+\frac2n$$

$$\int_0^2 x\thinspace dx = \lim_{n\to\infty}\left(2+\frac2n\right) = 2$$

**Pelo TFC.** $\displaystyle\int_0^2 x\thinspace dx = \left[\frac{x^2}{2}\right]_0^2 = 2$ ✔

> 💡 **E pela geometria.** A região é um triângulo de base $2$ e altura $2$, logo de área $\frac{2\cdot2}{2}=2$ ✔ Três caminhos, três vezes o mesmo número — é a confirmação de que a definição por somas de Riemann realmente captura a noção de área.

---

### 4.

**(a)** $0$ — intervalo nulo: $\displaystyle\int_a^a f = 0$ para qualquer $f$.

**(b)** $-12$ — inversão dos limites troca o sinal.

**(c)** $3 + (-5) = -2$ — aditividade.

**(d)** $0$ — $x^3$ é **ímpar** e o intervalo $[-2,2]$ é simétrico. (Este é o exercício 20b, aplicado.)

> 💡 **Nenhum dos quatro exigiu calcular integral.** Reconhecer a propriedade certa transforma quatro contas em quatro observações. Em prova, isso é tempo.

---

### 5.

**(a)** TFC parte 1 direto — troque $t$ por $x$:

$$F'(x) = \frac{1}{1+x^4}$$

**(b)** $G'(x) = \ln\big(1+x^2\big)$

**(c)** Limite superior composto, $g(x)=x^3$:

$$H'(x) = \cos\big(x^3\big)\cdot 3x^2 = 3x^2\cos\big(x^3\big)$$

**(d)** O $x$ está no limite **inferior**. Inverta primeiro:

$$K(x) = \int_x^5\sqrt{t}\thinspace dt = -\int_5^x\sqrt{t}\thinspace dt \ \Longrightarrow \ K'(x) = -\sqrt{x}$$

> ⚠️ **Em (a) e (b), nenhuma das integrais é calculável** em funções elementares — e isso não importa. O TFC parte 1 dá a derivada **sem** calcular a integral, e é exatamente para isso que ele serve.

---

### 6.

**(a)** $u = 2x+1$, $du = 2\thinspace dx$. Limites: $x=0 \Rightarrow u=1$; $x=1 \Rightarrow u=3$.

$$\int_0^1(2x+1)^4 dx = \frac12\int_1^3 u^4 du = \frac12\left[\frac{u^5}{5}\right]_1^3 = \frac{243-1}{10} = \frac{242}{10} = \frac{121}{5}$$

**(b)** $u = x^2$, $x\thinspace dx = \dfrac{du}{2}$. Limites: $x=0 \Rightarrow u=0$; $x=2 \Rightarrow u=4$.

$$\int_0^2 x\thinspace e^{x^2}dx = \frac12\int_0^4 e^u du = \frac12\Big[e^u\Big]_0^4 = \frac{e^4-1}{2}$$

**(c)** $u = \ln x$, $du = \dfrac{dx}{x}$. Limites: $x=1 \Rightarrow u=0$; $x=e \Rightarrow u=1$.

$$\int_1^e\frac{\ln x}{x}dx = \int_0^1 u\thinspace du = \left[\frac{u^2}{2}\right]_0^1 = \frac12$$

> 💡 **Note como os limites mudam de verdade.** Em (a) foram de $[0,1]$ para $[1,3]$; em (b), para $[0,4]$; em (c), para $[0,1]$. Só em (c) eles **coincidiriam** por acaso com os originais — e é justamente esse tipo de coincidência que faz o erro passar despercebido nas outras vezes.

---

### 7.

**(a)** $\displaystyle\int_{-1}^{2}x\thinspace dx = \left[\frac{x^2}{2}\right]_{-1}^{2} = 2-\frac12 = \frac32$

**(b)** A função $y=x$ é **negativa** em $[-1,0)$ e positiva em $(0,2]$. Quebre em $x=0$:

$$\int_{-1}^{0}x\thinspace dx = 0-\frac12 = -\frac12 \qquad \int_{0}^{2}x\thinspace dx = 2-0 = 2$$

$$\text{Área} = \left\lvert-\frac12\right\rvert + \lvert 2\rvert = \frac12+2 = \frac52$$

> 💡 **Confira pela geometria:** dois triângulos, um de base $1$ e altura $1$ (área $\frac12$) e outro de base $2$ e altura $2$ (área $2$). Total $\frac52$ ✔ E a integral, $\frac32$, é a diferença $2-\frac12$ — o triângulo abaixo do eixo entrou negativo.

---

### 8.

**(a)** $\displaystyle\int_0^4 x\thinspace dx = \left[\frac{x^2}{2}\right]_0^4 = 8$, logo

$$f_{\text{méd}} = \frac{1}{4-0}\cdot 8 = 2$$

O $c$ satisfaz $f(c)=2$, isto é, $c = 2$ ✔ (pertence a $[0,4]$).

**(b)** $\displaystyle\int_1^3 x^2 dx = \left[\frac{x^3}{3}\right]_1^3 = 9-\frac13 = \frac{26}{3}$, logo

$$f_{\text{méd}} = \frac{1}{3-1}\cdot\frac{26}{3} = \frac{13}{3}$$

O $c$ satisfaz $c^2 = \dfrac{13}{3}$:

$$c = \sqrt{\frac{13}{3}} = \frac{\sqrt{13}}{\sqrt3} = \frac{\sqrt{39}}{3} \approx 2{,}08$$

(a raiz negativa fica fora de $[1,3]$).

> 💡 **Em (a), a média caiu exatamente no meio** — porque $f(x)=x$ é **linear**, e a média de uma reta é o valor no ponto médio. Em (b) isso falha: o ponto médio é $2$, mas $c\approx2{,}08$. **A média coincide com o meio apenas para funções lineares**; para funções que crescem mais rápido, ela pende para a direita.

---

### 9.

**(a) Verdadeiro.** A variável de integração é **muda**: ela desaparece no resultado, que é um número. Trocar a letra não muda nada.

**(b) Falso.** Contraexemplo: $\displaystyle\int_{-1}^{1}x\thinspace dx = 0$, e $f(x)=x$ certamente não é nula.

> 💡 A afirmação **seria verdadeira** com a hipótese extra $f \geqslant 0$ e contínua: aí a área só pode ser nula se a função for nula.

**(c) Falso** — e o erro é grave. O integrando $\dfrac{1}{x^2}$ **não é contínuo** em $[-1,1]$: ele explode em $x=0$, que está **dentro** do intervalo. O TFC exige continuidade, então aplicá-lo aqui é ilegítimo.

**Como saber que está errado sem nenhuma teoria:** o integrando é **positivo** em todo ponto onde existe, e a conta deu $-2$. Uma soma de áreas positivas não pode ser negativa.

> 💡 **O que a integral realmente é.** Trata-se de uma **integral imprópria** (assunto de [5.5](../5.5-integrais-improprias.md)), e ela **diverge**: a área sob $\frac{1}{x^2}$ perto de zero é infinita.
>
> Este é o item mais importante da lista. **Antes de aplicar o TFC, confira se o integrando é contínuo em todo o intervalo** — em especial, se o denominador não zera lá dentro.

**(d) Verdadeiro.** É o TFC parte 1. Mudar o $a$ altera $F$ por uma **constante** (a área acumulada entre os dois pontos de partida), e constante some na derivada.

---

## Bloco B · Consolidação

### 10.

$u = x^2+1$, $x\thinspace dx = \dfrac{du}{2}$. Limites: $x=0 \Rightarrow u=1$; $x=1 \Rightarrow u=2$.

$$\int_0^1\frac{x\thinspace dx}{\big(x^2+1\big)^2} = \frac12\int_1^2 u^{-2}du = \frac12\left[-\frac1u\right]_1^2 = \frac12\left(-\frac12+1\right) = \frac14$$

---

### 11.

Por partes (exercício 4c da Lista 5.2), a primitiva é $\dfrac{x^2}{2}\ln x - \dfrac{x^2}{4}$:

$$\int_1^2 x\ln x\thinspace dx = \left[\frac{x^2}{2}\ln x - \frac{x^2}{4}\right]_1^2 = \left(2\ln 2 - 1\right) - \left(0 - \frac14\right) = 2\ln 2 - \frac34$$

---

### 12.

A primitiva de $x\cos x$ é $x\mathrm{sen}\thinspace x + \cos x$ (teoria 5.2):

$$\int_0^{\pi/2}x\cos x\thinspace dx = \Big[x\mathrm{sen}\thinspace x + \cos x\Big]_0^{\pi/2} = \left(\frac{\pi}{2}\cdot 1 + 0\right) - \big(0+1\big) = \frac{\pi}{2}-1$$

---

### 13.

$$\int_0^1\frac{dx}{x^2+1} = \Big[\mathrm{arctg}\thinspace x\Big]_0^1 = \mathrm{arctg}\thinspace 1 - \mathrm{arctg}\thinspace 0 = \frac{\pi}{4}$$

---

### 14.

Pela decomposição do exercício 8a da Lista 5.2, a primitiva é $\dfrac12\ln\left\lvert\dfrac{x-1}{x+1}\right\rvert$:

$$\int_2^3\frac{dx}{x^2-1} = \frac12\left[\ln\left\lvert\frac{x-1}{x+1}\right\rvert\right]_2^3 = \frac12\left(\ln\frac24 - \ln\frac13\right) = \frac12\left(\ln\frac12 + \ln 3\right) = \frac12\ln\frac32$$

> 💡 O intervalo $[2,3]$ **não contém** $x=\pm1$, onde o integrando explode — por isso o TFC pode ser aplicado. Compare com o exercício 9(c), onde a descontinuidade estava dentro do intervalo e invalidou tudo.

---

### 15.

A parábola $y=x^2-4$ corta o eixo em $x=\pm2$. Dentro de $[0,3]$, a raiz relevante é $x=2$: a função é **negativa** em $[0,2)$ e **positiva** em $(2,3]$.

$$\int_0^2\big(x^2-4\big)dx = \left[\frac{x^3}{3}-4x\right]_0^2 = \frac83-8 = -\frac{16}{3}$$

$$\int_2^3\big(x^2-4\big)dx = \left[\frac{x^3}{3}-4x\right]_2^3 = \big(9-12\big)-\left(\frac83-8\right) = -3+\frac{16}{3} = \frac73$$

$$\text{Área} = \frac{16}{3}+\frac73 = \frac{23}{3}$$

> ⚠️ **A integral simples daria $-\frac{16}{3}+\frac73 = -3$** — um número negativo, que não pode ser área. **Achar as raízes antes de integrar** é o passo que a questão realmente cobra.

---

### 16.

O cosseno troca de sinal em $x=\frac{\pi}{2}$:

$$\int_0^{\pi/2}\cos x\thinspace dx = \Big[\mathrm{sen}\thinspace x\Big]_0^{\pi/2} = 1 \qquad \int_{\pi/2}^{\pi}\cos x\thinspace dx = 0-1 = -1$$

$$\text{Área} = \lvert1\rvert+\lvert-1\rvert = 2$$

> 💡 A integral simples daria $0$ — os dois pedaços têm a mesma área e sinais opostos, como no caso do seno em $[0,2\pi]$.

---

### 17.

**(a)** Pelo TFC parte 1:

$$F'(x) = x^2-4 = (x-2)(x+2)$$

Pontos críticos: $x=-2$ e $x=2$.

**(b)** Quadro de sinais de $F'$:

| | $x<-2$ | $-2<x<2$ | $x>2$ |
| --- | :---: | :---: | :---: |
| $F'$ | $+$ | $-$ | $+$ |

$F$ **cresce** em $(-\infty,-2)$ e $(2,+\infty)$; **decresce** em $(-2,2)$.

**Máximo local** em $x=-2$; **mínimo local** em $x=2$.

**(c)** Calculando explicitamente:

$$F(x) = \int_0^x\big(t^2-4\big)dt = \left[\frac{t^3}{3}-4t\right]_0^x = \frac{x^3}{3}-4x$$

Derivando: $F'(x) = x^2-4$ ✔ E os valores extremos são

$$F(-2) = -\frac83+8 = \frac{16}{3} \qquad F(2) = \frac83-8 = -\frac{16}{3}$$

confirmando máximo em $-2$ e mínimo em $2$ ✔

> 💡 **Esta questão reúne as Unidades 4 e 5.** Uma função **definida por uma integral** foi analisada com as ferramentas de esboço de gráficos — e o TFC parte 1 forneceu a derivada de graça, sem precisar da fórmula explícita.
>
> Isso importa porque, em geral, a fórmula explícita **não existe**. Se o integrando fosse $e^{-t^2}$, o item (c) seria impossível — e os itens (a) e (b) continuariam saindo exatamente do mesmo jeito.

---

### 18.

$v(t) = t^2-3t+2 = (t-1)(t-2)$, que troca de sinal em $t=1$ e $t=2$.

| | $0<t<1$ | $1<t<2$ | $2<t<3$ |
| --- | :---: | :---: | :---: |
| $v$ | $+$ | $-$ | $+$ |

A primitiva é $s(t) = \dfrac{t^3}{3}-\dfrac{3t^2}{2}+2t$.

**(a) Deslocamento** — é a integral simples, **com** sinal:

$$\int_0^3 v\thinspace dt = \left[\frac{t^3}{3}-\frac{3t^2}{2}+2t\right]_0^3 = 9-\frac{27}{2}+6 = \frac{3}{2}\ \text{m}$$

**(b) Distância percorrida** — é a integral do **módulo**, pedaço por pedaço:

$$\int_0^1 v\thinspace dt = \frac13-\frac32+2 = \frac56 \qquad \int_1^2 v\thinspace dt = -\frac16 \qquad \int_2^3 v\thinspace dt = \frac56$$

$$\text{distância} = \frac56+\frac16+\frac56 = \frac{11}{6}\ \text{m}$$

**Conferindo:** o deslocamento tem de ser a soma **com sinal**: $\frac56-\frac16+\frac56 = \frac96 = \frac32$ ✔

> 💡 **A diferença entre os dois números é física, não matemática.** O móvel avançou, recuou um pouco e avançou de novo: percorreu $\frac{11}{6}$ m de caminho, mas terminou a apenas $\frac32$ m do ponto de partida. É o mesmo par integral/área da teoria, com nomes de cinemática.

---

### 19.

$$\int_0^b(2x-3)dx = \Big[x^2-3x\Big]_0^b = b^2-3b$$

Igualando a $4$:

$$b^2-3b-4 = 0 \ \Longrightarrow \ (b-4)(b+1) = 0 \ \Longrightarrow \ b=4 \ \text{ ou } \ b=-1$$

**As duas soluções servem.** Verificando $b=-1$:

$$\int_0^{-1}(2x-3)dx = \Big[x^2-3x\Big]_0^{-1} = 1+3 = 4 \ \checkmark$$

> 💡 **Não descarte a raiz negativa sem pensar.** Aqui nada no enunciado exige $b>0$, e a integral de $0$ a $-1$ é perfeitamente definida — é a inversão de limites em ação. Num problema **aplicado** (um tempo, um comprimento), o contexto descartaria o negativo; num problema puramente algébrico como este, ele é resposta.

---

## Bloco C · Desafio

### 20. Integrais em intervalos simétricos

Em ambos os casos, quebre no zero e trate a parte negativa com a substituição $u = -x$ (logo $du = -dx$; quando $x=-a$, $u=a$; quando $x=0$, $u=0$):

$$\int_{-a}^{0}f(x)\thinspace dx = \int_{a}^{0}f(-u)\thinspace(-du) = \int_{0}^{a}f(-u)\thinspace du$$

**(a) $f$ par.** Então $f(-u)=f(u)$, e a integral acima vale $\displaystyle\int_0^a f(u)du$. Logo

$$\int_{-a}^{a}f = \int_{-a}^{0}f + \int_{0}^{a}f = \int_0^a f + \int_0^a f = 2\int_0^a f \quad\blacksquare$$

**(b) $f$ ímpar.** Então $f(-u) = -f(u)$, e a integral vale $-\displaystyle\int_0^a f$. Logo

$$\int_{-a}^{a}f = -\int_0^a f + \int_0^a f = 0 \quad\blacksquare$$

> 💡 **Use isso sempre.** $\displaystyle\int_{-5}^{5}\frac{x^3\mathrm{sen}\thinspace x^2}{1+x^8}dx = 0$ — sem calcular nada, porque o integrando é ímpar e o intervalo é simétrico. Reconhecer paridade antes de integrar é o atalho mais rentável das integrais definidas, e aparece em prova disfarçado de integral monstruosa.

---

### 21.

Substituindo $x=0$ direto:

$$\frac{1}{0}\int_0^0(\cdots) = \frac{0}{0}$$

indeterminação. Reescreva como quociente e aplique L&#39;Hôspital:

$$\lim_{x\to0}\frac{\displaystyle\int_0^x\frac{dt}{1+t^2}}{x}$$

A derivada do **numerador** sai pelo TFC parte 1 — e é aí que os dois teoremas se encontram:

$$\frac{d}{dx}\int_0^x\frac{dt}{1+t^2} = \frac{1}{1+x^2}$$

A derivada do denominador é $1$. Logo:

$$\lim_{x\to0}\frac{1/\big(1+x^2\big)}{1} = \frac{1}{1+0} = 1$$

> 💡 **O que o resultado significa.** A expressão $\frac1x\int_0^x f$ é o **valor médio** de $f$ em $[0,x]$. O limite diz que, quando o intervalo encolhe para um ponto, a média tende ao valor da função nesse ponto — aqui, $f(0) = \frac{1}{1+0} = 1$.
>
> Isso vale em geral para $f$ contínua, e é outra maneira de enxergar o TFC parte 1.

---

### 22.

**Derive os dois lados** em relação a $x$. À esquerda, o TFC parte 1 dá $f(x)$; à direita, a regra da potência:

$$f(x) = \frac{d}{dx}\big(2\sqrt{x}-4\big) = 2\cdot\frac{1}{2\sqrt{x}} = \frac{1}{\sqrt{x}}$$

**Para achar $a$**, use que uma integral de limites iguais é zero. Fazendo $x=a$:

$$0 = \int_a^a f = 2\sqrt{a}-4 \ \Longrightarrow \ \sqrt{a} = 2 \ \Longrightarrow \ a = 4$$

**Verificando:**

$$\int_4^x t^{-1/2}dt = \Big[2\sqrt t\Big]_4^x = 2\sqrt{x}-4 \ \checkmark$$

> 💡 **Os dois passos usam partes diferentes do teorema.** Derivar usa o TFC parte 1 e entrega a **função**; substituir $x=a$ usa a propriedade do intervalo nulo e entrega a **constante**. É um padrão que vale guardar: numa equação com integral de limite variável, **derive para achar o integrando e avalie no limite inferior para achar a constante**.

---

### 23.

Aplique o TFC parte 1 **duas vezes**.

**Primeira vez.** $G$ é a integral, de $0$ a $x$, da função $u \mapsto \displaystyle\int_0^u\frac{dt}{1+t^2+t^4}$. Logo $G'(x)$ é essa função avaliada em $x$:

$$G'(x) = \int_0^x\frac{dt}{1+t^2+t^4}$$

**Segunda vez.** Agora $G'$ é ela própria uma integral de limite superior variável:

$$G''(x) = \frac{1}{1+x^2+x^4}$$

> 💡 **Note o que não foi preciso fazer:** calcular a integral interna — que, aliás, é horrível. O TFC parte 1 opera no nível da **estrutura**, não da fórmula, e por isso funciona com qualquer integrando contínuo.

---

### 24.

**Limite o integrando.** Para $x\in[0,1]$, tem-se $0\leqslant x^2\leqslant 1$ e $0\leqslant x^4\leqslant 1$, logo

$$1 \leqslant 1+x^2+x^4 \leqslant 3$$

Invertendo (o que troca o sentido das desigualdades, pois tudo é positivo):

$$\frac13 \leqslant \frac{1}{1+x^2+x^4} \leqslant 1$$

**Integre os três membros** em $[0,1]$, usando a propriedade de **comparação**:

$$\int_0^1\frac13\thinspace dx \ \leqslant \ \int_0^1\frac{dx}{1+x^2+x^4} \ \leqslant \ \int_0^1 1\thinspace dx$$

As integrais das pontas são de funções constantes, e valem $k(b-a) = k\cdot 1$:

$$\frac13 \ \leqslant \ \int_0^1\frac{dx}{1+x^2+x^4} \ \leqslant \ 1 \quad\blacksquare$$

> 💡 **Esta técnica resolve o problema que o TFC não resolve.** A integral do enunciado **tem** valor (o integrando é contínuo), mas sua primitiva é medonha. Mesmo assim, limitar o integrando entre duas constantes **estima** o resultado em três linhas.
>
> É a mesma ideia do [Teorema do Sanduíche](../../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md) da Unidade 2, transportada para integrais — e é o começo da análise numérica, onde quase nenhuma integral tem primitiva e todas precisam ser estimadas.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 5.3](../exercicios/lista-5.3-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [5.3 · Teoria](../5.3-integral-definida-e-o-teorema-fundamental-do-calculo.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
