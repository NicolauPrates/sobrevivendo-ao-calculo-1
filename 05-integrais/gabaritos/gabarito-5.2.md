# ✅ Gabarito — Lista 5.2

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 5.2](../exercicios/lista-5.2-propostos.md) · [Teoria 5.2](../5.2-tecnicas-de-integracao.md)

> 💡 **Sua resposta ficou diferente da minha?** Derive-a. Se devolver o integrando, está **certa** — veja os [três testes](README.md#minha-resposta-está-diferente-da-sua--está-errada) no índice dos gabaritos. Nesta lista isso acontece com frequência, principalmente nos itens trigonométricos.

---

# ✅ Parte 1 — Respostas finais

*(O $+\thinspace C$ está subentendido em todas.)*

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $\dfrac{(3x+5)^8}{24}$ |
| 1 (b) | $\dfrac{\big(x^2-4\big)^6}{6}$ |
| 1 (c) | $\sqrt{x^2+9}$ |
| 1 (d) | $-\dfrac{\cos 5x}{5}$ |
| 2 (a) | $\dfrac13\ln\lvert 3x-1\rvert$ |
| 2 (b) | $\ln\lvert x^2+3x+1\rvert$ |
| 2 (c) | $\dfrac{(\ln x)^2}{2}$ |
| 2 (d) | $\ln\lvert\mathrm{sen}\thinspace x\rvert$ |
| 3 (a) | $-\dfrac{\cos^4 x}{4}$ |
| 3 (b) | $-\dfrac{e^{-x^2}}{2}$ |
| 3 (c) | $2e^{\sqrt{x}}$ |
| 4 (a) | $-x\cos x + \mathrm{sen}\thinspace x$ |
| 4 (b) | $\dfrac{e^{3x}}{9}(3x-1)$ |
| 4 (c) | $\dfrac{x^2}{2}\ln x - \dfrac{x^2}{4}$ |
| 5 (a) | $e^{x}\big(x^2-2x+2\big)$ |
| 5 (b) | $x^2\mathrm{sen}\thinspace x + 2x\cos x - 2\mathrm{sen}\thinspace x$ |
| 6 (a) | $x\mathrm{arctg}\thinspace x - \dfrac12\ln\big(1+x^2\big)$ |
| 6 (b) | $x\mathrm{arcsen}\thinspace x + \sqrt{1-x^2}$ |
| 7 (a) | $\dfrac{1/2}{x-1} - \dfrac{1/2}{x+1}$ |
| 7 (b) | $\dfrac{11/5}{x-3} + \dfrac{14/5}{x+2}$ |
| 7 (c) | $\dfrac2x - \dfrac{2}{x+1} - \dfrac{2}{(x+1)^2}$ |
| 8 (a) | $\dfrac12\ln\left\lvert\dfrac{x-1}{x+1}\right\rvert$ |
| 8 (b) | $\dfrac{11}{5}\ln\lvert x-3\rvert + \dfrac{14}{5}\ln\lvert x+2\rvert$ |
| 9 | (a) $x=5\mathrm{sen}\thinspace\theta$ · (b) $x=2\mathrm{tg}\thinspace\theta$ · (c) $x=4\mathrm{sec}\thinspace\theta$ |
| 10 | $\mathrm{arcsen}\thinspace\dfrac{x}{2}$ pelos dois caminhos |

### Bloco B · Consolidação

| Ex. | Técnica | Resposta |
| :---: | :---: | --- |
| 11 | substituição | $\dfrac23\sqrt{x^3+1}$ |
| 12 | substituição | $\dfrac25 (x-1)^{5/2} + \dfrac23 (x-1)^{3/2}$ |
| 13 | partes (circular) | $\dfrac{e^x}{2}\big(\cos x + \mathrm{sen}\thinspace x\big)$ |
| 14 | frações parciais | $-\dfrac25\ln\lvert x+3\rvert + \dfrac75\ln\lvert x-2\rvert$ |
| 15 | divisão + tabela | $\dfrac{x^3}{3}+x^2+4x+8\ln\lvert x-2\rvert$ |
| 16 | identidade | $\dfrac{x}{2}-\dfrac{\mathrm{sen}\thinspace 2x}{4}$ |
| 17 | identidade + substituição | $-\cos x + \dfrac{\cos^3 x}{3}$ |
| 18 | completar quadrado | $\dfrac12\mathrm{arctg}\thinspace\dfrac{x+3}{2}$ |
| 19 | trigonométrica | $-\dfrac{\sqrt{4-x^2}}{x} - \mathrm{arcsen}\thinspace\dfrac{x}{2}$ |
| 20 | propriedade + partes | $2x\ln\lvert x\rvert - 2x$ |
| 21 | frações parciais | $-\ln\lvert x\rvert + 2\ln\big(x^2+1\big) + 2\mathrm{arctg}\thinspace x$ |
| 22 | substituição + partes | $\dfrac{\big(x^2-1\big)e^{x^2}}{2}$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 23 | Demonstração (o truque cria $u = \mathrm{sec}\thinspace x + \mathrm{tg}\thinspace x$) |
| 24 | Demonstração; $\displaystyle\int\mathrm{sen}^4\thinspace x\thinspace dx = -\dfrac{\mathrm{sen}^3\thinspace x\cos x}{4} + \dfrac{3x}{8} - \dfrac{3\mathrm{sen}\thinspace 2x}{16}$ |
| 25 | $x - \ln\big(1+e^{x}\big)$ |
| 26 | $\dfrac{\mathrm{sen}^2\thinspace x}{2}$, $-\dfrac{\cos^2 x}{2}$ e $-\dfrac{\cos 2x}{4}$ — **as três corretas** |
| 27 | $\mathrm{arcsec}\lvert x\rvert$ |

---

# 📖 Parte 2 — Resoluções completas

## Bloco A · Fixação

### 1.

**(a)** $u = 3x+5$, $du = 3\thinspace dx$, logo $dx = \dfrac{du}{3}$:

$$\int (3x+5)^7 dx = \frac13\int u^7 du = \frac13\cdot\frac{u^8}{8} = \frac{(3x+5)^8}{24}+C$$

**(b)** $u = x^2-4$, $du = 2x\thinspace dx$ — e o $2x$ já está lá:

$$\int 2x\big(x^2-4\big)^5 dx = \int u^5 du = \frac{u^6}{6} = \frac{\big(x^2-4\big)^6}{6}+C$$

**(c)** $u = x^2+9$, $du = 2x\thinspace dx$, logo $x\thinspace dx = \dfrac{du}{2}$:

$$\int\frac{x\thinspace dx}{\sqrt{x^2+9}} = \frac12\int u^{-1/2}du = \frac12\cdot 2u^{1/2} = \sqrt{x^2+9}+C$$

**(d)** $u = 5x$, $du = 5\thinspace dx$:

$$\int \mathrm{sen}\thinspace 5x\thinspace dx = \frac15\int\mathrm{sen}\thinspace u\thinspace du = -\frac{\cos 5x}{5}+C$$

> 💡 **O padrão de (a) e (d) é o mais simples de todos:** quando o argumento é $ax+b$, a substituição só introduz o fator $\frac1a$. Com prática, você escreve direto — mas escreva o $u$ explicitamente enquanto não estiver automático.

---

### 2.

**(a)** $u=3x-1$: $\displaystyle\int\frac{dx}{3x-1} = \frac13\int\frac{du}{u} = \frac13\ln\lvert 3x-1\rvert + C$

**(b)** Olhe o numerador: $(x^2+3x+1)' = 2x+3$ — **exatamente** o numerador. É o padrão $\frac{g'}{g}$:

$$\int\frac{2x+3}{x^2+3x+1}dx = \ln\lvert x^2+3x+1\rvert + C$$

**(c)** $u = \ln x$, $du = \dfrac{dx}{x}$:

$$\int\frac{\ln x}{x}dx = \int u\thinspace du = \frac{u^2}{2} = \frac{(\ln x)^2}{2}+C$$

**(d)** $\mathrm{cotg}\thinspace x = \dfrac{\cos x}{\mathrm{sen}\thinspace x}$, e o numerador é a derivada do denominador:

$$\int\mathrm{cotg}\thinspace x\thinspace dx = \ln\lvert\mathrm{sen}\thinspace x\rvert + C$$

> 💡 **Compare com $\int\mathrm{tg}\thinspace x\thinspace dx = -\ln\lvert\cos x\rvert$ do Exercício Resolvido 2.** A cotangente **não** ganha sinal negativo, porque $(\mathrm{sen}\thinspace x)' = +\cos x$. As duas integrais parecem simétricas e não são — e esse sinal é exatamente o que a prova cobra.

---

### 3.

**(a)** $u = \cos x$, $du = -\mathrm{sen}\thinspace x\thinspace dx$:

$$\int\cos^3 x\mathrm{sen}\thinspace x\thinspace dx = \int u^3(-du) = -\frac{u^4}{4} = -\frac{\cos^4 x}{4}+C$$

**(b)** $u = -x^2$, $du = -2x\thinspace dx$, logo $x\thinspace dx = -\dfrac{du}{2}$:

$$\int x\thinspace e^{-x^2}dx = -\frac12\int e^u du = -\frac{e^{-x^2}}{2}+C$$

**(c)** $u = \sqrt{x} = x^{1/2}$, $du = \dfrac{dx}{2\sqrt{x}}$, logo $\dfrac{dx}{\sqrt{x}} = 2\thinspace du$:

$$\int\frac{e^{\sqrt{x}}}{\sqrt{x}}dx = \int e^u\cdot 2\thinspace du = 2e^{\sqrt{x}}+C$$

> 💡 **Em (c), o $\frac{1}{\sqrt x}$ não é obstáculo — é a pista.** Ele é (duas vezes) a derivada de $\sqrt x$, que é justamente o que está no expoente. Sempre que uma expressão aparecer **no expoente** e sua derivada estiver multiplicando, a substituição está pronta.

---

### 4.

**(a)** LIATE: **A**lgébrica antes de **T**rigonométrica, logo $u=x$.

$$u = x,\quad dv = \mathrm{sen}\thinspace x\thinspace dx \ \Longrightarrow \ du = dx,\quad v = -\cos x$$

$$\int x\mathrm{sen}\thinspace x\thinspace dx = -x\cos x - \int(-\cos x)dx = -x\cos x + \mathrm{sen}\thinspace x + C$$

**(b)** $u = x$, $dv = e^{3x}dx$, logo $du = dx$ e $v = \dfrac{e^{3x}}{3}$:

$$\int x\thinspace e^{3x}dx = \frac{x\thinspace e^{3x}}{3} - \frac13\int e^{3x}dx = \frac{x\thinspace e^{3x}}{3} - \frac{e^{3x}}{9} + C = \frac{e^{3x}}{9}\big(3x-1\big)+C$$

**(c)** Atenção: aqui LIATE manda escolher a **L**ogarítmica, não a algébrica.

$$u = \ln x,\quad dv = x\thinspace dx \ \Longrightarrow \ du = \frac{dx}{x},\quad v = \frac{x^2}{2}$$

$$\int x\ln x\thinspace dx = \frac{x^2}{2}\ln x - \int\frac{x^2}{2}\cdot\frac1x dx = \frac{x^2}{2}\ln x - \frac12\int x\thinspace dx = \frac{x^2}{2}\ln x - \frac{x^2}{4}+C$$

> ⚠️ **Em (c), escolher $u=x$ seria desastroso:** $dv = \ln x\thinspace dx$ exigiria integrar $\ln x$ — que é mais difícil que a integral original. **O logaritmo quase sempre vai no $u$**, porque derivá-lo o faz desaparecer.

---

### 5.

**(a)** $u = x^2$, $dv = e^x dx$, logo $du = 2x\thinspace dx$ e $v = e^x$:

$$\int x^2 e^x dx = x^2 e^x - 2\int x\thinspace e^x dx$$

A integral que sobrou já foi resolvida no [Exercício Resolvido 3](../5.2-tecnicas-de-integracao.md): vale $(x-1)e^x$. Logo:

$$\int x^2 e^x dx = x^2 e^x - 2(x-1)e^x + C = e^x\big(x^2-2x+2\big)+C$$

**Conferindo:** $\big[e^x(x^2-2x+2)\big]' = e^x(x^2-2x+2) + e^x(2x-2) = e^x\cdot x^2$ ✔

**(b)** $u = x^2$, $dv = \cos x\thinspace dx$, logo $du = 2x\thinspace dx$ e $v = \mathrm{sen}\thinspace x$:

$$\int x^2\cos x\thinspace dx = x^2\mathrm{sen}\thinspace x - 2\int x\mathrm{sen}\thinspace x\thinspace dx$$

E $\int x\mathrm{sen}\thinspace x\thinspace dx = -x\cos x + \mathrm{sen}\thinspace x$ (exercício 4a):

$$= x^2\mathrm{sen}\thinspace x - 2\big(-x\cos x + \mathrm{sen}\thinspace x\big) + C = x^2\mathrm{sen}\thinspace x + 2x\cos x - 2\mathrm{sen}\thinspace x + C$$

> 💡 **O padrão geral:** cada aplicação de partes **baixa o grau do polinômio em uma unidade**. Com $x^2$, são duas aplicações; com $x^3$, três. É previsível — e é por isso que $\int x^{10}e^x dx$ é possível, mas ninguém pede em prova.

---

### 6.

**(a)** O truque $dv = dx$:

$$u = \mathrm{arctg}\thinspace x,\quad dv = dx \ \Longrightarrow \ du = \frac{dx}{1+x^2},\quad v = x$$

$$\int\mathrm{arctg}\thinspace x\thinspace dx = x\mathrm{arctg}\thinspace x - \int\frac{x}{1+x^2}dx$$

A integral que sobrou é do padrão $\frac{g'}{g}$ (a menos do fator $2$), com $w = 1+x^2$:

$$\int\frac{x}{1+x^2}dx = \frac12\ln\big(1+x^2\big)$$

$$\int\mathrm{arctg}\thinspace x\thinspace dx = x\mathrm{arctg}\thinspace x - \frac12\ln\big(1+x^2\big) + C$$

> 💡 O módulo foi dispensado porque $1+x^2 > 0$ sempre.

**(b)** Mesmo truque:

$$u = \mathrm{arcsen}\thinspace x,\quad dv = dx \ \Longrightarrow \ du = \frac{dx}{\sqrt{1-x^2}},\quad v = x$$

$$\int\mathrm{arcsen}\thinspace x\thinspace dx = x\mathrm{arcsen}\thinspace x - \int\frac{x\thinspace dx}{\sqrt{1-x^2}}$$

Com $w = 1-x^2$ e $x\thinspace dx = -\dfrac{dw}{2}$:

$$\int\frac{x\thinspace dx}{\sqrt{1-x^2}} = -\frac12\int w^{-1/2}dw = -\sqrt{1-x^2}$$

$$\int\mathrm{arcsen}\thinspace x\thinspace dx = x\mathrm{arcsen}\thinspace x + \sqrt{1-x^2} + C$$

**Conferindo:**

$$\mathrm{arcsen}\thinspace x + \frac{x}{\sqrt{1-x^2}} + \frac{-2x}{2\sqrt{1-x^2}} = \mathrm{arcsen}\thinspace x \ \checkmark$$

---

### 7.

**(a)** $x^2-1 = (x-1)(x+1)$, dois lineares distintos:

$$\frac{1}{(x-1)(x+1)} = \frac{A}{x-1}+\frac{B}{x+1} \ \Longrightarrow \ 1 = A(x+1)+B(x-1)$$

- $x=1$: $\ 1 = 2A \Rightarrow A = \frac12$
- $x=-1$: $\ 1 = -2B \Rightarrow B = -\frac12$

$$\frac{1}{x^2-1} = \frac{1/2}{x-1} - \frac{1/2}{x+1}$$

**(b)** $x^2-x-6 = (x-3)(x+2)$:

$$5x-4 = A(x+2)+B(x-3)$$

- $x=3$: $\ 11 = 5A \Rightarrow A = \frac{11}{5}$
- $x=-2$: $\ -14 = -5B \Rightarrow B = \frac{14}{5}$

$$\frac{5x-4}{x^2-x-6} = \frac{11/5}{x-3} + \frac{14/5}{x+2}$$

**(c)** Aqui há um fator **repetido**, $(x+1)^2$, que gera **duas** parcelas:

$$\frac{2}{x(x+1)^2} = \frac{A}{x} + \frac{B}{x+1} + \frac{D}{(x+1)^2}$$

$$2 = A(x+1)^2 + Bx(x+1) + Dx$$

- $x=0$: $\ 2 = A \Rightarrow A = 2$
- $x=-1$: $\ 2 = -D \Rightarrow D = -2$
- Para achar $B$, compare o **coeficiente de $x^2$**: à esquerda é $0$, à direita é $A+B$. Logo $B = -A = -2$.

$$\frac{2}{x(x+1)^2} = \frac2x - \frac{2}{x+1} - \frac{2}{(x+1)^2}$$

**Conferindo em $x=1$:** à esquerda, $\frac{2}{1\cdot4} = \frac12$; à direita, $2 - 1 - \frac12 = \frac12$ ✔

> ⚠️ **Fator repetido exige todas as potências.** Escrever só $\frac{D}{(x+1)^2}$ e esquecer o $\frac{B}{x+1}$ torna o sistema impossível. A regra é: $(x-a)^n$ gera **$n$** parcelas, com denominadores $(x-a), (x-a)^2, \ldots, (x-a)^n$.
>
> E note que, com fator repetido, as raízes não bastam — é preciso comparar coeficientes para fechar.

---

### 8.

**(a)** Usando a decomposição de 7(a):

$$\int\frac{dx}{x^2-1} = \frac12\int\frac{dx}{x-1} - \frac12\int\frac{dx}{x+1} = \frac12\ln\lvert x-1\rvert - \frac12\ln\lvert x+1\rvert + C$$

Juntando pela propriedade do logaritmo:

$$= \frac12\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C$$

**(b)** Usando 7(b):

$$\int\frac{5x-4}{x^2-x-6}dx = \frac{11}{5}\ln\lvert x-3\rvert + \frac{14}{5}\ln\lvert x+2\rvert + C$$

---

### 9.

| | Radical | Forma | Substituição |
| :---: | :---: | :---: | --- |
| **(a)** | $\sqrt{25-x^2}$ | $\sqrt{a^2-x^2}$ com $a=5$ | $x = 5\mathrm{sen}\thinspace\theta$ |
| **(b)** | $\sqrt{x^2+4}$ | $\sqrt{a^2+x^2}$ com $a=2$ | $x = 2\mathrm{tg}\thinspace\theta$ |
| **(c)** | $\sqrt{x^2-16}$ | $\sqrt{x^2-a^2}$ com $a=4$ | $x = 4\mathrm{sec}\thinspace\theta$ |

> 💡 **Como não confundir as três.** Pergunte qual identidade pitagórica **transforma a expressão num quadrado perfeito**:
> - $a^2-x^2$ precisa de $1-\mathrm{sen}^2 = \cos^2$ → **seno**;
> - $a^2+x^2$ precisa de $1+\mathrm{tg}^2 = \mathrm{sec}^2$ → **tangente**;
> - $x^2-a^2$ precisa de $\mathrm{sec}^2-1 = \mathrm{tg}^2$ → **secante**.
>
> Os sinais dizem tudo: **menos primeiro** é seno, **mais** é tangente, **menos depois** é secante.

---

### 10.

**Pela tabela.** A forma geral é $\displaystyle\int\frac{dx}{\sqrt{a^2-x^2}} = \mathrm{arcsen}\thinspace\frac{x}{a}+C$, com $a=2$:

$$\int\frac{dx}{\sqrt{4-x^2}} = \mathrm{arcsen}\thinspace\frac{x}{2}+C$$

**Por substituição trigonométrica.** Com $x = 2\mathrm{sen}\thinspace\theta$ e $dx = 2\cos\theta\thinspace d\theta$:

$$\sqrt{4-x^2} = \sqrt{4-4\mathrm{sen}^2\thinspace\theta} = 2\cos\theta$$

$$\int\frac{2\cos\theta\thinspace d\theta}{2\cos\theta} = \int d\theta = \theta + C$$

Voltando: de $x = 2\mathrm{sen}\thinspace\theta$ vem $\mathrm{sen}\thinspace\theta = \frac{x}{2}$, logo $\theta = \mathrm{arcsen}\thinspace\frac{x}{2}$.

$$\int\frac{dx}{\sqrt{4-x^2}} = \mathrm{arcsen}\thinspace\frac{x}{2}+C \ \checkmark$$

> 💡 **O segundo caminho é a demonstração do primeiro.** A linha da tabela não caiu do céu: ela é o resultado desta substituição, feita uma vez e guardada. Vale a pena ter visto de onde vem — tabela entendida se recupera quando a memória falha.

---

## Bloco B · Consolidação

### 11.

**Técnica:** substituição. A função de dentro é $x^3+1$, e sua derivada $3x^2$ está (a menos do $3$) no numerador.

$$u = x^3+1 \ \Longrightarrow \ du = 3x^2dx \ \Longrightarrow \ x^2 dx = \frac{du}{3}$$

$$\int\frac{x^2 dx}{\sqrt{x^3+1}} = \frac13\int u^{-1/2}du = \frac13\cdot 2\sqrt{u} = \frac23\sqrt{x^3+1}+C$$

---

### 12.

**Técnica:** substituição — mas de um tipo diferente. Não há "função e derivada": o que incomoda é a raiz, e a substituição serve só para **limpá-la**.

$$u = x-1 \ \Longrightarrow \ x = u+1, \quad dx = du$$

O $x$ que sobra fora da raiz é reescrito em $u$ — é por isso que a substituição funciona:

$$\int x\sqrt{x-1}\thinspace dx = \int (u+1)\sqrt{u}\thinspace du = \int\left(u^{3/2}+u^{1/2}\right)du$$

$$= \frac25 u^{5/2} + \frac23 u^{3/2} + C = \frac25 (x-1)^{5/2} + \frac23 (x-1)^{3/2} + C$$

> 💡 **Guarde esta variante.** Quando houver $\sqrt{x-a}$ multiplicando um polinômio, substitua $u = x-a$ e **reescreva o polinômio em $u$**. Diferente do caso clássico, aqui a substituição não desfaz uma cadeia — ela só troca o radical por uma potência.

---

### 13.

**Técnica:** por partes, duas vezes, com retorno circular. É a gêmea do [Exercício Resolvido 4](../5.2-tecnicas-de-integracao.md).

Chamando $J = \displaystyle\int e^x\cos x\thinspace dx$ e $I = \displaystyle\int e^x\mathrm{sen}\thinspace x\thinspace dx$, a conta do ER4 mostrou que

$$J = e^x\cos x + I \qquad\text{e}\qquad I = \frac{e^x}{2}\big(\mathrm{sen}\thinspace x-\cos x\big)$$

Substituindo:

$$J = e^x\cos x + \frac{e^x}{2}\mathrm{sen}\thinspace x - \frac{e^x}{2}\cos x = \frac{e^x}{2}\big(\cos x + \mathrm{sen}\thinspace x\big)+C$$

**Conferindo:**

$$\left[\frac{e^x}{2}(\cos x+\mathrm{sen}\thinspace x)\right]' = \frac{e^x}{2}(\cos x+\mathrm{sen}\thinspace x) + \frac{e^x}{2}(-\mathrm{sen}\thinspace x+\cos x) = e^x\cos x \ \checkmark$$

---

### 14.

**Técnica:** frações parciais. Grau $1 < 2$ ✔ e $x^2+x-6 = (x+3)(x-2)$.

$$x+5 = A(x-2)+B(x+3)$$

- $x=2$: $\ 7 = 5B \Rightarrow B = \frac75$
- $x=-3$: $\ 2 = -5A \Rightarrow A = -\frac25$

$$\int\frac{x+5}{x^2+x-6}dx = -\frac25\ln\lvert x+3\rvert + \frac75\ln\lvert x-2\rvert + C$$

---

### 15.

**Técnica:** o grau do numerador ($3$) é **maior** que o do denominador ($1$) — então, antes de qualquer coisa, **divida**.

$$x^3 = (x-2)\big(x^2+2x+4\big) + 8 \ \Longrightarrow \ \frac{x^3}{x-2} = x^2+2x+4+\frac{8}{x-2}$$

Agora tudo é imediato:

$$\int\frac{x^3}{x-2}dx = \frac{x^3}{3}+x^2+4x+8\ln\lvert x-2\rvert + C$$

> ⚠️ **Tentar frações parciais direto aqui não funciona.** A decomposição $\frac{A}{x-2}$ nunca reproduz um numerador de grau $3$. A divisão não é opcional: é pré-requisito.

---

### 16.

**Técnica:** identidade. A potência par do seno pede o **arco duplo**:

$$\mathrm{sen}^2\thinspace x = \frac{1-\cos 2x}{2}$$

$$\int\mathrm{sen}^2\thinspace x\thinspace dx = \frac12\int\big(1-\cos 2x\big)dx = \frac12\left(x - \frac{\mathrm{sen}\thinspace 2x}{2}\right) = \frac{x}{2}-\frac{\mathrm{sen}\thinspace 2x}{4}+C$$

---

### 17.

**Técnica:** potência **ímpar** — separa-se um fator e usa-se a identidade no resto.

$$\int\mathrm{sen}^3\thinspace x\thinspace dx = \int\mathrm{sen}^2\thinspace x\cdot\mathrm{sen}\thinspace x\thinspace dx = \int\big(1-\cos^2 x\big)\mathrm{sen}\thinspace x\thinspace dx$$

Agora é substituição, com $u = \cos x$ e $du = -\mathrm{sen}\thinspace x\thinspace dx$:

$$= \int\big(1-u^2\big)(-du) = -u + \frac{u^3}{3} + C = -\cos x + \frac{\cos^3 x}{3} + C$$

> 💡 **A regra de ouro das potências trigonométricas:**
> - expoente **ímpar** → separe um fator e substitua (exercício 17);
> - expoente **par** → use o arco duplo (exercício 16).
>
> Essas duas linhas resolvem a grande maioria das integrais de $\mathrm{sen}^n$ e $\cos^n$ que aparecem em Cálculo 1.

---

### 18.

**Técnica:** o denominador é quadrático **irredutível** ($\Delta = 36-52 < 0$), então não há frações parciais. O caminho é **completar o quadrado**:

$$x^2+6x+13 = \big(x^2+6x+9\big)+4 = (x+3)^2+4$$

Com $u = x+3$ (e $du = dx$), a integral vira a forma da arco-tangente:

$$\int\frac{dx}{(x+3)^2+4} = \int\frac{du}{u^2+4} = \frac12\mathrm{arctg}\thinspace\frac{u}{2} + C = \frac12\mathrm{arctg}\thinspace\frac{x+3}{2}+C$$

> 💡 **Completar o quadrado é o que faz a arco-tangente aparecer.** Sempre que o denominador for quadrático sem raízes reais, esse é o movimento: $(x+p)^2+q^2$, e então $\int\frac{du}{u^2+q^2} = \frac1q\mathrm{arctg}\thinspace\frac uq$.

---

### 19.

**Técnica:** substituição trigonométrica, radical $\sqrt{4-x^2}$ com $a=2$.

$$x = 2\mathrm{sen}\thinspace\theta,\quad dx = 2\cos\theta\thinspace d\theta,\quad \sqrt{4-x^2} = 2\cos\theta,\quad x^2 = 4\mathrm{sen}^2\thinspace\theta$$

$$\int\frac{\sqrt{4-x^2}}{x^2}dx = \int\frac{2\cos\theta\cdot 2\cos\theta\thinspace d\theta}{4\mathrm{sen}^2\thinspace\theta} = \int\frac{\cos^2\theta}{\mathrm{sen}^2\thinspace\theta}d\theta = \int\mathrm{cotg}^2\thinspace\theta\thinspace d\theta$$

E $\mathrm{cotg}^2 = \mathrm{cossec}^2-1$:

$$= \int\big(\mathrm{cossec}^2\thinspace\theta - 1\big)d\theta = -\mathrm{cotg}\thinspace\theta - \theta + C$$

**Voltando ao triângulo** (hipotenusa $2$, oposto $x$, adjacente $\sqrt{4-x^2}$):

$$\mathrm{cotg}\thinspace\theta = \frac{\sqrt{4-x^2}}{x} \qquad \theta = \mathrm{arcsen}\thinspace\frac{x}{2}$$

$$\int\frac{\sqrt{4-x^2}}{x^2}dx = -\frac{\sqrt{4-x^2}}{x} - \mathrm{arcsen}\thinspace\frac{x}{2} + C$$

---

### 20.

**Técnica:** propriedade do logaritmo **antes** de integrar.

$$\ln\big(x^2\big) = 2\ln\lvert x\rvert$$

$$\int\ln\big(x^2\big)dx = 2\int\ln\lvert x\rvert\thinspace dx = 2\big(x\ln\lvert x\rvert - x\big)+C = 2x\ln\lvert x\rvert - 2x + C$$

> ⚠️ **O módulo é obrigatório aqui.** Como $x^2>0$ para todo $x\neq0$, o integrando $\ln(x^2)$ existe também para $x$ negativo. Escrever $2\ln x$ perderia metade do domínio — é o mesmo cuidado de $\int\frac{dx}{x}$.

---

### 21.

**Técnica:** frações parciais com fator quadrático **irredutível**.

$$x^3+x = x\big(x^2+1\big)$$

Como $x^2+1$ não tem raiz real, a parcela correspondente tem numerador **linear**:

$$\frac{3x^2+2x-1}{x\big(x^2+1\big)} = \frac{A}{x} + \frac{Bx+D}{x^2+1}$$

Multiplicando por $x(x^2+1)$:

$$3x^2+2x-1 = A\big(x^2+1\big) + (Bx+D)x = (A+B)x^2 + Dx + A$$

**Comparando coeficientes:**

- termo constante: $A = -1$
- coeficiente de $x$: $D = 2$
- coeficiente de $x^2$: $A+B = 3 \Rightarrow B = 4$

$$\int\frac{3x^2+2x-1}{x^3+x}dx = \int\left(-\frac1x + \frac{4x+2}{x^2+1}\right)dx$$

A segunda parcela se separa em duas de tabela:

$$\int\frac{4x}{x^2+1}dx = 2\ln\big(x^2+1\big) \qquad \int\frac{2}{x^2+1}dx = 2\mathrm{arctg}\thinspace x$$

$$\int\frac{3x^2+2x-1}{x^3+x}dx = -\ln\lvert x\rvert + 2\ln\big(x^2+1\big) + 2\mathrm{arctg}\thinspace x + C$$

> ⚠️ **Fator irredutível pede numerador $Ax+B$, não só $A$.** E, como ele não tem raiz real, não dá para usar o atalho de substituir raízes: aqui é **comparar coeficientes** mesmo. Note também que a parcela $\frac{4x+2}{x^2+1}$ gera **duas** funções diferentes — logaritmo (da parte $4x$) e arco-tangente (da parte $2$). Separá-las é parte do exercício.

---

### 22.

**Técnica:** substituição **e depois** partes.

$$u = x^2 \ \Longrightarrow \ du = 2x\thinspace dx \ \Longrightarrow \ x\thinspace dx = \frac{du}{2}$$

Reescrevendo $x^3 dx = x^2\cdot x\thinspace dx = u\cdot\dfrac{du}{2}$:

$$\int x^3 e^{x^2}dx = \frac12\int u\thinspace e^u du$$

E $\int u e^u du = (u-1)e^u$ (Exercício Resolvido 3a):

$$= \frac12 (u-1)e^u + C = \frac{\big(x^2-1\big)e^{x^2}}{2}+C$$

**Conferindo:**

$$\left[\frac{(x^2-1)e^{x^2}}{2}\right]' = \frac{2x\thinspace e^{x^2} + (x^2-1)e^{x^2}\cdot 2x}{2} = x\thinspace e^{x^2}\big[1+x^2-1\big] = x^3 e^{x^2} \ \checkmark$$

> 💡 **Técnicas se combinam.** Uma integral pode exigir substituição **seguida de** partes, ou identidade seguida de substituição. Se a primeira técnica não terminou o serviço mas **melhorou** o integrando, está no caminho certo — continue.

---

## Bloco C · Desafio

### 23. A integral da secante

O truque é multiplicar e dividir pelo mesmo fator $\mathrm{sec}\thinspace x + \mathrm{tg}\thinspace x$:

$$\int\mathrm{sec}\thinspace x\thinspace dx = \int \mathrm{sec}\thinspace x\cdot\frac{\mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x}{\mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x}dx = \int\frac{\mathrm{sec}^2\thinspace x + \mathrm{sec}\thinspace x\mathrm{tg}\thinspace x}{\mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x}dx$$

Agora olhe o denominador e derive-o:

$$\big(\mathrm{sec}\thinspace x + \mathrm{tg}\thinspace x\big)' = \mathrm{sec}\thinspace x\mathrm{tg}\thinspace x + \mathrm{sec}^2\thinspace x$$

que é **exatamente** o numerador. Com $u = \mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x$, é o padrão $\frac{g'}{g}$:

$$\int\mathrm{sec}\thinspace x\thinspace dx = \int\frac{du}{u} = \ln\lvert u\rvert + C = \ln\lvert\mathrm{sec}\thinspace x+\mathrm{tg}\thinspace x\rvert + C \quad\blacksquare$$

> 💡 **De onde veio a ideia de multiplicar por isso?** De lugar nenhum — é um truque histórico, descoberto no século XVII e guardado desde então. Ninguém o redescobre em prova.
>
> **Essa é a exceção que confirma a regra:** quase toda integral de Cálculo 1 cede a uma das quatro técnicas aplicadas com método. Umas poucas, como esta, são **resultados a memorizar**. $\int\mathrm{sec}\thinspace x\thinspace dx$ é a principal delas — e aparece sempre que você calcular comprimento de arco em [5.4](../5.4-aplicacoes-da-integral-definida.md).

---

### 24. Fórmula de redução

**Dedução.** Separe um fator de seno e aplique partes:

$$I_n = \int\mathrm{sen}^n\thinspace x\thinspace dx = \int\underbrace{\mathrm{sen}^{n-1}\thinspace x}_{u}\cdot\underbrace{\mathrm{sen}\thinspace x\thinspace dx}_{dv}$$

$$du = (n-1)\mathrm{sen}^{n-2}\thinspace x\cos x\thinspace dx \qquad v = -\cos x$$

$$I_n = -\mathrm{sen}^{n-1}\thinspace x\cos x + (n-1)\int\mathrm{sen}^{n-2}\thinspace x\cos^2 x\thinspace dx$$

Usando $\cos^2 x = 1-\mathrm{sen}^2\thinspace x$:

$$I_n = -\mathrm{sen}^{n-1}\thinspace x\cos x + (n-1)\int\mathrm{sen}^{n-2}\thinspace x\thinspace dx - (n-1)\int\mathrm{sen}^{n}\thinspace x\thinspace dx$$

$$I_n = -\mathrm{sen}^{n-1}\thinspace x\cos x + (n-1)I_{n-2} - (n-1)I_n$$

**A integral original voltou** — é o mesmo fenômeno do Exercício Resolvido 4. Isolando:

$$n\thinspace I_n = -\mathrm{sen}^{n-1}\thinspace x\cos x + (n-1)I_{n-2}$$

$$I_n = -\frac{\mathrm{sen}^{n-1}\thinspace x\cos x}{n} + \frac{n-1}{n}I_{n-2} \quad\blacksquare$$

**Aplicando para $n=4$:**

$$I_4 = -\frac{\mathrm{sen}^3\thinspace x\cos x}{4} + \frac34 I_2$$

E $I_2 = \dfrac{x}{2}-\dfrac{\mathrm{sen}\thinspace 2x}{4}$ (exercício 16):

$$\int\mathrm{sen}^4\thinspace x\thinspace dx = -\frac{\mathrm{sen}^3\thinspace x\cos x}{4} + \frac{3x}{8} - \frac{3\mathrm{sen}\thinspace 2x}{16} + C$$

> 💡 **Fórmulas de redução são a resposta "industrial" às potências altas.** Em vez de resolver $\int\mathrm{sen}^6$ do zero, você aplica a fórmula três vezes e cai em $\int dx$. É assim que tabelas de integrais são construídas — e é por isso que elas têm entradas com $n$ genérico.

---

### 25.

Multiplique numerador e denominador por $e^{-x}$:

$$\int\frac{dx}{1+e^x} = \int\frac{e^{-x}}{e^{-x}+1}dx$$

Com $u = e^{-x}+1$ e $du = -e^{-x}dx$:

$$= \int\frac{-du}{u} = -\ln\lvert u\rvert + C = -\ln\big(e^{-x}+1\big)+C$$

**Forma mais usual.** Como $e^{-x}+1 = \dfrac{1+e^x}{e^x}$:

$$-\ln\frac{1+e^x}{e^x} = -\ln\big(1+e^x\big) + \ln e^x = x - \ln\big(1+e^x\big)$$

$$\int\frac{dx}{1+e^x} = x-\ln\big(1+e^x\big)+C$$

> 💡 **Um segundo caminho, mais direto.** Some e subtraia $e^x$ no numerador:
>
> $$\frac{1}{1+e^x} = \frac{\big(1+e^x\big)-e^x}{1+e^x} = 1 - \frac{e^x}{1+e^x}$$
>
> A segunda parcela é $\frac{g'}{g}$, e sai na hora. É o mesmo truque do exercício 15 da Lista 5.1 — **somar e subtrair** continua sendo um dos movimentos mais úteis da unidade.

---

### 26. Três respostas, todas certas

**(a)** $u = \mathrm{sen}\thinspace x$, $du = \cos x\thinspace dx$:

$$\int\mathrm{sen}\thinspace x\cos x\thinspace dx = \int u\thinspace du = \frac{\mathrm{sen}^2\thinspace x}{2}+C$$

**(b)** $u = \cos x$, $du = -\mathrm{sen}\thinspace x\thinspace dx$:

$$\int\mathrm{sen}\thinspace x\cos x\thinspace dx = -\int u\thinspace du = -\frac{\cos^2 x}{2}+C$$

**(c)** Com $\mathrm{sen}\thinspace x\cos x = \dfrac{\mathrm{sen}\thinspace 2x}{2}$:

$$\int\frac{\mathrm{sen}\thinspace 2x}{2}dx = \frac12\cdot\left(-\frac{\cos 2x}{2}\right) = -\frac{\cos 2x}{4}+C$$

**Por que as três estão corretas.** Basta mostrar que diferem por **constantes**.

**(a) menos (b):**

$$\frac{\mathrm{sen}^2\thinspace x}{2} - \left(-\frac{\cos^2 x}{2}\right) = \frac{\mathrm{sen}^2\thinspace x+\cos^2 x}{2} = \frac12$$

**(a) menos (c):** usando $\cos 2x = 1-2\mathrm{sen}^2\thinspace x$,

$$-\frac{\cos 2x}{4} = -\frac{1-2\mathrm{sen}^2\thinspace x}{4} = -\frac14 + \frac{\mathrm{sen}^2\thinspace x}{2}$$

logo a diferença para (a) é $\frac14$.

As três diferenças são constantes, então as três expressões pertencem à **mesma família de primitivas** $\blacksquare$

> 💡 **Esta é a questão mais importante da lista** — não pela conta, que é trivial, mas pelo que ela estabelece.
>
> Em integral, **"diferente do gabarito" não significa "errado"**. A integral indefinida é uma família, e qualquer membro dela, escrito de qualquer forma algébrica, é resposta correta. Antes de riscar a sua resolução, derive-a: se devolve o integrando, está certa, e nenhum gabarito pode dizer o contrário.

---

### 27.

**Técnica:** substituição trigonométrica, radical $\sqrt{x^2-1}$ com $a=1$.

$$x = \mathrm{sec}\thinspace\theta \ \Longrightarrow \ dx = \mathrm{sec}\thinspace\theta\mathrm{tg}\thinspace\theta\thinspace d\theta, \qquad \sqrt{x^2-1} = \sqrt{\mathrm{sec}^2\thinspace\theta-1} = \mathrm{tg}\thinspace\theta$$

$$\int\frac{dx}{x\sqrt{x^2-1}} = \int\frac{\mathrm{sec}\thinspace\theta\mathrm{tg}\thinspace\theta\thinspace d\theta}{\mathrm{sec}\thinspace\theta\cdot\mathrm{tg}\thinspace\theta} = \int d\theta = \theta + C$$

Tudo se cancelou. Voltando, de $x = \mathrm{sec}\thinspace\theta$ vem $\theta = \mathrm{arcsec}\thinspace x$:

$$\int\frac{dx}{x\sqrt{x^2-1}} = \mathrm{arcsec}\lvert x\rvert + C$$

> 💡 **O módulo cobre os dois ramos.** A substituição $x=\mathrm{sec}\thinspace\theta$ foi feita supondo $x>1$; para $x<-1$ o cálculo é análogo e o resultado se escreve com $\lvert x\rvert$, cobrindo os dois pedaços do domínio.
>
> **E repare no cancelamento total.** Quando uma substituição trigonométrica reduz a integral a $\int d\theta$, isso é sinal de que você acabou de redescobrir uma linha da tabela de derivadas — neste caso, $\big(\mathrm{arcsec}\thinspace x\big)' = \frac{1}{\lvert x\rvert\sqrt{x^2-1}}$, da [seção 3.4](../../03-derivadas/3.4-derivadas-das-funcoes-trigonometricas-inversas.md).

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 5.2](../exercicios/lista-5.2-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [5.2 · Teoria](../5.2-tecnicas-de-integracao.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
