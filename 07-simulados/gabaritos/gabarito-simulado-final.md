# ✅ Resolução comentada — Simulado Final

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado Final](../simulado-final.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

---

## 📊 Gabarito rápido

| Q. | Resposta |
| :---: | --- |
| **1** | $(1,\thinspace 2)\cup(2,\thinspace 3]$ |
| **2** | (a) $4$ · (b) $\dfrac32$ · (c) $\dfrac12$ |
| **3** | $a=3$ |
| **4** | (a) $x(2\ln x+1)$ · (b) $e^{\operatorname{sen} x}\cos x$ · (c) $\dfrac{(2x+1)^4(18x-1)}{2x\sqrt x}$ · (d) $-1$ |
| **5** | $\dfrac{8}{9\pi}$ m/min $\approx 0{,}28$ m/min |
| **6** | O ponto $(1,\thinspace 1)$, a distância $\sqrt5$ |
| **7** | (a) $\dfrac92$ · (b) $e^{6}$ |
| **8** | Raízes $1$ e $1\pm\sqrt3$; máx $(0,2)$; mín $(2,-2)$; inflexão $(1,0)$ |
| **9** | (a) $\frac25(x+1)^{5/2}-\frac23(x+1)^{3/2}$ · (b) $e^x\big(x^2-2x+2\big)$ · (c) $\dfrac14$ |
| **10** | (a) $A\to1$ · (b) $V\to\dfrac{\pi}{2}$ · (c) ambas finitas, ao contrário da trombeta |

---

## Questão 1 &nbsp;·&nbsp; *(1,0)*

Três restrições:

| De onde vem | Condição |
| --- | --- |
| radicando $\geqslant 0$ | $3-x\geqslant0 \Rightarrow x\leqslant3$ |
| argumento do $\ln$ $>0$ | $x-1>0 \Rightarrow x>1$ |
| denominador $\neq0$ | $\ln(x-1)\neq0 \Rightarrow x-1\neq1 \Rightarrow x\neq2$ |

$$D = (1,\thinspace 2)\ \cup\ (2,\thinspace 3]$$

> ⚠️ **A terceira restrição é a que derruba a questão.** Esquecer que $\ln 1 = 0$ — e que isso zeraria o denominador — custa o ponto inteiro. Sempre que houver logaritmo no denominador, o argumento não pode valer $1$.

---

## Questão 2 &nbsp;·&nbsp; *(1,0)*

**(a)** Substituindo dá $\frac00$. **Fatore e cancele:**

$$\frac{x^2-4}{x^2-3x+2} = \frac{(x-2)(x+2)}{(x-2)(x-1)} = \frac{x+2}{x-1} \ \longrightarrow \ \frac{4}{1} = 4$$

**(b)** A forma é $\infty-\infty$. **Racionalize** multiplicando pelo conjugado:

$$\sqrt{x^2+3x}-x = \frac{\big(x^2+3x\big)-x^2}{\sqrt{x^2+3x}+x} = \frac{3x}{\sqrt{x^2+3x}+x}$$

Dividindo numerador e denominador por $x$ (positivo, pois $x\to+\infty$):

$$= \frac{3}{\sqrt{1+\frac3x}+1} \ \longrightarrow \ \frac{3}{1+1} = \frac32$$

**(c)** É o limite notável:

$$\lim_{x\to0}\frac{1-\cos x}{x^2} = \frac12$$

(Quem não lembrar: L&#39;Hôspital duas vezes dá $\lim\frac{\operatorname{sen} x}{2x} = \frac12$.)

> ⚠️ **Em (b), não dá para "distribuir o limite".** Escrever $\lim\sqrt{x^2+3x} - \lim x = \infty-\infty$ não é conclusão — é a indeterminação. A álgebra precisa vir **antes** do limite.

---

## Questão 3 &nbsp;·&nbsp; *(0,5)*

A continuidade em $x=0$ exige $a = \displaystyle\lim_{x\to0}f(x)$:

$$\lim_{x\to0}\frac{\operatorname{sen}(3x)}{x} = \lim_{x\to0} 3\cdot\frac{\operatorname{sen}(3x)}{3x} = 3\cdot 1 = 3$$

$$\boxed{\ a = 3\ }$$

> ⚠️ **A resposta não é $1$.** O limite fundamental exige que o argumento do seno e o denominador sejam **a mesma** expressão. Aqui são $3x$ e $x$, e o ajuste produz o fator $3$.

---

## Questão 4 &nbsp;·&nbsp; *(1,5)*

**(a)** Regra do **produto**:

$$f'(x) = 2x\ln x + x^2\cdot\frac1x = 2x\ln x + x = x\big(2\ln x+1\big)$$

**(b)** Regra da **cadeia**:

$$g'(x) = e^{\operatorname{sen} x}\cdot\cos x$$

**(c)** Reescreva como produto de potências — fica mais simples que o quociente:

$$h(x) = (2x+1)^{5}x^{-1/2}$$

$$h'(x) = 5(2x+1)^4\cdot 2\cdot x^{-1/2} + (2x+1)^5\cdot\left(-\frac12\right)x^{-3/2}$$

**Fatorando** $\dfrac{(2x+1)^4 x^{-3/2}}{2}$:

$$h'(x) = \frac{(2x+1)^4}{2x^{3/2}}\Big[20x - (2x+1)\Big] = \frac{(2x+1)^4(18x-1)}{2x\sqrt{x}}$$

**(d)** Confirmando que o ponto pertence à curva: $27+27 = 54$ e $6(3)(3) = 54$ ✔

Derivando **implicitamente** (produto à direita, cadeia à esquerda):

$$3x^2 + 3y^2 y' = 6y + 6x y'$$

$$y'\big(3y^2-6x\big) = 6y-3x^2 \ \Longrightarrow \ y' = \frac{6y-3x^2}{3y^2-6x} = \frac{2y-x^2}{y^2-2x}$$

Em $(3,3)$:

$$y' = \frac{6-9}{9-6} = \frac{-3}{3} = -1$$

> 💡 **A tangente ao fólio de Descartes em $(3,3)$ tem inclinação $-1$** — ou seja, é perpendicular à bissetriz $y=x$. Faz sentido: o ponto $(3,3)$ está sobre a bissetriz, e a curva é **simétrica** em relação a ela (trocar $x$ por $y$ na equação devolve a mesma equação).

---

## Questão 5 &nbsp;·&nbsp; *(1,0)*

**A relação geométrica.** Num cone invertido, o raio da superfície da água e a profundidade são proporcionais. Por semelhança de triângulos, com $4$ m de altura e $2$ m de raio no topo:

$$\frac{r}{h} = \frac{2}{4} = \frac12 \ \Longrightarrow \ r = \frac{h}{2}$$

**O volume, só em função de $h$** — é o passo decisivo:

$$V = \frac13\pi r^2 h = \frac13\pi\left(\frac{h}{2}\right)^2 h = \frac{\pi h^3}{12}$$

**Derivando em relação a $t$:**

$$\frac{dV}{dt} = \frac{\pi}{12}\cdot 3h^2\cdot\frac{dh}{dt} = \frac{\pi h^2}{4}\cdot\frac{dh}{dt}$$

**Substituindo os dados do instante** ($\frac{dV}{dt}=2$ e $h=3$):

$$2 = \frac{\pi\cdot 9}{4}\cdot\frac{dh}{dt} \ \Longrightarrow \ \frac{dh}{dt} = \frac{8}{9\pi} \approx 0{,}28 \text{ m/min}$$

> [!TIP]
> **Eliminar o $r$ antes de derivar é o que resolve a questão.** Mantendo $V = \frac13\pi r^2h$ com **duas** variáveis, a derivação produz um termo em $\frac{dr}{dt}$ que não foi dado — e o problema trava. A semelhança de triângulos existe justamente para reduzir tudo a uma variável.

---

## Questão 6 &nbsp;·&nbsp; *(1,0)*

**A montagem.** Um ponto genérico da parábola é $\big(x,\thinspace x^2\big)$. A distância até $(3,0)$ é

$$d(x) = \sqrt{(x-3)^2 + \big(x^2\big)^2}$$

**Minimize o QUADRADO da distância**, não a distância:

$$S(x) = (x-3)^2 + x^4 = x^4 + x^2 - 6x + 9$$

> 💡 **Por que isso é legítimo:** a raiz quadrada é **crescente**, então ela não muda onde está o mínimo — só o valor. Derivar $S$ evita carregar um radical pela conta inteira.

**Derivando:**

$$S'(x) = 4x^3+2x-6 = 2\big(2x^3+x-3\big)$$

Testando $x=1$: $2+1-3 = 0$ ✔ Logo $(x-1)$ é fator:

$$2x^3+x-3 = (x-1)\big(2x^2+2x+3\big)$$

O fator quadrático tem $\Delta = 4-24 = -20 < 0$, logo é **sempre positivo**. O sinal de $S'$ é, portanto, o sinal de $x-1$:

| | $x<1$ | $x>1$ |
| --- | :---: | :---: |
| $S'$ | $-$ | $+$ |

**Mínimo** em $x=1$, único ponto crítico ✔

**Resposta.** O ponto é $(1,\thinspace 1)$, e a distância é

$$d = \sqrt{(1-3)^2+1^2} = \sqrt{4+1} = \sqrt5$$

---

## Questão 7 &nbsp;·&nbsp; *(1,0)*

**(a)** Substituindo: $\frac00$ ✔

$$\lim_{x\to0}\frac{e^{3x}-1-3x}{x^2} \overset{\text{L'H}}{=} \lim_{x\to0}\frac{3e^{3x}-3}{2x}$$

Ainda $\frac00$. De novo:

$$\overset{\text{L'H}}{=} \lim_{x\to0}\frac{9e^{3x}}{2} = \frac92$$

**(b)** Base tende a $1$, expoente a $\infty$: indeterminação $1^{\infty}$. **Use o logaritmo.**

Seja $L$ o limite. Então:

$$\ln L = \lim_{x\to+\infty} 3x\ln\left(1+\frac2x\right) = \lim_{x\to+\infty}\frac{3\ln\left(1+\frac2x\right)}{1/x}$$

Agora é $\frac00$:

$$\ln L \overset{\text{L'H}}{=} \lim_{x\to+\infty}\frac{3\cdot\dfrac{-2/x^2}{1+\frac2x}}{-1/x^2} = \lim_{x\to+\infty}\frac{6}{1+\frac2x} = 6$$

$$L = e^{6}$$

> ⚠️ **Não esqueça de exponenciar no fim.** Quem para em $\ln L = 6$ e responde "$6$" perde a questão. O logaritmo foi um **instrumento**; a resposta pedida era $L$.

---

## Questão 8 &nbsp;·&nbsp; *(1,0)*

**1. Domínio.** $D = \mathbb{R}$ (polinômio).

**2. Interseções.** Testando $x=1$: $1-3+2 = 0$ ✔ Logo $(x-1)$ é fator:

$$x^3-3x^2+2 = (x-1)\big(x^2-2x-2\big)$$

As outras raízes vêm de $x^2-2x-2=0$:

$$x = \frac{2\pm\sqrt{4+8}}{2} = 1\pm\sqrt3 \approx -0{,}73 \ \text{ e } \ 2{,}73$$

Com o eixo $y$: $f(0)=2$.

**3. Simetria.** Nenhuma.

**4. Assíntotas.** Nenhuma. No infinito: $f\to+\infty$ quando $x\to+\infty$, e $f\to-\infty$ quando $x\to-\infty$.

**5. Crescimento.** $f'(x) = 3x^2-6x = 3x(x-2)$:

| | $x<0$ | $0<x<2$ | $x>2$ |
| --- | :---: | :---: | :---: |
| $f'$ | $+$ | $-$ | $+$ |

**Máximo local** em $(0,\thinspace 2)$ e **mínimo local** em $(2,\thinspace -2)$.

**6. Concavidade.** $f''(x) = 6x-6 = 6(x-1)$: **baixo** para $x<1$, **cima** para $x>1$.

**Inflexão** em $\big(1,\thinspace 0\big)$.

**7. Tabela-resumo.**

| Intervalo | $f'$ | $f''$ | Comportamento |
| :---: | :---: | :---: | --- |
| $(-\infty,0)$ | $+$ | $-$ | sobe, concavidade para baixo |
| $(0,1)$ | $-$ | $-$ | desce, concavidade para baixo |
| $(1,2)$ | $-$ | $+$ | desce, concavidade para cima |
| $(2,+\infty)$ | $+$ | $+$ | sobe, concavidade para cima |

**8. O desenho.** Vem de $-\infty$, corta o eixo em $1-\sqrt3$, sobe até o pico $(0,2)$, desce atravessando a inflexão $(1,0)$ — que é **também uma raiz** —, atinge o vale $(2,-2)$ e sobe cortando o eixo em $1+\sqrt3$.

> 💡 **A inflexão coincidir com uma raiz é curioso, e não é acaso.** Todo cúbico $ax^3+bx^2+cx+d$ é **simétrico** em relação ao seu ponto de inflexão. Aqui, esse centro de simetria é $(1,0)$ — e as outras duas raízes, $1\pm\sqrt3$, estão à mesma distância dele dos dois lados ✔
>
> Essa simetria é uma conferência grátis do esboço: se o seu desenho não é simétrico em relação à inflexão, há erro em algum lugar.

---

## Questão 9 &nbsp;·&nbsp; *(1,5)*

**(a) Substituição**, do tipo que **reescreve o polinômio** em $u$:

$$u = x+1 \ \Longrightarrow \ x = u-1, \quad dx = du$$

$$\int x\sqrt{x+1}\thinspace dx = \int (u-1)u^{1/2}du = \int\left(u^{3/2}-u^{1/2}\right)du$$

$$= \frac25 u^{5/2} - \frac23 u^{3/2} + C = \frac25 (x+1)^{5/2} - \frac23 (x+1)^{3/2} + C$$

**(b) Integração por partes, duas vezes.** Com $u=x^2$ e $dv = e^x dx$:

$$\int x^2 e^x dx = x^2 e^x - 2\int x e^x dx$$

E $\int xe^x dx = (x-1)e^x$ (partes de novo, ou de memória):

$$= x^2 e^x - 2(x-1)e^x + C = e^x\big(x^2-2x+2\big)+C$$

**Conferindo:** $\big[e^x(x^2-2x+2)\big]' = e^x(x^2-2x+2)+e^x(2x-2) = x^2 e^x$ ✔

**(c) Substituição em integral definida**, com os limites convertidos:

$$u = \operatorname{sen} x \ \Longrightarrow \ du = \cos x\thinspace dx$$

| $x$ | $u=\operatorname{sen} x$ |
| :---: | :---: |
| $0$ | $0$ |
| $\frac{\pi}{2}$ | $1$ |

$$\int_0^{\pi/2}\operatorname{sen}^3 x\cos x\thinspace dx = \int_0^1 u^3 du = \left[\frac{u^4}{4}\right]_0^1 = \frac14$$

---

## Questão 10 &nbsp;·&nbsp; *(1,5)* — síntese

**(a) A área.**

$$A(b) = \int_0^b e^{-x}dx = \Big[-e^{-x}\Big]_0^b = 1-e^{-b}$$

$$\lim_{b\to\infty}A(b) = \lim_{b\to\infty}\big(1-e^{-b}\big) = 1$$

**A área é FINITA**, e vale $1$.

**(b) O volume**, pelo método do disco com raio $e^{-x}$:

$$V(b) = \pi\int_0^b\left(e^{-x}\right)^2 dx = \pi\int_0^b e^{-2x}dx = \pi\left[-\frac{e^{-2x}}{2}\right]_0^b = \frac{\pi}{2}\left(1-e^{-2b}\right)$$

$$\lim_{b\to\infty}V(b) = \frac{\pi}{2}$$

**O volume também é FINITO.**

> ⚠️ **Note que $\big(e^{-x}\big)^2 = e^{-2x}$, e não $e^{-x^2}$.** O primeiro integra em duas linhas; o segundo não tem primitiva elementar. Confundi-los transforma uma questão de prova numa integral impossível.

**(c) A comparação.**

| | $y = e^{-x}$ em $[0,\infty)$ | $y = \dfrac1x$ em $[1,\infty)$ |
| --- | :---: | :---: |
| **Área** | $1$ — **finita** | $\displaystyle\int_1^\infty\frac{dx}{x}$ — **infinita** |
| **Volume** | $\dfrac{\pi}{2}$ — **finito** | $\pi$ — **finito** |

A curva $y=\frac1x$ gera a **trombeta de Gabriel**: volume finito com área infinita. Já a exponencial não produz paradoxo nenhum — **as duas medidas são finitas**.

**Por que a diferença.** O método do disco **eleva o raio ao quadrado**, o que, no caso das potências, **dobra o expoente**: a área integra $x^{-1}$ (que diverge, pois $p=1$) e o volume integra $x^{-2}$ (que converge, pois $p=2>1$). A função $\frac1x$ está **exatamente na fronteira** $p=1$, e o quadrado a empurra para o lado convergente — daí o paradoxo.

A exponencial, por outro lado, decai **mais rápido que qualquer potência** (é a hierarquia do infinito da Unidade 4). Ela já está muito além da fronteira antes de qualquer quadrado, e por isso **nada muda**: área e volume convergem igualmente.

> 💡 **Esta questão fecha o curso porque usa as cinco unidades.**
>
> Limite ao infinito (U2), hierarquia do infinito (U4), integral definida (U5), método do disco (U5) e o teste da $p$-integral (U5) — e o que amarra tudo é uma única pergunta: **com que velocidade a função decai?**
>
> É a melhor síntese possível do que o Cálculo oferece. A intuição geométrica, treinada em figuras limitadas, não consegue decidir se um sólido infinitamente longo tem volume finito. O Cálculo decide — e mostra que a resposta depende de um expoente.

---

## 📋 Diagnóstico

| Acertos | O que fazer |
| :---: | --- |
| 9 ou 10 | Você domina a disciplina. Revise o [formulário](../../06-formulario/README.md) na véspera e vá. |
| 7 ou 8 | Muito bom. Refaça só as questões erradas. |
| 5 ou 6 | Identifique as **unidades** das questões erradas e refaça as revisões correspondentes. |
| 0 a 4 | Refaça os três simulados anteriores, um por dia, e estude as lacunas que eles apontarem. |

**Mapa questão → unidade**, para encontrar a lacuna:

| Errou | Volte para |
| :---: | --- |
| 1 | [Unidade 1](../../01-funcoes/README.md) — domínio |
| 2, 3 | [Unidade 2](../../02-limites-e-continuidade/README.md) — limites e continuidade |
| 4, 5 | [Unidade 3](../../03-derivadas/README.md) — regras e taxas |
| 6, 7, 8 | [Unidade 4](../../04-aplicacoes-das-derivadas/README.md) — otimização, L&#39;Hôspital, esboço |
| 9, 10 | [Unidade 5](../../05-integrais/README.md) — técnicas e aplicações |

---

> [!IMPORTANT]
> **Se você chegou até aqui, acertando ou errando, você já fez mais do que a maioria.** Fazer um simulado completo de três horas, com honestidade e sem consulta, é o treino que mais se aproxima da prova — e é exatamente o que quase ninguém faz.
>
> Boa prova. 🍀

---

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado Final](../simulado-final.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
