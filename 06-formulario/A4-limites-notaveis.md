# A4 · Limites notáveis

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A3 · Identidades trigonométricas](A3-identidades-trigonometricas.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A5 · Símbolos e alfabeto grego](A5-simbolos-e-alfabeto-grego.md) |

> **Teoria correspondente:** [Unidade 2](../02-limites-e-continuidade/README.md) e a [Regra de L&#39;Hôspital (4.3)](../04-aplicacoes-das-derivadas/4.3-regra-de-lhospital.md).

---

## 1. Os sete casos de indeterminação

$$\frac{0}{0} \qquad \frac{\infty}{\infty} \qquad 0\cdot\infty \qquad \infty-\infty \qquad 1^{\infty} \qquad 0^{0} \qquad \infty^{0}$$

> [!IMPORTANT]
> **"Indeterminado" não significa "não existe"** — significa que a **forma** não decide. O limite pode existir, pode ser infinito, pode não existir: é preciso investigar.
>
> E o contrário também vale: $\dfrac{5}{0}$, $\dfrac{0}{5}$ e $\infty+\infty$ **não** são indeterminações. Eles decidem na hora.

**Para usar L&#39;Hôspital**, converta tudo para $\frac00$ ou $\frac{\infty}{\infty}$:

| Forma | Como converter |
| :---: | --- |
| $0\cdot\infty$ | passe um fator para o denominador |
| $\infty-\infty$ | some as frações, ou racionalize |
| $1^{\infty}$, $0^0$, $\infty^0$ | aplique $\ln$, calcule, e **exponencie no fim** |

---

## 2. Os trigonométricos

$$\lim_{x\to0}\frac{\operatorname{sen} x}{x} = 1$$

$$\lim_{x\to0}\frac{1-\cos x}{x} = 0 \qquad\qquad \lim_{x\to0}\frac{1-\cos x}{x^2} = \frac12$$

$$\lim_{x\to0}\frac{\operatorname{tg} x}{x} = 1 \qquad\qquad \lim_{x\to0}\frac{\operatorname{arcsen} x}{x} = 1 \qquad\qquad \lim_{x\to0}\frac{\operatorname{arctg} x}{x} = 1$$

> 💡 **O primeiro é o limite fundamental da trigonometria**, demonstrado pelo [Teorema do Sanduíche (2.3)](../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md). Todos os outros desta seção saem dele, e é dele que vem a derivada do seno.

**Versão geral** (com $\square$ representando qualquer expressão que tenda a zero):

$$\lim_{\square\to0}\frac{\operatorname{sen}\square}{\square} = 1$$

Assim, $\displaystyle\lim_{x\to0}\frac{\operatorname{sen}(5x)}{5x} = 1$ — e, para $\frac{\operatorname{sen}(5x)}{x}$, multiplique e divida por $5$ para obter $5$.

---

## 3. Os exponenciais e logarítmicos

$$\lim_{x\to0}\frac{e^{x}-1}{x} = 1 \qquad\qquad \lim_{x\to0}\frac{a^{x}-1}{x} = \ln a$$

$$\lim_{x\to0}\frac{\ln(1+x)}{x} = 1$$

$$\lim_{x\to\infty}\left(1+\frac1x\right)^{x} = e \qquad\qquad \lim_{x\to0}\big(1+x\big)^{1/x} = e$$

$$\lim_{x\to\infty}\left(1+\frac{k}{x}\right)^{x} = e^{k}$$

> 💡 **Todos esses são, no fundo, derivadas disfarçadas.** $\lim_{x\to0}\frac{e^x-1}{x}$ é a definição de $\big(e^x\big)'$ em $x=0$, que vale $e^0=1$. Reconhecer isso evita decorar a lista: cada linha é $f'(0)$ para alguma função conhecida.

---

## 4. A hierarquia do infinito

Quando $x\to+\infty$, estas funções crescem em **velocidades incomparáveis**:

$$\ln x \ \ll \ x^{p} \ \ll \ a^{x} \ \ll \ x! \ \ll \ x^{x} \qquad (p>0,\ a>1)$$

**Consequências diretas:**

$$\lim_{x\to\infty}\frac{\ln x}{x^{p}} = 0 \qquad \lim_{x\to\infty}\frac{x^{p}}{e^{x}} = 0 \qquad \lim_{x\to\infty}\frac{x^{n}}{a^{x}} = 0$$

**E a versão "perto do zero":**

$$\lim_{x\to0^{+}} x^{p}\ln x = 0 \qquad (p>0)$$

> [!TIP]
> **A hierarquia resolve de cabeça limites que L&#39;Hôspital resolveria em cinco derivadas.** $\lim\frac{x^{100}}{e^x} = 0$: a exponencial vence, ponto final. Aplicar a regra cem vezes daria o mesmo resultado e cem vezes mais trabalho.
>
> E ela vale **para qualquer expoente**, por maior que seja. Não existe potência que vença uma exponencial.

---

## 5. Limites no infinito de funções racionais

Para $\displaystyle\lim_{x\to\pm\infty}\frac{P(x)}{Q(x)}$, compare os **graus**:

| | Limite | Assíntota |
| --- | :---: | --- |
| $\operatorname{gr} P < \operatorname{gr} Q$ | $0$ | horizontal $y=0$ |
| $\operatorname{gr} P = \operatorname{gr} Q$ | razão dos **coeficientes líderes** | horizontal nesse valor |
| $\operatorname{gr} P = \operatorname{gr} Q + 1$ | $\pm\infty$ | **oblíqua** (faça a divisão) |
| $\operatorname{gr} P > \operatorname{gr} Q + 1$ | $\pm\infty$ | nenhuma |

---

## 6. Limites laterais e infinitos

| Expressão | Resultado |
| :---: | :---: |
| $\dfrac{k}{0^{+}}$ &nbsp;($k>0$) | $+\infty$ |
| $\dfrac{k}{0^{-}}$ &nbsp;($k>0$) | $-\infty$ |
| $\dfrac{k}{\pm\infty}$ | $0$ |
| $\displaystyle\lim_{x\to0^{+}}\ln x$ | $-\infty$ |
| $\displaystyle\lim_{x\to-\infty}e^{x}$ | $0$ |
| $\displaystyle\lim_{x\to+\infty}e^{x}$ | $+\infty$ |
| $\displaystyle\lim_{x\to\pm\infty}\operatorname{arctg} x$ | $\pm\dfrac{\pi}{2}$ |

> ⚠️ **O sinal do $0$ no denominador decide tudo.** Escrever só "$\frac{k}{0}$" perde a informação: é preciso saber se o denominador se aproxima de zero **por cima** ou **por baixo**. Teste com um valor próximo e veja o sinal.

---

## 7. Os teoremas que decidem quando a conta não decide

| Teorema | Enunciado | Use quando |
| --- | --- | --- |
| **Sanduíche** | $g\leqslant f\leqslant h$ e $g,h\to L$ ⟹ $f\to L$ | há seno ou cosseno **limitado** multiplicando |
| **L&#39;Hôspital** | $\frac00$ ou $\frac\infty\infty$ ⟹ $\lim\frac fg = \lim\frac{f'}{g'}$ | **só** nessas duas formas |
| **TVI** | $f$ contínua troca de sinal ⟹ tem raiz | provar que existe solução |

> ⚠️ **Antes de aplicar L&#39;Hôspital, substitua.** Se a substituição der um número, esse número **é** a resposta — derivar numerador e denominador nesse caso **inventa** um resultado errado.

---

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A3 · Identidades trigonométricas](A3-identidades-trigonometricas.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A5 · Símbolos e alfabeto grego](A5-simbolos-e-alfabeto-grego.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
