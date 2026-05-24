---
name: blog-review
description: >
  Revisa posts de blog completos (HTML) cobrindo SEO on-page, qualidade
  editorial e alinhamento de voz. Use SEMPRE que o usuário pedir "revisar o post",
  "checar o artigo", "review do post", "auditoria do conteúdo", "está pronto para
  publicar?", "qualidade do post" ou quando vier de um post gerado pela skill
  blog-writer. Entrega relatório estruturado com score (0-100), problemas identificados
  por categoria e decisão clara: APROVADO (90+) ou REPROVADO (abaixo de 90). Nunca
  corrige automaticamente, só reporta para aprovação humana.
---

# blog-review

Skill de revisão editorial e SEO de posts de blog. Analisa o HTML gerado pelo
blog-writer, emite um relatório estruturado com score e lista de problemas, e
aguarda decisão humana antes de qualquer correção.

**Score mínimo para aprovação: 90/100.**
Abaixo disso: REPROVADO — o post volta para o blog-writer com lista de correções.

---

## Pré-requisito

Precisa do arquivo HTML do post. Pode vir de:

**A)** Caminho do arquivo: `~/blog-writer/{slug-do-blog}/{slug-do-post}/index.html`
**B)** HTML colado diretamente no chat

Precisa também do brief aprovado para checar conformidade:
`~/blog-brief/{slug-do-blog}/{slug-do-post}/brief.md`

Se o brief não estiver disponível, pergunte o slug do post antes de continuar.

Leia o perfil do blog em `references/clients/{slug}.md` para checar tom e CTA.

---

## Workflow

### Passo 1 — Carregar os arquivos

1. Leia o HTML do post
2. Leia o brief aprovado
3. Leia o perfil do cliente (`references/clients/{slug}.md`)
4. **Se blog Rucci:** leia também `references/voice-rucci.md`

### Passo 2 — Executar a auditoria por categoria

Execute cada categoria na ordem abaixo. Para cada item, marque:
- ✅ OK
- ⚠️ Problema menor (perde 1–3 pts)
- ❌ Problema grave (perde 4–10 pts)

Leia `references/review-criteria.md` para os critérios detalhados de cada categoria.

---

### Passo 3 — Montar o relatório

Formato de saída obrigatório:

```
═══════════════════════════════════════════════════
RELATÓRIO DE REVIEW — {Título do post}
Blog: {nome} | Data: {data} | Revisor: blog-review
═══════════════════════════════════════════════════

## SCORE FINAL: {X}/100

{APROVADO ✅ — pronto para deploy}
OU
{REPROVADO ❌ — requer correções antes do deploy}

---

## 1. SEO ON-PAGE ({X}/30 pts)

### Elementos técnicos ({X}/15 pts)
✅/⚠️/❌ <title>: {observação}
✅/⚠️/❌ Meta description: {observação}
✅/⚠️/❌ Canonical: {observação}
✅/⚠️/❌ JSON-LD Article: {observação}
✅/⚠️/❌ JSON-LD BreadcrumbList: {observação}
✅/⚠️/❌ JSON-LD adicional (FAQ/HowTo): {observação ou N/A}
✅/⚠️/❌ Meta robots: {observação}
✅/⚠️/❌ Open Graph tags: {observação}

### Uso de keywords ({X}/15 pts)
✅/⚠️/❌ Keyword no <title>: {observação}
✅/⚠️/❌ Keyword no H1: {observação}
✅/⚠️/❌ Keyword no 1º parágrafo: {observação}
✅/⚠️/❌ Keyword em ≥2 H2s: {observação}
✅/⚠️/❌ Keywords secundárias distribuídas: {observação}
✅/⚠️/❌ Ausência de keyword stuffing: {observação}
✅/⚠️/❌ Keyword no alt text (imagem principal): {observação}

---

## 2. ESTRUTURA HTML ({X}/20 pts)

✅/⚠️/❌ Único H1: {observação}
✅/⚠️/❌ Hierarquia sem pulos (H1→H2→H3): {observação}
✅/⚠️/❌ <article> como wrapper: {observação}
✅/⚠️/❌ Cada H2 em <section> própria: {observação}
✅/⚠️/❌ <nav aria-label="breadcrumb"> presente: {observação}
✅/⚠️/❌ <time datetime=""> no post-meta: {observação}
✅/⚠️/❌ FAQ usa <dl><dt><dd>: {observação ou N/A}
✅/⚠️/❌ Links externos com rel="noopener": {observação}
✅/⚠️/❌ Imagens com alt preenchido: {observação}
✅/⚠️/❌ Conteúdo importante em HTML estático (não JS): {observação}

---

## 3. QUALIDADE EDITORIAL ({X}/30 pts)

### Conformidade com o brief ({X}/10 pts)
✅/⚠️/❌ Estrutura de H2/H3 seguida: {observação}
✅/⚠️/❌ Word count dentro do alvo (±10%): {alvo: X | real: Y}
✅/⚠️/❌ Âncora de credibilidade presente: {observação}
✅/⚠️/❌ CTA correto e único: {observação}

### Qualidade do texto ({X}/20 pts)
✅/⚠️/❌ Introdução: problema → dificuldade → promessa (≤150 palavras): {observação}
✅/⚠️/❌ Primeiro parágrafo de cada H2 é snapshot: {observação}
✅/⚠️/❌ Parágrafos ≤4 linhas: {observação}
✅/⚠️/❌ Frases ≤25 palavras (maioria): {observação}
✅/⚠️/❌ Sem conteúdo genérico que IA escreveria sem contexto: {observação}
✅/⚠️/❌ Sem linguagem de coach ("mindset", "jornada", "propósito"): {observação}
✅/⚠️/❌ Links internos presentes (≥2): {observação}
✅/⚠️/❌ Links externos com URL real (sem inventado): {observação}
✅/⚠️/❌ Conclusão: síntese + próximo passo + CTA (≤120 palavras): {observação}
✅/⚠️/❌ Listas usadas apenas quando itens são realmente enumeráveis: {observação}

---

## 4. TOM E VOZ ({X}/20 pts)

✅/⚠️/❌ Tom alinhado com perfil do cliente: {observação}
✅/⚠️/❌ Vocabulário consistente com o ICP: {observação}
✅/⚠️/❌ Nível técnico adequado ao leitor: {observação}
✅/⚠️/❌ Dados e afirmações verificáveis (sem invenção): {observação}
✅/⚠️/❌ Sem exagero ou promessa que o post não cumpre: {observação}

[Se blog Rucci — itens adicionais:]
✅/⚠️/❌ Conceitos proprietários usados corretamente: {observação}
✅/⚠️/❌ Estrutura de argumento: afirmação → exemplo → princípio: {observação}
✅/⚠️/❌ Números específicos (não vagos): {observação}
✅/⚠️/❌ Sem cacoetes de live transcritos literalmente: {observação}

---

## 5. PROBLEMAS CRÍTICOS (itens que reprovam independente do score)

Liste aqui qualquer item que reprova o post independente do score total:
- [ ] URL inventada em link externo
- [ ] Dado estatístico sem fonte e não proprietário
- [ ] Âncora de credibilidade ausente
- [ ] Keyword stuffing evidente
- [ ] H1 duplicado
- [ ] JSON-LD Article ausente
- [ ] CTA ausente ou múltiplos CTAs

{Se nenhum: "Nenhum problema crítico identificado."}

---

## RESUMO DE CORREÇÕES NECESSÁRIAS

{Se APROVADO:}
> Post aprovado com score {X}/100. Pode seguir para blog-deploy.
> {Se houver ⚠️: "Sugestões opcionais de melhoria listadas abaixo — não bloqueiam o deploy."}

{Se REPROVADO:}
> Score: {X}/100 — abaixo do mínimo de 90. Correções obrigatórias antes do deploy:

### 🔴 Obrigatórias (bloqueiam o deploy)
1. {Descrição do problema + onde está no HTML + o que corrigir}
2. {idem}

### 🟡 Recomendadas (não bloqueiam, mas melhoram)
1. {Descrição}

---

**➜ APROVADO? Responda "deploy" para seguir para blog-deploy.**
**➜ REPROVADO? Responda "corrigir" para devolver ao blog-writer com esta lista.**
═══════════════════════════════════════════════════
```

---

### Passo 4 — Aguardar decisão

Após entregar o relatório, **não faça nada mais**. Aguarde:

- `"deploy"` → confirme: *"Passando para blog-deploy com o arquivo em `~/blog-writer/{slug}/{slug}/index.html`."*
- `"corrigir"` → gere um resumo de instruções para o blog-writer:

```
## Instruções de correção para blog-writer
Post: {slug}
Score atual: {X}/100 | Meta: 90/100

### Correções obrigatórias:
1. {instrução específica e acionável}
2. {idem}

### Correções recomendadas:
1. {instrução}
```

---

## Regras invioláveis

1. **Nunca corrige automaticamente** — só reporta
2. **Score abaixo de 90 = REPROVADO** — sem exceção, mesmo que o usuário peça para aprovar assim mesmo
3. **Problemas críticos reprovam independente do score** — um único crítico = REPROVADO
4. **Toda observação deve ser específica** — não "keyword mal usada", mas "keyword 'tráfego pago' ausente no primeiro parágrafo da seção 2"
5. **Não invente problemas** — se o item está OK, marca OK
6. **Word count conta apenas texto visível** — não contar tags HTML, comentários ou JSON-LD

---

## Cálculo do Score

| Categoria | Peso |
|---|---|
| SEO On-Page | 30 pts |
| Estrutura HTML | 20 pts |
| Qualidade Editorial | 30 pts |
| Tom e Voz | 20 pts |
| **Total** | **100 pts** |

Cada ⚠️ desconta conforme gravidade (1–3 pts).
Cada ❌ desconta conforme gravidade (4–10 pts).
Problemas críticos: score vai automaticamente abaixo de 90 independente dos demais.

---

## Arquivos de referência

- `references/review-criteria.md` — critérios detalhados por categoria
- `references/clients/{slug}.md` — perfil do blog (tom, ICP, CTA)
- `references/voice-rucci.md` — critérios de voz para blog Rucci
