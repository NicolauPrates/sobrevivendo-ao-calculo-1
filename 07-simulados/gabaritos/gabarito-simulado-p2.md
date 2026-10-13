# ✅ Resolução comentada — Simulado P2

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado P2](../simulado-p2-derivadas.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

---

## 📊 Gabarito rápido

| Q. | Resposta |
| :---: | --- |
| **1** | (a) $f'(x) = -\dfrac{1}{(x+1)^2}$ · (b) $y = -\dfrac{x}{4}+\dfrac34$ |
| **2 (a)** | $x^2 e^{2x}(3+2x)$ |
| **2 (b)** | $\dfrac{2}{x^2+1} - \dfrac{\ln\big(x^2+1\big)}{x^2}$ |
| **2 (c)** | $\dfrac{x\cos\left(\sqrt{x^2+1}\right)}{\sqrt{x^2+1}}$ |
| **2 (d)** | $\dfrac{3}{1+9x^2}$ |
| **3** | (a) $y' = -\dfrac{2xy}{x^2+3y^2}$ · (b) $y-2 = -\dfrac{4}{13}(x-1)$ |
| **4** | O topo desce a $\dfrac38 = 0{,}375$ m/s |
| **5** | Base $4\times4$ cm, altura $2$ cm; área mínima $48\text{ cm}^2$ |
| **6** | Ímpar; A.H. $y=0$; mín $\left(-1,-\frac12\right)$, máx $\left(1,\frac12\right)$; inflexões em $x=0$ e $x=\pm\sqrt3$ |

---

## Questão 1 &nbsp;·&nbsp; *(1,5)*

**(a) Pela definição:**

$$f'(x) = \lim_{h\to0}\frac{f(x+h)-f(x)}{h} = \lim_{h\to0}\frac{\dfrac{1}{x+h+1}-\dfrac{1}{x+1}}{h}$$

**Some as frações do numerador** — é o passo que faz o exercício:

$$\frac{1}{x+h+1}-\frac{1}{x+1} = \frac{(x+1)-(x+h+1)}{(x+h+1)(x+1)} = \frac{-h}{(x+h+1)(x+1)}$$

**Divida por $h$** (o $h$ cancela, que é o objetivo de todo o trabalho algébrico):

$$f'(x) = \lim_{h\to0}\frac{-h}{h\thinspace(x+h+1)(x+1)} = \lim_{h\to0}\frac{-1}{(x+h+1)(x+1)} = -\frac{1}{(x+1)^2}$$

**Conferindo pelas regras:** $f(x) = (x+1)^{-1}$, logo $f' = -(x+1)^{-2}$ ✔

**(b) A reta tangente.**

$$f(1) = \frac12 \qquad f'(1) = -\frac{1}{4}$$

$$y - \frac12 = -\frac14(x-1) \ \Longrightarrow \ y = -\frac{x}{4} + \frac34$$

> ⚠️ **"Pela definição" significa pela definição.** Resolver (a) usando a regra da potência zera o item, por mais correta que esteja a resposta. Quando o enunciado nomeia o método, ele está avaliando o método.

---

## Questão 2 &nbsp;·&nbsp; *(2,0)*

**(a)** Regra do **produto**, com a cadeia no segundo fator:

$$f'(x) = 3x^2 e^{2x} + x^3\cdot 2e^{2x} = x^2 e^{2x}\big(3+2x\big)$$

**(b)** Regra do **quociente**:

$$g'(x) = \frac{\dfrac{2x}{x^2+1}\cdot x - \ln\big(x^2+1\big)\cdot 1}{x^2} = \frac{\dfrac{2x^2}{x^2+1} - \ln\big(x^2+1\big)}{x^2}$$

Separando em duas frações:

$$g'(x) = \frac{2}{x^2+1} - \frac{\ln\big(x^2+1\big)}{x^2}$$

**(c)** Cadeia **dupla** — seno de raiz de polinômio:

$$h'(x) = \cos\left(\sqrt{x^2+1}\right)\cdot\frac{1}{2\sqrt{x^2+1}}\cdot 2x = \frac{x\cos\left(\sqrt{x^2+1}\right)}{\sqrt{x^2+1}}$$

**(d)** Com $u=3x$ e $u'=3$:

$$y' = \frac{3}{1+(3x)^2} = \frac{3}{1+9x^2}$$

> ⚠️ **Em (d), o quadrado é do $3x$ inteiro**, não só do $x$. Escrever $\frac{3}{1+3x^2}$ é o erro mais comum do item.

---

## Questão 3 &nbsp;·&nbsp; *(1,5)*

**Verificando que o ponto pertence à curva:** $1^2\cdot2 + 2^3 = 2+8 = 10$ ✔

**(a)** Derive **os dois lados** em relação a $x$, lembrando que $y$ é função de $x$ (logo todo $y$ derivado produz um $y'$):

$$\frac{d}{dx}\big(x^2y\big) + \frac{d}{dx}\big(y^3\big) = \frac{d}{dx}(10)$$

O primeiro termo exige a regra do **produto**:

$$\underbrace{2xy + x^2 y'}_{\text{produto}} + \underbrace{3y^2 y'}_{\text{cadeia}} = 0$$

**Isolando $y'$:**

$$y'\big(x^2+3y^2\big) = -2xy \ \Longrightarrow \ \boxed{\ y' = -\frac{2xy}{x^2+3y^2}\ }$$

**(b)** Em $(1,2)$:

$$y' = -\frac{2(1)(2)}{1+3(4)} = -\frac{4}{13}$$

$$y - 2 = -\frac{4}{13}(x-1)$$

> 💡 **Note que $y'$ depende de $x$ **e** de $y$.** Isso é característico da derivação implícita, e não é defeito: a curva não é gráfico de função, então a inclinação precisa dos dois valores para ser determinada.

---

## Questão 4 &nbsp;·&nbsp; *(1,5)*

**A montagem.** Sejam $x$ a distância da base à parede e $y$ a altura do topo, ambas funções do tempo. Pelo **Teorema de Pitágoras**, a escada tem comprimento constante:

$$x^2+y^2 = 25$$

**Derivando em relação a $t$** — os dois lados:

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0 \ \Longrightarrow \ \frac{dy}{dt} = -\frac{x}{y}\cdot\frac{dx}{dt}$$

**O instante pedido.** Quando $x=3$:

$$y = \sqrt{25-9} = 4$$

Com $\dfrac{dx}{dt} = 0{,}5$ m/s:

$$\frac{dy}{dt} = -\frac{3}{4}\cdot 0{,}5 = -\frac38 = -0{,}375 \text{ m/s}$$

**Resposta.** O topo desce a $0{,}375$ m/s — o sinal negativo indica que $y$ está **diminuindo**.

> [!TIP]
> **A ordem dos passos é o que a questão avalia:**
> 1. relação **geométrica** entre as variáveis (aqui, Pitágoras);
> 2. derivar **em relação a $t$**;
> 3. **só então** substituir os valores do instante.
>
> Quem substitui $x=3$ **antes** de derivar transforma a relação numa constante e obtém $\frac{dy}{dt}=0$ — resposta absurda, e erro frequente.

---

## Questão 5 &nbsp;·&nbsp; *(1,5)*

**(a) A montagem.** Sejam $x$ o lado da base quadrada e $h$ a altura.

- **Restrição** (volume dado): $x^2h = 32 \Rightarrow h = \dfrac{32}{x^2}$
- **Função a minimizar** (base **sem tampa** mais quatro laterais): $A = x^2 + 4xh$

**Eliminando $h$:**

$$A(x) = x^2 + 4x\cdot\frac{32}{x^2} = x^2 + \frac{128}{x}, \qquad x>0$$

**Derivando:**

$$A'(x) = 2x - \frac{128}{x^2} = 0 \ \Longrightarrow \ 2x^3 = 128 \ \Longrightarrow \ x^3 = 64 \ \Longrightarrow \ x = 4$$

$$h = \frac{32}{16} = 2$$

**Dimensões:** base $4\times4$ cm e altura $2$ cm.

**(b) Justificativa.**

$$A''(x) = 2 + \frac{256}{x^3} > 0 \quad\text{para todo } x>0$$

A função é côncava para cima em todo o domínio, logo o único ponto crítico é mínimo **absoluto** ✔

**(c) A área mínima:**

$$A(4) = 16 + \frac{128}{4} = 16+32 = 48\text{ cm}^2$$

> 💡 **Note que $h = \frac{x}{2}$:** a caixa ótima tem altura igual a **metade** do lado da base. Compare com a lata **fechada** (exercício 2 da [revisão da U4](../../04-aplicacoes-das-derivadas/exercicios/revisao-unidade-4.md)), em que a altura ótima é igual ao **diâmetro**. A diferença vem exatamente de faltar a tampa: sem ela, compensa alargar a base e baixar a caixa.

> ⚠️ **"Sem tampa" é a informação que decide o problema.** Com tampa, a função seria $A = 2x^2+4xh$ e a resposta mudaria. Sublinhar essa palavra no enunciado vale a questão inteira.

---

## Questão 6 &nbsp;·&nbsp; *(2,0)*

**1. Domínio.** $x^2+1$ nunca zera: $D = \mathbb{R}$.

**2. Interseções.** $\dfrac{x}{x^2+1}=0 \iff x=0$. Único corte: a **origem**.

**3. Simetria.** $f(-x) = \dfrac{-x}{x^2+1} = -f(x)$: função **ímpar**, simétrica em relação à origem.

**4. Assíntotas.** Não há verticais. Grau do numerador menor que o do denominador:

$$\lim_{x\to\pm\infty}\frac{x}{x^2+1} = 0 \ \Longrightarrow \ y=0 \text{ é assíntota horizontal}$$

**5. Crescimento.** Pela regra do quociente:

$$f'(x) = \frac{1\cdot\big(x^2+1\big) - x(2x)}{\big(x^2+1\big)^2} = \frac{1-x^2}{\big(x^2+1\big)^2}$$

O denominador é sempre positivo; o sinal é o de $1-x^2 = (1-x)(1+x)$:

| | $x<-1$ | $-1<x<1$ | $x>1$ |
| --- | :---: | :---: | :---: |
| $f'$ | $-$ | $+$ | $-$ |

**Mínimo local** em $\left(-1,\thinspace -\frac12\right)$ e **máximo local** em $\left(1,\thinspace \frac12\right)$ — ambos **absolutos**, já que a função tende a zero nas duas pontas.

**6. Concavidade.** Derivando de novo e simplificando:

$$f''(x) = \frac{2x\big(x^2-3\big)}{\big(x^2+1\big)^3}$$

O denominador é positivo; o sinal é o de $2x\big(x-\sqrt3\big)\big(x+\sqrt3\big)$:

| | $x<-\sqrt3$ | $-\sqrt3<x<0$ | $0<x<\sqrt3$ | $x>\sqrt3$ |
| --- | :---: | :---: | :---: | :---: |
| $f''$ | $-$ | $+$ | $-$ | $+$ |

**Três pontos de inflexão:** $x=-\sqrt3$, $x=0$ e $x=\sqrt3$, com $f\left(\pm\sqrt3\right) = \pm\dfrac{\sqrt3}{4}$.

**7. Tabela-resumo.**

| Intervalo | $f'$ | $f''$ | Comportamento |
| :---: | :---: | :---: | --- |
| $\left(-\infty,-\sqrt3\right)$ | $-$ | $-$ | desce, concavidade para baixo |
| $\left(-\sqrt3,-1\right)$ | $-$ | $+$ | desce, concavidade para cima |
| $(-1,0)$ | $+$ | $+$ | sobe, concavidade para cima |
| $\left(0,1\right)$ | $+$ | $-$ | sobe, concavidade para baixo |
| $\left(1,\sqrt3\right)$ | $-$ | $-$ | desce, concavidade para baixo |
| $\left(\sqrt3,+\infty\right)$ | $-$ | $+$ | desce, concavidade para cima |

**8. O desenho.** Curva em "S" deitado, simétrica em relação à origem: vem de $0^{-}$, desce até o vale $-\frac12$ em $x=-1$, sobe cruzando a origem, atinge o pico $\frac12$ em $x=1$ e decai de volta a zero.

> 💡 **O resultado tem uma consequência útil:** como os extremos absolutos são $\pm\frac12$,
>
> $$\left\lvert\frac{x}{x^2+1}\right\rvert \leqslant \frac12 \qquad\text{para todo } x$$
>
> O esboço entregou uma desigualdade de graça — e é assim que boa parte das desigualdades de análise é demonstrada.

> ⚠️ **Esta curva também responde a uma pegadinha clássica:** ela **cruza** a própria assíntota horizontal, em $x=0$. Assíntota descreve o comportamento **no infinito**; o que acontece no meio do caminho é livre.

---

## 📋 Diagnóstico

| Acertos | O que fazer |
| :---: | --- |
| 5 ou 6 | Pronto para a P2. Revise só a tabela de derivadas na véspera. |
| 3 ou 4 | Refaça as [revisões da U3](../../03-derivadas/exercicios/revisao-unidade-3.md) e da [U4](../../04-aplicacoes-das-derivadas/exercicios/revisao-unidade-4.md). |
| 0 a 2 | Volte às listas das seções que falharam, começando pela [regra da cadeia](../../03-derivadas/3.3-regra-da-cadeia-e-derivada-da-funcao-inversa.md). |

**Se você errou a questão 6**, refaça-a antes de qualquer outra coisa: o esboço completo é a questão que mais aparece em prova, e a única que cobra as quatro unidades ao mesmo tempo.

---

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado P2](../simulado-p2-derivadas.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
