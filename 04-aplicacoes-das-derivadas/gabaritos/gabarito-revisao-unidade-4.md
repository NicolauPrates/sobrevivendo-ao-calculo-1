# ✅ Gabarito — Revisão da Unidade 4

> **Como usar.** Parte 1: só as respostas, para você conferir e se pontuar. Parte 2: as resoluções completas.

➡️ [Voltar para a Revisão](../exercicios/revisao-unidade-4.md) · [Unidade 4](../README.md)

---

# ✅ Parte 1 — Respostas finais

| Q. | Resposta |
| :---: | --- |
| 1 | Máximo absoluto $10$ em $x=-1$; mínimo absoluto $-22$ em $x=3$ |
| 2 | (a) $r=\sqrt[3]{500/\pi}\approx5{,}42$ cm e $h\approx10{,}84$ cm · (b) $h=2r$ ✔ |
| 3 | (a) As três valem · (b) $c = \pm\dfrac{2\sqrt3}{3}$ |
| 4 | Demonstração (TVM com $f=\operatorname{sen}$ e $\lvert\cos c\rvert\leqslant1$) |
| 5 | (a) $\frac00$, limite $=2$ · (b) $1^{\infty}$, limite $=e^6$ · (c) $\infty-\infty$, limite $=0$ |
| 6 | Mín $(0,\thinspace 0)$; máx $\left(2,\thinspace 4e^{-2}\right)$; A.H. $y=0$ só à direita; inflexões em $x=2\pm\sqrt2$ |
| 7 | (a) **Sim** · (b) **Não** · (c) **Sim** · (d) **Não** — por quatro motivos diferentes |
| 8 | Mínimos locais $(\pm2,\thinspace -13)$; máximo local $(0,\thinspace 3)$ |
| 9 | Demonstração: TVI dá a existência, $f'>0$ dá a unicidade |
| 10 | $100 \text{ m} \times 200 \text{ m}$ (os $200$ m ao longo do rio); área $=20\thinspace000\text{ m}^2$ |
| 11 | $a=\dfrac{e}{2}$ e $b=-\dfrac12$ |
| 12 | (a) mínimo absoluto em $x=0$ · (b) demonstração · (c) côncava para cima em $\mathbb{R}$, sem inflexão · (d) $y=x+1$ ✔ |

---

# 📖 Parte 2 — Resoluções completas

## Questão 1

**Método dos candidatos** (a função é contínua num intervalo **fechado**, logo o Teorema de Weierstrass garante que os extremos existem).

**Passo 1 — pontos críticos.**

$$f'(x) = 3x^2-6x-9 = 3\big(x^2-2x-3\big) = 3(x-3)(x+1)$$

Críticos: $x=-1$ e $x=3$ — **ambos** dentro de $[-2,4]$ ✔

**Passo 2 — avaliar nos candidatos** (os dois críticos **e** as duas bordas):

| $x$ | $f(x)$ | |
| :---: | :---: | --- |
| $-2$ | $-8-12+18+5 = 3$ | borda |
| $-1$ | $-1-3+9+5 = \mathbf{10}$ | crítico |
| $3$ | $27-27-27+5 = \mathbf{-22}$ | crítico |
| $4$ | $64-48-36+5 = -15$ | borda |

**Resposta.** Máximo absoluto $\mathbf{10}$, em $x=-1$. Mínimo absoluto $\mathbf{-22}$, em $x=3$.

> ⚠️ **Não é preciso classificar os críticos** aqui. O método dos candidatos compara **valores**, não sinais — montar quadro de sinais de $f'$ nessa questão é trabalho jogado fora.

---

## Questão 2

**(a)** **Montagem.** Seja $r$ o raio e $h$ a altura.

- **Restrição** (volume dado): $\pi r^2 h = 1000$
- **Função a minimizar** (área total: duas tampas mais a lateral): $A = 2\pi r^2 + 2\pi r h$

**Eliminando $h$.** Da restrição, $h = \dfrac{1000}{\pi r^2}$, e substituindo:

$$A(r) = 2\pi r^2 + 2\pi r\cdot\frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}, \qquad r>0$$

**Derivando.**

$$A'(r) = 4\pi r - \frac{2000}{r^2} = 0 \ \Longrightarrow \ 4\pi r^3 = 2000 \ \Longrightarrow \ r^3 = \frac{500}{\pi}$$

$$\boxed{\ r = \sqrt[3]{\frac{500}{\pi}} \approx 5{,}42 \text{ cm}\ }$$

**Confirmando o mínimo.**

$$A''(r) = 4\pi + \frac{4000}{r^3} > 0 \quad \text{para todo } r>0$$

A função é côncava para cima em todo o domínio, logo o único ponto crítico é mínimo **absoluto** ✔

**A altura.** $h = \dfrac{1000}{\pi r^2} \approx \dfrac{1000}{\pi(29{,}37)} \approx 10{,}84$ cm.

A área mínima é $A = 6\pi r^2 \approx 553{,}6 \text{ cm}^2$.

**(b)** De $r^3 = \dfrac{500}{\pi}$ segue $\pi r^3 = 500$, ou seja, $\pi r^2 = \dfrac{500}{r}$. Então:

$$h = \frac{1000}{\pi r^2} = \frac{1000}{500/r} = \frac{1000\thinspace r}{500} = 2r$$

Como $2r$ é exatamente o **diâmetro**, a lata ótima tem **altura igual ao diâmetro** $\blacksquare$

> 💡 **E por que as latas de refrigerante não são assim?** Porque o modelo ignora o custo das tampas (mais grossas que a lateral), as perdas de corte na chapa e o empilhamento na prateleira. A matemática está certa; a lata real otimiza outra função. É um bom lembrete de que otimização é **tão boa quanto o modelo**.

---

## Questão 3

**(a) As três hipóteses de Rolle em $[-2,2]$:**

| Hipótese | Verificação |
| --- | --- |
| $f$ contínua em $[-2,2]$ | ✔ $f$ é polinômio, contínua em $\mathbb{R}$ |
| $f$ derivável em $(-2,2)$ | ✔ $f'(x)=3x^2-4$ existe em $\mathbb{R}$ |
| $f(-2)=f(2)$ | ✔ $f(-2) = -8+8 = 0$ e $f(2) = 8-8 = 0$ |

As três valem, logo o teorema **garante** ao menos um $c\in(-2,2)$ com $f'(c)=0$.

**(b)** Resolvendo:

$$f'(c) = 3c^2-4 = 0 \ \Longrightarrow \ c^2 = \frac43 \ \Longrightarrow \ c = \pm\frac{2}{\sqrt3} = \pm\frac{2\sqrt3}{3} \approx \pm1{,}15$$

Os **dois** valores pertencem a $(-2,2)$ ✔

**Resposta.** $c = \dfrac{2\sqrt3}{3}$ e $c = -\dfrac{2\sqrt3}{3}$.

> 💡 **Rolle garante "pelo menos um", não "exatamente um".** Aqui há dois, e a questão pede **todos** — descartar um deles custa metade da nota.

---

## Questão 4

**Caso trivial.** Se $a=b$, os dois lados valem zero e a desigualdade vale.

**Caso $a\neq b$.** Seja $f(x) = \operatorname{sen} x$. Como $f$ é contínua e derivável em $\mathbb{R}$, ela o é em particular no intervalo fechado de extremos $a$ e $b$.

Pelo **Teorema do Valor Médio**, existe $c$ **entre** $a$ e $b$ tal que

$$f'(c) = \frac{f(a)-f(b)}{a-b} \ \Longrightarrow \ \cos c = \frac{\operatorname{sen} a - \operatorname{sen} b}{a-b}$$

Tomando módulo dos dois lados:

$$\left\lvert\frac{\operatorname{sen} a - \operatorname{sen} b}{a-b}\right\rvert = \lvert\cos c\rvert \leqslant 1$$

pois o cosseno está sempre entre $-1$ e $1$. Multiplicando por $\lvert a-b\rvert>0$:

$$\lvert \operatorname{sen} a - \operatorname{sen} b\rvert \leqslant \lvert a-b\rvert \quad \blacksquare$$

> 💡 **O que a desigualdade diz.** O seno nunca "estica" distâncias: dois pontos próximos têm senos próximos, no mesmo ritmo ou mais devagar. Essa propriedade tem nome — a função é **lipschitziana de constante $1$** — e é o TVM que a entrega, em três linhas, para qualquer função com derivada limitada.

---

## Questão 5

**(a)** Substituindo: $\dfrac{e^0-1-0}{0} = \dfrac{0}{0}$ ✔ indeterminação $\frac00$.

$$\lim_{x\to0}\frac{e^{2x}-1-2x}{x^2} \overset{\text{L'H}}{=} \lim_{x\to0}\frac{2e^{2x}-2}{2x}$$

Ainda $\frac00$ (numerador $\to 2-2=0$). Aplicando de novo:

$$\overset{\text{L'H}}{=} \lim_{x\to0}\frac{4e^{2x}}{2} = \frac{4}{2} = \mathbf{2}$$

**(b)** A base tende a $1$ e o expoente a $+\infty$: indeterminação $\mathbf{1^{\infty}}$. Usa-se o logaritmo.

Seja $L$ o limite procurado. Então:

$$\ln L = \lim_{x\to+\infty} 2x\ln\left(1+\frac3x\right) = \lim_{x\to+\infty}\frac{2\ln\left(1+\frac3x\right)}{1/x}$$

Agora é $\frac00$. Derivando numerador e denominador:

$$\ln L \overset{\text{L'H}}{=} \lim_{x\to+\infty}\frac{2\cdot\dfrac{-3/x^2}{1+\frac3x}}{-1/x^2} = \lim_{x\to+\infty}\frac{6}{1+\frac3x} = 6$$

Portanto $L = \mathbf{e^6}$.

**(c)** Substituindo: $\dfrac{1}{0^{+}} - \dfrac{1}{0^{+}} = +\infty-\infty$ ✔ indeterminação $\infty-\infty$. **Combina-se numa fração:**

$$\frac1x - \frac{1}{\operatorname{sen} x} = \frac{\operatorname{sen} x - x}{x\operatorname{sen} x}$$

que é $\frac00$. Aplicando a regra:

$$\overset{\text{L'H}}{=} \lim_{x\to0^{+}}\frac{\cos x-1}{\operatorname{sen} x + x\cos x} = \frac{0}{0}$$

$$\overset{\text{L'H}}{=} \lim_{x\to0^{+}}\frac{-\operatorname{sen} x}{2\cos x - x\operatorname{sen} x} = \frac{0}{2-0} = \mathbf{0}$$

> ⚠️ **Note a ordem de operações em (b) e (c).** L&#39;Hôspital só aceita $\frac00$ e $\frac{\infty}{\infty}$. As outras formas precisam primeiro ser **convertidas**: $1^{\infty}$ pelo logaritmo, $\infty-\infty$ pela soma de frações, $0\cdot\infty$ passando um fator para o denominador.

---

## Questão 6 — esboço de $f(x)=x^2e^{-x}$

**1. Domínio.** Produto de funções definidas em $\mathbb{R}$: $D=\mathbb{R}$.

**2. Interseções.** Como $e^{-x}>0$ sempre, $f(x)=0$ exige $x^2=0$: único corte em $(0,\thinspace 0)$ (raiz **dupla**).

Além disso, $f(x) \geqslant 0$ para **todo** $x$ — o gráfico nunca desce abaixo do eixo.

**3. Simetria.** $f(-x) = x^2e^{x}$, que não é $f(x)$ nem $-f(x)$: nenhuma.

**4. Assíntotas.** Nenhuma vertical. No infinito:

$$\lim_{x\to+\infty} x^2e^{-x} = \lim_{x\to+\infty}\frac{x^2}{e^x} = 0$$

pela **hierarquia do infinito** de [4.3](../4.3-regra-de-lhospital.md) — a exponencial vence a potência. Logo $y=0$ é assíntota horizontal **à direita**.

$$\lim_{x\to-\infty} x^2e^{-x} = (+\infty)\cdot(+\infty) = +\infty$$

**Não** há assíntota à esquerda: aqui os dois fatores crescem juntos.

**5. Crescimento.** Pela regra do produto:

$$f'(x) = 2xe^{-x} + x^2e^{-x}(-1) = e^{-x}\big(2x-x^2\big) = x\thinspace e^{-x}(2-x)$$

Como $e^{-x}>0$, o sinal é o de $x(2-x)$:

| | $x<0$ | $0<x<2$ | $x>2$ |
| --- | :---: | :---: | :---: |
| $x$ | $-$ | $+$ | $+$ |
| $2-x$ | $+$ | $+$ | $-$ |
| $f'$ | $-$ | $+$ | $-$ |

**Mínimo local** em $(0,\thinspace 0)$ — e **absoluto**, já que $f\geqslant0$.

**Máximo local** em $\left(2,\thinspace 4e^{-2}\right) \approx (2;\thinspace 0{,}54)$ — apenas **local**, pois $f\to+\infty$ à esquerda.

**6. Concavidade.** Derivando $f'(x) = e^{-x}\big(2x-x^2\big)$:

$$f''(x) = -e^{-x}\big(2x-x^2\big) + e^{-x}(2-2x) = e^{-x}\big(x^2-4x+2\big)$$

O sinal é o de $x^2-4x+2$, cujas raízes são

$$x = \frac{4\pm\sqrt{16-8}}{2} = \frac{4\pm2\sqrt2}{2} = 2\pm\sqrt2$$

ou seja, $x\approx0{,}59$ e $x\approx3{,}41$. Uma parábola com concavidade para cima é positiva **fora** das raízes:

| | $x<2-\sqrt2$ | $2-\sqrt2<x<2+\sqrt2$ | $x>2+\sqrt2$ |
| --- | :---: | :---: | :---: |
| $f''$ | $+$ | $-$ | $+$ |

Concavidade **para cima** nas duas pontas e **para baixo** no meio. **Duas inflexões**, em $x=2-\sqrt2$ e $x=2+\sqrt2$, com

$$f\left(2\pm\sqrt2\right) = \big(6\pm4\sqrt2\big)\thinspace e^{-(2\pm\sqrt2)} \approx 0{,}19 \ \text{ e } \ 0{,}38$$

**7. Tabela-resumo.** Ordenando todos os pontos de divisão: $0 < 2-\sqrt2 < 2 < 2+\sqrt2$.

| Intervalo | $f'$ | $f''$ | Comportamento |
| :---: | :---: | :---: | --- |
| $(-\infty,\thinspace 0)$ | $-$ | $+$ | desce, concavidade para cima |
| $\left(0,\thinspace 2-\sqrt2\right)$ | $+$ | $+$ | sobe, concavidade para cima |
| $\left(2-\sqrt2,\thinspace 2\right)$ | $+$ | $-$ | sobe, concavidade para baixo |
| $\left(2,\thinspace 2+\sqrt2\right)$ | $-$ | $-$ | desce, concavidade para baixo |
| $\left(2+\sqrt2,\thinspace +\infty\right)$ | $-$ | $+$ | desce, concavidade para cima |

**8. Desenho.** Desce de $+\infty$ (à esquerda) curvando para cima, **toca** o eixo $x$ na origem — que é o mínimo absoluto —, sobe até o pico $\left(2,\thinspace 4e^{-2}\right)$ passando pela primeira inflexão, desce, muda de concavidade de novo em $x=2+\sqrt2$ e se achata contra $y=0$ pela direita, sem nunca tocá-lo.

> 💡 **Três pontos de atenção que a banca procura nesta questão:**
> 1. a assíntota existe **só de um lado** — é a diferença mais fácil de perder;
> 2. o mínimo em $(0,0)$ é **absoluto**, mas o máximo em $x=2$ é **só local**;
> 3. as inflexões são **irracionais** ($2\pm\sqrt2$) — deixe na forma exata, não arredonde na resposta.

---

## Questão 7

| | Há inflexão em $x=0$? | O motivo |
| :---: | :---: | --- |
| **(a)** $x^5$ | **Sim** | $f''=20x^3$ **troca de sinal** ($-$ para $+$) e $f$ é contínua |
| **(b)** $x^4$ | **Não** | $g''=12x^2\geqslant0$: **não** troca de sinal |
| **(c)** $\sqrt[3]{x}$ | **Sim** | $h''$ **não existe** em $0$, mas troca de sinal — e $h$ é contínua |
| **(d)** $\frac1x$ | **Não** | $k''$ troca de sinal, mas $k$ **não é contínua** em $0$ (nem definida) |

**Detalhando (c)**, que é o caso sutil:

$$h(x) = x^{1/3} \quad \Longrightarrow \quad h'(x) = \tfrac13 x^{-2/3} \quad \Longrightarrow \quad h''(x) = -\tfrac29 x^{-5/3}$$

- Para $x>0$: $x^{-5/3}>0$, logo $h''<0$ — concavidade para **baixo**.
- Para $x<0$: $x^{5/3}$ é **negativo** (raiz de índice ímpar), logo $x^{-5/3}<0$ e $h''>0$ — concavidade para **cima**.

A concavidade **muda**, e $h$ é contínua em $0$ (com $h(0)=0$). Logo **há** inflexão em $(0,0)$ — com a particularidade de ali a tangente ser **vertical**, pois $h'(x)\to+\infty$ quando $x\to0$.

> 💡 **A lição das quatro juntas.** A definição de inflexão pede duas coisas: **continuidade de $f$** no ponto e **troca de sinal de $f''$**. Ela **não** pede que $f''(c)=0$, nem mesmo que $f''(c)$ exista.
>
> - (b) falha na troca de sinal;
> - (d) falha na continuidade;
> - (c) passa **sem** ter $f''(0)$ — é a prova de que $f''(c)=0$ nunca foi a condição real.
>
> Quem decora "$f''=0$" acerta (a) e (b), e erra (c) e (d).

---

## Questão 8

**Pontos críticos.**

$$f'(x) = 4x^3-16x = 4x\big(x^2-4\big) = 4x(x-2)(x+2)$$

Críticos: $x=-2$, $x=0$ e $x=2$.

**Classificação pelo teste da derivada segunda.** $f''(x) = 12x^2-16$.

| $x$ | $f''(x)$ | Sinal | Conclusão | $f(x)$ |
| :---: | :---: | :---: | --- | :---: |
| $-2$ | $48-16=32$ | $+$ | **mínimo local** | $16-32+3 = -13$ |
| $0$ | $0-16=-16$ | $-$ | **máximo local** | $3$ |
| $2$ | $48-16=32$ | $+$ | **mínimo local** | $16-32+3 = -13$ |

**Resposta.** Mínimos locais em $(-2,\thinspace -13)$ e $(2,\thinspace -13)$; máximo local em $(0,\thinspace 3)$.

> 💡 **Os dois mínimos são absolutos**, já que $f(x)\to+\infty$ nas duas pontas. O máximo em $(0,3)$ é apenas local. E note a simetria: $f$ é **par**, o que explica os dois mínimos com o mesmo valor — verificar a paridade antes de calcular já adiantaria metade do trabalho.

---

## Questão 9

São duas afirmações independentes, e cada uma pede um teorema.

**Parte 1 — existe pelo menos uma raiz (Teorema do Valor Intermediário).**

Seja $f(x) = x^3+x-1$, que é polinômio e portanto **contínua** em $\mathbb{R}$.

$$f(0) = -1 < 0 \qquad f(1) = 1+1-1 = 1 > 0$$

Como $f$ é contínua em $[0,1]$ e troca de sinal, o [TVI](../../02-limites-e-continuidade/2.5-continuidade-e-tipos-de-descontinuidade.md) garante que existe $r\in(0,1)$ com $f(r)=0$ ✔

**Parte 2 — não existe mais de uma (Corolário do TVM).**

$$f'(x) = 3x^2+1 \geqslant 1 > 0 \quad \text{para todo } x\in\mathbb{R}$$

Pelo [Corolário do Teorema do Valor Médio](../4.2-teoremas-de-rolle-e-do-valor-medio.md), $f$ é **estritamente crescente** em $\mathbb{R}$, logo **injetora**: nunca repete um valor. Em particular, assume o valor $0$ **no máximo uma vez**.

**Conclusão.** Juntando as duas partes: a equação tem **exatamente uma** raiz real $\blacksquare$

> 💡 **A alternativa por Rolle (mesma ideia, outro caminho).** Suponha, por absurdo, duas raízes $a<b$. Então $f(a)=f(b)=0$ e, pelo **Teorema de Rolle**, existiria $c\in(a,b)$ com $f'(c)=0$. Mas $f'(x)=3x^2+1$ nunca se anula — contradição. Logo não há duas raízes.
>
> Esse par "**TVI** dá a existência, **Rolle** ou o **corolário do TVM** dá a unicidade" é um dos esquemas de prova mais reutilizáveis do Cálculo 1. Vale memorizar o **formato**, não o exemplo.

---

## Questão 10

**Montagem.** Seja $x$ o comprimento de cada lado **perpendicular** ao rio e $y$ o lado **paralelo** a ele. Como o lado do rio não é cercado, a cerca cobre dois lados $x$ e um lado $y$:

$$2x+y = 400 \ \Longrightarrow \ y = 400-2x$$

**Função a maximizar.**

$$A(x) = x\thinspace y = x(400-2x) = 400x-2x^2$$

**Domínio.** Precisamos de $x>0$ e $y=400-2x>0$, isto é, $x<200$. Logo $x\in(0,\thinspace 200)$.

**Derivando.**

$$A'(x) = 400-4x = 0 \ \Longrightarrow \ x = 100$$

**Confirmando o máximo.** $A''(x) = -4 < 0$: a parábola tem concavidade para baixo, logo o crítico é máximo **absoluto** ✔

(Confirmação adicional: nas bordas, $A(0)=0$ e $A(200)=0$ — o máximo está no interior.)

**Resposta.** $x=100$ m e $y = 400-200 = 200$ m, com

$$A = 100\cdot200 = \mathbf{20\thinspace000\text{ m}^2}$$

> 💡 **O lado do rio tem o dobro dos outros** — e isso **não** é coincidência. Num problema de cerca com um lado livre, a solução ótima sempre gasta metade da cerca no lado paralelo e metade nos dois perpendiculares. Se o terreno fosse cercado nos quatro lados, o ótimo seria o **quadrado** de $100\times100$ (área $10\thinspace000\text{ m}^2$): o rio **dobra** a área possível com a mesma cerca.

---

## Questão 11

**Derivando** pela regra do produto:

$$f'(x) = a\thinspace e^{bx} + a\thinspace x\thinspace b\thinspace e^{bx} = a\thinspace e^{bx}(1+bx)$$

**Condição 1 — $x=2$ é ponto crítico:** $f'(2)=0$, ou seja,

$$a\thinspace e^{2b}(1+2b) = 0$$

Como $e^{2b}\neq0$ sempre, e $a\neq0$ (se $a=0$ então $f\equiv0$, que não tem máximo local), resta

$$1+2b = 0 \ \Longrightarrow \ \boxed{b = -\tfrac12}$$

**Condição 2 — o ponto pertence à curva:** $f(2)=1$, isto é,

$$a\cdot2\cdot e^{2(-1/2)} = 2a\thinspace e^{-1} = 1 \ \Longrightarrow \ \boxed{a = \frac{e}{2}}$$

**Verificando que é máximo.** Derivando $f'(x) = a\thinspace e^{bx}(1+bx)$:

$$f''(x) = a\thinspace b\thinspace e^{bx}(1+bx) + a\thinspace e^{bx}b = a\thinspace b\thinspace e^{bx}(2+bx)$$

Em $x=2$, com $b=-\frac12$ e $a=\frac e2$:

$$f''(2) = \frac{e}{2}\cdot\left(-\frac12\right)e^{-1}(2-1) = -\frac14 < 0 \ \checkmark$$

**Resposta.** $a=\dfrac{e}{2}$ e $b=-\dfrac12$, ou seja, $f(x) = \dfrac{e}{2}\thinspace x\thinspace e^{-x/2}$.

**Conferindo:** $f(2) = \dfrac e2\cdot2\cdot e^{-1} = e\cdot e^{-1} = 1$ ✔

> ⚠️ **A verificação de que $a\neq0$ é parte da resolução.** Sem ela, $a=0$ aparece como "solução" da Condição 1 — e a função nula, que é constante, não tem máximo local. Descartar o caso degenerado é o tipo de rigor que separa a nota cheia da nota parcial.

---

## Questão 12 — síntese

Seja $f(x) = e^x-x-1$.

**(a) O único ponto crítico.**

$$f'(x) = e^x-1$$

$$f'(x) = 0 \iff e^x = 1 \iff x=0$$

e esse valor é **único**, porque a exponencial é injetora.

**Classificando pelo sinal de $f'$:**

| | $x<0$ | $x>0$ |
| --- | :---: | :---: |
| $e^x$ | $<1$ | $>1$ |
| $f'=e^x-1$ | $-$ | $+$ |

A derivada passa de **negativa** para **positiva**: $x=0$ é **mínimo local**. E, sendo o **único** ponto crítico, com $f$ decrescendo em todo $(-\infty,0)$ e crescendo em todo $(0,+\infty)$, ele é **mínimo absoluto**.

**(b) A desigualdade.** O valor mínimo é

$$f(0) = e^0-0-1 = 1-1 = 0$$

Como $f(0)=0$ é o mínimo **absoluto**, tem-se $f(x) \geqslant 0$ para **todo** $x\in\mathbb{R}$, ou seja,

$$e^x-x-1 \geqslant 0 \ \Longrightarrow \ e^x \geqslant x+1 \quad \blacksquare$$

(com igualdade **somente** em $x=0$).

**(c) Concavidade.**

$$f''(x) = e^x > 0 \quad \text{para todo } x$$

A função é **côncava para cima em todo $\mathbb{R}$**, e **não há** pontos de inflexão — $f''$ nunca se anula nem troca de sinal.

**(d) A interpretação geométrica.**

A tangente ao gráfico de $y=e^x$ em $x=0$ passa pelo ponto $\left(0,\thinspace e^0\right) = (0,\thinspace 1)$ e tem inclinação

$$\left.\frac{d}{dx}e^x\right|_{x=0} = e^0 = 1$$

Logo sua equação é $y-1 = 1(x-0)$, isto é, $\mathbf{y = x+1}$ ✔

Agora releia o item **(b)**: ele afirma que

$$e^x \geqslant x+1 \quad \text{para todo } x$$

ou seja, **o gráfico de $y=e^x$ fica sempre acima da sua reta tangente em $x=0$**.

E isso é, palavra por palavra, a **Definição 4.4.1** de concavidade para cima. Como $\big(e^x\big)'' = e^x > 0$ em toda parte, o mesmo vale para a tangente em **qualquer** ponto: a exponencial está sempre acima de todas as suas tangentes $\blacksquare$

> 💡 **O círculo se fecha aqui.** A Unidade 4 começou definindo concavidade pela posição da curva em relação às tangentes — uma ideia puramente geométrica — e provou que ela equivale ao sinal de $f''$. Esta questão percorre o caminho de volta: do sinal de $f''$ de novo até a geometria, e de lá até uma desigualdade ($e^x \geqslant x+1$) que é usada o tempo todo em análise, em probabilidade e em otimização numérica.
>
> É o que a unidade inteira ensina em uma frase: **a derivada segunda é a forma da curva, e a forma da curva prova desigualdades.**

---

## 🏁 Fim da Unidade 4

| Se você acertou | Faça agora |
| --- | --- |
| 11 ou 12 | Siga para a [Unidade 5 · Integral](../../05-integrais/README.md) |
| 8 a 10 | Refaça as questões que errou, depois siga |
| 5 a 7 | Refaça as [listas da unidade](../exercicios/README.md) dos tópicos que falharam |
| 0 a 4 | Volte a [4.1](../4.1-maximos-e-minimos.md) e releia a unidade |

---

| ← Revisão | 🏠 Índice | Próxima unidade → |
| :--- | :---: | ---: |
| [Revisão da Unidade 4](../exercicios/revisao-unidade-4.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [Unidade 5 · Integral](../../05-integrais/README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
