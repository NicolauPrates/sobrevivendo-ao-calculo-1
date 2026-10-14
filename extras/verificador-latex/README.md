# 🔎 Verificador de LaTeX

> [!IMPORTANT]
> **Isto não é material de estudo.** É uma ferramenta de manutenção, para quem escreve ou corrige páginas do repositório. Se você veio aprender Cálculo, volte para a [página inicial](../../README.md).

Confere se **todas** as fórmulas do material vão renderizar no GitHub — antes de publicar.

---

## Os dois problemas que ele resolve

### 1. Macros que o GitHub recusa

Ser LaTeX válido não basta: o GitHub bloqueia certas macros e descarta a fórmula inteira, imprimindo no lugar

> The following macros are not allowed: operatorname

A pior parte é que **nenhum teste local acusa**. O KaTeX, o MathJax e o VS Code aceitam `\operatorname` sem reclamar, e a mensagem é gerada no navegador — então nem baixar o HTML da página publicada revela o problema. Foi assim que `\operatorname` entrou em 82 arquivos deste repositório e passou por 16 mil fórmulas "verificadas".

Por isso a checagem de macros proibidas roda **antes** do KaTeX. A lista fica no topo do script em `verifica.html`; se aparecer outra macro recusada, acrescente-a ali.

> [!NOTE]
> A lista é **empírica** — o GitHub não publica a dele. Hoje tem `\operatorname` (confirmada na prática) e as macros de definição `\def`, `\newcommand`, `\renewcommand`, `\gdef` e `\let` (preventivas).

### 2. Escapes do Markdown comidos antes do LaTeX

O GitHub aplica os escapes do Markdown **antes** de entregar a fórmula ao renderizador de LaTeX. Dentro de `$...$`, toda barra invertida seguida de pontuação é apagada:

| Você escreve | O LaTeX recebe | Resultado |
| --- | --- | --- |
| `$\{a, b\}$` | `${a, b}$` | as chaves somem, sem aviso |
| `$S = \left\{ 1 \right\}$` | `$S = \left{ 1 }$` | **erro fatal** |
| `$[1,\,2]$` | `$[1,,2]$` | duas vírgulas |

> [!CAUTION]
> **Um único erro desses derruba todas as fórmulas da página**, não só a defeituosa: o GitHub mostra uma tarja vermelha no topo e exibe o resto da matemática como texto cru, com os cifrões à mostra. Já aconteceu aqui — um `\left\{` deixou a página 1.1 inteira sem renderizar.

A regra completa, com a tabela dos equivalentes seguros (`\lbrace`, `\thinspace`, blocos `$$` em várias linhas), está na **[§5.1 das convenções](../../CONVENCOES.md)**; a lista de macros proibidas, na **[§5.2](../../CONVENCOES.md)**.

> [!IMPORTANT]
> **O verificador reduz o risco; não o elimina.** Ele só conhece as armadilhas que já descobrimos. Continue abrindo a página publicada depois de cada mudança grande — foi assim que as duas desta lista apareceram.

---

## Como usar

### 1. Extraia as fórmulas

Na pasta `extras/verificador-latex`:

```bash
python extrai_formulas.py
```

O script varre todos os `.md` do repositório, aplica o mesmo pré-processamento que o GitHub aplica e grava `formulas.json`.

### 2. Abra a página de verificação

`verifica.html` precisa ser servida por HTTP — abrir o arquivo direto pelo `file://` faz o navegador bloquear a leitura do `formulas.json`. Da mesma pasta:

```bash
python -m http.server 8777
```

Depois, no navegador: **<http://127.0.0.1:8777/verifica.html>**

A página carrega o KaTeX, passa cada fórmula por ele e mostra o resultado em dois níveis:

| | O que é | Gravidade |
| :---: | --- | --- |
| ❌ **Erro** | O KaTeX recusa a fórmula. **Derruba todas as fórmulas da página**, não só a defeituosa. | Impede a publicação |
| ⚠️ **Alerta** | A fórmula renderiza, mas o Markdown comeu uma barra invertida pelo caminho — e ela sai **errada e sem aviso**. O caso típico é `\,` virando vírgula, e `\\` deixando de quebrar a linha. | Corrija antes de publicar |

Cada caso mostra o **arquivo**, o **contexto** (inline, `$$` de uma linha, bloco de várias linhas), o **LaTeX como o KaTeX o recebeu** e o motivo.

Se tudo estiver limpo, aparece **"nenhum problema"** — pode publicar.

Encerre o servidor com `Ctrl + C` quando terminar.

---

## Quando rodar

- Antes de **todo** commit que acrescente ou altere fórmulas.
- Antes de abrir um pull request — está no [checklist de contribuição](../../CONTRIBUTING.md).

> [!NOTE]
> O verificador pega erros de **sintaxe LaTeX**. Ele não confere se a matemática está certa: uma derivada errada renderiza lindamente. Para o conteúdo, não há atalho — é conferir a conta.

---

## O que ele não cobre

- **Mermaid** (os diagramas de fluxo): confira olhando a página publicada.
- **Erros de pareamento de cifrão** no documento inteiro — um `$` solto no texto pode desligar a matemática da página toda. O script tende a produzir fórmulas estranhas quando isso acontece; se aparecer um erro em uma "fórmula" que você não escreveu, procure um cifrão sobrando no arquivo.
- A **versão exata do KaTeX** do GitHub. O verificador usa a 0.16.11, que é próxima, mas não necessariamente idêntica.

---

| ← Extras | 🏠 Índice | Convenções |
| :--- | :---: | ---: |
| [Extras](../README.md) | [Página inicial](../../README.md) | [CONVENCOES.md](../../CONVENCOES.md) |

<sub>*Sobrevivendo ao Cálculo 1 (UENF)* · por **Nicolau Prates** · [CC BY-SA 4.0](../../LICENSE)</sub>
