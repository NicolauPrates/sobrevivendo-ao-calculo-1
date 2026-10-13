# A5 · Símbolos e alfabeto grego

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A4 · Limites notáveis](A4-limites-notaveis.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A6 · Glossário](A6-glossario.md) |

> Esta página existe para você parar de chamar $\varepsilon$ de "aquele *e* esquisito" — e, mais importante, para conseguir **ler o enunciado** antes de resolvê-lo.

---

## 1. Alfabeto grego

| Minúscula | Maiúscula | Nome | Onde aparece em Cálculo |
| :---: | :---: | --- | --- |
| $\alpha$ | $A$ | alfa | ângulos, expoentes, parâmetros |
| $\beta$ | $B$ | beta | ângulos, parâmetros |
| $\gamma$ | $\Gamma$ | gama | a **função Gama** $\Gamma$ generaliza o fatorial |
| $\delta$ | $\Delta$ | delta | $\delta$ na definição de limite; $\Delta$ = **variação** |
| $\varepsilon$ | $E$ | épsilon | "um número positivo tão pequeno quanto se queira" |
| $\theta$ | $\Theta$ | teta | **ângulos** — o padrão em substituição trigonométrica |
| $\lambda$ | $\Lambda$ | lambda | taxa de decaimento, multiplicador |
| $\mu$ | $M$ | mi | média (estatística), micro |
| $\pi$ | $\Pi$ | pi | $\pi\approx3{,}14159$; $\Pi$ = produtório |
| $\rho$ | $P$ | rô | densidade, raio polar |
| $\sigma$ | $\Sigma$ | sigma | desvio padrão; $\Sigma$ = **somatório** |
| $\tau$ | $T$ | tau | tempo, torque |
| $\varphi$ | $\Phi$ | fi | ângulo, razão áurea |
| $\omega$ | $\Omega$ | ômega | frequência angular |

> 💡 **$\Delta$ e $\delta$ são a mesma letra, mas significam coisas diferentes.** O $\Delta$ maiúsculo é uma **variação finita** ($\Delta x = x_2-x_1$); o $\delta$ minúsculo é a **distância arbitrariamente pequena** da definição formal de limite. Confundir os dois numa demonstração custa caro.

---

## 2. Conjuntos

| Símbolo | Leitura |
| :---: | --- |
| $\mathbb{N}$ | naturais: $0,1,2,3,\ldots$ |
| $\mathbb{Z}$ | inteiros: $\ldots,-2,-1,0,1,2,\ldots$ |
| $\mathbb{Q}$ | racionais (frações de inteiros) |
| $\mathbb{R}$ | reais |
| $\mathbb{C}$ | complexos |
| $\emptyset$ | conjunto vazio |
| $\in$ | pertence |
| $\notin$ | não pertence |
| $\subset$ | está contido |
| $\cup$ | união |
| $\cap$ | interseção |
| $\setminus$ | menos (diferença de conjuntos) |

**Intervalos:**

| Notação | Significa |
| :---: | --- |
| $[a,b]$ | **fechado**: inclui $a$ e $b$ |
| $(a,b)$ | **aberto**: exclui os dois |
| $[a,b)$ | inclui $a$, exclui $b$ |
| $(a,+\infty)$ | o infinito **nunca** é incluído |

---

## 3. Lógica e demonstração

| Símbolo | Leitura |
| :---: | --- |
| $\forall$ | para todo |
| $\exists$ | existe |
| $\exists!$ | existe um único |
| $\Rightarrow$ | implica ("se… então") |
| $\iff$ | se, e somente se |
| $\therefore$ | portanto |
| $\blacksquare$ | fim da demonstração |

> 💡 **$\Rightarrow$ só vale num sentido.** "Derivável $\Rightarrow$ contínua" é verdade; a recíproca é falsa ($\lvert x\rvert$ em zero). Trocar $\Rightarrow$ por $\iff$ sem verificar é o erro lógico mais comum em provas escritas.

---

## 4. Comparação

| Símbolo | Leitura |
| :---: | --- |
| $\leqslant$ · $\geqslant$ | menor ou igual · maior ou igual |
| $\neq$ | diferente |
| $\approx$ | aproximadamente igual |
| $\equiv$ | identicamente igual (para **todo** valor) |
| $\ll$ · $\gg$ | muito menor · muito maior |
| $\to$ | tende a |
| $\propto$ | proporcional a |

> 💡 **$=$ e $\equiv$ não são a mesma coisa.** $\operatorname{sen} x = 0$ vale só para certos $x$; $\operatorname{sen}^2 x + \cos^2 x \equiv 1$ vale para **todos**. Em identidades trigonométricas, o segundo é o correto.

---

## 5. Notação de Cálculo

### Derivada — as três notações

| Notação | Nome | Primeira | Segunda | $n$-ésima |
| --- | --- | :---: | :---: | :---: |
| **Lagrange** | linha | $f'(x)$ | $f''(x)$ | $f^{(n)}(x)$ |
| **Leibniz** | diferencial | $\dfrac{dy}{dx}$ | $\dfrac{d^2y}{dx^2}$ | $\dfrac{d^ny}{dx^n}$ |
| **Newton** | ponto | $\dot{y}$ | $\ddot{y}$ | — |

> 💡 **Cada uma serve a um uso.** Lagrange é compacta e boa para enunciar teoremas. **Leibniz diz em relação a quê** você está derivando — indispensável em taxas relacionadas e na regra da cadeia, onde o "cancelamento" $\frac{dy}{du}\cdot\frac{du}{dx} = \frac{dy}{dx}$ fica visível. Newton é usada em física, para derivadas **em relação ao tempo**.

### Integral

| Símbolo | Significa |
| :---: | --- |
| $\displaystyle\int f(x)\thinspace dx$ | integral **indefinida**: a família de primitivas |
| $\displaystyle\int_a^b f(x)\thinspace dx$ | integral **definida**: um número |
| $\Big[F(x)\Big]_a^b$ | abreviação de $F(b)-F(a)$ |

### Somatório

$$\sum_{i=1}^{n} a_i = a_1 + a_2 + \cdots + a_n$$

**Fórmulas que aparecem em somas de Riemann:**

$$\sum_{i=1}^{n} 1 = n \qquad \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \qquad \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} \qquad \sum_{i=1}^{n} i^3 = \left[\frac{n(n+1)}{2}\right]^2$$

### Outros

| Símbolo | Significa |
| :---: | --- |
| $\lvert x\rvert$ | valor absoluto |
| $n!$ | fatorial: $n(n-1)\cdots 2\cdot 1$, com $0!=1$ |
| $\lim\limits_{x\to a}$ | limite quando $x$ tende a $a$ |
| $x\to a^{+}$ · $x\to a^{-}$ | pela **direita** · pela **esquerda** |
| $f\circ g$ | composta: $f\big(g(x)\big)$ |
| $f^{-1}$ | função **inversa** (não é $\frac1f$) |

> ⚠️ **$f^{-1}$ versus $f^{-1}$.** Em $f^{-1}(x)$, o $-1$ indica **inversa**. Mas em $\operatorname{sen}^{2}x$, o $2$ indica **potência**. A notação é genuinamente ambígua e a convenção é só costume: $\operatorname{sen}^{-1}x$ significa $\operatorname{arcsen} x$, **não** $\frac{1}{\operatorname{sen} x}$ (que é $\operatorname{cossec} x$).
>
> É um dos motivos de este material preferir **$\operatorname{arcsen}$** a $\operatorname{sen}^{-1}$.

---

## 6. Como se lê em voz alta

| Escrito | Lê-se |
| --- | --- |
| $\displaystyle\lim_{x\to2} f(x) = 5$ | "o limite de $f$ de $x$, quando $x$ tende a $2$, é $5$" |
| $\dfrac{dy}{dx}$ | "dê ípsilon, dê xis" (ou "derivada de $y$ em relação a $x$") |
| $\displaystyle\int_0^1 x^2 dx$ | "integral, de zero a um, de $x$ ao quadrado, $de$ $x$" |
| $f''(3)$ | "efe duas linhas de três" |
| $\forall\thinspace\varepsilon>0,\ \exists\thinspace\delta>0$ | "para todo épsilon positivo, existe delta positivo" |

---

| ← Anterior | 🏠 | Próximo → |
| :--- | :---: | ---: |
| [A4 · Limites notáveis](A4-limites-notaveis.md) | [Formulário](README.md) · [Página inicial](../README.md) | [A6 · Glossário](A6-glossario.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
