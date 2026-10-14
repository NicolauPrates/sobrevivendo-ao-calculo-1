# A3 · Identidades trigonométricas

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A2 · Tabela de integrais](A2-tabela-de-integrais.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A4 · Limites notáveis](A4-limites-notaveis.md) |

> **Onde isso é usado:** limites trigonométricos ([2.3](../02-limites-e-continuidade/2.3-teorema-do-sanduiche.md)), derivadas ([3.2](../03-derivadas/3.2-derivadas-das-funcoes-elementares.md)) e, sobretudo, técnicas de integração ([5.2](../05-integrais/5.2-tecnicas-de-integracao.md)).

> 📝 **Notação brasileira:** $\mathrm{sen}$, $\mathrm{tg}$, $\mathrm{cotg}$, $\mathrm{sec}$, $\mathrm{cossec}$ — veja [CONVENCOES.md](../CONVENCOES.md).

---

## 1. Definições a partir de seno e cosseno

$$\mathrm{tg}\thinspace x = \frac{\mathrm{sen}\thinspace x}{\cos x} \qquad \mathrm{cotg}\thinspace x = \frac{\cos x}{\mathrm{sen}\thinspace x} = \frac{1}{\mathrm{tg}\thinspace x}$$

$$\mathrm{sec}\thinspace x = \frac{1}{\cos x} \qquad \mathrm{cossec}\thinspace x = \frac{1}{\mathrm{sen}\thinspace x}$$

> [!TIP]
> **Quando uma identidade trigonométrica não aparecer, reescreva tudo em seno e cosseno.** É o movimento que destrava a maioria das integrais trigonométricas estranhas — e muitas vezes revela um cancelamento que não estava visível.

---

## 2. Valores notáveis

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| graus | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $270°$ | $360°$ |
| $\mathrm{sen}\thinspace x$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}{2}$ | $\dfrac{\sqrt3}{2}$ | $1$ | $0$ | $-1$ | $0$ |
| $\cos x$ | $1$ | $\dfrac{\sqrt3}{2}$ | $\dfrac{\sqrt2}{2}$ | $\dfrac12$ | $0$ | $-1$ | $0$ | $1$ |
| $\mathrm{tg}\thinspace x$ | $0$ | $\dfrac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | ∄ | $0$ | ∄ | $0$ |

> 💡 **O truque da mão esquerda.** Para $0°,30°,45°,60°,90°$, o seno é $\dfrac{\sqrt0}{2}, \dfrac{\sqrt1}{2}, \dfrac{\sqrt2}{2}, \dfrac{\sqrt3}{2}, \dfrac{\sqrt4}{2}$ — basta contar $0,1,2,3,4$ sob a raiz. O cosseno é a mesma sequência **ao contrário**.

---

## 3. Identidades pitagóricas

$$\mathrm{sen}^2\thinspace x + \cos^2 x = 1$$

$$1 + \mathrm{tg}^2\thinspace x = \mathrm{sec}^2\thinspace x$$

$$1 + \mathrm{cotg}^2\thinspace x = \mathrm{cossec}^2\thinspace x$$

> 💡 **As duas últimas saem da primeira.** Divida $\mathrm{sen}^2+\cos^2=1$ por $\cos^2 x$ e aparece a segunda; divida por $\mathrm{sen}^2\thinspace x$ e aparece a terceira. **Decore uma, deduza três.**

**As formas mais usadas em integração:**

$$\mathrm{sen}^2\thinspace x = 1-\cos^2 x \qquad \mathrm{tg}^2\thinspace x = \mathrm{sec}^2\thinspace x - 1 \qquad \mathrm{cotg}^2\thinspace x = \mathrm{cossec}^2\thinspace x - 1$$

---

## 4. Paridade e periodicidade

| | |
| --- | --- |
| $\mathrm{sen}(-x) = -\mathrm{sen}\thinspace x$ | **ímpar** |
| $\cos(-x) = \cos x$ | **par** |
| $\mathrm{tg}(-x) = -\mathrm{tg}\thinspace x$ | **ímpar** |

**Períodos:** $\mathrm{sen}$, $\cos$, $\mathrm{sec}$ e $\mathrm{cossec}$ têm período $2\pi$; $\mathrm{tg}$ e $\mathrm{cotg}$ têm período $\pi$.

**Relações de complemento:**

$$\mathrm{sen}\left(\frac{\pi}{2}-x\right) = \cos x \qquad \cos\left(\frac{\pi}{2}-x\right) = \mathrm{sen}\thinspace x$$

---

## 5. Soma e diferença de arcos

$$\mathrm{sen}(a\pm b) = \mathrm{sen}\thinspace a\cos b \pm \cos a\mathrm{sen}\thinspace b$$

$$\cos(a\pm b) = \cos a\cos b \mp \mathrm{sen}\thinspace a\mathrm{sen}\thinspace b$$

$$\mathrm{tg}(a\pm b) = \frac{\mathrm{tg}\thinspace a \pm \mathrm{tg}\thinspace b}{1 \mp \mathrm{tg}\thinspace a\mathrm{tg}\thinspace b}$$

> ⚠️ **Atenção aos sinais cruzados do cosseno:** $\cos(a+b)$ leva **menos**, e $\cos(a-b)$ leva **mais**. É o contrário do seno, e é o erro mais comum desta página.

---

## 6. Arco duplo

$$\mathrm{sen}\thinspace 2x = 2\mathrm{sen}\thinspace x\cos x$$

$$\cos 2x = \cos^2 x - \mathrm{sen}^2\thinspace x = 2\cos^2 x - 1 = 1 - 2\mathrm{sen}^2\thinspace x$$

$$\mathrm{tg}\thinspace 2x = \frac{2\mathrm{tg}\thinspace x}{1-\mathrm{tg}^2\thinspace x}$$

> 💡 **As três formas de $\cos 2x$ existem porque cada uma serve a um propósito.** A segunda isola o cosseno; a terceira isola o seno — e é de onde saem as fórmulas de redução de potência abaixo.

---

## 7. Redução de potência — as que resolvem integrais

Isolando $\mathrm{sen}^2$ e $\cos^2$ nas identidades de arco duplo:

$$\mathrm{sen}^2\thinspace x = \frac{1-\cos 2x}{2} \qquad\qquad \cos^2 x = \frac{1+\cos 2x}{2}$$

> [!TIP]
> **Estas duas são as identidades mais rentáveis do formulário inteiro.** Toda integral de potência **par** de seno ou cosseno passa por aqui. Sem elas, $\int\mathrm{sen}^2\thinspace x\thinspace dx$ é impossível; com elas, é imediata.
>
> **Como lembrar o sinal:** $\cos^2$ fica com o **mais** (as duas palavras têm "co"). O seno fica com o menos.

---

## 8. Arco metade

$$\mathrm{sen}\thinspace\frac{x}{2} = \pm\sqrt{\frac{1-\cos x}{2}} \qquad \cos\frac{x}{2} = \pm\sqrt{\frac{1+\cos x}{2}}$$

(o sinal depende do quadrante de $\frac{x}{2}$)

---

## 9. Produto em soma

$$\mathrm{sen}\thinspace a\cos b = \frac12\Big[\mathrm{sen}(a+b)+\mathrm{sen}(a-b)\Big]$$

$$\mathrm{sen}\thinspace a\mathrm{sen}\thinspace b = \frac12\Big[\cos(a-b)-\cos(a+b)\Big]$$

$$\cos a\cos b = \frac12\Big[\cos(a-b)+\cos(a+b)\Big]$$

> 💡 **Para que servem:** transformam $\int\mathrm{sen}(3x)\cos(5x)\thinspace dx$ — que não tem padrão nenhum — numa soma de duas integrais imediatas. Raramente caem em Cálculo 1, mas quando caem, são a única saída.

---

## 10. Trigonométricas inversas

| Função | Domínio | Imagem |
| --- | :---: | :---: |
| $\mathrm{arcsen}\thinspace x$ | $[-1,1]$ | $\left[-\frac{\pi}{2},\thinspace\frac{\pi}{2}\right]$ |
| $\mathrm{arccos}\thinspace x$ | $[-1,1]$ | $[0,\thinspace\pi]$ |
| $\mathrm{arctg}\thinspace x$ | $\mathbb{R}$ | $\left(-\frac{\pi}{2},\thinspace\frac{\pi}{2}\right)$ |

**Relações úteis:**

$$\mathrm{arcsen}\thinspace x + \mathrm{arccos}\thinspace x = \frac{\pi}{2} \qquad \mathrm{arctg}\thinspace x + \mathrm{arccotg}\thinspace x = \frac{\pi}{2}$$

$$\cos\big(\mathrm{arcsen}\thinspace x\big) = \sqrt{1-x^2} \qquad \mathrm{sen}\big(\mathrm{arctg}\thinspace x\big) = \frac{x}{\sqrt{1+x^2}}$$

> 💡 **As duas últimas saem de um triângulo**, não de decoreba. Para $\theta = \mathrm{arcsen}\thinspace x$: monte o triângulo com hipotenusa $1$ e cateto oposto $x$; o adjacente é $\sqrt{1-x^2}$, e daí lê-se qualquer razão de $\theta$. É exatamente o procedimento da substituição trigonométrica.

**Limites notáveis das inversas:**

$$\lim_{x\to+\infty}\mathrm{arctg}\thinspace x = \frac{\pi}{2} \qquad \lim_{x\to-\infty}\mathrm{arctg}\thinspace x = -\frac{\pi}{2}$$

---

## 11. O que decorar e o que deduzir

| **Decore** | **Deduza** |
| --- | --- |
| $\mathrm{sen}^2+\cos^2=1$ | as outras duas pitagóricas (divida por $\cos^2$ ou $\mathrm{sen}^2$) |
| soma e diferença de arcos | arco duplo (faça $b=a$) |
| $\cos 2x = 1-2\mathrm{sen}^2\thinspace x$ | redução de potência (isole $\mathrm{sen}^2$) |
| a linha dos valores notáveis do seno | a do cosseno (é a mesma ao contrário) |
| as definições de $\mathrm{tg}$, $\mathrm{sec}$… | tudo que envolver elas (volte a seno e cosseno) |

> [!TIP]
> **Cinco linhas decoradas geram esta página inteira.** Em prova sem consulta, é isso que você precisa levar — o resto se reconstrói em trinta segundos.

---

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A2 · Tabela de integrais](A2-tabela-de-integrais.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A4 · Limites notáveis](A4-limites-notaveis.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
