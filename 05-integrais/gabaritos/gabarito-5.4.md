# ✅ Gabarito — Lista 5.4

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 5.4](../exercicios/lista-5.4-propostos.md) · [Teoria 5.4](../5.4-aplicacoes-da-integral-definida.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $\dfrac{32}{3}$ |
| 1 (b) | $\dfrac14$ |
| 1 (c) | $\sqrt2 - 1$ |
| 2 | $\dfrac83$ |
| 3 | $\dfrac{32}{3}$ |
| 4 (a) | $\dfrac{8\pi}{3}$ |
| 4 (b) | $\dfrac{\pi}{5}$ |
| 4 (c) | $\dfrac{\pi\big(e^2-1\big)}{2}$ |
| 5 | $\dfrac43\pi r^3$ — é a **esfera** de raio $r$ |
| 6 | $\dfrac{\pi}{6}$ |
| 7 | $\dfrac{256\pi}{5}$ |
| 8 | $8\pi$ |
| 9 | $\dfrac{17}{12}$ |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 10 | $\dfrac43$ |
| 11 | $\dfrac83$ |
| 12 | $1$ |
| 13 | $\dfrac{512\pi}{15}$ |
| 14 | $\dfrac{\pi^2}{2}$ |
| 15 | $4\pi$ |
| 16 | $8\pi$ — igual ao exercício 8 ✔ |
| 17 | $\ln\big(2+\sqrt3\big)$ |
| 18 | $\dfrac{\pi}{27}\big(10\sqrt{10}-1\big)$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | Demonstração: $V = \dfrac43\pi r^3$ |
| 20 | Demonstração: $V = \dfrac13\pi R^2 H$ |
| 21 | (a) $\pi\left(1-\frac1b\right)$ · (b) $\pi$ · (c) $\ln b \to +\infty$ · (d) volume finito, área infinita |
| 22 | $k = \sqrt[3]{16} = 2\sqrt[3]{2} \approx 2{,}52$ |
| 23 | Casca: $2\pi\displaystyle\int_0^1(x+1)\big(x-x^2\big)dx$ · Anel: $\pi\displaystyle\int_0^1\left[\big(\sqrt y+1\big)^2-(y+1)^2\right]dy$ |

---

# 📖 Parte 2 — Resoluções completas

## Bloco A · Fixação

### 1.

**(a)** Interseções: $x^2 = 4 \Rightarrow x = \pm2$. A reta $y=4$ está **acima** da parábola em $(-2,2)$.

$$A = \int_{-2}^{2}\big(4-x^2\big)dx = \left[4x-\frac{x^3}{3}\right]_{-2}^{2} = \left(8-\frac83\right)-\left(-8+\frac83\right) = 16-\frac{16}{3} = \frac{32}{3}$$

> 💡 **Atalho pela paridade:** o integrando $4-x^2$ é **par** e o intervalo é simétrico, logo $A = 2\int_0^2(4-x^2)dx$ — metade da conta (exercício 20a da [Lista 5.3](../exercicios/lista-5.3-propostos.md)).

**(b)** Interseções: $x^3 = x \Rightarrow x(x-1)(x+1) = 0$. No **primeiro quadrante**, $x=0$ e $x=1$.

Testando em $x=\frac12$: $x = 0{,}5$ e $x^3 = 0{,}125$ — a **reta** está acima.

$$A = \int_0^1\big(x-x^3\big)dx = \left[\frac{x^2}{2}-\frac{x^4}{4}\right]_0^1 = \frac12-\frac14 = \frac14$$

**(c)** Em $\left[0,\frac{\pi}{4}\right]$, o **cosseno** está acima do seno (eles se igualam exatamente em $\frac{\pi}{4}$).

$$A = \int_0^{\pi/4}\big(\cos x-\mathrm{sen}\thinspace x\big)dx = \Big[\mathrm{sen}\thinspace x+\cos x\Big]_0^{\pi/4} = \left(\frac{\sqrt2}{2}+\frac{\sqrt2}{2}\right)-\big(0+1\big) = \sqrt2-1$$

---

### 2.

$y = x^2-2x = x(x-2)$ é **negativa** em $(0,2)$ e **positiva** em $(2,3)$. Quebre em $x=2$:

$$\int_0^2\big(x^2-2x\big)dx = \left[\frac{x^3}{3}-x^2\right]_0^2 = \frac83-4 = -\frac43$$

$$\int_2^3\big(x^2-2x\big)dx = \big(9-9\big)-\left(\frac83-4\right) = \frac43$$

$$\text{Área} = \left\lvert-\frac43\right\rvert+\frac43 = \frac83$$

---

### 3.

Em $y$, a curva $x=y^2$ é a **da esquerda** e a reta $x=4$ é a **da direita**. Interseções: $y^2 = 4 \Rightarrow y = \pm2$.

$$A = \int_{-2}^{2}\big(4-y^2\big)dy = \frac{32}{3}$$

> 💡 **É a mesma integral do exercício 1(a)** — e não por acaso: as duas regiões são **a mesma**, refletida na reta $y=x$. Refletir não muda área, e aqui isso aparece como a mesma conta com outra letra.

---

### 4.

**(a)** $V = \pi\displaystyle\int_0^2 x^2 dx = \pi\left[\frac{x^3}{3}\right]_0^2 = \frac{8\pi}{3}$

> 💡 É um **cone** de raio $2$ e altura $2$, deitado. Pela fórmula da geometria: $\frac13\pi(2)^2(2) = \frac{8\pi}{3}$ ✔

**(b)** $V = \pi\displaystyle\int_0^1\big(x^2\big)^2 dx = \pi\int_0^1 x^4 dx = \pi\left[\frac{x^5}{5}\right]_0^1 = \frac{\pi}{5}$

**(c)** $V = \pi\displaystyle\int_0^1\big(e^x\big)^2 dx = \pi\int_0^1 e^{2x}dx = \pi\left[\frac{e^{2x}}{2}\right]_0^1 = \frac{\pi\big(e^2-1\big)}{2}$

> ⚠️ **Em (c), $\big(e^x\big)^2 = e^{2x}$, e não $e^{x^2}$.** O primeiro integra; o segundo, não. É a diferença entre uma questão de prova e uma integral impossível.

---

### 5.

$$V = \pi\int_{-r}^{r}\left(\sqrt{r^2-x^2}\right)^2 dx = \pi\int_{-r}^{r}\big(r^2-x^2\big)dx$$

$$= \pi\left[r^2x-\frac{x^3}{3}\right]_{-r}^{r} = \pi\left[\left(r^3-\frac{r^3}{3}\right)-\left(-r^3+\frac{r^3}{3}\right)\right] = \pi\left(2r^3-\frac{2r^3}{3}\right) = \frac43\pi r^3$$

**O sólido é a esfera de raio $r$** — porque $y=\sqrt{r^2-x^2}$ é a semicircunferência superior, e girá-la em torno do eixo $x$ varre a esfera inteira.

> 💡 **Você acabou de deduzir a fórmula do volume da esfera.** Ela aparece desde o ensino fundamental como um fato a decorar; aqui ela sai de três linhas de integral. Arquimedes chegou ao mesmo resultado sem Cálculo, e o considerou sua maior realização — pediu que uma esfera inscrita num cilindro fosse gravada em seu túmulo.

---

### 6.

Interseções: $\sqrt x = x \Rightarrow x = x^2 \Rightarrow x(x-1)=0$, logo $x=0$ e $x=1$.

Em $x=\frac14$: $\sqrt x = 0{,}5$ e $x=0{,}25$. A **raiz** está acima, então ela é o raio **externo**:

$$R(x)=\sqrt x \qquad r(x)=x$$

$$V = \pi\int_0^1\left[\big(\sqrt x\big)^2-x^2\right]dx = \pi\int_0^1\big(x-x^2\big)dx = \pi\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1 = \pi\left(\frac12-\frac13\right) = \frac{\pi}{6}$$

---

### 7.

Interseções de $y=4$ com $y=x^2$: $x=\pm2$.

Girando em torno do eixo $x$, o raio é a **distância ao eixo $x$**. A reta $y=4$ está mais longe, logo é o raio externo:

$$R = 4 \qquad r = x^2$$

$$V = \pi\int_{-2}^{2}\big(16-x^4\big)dx = \pi\left[16x-\frac{x^5}{5}\right]_{-2}^{2} = \pi\left[\left(32-\frac{32}{5}\right)-\left(-32+\frac{32}{5}\right)\right]$$

$$= \pi\left(64-\frac{64}{5}\right) = \pi\cdot\frac{256}{5} = \frac{256\pi}{5}$$

---

### 8.

Rotação em torno do eixo $y$ com fatia **vertical** (paralela ao eixo) ⟹ **casca**.

- raio $= x$ (distância ao eixo $y$)
- altura $= x^2$

$$V = 2\pi\int_0^2 x\cdot x^2 dx = 2\pi\int_0^2 x^3 dx = 2\pi\left[\frac{x^4}{4}\right]_0^2 = 2\pi\cdot 4 = 8\pi$$

---

### 9.

$$y = \frac{x^3}{6}+\frac{1}{2x} \ \Longrightarrow \ y' = \frac{x^2}{2}-\frac{1}{2x^2} = \frac12\left(x^2-\frac{1}{x^2}\right)$$

$$\big(y'\big)^2 = \frac14\left(x^4-2+\frac{1}{x^4}\right)$$

**Somando $1$** — e é aqui que a mágica acontece:

$$1+\big(y'\big)^2 = \frac14\left(x^4-2+\frac{1}{x^4}\right)+1 = \frac14\left(x^4+2+\frac{1}{x^4}\right) = \frac14\left(x^2+\frac{1}{x^2}\right)^2$$

O radicando virou **quadrado perfeito**, e a raiz sai limpa:

$$\sqrt{1+\big(y'\big)^2} = \frac12\left(x^2+\frac{1}{x^2}\right)$$

$$L = \frac12\int_1^2\left(x^2+x^{-2}\right)dx = \frac12\left[\frac{x^3}{3}-\frac1x\right]_1^2 = \frac12\left[\left(\frac83-\frac12\right)-\left(\frac13-1\right)\right]$$

$$= \frac12\left(\frac73+\frac12\right) = \frac12\cdot\frac{17}{6} = \frac{17}{12}$$

> 💡 **Note a estrutura da função.** O $-2$ de $(y')^2$ virou $+2$ ao somar $1$, e $x^4+2+\frac{1}{x^4}$ é exatamente $\left(x^2+\frac{1}{x^2}\right)^2$. **Toda** função de comprimento de arco que cai em prova é construída para isso acontecer. Se o seu radicando não virou quadrado perfeito, **confira a derivada antes de desistir**.
>
> **Conferindo a ordem de grandeza:** a distância reta entre os extremos é $\approx 1{,}36$, e $\frac{17}{12}\approx1{,}42$ — um pouco maior ✔

---

## Bloco B · Consolidação

### 10.

$y = x^2-4x+3 = (x-1)(x-3)$, **negativa** entre as raízes. A região fica abaixo do eixo:

$$\int_1^3\big(x^2-4x+3\big)dx = \left[\frac{x^3}{3}-2x^2+3x\right]_1^3 = \big(9-18+9\big)-\left(\frac13-2+3\right) = 0-\frac43 = -\frac43$$

$$\text{Área} = \left\lvert-\frac43\right\rvert = \frac43$$

---

### 11.

Interseções: $x^2 = -x^2+4x \Rightarrow 2x^2-4x = 0 \Rightarrow 2x(x-2)=0$, logo $x=0$ e $x=2$.

Em $x=1$: $x^2 = 1$ e $-x^2+4x = 3$. A **segunda** está acima.

$$A = \int_0^2\Big[\big(-x^2+4x\big)-x^2\Big]dx = \int_0^2\big(4x-2x^2\big)dx = \left[2x^2-\frac{2x^3}{3}\right]_0^2 = 8-\frac{16}{3} = \frac83$$

---

### 12.

$$A = \int_1^{e}\frac{dx}{x} = \Big[\ln x\Big]_1^{e} = 1-0 = 1$$

> 💡 **Essa é a definição geométrica do número $e$:** é o ponto em que a área sob a hipérbole $y=\frac1x$, a partir de $x=1$, atinge exatamente $1$. Historicamente, o logaritmo natural foi **definido** por essa área, antes de se perceber que era o inverso da exponencial.

---

### 13.

Agora o eixo de rotação é a reta $y=4$, **não** o eixo $x$. O raio é a **distância a essa reta**.

A região vai de $y=x^2$ até $y=4$, e a borda que está **mais longe** da reta $y=4$ é a parábola:

$$R(x) = 4-x^2 \qquad r(x) = 0$$

O raio interno é zero porque a região **encosta** no eixo de rotação — logo é **disco**, não anel.

$$V = \pi\int_{-2}^{2}\big(4-x^2\big)^2 dx = \pi\int_{-2}^{2}\big(16-8x^2+x^4\big)dx$$

Pela paridade, $= 2\pi\displaystyle\int_0^2\big(16-8x^2+x^4\big)dx$:

$$= 2\pi\left[16x-\frac{8x^3}{3}+\frac{x^5}{5}\right]_0^2 = 2\pi\left(32-\frac{64}{3}+\frac{32}{5}\right) = 2\pi\cdot\frac{480-320+96}{15} = \frac{512\pi}{15}$$

> ⚠️ **Este é o erro mais caro da lista:** usar $x^2$ como raio porque "a curva é $y=x^2$". O raio é sempre **distância ao eixo de rotação**, e aqui esse eixo é $y=4$. **Desenhe o eixo antes de escrever a fórmula.**

---

### 14.

$$V = \pi\int_0^{\pi}\mathrm{sen}^2\thinspace x\thinspace dx = \pi\int_0^{\pi}\frac{1-\cos 2x}{2}dx = \frac{\pi}{2}\left[x-\frac{\mathrm{sen}\thinspace 2x}{2}\right]_0^{\pi}$$

$$= \frac{\pi}{2}\big(\pi-0\big) = \frac{\pi^2}{2}$$

---

### 15.

Rotação em torno do eixo $y$, fatia vertical ⟹ casca, com raio $x$ e altura $\frac1x$:

$$V = 2\pi\int_1^3 x\cdot\frac1x\thinspace dx = 2\pi\int_1^3 dx = 2\pi\big(3-1\big) = 4\pi$$

> 💡 **O $x$ do raio cancelou o $\frac1x$ da altura**, e a integral virou a de uma constante. É o melhor exemplo de por que escolher o método certo importa: pelo método do anel, esta mesma questão exigiria inverter $y=\frac1x$ e quebrar a região em duas.

---

### 16.

**O mesmo sólido do exercício 8, agora por anéis.** Fatia **horizontal**, perpendicular ao eixo $y$, integrando em $y$ de $0$ a $4$.

Para uma altura $y$ fixada, a fatia da região vai de $x=\sqrt y$ (sobre a parábola) até $x=2$ (a borda direita). Girando:

$$R = 2 \qquad r = \sqrt y$$

$$V = \pi\int_0^4\left[4-\big(\sqrt y\big)^2\right]dy = \pi\int_0^4\big(4-y\big)dy = \pi\left[4y-\frac{y^2}{2}\right]_0^4 = \pi\big(16-8\big) = 8\pi$$

**Igual ao exercício 8** ✔

> 💡 **A confirmação não é só uma conferência — é o ponto da questão.** Disco, anel e casca são **três maneiras de fatiar o mesmo sólido**, e por isso têm de concordar. Quando uma questão de prova aceitar os dois métodos, escolha o que der a integral mais simples e siga em frente sem medo.

---

### 17.

$$y = \ln(\cos x) \ \Longrightarrow \ y' = \frac{-\mathrm{sen}\thinspace x}{\cos x} = -\mathrm{tg}\thinspace x$$

$$1+\big(y'\big)^2 = 1+\mathrm{tg}^2\thinspace x = \mathrm{sec}^2\thinspace x \ \Longrightarrow \ \sqrt{1+\big(y'\big)^2} = \mathrm{sec}\thinspace x$$

(positivo, pois $\cos x>0$ em $\left[0,\frac{\pi}{3}\right]$).

$$L = \int_0^{\pi/3}\mathrm{sec}\thinspace x\thinspace dx = \Big[\ln\lvert\mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x\rvert\Big]_0^{\pi/3}$$

Em $x=\frac{\pi}{3}$: $\mathrm{sec} = 2$ e $\mathrm{tg} = \sqrt3$. Em $x=0$: $\mathrm{sec}=1$ e $\mathrm{tg}=0$.

$$L = \ln\big(2+\sqrt3\big)-\ln 1 = \ln\big(2+\sqrt3\big) \approx 1{,}317$$

> 💡 **Aqui está a integral da secante**, prometida no exercício 23 da [Lista 5.2](../exercicios/lista-5.2-propostos.md). Ela aparece em comprimento de arco com frequência desconfortável — é a razão prática de valer a pena memorizá-la.

---

### 18.

$y = x^3$, logo $y' = 3x^2$ e $1+\big(y'\big)^2 = 1+9x^4$.

$$S = 2\pi\int_0^1 x^3\sqrt{1+9x^4}\thinspace dx$$

Com $u = 1+9x^4$, $du = 36x^3 dx$, logo $x^3 dx = \dfrac{du}{36}$. Limites: $x=0\Rightarrow u=1$; $x=1\Rightarrow u=10$.

$$S = \frac{2\pi}{36}\int_1^{10}u^{1/2}du = \frac{\pi}{18}\left[\frac23 u^{3/2}\right]_1^{10} = \frac{\pi}{27}\left(10\sqrt{10}-1\right) \approx 3{,}56$$

> 💡 **O $x^3$ do raio foi o que salvou a conta** — ele é (a menos de constante) a derivada de $1+9x^4$, o que torna a substituição imediata. Troque $x^3$ por $x^2$ e a integral deixa de ser elementar. Mais uma vez: o exercício foi construído para funcionar.

---

## Bloco C · Desafio

### 19. O volume da esfera

Gire o semicírculo superior $y = \sqrt{r^2-x^2}$, de $x=-r$ a $x=r$, em torno do eixo $x$. Pelo método do disco:

$$V = \pi\int_{-r}^{r}\big(r^2-x^2\big)dx$$

O integrando é **par**, então vale o dobro da metade direita:

$$V = 2\pi\int_0^r\big(r^2-x^2\big)dx = 2\pi\left[r^2x-\frac{x^3}{3}\right]_0^r = 2\pi\left(r^3-\frac{r^3}{3}\right) = 2\pi\cdot\frac{2r^3}{3} = \frac43\pi r^3 \quad\blacksquare$$

---

### 20. O volume do cone

Um cone de raio da base $R$ e altura $H$ é gerado girando, em torno do eixo $x$, o triângulo sob a reta que vai de $(0,0)$ a $(H,R)$ — ou seja, sob

$$y = \frac{R}{H}x, \qquad 0\leqslant x\leqslant H$$

Pelo método do disco:

$$V = \pi\int_0^H\left(\frac{R}{H}x\right)^2 dx = \pi\frac{R^2}{H^2}\int_0^H x^2 dx = \pi\frac{R^2}{H^2}\cdot\frac{H^3}{3} = \frac13\pi R^2 H \quad\blacksquare$$

> 💡 **De onde vem o $\frac13$.** Ele não tem nada de arbitrário: é o $\frac13$ de $\int x^2 dx = \frac{x^3}{3}$. O mesmo expoente que faz a pirâmide ter $\frac13$ do prisma — e a razão de todo sólido "de ponta" ter esse fator é sempre essa integral.

---

### 21. A trombeta de Gabriel

**(a)** Método do disco, com raio $\frac1x$:

$$V(b) = \pi\int_1^{b}\frac{dx}{x^2} = \pi\left[-\frac1x\right]_1^{b} = \pi\left(1-\frac1b\right)$$

**(b)**

$$\lim_{b\to\infty}V(b) = \lim_{b\to\infty}\pi\left(1-\frac1b\right) = \pi$$

**O volume é FINITO**, e vale exatamente $\pi$.

**(c)** A área da região plana:

$$A(b) = \int_1^{b}\frac{dx}{x} = \ln b \qquad\Longrightarrow\qquad \lim_{b\to\infty}\ln b = +\infty$$

**A área é INFINITA.**

**(d) O paradoxo.** Girando uma região de **área infinita**, obtém-se um sólido de **volume finito**.

A formulação clássica é ainda mais provocante: como a área da **superfície** da trombeta também é infinita, poder-se-ia "enchê-la de tinta" com $\pi$ unidades de volume, mas nunca "pintá-la" por dentro, pois isso exigiria tinta infinita.

**A resolução.** O paradoxo é verbal, não matemático. "Pintar" uma superfície com uma camada de espessura **fixa** $\varepsilon$ exige volume $\approx \varepsilon\times(\text{área})$, que é infinito — mas dentro da trombeta não cabe camada nenhuma de espessura fixa, porque o tubo afina indefinidamente. A tinta que a enche é uma camada de espessura que **tende a zero**. Os dois cálculos medem coisas diferentes.

> 💡 **O que o exemplo ensina de verdade.** A intuição geométrica, treinada em figuras limitadas, **falha** no infinito: "infinitamente longo" não implica "infinitamente grande em todas as medidas". $\frac1x$ decresce devagar demais para a área convergir, mas $\frac{1}{x^2}$ — que é o que o volume integra — decresce rápido o bastante.
>
> **É exatamente a comparação que abre a [seção 5.5](../5.5-integrais-improprias.md)**, e a trombeta é o motivo de aquela seção existir.

---

### 22.

**A área total** é a do exercício 1(a): $\dfrac{32}{3}$. Cada metade deve valer $\dfrac{16}{3}$.

**A parte de baixo** é a região entre a parábola $y=x^2$ e a reta $y=k$, que vai de $x=-\sqrt k$ a $x=\sqrt k$:

$$A_{\text{baixo}} = \int_{-\sqrt k}^{\sqrt k}\big(k-x^2\big)dx = 2\int_0^{\sqrt k}\big(k-x^2\big)dx = 2\left[kx-\frac{x^3}{3}\right]_0^{\sqrt k}$$

$$= 2\left(k^{3/2}-\frac{k^{3/2}}{3}\right) = \frac43 k^{3/2}$$

**Igualando a $\frac{16}{3}$:**

$$\frac43 k^{3/2} = \frac{16}{3} \ \Longrightarrow \ k^{3/2} = 4 \ \Longrightarrow \ k = 4^{2/3} = \sqrt[3]{16} = 2\sqrt[3]{2} \approx 2{,}52$$

**Verificando:** $k\approx2{,}52$ está entre $0$ e $4$ ✔

> 💡 **A reta divisora fica ACIMA do meio** ($2{,}52 > 2$), e isso faz sentido geométrico: a região é mais **larga** em cima (perto de $y=4$) do que embaixo, perto do vértice. Para igualar as áreas, a parte de baixo precisa ser mais **alta** e compensar a estreiteza.

---

### 23.

A região é $0\leqslant x\leqslant 1$, com $x^2\leqslant y\leqslant x$. O eixo de rotação é a reta **vertical** $x=-1$.

**Pelo método da casca** (fatia vertical, **paralela** ao eixo):

- **raio** $=$ distância de $x$ à reta $x=-1$, ou seja, $x+1$;
- **altura** $= x-x^2$.

$$V = 2\pi\int_0^1 (x+1)\big(x-x^2\big)dx$$

**Pelo método do anel** (fatia horizontal, **perpendicular** ao eixo). Para $y$ entre $0$ e $1$, a fatia vai de $x=y$ (sobre a reta $y=x$) até $x=\sqrt y$ (sobre a parábola). As distâncias à reta $x=-1$ são:

$$R = \sqrt y + 1 \qquad r = y+1$$

$$V = \pi\int_0^1\left[\big(\sqrt y+1\big)^2-(y+1)^2\right]dy$$

> 💡 **Confirmando que as duas dão o mesmo** (o exercício não pedia, mas vale ver):
>
> **Casca:** $2\pi\displaystyle\int_0^1\big(x-x^3\big)dx = 2\pi\left(\frac12-\frac14\right) = \frac{\pi}{2}$
>
> **Anel:** $\pi\displaystyle\int_0^1\left(2\sqrt y-y^2-y\right)dy = \pi\left(\frac43-\frac13-\frac12\right) = \frac{\pi}{2}$ ✔
>
> **E note que a casca é visivelmente mais fácil.** Com eixo de rotação **vertical** e região descrita por $y=f(x)$, a casca quase sempre vence — ela integra na variável em que as curvas já estão escritas, e dispensa inverter $y=x^2$ em $x=\sqrt y$.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 5.4](../exercicios/lista-5.4-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [5.4 · Teoria](../5.4-aplicacoes-da-integral-definida.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
