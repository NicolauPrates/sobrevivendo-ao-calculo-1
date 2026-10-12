# ✅ Gabarito — Lista 2.5

> **Como usar.** Parte 1: só as respostas. Parte 2: as resoluções completas.

➡️ [Voltar para a Lista 2.5](../exercicios/lista-2.5-propostos.md) · [Teoria 2.5](../2.5-continuidade-e-tipos-de-descontinuidade.md)

---

# ✅ Parte 1 — Respostas finais

### Bloco A · Fixação

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | contínua |
| 1 (b) | descontínua (removível) |
| 1 (c) | contínua |
| 2 (a) | $\mathbb{R}$ |
| 2 (b) | $\mathbb{R}\setminus\lbrace 4 \rbrace$ |
| 2 (c) | $[2,\thinspace +\infty)$ |
| 2 (d) | $(-3,\thinspace +\infty)$ |
| 2 (e) | $x \neq \frac{\pi}{2}+k\pi$ |
| 3 (a) | removível |
| 3 (b) | infinita |
| 3 (c) | de salto |
| 3 (d) | oscilatória |
| 4 (a) | $k = 10$ |
| 4 (b) | $k = -2$ |
| 5 (a) | $4$ |
| 5 (b) | $e$ |
| 5 (c) | $\ln 5$ |
| 5 (d) | $0$ |
| 6 | Demonstração — veja a Parte 2 |
| 7 | (a) V · (b) F · (c) V · (d) F · (e) F |
| 8 | Exemplos — veja a Parte 2 |

### Bloco B · Consolidação

| Ex. | Resposta |
| :---: | --- |
| 9 | $x=2$ removível; $x=3$ infinita |
| 10 | $a=2$ e $b=0$ |
| 11 | $k=3$ |
| 12 | $k=\dfrac14$ |
| 13 | Demonstração — veja a Parte 2 |
| 14 | Demonstração — veja a Parte 2 |
| 15 | Descontínua; descontinuidade **infinita** |
| 16 | $1$ |
| 17 | Contínua em $\mathbb{R}$; bicos em $x=-2$ e $x=2$ |
| 18 | $f$ é contínua; $g$ não é (oscilatória) |

### Bloco C · Desafio

| Ex. | Resposta |
| :---: | --- |
| 19 | Demonstração — veja a Parte 2 |
| 20 | Demonstração — veja a Parte 2 |
| 21 | Não contradiz: $f$ **não é contínua** em $[-1,1]$ |
| 22 | $a = -\dfrac78$ e $b = \dfrac{23}{8}$ |

---
---

# 🧠 Parte 2 — Resoluções completas

## Bloco A · Fixação

### Exercício 1

**(a)** (i) $f(1) = 1$ ✔ &nbsp; (ii) $\lim_{x\to1} x^2 = 1$ ✔ &nbsp; (iii) $1 = 1$ ✔ → **contínua**.

**(b)** (i) $g(1) = 5$ ✔ &nbsp; (ii) $\lim_{x\to1}(x+2) = 3$ ✔ &nbsp; (iii) $3 \neq 5$ ✘ → **descontínua**, com descontinuidade **removível** (bastaria redefinir $g(1)=3$).

**(c)** (i) $h(1) = 2$ ✔ &nbsp; (ii) laterais: $\lim_{x\to1^{-}}(x+1) = 2$ e $\lim_{x\to1^{+}} 2x = 2$ — iguais, logo o limite existe e vale $2$ ✔ &nbsp; (iii) $2 = 2$ ✔ → **contínua**.

---

### Exercício 2

Pelo Teorema 2.5.1, basta determinar o **domínio**:

**(a)** Polinômio: contínua em $\mathbb{R}$.

**(b)** Racional: contínua onde o denominador não zera, $\mathbb{R}\setminus\lbrace 4 \rbrace$.

**(c)** Raiz par: $x-2 \geqslant 0$, logo $[2,+\infty)$.

**(d)** Logaritmo: $x+3>0$, logo $(-3,+\infty)$.

**(e)** $\operatorname{tg} x = \frac{\operatorname{sen} x}{\cos x}$: contínua onde $\cos x \neq 0$, isto é, $x \neq \frac{\pi}{2}+k\pi$, $k\in\mathbb{Z}$.

---

### Exercício 3

**(a)** $\lim_{x\to1}\frac{(x-1)(x+1)}{x-1} = 2$, finito, e $f(1)$ não existe → **removível**.

**(b)** $\lim_{x\to2^{+}}\frac{1}{x-2} = +\infty$ → **infinita**.

**(c)** Laterais $-1$ e $1$ ([2.2](../2.2-limites-laterais.md)), finitos e diferentes → **de salto**.

**(d)** Nenhum dos laterais existe, por oscilação ([2.1](../2.1-conceito-e-nocao-intuitiva-de-limite.md)) → **oscilatória**.

---

### Exercício 4

**(a)** Para $x \neq 5$: $\frac{(x-5)(x+5)}{x-5} = x+5$, cujo limite em $5$ é $10$. A continuidade exige $k = 10$.

**(b)** Laterais: $\lim_{x\to1^{-}}(3x+k) = 3+k$ e $\lim_{x\to1^{+}} x^2 = 1$; o valor é $f(1)=1$. Igualando: $3+k = 1$, logo $k = -2$.

---

### Exercício 5

Em todos, as funções externas são contínuas no ponto, então o limite **entra**:

**(a)** $\sqrt{\lim(x^2+7)} = \sqrt{16} = 4$

**(b)** $e^{\lim \cos x} = e^{\cos 0} = e^1 = e$

**(c)** $\ln\big(\lim(x^2+1)\big) = \ln 5$

**(d)** $\cos\left(\frac{\pi}{2}\right) = 0$

---

### Exercício 6

1. Seja $f(x) = x^3+x-3$. É **polinomial**, logo contínua em $[1,2]$.
2. $f(1) = 1+1-3 = -1 < 0$ e $f(2) = 8+2-3 = 7 > 0$.
3. Sinais opostos ⟹ pelo Corolário de Bolzano, existe $c \in (1,2)$ com $f(c) = 0$. $\blacksquare$

---

### Exercício 7

**(a) Verdadeiro.** É a condição (ii) da definição.

**(b) Falso.** O limite pode existir sem que $f(a)$ exista, ou sendo diferente dele — Exercício 1(b).

**(c) Verdadeiro.** Teorema 2.5.1.

**(d) Falso.** O TVI garante **existência**, não unicidade. Por exemplo, $f(x) = \operatorname{sen} x$ em $[-\pi, \pi]$ tem $f(-\pi)\cdot f(\pi) = 0$... tomando $f(x) = x^3 - x$ em $[-2,2]$: $f(-2) = -6 < 0$, $f(2) = 6 > 0$, e há **três** raízes ($-1$, $0$ e $1$).

**(e) Falso.** Só as **removíveis**. Em um salto, nenhum valor de $f(a)$ satisfaz os dois lados.

---

### Exercício 8

**(a)** $f(x) = \dfrac{x^2-4}{x-2}$ — limite $4$ em $x=2$, mas a função não existe ali.

**(b)** $f(x) = \dfrac{\lvert x\rvert}{x}$ — laterais $-1$ e $1$. (Ou a função maior inteiro em qualquer inteiro.)

**(c)** $f(x) = \lvert x \rvert$ — contínua em $\mathbb{R}$, com bico em $x=0$.

> 💡 O item (c) adianta a Unidade 3: **contínua não significa derivável**. O bico é contínuo e não tem reta tangente.

---

## Bloco B · Consolidação

### Exercício 9

Fatore numerador e denominador:

$$f(x) = \frac{(x-2)(x+2)}{(x-2)(x-3)} = \frac{x+2}{x-3} \qquad (x \neq 2)$$

**Em $x=2$** (fator cancelado): o limite vale

$$\lim_{x\to2}\frac{x+2}{x-3} = \frac{4}{-1} = -4$$

finito, e a função não existe ali → **removível**.

**Em $x=3$:** o denominador zera e o numerador vale $5 \neq 0$ → laterais $\pm\infty$ → **infinita** (assíntota vertical $x=3$).

Em todos os demais pontos, $f$ é contínua.

---

### Exercício 10

Cada ramo é contínuo; só as **trocas** importam.

**Em $x=2$:** $f(2) = 4$ (primeira linha) e $\lim_{x\to2^{+}}(ax+b) = 2a+b$. Logo

$$2a+b = 4$$

**Em $x=5$:** $f(5) = 10$ (terceira linha) e $\lim_{x\to5^{-}}(ax+b) = 5a+b$. Logo

$$5a+b = 10$$

Subtraindo: $3a = 6 \Rightarrow a = 2$, e então $b = 4 - 4 = 0$.

**Resposta.** $a=2$ e $b=0$.

*Conferência:* o ramo do meio vira $2x$; em $x=2$ dá $4$ ✔ e em $x=5$ dá $10$ ✔.

---

### Exercício 11

$$\lim_{x\to0}\frac{\operatorname{sen} 3x}{x} = \lim_{x\to0} 3\cdot\frac{\operatorname{sen} 3x}{3x} = 3$$

A continuidade exige $k = 3$.

---

### Exercício 12

Racionalizando:

$$\frac{\sqrt{x+4}-2}{x} = \frac{(x+4)-4}{x\big(\sqrt{x+4}+2\big)} = \frac{1}{\sqrt{x+4}+2} \ \longrightarrow \ \frac{1}{4}$$

Logo $k = \dfrac14$.

---

### Exercício 13

Seja $f(x) = x^4-3x+1$, contínua em $\mathbb{R}$ por ser polinomial. Teste alguns valores:

$$f(0) = 1 > 0 \qquad f(1) = 1-3+1 = -1 < 0 \qquad f(2) = 16-6+1 = 11 > 0$$

- Entre $0$ e $1$ há troca de sinal ⟹ existe raiz em $(0,1)$.
- Entre $1$ e $2$ há outra troca ⟹ existe raiz em $(1,2)$.

Como os intervalos são disjuntos, as raízes são **distintas**: $f$ tem pelo menos duas raízes reais. $\blacksquare$

---

### Exercício 14

**Raiz.** $f(1) = 3 > 0$ e $f(4) = -2 < 0$: sinais opostos. Como $f$ é contínua em $[1,4]$, o Corolário de Bolzano garante $c \in (1,4)$ com $f(c)=0$.

**Valor $1$.** O número $N=1$ está **entre** $f(4) = -2$ e $f(1) = 3$. Pelo TVI, existe $d \in (1,4)$ com $f(d) = 1$. $\blacksquare$

> 💡 O TVI não exige que $N$ seja zero nem que $f(a) < f(b)$: basta $N$ estar **entre** os dois valores das pontas, em qualquer ordem.

---

### Exercício 15

**(i)** $f(0) = 0+1 = 1$ — existe ✔

**(ii)** Os laterais:

$$\lim_{x\to0^{-}}(x+1) = 1 \qquad \lim_{x\to0^{+}}\frac1x = +\infty$$

O limite **não existe** ✘

**Resposta.** $f$ é **descontínua** em $x=0$, e a descontinuidade é **infinita** — um dos laterais explode. (A reta $x=0$ é assíntota vertical pela direita.)

---

### Exercício 16

A função $\operatorname{sen}$ é contínua em $\mathbb{R}$, e $\frac{\pi}{2}\cos x$ é contínua. Logo o limite entra (Teorema 2.5.3):

$$\lim_{x\to0}\operatorname{sen}\left(\frac{\pi}{2}\cos x\right) = \operatorname{sen}\left(\frac{\pi}{2}\lim_{x\to0}\cos x\right) = \operatorname{sen}\left(\frac{\pi}{2}\cdot 1\right) = \operatorname{sen}\frac{\pi}{2} = 1$$

---

### Exercício 17

**Continuidade.** $f(x) = \lvert x^2-4\rvert$ é a composta de $u \mapsto \lvert u\rvert$ (contínua em $\mathbb{R}$) com $x \mapsto x^2-4$ (polinômio). Pelo Teorema 2.5.3, $f$ é **contínua em $\mathbb{R}$**.

**Bicos.** O rebatimento do módulo cria quinas exatamente onde a função interna **troca de sinal**, ou seja, onde $x^2-4=0$:

$$x = -2 \qquad \text{e} \qquad x = 2$$

> 💡 Nesses pontos $f$ é contínua e **não derivável** — assunto de [3.1](../../03-derivadas/3.1-conceito-interpretacao-geometrica-e-regras-basicas.md). A regra geral: $\lvert g(x)\rvert$ ganha um bico em cada raiz **simples** de $g$.

---

### Exercício 18

**Para $f$:**

(i) $f(0) = 0$ ✔ &nbsp; (ii) pelo anulamento, $\lim_{x\to0} x\operatorname{sen}\frac1x = 0$ ✔ &nbsp; (iii) $0=0$ ✔

**$f$ é contínua em $x=0$.**

**Para $g$:**

(i) $g(0) = 0$ ✔ &nbsp; (ii) $\lim_{x\to0}\operatorname{sen}\frac1x$ **não existe** ✘

**$g$ é descontínua**, com descontinuidade **oscilatória** — e nenhum valor atribuído a $g(0)$ conserta isso.

> 💡 A diferença é o fator $x$: ele esmaga a oscilação contra o zero. Sem ele, a oscilação continua com amplitude $1$ por mais perto da origem que se chegue.

---

## Bloco C · Desafio

### Exercício 19

Seja $p(x) = a_n x^n + \cdots + a_0$ com $n$ **ímpar** e $a_n \neq 0$. Suponha, sem perda de generalidade, $a_n > 0$ (se for negativo, aplique o argumento a $-p$, que tem as mesmas raízes).

**Comportamento nos extremos.** No infinito, o termo dominante manda ([2.4](../2.4-limites-infinitos-no-infinito-e-assintotas.md)). Como $n$ é ímpar:

$$\lim_{x\to+\infty} p(x) = +\infty \qquad \lim_{x\to-\infty} p(x) = -\infty$$

**Escolhendo as pontas.** Dos limites segue que existe $b$ grande com $p(b) > 0$, e existe $a$ muito negativo com $p(a) < 0$.

**Aplicando Bolzano.** $p$ é contínua em $[a,b]$ (é polinômio) e $p(a)\cdot p(b) < 0$. Logo existe $c \in (a,b)$ com $p(c) = 0$. $\blacksquare$

> 💡 **É por isso que toda equação de grau ímpar tem solução real**, enquanto $x^2+1=0$ (grau par) não tem. Com $n$ par, os dois extremos vão para o **mesmo** infinito, e a curva pode nunca cruzar o eixo.

---

### Exercício 20

**Estratégia.** Transformar "$f(c) = f(c+1)$" em "raiz de alguma função".

**Solução.** Defina, para $x \in [0,1]$,

$$g(x) = f(x+1) - f(x)$$

Ela é contínua em $[0,1]$, por ser diferença de funções contínuas (note que $x+1$ percorre $[1,2]$, dentro do domínio de $f$).

**Nas extremidades:**

$$g(0) = f(1)-f(0) \qquad g(1) = f(2)-f(1) = f(0)-f(1) = -g(0)$$

(na penúltima igualdade usou-se a hipótese $f(2)=f(0)$).

**Dois casos:**

- Se $g(0)=0$, então $f(1)=f(0)$ e $c=0$ serve.
- Se $g(0) \neq 0$, então $g(0)$ e $g(1) = -g(0)$ têm **sinais opostos**. Por Bolzano, existe $c \in (0,1)$ com $g(c)=0$, isto é, $f(c+1) = f(c)$. $\blacksquare$

> 💡 **Tradução:** se você sai de um ponto e volta a ele depois de duas horas de caminhada, existe algum instante $c$ tal que a sua posição em $c$ e em $c+1$ hora era a mesma. O resultado é conhecido como "teorema do alpinista".

---

### Exercício 21

**Não há contradição.** O TVI exige que $f$ seja **contínua em todo o intervalo** $[-1,1]$ — e essa função **não é**: em $x=0$ ela dá um salto de $-1$ para $1$.

$$\lim_{x\to0^{-}} f(x) = -1 \qquad \lim_{x\to0^{+}} f(x) = 1$$

A hipótese do teorema falha, logo a conclusão não precisa valer. O exemplo mostra exatamente **por que** a hipótese está lá: é a continuidade que impede a curva de "pular por cima" do eixo.

> ⚠️ Em prova, ao aplicar o TVI, **declare a continuidade explicitamente** — é a parte da resposta que vale ponto. Testar os sinais sem justificar a continuidade é a mesma falha deste exercício, do avesso.

---

### Exercício 22

Os ramos são contínuos no interior de cada faixa; os pontos a verificar são $x=1$ e $x=3$.

**Em $x=1$.** Pela esquerda, para $x<1$:

$$\lim_{x\to1^{-}}\frac{x^2-1}{x-1} = \lim_{x\to1^{-}}(x+1) = 2$$

E $f(1) = a+b$ (segunda linha, que inclui $x=1$). Logo

$$a+b = 2$$

**Em $x=3$.** O valor é $f(3) = 3a+b$ (a segunda linha inclui $x=3$). Pela direita, para $x>3$, racionalize:

$$\frac{\sqrt{x+1}-2}{x-3} = \frac{(x+1)-4}{(x-3)\big(\sqrt{x+1}+2\big)} = \frac{1}{\sqrt{x+1}+2} \ \longrightarrow \ \frac{1}{4}$$

Logo

$$3a+b = \frac14$$

**Resolvendo o sistema.** Subtraindo a primeira equação da segunda:

$$2a = \frac14 - 2 = -\frac74 \ \Longrightarrow \ a = -\frac78$$

$$b = 2 - a = 2 + \frac78 = \frac{23}{8}$$

**Resposta.** $a = -\dfrac78$ e $b = \dfrac{23}{8}$.

*Conferência:* $3a+b = -\dfrac{21}{8} + \dfrac{23}{8} = \dfrac{2}{8} = \dfrac14$ ✔

---

| ← Lista | 🏠 Índice | Teoria |
| :--- | :---: | ---: |
| [Lista 2.5](../exercicios/lista-2.5-propostos.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [2.5 · Teoria](../2.5-continuidade-e-tipos-de-descontinuidade.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
