# ✅ Gabarito — Revisão da Unidade 2

> **Corrija com honestidade.** Para cada questão errada, classifique a causa: não sabia a teoria, sabia e errei a montagem, montei certo e errei a conta, ou acabou o tempo. Cada uma pede um remédio diferente.

➡️ [Voltar para a Revisão](../exercicios/revisao-unidade-2.md)

---

# ✅ Parte 1 — Respostas finais

| Questão | Resposta |
| :---: | --- |
| 1 (a) | $\dfrac65$ |
| 1 (b) | $\dfrac12$ |
| 1 (c) | $3$ |
| 2 (a) | $2$ pela esquerda, $3$ pela direita |
| 2 (b) | Não existe |
| 2 (c) | Descontínua; descontinuidade **de salto** |
| 3 | $-4$ pela esquerda, $4$ pela direita; o limite bilateral não existe |
| 4 (a) | $0$ |
| 4 (b) | $2$ |
| 5 (a) | $\dfrac52$ |
| 5 (b) | $\dfrac92$ |
| 5 (c) | $\dfrac23$ |
| 6 (a) | $\dfrac35$ |
| 6 (b) | $-3$ |
| 6 (c) | $2$ |
| 7 | Vertical $x=2$; horizontal $y=2$; em $x=-1$ há um **furo**, não assíntota |
| 8 | $x=3$ removível; $x=-3$ infinita |
| 9 | $a = \dfrac23$ e $b = \dfrac83$ |
| 10 | Demonstração — veja a Parte 2 |
| 11 (a) | $\lim = 2$ e $f(1) = 3$ |
| 11 (b) | Descontínua; **removível** |
| 11 (c) | Redefinindo $f(1) = 2$ |
| 12 | $D = \mathbb{R}\setminus\lbrace -2,\thinspace 2 \rbrace$; $f(x) = \frac{x+1}{x+2}$; vertical $x=-2$, horizontal $y=1$; furo em $x=2$ |

---
---

# 🧠 Parte 2 — Resoluções completas

### Questão 1

**(a)** Substituindo dá $\frac00$. Fatore os dois lados:

$$\frac{x^2-9}{x^2-x-6} = \frac{(x-3)(x+3)}{(x-3)(x+2)} = \frac{x+3}{x+2} \ \longrightarrow \ \frac{6}{5}$$

**(b)** Racionalize o numerador:

$$\frac{\sqrt{x+1}-1}{x}\cdot\frac{\sqrt{x+1}+1}{\sqrt{x+1}+1} = \frac{(x+1)-1}{x\big(\sqrt{x+1}+1\big)} = \frac{1}{\sqrt{x+1}+1} \ \longrightarrow \ \frac12$$

**(c)** Diferença de cubos no numerador:

$$\frac{x^3-8}{x^2-4} = \frac{(x-2)\big(x^2+2x+4\big)}{(x-2)(x+2)} = \frac{x^2+2x+4}{x+2} \ \longrightarrow \ \frac{4+4+4}{4} = 3$$

---

### Questão 2

**(a)**

$$\lim_{x\to1^{-}} f(x) = \lim_{x\to1^{-}}\big(x^2+1\big) = 2$$
$$\lim_{x\to1^{+}} f(x) = \lim_{x\to1^{+}}\big(4-x^2\big) = 3$$

**(b)** **Não existe**: os laterais existem, mas são diferentes ($2 \neq 3$).

**(c)** **Não é contínua** — falha já a condição (ii) da definição. Como os dois laterais são finitos e diferentes, a descontinuidade é **de salto** (de altura $1$).

> ⚠️ O valor $f(1)=3$ não ajuda em nada: nenhum valor atribuído ao ponto conserta um salto.

---

### Questão 3

Fatore o numerador: $x^2-4 = (x-2)(x+2)$.

**Pela esquerda** ($x<2$, logo $\lvert x-2\rvert = -(x-2)$):

$$\frac{(x-2)(x+2)}{-(x-2)} = -(x+2) \ \longrightarrow \ -4$$

**Pela direita** ($x>2$, logo $\lvert x-2\rvert = x-2$):

$$\frac{(x-2)(x+2)}{x-2} = x+2 \ \longrightarrow \ 4$$

Como $-4 \neq 4$, **o limite bilateral não existe**.

---

### Questão 4

**(a)** A função $\cos\frac{1}{x^2}$ é **limitada** ($\lvert\cos u\rvert \leqslant 1$) e $x^3 \to 0$. Pelo **teorema do anulamento**:

$$\lim_{x\to0} x^3\cos\frac{1}{x^2} = 0$$

*(Pelo confronto: $-\lvert x\rvert^3 \leqslant x^3\cos\frac{1}{x^2} \leqslant \lvert x\rvert^3$, e as duas pontas tendem a $0$.)*

**(b)** As funções que prendem $f$ são polinômios:

$$\lim_{x\to1} 2x = 2 \qquad \lim_{x\to1}\big(x^2+1\big) = 2$$

As pontas tendem ao mesmo valor. Pelo **Teorema do Confronto**, $\lim_{x\to1} f(x) = 2$.

---

### Questão 5

**(a)** Prepare as duas frações:

$$\frac{\mathrm{sen}\thinspace 5x}{\mathrm{sen}\thinspace 2x} = \frac{\mathrm{sen}\thinspace 5x}{5x}\cdot\frac{2x}{\mathrm{sen}\thinspace 2x}\cdot\frac{5}{2} \ \longrightarrow \ 1\cdot1\cdot\frac52 = \frac52$$

**(b)** Ajuste o argumento, multiplicando e dividindo por $9$:

$$\frac{1-\cos 3x}{x^2} = 9\cdot\frac{1-\cos 3x}{(3x)^2} \ \longrightarrow \ 9\cdot\frac12 = \frac92$$

*(usando $\lim_{u\to0}\frac{1-\cos u}{u^2} = \frac12$)*

**(c)**

$$\frac{\mathrm{tg}\thinspace 2x}{3x} = \frac{\mathrm{sen}\thinspace 2x}{3x\cos 2x} = \frac23\cdot\frac{\mathrm{sen}\thinspace 2x}{2x}\cdot\frac{1}{\cos 2x} \ \longrightarrow \ \frac23 \cdot 1 \cdot 1 = \frac23$$

---

### Questão 6

**(a)** Graus iguais. Dividindo por $x^2$:

$$\frac{3-\frac1x}{5+\frac{2}{x^2}} \ \longrightarrow \ \frac35$$

**(b)** Atenção ao sinal: com $x\to-\infty$, $\sqrt{9x^2+1} = \lvert x\rvert\sqrt{9+\frac{1}{x^2}} = -x\sqrt{9+\frac{1}{x^2}}$.

$$\frac{-x\sqrt{9+\frac{1}{x^2}}}{x+2} = \frac{-\sqrt{9+\frac{1}{x^2}}}{1+\frac2x} \ \longrightarrow \ \frac{-3}{1} = -3$$

*Confirmação de sinal:* a raiz é positiva e $x+2$ é negativo para $x\to-\infty$ — a resposta **tem** de ser negativa ✔

**(c)** Forma $\infty-\infty$: conjugado.

$$\sqrt{x^2+4x}-x = \frac{4x}{\sqrt{x^2+4x}+x} = \frac{4}{\sqrt{1+\frac4x}+1} \ \longrightarrow \ \frac{4}{2} = 2$$

---

### Questão 7

**Simplifique primeiro:**

$$f(x) = \frac{2\big(x^2-1\big)}{(x-2)(x+1)} = \frac{2(x-1)(x+1)}{(x-2)(x+1)} = \frac{2(x-1)}{x-2} \qquad (x \neq -1)$$

**Assíntota vertical.** Depois da simplificação, o denominador zera só em $x=2$, e ali o numerador vale $2 \neq 0$:

$$\lim_{x\to2^{+}} f(x) = \frac{2}{0^{+}} = +\infty \qquad \lim_{x\to2^{-}} f(x) = \frac{2}{0^{-}} = -\infty$$

**Assíntota vertical: $x=2$.**

**Assíntota horizontal.** Na forma simplificada, graus iguais:

$$\lim_{x\to\pm\infty}\frac{2x-2}{x-2} = 2$$

**Assíntota horizontal: $y=2$**, nos dois extremos.

**No ponto $x=-1$:** o fator cancelou. Não é assíntota, e sim um **furo** — o limite existe:

$$\lim_{x\to-1}\frac{2(x-1)}{x-2} = \frac{2(-2)}{-3} = \frac43$$

A descontinuidade ali é **removível**.

---

### Questão 8

$$f(x) = \frac{x-3}{x^2-9} = \frac{x-3}{(x-3)(x+3)} = \frac{1}{x+3} \qquad (x \neq 3)$$

**Em $x=3$:** o fator cancelou, e o limite é finito:

$$\lim_{x\to3}\frac{1}{x+3} = \frac16$$

→ descontinuidade **removível**.

**Em $x=-3$:** o denominador zera e o numerador simplificado vale $1$:

$$\lim_{x\to-3^{+}}\frac{1}{x+3} = +\infty \qquad \lim_{x\to-3^{-}}\frac{1}{x+3} = -\infty$$

→ descontinuidade **infinita** (assíntota vertical $x=-3$).

---

### Questão 9

Cada ramo é contínuo no seu interior; verifique as **trocas**.

**Em $x=2$.** Pela esquerda, $\frac{x^2-4}{x-2} = x+2 \to 4$. O valor é $f(2) = 2a+b$ (segunda linha). Logo

$$2a+b = 4$$

**Em $x=5$.** Pela esquerda, $5a+b$. O valor é $f(5) = 6$ (terceira linha). Logo

$$5a+b = 6$$

**Sistema.** Subtraindo: $3a = 2 \Rightarrow a = \dfrac23$, e então

$$b = 4 - 2\cdot\frac23 = 4 - \frac43 = \frac83$$

**Resposta.** $a = \dfrac23$ e $b = \dfrac83$.

*Conferência:* $5\cdot\frac23 + \frac83 = \frac{10}{3}+\frac83 = \frac{18}{3} = 6$ ✔

---

### Questão 10

1. Seja $f(x) = x - \cos 2x$. É diferença de funções contínuas em $\mathbb{R}$, logo **contínua** em $\left[0,\frac\pi4\right]$.
2. Nas extremidades:
   $$f(0) = 0 - \cos 0 = -1 < 0$$
   $$f\left(\frac{\pi}{4}\right) = \frac{\pi}{4} - \cos\frac{\pi}{2} = \frac{\pi}{4} - 0 \approx 0{,}785 > 0$$
3. Sinais opostos ⟹ pelo Corolário de Bolzano, existe $c \in \left(0,\frac\pi4\right)$ com $f(c)=0$, isto é, $c = \cos 2c$. $\blacksquare$

---

### Questão 11

**(a)** Para $x \neq 1$, $\frac{x^2-1}{x-1} = x+1$, logo

$$\lim_{x\to1} f(x) = 2 \qquad\qquad f(1) = 3$$

**(b)** As condições (i) e (ii) valem, mas (iii) falha: $2 \neq 3$. **Descontínua**, com descontinuidade **removível**.

**(c)** Redefinindo $f(1) = 2$, as três condições passam a valer e $f$ fica contínua. Geometricamente: o ponto solto em $(1,3)$ desce para tapar o furo em $(1,2)$.

---

### Questão 12 — síntese

**(a) Domínio.** $x^2-4 = 0$ em $x = \pm2$:

$$D(f) = \mathbb{R}\setminus\lbrace -2,\thinspace 2 \rbrace$$

**(b) Simplificação.** Fatorando: $x^2-x-2 = (x-2)(x+1)$ e $x^2-4 = (x-2)(x+2)$:

$$f(x) = \frac{(x-2)(x+1)}{(x-2)(x+2)} = \frac{x+1}{x+2} \qquad \textbf{para } x \neq 2$$

**(c) Assíntotas.**

- **Vertical:** na forma simplificada, o denominador zera em $x=-2$, e o numerador vale $-1 \neq 0$:
  $$\lim_{x\to-2^{+}}\frac{x+1}{x+2} = \frac{-1}{0^{+}} = -\infty \qquad \lim_{x\to-2^{-}} = \frac{-1}{0^{-}} = +\infty$$
  **Assíntota: $x=-2$.**
- **Horizontal:** graus iguais, razão dos líderes $1$:
  $$\lim_{x\to\pm\infty}\frac{x+1}{x+2} = 1$$
  **Assíntota: $y=1$.**
- **Oblíqua:** não há (já existe horizontal).

**(d) Descontinuidades.**

- Em $x=2$: **removível** — o limite existe e vale $\frac{2+1}{2+2} = \frac34$.
- Em $x=-2$: **infinita**.

**(e) Esboço.** O gráfico é o de $\frac{x+1}{x+2} = 1 - \frac{1}{x+2}$, isto é, a hipérbole $-\frac1x$ deslocada $2$ para a esquerda e $1$ para cima:

- dois ramos, separados pela assíntota $x=-2$;
- aproximando-se de $y=1$ nos dois extremos;
- cortando o eixo $x$ em $x=-1$ e o eixo $y$ em $y=\frac12$;
- com um **furo** no ponto $\left(2,\thinspace \frac34\right)$.

> 💡 A reescrita $\frac{x+1}{x+2} = 1 - \frac{1}{x+2}$ é a mesma técnica de [1.3](../../01-funcoes/1.3-funcoes-elementares-paridade-e-graficos.md): dividir para revelar a transformação escondida. Ela entrega as duas assíntotas de graça.

---

## 🎓 Fim da Unidade 2

Se você chegou até aqui resolvendo, está pronto para derivadas. O que a Unidade 3 vai cobrar desta aqui:

- **a derivada é um limite** — o quociente de Newton de [1.2](../../01-funcoes/1.2-funcoes-dominio-contradominio-imagem.md) agora com $h \to 0$;
- **os limites trigonométricos** de [2.3](../2.3-teorema-do-sanduiche.md), que produzem as derivadas do seno e do cosseno;
- **continuidade**, porque "derivável ⟹ contínua" (e a recíproca é falsa — lembre do bico de $\lvert x\rvert$);
- **assíntotas**, que voltam no esboço de gráficos de [4.4](../../04-aplicacoes-das-derivadas/4.4-crescimento-concavidade-e-esboco-de-graficos.md).

➡️ **[Unidade 3 · Derivadas: conceito e regras](../../03-derivadas/README.md)**

---

| ← Revisão | 🏠 Índice | Próxima unidade → |
| :--- | :---: | ---: |
| [Revisão da Unidade 2](../exercicios/revisao-unidade-2.md) | [Gabaritos da unidade](README.md) · [Página inicial](../../README.md) | [Unidade 3](../../03-derivadas/README.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
