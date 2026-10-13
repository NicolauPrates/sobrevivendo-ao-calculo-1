# ✅ Resolução comentada — Simulado P1

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado P1](../simulado-p1-funcoes-e-limites.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

> **Como corrigir.** Vá questão por questão e pergunte-se: *"eu teria escrito isto?"* — e não *"ah, eu sabia"*. Depois, classifique cada erro pela causa (teoria / montagem / conta / tempo). A causa diz o remédio.

---

## 📊 Gabarito rápido

| Q. | Resposta |
| :---: | --- |
| **1 (a)** | $(-\infty,-2]\cup[2,3)\cup(3,+\infty)$ |
| **1 (b)** | $(-2,\thinspace 5)$ |
| **2** | $D=\mathbb{R}\setminus\lbrace-3\rbrace$, $\operatorname{Im}=\mathbb{R}\setminus\lbrace2\rbrace$, $f^{-1}(x)=\dfrac{3x+1}{2-x}$ |
| **3** | (a) $\frac65$ · (b) $\frac14$ · (c) $\frac32$ · (d) $\frac53$ |
| **4** | (a) $2$ e $3$; o limite **não** existe · (b) descontinuidade **de salto** |
| **5** | A.V. $x=\pm3$; A.H. $y=2$; cortes em $(\pm2,0)$ e $\left(0,\frac89\right)$ |
| **6** | (a) $k=4$ · (b) TVI com $f(1)=-1$ e $f(2)=7$ |

---

## Questão 1 &nbsp;·&nbsp; *(1,5)*

**(a)** $f(x) = \dfrac{\sqrt{x^2-4}}{x-3}$

Duas restrições:

| Restrição | De onde vem | Condição |
| --- | --- | --- |
| radicando $\geqslant 0$ | raiz de índice par | $x^2-4\geqslant0$ |
| denominador $\neq 0$ | fração | $x-3\neq0$ |

**Resolvendo a primeira** pelo quadro de sinais, com $x^2-4=(x-2)(x+2)$:

| | $x<-2$ | $-2<x<2$ | $x>2$ |
| --- | :---: | :---: | :---: |
| $x^2-4$ | $+$ | $-$ | $+$ |

Logo $x\leqslant-2$ ou $x\geqslant2$ (os extremos **entram**, porque a desigualdade é $\geqslant$).

**A segunda** exclui $x=3$.

$$D = (-\infty,\thinspace -2]\ \cup\ [2,\thinspace 3)\ \cup\ (3,\thinspace +\infty)$$

**(b)** $g(x) = \dfrac{\ln(x+2)}{\sqrt{5-x}}$

| Restrição | Condição |
| --- | --- |
| argumento do logaritmo $>0$ | $x+2>0 \Rightarrow x>-2$ |
| radicando $\geqslant 0$ | $5-x\geqslant0$ |
| denominador $\neq0$ | $\sqrt{5-x}\neq0 \Rightarrow x\neq5$ |

As duas últimas se combinam em $5-x>0$, ou seja, $x<5$ — **estrito**, porque a raiz está no **denominador**.

$$D = (-2,\thinspace 5)$$

> ⚠️ **Radical no denominador é desigualdade ESTRITA.** Se a raiz estivesse no numerador, $x=5$ entraria. Essa distinção de um único ponto é exatamente o tipo de detalhe que separa $1{,}5$ de $1{,}0$ na questão.

---

## Questão 2 &nbsp;·&nbsp; *(2,0)*

**(a) Domínio.** O denominador zera em $x=-3$:

$$D = \mathbb{R}\setminus\lbrace-3\rbrace$$

**Imagem.** Isole $x$ em $y=\dfrac{2x-1}{x+3}$:

$$y(x+3) = 2x-1 \ \Longrightarrow \ yx+3y = 2x-1 \ \Longrightarrow \ x(y-2) = -3y-1$$

$$x = \frac{-3y-1}{y-2} = \frac{3y+1}{2-y}$$

Essa expressão existe para todo $y$ **exceto** $y=2$. Logo

$$\operatorname{Im} = \mathbb{R}\setminus\lbrace2\rbrace$$

**(b) Injetividade.** O próprio cálculo de (a) já prova: para cada $y$ da imagem, a equação $f(x)=y$ tem **uma única** solução, dada pela fórmula acima. Logo $f$ é injetora.

> 💡 **Uma observação que vale ponto extra.** Pode-se estranhar a injetividade porque o domínio tem **dois ramos**. Mas os ramos cobrem imagens **disjuntas**: escrevendo
>
> $$f(x) - 2 = \frac{2x-1-2(x+3)}{x+3} = \frac{-7}{x+3}$$
>
> vê-se que $f(x)>2$ quando $x<-3$ e $f(x)<2$ quando $x>-3$. Como os dois ramos nunca assumem o mesmo valor, não há repetição.

**(c) A inversa.** Trocando os nomes das variáveis na fórmula de (a):

$$f^{-1}(x) = \frac{3x+1}{2-x}, \qquad D\big(f^{-1}\big) = \mathbb{R}\setminus\lbrace2\rbrace$$

**Conferindo** com $u = \dfrac{3x+1}{2-x}$:

$$f(u) = \frac{2u-1}{u+3} = \frac{\frac{6x+2}{2-x}-1}{\frac{3x+1}{2-x}+3} = \frac{\frac{6x+2-2+x}{2-x}}{\frac{3x+1+6-3x}{2-x}} = \frac{7x}{7} = x \ \checkmark$$

> 💡 **O domínio da inversa é a imagem da original** — sempre. Por isso o item (a) não era enfeite: ele já tinha resolvido metade do item (c).

---

## Questão 3 &nbsp;·&nbsp; *(2,0)*

**(a)** Substituindo: $\dfrac{0}{0}$ — indeterminação. **Fatore e cancele:**

$$\frac{x^2-9}{x^2-x-6} = \frac{(x-3)(x+3)}{(x-3)(x+2)} = \frac{x+3}{x+2}$$

$$\lim_{x\to3}\frac{x+3}{x+2} = \frac{6}{5}$$

**(b)** Substituindo: $\dfrac00$. **Racionalize o numerador:**

$$\frac{\sqrt{x+4}-2}{x}\cdot\frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \frac{(x+4)-4}{x\left(\sqrt{x+4}+2\right)} = \frac{x}{x\left(\sqrt{x+4}+2\right)} = \frac{1}{\sqrt{x+4}+2}$$

$$\lim_{x\to0}\frac{1}{\sqrt{x+4}+2} = \frac{1}{2+2} = \frac14$$

**(c)** Graus **iguais** ⟹ o limite é a razão dos coeficientes líderes:

$$\lim_{x\to+\infty}\frac{3x^2-x+1}{2x^2+5} = \frac32$$

(Formalmente: divida numerador e denominador por $x^2$ e os termos com $\frac1x$ somem.)

**(d)** Ajuste para a forma do limite fundamental $\dfrac{\operatorname{sen}\square}{\square}$:

$$\frac{\operatorname{sen}(5x)}{3x} = \frac{5}{3}\cdot\frac{\operatorname{sen}(5x)}{5x} \ \longrightarrow \ \frac53\cdot 1 = \frac53$$

> ⚠️ **A resposta de (d) não é $1$.** O limite fundamental exige que o **argumento do seno** e o **denominador** sejam a mesma expressão. Aqui são $5x$ e $3x$ — daí o fator $\frac53$.

---

## Questão 4 &nbsp;·&nbsp; *(1,5)*

**(a)** Cada limite lateral usa o **ramo correspondente** da definição:

$$\lim_{x\to1^{-}}f(x) = \lim_{x\to1^{-}}\big(x^2+1\big) = 2$$

$$\lim_{x\to1^{+}}f(x) = \lim_{x\to1^{+}}\big(4-x\big) = 3$$

Como $2\neq3$, os limites laterais **diferem** e

$$\lim_{x\to1}f(x) \quad\textbf{não existe}$$

**(b)** Não é contínua: a continuidade exige que o limite exista, e ele não existe.

Como os dois limites laterais **existem** (são finitos) mas são **diferentes**, trata-se de uma **descontinuidade de salto**, de amplitude $3-2 = 1$.

> ⚠️ **O valor $f(1)=3$ é uma pista falsa.** Ele coincide com o limite pela direita, o que dá a impressão de "quase contínuo". Mas a continuidade exige o limite **bilateral**, e esse não existe — o valor em $1$ nem chega a ser examinado.

---

## Questão 5 &nbsp;·&nbsp; *(2,0)*

**(a)** $x^2-9\neq0 \Rightarrow D = \mathbb{R}\setminus\lbrace-3,\thinspace 3\rbrace$

**(b) Assíntotas verticais** em $x=-3$ e $x=3$. Em $x=3$, o numerador vale $2(9)-8 = 10 > 0$:

$$\lim_{x\to3^{+}}\frac{2x^2-8}{x^2-9} = \frac{10}{0^{+}} = +\infty \qquad \lim_{x\to3^{-}} = \frac{10}{0^{-}} = -\infty$$

Em $x=-3$, o numerador também vale $10>0$, e o denominador é positivo **à esquerda** de $-3$:

$$\lim_{x\to-3^{-}} = \frac{10}{0^{+}} = +\infty \qquad \lim_{x\to-3^{+}} = \frac{10}{0^{-}} = -\infty$$

**(c) Assíntota horizontal.** Graus iguais, razão dos líderes:

$$\lim_{x\to\pm\infty}\frac{2x^2-8}{x^2-9} = 2 \ \Longrightarrow \ y=2$$

**(d) Interseções.**

- Com o eixo $x$: $2x^2-8=0 \Rightarrow x=\pm2$ ⟹ pontos $(-2,0)$ e $(2,0)$.
- Com o eixo $y$: $f(0) = \dfrac{-8}{-9} = \dfrac89$.

**O esboço.** A função é **par** ($f(-x)=f(x)$), logo simétrica em relação ao eixo $y$ — o que já economiza metade do desenho.

São **três ramos**:

| Ramo | Comportamento |
| --- | --- |
| $x<-3$ | vem de $y=2$ **por cima** (quando $x\to-\infty$) e sobe para $+\infty$ junto à assíntota |
| $-3<x<3$ | vem de $-\infty$, sobe cruzando $(-2,0)$, atinge o topo em $\left(0,\frac89\right)$, desce cruzando $(2,0)$ e mergulha para $-\infty$ |
| $x>3$ | desce de $+\infty$ e se achata contra $y=2$ **por cima** |

> 💡 **Confira a coerência do desenho:** o ramo central tem de ficar **abaixo** de $y=2$ (ele passa por $\frac89 < 2$) e os externos **acima** dela. De fato,
>
> $$f(x)-2 = \frac{2x^2-8-2x^2+18}{x^2-9} = \frac{10}{x^2-9}$$
>
> que é **positivo** quando $\lvert x\rvert>3$ e **negativo** quando $\lvert x\rvert<3$ ✔ Essa conta de uma linha confirma o esboço inteiro.

---

## Questão 6 &nbsp;·&nbsp; *(1,0)*

**(a)** Para $x\neq2$:

$$\frac{x^2-4}{x-2} = \frac{(x-2)(x+2)}{x-2} = x+2$$

$$\lim_{x\to2}f(x) = \lim_{x\to2}(x+2) = 4$$

A continuidade em $x=2$ exige $f(2) = \lim_{x\to2}f(x)$, ou seja,

$$\boxed{\ k = 4\ }$$

> 💡 **Esta é a descontinuidade removível em estado puro:** o limite existe, e basta **definir** $f(2)$ como esse valor para consertar a função.

**(b)** Seja $f(x) = x^3+x-3$.

**Hipótese:** $f$ é polinômio, logo **contínua** em $[1,2]$ ✔

**Troca de sinal:**

$$f(1) = 1+1-3 = -1 < 0 \qquad f(2) = 8+2-3 = 7 > 0$$

Pelo **Teorema do Valor Intermediário**, como $f$ é contínua em $[1,2]$ e $0$ está entre $f(1)=-1$ e $f(2)=7$, existe $c\in(1,2)$ com $f(c)=0$ $\blacksquare$

> ⚠️ **Enunciar a continuidade não é formalidade.** O TVI **exige** essa hipótese, e uma demonstração que só calcula $f(1)$ e $f(2)$ sem mencioná-la está incompleta. É um ponto que a banca cobra com frequência.

---

## 📋 Diagnóstico

| Acertos | O que fazer |
| :---: | --- |
| 5 ou 6 | Pronto para a P1. Faça só uma revisão de fórmulas na véspera. |
| 3 ou 4 | Refaça as [revisões da U1](../../01-funcoes/exercicios/revisao-unidade-1.md) e da [U2](../../02-limites-e-continuidade/exercicios/revisao-unidade-2.md). |
| 0 a 2 | Volte às listas das seções que falharam. Há tempo, mas não para adiar. |

**Se o erro foi de álgebra** (fatoração na Q3, quadro de sinais na Q1), o remédio não é estudar limites — é a [Revisão de Pré-Cálculo](../../00-comece-aqui/revisao-pre-calculo.md).

---

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado P1](../simulado-p1-funcoes-e-limites.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
