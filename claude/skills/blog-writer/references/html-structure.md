# HTML Structure — blog-writer

Template completo e anotado para posts de blog. Baseado nas diretrizes do Google
Search Central: rastreabilidade, semântica, dados estruturados JSON-LD e
compatibilidade com leitura por IAs (Claude web fetch, OAI-SearchBot, Googlebot).

---

## Princípios de HTML para SEO e AI Visibility

1. **Conteúdo importante nunca em JS dinâmico** — Claude web fetch e Googlebot
   leem o HTML estático. Se o texto depende de JavaScript para aparecer, pode
   não ser indexado nem citado.

2. **Semântica antes de estilo** — usar as tags corretas (`<article>`, `<section>`,
   `<header>`, `<nav>`, `<dl>`) ajuda crawlers a entender a hierarquia do conteúdo.

3. **JSON-LD no `<head>`** — o Google recomenda JSON-LD (não Microdata ou RDFa).
   Deve refletir exatamente o conteúdo visível na página.

4. **Canonical sempre** — evita conteúdo duplicado se o CMS gerar múltiplas URLs.

5. **`lang="pt-BR"`** — sinaliza idioma para indexação correta e hreflang futuro.

---

## Template Completo Anotado

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- TÍTULO: 50–65 chars. Keyword o mais à esquerda possível. -->
  <title>{Título SEO — máx 65 chars}</title>

  <!-- META: 140–155 chars. Sem aspas duplas. Keyword presente. -->
  <meta name="description" content="{Meta description — máx 155 chars}">

  <!-- CANONICAL: URL exata e completa. Previne conteúdo duplicado. -->
  <link rel="canonical" href="https://{dominio}/blog/{slug-do-post}/">

  <!-- ROBOTS: Permitir snippet amplo. Não bloquear OAI-SearchBot no robots.txt. -->
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">

  <!-- OPEN GRAPH: Para compartilhamento social. -->
  <meta property="og:title" content="{Título SEO}">
  <meta property="og:description" content="{Meta description}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://{dominio}/blog/{slug-do-post}/">
  <meta property="og:image" content="https://{dominio}/blog/{slug-do-post}/og-image.webp">
  <meta property="og:locale" content="pt_BR">

  <!-- TWITTER CARD -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{Título SEO}">
  <meta name="twitter:description" content="{Meta description}">

  <!-- =====================================================
       JSON-LD: Article (OBRIGATÓRIO em todo post)
       Fonte: Google Search Central — Structured Data
       ===================================================== -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{Título SEO — idêntico ao <title>}",
    "description": "{Meta description — idêntica à <meta name=description>}",
    "inLanguage": "pt-BR",
    "url": "https://{dominio}/blog/{slug-do-post}/",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://{dominio}/blog/{slug-do-post}/"
    },
    "author": {
      "@type": "Person",
      "name": "{Nome do autor}",
      "url": "https://{dominio}/sobre"
    },
    "publisher": {
      "@type": "Organization",
      "name": "{Nome do blog/empresa}",
      "logo": {
        "@type": "ImageObject",
        "url": "https://{dominio}/logo.webp"
      }
    },
    "datePublished": "{YYYY-MM-DD}",
    "dateModified": "{YYYY-MM-DD}",
    "image": {
      "@type": "ImageObject",
      "url": "https://{dominio}/blog/{slug-do-post}/og-image.webp",
      "width": 1200,
      "height": 630
    }
  }
  </script>

  <!-- =====================================================
       JSON-LD: BreadcrumbList (SEMPRE)
       Melhora navegação na SERP e hierarquia para crawlers.
       ===================================================== -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://{dominio}/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Blog",
        "item": "https://{dominio}/blog/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "{Título SEO}",
        "item": "https://{dominio}/blog/{slug-do-post}/"
      }
    ]
  }
  </script>

  <!-- =====================================================
       JSON-LD: FAQPage (APENAS se o post tiver seção FAQ)
       Ativa perguntas expandíveis na SERP.
       ===================================================== -->
  <!--
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "{Pergunta 1 — idêntica ao <dt> na página}",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "{Resposta 1 — idêntica ao <dd> na página}"
        }
      },
      {
        "@type": "Question",
        "name": "{Pergunta 2}",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "{Resposta 2}"
        }
      }
    ]
  }
  </script>
  -->

  <!-- =====================================================
       JSON-LD: HowTo (APENAS se o post for guia passo a passo)
       ===================================================== -->
  <!--
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "{Título SEO}",
    "description": "{Meta description}",
    "step": [
      {
        "@type": "HowToStep",
        "position": 1,
        "name": "{Nome do passo — idêntico ao H3 correspondente}",
        "text": "{Descrição do passo}"
      }
    ]
  }
  </script>
  -->

  <!-- CSS do blog — link externo ou inline mínimo -->
  <link rel="stylesheet" href="/assets/css/blog.css">

</head>
<body>

<!-- =====================================================
     SKIP LINK: Acessibilidade — permite pular para conteúdo
     ===================================================== -->
<a href="#main-content" class="skip-link">Ir para o conteúdo principal</a>

<!-- =====================================================
     HEADER DO SITE (nav global — fora do <article>)
     ===================================================== -->
<header class="site-header">
  <!-- Logo e navegação global do site — não alterar por post -->
</header>

<!-- =====================================================
     CONTEÚDO PRINCIPAL
     ===================================================== -->
<main id="main-content">
<article class="blog-post">

  <!-- BREADCRUMB NAVEGACIONAL (visual, além do JSON-LD) -->
  <nav aria-label="breadcrumb" class="breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li aria-current="page">{Título SEO curto}</li>
    </ol>
  </nav>

  <!-- HEADER DO POST -->
  <header class="post-header">
    <!-- H1: único, idêntico ou muito próximo ao título SEO -->
    <h1>{H1 do post}</h1>

    <div class="post-meta">
      <span class="author">Por <a href="/sobre" rel="author">{Nome do autor}</a></span>
      <time datetime="{YYYY-MM-DD}" class="published-date">{DD de Mês de AAAA}</time>
      <span class="reading-time">{X} min de leitura</span>
    </div>

    <!-- Imagem de destaque do post -->
    <!-- [IMAGEM: {descrição da imagem de destaque}] -->
    <!-- [ALT: {alt text — descritivo, com keyword se natural}] -->
    <!--
    <figure class="post-hero">
      <img
        src="{slug-do-post}/hero.webp"
        alt="{alt text}"
        width="1200"
        height="630"
        loading="eager"
        fetchpriority="high"
      >
    </figure>
    -->
  </header>

  <!-- =====================================================
       INTRODUÇÃO
       Máx 150 palavras. Problema → erro comum → promessa.
       SEM heading — vai direto ao texto.
       ===================================================== -->
  <section class="post-intro">
    <p>{Parágrafo 1 da introdução — problema/situação do ICP}</p>
    <p>{Parágrafo 2 — por que é difícil / erro comum}</p>
    <p>{Parágrafo 3 — promessa do post}</p>
  </section>

  <!-- =====================================================
       SEÇÃO 1 — Primeiro H2
       Primeiro parágrafo: resposta direta (snapshot para IA/featured snippet)
       ===================================================== -->
  <section>
    <h2>{H2 — Seção 1 com keyword secundária}</h2>
    <p>{Resposta direta à pergunta do H2 — 2 a 4 frases, funciona standalone}</p>
    <p>{Desenvolvimento do argumento}</p>
    <p>{Dado, caso ou detalhe técnico}</p>

    <!-- H3 (se existir no brief) -->
    <h3>{H3 — subtópico}</h3>
    <p>{Conteúdo do H3}</p>

    <!-- Exemplo de imagem inline -->
    <!-- [IMAGEM: {descrição}] [ALT: {alt}] -->

    <!-- Exemplo de lista quando os itens são realmente enumeráveis -->
    <!--
    <ul>
      <li>{Item 1 — frase completa}</li>
      <li>{Item 2 — frase completa}</li>
    </ul>
    -->
  </section>

  <!-- =====================================================
       SEÇÃO 2 — Segundo H2
       ===================================================== -->
  <section>
    <h2>{H2 — Seção 2}</h2>
    <p>{Snapshot}</p>
    <p>{Desenvolvimento}</p>

    <!-- Exemplo de tabela comparativa -->
    <!--
    <table>
      <caption>{O que a tabela compara}</caption>
      <thead>
        <tr>
          <th scope="col">{Critério}</th>
          <th scope="col">{Opção A}</th>
          <th scope="col">{Opção B}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{Critério 1}</td>
          <td>{Valor A}</td>
          <td>{Valor B}</td>
        </tr>
      </tbody>
    </table>
    -->
  </section>

  <!-- Repetir <section> para cada H2 do brief -->

  <!-- =====================================================
       SEÇÃO FAQ (APENAS se estiver no brief)
       Usar <dl><dt><dd> — semântico para FAQPage schema.
       O texto aqui DEVE ser idêntico ao JSON-LD FAQPage.
       ===================================================== -->
  <!--
  <section class="faq-section">
    <h2>Perguntas frequentes sobre {tema}</h2>
    <dl class="faq-list">

      <dt>{Pergunta 1 — idêntica ao JSON-LD}</dt>
      <dd>{Resposta direta, 2–4 frases — idêntica ao JSON-LD}</dd>

      <dt>{Pergunta 2}</dt>
      <dd>{Resposta 2}</dd>

      <dt>{Pergunta 3}</dt>
      <dd>{Resposta 3}</dd>

    </dl>
  </section>
  -->

  <!-- =====================================================
       CONCLUSÃO + CTA
       Máx 120 palavras. Síntese → próximo passo → CTA.
       Um único CTA. Texto: verbo + benefício.
       ===================================================== -->
  <section class="post-conclusion">
    <h2>{Título da conclusão — ex: "Próximo passo" ou síntese do argumento}</h2>
    <p>{Síntese do argumento central — 2 frases}</p>
    <p>{O que o leitor deve fazer agora — concreto}</p>
    <a href="{URL do CTA}" class="cta-button">{Texto do CTA — verbo + benefício}</a>
  </section>

  <!-- =====================================================
       BIO DO AUTOR
       Contribui para E-E-A-T — Autoridade do autor.
       ===================================================== -->
  <footer class="author-bio">
    <div class="author-info">
      <!-- [IMAGEM: foto do autor] [ALT: Foto de {Nome do autor}] -->
      <div class="author-text">
        <strong>{Nome do autor}</strong>
        <p>{Bio de 2–3 linhas: credencial + experiência relevante para o tema}</p>
      </div>
    </div>
  </footer>

</article>
</main>

<!-- =====================================================
     FOOTER DO SITE (fora do <article>)
     ===================================================== -->
<footer class="site-footer">
  <!-- Footer global do site -->
</footer>

</body>
</html>
```

---

## Checklist Final de HTML

Antes de entregar o arquivo, confirme:

**Estrutura**
- [ ] `<!DOCTYPE html>` presente
- [ ] `<html lang="pt-BR">`
- [ ] `<meta charset="UTF-8">` e `<meta name="viewport">`
- [ ] `<title>` entre 50–65 chars
- [ ] `<meta name="description">` entre 140–155 chars
- [ ] `<link rel="canonical">` com URL completa e correta
- [ ] Apenas um `<h1>` em todo o documento
- [ ] Hierarquia de headings sem pulos (H1→H2→H3)
- [ ] `<article>` como wrapper do post
- [ ] Cada H2 dentro de `<section>` própria

**JSON-LD**
- [ ] Article preenchido e coerente com o conteúdo visível
- [ ] BreadcrumbList presente e com URLs corretas
- [ ] FAQPage presente SE houver seção FAQ (e texto idêntico ao `<dl>`)
- [ ] HowTo presente SE for guia passo a passo

**Acessibilidade e AI Visibility**
- [ ] Skip link presente
- [ ] `aria-label="breadcrumb"` no `<nav>` do breadcrumb
- [ ] `aria-current="page"` no último item do breadcrumb
- [ ] `rel="author"` no link do autor
- [ ] `<time datetime="{YYYY-MM-DD}">` no post-meta
- [ ] Todos os `<img>` com `alt` preenchido (ou placeholder `[IMAGEM:]`)
- [ ] Links externos com `rel="noopener" target="_blank"`
- [ ] Conteúdo importante em texto estático — nada relevante dependendo de JS
