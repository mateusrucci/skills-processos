---
name: blog-writer
description: Escreve posts de blog completos em HTML semântico a partir de um brief
  aprovado. Use SEMPRE que o usuário pedir "escrever o post", "escrever o artigo",
  "criar o conteúdo", "redigir o post", "gerar o HTML do blog", "escrever com base
  no brief", ou quando vier de um brief aprovado pela skill blog-brief. Entrega HTML
  completo, semântico, com JSON-LD, pronto para publicar no servidor. Nunca escreve
  sem brief aprovado.
---

# blog-writer

Skill de redação de posts de blog. Recebe um brief aprovado e entrega um arquivo HTML
completo, semântico e otimizado — pronto para a skill blog-review e depois deploy.

Baseada nas diretrizes do Google Search Central (E-E-A-T, Core Web Vitals semânticos,
dados estruturados JSON-LD) e nas boas práticas de visibilidade em AI Overviews,
Claude web search e ChatGPT Search.

---

## Pré-requisito BLOQUEANTE

Precisa de um brief aprovado. Verifique:

```
~/blog-brief/{slug-do-blog}/{slug-do-post}/brief.md
```

Se o arquivo não existir e o usuário não colar o brief no chat, **PARE** e responda:

> "Preciso do brief aprovado antes de escrever. Rode a skill blog-brief ou cole o
> brief aqui no chat."

Não improvise estrutura. Não escreva com base em pauta solta.

Leia também `references/clients/{slug}.md` para tom de voz, ICP e CTA.

---

## Workflow

### Passo 1 — Ler e internalizar o brief

Leia o brief completo. Extraia e confirme mentalmente:

- [ ] Título SEO e H1
- [ ] Slug e URL final
- [ ] Meta description
- [ ] Keyword principal e keywords secundárias
- [ ] Ângulo editorial (sacada central)
- [ ] Âncora de credibilidade (dado, caso ou experiência)
- [ ] Estrutura de H2/H3 aprovada
- [ ] Word count alvo
- [ ] Schemas JSON-LD definidos
- [ ] CTA do blog

Se qualquer item estiver faltando no brief, pergunte antes de escrever.

---

### Passo 2 — Escrever o conteúdo

Leia `references/writing-rules.md` antes de escrever qualquer linha.

**Se o blog for do Mateus Rucci (`references/clients/rucci.md`):**
Leia também `references/voice-rucci.md` antes de escrever. Este arquivo contém
os padrões de linguagem extraídos das transcrições reais dos vídeos — vocabulário,
estrutura de argumento, conceitos proprietários e o que evitar. O texto deve soar
como Mateus escrevendo, não como IA escrevendo sobre tráfego pago.

#### Ordem de escrita recomendada

1. **Introdução** — escreva por último (mais fácil depois do corpo pronto), mas posicione no topo
2. **H2s do corpo** — em ordem, um por vez
3. **FAQ** — se estiver no brief
4. **Conclusão + CTA**
5. **Introdução** — revise e ajuste após o corpo pronto

#### Regras de escrita (resumo — detalhes em references/writing-rules.md)

- Tom de voz do perfil do cliente (`references/clients/{slug}.md`) — nunca genérico
- Primeiro parágrafo de cada H2: resposta direta à pergunta do heading (snapshot)
- Keyword principal no H1, primeiro parágrafo e pelo menos 2 H2s
- Keywords secundárias distribuídas naturalmente nos H2/H3 e corpo
- Âncora de credibilidade presente e explícita — não enterrada no fim
- Frases curtas — máx 25 palavras por frase como regra geral
- Parágrafos curtos — máx 4 linhas por parágrafo
- Sem linguagem de coach, sem floreio, sem adjetivos vagos
- Links internos: indicar `[LINK INTERNO: {tema relacionado}]` onde fizer sentido
- Links externos: citar fonte real quando houver dado — nunca inventar URL

---

### Passo 3 — Montar o HTML

Leia `references/html-structure.md` para o template completo.

#### Estrutura mínima obrigatória

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Título SEO}</title>
  <meta name="description" content="{Meta description}">
  <link rel="canonical" href="{URL completa do post}">

  <!-- JSON-LD: Article (obrigatório) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{Título SEO}",
    "description": "{Meta description}",
    "inLanguage": "pt-BR",
    "author": {
      "@type": "Person",
      "name": "{Nome do autor}"
    },
    "publisher": {
      "@type": "Organization",
      "name": "{Nome do blog/empresa}"
    },
    "datePublished": "{YYYY-MM-DD}",
    "dateModified": "{YYYY-MM-DD}",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "{URL completa do post}"
    }
  }
  </script>

  <!-- JSON-LD: BreadcrumbList (sempre) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "{URL base}"},
      {"@type": "ListItem", "position": 2, "name": "Blog", "item": "{URL base}/blog"},
      {"@type": "ListItem", "position": 3, "name": "{Título SEO}", "item": "{URL completa}"}
    ]
  }
  </script>

  <!-- JSON-LD adicional conforme brief (FAQPage, HowTo) -->

</head>
<body>

<article>

  <!-- Breadcrumb navegacional -->
  <nav aria-label="breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><a href="/blog">Blog</a></li>
      <li aria-current="page">{Título SEO}</li>
    </ol>
  </nav>

  <header>
    <h1>{H1 — idêntico ou muito próximo ao título SEO}</h1>
    <p class="post-meta">
      Por <span class="author">{Nome do autor}</span> |
      <time datetime="{YYYY-MM-DD}">{Data por extenso}</time> |
      <span class="reading-time">{X} min de leitura</span>
    </p>
  </header>

  <section class="intro">
    <p>{Introdução — parágrafo 1}</p>
    <p>{Introdução — parágrafo 2 se necessário}</p>
  </section>

  <section>
    <h2>{H2 seção 1}</h2>
    <p>{Primeiro parágrafo: resposta direta — snapshot}</p>
    <p>{Desenvolvimento}</p>
    <!-- H3s se existirem no brief -->
    <h3>{H3}</h3>
    <p>{Conteúdo}</p>
  </section>

  <!-- Repetir <section> para cada H2 -->

  <!-- FAQ — se estiver no brief -->
  <section class="faq">
    <h2>Perguntas frequentes</h2>
    <dl>
      <dt>{Pergunta 1}</dt>
      <dd>{Resposta direta}</dd>
      <dt>{Pergunta 2}</dt>
      <dd>{Resposta direta}</dd>
    </dl>
  </section>

  <section class="conclusion">
    <h2>{Título da conclusão}</h2>
    <p>{Resumo do argumento central}</p>
    <p>{CTA — conforme perfil do cliente}</p>
    <a href="{URL do CTA}" class="cta-button">{Texto do CTA}</a>
  </section>

</article>

</body>
</html>
```

#### Regras de HTML semântico

- Usar `<article>` como wrapper do post inteiro
- Cada H2 dentro de `<section>` própria
- FAQ usar `<dl>`, `<dt>`, `<dd>` (semântico para schema)
- Imagens: sempre com `alt` descritivo (não decorativo, não keyword stuffing)
- Imagens: indicar `[IMAGEM: {descrição do que deve ser a imagem}]` onde cabem — o deploy vai inserir
- Links internos: `<a href="/blog/{slug-relacionado}">{texto âncora natural}</a>`
- Links externos: `<a href="{URL real}" rel="noopener" target="_blank">{texto âncora}</a>`
- Negrito `<strong>`: apenas para informação genuinamente crítica — máx 3 por seção
- Itálico `<em>`: termos técnicos na primeira ocorrência ou ênfase semântica real
- Nunca usar `<b>` ou `<i>` direto — sempre `<strong>` e `<em>`
- Listas `<ul>/<ol>`: apenas quando os itens são realmente enumeráveis — não para quebrar parágrafos

---

### Passo 4 — Calcular tempo de leitura

```
palavras_totais ÷ 200 = minutos de leitura (arredondado para cima)
```

Inserir no `<span class="reading-time">` do header.

---

### Passo 5 — Validar antes de entregar

Antes de entregar o HTML, passe pelo checklist:

**SEO**
- [ ] Keyword principal no `<title>`, H1, primeiro parágrafo e ≥ 2 H2s
- [ ] Meta description entre 140–155 chars
- [ ] `<link rel="canonical">` presente e com URL correta
- [ ] JSON-LD Article preenchido corretamente
- [ ] JSON-LD BreadcrumbList presente
- [ ] JSON-LD adicional (FAQ/HowTo) se estava no brief

**HTML Semântico**
- [ ] `<html lang="pt-BR">`
- [ ] `<article>` como wrapper
- [ ] Cada H2 dentro de `<section>`
- [ ] Apenas um H1
- [ ] Sem heading pulado (H1 → H3 sem H2)
- [ ] Imagens com `alt` (ou placeholder `[IMAGEM: ...]`)

**Conteúdo**
- [ ] Âncora de credibilidade presente e explícita
- [ ] Primeiro parágrafo de cada H2 é snapshot (resposta direta)
- [ ] CTA presente na conclusão
- [ ] Word count dentro do alvo do brief (± 10%)
- [ ] Sem seção que qualquer IA escreveria sem contexto real

**Acessibilidade e AI Visibility**
- [ ] Conteúdo importante em texto estático (não depende de JS para aparecer)
- [ ] `<nav aria-label="breadcrumb">` presente
- [ ] Links com texto âncora descritivo (sem "clique aqui")

---

### Passo 6 — Salvar o arquivo

Salve o HTML em:

```
~/blog-writer/{slug-do-blog}/{slug-do-post}/index.html
```

Confirme ao usuário:

> "Post escrito e salvo em `~/blog-writer/{slug-do-blog}/{slug-do-post}/index.html`.
> Word count: {X} palavras | Tempo de leitura: {Y} min.
> Próximo passo: rode a skill `blog-review` para revisão editorial e SEO."

---

## Regras invioláveis

1. **Nunca escreve sem brief aprovado** — sem exceção
2. **Âncora de credibilidade obrigatória** — dado real, caso ou experiência. Sem isso, o post não é entregue
3. **Conteúdo importante nunca em JS** — tudo relevante para SEO deve estar no HTML estático
4. **Sem heading pulado** — H1 → H2 → H3, nunca H1 → H3
5. **Keyword sem stuffing** — densidade natural, nunca forçada
6. **Tom do cliente, não tom genérico de IA** — leia o perfil antes de escrever
7. **Links externos só com URL real** — nunca inventar domínio ou URL
8. **Canonical sempre presente** — URL exata e completa

---

## Arquivos de referência

- `references/writing-rules.md` — regras detalhadas de redação e tom
- `references/html-structure.md` — template HTML completo e anotado
- `references/voice-rucci.md` — padrões de voz e linguagem do Mateus Rucci (usar para blog rucci.md)
- `references/clients/{slug}.md` — perfil do blog (tom, ICP, CTA, keywords)
- `references/clients/_template.md` — template para novos clientes
