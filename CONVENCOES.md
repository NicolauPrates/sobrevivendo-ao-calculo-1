# Convenções de escrita

Este arquivo é o padrão editorial do repositório. Ele existe por um motivo prático: um material de centenas de páginas, escrito ao longo de meses, precisa parecer **um único livro** — e não uma colagem de anotações. Quem for escrever ou revisar qualquer página deve seguir o que está aqui.

> **Autor e mantenedor:** Nicolau Prates

---

## 1. Idioma e tom

- **Português do Brasil**, norma padrão. Sem gírias, sem emojis no corpo do texto (eles só aparecem nos marcadores de seção definidos na §4).
- Tom **didático e formal acadêmico**: o rigor é o dos livros de referência; a clareza é a de quem explica para um colega na véspera.
- **Trate o aluno por "você"**, nunca por "o aluno" ou "o leitor". O material fala com uma pessoa.
- Primeira pessoa do plural é permitida no desenvolvimento matemático, como nos livros: *"derivamos ambos os lados"*, *"obtemos"*, *"note que"*.
- **Explique antes de formalizar.** A ordem é sempre: motivação em uma frase → definição formal → intuição → exemplo. Nunca comece uma seção pela definição seca.
- **Nunca escreva "é óbvio", "é trivial" ou "basta ver que".** Se é óbvio, não precisa estar escrito; se precisa estar escrito, não é óbvio. Essas três expressões são a forma mais eficiente de fazer um aluno desistir da página.
- Terminologia **fixa** (escolha uma e nunca alterne):

| Use | Não use |
| --- | --- |
| função **crescente** / **decrescente** | "subindo", "descendo" |
| **concavidade para cima / para baixo** | "côncava", "convexa" |
| **ponto crítico** | "ponto singular" |
| **assíntota vertical / horizontal** | "assíntota em $x$", "limite infinito da reta" |
| **primitiva** (e "integral indefinida" como sinônimo, declarado uma vez) | "antiderivada" sem apresentar o termo |
| **Teorema do Confronto** (com "do Sanduíche" entre parênteses na primeira menção) | alternar os dois nomes ao longo do texto |
| **Regra de L&#39;Hôspital** | "L&#39;Hopital", "LHospital", "Lhôpital" |

---

## 2. Estrutura de arquivos e nomes

```text
<NN>-<nome-da-unidade>/
├── README.md                       índice da unidade
├── <N.M>-<titulo-em-kebab-case>.md teoria
├── exercicios/
│   ├── README.md
│   ├── lista-<N.M>-propostos.md
│   └── revisao-unidade-<N>.md
└── gabaritos/
    ├── README.md
    ├── gabarito-<N.M>.md
    └── gabarito-revisao-unidade-<N>.md
```

Regras de nome de arquivo:

- **minúsculas, sem acento, sem cedilha, palavras separadas por hífen** (`kebab-case`). `3.3-regra-da-cadeia-e-derivada-da-funcao-inversa.md`, nunca `3.3 Regra da Cadeia.md`.
- O **número do tópico vem primeiro** e é igual ao da ementa. Isso garante a ordenação correta na listagem do GitHub.
- Imagens: `assets/img/<pasta-da-unidade>/<N.M>-<descricao-curta>.svg`, por exemplo `assets/img/01-funcoes/1.3-paridade-x3-3x.svg`.
- Scripts de gráfico: `extras/scripts-graficos/u<N>_<assunto>.py`.

---

## 3. Anatomia padrão de uma página de teoria

Toda página `N.M-*.md` tem estas seções, **nesta ordem**. Seções que não se aplicam ao tópico são omitidas; nenhuma é reordenada.

| # | Seção | Conteúdo |
| :---: | --- | --- |
| 1 | Título `#` | `# N.M · Título do tópico` |
| 2 | 🎯 **O que você vai aprender** | 3 a 5 bullets, cada um começando por verbo no infinitivo |
| 3 | **Pré-requisitos** | Links para as páginas anteriores e para a seção específica do pré-cálculo |
| 4 | **Por que isso importa** | Um parágrafo. Onde o conceito reaparece no curso e para que ele serve |
| 5 | Teoria | Subseções `##`, alternando 📐 definição → 💡 intuição → ✍️ exemplo |
| 6 | 📊 Gráficos | Imagens de `assets/img/`, sempre com uma frase dizendo **o que olhar** na figura |
| 7 | ⚠️ **Armadilhas** | O erro típico de prova, o motivo dele e a forma correta, lado a lado |
| 8 | 🧠 **Exercícios resolvidos** | 3 a 6, acima do nível dos exemplos, com a estratégia explicitada antes da conta |
| 9 | 📝 **Agora é com você** | Link para a lista de propostos e para o gabarito |
| 10 | **Resumo da página** | Caixa com o essencial: o que decorar, o que saber deduzir |
| 11 | 📚 **Para aprofundar** | Capítulo/seção correspondente nos livros da bibliografia |
| 12 | Navegação + assinatura | Rodapé padrão da §7 |

### Blocos matemáticos

Definições, teoremas e propriedades vão em **citação** (`>`), com rótulo em negrito e numeração dentro da página:

```markdown
> 📐 **Definição 1.2 (Função).** Sejam $A$ e $B$ conjuntos não vazios. Uma função
> de $A$ em $B$ é uma regra que associa a **cada** elemento $x \in A$ **um único**
> elemento $y \in B$.
```

Numeração: `Definição N.M.k`, `Teorema N.M.k`, `Propriedade N.M.k`, reiniciando em cada página (`k = 1, 2, 3...`). Exemplos e exercícios usam numeração simples e independente: **Exemplo 1**, **Exemplo 2**, …; **Exercício Resolvido 1**, …

### Exemplos resolvidos

Formato obrigatório, em três partes:

```markdown
#### ✍️ Exemplo 3 — enunciado curto do que se pede

**Estratégia.** Uma frase dizendo qual caminho será seguido e por quê.

**Solução.**

1. Primeiro passo, com a justificativa da passagem.
   $$ \ldots $$
2. Segundo passo.

**Resposta.** $\;\boxed{\text{resultado}}$

> 💡 **Por que funcionou:** o que generalizar deste exemplo.
```

Nunca "pule conta". Se uma passagem usa fatoração, produto notável ou identidade trigonométrica, ela aparece explicitamente ou é citada pelo nome.

---

## 4. Marcadores de seção

Os ícones são **semânticos**, não decorativos. Cada um tem um único uso:

| Ícone | Uso exclusivo |
| :---: | --- |
| 🎯 | Objetivos de aprendizagem (seção 2 da anatomia) |
| 📐 | Definição, teorema, corolário ou propriedade formal |
| 💡 | Intuição, interpretação, "por que funcionou" |
| 📊 | Gráfico, figura ou tabela de valores |
| ✍️ | Exemplo resolvido |
| ⚠️ | Armadilha, erro clássico de prova |
| 🧠 | Exercício resolvido |
| 📝 | Exercícios propostos |
| ✅ | Gabarito, respostas |
| 📚 | Referência bibliográfica |
| ⭐ | Conteúdo de nivelamento (pré-cálculo) ou material-chave de revisão |

### Alertas nativos do GitHub

Use com parcimônia — no máximo dois por página, ou eles perdem o efeito:

| Sintaxe | Quando |
| --- | --- |
| `> [!NOTE]` | Observação lateral, convenção de notação, aviso de escopo |
| `> [!TIP]` | Atalho legítimo, truque de prova, forma de conferir o resultado |
| `> [!IMPORTANT]` | Hipótese que não pode ser esquecida (continuidade, domínio, sinal) |
| `> [!WARNING]` | Erro que o aluno vai cometer se não for avisado agora |
| `> [!CAUTION]` | Reservado para armadilhas graves, do tipo que invalida a questão inteira |

---

## 5. LaTeX no GitHub

O GitHub renderiza LaTeX nativamente. As regras abaixo não são estéticas: cada uma delas evita um caso real de falha de renderização.

| Situação | Escreva assim | Nunca |
| --- | --- | --- |
| Fórmula no meio do texto | `$f(x) = x^2$` | `\(f(x)=x^2\)` |
| Fórmula destacada | `$$ \ldots $$` em **linha própria**, com linha em branco antes e depois | `\[ \ldots \]` |
| Várias linhas alinhadas | bloco `$$` em **várias linhas**, com `\begin{aligned}` | `\begin{equation}`, `\begin{align}` (sem o `ed`) |
| Fração em destaque | `\dfrac{a}{b}` | `\frac` em display quando a fração ficar pequena |
| Módulo | `\lvert x \rvert` | `|x|` — a barra vertical quebra tabelas |
| Chaves de conjunto | `\lbrace x \rbrace` | `\{x\}` — veja a §5.1 |
| Espaço fino | `\thinspace` | `\,` — veja a §5.1 |
| Conjunto dos reais | `\mathbb{R}` | `R`, `IR` |
| Limite | `\lim_{x \to a}` | `lim`, `\lim_{x->a}` |
| Diferencial | `\int f(x)\thinspace dx` | `\int f(x) dx`, `\int f(x)\,dx` |
| Texto dentro da fórmula | `\text{se } x > 0` | palavras em itálico de variável |
| Função composta de nome longo | `\mathrm{arcsec}\thinspace x` | `arcsec\,x` |
| Épsilon e delta | `\varepsilon`, `\delta` | `\epsilon` (o símbolo "lunar" não é o usado nos livros) |
| Seno e tangente | `\mathrm{sen}`, `\mathrm{tg}` | `\sin`, `\tan`, `sen` sem comando |
| Cosseno, log | `\cos`, `\ln`, `\log` | `cos` sem barra, `Ln` |

### Notação trigonométrica — padrão brasileiro

O material usa a notação dos livros brasileiros e do quadro do professor, e **não** a do LaTeX em inglês. O LaTeX não traz esses comandos prontos, então eles são escritos com **`\mathrm`** — veja a **§5.2** logo abaixo para o motivo de não ser `\operatorname`:

| Função | Escreva | Renderiza | Nunca use |
| --- | --- | :---: | --- |
| seno | `\mathrm{sen}\thinspace x` | $\mathrm{sen}\thinspace x$ | `\sin` |
| cosseno | `\cos x` | $\cos x$ | `cos` sem barra |
| tangente | `\mathrm{tg}\thinspace x` | $\mathrm{tg}\thinspace x$ | `\tan` |
| cotangente | `\mathrm{cotg}\thinspace x` | $\mathrm{cotg}\thinspace x$ | `\cot` |
| secante | `\sec x` | $\sec x$ | — |
| cossecante | `\mathrm{cossec}\thinspace x` | $\mathrm{cossec}\thinspace x$ | `\csc` |
| arco seno | `\mathrm{arcsen}\thinspace x` | $\mathrm{arcsen}\thinspace x$ | `\arcsin` |
| arco tangente | `\mathrm{arctg}\thinspace x` | $\mathrm{arctg}\thinspace x$ | `\arctan` |

Potências e inversas funcionam normalmente: `\mathrm{sen}^2\thinspace x` dá $\mathrm{sen}^2\thinspace x$, e `\mathrm{tg}^{-1}\thinspace x` dá $\mathrm{tg}^{-1}\thinspace x$.

> [!CAUTION]
> **O `\thinspace` é obrigatório, e precisa de um espaço depois quando vier letra.**
>
> O `\mathrm` só troca a fonte: ele **não** gera o espaçamento de operador. Sem o `\thinspace`, `\mathrm{sen}x` sai grudado — "senx".
>
> E, como nome de comando no TeX é uma sequência de letras, `\thinspacex` vira um comando inexistente e derruba a página. Escreva sempre `\thinspace x`, com o espaço.

> [!NOTE]
> Nos **scripts de gráfico** o rótulo é escrito com o *mathtext* do matplotlib, que é mais limitado: lá se escreve `$\mathrm{sen}\,x$` — com `\,` mesmo, porque ali não há Markdown para comer a barra — e `|x|` no lugar de `\lvert x \rvert`, porque o mathtext não conhece esse comando.

### 5.1 ⚠️ A regra mais importante deste arquivo: barra invertida antes de pontuação

O GitHub processa os **escapes do Markdown antes** de entregar a fórmula ao renderizador de LaTeX. Consequência, verificada no próprio GitHub:

> **Dentro de `$...$` — e também de um `$$...$$` escrito em uma única linha — toda barra invertida seguida de um sinal de pontuação ASCII é simplesmente apagada.**

O que o autor escreve, o que o LaTeX recebe e o que acontece:

| Você escreve | O LaTeX recebe | Resultado |
| --- | --- | --- |
| `$\{a, b\}$` | `${a, b}$` | as chaves **somem** da fórmula, sem aviso nenhum |
| `$S = \left\{ 1 \right\}$` | `$S = \left{ 1 }$` | **erro fatal**: "Missing or unrecognized delimiter for \left" |
| `$[1,\,2]$` | `$[1,,2]$` | aparecem **duas vírgulas** |
| `$$a \\ b$$` (uma linha) | `$$a \ b$$` | a quebra de linha vira um espaço |

> [!CAUTION]
> **Um único erro desses derruba TODAS as fórmulas da página**, não só a defeituosa. O GitHub exibe uma tarja de erro no topo e mostra o restante da matemática como texto cru, com os cifrões à mostra. Já aconteceu neste repositório: um `\left\{` deixou a página 1.1 inteira sem renderizar.

**Portanto, dentro de matemática, nunca escreva barra invertida antes de pontuação.** Use sempre os equivalentes só com letras:

| Em vez de | Escreva | Significado |
| :---: | :---: | --- |
| `\{` e `\}` | `\lbrace` e `\rbrace` | chaves de conjunto |
| `\,` | `\thinspace` | espaço fino |
| barra invertida + barra vertical | `\Vert`, `\mid`, `\lvert`, `\rvert` | barra vertical (que também quebra tabelas) |
| `\[` e `\]` | `\lbrack` e `\rbrack` | colchetes (ou use `[` e `]` sem barra) |
| `\\` | bloco `$$` em várias linhas | quebra de linha em `cases`, `aligned`, `matrix` |
| `\%` | escreva "por cento" no texto | em LaTeX, `%` inicia comentário |

**Para quebrar linha** (em `\begin{cases}`, `\begin{aligned}`, matrizes), o bloco `$$` precisa estar escrito em **várias linhas**, com os delimitadores sozinhos:

```markdown
$$
\lvert x \rvert = \begin{cases}
x, & \text{se } x \geqslant 0 \\
-x, & \text{se } x < 0
\end{cases}
$$
```

Nesse formato o GitHub **não** aplica escapes, e `\\`, `&` e tudo mais chegam intactos ao LaTeX. O mesmo vale dentro de citação (`>`), desde que cada linha do bloco leve o seu `>`.

### 5.2 ⚠️ Macros que o GitHub recusa

Ser LaTeX válido **não basta**. O GitHub mantém uma lista própria de macros bloqueadas e, ao encontrar uma, descarta a fórmula inteira e imprime no lugar uma tarja vermelha:

> The following macros are not allowed: operatorname

| Nunca use | Use em lugar dele |
| --- | --- |
| `\operatorname{sen}` | `\mathrm{sen}\thinspace` |
| `\def`, `\newcommand`, `\renewcommand`, `\gdef`, `\let` | escreva a expressão por extenso |

> [!CAUTION]
> **Esta armadilha é invisível em qualquer teste local.** O KaTeX, o MathJax e o VS Code aceitam `\operatorname` sem reclamar — só o GitHub recusa. E a mensagem de erro é gerada **no navegador**, então nem baixar o HTML da página publicada acusa o problema.
>
> Foi assim que `\operatorname` entrou em 82 arquivos deste repositório e passou por 16 mil fórmulas verificadas antes de alguém abrir a página e ver a tarja.

**O verificador agora pega isso.** A checagem de macros proibidas roda **antes** do KaTeX, exatamente porque o KaTeX não reclamaria. A lista está no topo do script em [`extras/verificador-latex/verifica.html`](extras/verificador-latex/verifica.html) — se você descobrir outra macro recusada, acrescente-a ali.

> [!NOTE]
> **Não existe lista oficial.** O GitHub não documenta quais macros bloqueia. A nossa é empírica: cresce quando alguém encontra mais uma. Por isso a regra do final da §5.3 continua valendo — **confira na página publicada**.

### 5.3 Outras armadilhas de renderização

1. **Não deixe espaço depois do `$` de abertura**: `$ x $` pode não renderizar; `$x$` sempre renderiza.
2. **Dentro de tabelas**, o caractere `|` quebra a célula: use `\mid`, `\lvert`, `\rvert`.
3. **Em listas numeradas**, um `$$` destacado precisa estar **indentado com 3 espaços** para continuar pertencendo ao item.
4. **Um cifrão solto no texto** (`custa \$5`) pode desregular o pareamento de `$` e desligar a matemática do **documento inteiro**. Escreva "5 reais", ou ponha o cifrão dentro de `código`.
5. **Não use `\label`, `\ref` nem `\tag`** — o renderizador do GitHub não mantém estado entre blocos. (`\newcommand` e as outras macros de definição estão na §5.2.)

> [!TIP]
> **Confira sempre na página publicada, não no editor local.** O VS Code renderiza `\{` sem reclamar; o GitHub, não. Depois de publicar, abra a página e verifique se há tarja vermelha no topo e se os cifrões sumiram do texto.

### Números e decimais

- **Vírgula decimal**, como nos livros brasileiros. Dentro de fórmulas, escreva `0{,}5` (com as chaves) para o espaçamento sair correto: $0{,}5$.
- Quando houver decimal **dentro** de um intervalo ou de um par ordenado, troque o separador por ponto e vírgula para não gerar ambiguidade: $[0{,}5\thinspace ;\thinspace 2]$, $(1{,}5\thinspace ;\thinspace 3)$.
- Milhar sem separador: $12000$, não $12.000$.
- Resultados aproximados sempre com o símbolo correto e a precisão declarada: $\pi \approx 3{,}14$.

### Intervalos

Padrão brasileiro: $[a,b]$, $(a,b)$, $[a,b)$, $(-\infty, 3]$. Não use a notação de colchete invertido ($]a,b[$) — ela aparece em alguns livros, mas misturar as duas confunde.

---

## 6. Exercícios e gabaritos

### Listas de propostos (`exercicios/lista-N.M-propostos.md`)

- De **15 a 25 exercícios** por lista, em ordem crescente de dificuldade, divididos em três blocos: **Fixação** (mecânica), **Consolidação** (nível de prova), **Desafio** (1 a 3, para quem quer nota máxima).
- Numeração contínua dentro da lista: **1, 2, 3…**, com itens **(a), (b), (c)**.
- Cada exercício indica, quando pertinente, a técnica central entre parênteses no fim do enunciado — *(use o Teorema do Confronto)*. No bloco Desafio, não indique nada.
- Todo exercício proposto **tem** entrada no gabarito. Sem exceção.

### Gabaritos (`gabaritos/gabarito-N.M.md`)

Estrutura de **duas seções**, nesta ordem — essa é a regra mais importante deste arquivo:

```markdown
## ✅ Parte 1 — Respostas finais

Confira a sua resposta aqui primeiro. Só vá para a Parte 2 se a sua não bater
(ou se bater e você quiser comparar o caminho).

| Ex. | Resposta |
| :---: | --- |
| 1 (a) | $x \in (-2, 5]$ |
| 1 (b) | $\varnothing$ |

---

## 🧠 Parte 2 — Resoluções completas

### Exercício 1

**(a)** ... resolução passo a passo, no mesmo formato dos exemplos da teoria ...
```

Motivo: o aluno que confere a resposta antes de ver a solução **aprende**; o que lê a solução primeiro apenas reconhece. A separação física das duas partes protege quem tem boa intenção da própria ansiedade.

> [!WARNING]
> **Não use `<details>` para esconder resoluções com fórmulas.** O conteúdo recolhível do GitHub é HTML, e blocos `$$...$$` dentro dele falham em renderizar com frequência. Separe em seções, como acima.

Além disso:

- A resolução do gabarito tem o **mesmo rigor** da teoria: estratégia, passos justificados, resposta em destaque.
- Quando houver mais de um caminho válido, apresente o mais curto e mencione o alternativo em uma linha.
- **Toda resposta é verificada** antes do commit: derivada conferida por regra, integral conferida por derivação, limite conferido numericamente, raiz substituída na equação original.

---

## 7. Rodapé padrão

Toda página termina com estes dois blocos, exatamente nesta forma (ajustando os links):

```markdown
---

| ← Anterior | 🏠 Índice | Próximo → |
| :--- | :---: | ---: |
| [1.1 · Números reais](1.1-numeros-reais-intervalos-valor-absoluto-desigualdades.md) | [Unidade 1](README.md) · [Página inicial](../README.md) | [1.3 · Funções elementares](1.3-funcoes-elementares-paridade-e-graficos.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../LICENSE)</sub>
```

Na primeira e na última página de uma unidade, a célula correspondente recebe um travessio (`—`) ou aponta para a unidade vizinha.

---

## 8. Gráficos

- **Formato SVG**, sempre. Texto nítido em qualquer zoom e diff legível no Git.
- Gerados **exclusivamente** pelos scripts de [`extras/scripts-graficos/`](extras/scripts-graficos), usando o estilo compartilhado `estilo_calculo.py`. Nenhuma imagem entra no repositório sem o script que a produz.
- **Fundo branco explícito.** O GitHub tem tema escuro; uma figura de fundo transparente com eixos preto some para metade dos leitores.
- Toda figura é inserida com **texto alternativo descritivo** e seguida de uma frase dizendo o que observar:

```markdown
![Gráfico de f(x) = x^3 - 3x, simétrico em relação à origem](../assets/img/01-funcoes/1.3-paridade-x3-3x.svg)

> 📊 Observe que girar o gráfico de 180° em torno da origem o deixa idêntico:
> é isso que significa ser uma função ímpar.
```

- Caminhos de imagem são **relativos** (`../assets/img/...`). Nunca use URL absoluta do GitHub: ela quebra em *forks* e no material impresso.
- **Mermaid** é permitido para o que é esquema, e não curva: mapas de unidade, fluxogramas de decisão ("qual técnica de integração usar?"), hierarquias de conjuntos. Para gráfico de função, use SVG.

---

## 9. Checklist de revisão

Antes de dar commit em qualquer página de conteúdo:

- [ ] Todas as fórmulas renderizam na **Preview** do GitHub.
- [ ] Todas as contas foram conferidas, inclusive as dos gabaritos.
- [ ] A página segue a anatomia da §3, sem seção fora de ordem.
- [ ] Os ícones seguem a tabela da §4 e os alertas não passam de dois.
- [ ] Decimais com vírgula; módulos com `\lvert \rvert`; diferenciais com `\,dx`.
- [ ] Rodapé de navegação e assinatura presentes, com links testados.
- [ ] Nenhum trecho copiado de livro ou de lista de professor (ver [CONTRIBUTING.md](CONTRIBUTING.md)).
- [ ] O aluno consegue ler tudo **pelo navegador, sem instalar nada**.
