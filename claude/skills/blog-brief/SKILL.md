---
name: blog-brief
description: Gera briefs estruturados e completos para posts de blog a partir de pautas
  aprovadas. Use SEMPRE que o usuário pedir "criar brief", "estruturar o post", "montar
  o brief", "preparar o artigo", "estrutura do post", "outline do post", "esqueleto do
  artigo" ou quando vier de uma pauta aprovada pela skill blog-research. Entrega título
  SEO, slug, meta description, hierarquia H2/H3, ângulo editorial, keywords, word count
  e CTA — tudo pronto para aprovação humana antes de passar para blog-writer.
---

# blog-brief

Skill de geração de brief editorial para posts de blog. Transforma uma pauta aprovada
em um documento estruturado e completo que o blog-writer vai executar sem ambiguidade.

Baseada nas diretrizes do Google Search Central (E-E-A-T, intenção de busca, Core Web
Vitals semânticos, dados estruturados) e nas melhores práticas de SEO para visibilidade
em AI Overviews e busca com IA.

---

## Pré-requisito

Precisa de uma pauta aprovada. Pode vir de duas formas:

**A) Output da blog-research** — pauta com keyword, ângulo e fonte já definidos.
Leia o arquivo `~/blog-research/{slug}/{timestamp}/raw.json` se disponível.

**B) Input direto do usuário** — ele descreve o tema/pauta no chat.

Se faltar informação mínima (keyword principal + público do blog), pergunte antes de continuar.

Leia também o perfil do blog em `references/clients/{slug}.md`.
Se não existir, pergunte qual é o blog e use o `_template.md`.

---

## Workflow

### Passo 1 — Extrair os dados da pauta

Da pauta aprovada, identifique:

- **Keyword principal** (exata, como o usuário buscaria)
- **Intenção de busca** (informacional / comercial / transacional)
- **Ângulo contraintuitivo** (a sacada do post)
- **Dado/fonte âncora** (o que torna o post não-genérico)
- **ICP do blog** (quem vai ler)

Se algum desses estiver faltando, infira a partir do perfil do cliente ou pergunte.

---

### Passo 2 — Gerar os elementos SEO

Leia `references/seo-brief.md` para as regras detalhadas. Resumo:

#### Título SEO
- 50–65 caracteres (Google trunca acima disso)
- Keyword principal o mais à esquerda possível
- Formato gancho: número, pergunta, promessa concreta ou contraintuitivo
- Sem clickbait vazio — a promessa do título deve ser cumprida no post
- Exemplos de formato:
  - `Como [resultado] sem [objeção comum]`
  - `[Número] erros de [tema] que custam [consequência]`
  - `Por que [crença comum] está errada — e o que fazer`
  - `[Tema]: o guia para [ICP] em [ano]`

#### Slug
- Apenas keyword principal, hifenizada, sem stopwords
- Máximo 5 palavras
- Minúsculas, sem acentos, sem caracteres especiais
- Exemplo: `trafego-pago-pequenas-empresas`

#### Meta Description
- 140–155 caracteres (Google trunca acima)
- Deve conter a keyword principal
- Deve incluir um benefício claro e um CTA implícito
- Não repetir o título palavra por palavra
- Escrita para o humano clicar, não só para o robô indexar

#### Keywords Secundárias (LSI)
- 4–6 termos semanticamente relacionados
- Inclui variações da keyword principal, sinônimos, perguntas do "People Also Ask"
- Serão usadas naturalmente nos H2/H3 e no corpo do texto

---

### Passo 3 — Montar a estrutura do post

#### Regras de estrutura (baseadas no Google Search Central)

- **H1**: apenas um, idêntico ou muito próximo ao Título SEO
- **H2**: 3–6 seções principais, cada uma respondendo uma pergunta real do ICP
- **H3**: subtópicos dentro de cada H2, quando necessário
- Cada H2 deve poder gerar um snippet independente (resposta direta no primeiro parágrafo)
- A estrutura deve ser **snapshot-friendly**: quem ler só os headings entende o argumento
- Nenhum H2 deve ser genérico — cada um carrega uma keyword secundária ou variação

#### Seções obrigatórias

| Seção | Tipo | Objetivo |
|---|---|---|
| Introdução | Texto | Confirmar que o leitor está no lugar certo. Problema + promessa. Máx 150 palavras. |
| [H2 principal 1] | Conteúdo | Responde a pergunta mais importante da keyword |
| [H2 principal 2–4] | Conteúdo | Aprofunda com dado, caso, ou passo a passo |
| Conclusão + CTA | Texto | Resume o argumento central. CTA do blog. |

#### Seções opcionais (adicione se fizer sentido para o tema)

- **FAQ** — 3–5 perguntas reais do "People Also Ask" com respostas diretas (ativa FAQ Schema)
- **Tabela comparativa** — quando o post envolve comparação de opções
- **Checklist** — quando o post é um guia de ação
- **Caso real** — bloco dedicado ao exemplo âncora do post

---

### Passo 4 — Calcular word count e dados estruturados

#### Word Count
Baseado na concorrência e na intenção:

| Intenção | Concorrência | Word Count sugerido |
|---|---|---|
| Informacional | Baixa | 1.200–1.800 palavras |
| Informacional | Média/Alta | 2.000–3.000 palavras |
| Comercial | Qualquer | 1.500–2.500 palavras |
| Checklist/guia rápido | Baixa | 800–1.200 palavras |

Não infle artificialmente — o Google penaliza conteúdo que aumenta word count sem valor.

#### Dados Estruturados (JSON-LD)
Indique qual schema aplicar (o blog-writer vai implementar):

- **Article** — padrão para todos os posts
- **FAQPage** — quando houver seção FAQ
- **HowTo** — quando for guia passo a passo
- **BreadcrumbList** — sempre, para hierarquia de navegação

---

### Passo 5 — Montar e apresentar o brief

Formato de saída obrigatório:

```
---
## BRIEF — {Título SEO}
**Blog:** {nome do blog}
**Data de criação:** {data}
**Status:** AGUARDANDO APROVAÇÃO

---

### Metadados SEO
- **Título SEO:** {título — X chars}
- **Slug:** /{slug}
- **Meta Description:** {meta — X chars}
- **Keyword principal:** {keyword}
- **Keywords secundárias:** {kw1}, {kw2}, {kw3}, {kw4}
- **Intenção de busca:** {Informacional / Comercial}
- **Concorrência estimada:** {Baixa / Média / Alta}

---

### Ângulo Editorial
**Sacada central:** {o ângulo contraintuitivo em 1–2 frases}
**Âncora de credibilidade:** {dado real, caso ou experiência que torna o post não-genérico}
**Por que o ICP vai ler até o fim:** {motivação do leitor em 1 frase}

---

### Estrutura do Post

**Word count estimado:** {X.XXX palavras}
**Schemas JSON-LD:** Article + {outros se aplicável}

**[H1] {título do post}**

**Introdução** *(~150 palavras)*
> {descrição do que a introdução deve conter — problema, promessa, estrutura do post}

**[H2] {seção 1}** *(keyword secundária: {kw})*
> {o que esta seção responde e como — 2–3 linhas}
  - [H3] {subtópico se necessário}
  - [H3] {subtópico se necessário}

**[H2] {seção 2}** *(keyword secundária: {kw})*
> {descrição}

**[H2] {seção 3}** *(keyword secundária: {kw})*
> {descrição}

[adicionar H2s conforme necessário]

**[H2] FAQ** *(opcional — incluir se houver perguntas reais do People Also Ask)*
- P: {pergunta 1}
- P: {pergunta 2}
- P: {pergunta 3}

**Conclusão + CTA** *(~100 palavras)*
> {resumo do argumento central + CTA: {CTA padrão do blog}}

---

### Checklist pré-escrita

- [ ] Keyword principal aparece no H1, primeiro parágrafo e pelo menos 2 H2s
- [ ] Cada H2 pode gerar um snippet independente
- [ ] Tem âncora de credibilidade (dado, caso ou experiência real)
- [ ] Sem seção genérica que qualquer IA escreveria sem contexto
- [ ] CTA alinhado com o objetivo do blog
- [ ] Schema JSON-LD definido

---

**➜ APROVADO? Responda "aprovado" para salvar o brief e passar para blog-writer.**
**➜ AJUSTE? Diga o que mudar e regenero.**
```

---

### Passo 6 — Salvar após aprovação

Quando o usuário aprovar, salve o brief em:

```
~/blog-brief/{slug-do-blog}/{slug-do-post}/brief.md
```

Confirme o caminho salvo e informe:

> "Brief salvo. Próximo passo: rode a skill `blog-writer` passando este brief."

---

## Regras invioláveis

1. **Título nunca acima de 65 chars** — conte sempre antes de entregar
2. **Meta nunca acima de 155 chars** — idem
3. **Slug sem acentos, sem maiúsculas, sem stopwords**
4. **Nenhum H2 genérico** — cada heading carrega keyword ou pergunta real
5. **Âncora obrigatória** — sem dado, caso ou experiência real = brief devolvido
6. **Não invente "People Also Ask"** — use web_search para verificar perguntas reais se necessário
7. **Não salvar sem aprovação explícita** do usuário

---

## Arquivos de referência

- `references/seo-brief.md` — regras detalhadas de SEO para cada elemento do brief
- `references/clients/{slug}.md` — perfil do blog (tom, ICP, CTA, keywords raiz)
- `references/clients/_template.md` — template para novos clientes
