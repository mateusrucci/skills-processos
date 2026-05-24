---
name: blog-research
description: Pesquisa temas para blog combinando sinais de viralidade (HN, Reddit) com análise
  de SEO (intenção de busca, concorrência, E-E-A-T). Use SEMPRE que o usuário pedir "pesquisar
  temas para o blog", "pautas do mês", "o que está em alta", "sugestão de posts", "keywords
  para o blog", "o que escrever", "temas para artigo", "grade de conteúdo", "calendário editorial"
  ou qualquer variação de descoberta de pauta para blog. Também use quando o usuário mencionar
  cliente + blog + tema/pauta. Suporta múltiplos blogs/clientes via arquivos de config em
  references/clients/.
---

# blog-research

Skill de pesquisa de pautas para blog. Combina viralidade real (HN + Reddit) com critérios
de SEO baseados nas diretrizes do Google Search Central e visibilidade em AI Overviews.

## Pré-requisito

Precisa saber para qual blog/cliente vai pesquisar. Se não estiver claro no pedido, pergunte:

> "Para qual blog? Me diz o nome ou nicho."

Depois, leia o arquivo de config correspondente em `references/clients/{slug}.md`.
Se não existir, use `references/clients/_template.md` e peça as informações ao usuário
antes de continuar.

---

## Workflow (siga nesta ordem)

### Passo 1 — Carregar o perfil do blog

Leia `references/clients/{slug}.md`. Extraia:
- Nicho e palavras-chave raiz
- ICP (quem lê)
- Tom de voz
- Subreddits relevantes
- Concorrentes para monitorar
- CTA padrão

### Passo 2 — Pesquisa de sinais virais

Rode o script de busca com os termos do perfil:

```bash
python3 <SKILL_DIR>/scripts/find_themes.py \
  --query "TERMO_1" --query "TERMO_2" \
  --reddit r/SUBREDDIT_1 --reddit r/SUBREDDIT_2
```

O script bate em:
- **Hacker News** (Algolia API): posts com > 100 pontos
- **Reddit**: top posts da semana nos subreddits do nicho

Salva resultado em `~/blog-research/{slug}/{timestamp}/raw.json`.

### Passo 3 — Pesquisa de SEO com web_search

Para cada tema que surgiu no Passo 2 (e para termos do perfil que ainda não apareceram),
faça buscas usando a ferramenta de busca nativa:

**Buscas obrigatórias:**
1. `{keyword} blog {ano}` — ver quem domina a SERP
2. `{keyword} perguntas frequentes` — capturar intenção informacional
3. `{keyword} {cidade/país do ICP}` — se for nicho local

**Análise dos resultados de busca:**
- Quem aparece na posição 1–3? (Domínio, autoridade aparente)
- Tem featured snippet ou AI Overview ocupado?
- Os resultados existentes têm mais de 1 ano? (oportunidade de conteúdo frescos)
- Há "People Also Ask" relevante? (capturar perguntas reais)

Leia `references/seo-criteria.md` para guiar a análise.

### Passo 4 — Curadoria e scoring

Para cada tema, calcule um **Score de Oportunidade (0–10)**:

| Critério | Peso | Como avaliar |
|---|---|---|
| Alinhamento com ICP | 30% | Quanto o tema resolve a dor do leitor do blog |
| Concorrência baixa ou média | 25% | Poucos resultados fortes na SERP, conteúdo antigo |
| Intenção comercial/informacional útil | 20% | Topo/meio de funil preferível para blogs B2B |
| Potencial viral (pontos HN / upvotes Reddit) | 15% | Sinal de que o mercado se importa com isso |
| E-E-A-T viável | 10% | O blog pode demonstrar experiência real no tema? |

Score ≥ 7: Alta prioridade  
Score 5–6: Média prioridade  
Score < 5: Descartar ou arquivar

### Passo 5 — Entregar o relatório

Formato de saída obrigatório:

```
## Relatório de Pautas — {Nome do Blog} — {Mês/Ano}

### 🔥 Alta prioridade (score ≥ 7)

**1. {Título sugerido — 50–65 chars, formato gancho}**
- Keyword principal: {keyword}
- Intenção: Informacional / Comercial / Transacional
- Concorrência: Baixa / Média / Alta
- Ângulo contraintuitivo: {a "sacada" — por que este post seria diferente}
- Dado/fonte que sustenta: {link ou dado real}
- Por que encaixa no ICP: {1 linha}
- Score: {X}/10

---

### 📈 Média prioridade (score 5–6)
[mesma estrutura]

### 💡 Long tail / oportunidade futura (score < 5, mas vale guardar)
[apenas título + keyword + motivo em 1 linha]

---

**Próximo passo:** escolha as pautas aprovadas e rode a skill `blog-brief`.
```

---

## Regras invioláveis

1. **Nunca invente dados** — se não encontrou volume ou fonte real, diga "sem dado disponível"
2. **Conteúdo genérico = descarte** — sem dado concreto ou ângulo diferente, o tema vai para long tail
3. **Linguagem de coach é eliminatória** — "mindset", "jornada", "propósito" como tema principal: fora
4. **Tutorial técnico sem ângulo** — tutorial genérico que todo mundo já fez: descarte
5. **SHARES é a métrica de viralidade** — tema que as pessoas querem mostrar pra alguém > tema que só resolvem sozinhos
6. **E-E-A-T sempre** — priorize temas onde o blog pode trazer experiência real, caso próprio, dado proprietário

---

## Arquivos de referência

- `references/seo-criteria.md` — critérios detalhados de avaliação SEO
- `references/clients/_template.md` — template para novos clientes/blogs
- `references/clients/{slug}.md` — perfil específico do blog
- `scripts/find_themes.py` — script de busca HN + Reddit
