# ✅ Gabarito — Lista 5.1

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 5.1](../exercicios/lista-5.1-propostos.md) · [Teoria 5.1](../5.1-primitivas-e-o-conceito-de-integral.md)

> 💡 **Antes de conferir:** derive a sua resposta. Se der o integrando, está certa — mesmo que a forma pareça diferente da minha. Duas primitivas corretas podem diferir por uma constante.

---

# ✅ Parte 1 — Respostas finais

*(O $+\thinspace C$ está subentendido em todas.)*

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $x^4-3x^2+7x$ |
| 1 (b) | $\dfrac{x^6}{6}-x^3$ |
| 1 (c) | $8x$ |
| 1 (d) | $4x-2x^2+\dfrac{x^3}{3}$ |
| 2 (a) | $\dfrac34 x^{4/3}$ |
| 2 (b) | $-\dfrac{1}{2x^2}$ |
| 2 (c) | $2\sqrt{x}$ |
| 2 (d) | $\dfrac25 x^{5/2}$ |
| 3 (a) | $3e^x - 2\ln\lvert x\rvert$ |
| 3 (b) | $-\cos x + 4\operatorname{sen} x$ |
| 3 (c) | $2\operatorname{tg} x - 5x$ |
| 3 (d) | $\dfrac{3^x}{\ln 3}$ |
| 4 (a) | $\dfrac{x^2}{2}+3x$ |
| 4 (b) | $\dfrac43 x^3 - \ln\lvert x\rvert - \dfrac{3}{x^2}$ |
| 5 | (a) **errada** · (b) **errada** · (c) **certa** · (d) **errada** |
| 6 | $f(x)=2x^2-3x-1$ |
| 7 | $f(x)=4-\dfrac1x$ |
| 8 | $f(x)=x^3+x-2$ |
| 9 | (a) V · (b) F · (c) V · (d) F |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 10 | $\dfrac{x^2}{2}+\dfrac43 x^{3/2}+x$ |
| 11 | $\dfrac25 x^{5/2}+\dfrac43 x^{3/2}+2\sqrt{x}$ |
| 12 | $-\operatorname{cotg} x - x$ |
| 13 | $\operatorname{sec} x$ |
| 14 | $\operatorname{tg} x + x$ |
| 15 | $x-\operatorname{arctg} x$ |
| 16 | $2\operatorname{arcsen} x$ |
| 17 | $f(x)=x^3-x-1$ |
| 18 | $s(t)=t^3-2t^2+2t+1$ |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | Demonstração (dois casos, $x>0$ e $x<0$) |
| 20 | Existem; **não** contradiz, porque $\mathbb{R}\setminus\lbrace0\rbrace$ não é intervalo |
| 21 | $a=1$ e $b=-1$, ou seja, $F(x)=(x-1)e^x$ |
| 22 | Demonstração (inclusive $F'(0)=0$ pela definição) |

---

# 📖 Parte 2 — Resoluções completas

## Bloco A · Fixação

### 1.

**(a)** Termo a termo, pela regra da potência:

$$\int \big(4x^3-6x+7\big)dx = 4\cdot\frac{x^4}{4} - 6\cdot\frac{x^2}{2} + 7x + C = x^4-3x^2+7x+C$$

**(b)** $\displaystyle\int \big(x^5-3x^2\big)dx = \frac{x^6}{6} - 3\cdot\frac{x^3}{3} + C = \frac{x^6}{6}-x^3+C$

**(c)** $\displaystyle\int 8\thinspace dx = 8x+C$

**(d)** **Expanda primeiro** — a tabela não integra potências de binômio:

$$(2-x)^2 = 4-4x+x^2$$

$$\int \big(4-4x+x^2\big)dx = 4x-2x^2+\frac{x^3}{3}+C$$

> 💡 **Se você respondeu $-\dfrac{(2-x)^3}{3}+C$, também está certo.** Derivando: $-\frac{3(2-x)^2\cdot(-1)}{3} = (2-x)^2$ ✔ As duas respostas diferem por $\frac83$, que é constante — e portanto descrevem a mesma família. Em integral, **formas diferentes podem ser igualmente corretas**.

---

### 2.

A regra é sempre a mesma: **reescreva como potência de $x$**, depois aplique $\int x^n dx = \frac{x^{n+1}}{n+1}$.

| Original | Como potência | Integral |
| --- | :---: | --- |
| **(a)** $\sqrt[3]{x}$ | $x^{1/3}$ | $\dfrac{x^{4/3}}{4/3} = \dfrac34 x^{4/3}+C$ |
| **(b)** $\dfrac{1}{x^3}$ | $x^{-3}$ | $\dfrac{x^{-2}}{-2} = -\dfrac{1}{2x^2}+C$ |
| **(c)** $\dfrac{1}{\sqrt{x}}$ | $x^{-1/2}$ | $\dfrac{x^{1/2}}{1/2} = 2\sqrt{x}+C$ |
| **(d)** $x\sqrt{x}$ | $x^{3/2}$ | $\dfrac{x^{5/2}}{5/2} = \dfrac25 x^{5/2}+C$ |

> ⚠️ **Dividir por uma fração é multiplicar pelo inverso.** O erro clássico aqui é escrever $\int x^{1/2}dx = \frac23 x^{3/2}$ e depois, em (c), "simplificar" $\frac{x^{1/2}}{1/2}$ para $\frac12 x^{1/2}$. Dividir por $\frac12$ **dobra**, não reduz pela metade.

---

### 3.

**(a)** $\displaystyle\int \left(3e^x-\frac2x\right)dx = 3e^x - 2\ln\lvert x\rvert + C$

**(b)** $\displaystyle\int \big(\operatorname{sen} x + 4\cos x\big)dx = -\cos x + 4\operatorname{sen} x + C$

> ⚠️ **O sinal.** $\int\operatorname{sen} = -\cos$ e $\int\cos = +\operatorname{sen}$. Se confundir, derive de volta: $(-\cos x)' = +\operatorname{sen} x$ ✔ Esse teste de dez segundos resolve a dúvida para sempre.

**(c)** $\displaystyle\int \big(2\operatorname{sec}^2 x - 5\big)dx = 2\operatorname{tg} x - 5x + C$

**(d)** $\displaystyle\int 3^x dx = \frac{3^x}{\ln 3} + C$

> 💡 **De onde vem o $\ln 3$.** Como $\big(3^x\big)' = 3^x\ln 3$, derivar introduz um fator $\ln 3$ — então integrar precisa **dividir** por ele para compensar. Toda exponencial de base diferente de $e$ carrega esse fator.

---

### 4.

**(a)** O denominador é um monômio, então a fração se divide:

$$\frac{x^2+3x}{x} = x+3 \qquad\Longrightarrow\qquad \int (x+3)\thinspace dx = \frac{x^2}{2}+3x+C$$

**(b)** Mesmo procedimento, com três parcelas:

$$\frac{4x^5-x^2+6}{x^3} = 4x^2 - x^{-1} + 6x^{-3}$$

$$\int \big(4x^2-x^{-1}+6x^{-3}\big)dx = \frac43 x^3 - \ln\lvert x\rvert + 6\cdot\frac{x^{-2}}{-2} + C = \frac43 x^3 - \ln\lvert x\rvert - \frac{3}{x^2} + C$$

> ⚠️ **A parcela $-x^{-1}$ é a única que foge da regra da potência.** Num mesmo exercício convivem $4x^2$ (potência), $x^{-1}$ (logaritmo) e $6x^{-3}$ (potência de novo). Identificar o expoente $-1$ no meio dos outros é exatamente o que a questão testa.

---

### 5.

**(a) ERRADA.** Derivando o resultado proposto: $(-\operatorname{sen} x)' = -\cos x$, mas o integrando era $+\cos x$.

**Correto:** $\displaystyle\int\cos x\thinspace dx = \operatorname{sen} x + C$

**(b) ERRADA** (ou, no mínimo, incompleta). A expressão $\ln x$ só existe para $x>0$, mas o integrando $\frac1x$ está definido também para $x<0$.

**Correto:** $\displaystyle\int\frac{dx}{x} = \ln\lvert x\rvert + C$

**(c) CERTA.** Verificando:

$$\big(2\sqrt{x}\big)' = 2\cdot\frac{1}{2\sqrt{x}} = \frac{1}{\sqrt{x}} = x^{-1/2} \ \checkmark$$

**(d) ERRADA.** Derivando o resultado proposto, pela regra da cadeia:

$$\big(\operatorname{sec}^2 x\big)' = 2\operatorname{sec} x\cdot\big(\operatorname{sec} x\operatorname{tg} x\big) = 2\operatorname{sec}^2 x\operatorname{tg} x$$

que não é o integrando. **Correto:** $\displaystyle\int\operatorname{sec} x\operatorname{tg} x\thinspace dx = \operatorname{sec} x + C$

> 💡 **Esta questão é o método da seção inteira em forma de exercício.** Toda integral pode ser auditada derivando — e três das quatro afirmações acima são erros que aparecem em prova todo semestre.

---

### 6.

$$f(x) = \int (4x-3)\thinspace dx = 2x^2-3x+C$$

Impondo $f(2)=1$:

$$2(4)-3(2)+C = 8-6+C = 1 \ \Longrightarrow \ C=-1$$

**Resposta.** $f(x) = 2x^2-3x-1$.

---

### 7.

$$f(x) = \int x^{-2}dx = \frac{x^{-1}}{-1}+C = -\frac1x + C$$

Impondo $f(1)=3$:

$$-1+C = 3 \ \Longrightarrow \ C = 4$$

**Resposta.** $f(x) = 4-\dfrac1x$.

---

### 8.

**Primeira integração.**

$$f'(x) = \int 6x\thinspace dx = 3x^2+C_1 \qquad f'(0) = C_1 = 1$$

logo $f'(x) = 3x^2+1$.

**Segunda integração.**

$$f(x) = \int \big(3x^2+1\big)dx = x^3+x+C_2 \qquad f(0) = C_2 = -2$$

**Resposta.** $f(x) = x^3+x-2$.

---

### 9.

**(a) Verdadeiro.** É o Teorema 5.1.1, e a hipótese está satisfeita: $\mathbb{R}$ **é** um intervalo.

**(b) Falso.** Derivando o resultado proposto, pela regra do produto:

$$\left(\frac{x^2}{2}\operatorname{sen} x\right)' = x\operatorname{sen} x + \frac{x^2}{2}\cos x \ \neq\ x\cos x$$

O erro de fundo é ter integrado cada fator separadamente, como se existisse "regra do produto" para integrais. A integral correta é $x\operatorname{sen} x + \cos x + C$, e sai por **integração por partes** ([5.2](../5.2-tecnicas-de-integracao.md)).

**(c) Verdadeiro.** Toda função contínua num intervalo tem primitiva. A demonstração vem na [seção 5.3](../5.3-integral-definida-e-o-teorema-fundamental-do-calculo.md): a função $F(x) = \int_a^x f(t)\thinspace dt$ é uma primitiva de $f$, e é exatamente isso que a **primeira parte do Teorema Fundamental** afirma.

> 💡 **Mas "ter primitiva" não é o mesmo que "saber escrevê-la".** A função $e^{-x^2}$ é contínua, logo **tem** primitiva — e está demonstrado que essa primitiva **não** pode ser escrita com as funções elementares. Existir e ser calculável são coisas diferentes.

**(d) Falso.** Contraexemplo com $f(x)=x$:

$$\int x^2 dx = \frac{x^3}{3}+C \qquad\text{mas}\qquad \left(\int x\thinspace dx\right)^2 = \left(\frac{x^2}{2}\right)^2 = \frac{x^4}{4}$$

---

## Bloco B · Consolidação

### 10.

**Expanda antes de integrar:**

$$\big(\sqrt{x}+1\big)^2 = x + 2\sqrt{x} + 1 = x + 2x^{1/2} + 1$$

$$\int \big(x+2x^{1/2}+1\big)dx = \frac{x^2}{2} + 2\cdot\frac23 x^{3/2} + x + C = \frac{x^2}{2} + \frac43 x^{3/2} + x + C$$

---

### 11.

$$\frac{(x+1)^2}{\sqrt{x}} = \frac{x^2+2x+1}{x^{1/2}} = x^{3/2} + 2x^{1/2} + x^{-1/2}$$

$$\int \left(x^{3/2}+2x^{1/2}+x^{-1/2}\right)dx = \frac25 x^{5/2} + \frac43 x^{3/2} + 2\sqrt{x} + C$$

> 💡 **Subtrair expoentes é o truque dos dois últimos exercícios.** Dividir por $\sqrt x = x^{1/2}$ é subtrair $\frac12$ de cada expoente: $x^2 \to x^{3/2}$, $x \to x^{1/2}$, $1 \to x^{-1/2}$. Feito isso, a integral é mecânica.

---

### 12.

A tabela não tem $\operatorname{cotg}^2$, mas tem $\operatorname{cossec}^2$. A identidade pitagórica correspondente é

$$\operatorname{cossec}^2 x = 1+\operatorname{cotg}^2 x \ \Longrightarrow \ \operatorname{cotg}^2 x = \operatorname{cossec}^2 x - 1$$

$$\int \operatorname{cotg}^2 x\thinspace dx = \int \big(\operatorname{cossec}^2 x - 1\big)dx = -\operatorname{cotg} x - x + C$$

---

### 13.

**Reescreva separando os fatores:**

$$\frac{\operatorname{sen} x}{\cos^2 x} = \frac{1}{\cos x}\cdot\frac{\operatorname{sen} x}{\cos x} = \operatorname{sec} x\operatorname{tg} x$$

que **está** na tabela:

$$\int \operatorname{sec} x\operatorname{tg} x\thinspace dx = \operatorname{sec} x + C$$

**Conferindo:** $(\operatorname{sec} x)' = \operatorname{sec} x\operatorname{tg} x = \dfrac{\operatorname{sen} x}{\cos^2 x}$ ✔

---

### 14.

**Divida a fração:**

$$\frac{1+\cos^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} + \frac{\cos^2 x}{\cos^2 x} = \operatorname{sec}^2 x + 1$$

$$\int \big(\operatorname{sec}^2 x + 1\big)dx = \operatorname{tg} x + x + C$$

---

### 15.

O grau do numerador **não é menor** que o do denominador, então o integrando não é uma forma de tabela. O ajuste é somar e subtrair $1$ no numerador:

$$\frac{x^2}{1+x^2} = \frac{\big(1+x^2\big)-1}{1+x^2} = 1 - \frac{1}{1+x^2}$$

$$\int \left(1-\frac{1}{1+x^2}\right)dx = x - \operatorname{arctg} x + C$$

> 💡 **Somar e subtrair o mesmo termo é um dos truques mais rentáveis da unidade.** Sempre que o numerador tiver grau maior ou igual ao do denominador, o primeiro movimento é esse (ou a divisão de polinômios, que é a versão geral dele).

---

### 16.

$$\int \frac{2}{\sqrt{1-x^2}}\thinspace dx = 2\int\frac{dx}{\sqrt{1-x^2}} = 2\operatorname{arcsen} x + C$$

---

### 17.

"A inclinação da tangente em cada ponto é $3x^2-1$" significa $f'(x) = 3x^2-1$.

$$f(x) = \int \big(3x^2-1\big)dx = x^3-x+C$$

A curva passa por $(2,5)$, isto é, $f(2)=5$:

$$8-2+C = 5 \ \Longrightarrow \ C = -1$$

**Resposta.** $f(x) = x^3-x-1$.

---

### 18.

**Da aceleração para a velocidade**, com $v(0)=2$:

$$v(t) = \int (6t-4)\thinspace dt = 3t^2-4t+C_1 \qquad v(0) = C_1 = 2$$

$$v(t) = 3t^2-4t+2$$

**Da velocidade para a posição**, com $s(0)=1$:

$$s(t) = \int \big(3t^2-4t+2\big)dt = t^3-2t^2+2t+C_2 \qquad s(0) = C_2 = 1$$

**Resposta.** $s(t) = t^3-2t^2+2t+1$.

---

## Bloco C · Desafio

### 19. Por que o módulo

**Caso $x>0$.** Aqui $\lvert x\rvert = x$, logo $\ln\lvert x\rvert = \ln x$ e

$$\frac{d}{dx}\ln x = \frac1x \ \checkmark$$

**Caso $x<0$.** Aqui $\lvert x\rvert = -x$ (que é **positivo**, então o logaritmo existe), logo $\ln\lvert x\rvert = \ln(-x)$. Pela regra da cadeia:

$$\frac{d}{dx}\ln(-x) = \frac{1}{-x}\cdot(-1) = \frac1x \ \checkmark$$

Nos **dois** casos a derivada é $\frac1x$ $\blacksquare$

**Por que isso justifica o módulo.** O integrando $\frac1x$ está definido para todo $x\neq0$. Se a resposta fosse $\ln x$, ela só faria sentido em $x>0$ — **metade** do domínio ficaria sem primitiva. Com o módulo, a fórmula cobre os dois lados de uma vez.

---

### 20. Duas primitivas cuja diferença não é constante

Considere, em $D = \mathbb{R}\setminus\lbrace0\rbrace$:

$$
F(x) = \ln\lvert x\rvert
\qquad\text{e}\qquad
G(x) = \begin{cases}
\ln\lvert x\rvert + 1 & \text{se } x>0 \\
\ln\lvert x\rvert & \text{se } x<0
\end{cases}
$$

**Ambas são primitivas de $\frac1x$ em $D$:** em cada ponto do domínio, somar a constante $1$ (ou $0$) não altera a derivada, que vale $\frac1x$ nos dois casos.

**Mas a diferença não é constante:**

$$
G(x)-F(x) = \begin{cases}
1 & \text{se } x>0 \\
0 & \text{se } x<0
\end{cases}
$$

**Isso contradiz o Teorema 5.1.1?** **Não.** O teorema exige que as funções estejam definidas **num intervalo**, e $\mathbb{R}\setminus\lbrace0\rbrace$ não é um intervalo — é a união de dois intervalos disjuntos, $(-\infty,0)$ e $(0,+\infty)$.

Dentro de **cada** um deles, a diferença **é** constante (vale $1$ num, $0$ no outro), exatamente como o teorema prevê. O que não existe é uma constante **única** servindo para os dois pedaços ao mesmo tempo.

> 💡 **A consequência prática.** Escrever $\int\frac{dx}{x} = \ln\lvert x\rvert + C$ é uma simplificação: rigorosamente, há **duas** constantes independentes, uma de cada lado do zero. Em Cálculo 1 isso quase nunca incomoda, porque os problemas ficam de um lado só. Mas em equações diferenciais a distinção passa a importar — e é bom já saber de onde ela vem.

---

### 21.

$$F(x) = (ax+b)e^x \ \Longrightarrow \ F'(x) = a\thinspace e^x + (ax+b)e^x = e^x\big(ax + a + b\big)$$

Queremos $F'(x) = x\thinspace e^x$, isto é,

$$e^x\big(ax+a+b\big) = e^x\cdot x$$

Como $e^x \neq 0$, podemos cancelá-lo e **igualar os coeficientes** dos polinômios:

$$ax + (a+b) = 1\cdot x + 0$$

Daí $a = 1$ e $a+b = 0$, o que dá $b = -1$.

**Resposta.** $F(x) = (x-1)e^x$, ou seja,

$$\int x\thinspace e^x\thinspace dx = (x-1)e^x + C$$

> 💡 **Você acabou de descobrir, por tentativa estruturada, o resultado que a integração por partes entrega direto.** O método usado aqui — chutar a **forma** da resposta e determinar os coeficientes — chama-se *coeficientes a determinar*, e é a base de boa parte da teoria de equações diferenciais. Em [5.2](../5.2-tecnicas-de-integracao.md) você verá o caminho sistemático.

---

### 22.

Seja $F(x) = \dfrac{x\lvert x\rvert}{2}$. Precisamos mostrar que $F'(x) = \lvert x\rvert$ para **todo** $x\in\mathbb{R}$.

**Caso $x>0$.** Aqui $\lvert x\rvert = x$, então $F(x) = \dfrac{x^2}{2}$ e

$$F'(x) = x = \lvert x\rvert \ \checkmark$$

**Caso $x<0$.** Aqui $\lvert x\rvert = -x$, então $F(x) = \dfrac{x(-x)}{2} = -\dfrac{x^2}{2}$ e

$$F'(x) = -x = \lvert x\rvert \ \checkmark$$

(a última igualdade vale justamente porque $x<0$).

**Caso $x=0$.** As regras acima não se aplicam no ponto de junção — é preciso voltar à **definição** de derivada:

$$F'(0) = \lim_{h\to0}\frac{F(0+h)-F(0)}{h} = \lim_{h\to0}\frac{\frac{h\lvert h\rvert}{2} - 0}{h} = \lim_{h\to0}\frac{\lvert h\rvert}{2} = 0$$

E, de fato, $f(0) = \lvert 0\rvert = 0$ ✔

Como $F'(x) = \lvert x\rvert$ nos três casos, $F$ é primitiva de $\lvert x\rvert$ em todo $\mathbb{R}$ $\blacksquare$

> 💡 **O detalhe bonito desta questão.** A função $\lvert x\rvert$ **não é derivável** em $x=0$ — é o exemplo clássico de bico. Mesmo assim ela **tem** primitiva, e a primitiva é perfeitamente lisa ali.
>
> O padrão é geral: **integrar suaviza, derivar aspereza**. Uma função com bico tem primitiva sem bico; uma função apenas contínua tem primitiva derivável. É a razão de a integral ser uma operação muito mais "bem-comportada" que a derivada — e um dos motivos de ela ser a ferramenta preferida em física e em análise numérica.

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 5.1](../exercicios/lista-5.1-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [5.1 · Teoria](../5.1-primitivas-e-o-conceito-de-integral.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
