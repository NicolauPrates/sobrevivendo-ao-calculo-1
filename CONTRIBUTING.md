# Como contribuir

Este material é de aluno para aluno — ele melhora quando quem usa aponta o que está errado ou confuso. Há três níveis de contribuição, do mais simples ao mais técnico. **O primeiro não exige saber nada de Git.**

> **Autor e mantenedor:** Nicolau Prates

---

## Nível 1 — Abrir uma issue (dois cliques)

É a forma mais útil de ajudar. Use quando encontrar:

| Situação | Template |
| --- | --- |
| Erro de conta, sinal trocado, resposta divergente do gabarito, erro de digitação | 🐛 [Achei um erro no material](../../issues/new?template=01-erro-no-material.yml) |
| Uma passagem que você leu três vezes e não entendeu | ❓ [Não entendi este trecho](../../issues/new?template=02-nao-entendi.yml) |
| Ideia de exercício, de exemplo, de gráfico ou de tópico que falta | 💡 [Sugestão](../../issues/new?template=03-sugestao.yml) |

> [!TIP]
> **Como citar o trecho exato:** no GitHub, clique no número da linha do arquivo (ou arraste para selecionar várias) e depois em **Copy permalink**. Cole o link na issue. Se estiver no celular, basta dizer o arquivo e o título da seção — por exemplo, *"1.2, seção Domínio de uma função, Exemplo 3"*.

**Perguntar não é incomodar.** Se um trecho não ficou claro para você, provavelmente não ficou claro para mais vinte pessoas da turma. A issue conserta o material para todas elas.

---

## Nível 2 — Editar pelo navegador (sem instalar nada)

Para correções pequenas — um sinal, uma palavra, um link quebrado:

1. Abra o arquivo `.md` aqui no GitHub.
2. Clique no ícone de **lápis** (*Edit this file*), no canto superior direito.
3. Faça a correção. Use a aba **Preview** para checar se o LaTeX e as tabelas continuam renderizando.
4. Em **Commit changes**, escreva uma mensagem curta no formato descrito abaixo.
5. Escolha **Create a new branch and start a pull request** e confirme.

O GitHub cria o *fork* e o *pull request* para você automaticamente. Pronto.

---

## Nível 3 — Clonar o repositório

Para contribuições maiores: uma lista nova, uma seção de teoria, gráficos.

```bash
git clone https://github.com/NicolauPrates/sobrevivendo-ao-calculo-1.git
```

```bash
git checkout -b conteudo/2.3-exemplos-sanduiche
```

Antes de escrever uma linha, leia as **[convenções de escrita](CONVENCOES.md)** — elas existem para que 150 páginas escritas por pessoas diferentes pareçam um único material, e não uma colagem.

### Gráficos

Todo gráfico de `assets/img/` é gerado por um script de [`extras/scripts-graficos/`](extras/scripts-graficos). Se você for criar um gráfico novo:

1. Escreva a função que o gera no script da unidade correspondente (por exemplo, `u1_funcoes.py`).
2. Use **sempre** o estilo compartilhado de `estilo_calculo.py` — nada de cores ou fontes avulsas.
3. Rode o script, confira o `.svg` gerado e comite **o script e a imagem juntos**.

### Mensagens de commit

Formato: `<tipo>(<escopo>): <o que mudou>`

| Tipo | Quando usar |
| --- | --- |
| `conteudo` | Teoria, exemplos, exercícios ou gabaritos novos |
| `fix` | Correção de erro matemático, de digitação ou de link |
| `graficos` | Imagens em `assets/img/` e scripts em `extras/` |
| `docs` | README, CONTRIBUTING, CONVENCOES, índices |
| `estrutura` | Pastas, renomeações, arquivos de configuração |

Exemplos reais:

```text
conteudo(2.3): adiciona teoria e 4 exemplos do Teorema do Confronto
fix(1.1): corrige sinal na solucao da inequacao do Exemplo 7
graficos(1.3): adiciona grafico de paridade de x^3 - 3x
```

### Checklist antes de abrir o pull request

- [ ] O LaTeX renderiza — rode o **[verificador](extras/verificador-latex/README.md)** (`python extrai_formulas.py` e depois `verifica.html`). O editor local aceita coisas que o GitHub rejeita.
- [ ] As contas foram **verificadas**: toda resposta de exercício proposto está no gabarito e está certa.
- [ ] Os links relativos funcionam, incluindo a navegação `anterior / índice / próximo` no rodapé.
- [ ] A página segue a anatomia padrão descrita em [CONVENCOES.md](CONVENCOES.md).
- [ ] Nenhuma dependência nova foi exigida do aluno — a teoria e os exercícios continuam legíveis só pelo navegador.
- [ ] Nenhum conteúdo foi copiado literalmente de livro, lista ou prova. Veja a seção abaixo.

---

## ⚖️ Direito autoral — leia antes de contribuir

Este repositório é licenciado em [CC BY-SA 4.0](LICENSE) e só pode conter **material original**.

**Não envie:**

- texto, exemplo, exercício ou figura **copiados** de Leithold, Stewart, Thomas, Anton, Swokowski, Munem & Foulis ou de qualquer outro livro;
- listas, provas, gabaritos ou notas de aula de professores, digitalizados ou transcritos;
- PDFs de livros, de qualquer origem.

**Pode e deve:**

- escrever exercícios **autorais** inspirados no *estilo* e no *nível* desses livros — a técnica é a mesma, os números e o enunciado são seus;
- **citar** a referência para o aluno aprofundar: *"Leithold, Cap. 2, Seção 2.4"*.

A linha é simples: **ideias matemáticas são de todos; a redação de um autor é dele.**

---

## Código de convivência

Material didático atrai gente insegura com a matéria — é exatamente para quem este repositório existe. Nas issues e nos pull requests:

- nenhuma pergunta é boba, e dúvida de pré-cálculo é bem-vinda;
- critique o conteúdo, nunca a pessoa;
- se for corrigir alguém, mostre a conta certa.

Dúvidas sobre como contribuir? Abra uma issue com o template de [sugestão](../../issues/new?template=03-sugestao.yml) e pergunte.
