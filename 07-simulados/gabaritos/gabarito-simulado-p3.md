# ✅ Resolução comentada — Simulado P3

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado P3](../simulado-p3-integrais.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

> 💡 **Sua resposta ficou diferente da minha?** Derive-a. Se devolve o integrando, está **certa** — duas primitivas corretas podem diferir por uma constante e ter aparências bem distintas.

---

## 📊 Gabarito rápido

*(O $+\thinspace C$ está subentendido nas indefinidas.)*

| Q. | Resposta |
| :---: | --- |
| **1 (a)** | $x^4 - 3\ln\lvert x\rvert + \dfrac43 x^{3/2}$ |
| **1 (b)** | $\dfrac{e^{2x}}{2} + \operatorname{tg} x$ |
| **1 (c)** | $\dfrac{x^2}{2} - 2x + \ln\lvert x\rvert$ |
| **2 (a)** | $\dfrac12\ln\big(x^2+4\big)$ — substituição |
| **2 (b)** | $\dfrac{x\operatorname{sen} 2x}{2} + \dfrac{\cos 2x}{4}$ — por partes |
| **2 (c)** | $-\dfrac45\ln\lvert x+3\rvert + \dfrac95\ln\lvert x-2\rvert$ — frações parciais |
| **3** | $f(x) = 2x^3-x^2-x$ |
| **4** | (a) $\dfrac{65}{12}$ · (b) $3x^2\cos\big(x^6\big)$ · (c) $\dfrac14$ |
| **5** | (a) área $=\dfrac43$ · (b) $V = \dfrac{64\pi}{15}$ |
| **6** | (a) $\dfrac12$ · (b) **diverge** · (c) **converge** |

---

## Questão 1 &nbsp;·&nbsp; *(1,5)*

**(a)** Reescreva a raiz como potência:

$$\int\left(4x^3 - \frac3x + 2x^{1/2}\right)dx = 4\cdot\frac{x^4}{4} - 3\ln\lvert x\rvert + 2\cdot\frac{x^{3/2}}{3/2} + C$$

$$= x^4 - 3\ln\lvert x\rvert + \frac43 x^{3/2} + C$$

**(b)**

$$\int\left(e^{2x}+\operatorname{sec}^2 x\right)dx = \frac{e^{2x}}{2} + \operatorname{tg} x + C$$

> ⚠️ **O $\frac12$ de $e^{2x}$ é obrigatório.** Derivando $e^{2x}$ sai $2e^{2x}$, então integrar precisa **dividir** por $2$ para compensar. Esquecer esse fator é o erro mais frequente do item.

**(c)** **Expanda e divida termo a termo** — não existe regra para integrar quociente:

$$\frac{(x-1)^2}{x} = \frac{x^2-2x+1}{x} = x - 2 + \frac1x$$

$$\int\left(x-2+\frac1x\right)dx = \frac{x^2}{2} - 2x + \ln\lvert x\rvert + C$$

---

## Questão 2 &nbsp;·&nbsp; *(2,5)*

**(a) Técnica: substituição.** O numerador é (metade da) derivada do denominador — é o padrão $\frac{g'}{g}$:

$$u = x^2+4 \ \Longrightarrow \ du = 2x\thinspace dx \ \Longrightarrow \ x\thinspace dx = \frac{du}{2}$$

$$\int\frac{x\thinspace dx}{x^2+4} = \frac12\int\frac{du}{u} = \frac12\ln\lvert u\rvert = \frac12\ln\big(x^2+4\big) + C$$

(o módulo foi dispensado porque $x^2+4>0$ sempre)

> ⚠️ **Não confunda com $\int\frac{dx}{x^2+4}$**, que é **arco-tangente**. A diferença é o $x$ no numerador: com ele, é substituição e dá logaritmo; sem ele, é tabela e dá arco. Um único fator muda a família da resposta.

**(b) Técnica: integração por partes.** Produto de **A**lgébrica e **T**rigonométrica; por LIATE, $u$ é a algébrica:

$$u = x, \quad dv = \cos(2x)\thinspace dx \ \Longrightarrow \ du = dx, \quad v = \frac{\operatorname{sen}(2x)}{2}$$

$$\int x\cos(2x)\thinspace dx = \frac{x\operatorname{sen}(2x)}{2} - \frac12\int\operatorname{sen}(2x)\thinspace dx = \frac{x\operatorname{sen}(2x)}{2} + \frac{\cos(2x)}{4} + C$$

**Conferindo:**

$$\left[\frac{x\operatorname{sen} 2x}{2}+\frac{\cos 2x}{4}\right]' = \frac{\operatorname{sen} 2x}{2} + x\cos 2x - \frac{2\operatorname{sen} 2x}{4} = x\cos 2x \ \checkmark$$

**(c) Técnica: frações parciais.** Grau $1<2$ ✔ e $x^2+x-6 = (x+3)(x-2)$:

$$x+7 = A(x-2) + B(x+3)$$

Substituindo as **raízes**:

- $x=2$: $\ 9 = 5B \Rightarrow B = \dfrac95$
- $x=-3$: $\ 4 = -5A \Rightarrow A = -\dfrac45$

$$\int\frac{x+7}{x^2+x-6}dx = -\frac45\ln\lvert x+3\rvert + \frac95\ln\lvert x-2\rvert + C$$

---

## Questão 3 &nbsp;·&nbsp; *(1,0)*

**Primeira integração**, com a condição $f'(1)=3$:

$$f'(x) = \int(12x-2)\thinspace dx = 6x^2-2x+C_1$$

$$f'(1) = 6-2+C_1 = 3 \ \Longrightarrow \ C_1 = -1 \ \Longrightarrow \ f'(x) = 6x^2-2x-1$$

**Segunda integração**, com $f(1)=0$:

$$f(x) = \int\big(6x^2-2x-1\big)dx = 2x^3-x^2-x+C_2$$

$$f(1) = 2-1-1+C_2 = 0 \ \Longrightarrow \ C_2 = 0$$

$$\boxed{\ f(x) = 2x^3-x^2-x\ }$$

> ⚠️ **Resolva $C_1$ antes de integrar de novo.** Quem carrega o $C_1$ para a segunda integração termina com um termo $C_1x$ e um sistema de duas equações — mais trabalho e mais chance de erro. Cada condição resolve a constante **da sua etapa**.

---

## Questão 4 &nbsp;·&nbsp; *(2,0)*

**(a)**

$$\int_1^4\left(x^{1/2}+x^{-2}\right)dx = \left[\frac23 x^{3/2}-\frac1x\right]_1^4$$

$$= \left(\frac23\cdot 8 - \frac14\right) - \left(\frac23 - 1\right) = \left(\frac{16}{3}-\frac14\right) - \left(-\frac13\right)$$

$$= \frac{16}{3}-\frac14+\frac13 = \frac{17}{3}-\frac14 = \frac{68-3}{12} = \frac{65}{12}$$

> ⚠️ **Os parênteses em $F(1)$ são obrigatórios.** Aqui $F(1) = -\frac13$ é **negativo**, e subtrair um negativo **soma**. Quem escreve $\frac{16}{3}-\frac14-\frac13$ erra por $\frac23$.

**(b)** TFC parte 1 com limite superior composto, $g(x)=x^3$:

$$F'(x) = \cos\left(\big(x^3\big)^2\right)\cdot 3x^2 = 3x^2\cos\big(x^6\big)$$

**(c)** Com $u = x^2+1$ e $x\thinspace dx = \dfrac{du}{2}$:

| $x$ | $u = x^2+1$ |
| :---: | :---: |
| $0$ | $1$ |
| $1$ | $2$ |

$$\int_0^1\frac{x\thinspace dx}{\big(x^2+1\big)^2} = \frac12\int_1^2 u^{-2}du = \frac12\left[-\frac1u\right]_1^2 = \frac12\left(-\frac12+1\right) = \frac14$$

> 💡 **Note que os limites mudaram de verdade** ($[0,1]$ virou $[1,2]$). Manter os originais daria $\frac12\left[-\frac1u\right]_0^1$ — expressão que nem existe, já que $u=0$ anularia o denominador. Nesse caso o erro é visível; em outros, não.

---

## Questão 5 &nbsp;·&nbsp; *(2,0)*

**(a) A região.** Interseções:

$$x^2 = 2x \ \Longrightarrow \ x(x-2) = 0 \ \Longrightarrow \ x=0 \ \text{ e } \ x=2$$

**Quem está por cima?** Em $x=1$: a reta dá $2$, a parábola dá $1$. A **reta** está acima.

$$A = \int_0^2\big(2x-x^2\big)dx = \left[x^2-\frac{x^3}{3}\right]_0^2 = 4-\frac83 = \frac43$$

**O esboço:** uma região em forma de "lente", limitada abaixo pela parábola e acima pela reta, entre a origem e o ponto $(2,4)$.

**(b) O volume.** A região **não encosta** no eixo $x$ (salvo nos extremos), então a secção é um **anel**. O raio externo é o da curva mais **distante** do eixo — a reta:

$$R(x) = 2x \qquad r(x) = x^2$$

$$V = \pi\int_0^2\left[(2x)^2-\big(x^2\big)^2\right]dx = \pi\int_0^2\left(4x^2-x^4\right)dx$$

$$= \pi\left[\frac{4x^3}{3}-\frac{x^5}{5}\right]_0^2 = \pi\left(\frac{32}{3}-\frac{32}{5}\right) = 32\pi\cdot\frac{5-3}{15} = \frac{64\pi}{15}$$

> ⚠️ **Dois erros caros neste item:**
> 1. usar $\pi\int(2x-x^2)^2dx$ — o quadrado é de **cada raio separadamente**, e $R^2-r^2 \neq (R-r)^2$;
> 2. inverter $R$ e $r$ — o que daria volume **negativo**, sinal inequívoco de que a ordem está trocada.

---

## Questão 6 &nbsp;·&nbsp; *(1,0)*

**(a)** É uma $p$-integral com $p=3>1$, logo **converge**. Pela definição:

$$\int_1^{\infty}\frac{dx}{x^3} = \lim_{b\to\infty}\left[-\frac{1}{2x^2}\right]_1^{b} = \lim_{b\to\infty}\left(\frac12 - \frac{1}{2b^2}\right) = \frac12$$

**(b)** O integrando explode em $x=0$, que é o extremo inferior — **imprópria do tipo 2**, com $p=2\geqslant1$:

$$\int_0^1\frac{dx}{x^2} = \lim_{t\to0^{+}}\left[-\frac1x\right]_t^{1} = \lim_{t\to0^{+}}\left(-1+\frac1t\right) = +\infty$$

**DIVERGE.**

> 💡 **Compare (a) e (b): mesmo tipo de função, vereditos opostos.** O expoente grande faz a função decair rápido **longe** da origem (bom para $\int_1^\infty$) e explodir violentamente **perto** dela (ruim para $\int_0^1$). Não existe "$p$ bom" — existe $p$ bom **para cada região**.

**(c)** Quero provar convergência, logo preciso de um **teto** que convirja.

Para $x\geqslant1$, tem-se $x^2+x > x^2$, e invertendo:

$$0 < \frac{1}{x^2+x} < \frac{1}{x^2}$$

Como $\displaystyle\int_1^{\infty}\frac{dx}{x^2}$ **converge** ($p=2>1$), o teste da comparação garante:

$$\int_1^{\infty}\frac{dx}{x^2+x} \quad\textbf{CONVERGE}$$

> 💡 **Esta integral até dá para calcular** por frações parciais ($\frac{1}{x(x+1)} = \frac1x - \frac{1}{x+1}$), e o resultado é $\ln 2$. Mas a questão pede **comparação** — e a comparação decide em três linhas, sem primitiva nenhuma. Quando o enunciado nomeia o método, use o método.

---

## 📋 Diagnóstico

| Acertos | O que fazer |
| :---: | --- |
| 5 ou 6 | Pronto para a P3. |
| 3 ou 4 | Refaça a [revisão da U5](../../05-integrais/exercicios/revisao-unidade-5.md). |
| 0 a 2 | Refaça a [Lista 5.2](../../05-integrais/exercicios/lista-5.2-propostos.md) **inteira** — é volume de exercícios que falta. |

> [!IMPORTANT]
> **Se você errou alguma integral indefinida (questões 1 e 2), confira: você derivou a sua resposta antes de entregar?**
>
> Esses $4{,}0$ pontos são os únicos de toda a disciplina que podem ser **garantidos** com uma conferência de dois minutos. Perder qualquer parte deles é perder ponto que não dependia de saber mais matemática.

---

| ← Simulado | 🏠 | Índice → |
| :--- | :---: | ---: |
| [Simulado P3](../simulado-p3-integrais.md) | [Página inicial](../../README.md) | [Simulados](../README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
