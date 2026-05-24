# Critérios Detalhados de Review — blog-review

Guia de avaliação item a item para cada categoria do relatório.
Cada critério tem: o que verificar, como verificar, e o peso do desconto.

---

## CATEGORIA 1 — SEO ON-PAGE (30 pts)

### 1.1 Elementos Técnicos (15 pts)

#### `<title>`
**O que verificar:**
- Está entre 50–65 caracteres (contar exatamente)
- Contém a keyword principal
- Keyword está nos primeiros 30 chars sempre que possível
- Não é idêntico ao H1 palavra por palavra (pode ser muito próximo)

**Descontos:**
- Fora do range (>65 ou <50 chars): ❌ -5 pts
- Sem keyword: ❌ -5 pts
- Keyword depois dos 40 chars: ⚠️ -2 pts

---

#### Meta description
**O que verificar:**
- Está entre 140–155 caracteres (contar exatamente)
- Contém a keyword principal
- Não tem aspas duplas `"` no conteúdo
- Não é igual à meta de outro post conhecido

**Descontos:**
- Fora do range (>155 ou <140 chars): ⚠️ -3 pts
- Sem keyword: ❌ -4 pts
- Com aspas duplas: ⚠️ -2 pts
- Ausente: ❌ -8 pts

---

#### `<link rel="canonical">`
**O que verificar:**
- Presente no `<head>`
- URL completa (https://)
- URL corresponde ao slug do post
- Sem parâmetros desnecessários

**Descontos:**
- Ausente: ❌ -5 pts
- URL incompleta (sem domínio): ❌ -4 pts
- URL com parâmetros: ⚠️ -2 pts

---

#### JSON-LD Article
**O que verificar:**
- Presente no `<head>` em `<script type="application/ld+json">`
- `"@type": "Article"` correto
- `headline` idêntico ao `<title>`
- `description` idêntico à meta description
- `datePublished` preenchido no formato YYYY-MM-DD
- `author.name` preenchido
- `publisher.name` preenchido
- `mainEntityOfPage` com URL correta

**Descontos:**
- Ausente: ❌ -8 pts (PROBLEMA CRÍTICO)
- headline diferente do title: ⚠️ -3 pts
- datePublished ausente: ⚠️ -2 pts
- author ausente: ⚠️ -2 pts

---

#### JSON-LD BreadcrumbList
**O que verificar:**
- Presente
- 3 níveis: Home → Blog → Post
- URLs corretas em cada nível

**Descontos:**
- Ausente: ⚠️ -3 pts
- URLs erradas: ⚠️ -2 pts

---

#### JSON-LD FAQPage (quando brief indicar FAQ)
**O que verificar:**
- Se o post tem seção FAQ: JSON-LD FAQPage deve estar presente
- Texto das perguntas e respostas idêntico ao `<dl>` da página
- Mínimo 3 perguntas

**Descontos:**
- FAQ no post mas JSON-LD ausente: ❌ -5 pts
- Texto divergente entre JSON-LD e HTML visível: ❌ -4 pts

---

#### Meta robots
**O que verificar:**
- Presente: `<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">`
- Não está bloqueando indexação acidentalmente (noindex)

**Descontos:**
- Ausente: ⚠️ -2 pts
- `noindex` acidental: ❌ -10 pts (PROBLEMA CRÍTICO)

---

#### Open Graph
**O que verificar:**
- `og:title`, `og:description`, `og:type`, `og:url`, `og:image` presentes

**Descontos:**
- Ausente completo: ⚠️ -2 pts
- Campos individuais faltando: ⚠️ -1 pt cada

---

### 1.2 Uso de Keywords (15 pts)

#### Keyword no `<title>`
- Presente e nos primeiros 30 chars: ✅
- Presente mas após 30 chars: ⚠️ -2 pts
- Ausente: ❌ -6 pts

#### Keyword no H1
- Presente: ✅
- Ausente: ❌ -5 pts

#### Keyword no primeiro parágrafo (primeiras 100 palavras)
- Presente: ✅
- Ausente: ❌ -4 pts

#### Keyword em ≥2 H2s
- 2 ou mais H2s com keyword ou variação próxima: ✅
- Apenas 1: ⚠️ -2 pts
- Nenhum: ❌ -3 pts

#### Keywords secundárias distribuídas
- Cada keyword secundária do brief presente em pelo menos 1 H2/H3 ou parágrafo de abertura: ✅
- 50–80% presentes: ⚠️ -2 pts
- Menos de 50%: ❌ -3 pts

#### Ausência de keyword stuffing
- Densidade natural, não forçada: ✅
- Repetição excessiva em 1 parágrafo (3+ vezes): ⚠️ -3 pts
- Keyword stuffing evidente: ❌ -6 pts (PROBLEMA CRÍTICO)

---

## CATEGORIA 2 — ESTRUTURA HTML (20 pts)

#### Único H1
- Exatamente 1 H1: ✅ (2 pts)
- 2 ou mais H1s: ❌ -8 pts (PROBLEMA CRÍTICO)

#### Hierarquia sem pulos
- H1→H2→H3 sem pular nível: ✅ (2 pts)
- H1→H3 sem H2: ❌ -5 pts
- H2→H4 sem H3: ⚠️ -2 pts

#### `<article>` como wrapper
- Post dentro de `<article>`: ✅ (2 pts)
- Ausente: ⚠️ -2 pts

#### Cada H2 em `<section>` própria
- Todos os H2s dentro de `<section>`: ✅ (2 pts)
- Maioria dentro: ⚠️ -1 pt
- Nenhum: ⚠️ -2 pts

#### `<nav aria-label="breadcrumb">`
- Presente com aria-label correto: ✅ (2 pts)
- Ausente: ⚠️ -2 pts

#### `<time datetime="">`
- Presente com formato YYYY-MM-DD: ✅ (2 pts)
- Ausente: ⚠️ -1 pt

#### FAQ usa `<dl><dt><dd>` (quando aplicável)
- FAQ presente e usando `<dl>`: ✅ (2 pts)
- FAQ usando `<ul>` ou outro elemento: ⚠️ -2 pts
- N/A (sem FAQ): marcar N/A

#### Links externos com `rel="noopener"`
- Todos os links externos com `rel="noopener" target="_blank"`: ✅ (2 pts)
- Alguns sem: ⚠️ -1 pt
- Nenhum com: ⚠️ -2 pts

#### Imagens com alt preenchido
- Todos os `<img>` com `alt` não vazio ou placeholder `[IMAGEM:]`: ✅ (2 pts)
- Algum sem alt: ⚠️ -1 pt por imagem, máx -3 pts
- Alt vazio (`alt=""`): ⚠️ -2 pts

#### Conteúdo importante em HTML estático
- Todo texto relevante em HTML puro, sem depender de JS: ✅ (2 pts)
- Conteúdo crítico em componente JS sem fallback: ❌ -6 pts

---

## CATEGORIA 3 — QUALIDADE EDITORIAL (30 pts)

### 3.1 Conformidade com o Brief (10 pts)

#### Estrutura de H2/H3 seguida
Comparar os headings do HTML com a estrutura aprovada no brief.
- Igual ou com divergência justificável (ex: H3 a mais): ✅ (3 pts)
- 1 H2 diferente do brief: ⚠️ -2 pts
- Estrutura completamente diferente do brief: ❌ -6 pts

#### Word count dentro do alvo (±10%)
Contar palavras do texto visível (excluir tags, JSON-LD, comentários).
- Dentro do range: ✅ (3 pts)
- 10–20% abaixo ou acima: ⚠️ -2 pts
- Mais de 20% fora: ❌ -4 pts

#### Âncora de credibilidade presente
Verificar se existe pelo menos UMA das: dado proprietário, caso real anonimizado,
experiência pessoal com número específico.
- Presente e explícita: ✅ (2 pts)
- Vaga ou genérica: ⚠️ -2 pts
- Ausente: ❌ -6 pts (PROBLEMA CRÍTICO)

#### CTA correto e único
- CTA do perfil do cliente, aparece uma vez, na conclusão: ✅ (2 pts)
- CTA errado (diferente do perfil): ⚠️ -2 pts
- Múltiplos CTAs: ⚠️ -2 pts
- CTA ausente: ❌ -5 pts (PROBLEMA CRÍTICO)

---

### 3.2 Qualidade do Texto (20 pts)

#### Introdução: problema → dificuldade → promessa (≤150 palavras)
- Estrutura correta e dentro do limite: ✅ (2 pts)
- Estrutura correta mas longa (150–200): ⚠️ -1 pt
- Sem problema/promessa claros: ⚠️ -2 pts
- Introdução genérica ("Neste artigo vamos explorar..."): ❌ -4 pts

#### Primeiro parágrafo de cada H2 é snapshot
Verificar os 3 primeiros H2s do post.
- Todos têm resposta direta no 1º parágrafo: ✅ (3 pts)
- 1–2 sem snapshot: ⚠️ -2 pts
- Nenhum tem snapshot: ❌ -5 pts

#### Parágrafos ≤4 linhas
Verificar no HTML renderizado (estimar).
- Maioria dentro do limite: ✅ (2 pts)
- 3–5 parágrafos longos: ⚠️ -1 pt
- Blocos de texto densos frequentes: ❌ -3 pts

#### Frases ≤25 palavras (maioria)
- Maioria das frases dentro do limite: ✅ (2 pts)
- Frases longas frequentes mas legíveis: ⚠️ -1 pt
- Frases longas e complexas frequentes: ⚠️ -2 pts

#### Sem conteúdo genérico
Verificar se existe seção que qualquer IA escreveria sem contexto real.
- Todo conteúdo tem especificidade real: ✅ (3 pts)
- 1 seção genérica: ⚠️ -2 pts
- 2+ seções genéricas: ❌ -5 pts

#### Sem linguagem de coach
Verificar presença de "mindset", "jornada", "propósito", "transformação" como
tema central de seção (uso casual não conta).
- Ausente: ✅ (1 pt)
- Presente pontualmente: ⚠️ -1 pt
- Seção inteira com esse tom: ❌ -3 pts

#### Links internos presentes (≥2)
- 2 ou mais links internos ou placeholders `[LINK INTERNO:]`: ✅ (2 pts)
- 1 link interno: ⚠️ -1 pt
- Nenhum: ⚠️ -2 pts

#### Links externos com URL real
- Todos os links externos têm URL real verificável: ✅ (2 pts)
- URL claramente inventada (ex: `exemplo.com/estudo`): ❌ -8 pts (PROBLEMA CRÍTICO)
- Placeholder `[FONTE:]` em vez de URL: ✅ (aceitável, não desconta)

#### Conclusão: síntese + próximo passo + CTA (≤120 palavras)
- Estrutura completa e dentro do limite: ✅ (1 pt)
- Sem próximo passo: ⚠️ -1 pt
- Sem síntese: ⚠️ -1 pt

#### Listas usadas corretamente
- Listas apenas para itens genuinamente enumeráveis: ✅ (2 pts)
- Lista usada para quebrar parágrafo que seria melhor em prosa: ⚠️ -1 pt
- Abuso de listas em todo o post: ⚠️ -2 pts

---

## CATEGORIA 4 — TOM E VOZ (20 pts)

#### Tom alinhado com perfil do cliente
Comparar o tom do post com o definido em `references/clients/{slug}.md`.
- Tom consistente em todo o post: ✅ (4 pts)
- Oscilações pontuais: ⚠️ -2 pts
- Tom completamente diferente do perfil: ❌ -6 pts

#### Vocabulário consistente com o ICP
O vocabulário usado é adequado para o leitor definido no perfil?
- Adequado: ✅ (3 pts)
- Muito técnico para o ICP: ⚠️ -2 pts
- Muito simplista para o ICP: ⚠️ -2 pts

#### Nível técnico adequado ao leitor
- Adequado: ✅ (3 pts)
- Inconsistente ao longo do post: ⚠️ -2 pts

#### Dados e afirmações verificáveis
- Todos os dados têm fonte citada ou são proprietários: ✅ (4 pts)
- 1–2 afirmações sem fonte mas plausíveis: ⚠️ -2 pts
- Dado estatístico inventado sem fonte: ❌ -8 pts (PROBLEMA CRÍTICO)

#### Sem exagero ou promessa não cumprida
O post cumpre a promessa do título?
- Cumpre: ✅ (3 pts)
- Cumpre parcialmente: ⚠️ -2 pts
- Título promete X, post entrega Y: ❌ -5 pts

---

### Critérios adicionais para Blog Rucci

(Aplicar APENAS quando o blog for `rucci.md`. Estes itens fazem parte dos 20 pts
de Tom e Voz — redistribuir pontuação internamente.)

#### Conceitos proprietários usados corretamente
Verificar se "lançamento é colheita", "conta de padaria", "princípio do teste" etc.
estão sendo usados com o significado correto (ver `references/voice-rucci.md`).
- Corretos: ✅
- Distorcidos: ⚠️ -2 pts por conceito

#### Estrutura de argumento: afirmação → exemplo → princípio
Verificar o padrão de argumentação do Mateus nas seções principais.
- Padrão seguido: ✅
- Seções que pulam o exemplo e vão direto ao princípio: ⚠️ -2 pts
- Argumentação genérica sem o padrão: ❌ -4 pts

#### Números específicos (não vagos)
- "mais de 120 lançamentos", "R$ 600 para R$ 80": ✅
- "muitos lançamentos", "custo caiu muito": ❌ -3 pts

#### Sem cacoetes de live transcritos
Verificar presença de "vamos lá", "né", "então né", "beleza", "tá bom".
- Ausentes: ✅
- 1–3 ocorrências: ⚠️ -1 pt
- Frequentes: ⚠️ -3 pts

---

## Problemas Críticos (reprovam independente do score)

Qualquer um destes itens resulta em REPROVADO automaticamente:

| Problema | Consequência |
|---|---|
| JSON-LD Article ausente | REPROVADO |
| H1 duplicado (2 ou mais) | REPROVADO |
| `noindex` acidental | REPROVADO |
| Keyword stuffing evidente | REPROVADO |
| Âncora de credibilidade ausente | REPROVADO |
| CTA ausente | REPROVADO |
| URL inventada em link externo | REPROVADO |
| Dado estatístico inventado sem fonte | REPROVADO |
| FAQ no post sem JSON-LD FAQPage | REPROVADO |
| Canonical ausente | REPROVADO |
