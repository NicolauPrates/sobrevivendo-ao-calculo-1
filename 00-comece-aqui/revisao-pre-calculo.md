# ⭐ Revisão de Pré-Cálculo

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [Como usar este material](como-usar-este-material.md) | [Comece aqui](README.md) · [Página inicial](../README.md) | [Plano de estudos](plano-de-estudos.md) |

> **Se você só vai ler uma página deste repositório, que seja esta.**

---

## Por que esta página existe

**Quase ninguém reprova em Cálculo 1 por não entender limite, derivada ou integral.** Reprova-se por errar a álgebra no meio da questão.

O enunciado pede o limite; você monta corretamente; e aí precisa fatorar $x^3-8$, racionalizar um denominador ou simplificar uma fração de frações — e a conta trava. A ideia de Cálculo estava certa; o ensino médio é que cobrou a conta.

Esta página é a lista completa dessas ferramentas. **Não é matéria nova**, e por isso nenhum professor vai revisá-la em aula. Ela é pré-requisito silencioso de tudo.

> [!TIP]
> **Como usar.** Não leia de cabo a rabo agora. Faça o [diagnóstico de 10 minutos](README.md#o-diagnóstico-de-10-minutos) e leia **as seções em que você errou**. Depois, volte aqui toda vez que travar numa conta no meio de um exercício.

---

## 1. Produtos notáveis e fatoração

### Os que você usa toda semana

$$(a+b)^2 = a^2+2ab+b^2 \qquad (a-b)^2 = a^2-2ab+b^2$$

$$a^2-b^2 = (a+b)(a-b)$$

$$(a+b)^3 = a^3+3a^2b+3ab^2+b^3 \qquad (a-b)^3 = a^3-3a^2b+3ab^2-b^3$$

$$a^3-b^3 = (a-b)\big(a^2+ab+b^2\big) \qquad a^3+b^3 = (a+b)\big(a^2-ab+b^2\big)$$

> ⚠️ **$(a+b)^2 \neq a^2+b^2$.** O termo $2ab$ não é opcional. Esse é, com folga, o erro de álgebra mais frequente em provas de Cálculo — e ele aparece disfarçado em $\left(\sqrt{x}+1\right)^2$, em $(f+g)^2$, em tudo.

### Fatoração de trinômio

$$ax^2+bx+c = a(x-r_1)(x-r_2) \qquad\text{onde } r_{1,2} = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

**Atalho (soma e produto):** se $x^2+bx+c$ tem raízes inteiras, elas somam $-b$ e multiplicam $c$.

$$x^2-5x+6: \quad \text{somam } 5,\ \text{multiplicam } 6 \ \Longrightarrow \ 2 \text{ e } 3 \ \Longrightarrow \ (x-2)(x-3)$$

### Fator comum e agrupamento

$$x^3+2x^2-3x-6 = x^2(x+2)-3(x+2) = \big(x^2-3\big)(x+2)$$

> [!IMPORTANT]
> **Por que fatorar é a habilidade central de limites.** Em $\lim_{x\to2}\frac{x^2-4}{x-2}$, a substituição dá $\frac00$. O caminho é **fatorar e cancelar**:
>
> $$\frac{x^2-4}{x-2} = \frac{(x-2)(x+2)}{x-2} = x+2 \ \longrightarrow \ 4$$
>
> Toda a seção [2.1](../02-limites-e-continuidade/2.1-conceito-e-nocao-intuitiva-de-limite.md) depende disso.

---

## 2. Frações algébricas

### Somar

$$\frac{a}{b}+\frac{c}{d} = \frac{ad+bc}{bd}$$

$$\frac{1}{x}+\frac{1}{x+1} = \frac{(x+1)+x}{x(x+1)} = \frac{2x+1}{x^2+x}$$

### Dividir fração por fração

**Multiplique pelo inverso:**

$$\frac{a/b}{c/d} = \frac{a}{b}\cdot\frac{d}{c} = \frac{ad}{bc}$$

### A fração de frações do quociente de Newton

Esta aparece **em toda questão de derivada pela definição**:

$$\frac{\frac{1}{x+h}-\frac1x}{h}$$

**Passo 1 — some as frações de cima:**

$$\frac{1}{x+h}-\frac1x = \frac{x-(x+h)}{x(x+h)} = \frac{-h}{x(x+h)}$$

**Passo 2 — divida pelo $h$ (ou seja, multiplique por $\frac1h$):**

$$\frac{-h}{x(x+h)}\cdot\frac1h = \frac{-1}{x(x+h)}$$

> 💡 **O $h$ cancelou** — e é exatamente isso que precisa acontecer para o limite $h\to0$ existir. Em toda derivada pela definição, o trabalho algébrico é **fazer o $h$ do denominador sumir**.

### O que NÃO se pode cancelar

$$\frac{x+2}{x} \ \neq\ 2 \qquad\qquad \frac{x^2+1}{x^2} \ \neq\ 1$$

> ⚠️ **Só se cancela FATOR, nunca PARCELA.** Em $\frac{x(x+2)}{x}$ o $x$ cancela, porque multiplica. Em $\frac{x+2}{x}$ não cancela, porque soma. Na dúvida, teste com $x=1$: $\frac{1+2}{1}=3$, e não $2$.

---

## 3. Potências e radicais

| Regra | |
| --- | --- |
| $a^{m}\cdot a^{n} = a^{m+n}$ | multiplicou, **soma** expoente |
| $\dfrac{a^{m}}{a^{n}} = a^{m-n}$ | dividiu, **subtrai** |
| $\big(a^{m}\big)^{n} = a^{mn}$ | potência de potência, **multiplica** |
| $a^{-n} = \dfrac{1}{a^{n}}$ | expoente negativo **inverte** |
| $a^{0} = 1$ &nbsp;($a\neq0$) | |
| $a^{1/n} = \sqrt[n]{a}$ | **raiz é potência fracionária** |
| $a^{m/n} = \sqrt[n]{a^{m}}$ | |

> [!IMPORTANT]
> **A linha mais importante da tabela é $\sqrt[n]{a} = a^{1/n}$.** A regra da potência ($x^n \to nx^{n-1}$) **só** se aplica a potências — então, antes de derivar ou integrar qualquer raiz, reescreva-a como expoente fracionário.
>
> $$\sqrt{x} = x^{1/2} \qquad \frac{1}{\sqrt{x}} = x^{-1/2} \qquad \sqrt[3]{x^2} = x^{2/3} \qquad \frac{1}{x^2\sqrt x} = x^{-5/2}$$
>
> Quem não faz isso automaticamente perde tempo em **toda** questão das Unidades 3 e 5.

### Racionalização

Multiplique pelo **conjugado** (o mesmo binômio com o sinal trocado):

$$\frac{1}{\sqrt{x+1}-1} = \frac{1}{\sqrt{x+1}-1}\cdot\frac{\sqrt{x+1}+1}{\sqrt{x+1}+1} = \frac{\sqrt{x+1}+1}{(x+1)-1} = \frac{\sqrt{x+1}+1}{x}$$

> 💡 **Por que funciona:** $\big(\sqrt{A}-B\big)\big(\sqrt{A}+B\big) = A-B^2$, e a raiz some. É o produto notável $a^2-b^2$ a serviço do cancelamento.
>
> **Em limites, às vezes é preciso racionalizar o NUMERADOR** — o objetivo não é "tirar a raiz de baixo", é **fazer aparecer um fator que cancele**:
>
> $$\lim_{x\to0}\frac{\sqrt{x+4}-2}{x} = \lim_{x\to0}\frac{(x+4)-4}{x\left(\sqrt{x+4}+2\right)} = \lim_{x\to0}\frac{1}{\sqrt{x+4}+2} = \frac14$$

### O erro clássico das raízes

$$\sqrt{a+b} \ \neq\ \sqrt a + \sqrt b$$

**Teste:** $\sqrt{9+16} = \sqrt{25} = 5$, mas $\sqrt9+\sqrt{16} = 3+4 = 7$.

E, para raiz quadrada:

$$\sqrt{x^2} = \lvert x\rvert, \quad\text{não } x$$

---

## 4. Valor absoluto

$$
\lvert x\rvert = \begin{cases}
x & \text{se } x\geqslant0 \\
-x & \text{se } x<0
\end{cases}
$$

**Geometricamente:** $\lvert x\rvert$ é a **distância de $x$ até zero**, e $\lvert x-a\rvert$ é a distância de $x$ até $a$.

| Equação / inequação | Equivale a |
| --- | --- |
| $\lvert x\rvert = k$ &nbsp;($k>0$) | $x=k$ **ou** $x=-k$ |
| $\lvert x\rvert < k$ | $-k < x < k$ |
| $\lvert x\rvert > k$ | $x<-k$ **ou** $x>k$ |
| $\lvert x-a\rvert < \delta$ | $a-\delta < x < a+\delta$ |

> 💡 **A última linha é a definição formal de limite em notação de distância.** "$\lvert x-a\rvert<\delta$" lê-se "$x$ está a menos de $\delta$ de $a$" — e é assim que a Unidade 2 formaliza "$x$ se aproxima de $a$".

---

## 5. Inequações

### A regra que todo mundo esquece

> [!CAUTION]
> **Multiplicar ou dividir por número NEGATIVO inverte a desigualdade.**
>
> $$-2x < 6 \ \Longrightarrow \ x > -3 \qquad\text{(e não } x<-3\text{)}$$

### Inequação com fração: o quadro de sinais

**Nunca multiplique cruzado** numa inequação com variável no denominador — você não sabe o sinal dele.

**Resolva** $\dfrac{x-1}{x+2}\geqslant 0$:

**Passo 1 — ache os pontos de divisão.** Numerador zera em $x=1$; denominador zera em $x=-2$ (e ali a expressão **não existe**).

**Passo 2 — monte o quadro:**

| | $x<-2$ | $-2<x<1$ | $x>1$ |
| --- | :---: | :---: | :---: |
| $x-1$ | $-$ | $-$ | $+$ |
| $x+2$ | $-$ | $+$ | $+$ |
| **quociente** | $+$ | $-$ | $+$ |

**Passo 3 — leia a resposta.** Queremos $\geqslant0$:

$$S = (-\infty,\thinspace -2)\ \cup\ [1,\thinspace +\infty)$$

> ⚠️ **Note os colchetes:** $x=1$ **entra** (ali a fração vale zero, e queríamos $\geqslant$), mas $x=-2$ **nunca** entra — ali a expressão não existe. Essa distinção vale ponto.

> 💡 **O quadro de sinais reaparece o curso inteiro:** em domínio de função (Unidade 1), em sinal de $f'$ (Unidade 4), em concavidade (4.4). Aprender a montá-lo bem agora rende o semestre todo.

---

## 6. Exponencial e logaritmo

### Exponencial

$$a^{x}\cdot a^{y} = a^{x+y} \qquad \frac{a^{x}}{a^{y}} = a^{x-y} \qquad \big(a^{x}\big)^{y} = a^{xy} \qquad a^{0}=1$$

**O número $e \approx 2{,}71828$** é a base natural. $e^x$ é a única função que é a própria derivada — por isso ela domina o Cálculo.

### Logaritmo

$$\log_a b = c \iff a^{c} = b$$

| Propriedade | |
| --- | --- |
| $\ln(xy) = \ln x + \ln y$ | produto vira **soma** |
| $\ln\dfrac{x}{y} = \ln x - \ln y$ | quociente vira **diferença** |
| $\ln\big(x^{n}\big) = n\ln x$ | expoente **desce** |
| $\ln 1 = 0$ &nbsp;·&nbsp; $\ln e = 1$ | |
| $e^{\ln x} = x$ &nbsp;·&nbsp; $\ln\big(e^{x}\big) = x$ | são inversas |
| $\log_a b = \dfrac{\ln b}{\ln a}$ | mudança de base |

> ⚠️ **As três não-propriedades:**
>
> $$\ln(x+y) \neq \ln x + \ln y \qquad \ln(xy) \neq \ln x\cdot\ln y \qquad \frac{\ln x}{\ln y} \neq \ln\frac{x}{y}$$
>
> O logaritmo transforma **produto** em soma, não soma em nada.

> 💡 **A terceira linha da tabela é a chave da derivação logarítmica** (seção [3.3](../03-derivadas/3.3-regra-da-cadeia-e-derivada-da-funcao-inversa.md)) e de todo limite da forma $1^{\infty}$ ([4.3](../04-aplicacoes-das-derivadas/4.3-regra-de-lhospital.md)). Fazer o expoente descer é o movimento que transforma um problema impossível num fácil.

### Domínio: a restrição que derruba gente

**$\ln x$ só existe para $x>0$.** Ao resolver uma equação logarítmica, **toda solução precisa ser verificada**:

$$\ln x + \ln(x-3) = \ln 4 \ \Longrightarrow \ \ln\big[x(x-3)\big] = \ln 4 \ \Longrightarrow \ x^2-3x-4 = 0$$

$$\Longrightarrow \ (x-4)(x+1) = 0 \ \Longrightarrow \ x=4 \ \text{ ou } \ x=-1$$

**Verificando:** $x=-1$ daria $\ln(-1)$, que **não existe**. A única solução é $x=4$.

---

## 7. Trigonometria

### O essencial

| | |
| --- | --- |
| **Radianos** | $180° = \pi$ rad. Em Cálculo, **sempre** radianos |
| **Pitagórica** | $\mathrm{sen}^2\thinspace x + \cos^2 x = 1$ |
| **Definições** | $\mathrm{tg} = \frac{\mathrm{sen}}{\cos}$, $\mathrm{sec} = \frac{1}{\cos}$, $\mathrm{cossec} = \frac{1}{\mathrm{sen}}$, $\mathrm{cotg} = \frac{\cos}{\mathrm{sen}}$ |
| **Paridade** | seno é **ímpar**, cosseno é **par** |
| **Período** | $2\pi$ para seno e cosseno; $\pi$ para tangente |

### Valores notáveis

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathrm{sen}\thinspace x$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}{2}$ | $\dfrac{\sqrt3}{2}$ | $1$ |
| $\cos x$ | $1$ | $\dfrac{\sqrt3}{2}$ | $\dfrac{\sqrt2}{2}$ | $\dfrac12$ | $0$ |

> 💡 **O truque:** o seno é $\frac{\sqrt0}{2},\frac{\sqrt1}{2},\frac{\sqrt2}{2},\frac{\sqrt3}{2},\frac{\sqrt4}{2}$ — conte $0,1,2,3,4$ sob a raiz. O cosseno é a mesma lista **ao contrário**.

### Fora do primeiro quadrante

Use a redução ao primeiro quadrante e o sinal do quadrante:

$$\cos\frac{2\pi}{3} = \cos\left(\pi - \frac{\pi}{3}\right) = -\cos\frac{\pi}{3} = -\frac12$$

| Quadrante | Positivos |
| :---: | --- |
| 1º | **todos** |
| 2º | só **seno** |
| 3º | só **tangente** |
| 4º | só **cosseno** |

> 💡 O arsenal completo — soma de arcos, arco duplo, redução de potência — está em [A3](../06-formulario/A3-identidades-trigonometricas.md). Para começar o curso, as cinco linhas acima bastam.

---

## 8. Retas e parábolas

### Reta

$$y - y_0 = m(x-x_0) \qquad m = \frac{y_2-y_1}{x_2-x_1}$$

| | |
| --- | --- |
| **paralelas** | mesma inclinação: $m_1 = m_2$ |
| **perpendiculares** | $m_1\cdot m_2 = -1$ |

> 💡 **A equação ponto-inclinação é a fórmula mais usada da Unidade 3.** A reta tangente ao gráfico em $x=a$ é $y - f(a) = f'(a)(x-a)$ — é literalmente a fórmula acima, com $m=f'(a)$. E a **normal** é a perpendicular, com inclinação $-\frac{1}{f'(a)}$.

### Parábola

$$y = ax^2+bx+c \qquad x_{\text{vértice}} = -\frac{b}{2a}$$

Concavidade **para cima** se $a>0$, **para baixo** se $a<0$.

---

## 9. Funções: o vocabulário mínimo

| Termo | Significa |
| --- | --- |
| **Domínio** | os $x$ para os quais $f(x)$ existe |
| **Imagem** | os valores que $f$ efetivamente assume |
| **Composta** | $\big(f\circ g\big)(x) = f\big(g(x)\big)$ |
| **Inversa** | $f^{-1}$ desfaz $f$ — existe só se $f$ for bijetora |

### As três restrições de domínio

Ao determinar o domínio de uma expressão, procure sempre estas três coisas:

1. **Denominador** não pode ser zero.
2. **Radical de índice par** exige radicando $\geqslant0$.
3. **Logaritmo** exige argumento $>0$.

$$f(x) = \frac{\sqrt{x-1}}{\ln(5-x)} \ \Longrightarrow \ \underbrace{x\geqslant1}_{\text{raiz}} \ \text{ e } \ \underbrace{5-x>0}_{\ln} \ \text{ e } \ \underbrace{\ln(5-x)\neq0}_{\text{denominador}}$$

$$D = [1,\thinspace 4)\cup(4,\thinspace 5)$$

(o $x=4$ sai porque $\ln(5-4) = \ln 1 = 0$ zeraria o denominador)

---

## 10. Teste final

Refaça o [diagnóstico de 10 minutos](README.md#o-diagnóstico-de-10-minutos) agora, **sem olhar as respostas**. Se acertar 7 ou 8, você está pronto para a [Unidade 1](../01-funcoes/README.md).

Se ainda errar alguma, volte à seção correspondente desta página:

| Errou a questão | Releia a seção |
| :---: | --- |
| 1 | [1 · Produtos notáveis e fatoração](#1-produtos-notáveis-e-fatoração) |
| 2 | [1 · Fatoração](#1-produtos-notáveis-e-fatoração) e [2 · Frações](#2-frações-algébricas) |
| 3 | [3 · Potências e radicais](#3-potências-e-radicais) |
| 4 | [5 · Inequações](#5-inequações) |
| 5 | [7 · Trigonometria](#7-trigonometria) |
| 6 | [6 · Exponencial e logaritmo](#6-exponencial-e-logaritmo) |
| 7 | [4 · Valor absoluto](#4-valor-absoluto) |
| 8 | [2 · Frações algébricas](#2-frações-algébricas) |

> [!IMPORTANT]
> **Dois dias gastos aqui valem duas semanas economizadas depois.** Não existe atalho: quem começa Cálculo sem fatorar com fluência vai travar na Unidade 2 e culpar o limite — quando o problema era o produto notável.

---

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [Como usar este material](como-usar-este-material.md) | [Comece aqui](README.md) · [Página inicial](../README.md) | [Plano de estudos](plano-de-estudos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
