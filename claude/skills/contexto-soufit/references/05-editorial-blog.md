# 05 — Editorial & Blog SouFit

> Estrutura visual, editorial e técnica do blog `soufit.com/blog/`.
> Fonte canônica: `/Modernitty/Blog/blog-scope.md` (28kB)

---

## 🎯 Tese editorial

> *"Cuidar de si pode ser leve, científico e completamente seu."*

O blog é o **músculo editorial** que entrega essa tese. Não é repositório de SEO genérico. É prova viva de que a SouFit:

- É **leve** — sem culpa, urgência artificial, antes-e-depois agressivo
- É **científica** — explica ativos, cita estudos, traz reviewer técnico
- É **completamente sua** — fala em personas múltiplas, sem fórmula universal

### Promessa de leitura

Em cada post a leitora deve sentir: *"essa marca me entende, me explica direito e não me cobra nada."*

### Três coisas que o blog NUNCA faz

1. **Sermão estético** — nada de "você precisa", "está na hora de", "antes que seja tarde"
2. **Ciência hipnótica** — jargão para impressionar sem informar
3. **Conteúdo genérico** — texto que serve para qualquer marca de suplemento

### Quatro pilares de tom (mesmos do brand)

| Pilar | Aparição no blog |
|---|---|
| Amiga que entende | Abre histórias com cotidiano real, não com claim |
| Especialista sem esnobismo | Cita ciência, nunca usa termo sem explicar |
| Motivadora sem pressão | CTA é convite, nunca exigência |
| Girly com substância | Estética cuidada, humor suave, profundidade |

---

## 🏗️ Arquitetura de informação

### URLs

```
soufit.com/blog/                          → Home do blog
soufit.com/blog/[categoria]/              → Pillar de categoria
soufit.com/blog/[slug-do-artigo]/         → Artigo (URL sem data, evergreen)
soufit.com/blog/autor/[slug]/             → Página de autor
soufit.com/blog/tag/[slug]/               → Tag (cluster)
soufit.com/blog/busca?q=                  → Busca
soufit.com/blog/sobre-editorial/          → E-E-A-T (como produzimos)
```

**Regras:**
- Slugs em **kebab-case**, sem acento, sem stopwords
- URL **sem data** (evergreen, evita parecer desatualizado)
- Categoria **NÃO entra na URL do artigo** (evita duplicação + permite migração sem 301 em massa)
- Trailing slash consistente

### 6 Categorias-mãe

| # | Categoria | Slug | Cobertura | Produto-âncora |
|---|---|---|---|---|
| 1 | **Você Magra** | `voce-magra` | Composição corporal, metabolismo, jejum, platôs | Fit Moderno |
| 2 | **Performance & Suplementos** | `performance-suplementos` | Treino, hipertrofia, recuperação | Whey, Creatina |
| 3 | **Nutrição** | `nutricao` | Alimentação flexível, receitas, ingredientes | Cross-line |
| 4 | **Saúde** | `saude` | Ciclo, hormônios, sono, intestino, imunidade | Linha Saúde |
| 5 | **Dicas & Rotina** | `dicas-rotina` | Autocuidado, mini-hábitos, rituais | Lifestyle |
| 6 | **Beleza** | `beleza` | Colágeno, pele, cabelo, antioxidantes | Linha Beleza |

> **Por que 6?** Espelha as 3 categorias-mãe da loja (Emagrecimento/Performance/Saúde) + 3 extensões editoriais (Nutrição, Dicas & Rotina, Beleza) para sustentar "marca de estilo de vida".

### Tags (eixos transversais — não substituem categoria)

- **Nível:** `iniciante` · `intermediario` · `avancado`
- **Idade:** `30+` · `40+` · `50+` · `pos-menopausa`
- **Formato:** `7-minutos-leitura` · `leitura-rapida`
- **Tipo:** `ciencia` · `receita` · `mito-x-verdade` · `guia-completo`
- **Ativos canônicos:** `colageno` · `creatina` · `whey` · `magnesio`

---

## 📝 Templates editoriais

| Tipo | Tamanho | Para que serve | Frequência |
|---|---|---|---|
| **Pillar Page** | 3-5k palavras | Concentra autoridade da categoria | 1 por categoria (6 total) |
| **Cluster Post** | 1.200-2.000 palavras | Aprofunda sub-tópico da pillar | 4-6/mês |
| **Guia Prático** (HowTo) | — | Tutoriais passo a passo (Schema HowTo) | 1-2/mês |
| **Mito x Verdade** | — | Quebra de mito com fonte (alto compartilhamento) | 1/mês |
| **Ingrediente em Profundidade** | — | Ativo isolado (creatina, colágeno verisol, picolinato de cromo) | 1/mês |
| **Receita Funcional** | — | Receita com função (saciedade, antiinflamatória) | 2/mês |
| **Diário Editorial** | — | Voz da marca, opinião, manifesto. Pouco SEO, muito branding | 1/mês |

---

## 🎨 Identidade visual do blog

### Tokens herdados do Design System

```css
--fm-brand: #ACC435;   /* lima — CTA e destaques */
--fm-font-display: "obviously-narrow", sans-serif;
--fm-font-body: "Archivo", sans-serif;
```

### Tokens NOVOS exclusivos do blog

```css
:root {
  /* Leitura longa */
  --blog-text:       #1a1a1a;
  --blog-text-soft:  #4a4a4a;
  --blog-rule:       #e6e6e6;
  --blog-highlight:  #f4f9d8;  /* fundo de pull-quote/TL;DR */
  --blog-link:       #6a8a0f;  /* lima escurecido p/ contraste AA */
  --blog-link-hover: #4d6608;

  /* Tipografia de leitura */
  --blog-body-size:    18px;
  --blog-body-leading: 1.7;
  --blog-measure:      68ch;   /* largura ótima de leitura */

  --blog-shadow-soft: 0 10px 40px rgba(0,0,0,.06);
}
```

> ⚠️ **Contraste:** o `#ACC435` reprova WCAG AA sobre branco para texto. Em links e texto sobre fundo claro use `--blog-link` (`#6a8a0f`). O verde original fica para badges, CTAs (com texto preto) e elementos decorativos.

### Tipografia editorial

| Elemento | Família | Desk | Mob | Peso |
|---|---|---|---|---|
| H1 capa do artigo | obviously-narrow | 64px | 36px | 600 |
| H2 seção | obviously-narrow | 36px | 28px | 700 |
| H3 sub-seção | Archivo | 24px | 20px | 600 |
| Kicker / categoria | obviously-narrow | 13px | 12px | 700 (tracking 6px) |
| Body | Archivo | 18px | 17px | 400 |
| Pull quote | obviously-narrow | 28px | 24px | 600 |
| Caption / meta | Archivo | 14px | 13px | 500 |
| TL;DR / FAQ Q | Archivo | 17px | 16px | 600 |

### Sistema de cards

| Card | Uso | Especificação |
|---|---|---|
| **Hero Editorial** | Topo home, post em destaque | Imagem 16:9, raio 20px, badge categoria pílula verde |
| **Padrão** | Grid de artigos | Imagem 4:3, raio 16px, badge, H3, excerpt 2 linhas |
| **Compacto** | Sidebar, posts relacionados | Imagem 1:1 esquerda, raio 12px |
| **Produto Contextual** | Dentro do artigo | Fundo `--fm-card-dark`, CTA verde, imagem do pote 1:1 |
| **TL;DR** | Topo do artigo | Fundo `--blog-highlight`, borda esquerda verde 4px, 3-5 bullets |
| **FAQ** | Final do artigo | Accordion, divisor `--blog-rule` |

### Componentes proprietários

- **Kicker condensado em lima** sobre H1
- **Pull-quote** com aspas tipográficas grandes em lima sobre texto preto
- **Selo "Revisado por"** com foto + credencial (clicável para autor)
- **TOC sticky** — lateral em desktop, accordion no topo em mobile
- **Newsletter inline** — bloco verde lima com texto preto e input pill
- **Barra de progresso de leitura** — linha lima 3px no topo
- **Botão "Continuar lendo"** — pill verde com ícone circular

---

## 🛠️ Skills do Claude para o blog

| Skill | Função |
|---|---|
| `/blog-research` | Pesquisa de pauta (HN + Reddit + SEO + E-E-A-T) |
| `/blog-brief` | Brief estruturado a partir de pauta aprovada |
| `/blog-writer` | Escreve o post em HTML semântico |
| `/blog-review` | Auditoria de SEO + qualidade + voz (score 0-100, aprova se 90+) |
| `/blog-publish` | Publica no repo, atualiza índice, prepara deploy |
| `/blog-orchestrator` | Roda o pipeline inteiro com checkpoints humanos |

**Configuração de cliente:** `/.claude/skills/blog-research/references/clients/soufit.md`

---

## 📅 Cadência editorial sugerida

| Mês | Output mínimo |
|---|---|
| Posts cluster | 4-6 |
| Guia prático ou Mito x Verdade | 1-2 |
| Ingrediente em profundidade | 1 |
| Receita funcional | 2 |
| Diário editorial | 1 |
| **TOTAL** | **9-12 posts/mês** |

Pillar pages: 1 lançamento por trimestre até completar as 6.
