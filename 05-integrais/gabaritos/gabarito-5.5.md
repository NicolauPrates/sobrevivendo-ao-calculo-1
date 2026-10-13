# ✅ Gabarito — Lista 5.5

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 5.5](../exercicios/lista-5.5-propostos.md) · [Teoria 5.5](../5.5-integrais-improprias.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | Imprópria, **tipo 1** (limite superior infinito) |
| 1 (b) | **Não** é imprópria — o $x=2$ está fora de $[0,1]$ |
| 1 (c) | Imprópria, **tipo 2** em $x=1$, **dentro** do intervalo |
| 1 (d) | Imprópria, **tipo 2** em $x=1$ (extremo inferior) |
| 1 (e) | Imprópria, **tipo 1** nos **dois** limites |
| 1 (f) | Imprópria, **tipo 2** em $x=\frac{\pi}{2}$, **dentro** do intervalo |
| 2 (a) | Converge ($p=3>1$) |
| 2 (b) | Diverge ($p=\frac12\leqslant1$) |
| 2 (c) | Diverge ($p=3\geqslant1$) |
| 2 (d) | Converge ($p=\frac13<1$) |
| 3 (a) | $\dfrac12$ |
| 3 (b) | $\dfrac13$ |
| 3 (c) | $1$ |
| 4 (a) | $4$ |
| 4 (b) | $-1$ |
| 4 (c) | **Diverge** |
| 5 | $\pi$ |
| 6 | Diverge; o TFC foi aplicado por cima da descontinuidade |
| 7 (a) | $p>1$ |
| 7 (b) | $p<1$ |
| 8 (a) | **Converge** |
| 8 (b) | **Diverge** |
| 9 | (a) F · (b) V · (c) F · (d) V |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 10 | $\dfrac12$ |
| 11 | **Diverge** |
| 12 | $\dfrac{1}{\ln 2}$ |
| 13 | $\dfrac12$ |
| 14 | $\dfrac{\pi}{2}$ |
| 15 | **Diverge** |
| 16 | $0$ (converge) |
| 17 | $\dfrac12$ |
| 18 (a) | **Diverge** |
| 18 (b) | **Converge** |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | **Nenhum $p$** — diverge sempre |
| 20 | Demonstração |
| 21 | $V=\pi$ (converge) e $A$ diverge |
| 22 | $\dfrac12 < a < 1$ |

---

# 📖 Parte 2 — Resoluções completas

## Bloco A · Fixação

### 1.

| | É imprópria? | Tipo | Onde |
| :---: | :---: | :---: | --- |
| **(a)** | sim | 1 | o limite superior é $\infty$ |
| **(b)** | **não** | — | $x-2$ zera em $x=2$, **fora** de $[0,1]$ |
| **(c)** | sim | 2 | $x=1$, **dentro** de $[0,2]$ — precisa quebrar |
| **(d)** | sim | 2 | $\ln(x-1)\to-\infty$ quando $x\to1^{+}$ |
| **(e)** | sim | 1 | **os dois** limites são infinitos |
| **(f)** | sim | 2 | $\operatorname{tg} x$ explode em $x=\frac{\pi}{2}$, dentro de $[0,\pi]$ |

> ⚠️ **O item (b) é a pegadinha, e é a mais importante da lista.** A presença de um denominador que zera **não** torna a integral imprópria — ele precisa zerar **dentro** do intervalo. Em $[0,1]$, a função $\frac{1}{x-2}$ é perfeitamente contínua (vale entre $-1$ e $-\frac12$), e o TFC se aplica normalmente.
>
> **Sempre localize o ponto ruim e compare com o intervalo.** É um passo de cinco segundos que separa a questão certa da errada.

---

### 2.

| | $p$ | Regra | Veredito |
| :---: | :---: | --- | :---: |
| **(a)** | $3$ | no infinito, converge se $p>1$ | **converge** |
| **(b)** | $\frac12$ | no infinito, $p\leqslant1$ | **diverge** |
| **(c)** | $3$ | no zero, converge se $p<1$ | **diverge** |
| **(d)** | $\frac13$ | no zero, $p<1$ | **converge** |

> 💡 **Compare (a) com (c): mesmo $p=3$, vereditos opostos.** O expoente grande faz a função decair **rápido** longe da origem (bom para $\int_1^\infty$) e explodir **violentamente** perto de zero (ruim para $\int_0^1$). Não existe "$p$ bom"; existe $p$ bom **para cada região**.

---

### 3.

**(a)**

$$\int_0^{\infty}e^{-2x}dx = \lim_{b\to\infty}\left[-\frac{e^{-2x}}{2}\right]_0^{b} = \lim_{b\to\infty}\left(\frac12-\frac{1}{2e^{2b}}\right) = \frac12$$

**(b)** Com $p=4>1$, o teorema dá direto $\dfrac{1}{p-1} = \dfrac13$. Verificando:

$$\int_1^{\infty}x^{-4}dx = \lim_{b\to\infty}\left[-\frac{1}{3x^3}\right]_1^{b} = \frac13$$

**(c)**

$$\int_{-\infty}^{0}e^{x}dx = \lim_{a\to-\infty}\Big[e^{x}\Big]_a^{0} = \lim_{a\to-\infty}\big(1-e^{a}\big) = 1$$

---

### 4.

**(a)** Singularidade em $x=0$ (extremo inferior):

$$\int_0^{4}\frac{dx}{\sqrt x} = \lim_{t\to0^{+}}\Big[2\sqrt x\Big]_t^{4} = \lim_{t\to0^{+}}\big(4-2\sqrt t\big) = 4$$

**(b)** $\ln x\to-\infty$ quando $x\to0^{+}$. A primitiva é $x\ln x - x$:

$$\int_0^{1}\ln x\thinspace dx = \lim_{t\to0^{+}}\Big[x\ln x - x\Big]_t^{1} = \big(0-1\big) - \lim_{t\to0^{+}}\big(t\ln t - t\big)$$

Pela hierarquia do infinito, $t\ln t\to0$. Logo:

$$\int_0^{1}\ln x\thinspace dx = -1-0 = -1$$

> 💡 **Resposta negativa, e está certo:** $\ln x<0$ em todo $(0,1)$, então a região fica **abaixo** do eixo. A área é $1$; a integral é $-1$.

**(c)** Singularidade em $x=1$ (extremo inferior):

$$\int_1^{2}\frac{dx}{x-1} = \lim_{t\to1^{+}}\Big[\ln\lvert x-1\rvert\Big]_t^{2} = \lim_{t\to1^{+}}\big(0-\ln(t-1)\big) = +\infty$$

**DIVERGE.**

---

### 5.

Os **dois** limites são infinitos, então quebre (em $0$, por conveniência):

$$\int_{-\infty}^{\infty}\frac{dx}{1+x^2} = \int_{-\infty}^{0}\frac{dx}{1+x^2} + \int_{0}^{\infty}\frac{dx}{1+x^2}$$

$$\int_0^{\infty}\frac{dx}{1+x^2} = \lim_{b\to\infty}\Big[\operatorname{arctg} x\Big]_0^{b} = \frac{\pi}{2}-0 = \frac{\pi}{2}$$

$$\int_{-\infty}^{0}\frac{dx}{1+x^2} = \lim_{a\to-\infty}\Big[\operatorname{arctg} x\Big]_a^{0} = 0-\left(-\frac{\pi}{2}\right) = \frac{\pi}{2}$$

**As duas convergem**, logo a soma vale

$$\int_{-\infty}^{\infty}\frac{dx}{1+x^2} = \pi$$

> 💡 **A área total sob a curva de Agnesi é exatamente $\pi$** — um resultado bonito, e a razão de $\frac{1}{\pi(1+x^2)}$ ser uma densidade de probabilidade (a **distribuição de Cauchy**): dividir por $\pi$ faz a área valer $1$.

---

### 6.

**Por que diverge.** O integrando explode em $x=1$, que está **dentro** de $[0,2]$. Quebrando:

$$\int_0^{2}\frac{dx}{(x-1)^2} = \int_0^{1}\frac{dx}{(x-1)^2} + \int_1^{2}\frac{dx}{(x-1)^2}$$

Calculando a segunda metade:

$$\int_1^{2}\frac{dx}{(x-1)^2} = \lim_{t\to1^{+}}\left[-\frac{1}{x-1}\right]_t^{2} = \lim_{t\to1^{+}}\left(-1+\frac{1}{t-1}\right) = +\infty$$

**Uma das metades diverge ⟹ a integral toda diverge.** (Não é preciso calcular a outra.)

**Por que a conta do enunciado está errada.** Ela aplica o TFC diretamente em $[0,2]$ — mas o teorema **exige que o integrando seja contínuo em todo o intervalo**, e aqui ele não é: há uma assíntota vertical em $x=1$. A fórmula $F(b)-F(a)$ simplesmente não vale nesse caso.

**E dá para saber que está errada sem teoria nenhuma:** o integrando $\frac{1}{(x-1)^2}$ é **positivo** em todo ponto onde existe, e a conta deu $-2$. Área positiva não dá resultado negativo.

> [!TIP]
> **Guarde este teste de sanidade.** Integrando positivo com resultado negativo = você passou por cima de uma descontinuidade. É o sinal mais confiável de que a integral era imprópria e você não percebeu.

---

### 7.

**(a)** $\displaystyle\int_2^{\infty}\frac{dx}{x^p}$ — o único problema é o $\infty$ (em $x=2$ a função é perfeitamente contínua). Vale o Teorema 5.5.1:

$$\textbf{converge} \iff p>1$$

> 💡 O limite inferior ser $2$ em vez de $1$ **não muda nada**: a convergência é decidida pela cauda, e o trecho finito $[1,2]$ contribui com uma área finita de qualquer jeito.

**(b)** $\displaystyle\int_0^{3}\frac{dx}{x^p}$ — o problema é o $0$. Pelo Teorema 5.5.2:

$$\textbf{converge} \iff p<1$$

---

### 8.

**(a)** Quero provar **convergência**, logo preciso de um **teto** que convirja.

Para $x\geqslant1$: $x^3+1 > x^3$, e invertendo,

$$0 < \frac{1}{x^3+1} < \frac{1}{x^3}$$

Como $\displaystyle\int_1^{\infty}\frac{dx}{x^3}$ converge ($p=3>1$), o teste da comparação dá:

$$\int_1^{\infty}\frac{dx}{x^3+1} \quad\textbf{CONVERGE}$$

**(b)** Quero provar **divergência**, logo preciso de um **piso** que divirja.

Como $\operatorname{sen} x\geqslant-1$ sempre, tem-se $2+\operatorname{sen} x\geqslant 1$, e para $x\geqslant1$:

$$\frac{2+\operatorname{sen} x}{x} \geqslant \frac{1}{x} > 0$$

Como $\displaystyle\int_1^{\infty}\frac{dx}{x}$ diverge, a comparação dá:

$$\int_1^{\infty}\frac{2+\operatorname{sen} x}{x}dx \quad\textbf{DIVERGE}$$

> 💡 **O seno oscilando não atrapalha** — basta limitá-lo. O fator $2+\operatorname{sen} x$ vive entre $1$ e $3$, então o integrando é, a menos de uma constante, exatamente $\frac1x$. **Limitar o fator chato por constantes** é a jogada padrão quando aparece seno ou cosseno num teste de comparação.

---

### 9.

**(a) Falso.** O contraexemplo é o mais importante da seção: $f(x)=\frac1x$ tende a zero e $\displaystyle\int_1^{\infty}\frac{dx}{x}$ **diverge**.

Tender a zero é **necessário** (se $f\not\to0$, a integral certamente diverge), mas longe de suficiente: é preciso tender **rápido o bastante**.

**(b) Verdadeiro.** É exatamente o teste da comparação: $g$ está ensanduichada entre $0$ e uma função cuja integral converge.

**(c) Falso.** Cada metade diverge:

$$\int_0^{\infty}x\thinspace dx = \lim_{b\to\infty}\frac{b^2}{2} = +\infty$$

e, por simetria, a outra tende a $-\infty$. A definição exige que **ambas** convirjam, logo a integral **diverge**.

O "argumento de simetria" calcula na verdade $\displaystyle\lim_{b\to\infty}\int_{-b}^{b}x\thinspace dx$, que é uma coisa diferente (chama-se **valor principal de Cauchy**) e **não** é a integral imprópria.

**(d) Verdadeiro.** Para $f\geqslant0$, a função $b\mapsto\displaystyle\int_a^b f$ é **crescente** em $b$ — acrescentar intervalo só acrescenta área. Uma função crescente ou tem limite finito, ou tende a $+\infty$; não há terceira possibilidade.

> 💡 **Para funções que trocam de sinal isso falha.** Em $\displaystyle\int_0^{\infty}\operatorname{sen} x\thinspace dx$, a integral parcial é $1-\cos b$, que **oscila** entre $0$ e $2$ sem tender a nada. A integral diverge, mas não "para $+\infty$" — ela simplesmente não tem limite.

---

## Bloco B · Consolidação

### 10.

Com $u=x^2$ e $x\thinspace dx = \frac{du}{2}$ (limites: $0\to0$ e $\infty\to\infty$):

$$\int_0^{\infty}x\thinspace e^{-x^2}dx = \frac12\int_0^{\infty}e^{-u}du = \frac12\lim_{b\to\infty}\Big[-e^{-u}\Big]_0^{b} = \frac12\big(0+1\big) = \frac12$$

**CONVERGE.**

---

### 11.

Com $u = \ln x$ e $du = \frac{dx}{x}$ (limites: $x=2\Rightarrow u=\ln2$; $x\to\infty\Rightarrow u\to\infty$):

$$\int_2^{\infty}\frac{dx}{x\ln x} = \int_{\ln 2}^{\infty}\frac{du}{u} = \lim_{c\to\infty}\Big[\ln u\Big]_{\ln 2}^{c} = +\infty$$

**DIVERGE.**

---

### 12.

Mesma substituição:

$$\int_2^{\infty}\frac{dx}{x\big(\ln x\big)^2} = \int_{\ln 2}^{\infty}\frac{du}{u^2} = \lim_{c\to\infty}\left[-\frac1u\right]_{\ln2}^{c} = \frac{1}{\ln 2}$$

**CONVERGE**, e vale $\dfrac{1}{\ln 2}\approx1{,}44$.

> 💡 **Os exercícios 11 e 12 são a versão logarítmica do par $\frac1x$ versus $\frac{1}{x^2}$.** Depois da substituição $u=\ln x$, eles **viram** exatamente aquele par — e por isso têm destinos opostos pela mesma razão.
>
> O detalhe impressionante: $\frac{1}{x\ln x}$ decai **mais rápido** que $\frac1x$, e mesmo assim ainda diverge. O logaritmo cresce devagar demais para salvar a integral. É preciso o **quadrado** dele para virar o jogo.

---

### 13.

Com $u = 1+x$ (limites: $1$ e $\infty$):

$$\int_0^{\infty}\frac{dx}{(1+x)^3} = \int_1^{\infty}\frac{du}{u^3} = \frac{1}{3-1} = \frac12$$

**CONVERGE** (é uma $p$-integral com $p=3>1$, disfarçada pela translação).

---

### 14.

Imprópria do **tipo 2**: o denominador zera em $x=1$ (extremo superior).

$$\int_0^{1}\frac{dx}{\sqrt{1-x^2}} = \lim_{t\to1^{-}}\Big[\operatorname{arcsen} x\Big]_0^{t} = \operatorname{arcsen}(1) - 0 = \frac{\pi}{2}$$

**CONVERGE.**

> ⚠️ **Muita gente resolve esta integral sem perceber que ela é imprópria** — e, por sorte, chega ao resultado certo, porque $\operatorname{arcsen}$ é contínua em $x=1$. **A sorte não é método:** o mesmo descuido em $\int_{-1}^{1}\frac{dx}{x^2}$ produz $-2$.

---

### 15.

Com $u = 1+x^2$ e $x\thinspace dx = \frac{du}{2}$ (limites: $1$ e $\infty$):

$$\int_0^{\infty}\frac{x\thinspace dx}{1+x^2} = \frac12\int_1^{\infty}\frac{du}{u} = \frac12\lim_{c\to\infty}\ln c = +\infty$$

**DIVERGE.**

> 💡 **Compare com o exercício 5.** Lá, $\frac{1}{1+x^2}$ convergia; aqui, o mesmo denominador com um $x$ no numerador diverge. O numerador extra faz o integrando se comportar como $\frac1x$ em vez de $\frac{1}{x^2}$ — e isso muda tudo.
>
> **Para decidir uma integral imprópria de função racional, compare os graus:** se o denominador excede o numerador em **mais de uma** unidade, converge; se excede em exatamente uma (como aqui), diverge.

---

### 16.

$\dfrac{1}{\sqrt[3]{x}} = x^{-1/3}$ explode em $x=0$, que está **dentro** de $[-1,1]$. **Quebre.**

**Metade direita:**

$$\int_0^{1}x^{-1/3}dx = \lim_{t\to0^{+}}\left[\frac32 x^{2/3}\right]_t^{1} = \frac32$$

(Converge, como previsto pelo Teorema 5.5.2 com $p=\frac13<1$.)

**Metade esquerda:**

$$\int_{-1}^{0}x^{-1/3}dx = \lim_{t\to0^{-}}\left[\frac32 x^{2/3}\right]_{-1}^{t} = 0-\frac32 = -\frac32$$

**As duas convergem**, logo a integral converge:

$$\int_{-1}^{1}\frac{dx}{\sqrt[3]{x}} = \frac32 + \left(-\frac32\right) = 0$$

> 💡 **O resultado $0$ sai da paridade:** $x^{-1/3}$ é **ímpar**, e o intervalo é simétrico. Mas atenção — **a paridade só pode ser invocada depois de verificar a convergência**. Em $\int_{-1}^{1}\frac{dx}{x}$ o integrando também é ímpar e a integral **diverge**, porque cada metade é infinita. Compare com o item 9(c): o mesmo erro, em outra roupa.

---

### 17.

A primitiva sai pela integração por partes circular de [5.2](../5.2-tecnicas-de-integracao.md), adaptada a $e^{-x}$:

$$\int e^{-x}\operatorname{sen} x\thinspace dx = -\frac{e^{-x}}{2}\big(\operatorname{sen} x + \cos x\big)$$

**Conferindo:**

$$\left[-\frac{e^{-x}}{2}(\operatorname{sen} x+\cos x)\right]' = \frac{e^{-x}}{2}(\operatorname{sen} x+\cos x) - \frac{e^{-x}}{2}(\cos x-\operatorname{sen} x) = e^{-x}\operatorname{sen} x \ \checkmark$$

Agora o limite:

$$\int_0^{\infty}e^{-x}\operatorname{sen} x\thinspace dx = \lim_{b\to\infty}\left[-\frac{e^{-x}}{2}\big(\operatorname{sen} x+\cos x\big)\right]_0^{b}$$

Em $b$: o fator $(\operatorname{sen} b+\cos b)$ é **limitado** (fica entre $-\sqrt2$ e $\sqrt2$) e $e^{-b}\to0$, logo o produto tende a $0$.

Em $0$: $-\frac12(0+1) = -\frac12$.

$$\int_0^{\infty}e^{-x}\operatorname{sen} x\thinspace dx = 0-\left(-\frac12\right) = \frac12$$

**CONVERGE.**

> 💡 **"Limitado vezes algo que tende a zero tende a zero"** é o argumento que fecha a questão — o mesmo do [Teorema do Sanduíche](../../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md). Sem ele, seria tentador dizer que $\operatorname{sen} b$ "não tem limite, logo a integral diverge" — conclusão errada, porque a exponencial esmaga a oscilação.

---

### 18.

**(a)** Para $x\geqslant e$, tem-se $\ln x\geqslant1$, logo

$$\frac{\ln x}{x} \geqslant \frac1x > 0$$

Como $\displaystyle\int_e^{\infty}\frac{dx}{x}$ diverge, a comparação dá divergência em $[e,\infty)$ — e acrescentar o trecho finito $[1,e]$ não muda nada:

$$\int_1^{\infty}\frac{\ln x}{x}dx \quad\textbf{DIVERGE}$$

> 💡 Dá para confirmar calculando: com $u=\ln x$, a integral vira $\int_0^{\infty}u\thinspace du = \infty$.

**(b)** Para $x\geqslant1$, tem-se $x^2\geqslant x$, logo $-x^2\leqslant-x$ e, como a exponencial é crescente,

$$0 < e^{-x^2} \leqslant e^{-x}$$

Como $\displaystyle\int_1^{\infty}e^{-x}dx = \frac1e$ converge:

$$\int_1^{\infty}e^{-x^2}dx \quad\textbf{CONVERGE}$$

> 💡 **Esta é a integral mais importante da estatística, e a comparação é a única saída.** A função $e^{-x^2}$ **não tem primitiva elementar** — está demonstrado que ela não pode ser escrita com funções elementares. O teste da comparação decide a convergência sem nunca calcular nada.
>
> E o valor existe: $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}dx = \sqrt{\pi}$, um dos resultados mais famosos da matemática. A demonstração exige coordenadas polares em integrais duplas — assunto de Cálculo 2.

---

## Bloco C · Desafio

### 19.

A integral $\displaystyle\int_0^{\infty}\frac{dx}{x^p}$ é imprópria **nas duas pontas**: em $0$ (o integrando explode, para $p>0$) e em $\infty$. Quebre em $x=1$:

$$\int_0^{\infty}\frac{dx}{x^p} = \underbrace{\int_0^{1}\frac{dx}{x^p}}_{\text{Teorema 5.5.2}} + \underbrace{\int_1^{\infty}\frac{dx}{x^p}}_{\text{Teorema 5.5.1}}$$

| Parcela | Converge se |
| --- | :---: |
| $\displaystyle\int_0^{1}\frac{dx}{x^p}$ | $p<1$ |
| $\displaystyle\int_1^{\infty}\frac{dx}{x^p}$ | $p>1$ |

Para a integral total convergir, **as duas** precisam convergir — ou seja, seria preciso ter $p<1$ **e** $p>1$ ao mesmo tempo.

**Impossível.** Logo:

$$\int_0^{\infty}\frac{dx}{x^p} \quad\textbf{diverge para TODO } p \quad\blacksquare$$

> 💡 **A lição é geral e vale guardar.** Nenhuma potência pura $x^{-p}$ é integrável em $(0,\infty)$: ou ela explode rápido demais na origem, ou decai devagar demais no infinito. **Não existe expoente que sirva nas duas pontas.**
>
> Por isso, toda função que de fato é integrável em $(0,\infty)$ — como $e^{-x}$, ou $\frac{1}{1+x^2}$ — precisa **mudar de comportamento** entre as duas regiões. É exatamente o que o exercício 22 explora.

---

### 20.

A integral é imprópria em $x=0$, onde $\ln x\to-\infty$.

**Por partes**, com $u=\ln x$ e $dv = x^n dx$:

$$du = \frac{dx}{x} \qquad v = \frac{x^{n+1}}{n+1}$$

$$\int_0^1 x^n\ln x\thinspace dx = \left[\frac{x^{n+1}\ln x}{n+1}\right]_0^1 - \frac{1}{n+1}\int_0^1 \frac{x^{n+1}}{x}dx$$

**O termo de fronteira é zero nas duas pontas:**

- em $x=1$: $\dfrac{1\cdot\ln 1}{n+1} = 0$;
- em $x\to0^{+}$: $x^{n+1}\ln x\to0$, pela hierarquia do infinito (a potência vence o logaritmo, pois $n+1\geqslant1>0$ — é o exercício 20 da [Lista 4.3](../../04-aplicacoes-das-derivadas/exercicios/lista-4.3-propostos.md)).

**Sobra a integral da direita:**

$$-\frac{1}{n+1}\int_0^1 x^n dx = -\frac{1}{n+1}\left[\frac{x^{n+1}}{n+1}\right]_0^1 = -\frac{1}{(n+1)^2}$$

$$\int_0^1 x^n\ln x\thinspace dx = -\frac{1}{(n+1)^2} \quad\blacksquare$$

**Conferindo em $n=0$:** a fórmula dá $-1$, que é exatamente o resultado do exercício 4(b) ✔

---

### 21. A trombeta de Gabriel, reescrita

**(a) O volume**, pelo método do disco com raio $\frac1x$, agora como integral imprópria:

$$V = \pi\int_1^{\infty}\frac{dx}{x^2}$$

É uma $p$-integral com $p=2>1$, logo **converge**, e vale $\dfrac{1}{p-1}=1$:

$$V = \pi\cdot 1 = \pi$$

**(b)** Já está: $V=\pi$, **finito**.

**(c) A área da região plana:**

$$A = \int_1^{\infty}\frac{dx}{x}$$

$p$-integral com $p=1$ — **diverge**. A área é **infinita**.

> 💡 **A seção 5.5 explica o paradoxo em uma linha.** O volume integra $\frac{1}{x^2}$ (porque o raio é elevado ao quadrado) e a área integra $\frac1x$. São exatamente as duas integrais do Exercício Resolvido 1 — a que converge e a que diverge.
>
> **O quadrado do método do disco é o responsável pelo paradoxo inteiro.** Ele empurra o expoente de $1$ para $2$, cruzando a fronteira $p=1$. Não há mistério: há uma $p$-integral de cada lado da linha.

---

### 22.

A integral $\displaystyle\int_0^{\infty}\frac{dx}{x^a+x^{2a}}$ é imprópria nas **duas** pontas. Analise cada uma separadamente, perguntando **qual termo do denominador domina**.

**Perto de $0$.** Para $x$ pequeno e $a>0$, tem-se $x^{2a}\ll x^{a}$ (expoente maior, base menor que $1$). O denominador se comporta como $x^a$:

$$\frac{1}{x^a+x^{2a}} \approx \frac{1}{x^a}$$

Pelo Teorema 5.5.2, essa parte converge se, e só se, $a<1$.

**Perto de $\infty$.** Agora $x^{2a}\gg x^{a}$, e o denominador se comporta como $x^{2a}$:

$$\frac{1}{x^a+x^{2a}} \approx \frac{1}{x^{2a}}$$

Pelo Teorema 5.5.1, essa parte converge se, e só se, $2a>1$, isto é, $a>\dfrac12$.

**Juntando as duas condições:**

$$\boxed{\ \frac12 < a < 1\ }$$

**Testando os extremos** para confirmar que são excluídos:

- $a=1$: perto de zero o integrando vira $\frac1x$ — diverge ✗
- $a=\frac12$: no infinito o integrando vira $\frac1x$ — diverge ✗
- $a=\frac34$ (no meio): perto de zero é $x^{-3/4}$, com $p<1$ ✔; no infinito é $x^{-3/2}$, com $p>1$ ✔ **converge**

> 💡 **Esta questão é o exercício 19 ao contrário, e resume a seção.** Lá, uma potência **pura** não conseguia servir às duas pontas. Aqui, a soma $x^a+x^{2a}$ consegue — porque ela **muda de comportamento**: perto de zero age como $x^a$, longe age como $x^{2a}$.
>
> E a faixa de sucesso é estreita: o expoente precisa ser grande o bastante para domar o infinito ($2a>1$) e pequeno o bastante para não explodir na origem ($a<1$). **Convergência em $(0,\infty)$ é sempre esse equilíbrio** — e é por isso que a distribuição normal usa $e^{-x^2}$, que decai mais rápido que qualquer potência no infinito e é perfeitamente finita na origem.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 5.5](../exercicios/lista-5.5-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [5.5 · Teoria](../5.5-integrais-improprias.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
