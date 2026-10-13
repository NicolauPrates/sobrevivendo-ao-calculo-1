# A3 · Identidades trigonométricas

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A2 · Tabela de integrais](A2-tabela-de-integrais.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A4 · Limites notáveis](A4-limites-notaveis.md) |

> **Onde isso é usado:** limites trigonométricos ([2.3](../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md)), derivadas ([3.2](../03-derivadas/3.2-derivadas-das-funcoes-elementares.md)) e, sobretudo, técnicas de integração ([5.2](../05-integrais/5.2-tecnicas-de-integracao.md)).

> 📝 **Notação brasileira:** $\operatorname{sen}$, $\operatorname{tg}$, $\operatorname{cotg}$, $\operatorname{sec}$, $\operatorname{cossec}$ — veja [CONVENCOES.md](../CONVENCOES.md).

---

## 1. Definições a partir de seno e cosseno

$$\operatorname{tg} x = \frac{\operatorname{sen} x}{\cos x} \qquad \operatorname{cotg} x = \frac{\cos x}{\operatorname{sen} x} = \frac{1}{\operatorname{tg} x}$$

$$\operatorname{sec} x = \frac{1}{\cos x} \qquad \operatorname{cossec} x = \frac{1}{\operatorname{sen} x}$$

> [!TIP]
> **Quando uma identidade trigonométrica não aparecer, reescreva tudo em seno e cosseno.** É o movimento que destrava a maioria das integrais trigonométricas estranhas — e muitas vezes revela um cancelamento que não estava visível.

---

## 2. Valores notáveis

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| graus | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $270°$ | $360°$ |
| $\operatorname{sen} x$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}{2}$ | $\dfrac{\sqrt3}{2}$ | $1$ | $0$ | $-1$ | $0$ |
| $\cos x$ | $1$ | $\dfrac{\sqrt3}{2}$ | $\dfrac{\sqrt2}{2}$ | $\dfrac12$ | $0$ | $-1$ | $0$ | $1$ |
| $\operatorname{tg} x$ | $0$ | $\dfrac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | ∄ | $0$ | ∄ | $0$ |

> 💡 **O truque da mão esquerda.** Para $0°,30°,45°,60°,90°$, o seno é $\dfrac{\sqrt0}{2}, \dfrac{\sqrt1}{2}, \dfrac{\sqrt2}{2}, \dfrac{\sqrt3}{2}, \dfrac{\sqrt4}{2}$ — basta contar $0,1,2,3,4$ sob a raiz. O cosseno é a mesma sequência **ao contrário**.

---

## 3. Identidades pitagóricas

$$\operatorname{sen}^2 x + \cos^2 x = 1$$

$$1 + \operatorname{tg}^2 x = \operatorname{sec}^2 x$$

$$1 + \operatorname{cotg}^2 x = \operatorname{cossec}^2 x$$

> 💡 **As duas últimas saem da primeira.** Divida $\operatorname{sen}^2+\cos^2=1$ por $\cos^2 x$ e aparece a segunda; divida por $\operatorname{sen}^2 x$ e aparece a terceira. **Decore uma, deduza três.**

**As formas mais usadas em integração:**

$$\operatorname{sen}^2 x = 1-\cos^2 x \qquad \operatorname{tg}^2 x = \operatorname{sec}^2 x - 1 \qquad \operatorname{cotg}^2 x = \operatorname{cossec}^2 x - 1$$

---

## 4. Paridade e periodicidade

| | |
| --- | --- |
| $\operatorname{sen}(-x) = -\operatorname{sen} x$ | **ímpar** |
| $\cos(-x) = \cos x$ | **par** |
| $\operatorname{tg}(-x) = -\operatorname{tg} x$ | **ímpar** |

**Períodos:** $\operatorname{sen}$, $\cos$, $\operatorname{sec}$ e $\operatorname{cossec}$ têm período $2\pi$; $\operatorname{tg}$ e $\operatorname{cotg}$ têm período $\pi$.

**Relações de complemento:**

$$\operatorname{sen}\left(\frac{\pi}{2}-x\right) = \cos x \qquad \cos\left(\frac{\pi}{2}-x\right) = \operatorname{sen} x$$

---

## 5. Soma e diferença de arcos

$$\operatorname{sen}(a\pm b) = \operatorname{sen} a\cos b \pm \cos a\operatorname{sen} b$$

$$\cos(a\pm b) = \cos a\cos b \mp \operatorname{sen} a\operatorname{sen} b$$

$$\operatorname{tg}(a\pm b) = \frac{\operatorname{tg} a \pm \operatorname{tg} b}{1 \mp \operatorname{tg} a\operatorname{tg} b}$$

> ⚠️ **Atenção aos sinais cruzados do cosseno:** $\cos(a+b)$ leva **menos**, e $\cos(a-b)$ leva **mais**. É o contrário do seno, e é o erro mais comum desta página.

---

## 6. Arco duplo

$$\operatorname{sen} 2x = 2\operatorname{sen} x\cos x$$

$$\cos 2x = \cos^2 x - \operatorname{sen}^2 x = 2\cos^2 x - 1 = 1 - 2\operatorname{sen}^2 x$$

$$\operatorname{tg} 2x = \frac{2\operatorname{tg} x}{1-\operatorname{tg}^2 x}$$

> 💡 **As três formas de $\cos 2x$ existem porque cada uma serve a um propósito.** A segunda isola o cosseno; a terceira isola o seno — e é de onde saem as fórmulas de redução de potência abaixo.

---

## 7. Redução de potência — as que resolvem integrais

Isolando $\operatorname{sen}^2$ e $\cos^2$ nas identidades de arco duplo:

$$\operatorname{sen}^2 x = \frac{1-\cos 2x}{2} \qquad\qquad \cos^2 x = \frac{1+\cos 2x}{2}$$

> [!TIP]
> **Estas duas são as identidades mais rentáveis do formulário inteiro.** Toda integral de potência **par** de seno ou cosseno passa por aqui. Sem elas, $\int\operatorname{sen}^2 x\thinspace dx$ é impossível; com elas, é imediata.
>
> **Como lembrar o sinal:** $\cos^2$ fica com o **mais** (as duas palavras têm "co"). O seno fica com o menos.

---

## 8. Arco metade

$$\operatorname{sen}\frac{x}{2} = \pm\sqrt{\frac{1-\cos x}{2}} \qquad \cos\frac{x}{2} = \pm\sqrt{\frac{1+\cos x}{2}}$$

(o sinal depende do quadrante de $\frac{x}{2}$)

---

## 9. Produto em soma

$$\operatorname{sen} a\cos b = \frac12\Big[\operatorname{sen}(a+b)+\operatorname{sen}(a-b)\Big]$$

$$\operatorname{sen} a\operatorname{sen} b = \frac12\Big[\cos(a-b)-\cos(a+b)\Big]$$

$$\cos a\cos b = \frac12\Big[\cos(a-b)+\cos(a+b)\Big]$$

> 💡 **Para que servem:** transformam $\int\operatorname{sen}(3x)\cos(5x)\thinspace dx$ — que não tem padrão nenhum — numa soma de duas integrais imediatas. Raramente caem em Cálculo 1, mas quando caem, são a única saída.

---

## 10. Trigonométricas inversas

| Função | Domínio | Imagem |
| --- | :---: | :---: |
| $\operatorname{arcsen} x$ | $[-1,1]$ | $\left[-\frac{\pi}{2},\thinspace\frac{\pi}{2}\right]$ |
| $\operatorname{arccos} x$ | $[-1,1]$ | $[0,\thinspace\pi]$ |
| $\operatorname{arctg} x$ | $\mathbb{R}$ | $\left(-\frac{\pi}{2},\thinspace\frac{\pi}{2}\right)$ |

**Relações úteis:**

$$\operatorname{arcsen} x + \operatorname{arccos} x = \frac{\pi}{2} \qquad \operatorname{arctg} x + \operatorname{arccotg} x = \frac{\pi}{2}$$

$$\cos\big(\operatorname{arcsen} x\big) = \sqrt{1-x^2} \qquad \operatorname{sen}\big(\operatorname{arctg} x\big) = \frac{x}{\sqrt{1+x^2}}$$

> 💡 **As duas últimas saem de um triângulo**, não de decoreba. Para $\theta = \operatorname{arcsen} x$: monte o triângulo com hipotenusa $1$ e cateto oposto $x$; o adjacente é $\sqrt{1-x^2}$, e daí lê-se qualquer razão de $\theta$. É exatamente o procedimento da substituição trigonométrica.

**Limites notáveis das inversas:**

$$\lim_{x\to+\infty}\operatorname{arctg} x = \frac{\pi}{2} \qquad \lim_{x\to-\infty}\operatorname{arctg} x = -\frac{\pi}{2}$$

---

## 11. O que decorar e o que deduzir

| **Decore** | **Deduza** |
| --- | --- |
| $\operatorname{sen}^2+\cos^2=1$ | as outras duas pitagóricas (divida por $\cos^2$ ou $\operatorname{sen}^2$) |
| soma e diferença de arcos | arco duplo (faça $b=a$) |
| $\cos 2x = 1-2\operatorname{sen}^2 x$ | redução de potência (isole $\operatorname{sen}^2$) |
| a linha dos valores notáveis do seno | a do cosseno (é a mesma ao contrário) |
| as definições de $\operatorname{tg}$, $\operatorname{sec}$… | tudo que envolver elas (volte a seno e cosseno) |

> [!TIP]
> **Cinco linhas decoradas geram esta página inteira.** Em prova sem consulta, é isso que você precisa levar — o resto se reconstrói em trinta segundos.

---

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A2 · Tabela de integrais](A2-tabela-de-integrais.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A4 · Limites notáveis](A4-limites-notaveis.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
