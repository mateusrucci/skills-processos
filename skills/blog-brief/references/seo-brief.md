# SEO Brief — Regras Detalhadas

Baseado no Google Search Central, diretrizes E-E-A-T e boas práticas para
visibilidade em AI Overviews, Claude web search e ChatGPT Search.

---

## 1. Título SEO

### Regras técnicas
- **50–65 caracteres** — faixa ideal para exibição completa na SERP
- Keyword principal nos primeiros 30 caracteres sempre que possível
- Não usar pipe `|` ou dois pontos `:` no início — reservar para separar marca no final
- Letras maiúsculas apenas na primeira palavra e em nomes próprios (sentence case)

### Fórmulas testadas por intenção

**Informacional (como, por que, o que):**
- `Como [verbo resultado] sem [objeção]`
- `Por que [crença comum] está errada — e o que fazer`
- `[Tema]: tudo que [ICP] precisa saber em [ano]`

**Comercial (melhor, vale a pena, comparativo):**
- `[Opção A] vs [Opção B]: qual escolher para [contexto]`
- `[Número] critérios para [decisão] — guia para [ICP]`
- `Vale a pena [ação]? Análise para [ICP]`

**Guia/checklist:**
- `[Número] passos para [resultado] em [tempo]`
- `Checklist: como [ação] do zero`

### O que evitar
- Clickbait sem entrega: "O segredo que ninguém conta sobre X" (sem revelar o segredo no post)
- Keyword stuffing: repetir a keyword duas vezes no título
- Título idêntico ao de concorrente top 1 — diferenciar sempre
- Datas desnecessárias em posts evergreen (exceto quando o ano é diferencial real)

---

## 2. Slug

### Regras
- Apenas a keyword principal, hifenizada
- Remover: artigos (o, a, os, as), preposições (de, da, do, para, com), conjunções
- Máximo 5 palavras no slug
- Sempre minúsculas, sem acentos, sem caracteres especiais
- Usar hífen `-` como separador, nunca underscore `_`

### Exemplos
| Título | Slug correto | Slug errado |
|---|---|---|
| Como estruturar um time de tráfego pago | `time-trafego-pago` | `como-estruturar-um-time-de-trafego-pago` |
| 5 erros de gestor de tráfego que custam caro | `erros-gestor-trafego` | `5-erros-gestor-de-trafego-que-custam-caro` |
| Meta Ads para pequenas empresas em 2026 | `meta-ads-pequenas-empresas` | `Meta_Ads_Pequenas_Empresas_2026` |

### Slugs e URLs estáveis
Uma vez publicado, o slug **não deve mudar**. Mudança de URL exige redirecionamento 301
e perde autoridade acumulada. Escolher bem na criação do brief evita retrabalho.

---

## 3. Meta Description

### Regras técnicas
- **140–155 caracteres** — Google trunca com `...` acima disso
- Deve conter a keyword principal (influencia o destaque em negrito na SERP)
- Não usar aspas duplas `"` — causam truncamento no HTML
- Cada post deve ter meta única — meta duplicada entre posts é sinal negativo

### Estrutura recomendada
```
[Benefício/promessa principal]. [Keyword naturalizada]. [CTA implícito ou pergunta].
```

Exemplo para "tráfego pago pequenas empresas":
> Descubra como pequenas empresas estruturam tráfego pago sem desperdiçar verba.
> Guia prático com exemplos reais e checklist de implementação.

*(152 chars — dentro do limite)*

### Para AI Overviews e busca com IA
A meta description não é fator direto de ranking para AI Overviews, mas influencia
o snippet exibido. Posts com meta clara e direta têm mais chance de ser citados.
O conteúdo do primeiro parágrafo do post tem peso maior — a meta deve antecipar
o que está lá.

---

## 4. Keywords Secundárias (LSI)

### O que são
Termos semanticamente relacionados que o Google espera ver em um post sobre o tema.
Não são sinônimos forçados — são o vocabulário natural do assunto.

### Como encontrar
1. **People Also Ask** na SERP da keyword principal
2. **Related searches** no rodapé do Google
3. **Autocomplete** do Google ao digitar a keyword
4. Headings dos posts concorrentes no top 3
5. web_search: `{keyword} perguntas frequentes`

### Como usar no brief
- Distribuir nos H2/H3 (um por seção, naturalizado)
- Mencionar no primeiro parágrafo de cada seção quando possível
- Nunca forçar — se não couber naturalmente, remover

---

## 5. Estrutura de Headings

### Por que importa para SEO e AI Overviews
O Google usa headings para entender a hierarquia do conteúdo e extrair snippets.
AI Overviews e o Claude via web fetch leem o HTML — conteúdo importante apenas
em JavaScript ou em elementos visuais não é indexado/lido.

Regra do Google Search Central: **conteúdo importante deve estar em texto estático,
acessível sem renderização dinâmica.**

### Hierarquia correta
```
H1 — único, idêntico ou muito próximo ao título SEO
  H2 — seção principal 1
    H3 — subtópico (opcional)
    H3 — subtópico (opcional)
  H2 — seção principal 2
  H2 — seção principal N
  H2 — FAQ (se houver)
  H2 — Conclusão (opcional marcar como H2)
```

### Headings snapshot-friendly
Cada H2 deve funcionar como resposta independente. Quem ler só os headings
deve entender o argumento central do post. Teste: cubra o corpo do texto e leia
só H1 + H2s — o post faz sentido?

### H2s ruins vs bons
| Ruim (genérico) | Bom (específico + keyword) |
|---|---|
| Introdução | *(sem H2 na intro — vai direto pro conteúdo)* |
| O que é tráfego pago | O que é tráfego pago e por que não funciona sem estratégia |
| Dicas importantes | 4 métricas de tráfego pago que gestores negligenciam |
| Conclusão | Próximo passo: como estruturar seu time de tráfego |

---

## 6. Schemas JSON-LD

Baseado na recomendação do Google: usar JSON-LD (não Microdata ou RDFa).
O markup deve refletir exatamente o conteúdo visível na página.

### Article (obrigatório em todo post)
```json
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
  "datePublished": "{YYYY-MM-DD}",
  "dateModified": "{YYYY-MM-DD}"
}
```

### FAQPage (quando houver seção FAQ)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{Pergunta 1}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{Resposta direta em texto}"
      }
    }
  ]
}
```

### HowTo (quando for guia passo a passo)
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "{Título SEO}",
  "step": [
    {
      "@type": "HowToStep",
      "name": "{Nome do passo}",
      "text": "{Descrição do passo}"
    }
  ]
}
```

### BreadcrumbList (sempre)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{URL base do blog}"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "{URL base do blog}/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "{Título SEO}",
      "item": "{URL completa do post}"
    }
  ]
}
```

---

## 7. E-E-A-T no Brief

O brief deve garantir que o post terá elementos de E-E-A-T antes de ser escrito.

| Pilar | O que o brief deve especificar |
|---|---|
| **Experiência** | Qual caso real, dado proprietário ou vivência prática o post vai citar |
| **Especialidade** | Qual seção demonstra conhecimento técnico profundo (não superficial) |
| **Autoridade** | Existe fonte externa para linkar? O autor tem bio/credencial na página? |
| **Confiança** | O post cumpre a promessa do título? Tem fontes citadas? Sem exageros? |

**Regra prática:** se o post pudesse ser escrito por qualquer IA sem contexto real,
o brief falhou. O campo "Âncora de credibilidade" é obrigatório.

---

## 8. Visibilidade em AI Overviews e Busca com IA

Baseado no relatório de SEO para IA (OpenAI, Anthropic, Google):

### Google AI Overviews
- Não exige otimização especial — o que rankeia na busca orgânica tende a aparecer
- Priorize conteúdo textual estático (não JS-dependente)
- Headings semânticos com resposta direta no primeiro parágrafo de cada seção
- JSON-LD Article coerente com o texto visível

### Claude / Anthropic web search
- Claude usa web fetch — conteúdo em JS dinâmico pode não ser lido
- URLs estáveis e públicas são fundamentais
- Texto claro e diretamente no HTML aumenta chance de citação

### ChatGPT Search
- Não bloquear OAI-SearchBot no robots.txt
- Conteúdo em texto puro, sem depender de interação para revelar informação

### Implicação para o brief
Toda informação importante deve ser especificada como **texto no corpo do post**,
não em imagens, vídeos sem transcrição, ou elementos interativos sem fallback textual.
