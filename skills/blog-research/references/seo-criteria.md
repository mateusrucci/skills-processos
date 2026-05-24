# Critérios de Avaliação SEO — blog-research

Baseado nas diretrizes do Google Search Central e boas práticas de SEO para IA (AI Overviews).

---

## 1. Intenção de Busca

O Google prioriza páginas que satisfazem a intenção real do usuário. Identificar corretamente
a intenção é o primeiro filtro.

| Tipo | Sinal de identificação | Valor para blog |
|---|---|---|
| **Informacional** | "como fazer", "o que é", "por que", "guia de" | Alto — constrói autoridade |
| **Comercial** | "melhor X para Y", "comparativo", "vale a pena" | Alto — meio de funil |
| **Transacional** | "contratar", "comprar", "preço de" | Médio — landing page é melhor |
| **Navegacional** | nome de marca, URL direta | Baixo para blog |

**Priorize informacional + comercial.** São os que mais atraem leitores qualificados para blogs B2B.

---

## 2. Análise de Concorrência na SERP

### Como avaliar sem ferramentas pagas

Busque a keyword e observe:

**Sinais de concorrência BAIXA (oportunidade):**
- Resultados com mais de 18 meses de publicação dominando a posição 1
- Domínios de autoridade genérica (não especialistas no nicho)
- Ausência de featured snippet ou AI Overview estruturado
- "People Also Ask" com perguntas ainda sem respostas claras nos resultados
- Conteúdo raso nos primeiros resultados (listicles sem profundidade)

**Sinais de concorrência ALTA (evitar ou diferenciar muito):**
- Domínios .gov, .edu ou grandes publishers (G1, Folha, Exame) nos top 3
- Featured snippet já ocupado com resposta completa
- AI Overview extenso que responde tudo sem precisar clicar
- Múltiplos resultados com conteúdo atualizado no ano corrente

**Concorrência MÉDIA (vale tentar com ângulo diferente):**
- Top 3 tem conteúdo bom mas genérico, sem experiência do autor
- Featured snippet existe mas é incompleto ou desatualizado
- Há espaço para um post com dados proprietários ou caso real

---

## 3. E-E-A-T (Experiência, Especialidade, Autoridade, Confiança)

O Google avalia se o criador tem **experiência real** com o assunto. Para blogs:

**Como demonstrar E-E-A-T em pauta:**
- O blog pode trazer caso próprio ou dado interno? → score sobe
- Tem histórico publicando sobre o tema? → autoridade construída
- O autor tem credenciais demonstráveis (8 anos de mercado, projetos reais)? → especialidade
- O conteúdo vai além do que qualquer IA geraria sem contexto real? → confiança

**Temas onde E-E-A-T é crítico (YMYL adjacente):**
- Finanças, saúde, jurídico, decisões de negócio de alto impacto
- Nesses casos, exigir ainda mais: dado real, fonte citada, experiência do autor explícita

---

## 4. Potencial para AI Overviews e Busca com IA

Baseado nas diretrizes do Google: **não há otimização especial para AI Overviews**.
O que rankeia na busca orgânica tende a aparecer em AI Overviews. Foque em:

- Conteúdo textual claro, não dependente de JavaScript para renderizar o essencial
- Headings semânticos (H1, H2, H3) que respondem perguntas diretamente
- Parágrafos de resposta direta no início de cada seção (snapshot-friendly)
- JSON-LD Article implementado na página publicada
- Conteúdo original com dado proprietário > conteúdo agregador

**Para visibilidade em Claude/ChatGPT via web search:**
- Evitar conteúdo importante só em JS client-side
- URLs estáveis e públicas, sem parâmetros desnecessários
- Texto legível diretamente no HTML (não requer renderização dinâmica)

---

## 5. Frescor e Sazonalidade

- **Trending agora** (HN/Reddit da semana): janela de 2–4 semanas para publicar
- **Sazonal** (ex: planejamento de tráfego para Q4): publicar 6–8 semanas antes
- **Evergreen** (conteúdo atemporal): prioridade pois amortiza esforço por meses

Prefira evergreen com ângulo atual. Exemplo: "Como estruturar um time de tráfego em 2026"
é evergreen + atual, melhor que "novidade X do Meta de março".

---

## 6. Critério de Descarte

Descarte imediato se:
- Tema sem dado concreto disponível para sustentar
- Concorrência dominada por publishers gigantes sem ângulo de diferenciação possível
- Tema puramente genérico que qualquer IA gera sem contexto real
- Linguagem de "guru" como tema central (mindset, propósito, jornada)
- Tutorial técnico idêntico ao que já existe em 10 outros blogs do nicho
