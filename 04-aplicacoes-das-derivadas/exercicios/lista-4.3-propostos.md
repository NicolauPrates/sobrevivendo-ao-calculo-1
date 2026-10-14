# 📝 Lista 4.3 — Regra de L&#39;Hôspital

> **Antes de começar:** leia a [teoria 4.3](../4.3-regra-de-lhospital.md).

**A regra de ouro:** substitua **primeiro**. Se não der $\frac00$ nem $\frac{\infty}{\infty}$, L&#39;Hôspital está proibida.

| Bloco | Exercícios | Quanto fazer |
| --- | :---: | --- |
| **A · Fixação** | 1 a 8 | Todos |
| **B · Consolidação** | 9 a 16 | Todos |
| **C · Desafio** | 17 a 20 | Os que der |

---

## Bloco A · Fixação

**1.** Calcule (forma $\frac00$):

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to0}\dfrac{\mathrm{sen}\thinspace x}{x}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to0}\dfrac{e^x-1}{x}$

&nbsp;&nbsp;**(c)** $\lim\limits_{x\to1}\dfrac{\ln x}{x-1}$ &nbsp;&nbsp;&nbsp; **(d)** $\lim\limits_{x\to0}\dfrac{1-\cos x}{x}$

**2.** Calcule (forma $\frac{\infty}{\infty}$):

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to+\infty}\dfrac{\ln x}{x^2}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to+\infty}\dfrac{x}{e^x}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x\to+\infty}\dfrac{3x^2+1}{2x^2-x}$

**3.** Em cada caso, diga se L&#39;Hôspital **se aplica** e justifique. Depois calcule o limite (pelo método correto):

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to0}\dfrac{x+2}{x+1}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to2}\dfrac{x^2-4}{x-2}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x\to0^{+}}\dfrac{\mathrm{sen}\thinspace x}{x^2}$

**4.** Calcule (precisa de **duas** aplicações):

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to0}\dfrac{e^x-1-x}{x^2}$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to0}\dfrac{x-\mathrm{sen}\thinspace x}{x^3}$

**5.** Calcule (forma $0\cdot\infty$):

&nbsp;&nbsp;**(a)** $\lim\limits_{x\to0^{+}} x\ln x$ &nbsp;&nbsp;&nbsp; **(b)** $\lim\limits_{x\to+\infty} x\thinspace e^{-x}$ &nbsp;&nbsp;&nbsp; **(c)** $\lim\limits_{x\to0^{+}} x^2\ln x$

**6.** Calcule (forma $\infty-\infty$): $\lim\limits_{x\to1}\left(\dfrac{1}{\ln x} - \dfrac{1}{x-1}\right)$

**7.** Calcule (forma $1^{\infty}$): $\lim\limits_{x\to+\infty}\left(1+\dfrac2x\right)^x$

**8.** Verdadeiro ou falso? Justifique.

&nbsp;&nbsp;**(a)** A Regra de L&#39;Hôspital vale para qualquer limite de quociente.

&nbsp;&nbsp;**(b)** Na regra, deriva-se o numerador e o denominador **separadamente**.

&nbsp;&nbsp;**(c)** Se $\lim\frac{f'}{g'}$ não existe, então $\lim\frac fg$ também não existe.

&nbsp;&nbsp;**(d)** $0^0 = 1$, sempre.

---

## Bloco B · Consolidação

**9.** $\lim\limits_{x\to0}\dfrac{\mathrm{tg}\thinspace x - x}{x^3}$

**10.** $\lim\limits_{x\to+\infty}\dfrac{(\ln x)^2}{x}$

**11.** $\lim\limits_{x\to0^{+}} \mathrm{sen}\thinspace x\cdot\ln x$

**12.** $\lim\limits_{x\to0}\left(\dfrac1x - \dfrac{1}{e^x-1}\right)$

**13.** $\lim\limits_{x\to+\infty}\left(1-\dfrac3x\right)^x$

**14.** $\lim\limits_{x\to0}\big(\cos x\big)^{1/x^2}$

**15.** $\lim\limits_{x\to+\infty} x\left(e^{1/x}-1\right)$

**16.** Determine $a$ para que $\lim\limits_{x\to0}\dfrac{\mathrm{sen}(ax) - 2x}{x^3}$ seja **finito**, e calcule o limite nesse caso.

---

## Bloco C · Desafio

**17.** Mostre que $\lim\limits_{x\to+\infty}\dfrac{x^n}{e^x} = 0$ para todo inteiro $n \geqslant 1$.

&nbsp;&nbsp;*(Sugestão: aplique a regra $n$ vezes e descreva o que acontece com o numerador.)*

**18.** $\lim\limits_{x\to0^{+}}\left(\dfrac1x\right)^{\mathrm{sen}\thinspace x}$

**19.** Explique por que **não** se pode concluir nada aplicando L&#39;Hôspital a

$$\lim_{x\to+\infty}\frac{x+\mathrm{sen}\thinspace x}{x}$$

&nbsp;&nbsp;e calcule o limite por outro método.

**20.** Mostre que $\lim\limits_{x\to0^{+}} x^{\alpha}\ln x = 0$ para todo $\alpha>0$.

---

## ✅ Conferir

➡️ **[Gabarito da Lista 4.3](../gabaritos/gabarito-4.3.md)**

---

| ← Lista anterior | 🏠 Índice | Próxima lista → |
| :--- | :---: | ---: |
| [Lista 4.2](lista-4.2-propostos.md) | [Exercícios da unidade](README.md) · [Página inicial](../../README.md) | [Lista 4.4](lista-4.4-propostos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
