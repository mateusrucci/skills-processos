# 🎯 Processo de Construção de Landing Pages de Alta Performance
## Metodologia em 8 fases — da pesquisa ao deploy validado

> **Material de aula** — Mateus Rucci · SouFit / Grupo MDT
> Versão 1.0 — Maio/2026
>
> Este documento descreve um processo reprodutível para construir landing pages que convertem **acima da média do mercado**, combinando:
> - **Pesquisa estruturada** (produto + público + concorrência)
> - **Copy de alta persuasão** (5 livros bíblia destilados)
> - **Engenharia técnica enxuta** (HTML/CSS mobile-first, SEO, performance)
> - **Deploy automatizado e validado**
> - **Cultura de A/B test contínuo**

---

## 📊 Visão Geral — As 8 Fases

```
┌───────────────────────────────────────────────────────────────────┐
│  FASE 0    Briefing & escopo                                       │
│  FASE 1    Pesquisa & extração de assets                           │
│  FASE 2    Estratégia de copy (One Belief → Big Idea)              │
│  FASE 3    Criação da copy (em camadas + checklist)                │
│  FASE 4    Construção técnica (HTML semântico mobile-first)        │
│  FASE 5    SEO + performance (Schema.org + Core Web Vitals)        │
│  FASE 6    Deploy automatizado + validação                         │
│  FASE 7    Tracking + UTMs + integrações                           │
│  FASE 8    Variações + A/B test + iteração                         │
└───────────────────────────────────────────────────────────────────┘
```

**Tempo típico de execução:**
- Página simples: 4-8 horas
- Página complexa (com pesquisa + copy autoral): 16-24 horas
- Página de alta conversão (com A/B test estruturado): 40+ horas

**Pré-requisitos do executor:**
- Markdown + HTML/CSS básico
- Noções de copy de resposta direta
- Acesso a Git / GitHub + ferramenta de deploy (Cloudflare Pages, Vercel, cPanel, Netlify)
- Stack de skills compilada (ver Apêndice C)

---

## FASE 0 · BRIEFING & ESCOPO

**Objetivo:** definir o que se vai construir antes de gastar um minuto na execução.

### 0.1 — Defina o objetivo único da página

A página é para:
- ☐ **Captura de lead** (e-book, webinar, formulário)
- ☐ **Conversão direta** (venda do produto na própria página)
- ☐ **Pré-venda / agendamento** (calendly, ligação)
- ☐ **Tráfego para checkout externo** (e-commerce, plataforma)

> ⚠️ **Regra do Um (Ogilvy):** uma página = um objetivo. Múltiplos CTAs = zero conversão.

### 0.2 — Defina o tipo de oferta

- ☐ **Promocional** (desconto, urgência real, escassez)
- ☐ **Evergreen** (preço cheio, sem urgência, brand-led)
- ☐ **Lançamento** (com janela de vendas datada)
- ☐ **Hard offer** (compra direta) vs **Soft offer** (lead → nurturing)

### 0.3 — Defina KPI primário

Sem KPI, não há sucesso. Escolha **um**:
- Taxa de conversão (cliques no CTA / visitas)
- CPA (custo por aquisição)
- ROAS
- Lead-to-sale
- Scroll depth + tempo na página (para conteúdo)

### 0.4 — Defina a URL de destino dos CTAs

A LP geralmente **não** processa o checkout — ela manda pra:
- E-commerce próprio (`/produtos/X` na sua plataforma)
- Plataforma de checkout (Kiwify, Hotmart, Eduzz, Yampi)
- WhatsApp (`wa.me/...`)
- Formulário em si (lead)

### 0.5 — Public segmentation (Schwartz)

| Nível | Características | Lead recomendado |
|---|---|---|
| **5. Mais consciente** | Já conhece marca + produto | Oferta direta |
| **4. Consciente do produto** | Conhece, não decidiu | Promessa + benefício |
| **3. Consciente da solução** | Sabe que existe solução | Solução + mecanismo |
| **2. Consciente do problema** | Sente a dor | Problema + esperança |
| **1. Inconsciente** | Não sabe nem do problema | História + Big Idea |

**📌 Sua decisão aqui muda todo o resto.** Página para tráfego frio (nível 1-2) precisa de muito mais lead emocional. Página para retargeting (nível 4-5) corta direto pra oferta.

### 0.6 — Documento de briefing (1 página max)

```markdown
PRODUTO: ___________
URL DE DESTINO DOS CTAs: ___________
OBJETIVO: ___________
KPI PRIMÁRIO: ___________
TIPO DE OFERTA: promocional / evergreen / lançamento
NÍVEL DE CONSCIÊNCIA DO PÚBLICO: 1 a 5
NÍVEL DE SOFISTICAÇÃO DO MERCADO: 1 a 5
ORÇAMENTO DE TRÁFEGO ESPERADO/MÊS: ___________
PRAZO: ___________
ENTREGÁVEL: standalone LP / página dentro de e-commerce / template
```

> **Case Fit Moderno:** decidimos LP standalone hospedada em `lp.soufit.com/fitmoderno-soufit-2/`, evergreen, KPI = conversão direta para `soufit.com/produtos/430/fit-moderno`, público nível 3-4 (já viu suplementos, talvez já viu o produto), sofisticação 4-5 (mercado saturado de termogênico/Ozempic).

---

## FASE 1 · PESQUISA & EXTRAÇÃO DE ASSETS

**Objetivo:** levantar tudo que vai compor a página antes de começar a escrever.

### 1.1 — Extração do design system existente

Se o produto já tem uma marca/site, **respeite a identidade**. Não invente.

**Fontes pra extrair:**
```bash
# Tipografia (procurar no <link> e no CSS)
curl -s "URL_PROD" | grep -oE "fonts\.googleapis\.com[^\"]*|typekit\.net/[^\"]*"

# Cores (variáveis CSS, hex codes)
curl -s "URL_PROD" | grep -oE "#[0-9a-fA-F]{6}" | sort -u

# Logos (CDN do produto)
curl -s "URL_PROD" | grep -oE "logos/[a-zA-Z0-9]+\.(png|svg|webp)"
```

**Checklist de design system:**
- ☐ Paleta de cores principal (3-5 hex)
- ☐ Fonte de display (headlines)
- ☐ Fonte de body (texto corrido)
- ☐ Logo (SVG ou PNG transparente, alta resolução)
- ☐ Padrão de border-radius (cards arredondados? cantos retos?)
- ☐ Estilo de botões (pill? retangular? gradiente?)
- ☐ Padrão de espaçamento (8px grid? 16px?)

### 1.2 — Extração de assets do produto

**Imagens do produto (de CDN do e-commerce):**
```bash
# Catalogar todas as URLs de imagem de uma página de produto
curl -s "URL_PRODUTO" | grep -oE 'https?://[^"&<> ]+\.(png|jpe?g|webp)' | sort -u

# Verificar se há srcset com múltiplas resoluções
curl -s "URL_PRODUTO" | grep -oE 'srcset="[^"]+' | head -3
```

**Vídeos, gifs, ícones, selos:**
- Print do produto em 3-5 ângulos
- Vídeo do produto (se houver)
- Selos: Anvisa, Reclame Aqui, Compre & Confie, certificações

### 1.3 — Extração de dados de oferta

Preços, variações, IDs:
```bash
curl -s "URL_PRODUTO" | grep -oE 'R\$ ?[0-9.]+,?[0-9]*' | sort -u
curl -s "URL_PRODUTO" | grep -oE '"id":[0-9]+|"slug":"[^"]+"'
```

**Você precisa saber:**
- Preço cheio
- Preço promocional (se houver)
- Parcelamento (12x sem juros? com taxa?)
- PIX (tem desconto adicional?)
- Frete (grátis acima de quanto?)
- Variações (sabor, tamanho, kit)
- Estoque

### 1.4 — Auditoria da página atual (se existir)

**Faça um audit estruturado.** Não escreva uma copy nova sem entender por que a atual não converte.

**Framework de audit (anota cada um numa lista):**

| Camada | Pergunta |
|---|---|
| **Above the fold** | Em 5 segundos eu entendo o produto, o benefício, e como comprar? |
| **Headline** | Tem promessa ou só nome do produto? Tem USP? |
| **Hero image** | Mostra o produto claramente? Existe um "antes/depois" ou lifestyle? |
| **Prova social** | Tem estrelas + número de avaliações + reviews visíveis? |
| **Tabela nutricional / ficha técnica** | Está coerente? (verifique erros de conteúdo!) |
| **Promessas / compliance** | Há alegações proibidas? (Anvisa, Procon, Meta/Google ad policies) |
| **Garantia** | Visível ou escondida? Específica ou genérica? |
| **Variações de oferta** | 1 frasco vs kit? Âncora de preço? |
| **CTAs** | Quantos? Conflitantes? Texto genérico ("comprar") ou específico? |
| **FAQ** | Existe? Cobre as objeções principais? |
| **Mobile UX** | Sticky CTA? WhatsApp flutuante? Tap targets ≥ 48px? |
| **Performance** | LCP < 2.5s? Imagens com srcset? CSS inline crítico? |
| **Trust signals** | Selos Anvisa, SSL, CNPJ, endereço, política? |

### 1.5 — Dossiê técnico do produto

Para produtos científicos (suplementos, cosméticos, eletrônicos), você precisa de **um dossiê interno** que cobre:

- ☐ Ficha técnica completa (composição, dose, modo de uso)
- ☐ Para cada ativo/feature: o que faz, como atua, estudo ou referência
- ☐ Sinergias entre componentes
- ☐ Contraindicações e segurança
- ☐ Diretrizes regulatórias (o que pode e o que não pode falar)

> **Case Fit Moderno:** o dossiê tinha 556 linhas com mecanismo de cada um dos 13 ingredientes + 50+ estudos científicos referenciados + lista de "armadilhas de copy" (Anvisa). **Sem esse documento, a copy era genérica.** Com ele, conseguimos citar Briskey 2022, Anton 2008, Parnell 2009 etc. — autoridade real.

### 1.6 — Compliance regulatório

Antes de escrever qualquer copy, **liste o que NÃO pode dizer** no seu nicho:

| Nicho | Regulador | Termos proibidos comuns |
|---|---|---|
| Suplementos | Anvisa (RDC 27/2010, 243/2018) | "emagrece", "perde X kg", "queima gordura", "detox", "cura", "substitui medicamento" |
| Cosméticos | Anvisa | "rejuvenesce", "elimina rugas", "tratamento de" |
| Saúde mental | CFP/CFM | "cura ansiedade", "antidepressivo natural" |
| Finanças | CVM | "garantido", "sem risco", "rentabilidade fixa" |
| Educação | MEC | "diploma garantido em X meses" |

> **Regra de ouro:** se você não tem certeza, **substitua por linguagem de claim funcional reconhecido** (Anvisa, EFSA, FDA). Ex: em vez de "queima gordura", use "contribui para o metabolismo normal de gorduras".

---

## FASE 2 · ESTRATÉGIA DE COPY

**Objetivo:** definir a arquitetura mental da copy antes de escrever uma palavra. Aqui você usa a skill de copywriting (compilado dos 5 livros).

> 📖 **Skill obrigatória:** `/Users/.../Copy Master/COMPILADO-MASTER-COPYWRITING.md` (ou equivalente). Esse documento destila Masterson, Makepeace, Evaldo, Kern e Schwartz em ~500 linhas executáveis.

### 2.1 — Defina o ONE BELIEF (Evaldo — 16 palavras)

**Template:**
> "[Nova oportunidade] é a chave para [satisfazer desejo profundo] e só é alcançável através do [novo mecanismo nomeado]."

**Componentes:**
- Nova oportunidade (USP único)
- Desejo profundo do público (não superficial)
- Novo mecanismo (o "molho secreto" — dê um nome próprio)

> **Case Fit Moderno:** *"Equilibrar serotonina + glicose + saciedade é a chave para emagrecer sem sofrer e só é alcançável através do Complexo Fit 13™."*

### 2.2 — Defina a BIG IDEA (Ogilvy — uma frase)

A Big Idea é o que sobra na cabeça da pessoa depois que ela fecha a página. **Uma frase. Memorável. Polarizadora.**

**Critérios:**
- Reframe (vira a narrativa de cabeça pra baixo)
- Justifica o fracasso passado (Blair Warren)
- Abre curiosidade (ativa dopamina)
- Promete um benefício final

> **Case Fit Moderno:** *"A causa da sua vontade de doce não é falta de disciplina. É falta de serotonina."*

### 2.3 — Mapeie a Persona

Para cada produto, escreva (1 página):

```markdown
PERSONA: ___________
IDADE / GÊNERO: ___________
RENDA / CLASSE SOCIAL: ___________

RESULTADO DOS SONHOS (o que ela quer no fundo):
___________

PROBLEMA MAIS URGENTE (o que tira o sono):
___________

O QUE ELA QUER EVITAR:
___________

CRENÇA SOBRE O PROBLEMA (hoje):
___________

CRENÇA A QUEBRAR (e substituir por):
___________

EMOÇÃO AO BUSCAR SOLUÇÃO:
___________ (cansaço, esperança, raiva, vergonha, medo)

CANAL DE DECISÃO:
Onde compra? O que pesquisa antes? Quem influencia?
```

### 2.4 — Defina os inimigos comuns (Kern + Evaldo)

Inimigo comum libera ocitocina (sensação de "estamos juntos contra eles").

**Sempre 2-3 inimigos:**
- Inimigo do problema atual (indústria de dieta, Big Pharma, etc)
- Inimigo da narrativa errada ("é falta de força de vontade")
- Inimigo do concorrente (produtos pobres / soluções incompletas)

### 2.5 — Escolha o tipo de Lead (Masterson — 6 tipos)

| Tipo | Quando usar |
|---|---|
| Lead de Oferta | Público nível 5 (mais consciente) |
| Lead de Promessa | Público nível 4 |
| Lead de Solução de Problemas | Público nível 2-3 |
| Lead de Bolsa de Veludo (segredo) | Curiosidade alta (publicações financeiras) |
| Lead de Revelação | Descoberta científica / conspiração (saúde, política) |
| Lead de História/Big Idea | Público nível 1 (frio, inconsciente) |

### 2.6 — Liste os 10 questions de Evaldo

Antes de escrever, **responda em uma linha cada** as 10 perguntas que a copy DEVE responder:

1. Como isso é diferente de tudo que já vi?
2. Por que devo me importar?
3. Como sei que isso é verdade? (provas)
4. Por que não estou tendo sucesso até agora?
5. Quem é o culpado?
6. Por que agora?
7. Por que eu deveria confiar em vocês?
8. Como funciona? (mecanismo)
9. Como posso começar? (oferta)
10. O que tenho a perder? (garantia + risco reverso)

Se não souber responder uma, **pare e pesquise**. Não escreva sem ter resposta para todas.

---

## FASE 3 · CRIAÇÃO DA COPY

**Objetivo:** escrever a copy em camadas, aplicando o framework dos 5 livros.

### 3.1 — Estrutura padrão de página de alta conversão

Esta é a sequência que comprovadamente funciona em 95% dos nichos. Adapte ao seu objetivo:

```
┌─────────────────────────────────────────────────────┐
│ 1.  TOPBAR (informativo, sem urgência falsa)         │
│ 2.  HEADER (logo + nav + CTA)                        │
│ 3.  HERO                                              │
│       ├─ Eyebrow (USP em 6 palavras)                 │
│       ├─ H1 Big Idea                                 │
│       ├─ Subtítulo (mecanismo em 2 linhas)           │
│       ├─ Bullets validação (3-4)                     │
│       ├─ Estrelas + nº avaliações                    │
│       ├─ Preço + parcelamento                        │
│       ├─ CTA primário grande                         │
│       └─ Microcopy de segurança                      │
│ 4.  POLARIZAÇÃO (Kern — "Não é pra você se...")      │
│ 5.  TRUST STRIP (4 colunas com números)              │
│ 6.  LEAD emocional (Pergunta 4 + 5)                  │
│ 7.  MECANISMO (Pergunta 8)                            │
│ 8.  PROVA / Ingredientes / Features (Pergunta 3)     │
│ 9.  AUTORIDADE (Pergunta 7)                           │
│ 10. WHY FAILED (Blair Warren)                         │
│ 11. PROVA SOCIAL (reviews + autoridade)               │
│ 12. COMPARAÇÃO (com inimigos comuns)                  │
│ 13. OFERTA / Value Ladder (Pergunta 9)                │
│ 14. GARANTIA + ANTI-GARANTIA (Pergunta 10)            │
│ 15. WHY NOW (Pergunta 6 — sem urgência falsa)         │
│ 16. CLOSE com 3 opções (Carlton/Kern)                 │
│ 17. CTA FINAL                                          │
│ 18. P.S. (revende a oferta)                            │
│ 19. FAQ (14-16 perguntas — mata objeções)             │
│ 20. FOOTER (compliance + selos)                        │
│ 21. STICKY MOBILE CTA (preço + botão)                  │
│ 22. WHATSAPP FLOAT                                     │
└─────────────────────────────────────────────────────┘
```

### 3.2 — Regra da escrita em camadas

Escreva em **3 passadas**:

**Passada 1 — Esqueleto (1h)**
- Headline + subtítulo
- Lista de bullets do hero
- Section-heads (H2) de cada seção
- CTA principal

**Passada 2 — Recheio (3-5h)**
- Lead emocional completo
- Mecanismo explicado
- Reviews placeholders alinhadas com a dor
- FAQ (responda às 10 perguntas)
- P.S. que revende

**Passada 3 — Polimento (1-2h)**
- Aplicar momentum (Makepeace): subheads a cada 200-300 palavras
- Substituir frases longas por curtas
- Verbo de ação em cada parágrafo
- Substituir palavras técnicas por coloquiais
- Verificar que cada claim tem prova

### 3.3 — Checklist de copy (antes de passar pro tech)

**Estrutura**
- ☐ One Belief claro (16 palavras)
- ☐ Big Idea em uma frase
- ☐ Lead segura nos primeiros 30 segundos
- ☐ 10 perguntas de Evaldo respondidas
- ☐ 9 etapas Carlton/Kern no close

**Prova**
- ☐ Cada claim tem prova (estudo, depoimento, número)
- ☐ Estrutura ABT (and-but-therefore) em vez de dados secos
- ☐ 3 histórias de credibilidade

**Emoção**
- ☐ Inimigo comum claro
- ☐ Desejo profundo (não superficial — não é "perder peso", é "voltar a se sentir confortável no espelho")
- ☐ Justifica fracasso passado
- ☐ Dá esperança real

**Oferta**
- ☐ Value Ladder claro (1/2/3 kits ou opções)
- ☐ Garantia específica e tangível
- ☐ Escassez real (se houver)
- ☐ CTA único e específico

**Push-Pull**
- ☐ Não pareço desesperado
- ☐ Polarizei desde o início
- ☐ 3 opções no final
- ☐ P.S. revende a oferta

> **Padrão de qualidade:** se você marcar "sim" em 80%+, está pronto. Senão, ajuste.

---

## FASE 4 · CONSTRUÇÃO TÉCNICA (HTML SEMÂNTICO MOBILE-FIRST)

**Objetivo:** transformar a copy em código que carrega rápido, renderiza em qualquer device e é navegável por humanos e bots.

### 4.1 — Arquitetura HTML

**Boilerplate inicial:**
```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>[TÍTULO COM BIG IDEA] | [MARCA]</title>
  <meta name="description" content="[150-160 caracteres com benefício principal + USP]">
  <link rel="canonical" href="[URL CANÔNICA]">

  <!-- Open Graph -->
  <meta property="og:title" content="[H1 ou variação]">
  <meta property="og:description" content="[Mesmo de description ou versão alternativa]">
  <meta property="og:type" content="product">
  <meta property="og:url" content="[URL]">
  <meta property="og:image" content="[URL DA IMAGEM HERO]">

  <!-- Performance: preconnect a tudo que é crítico -->
  <link rel="preconnect" href="[CDN DE IMAGENS]">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <!-- Preload da imagem hero (LCP) -->
  <link rel="preload" as="image" href="[IMG HERO]" fetchpriority="high">

  <!-- Schema.org -->
  <script type="application/ld+json">{...Product...}</script>
  <script type="application/ld+json">{...FAQPage...}</script>

  <!-- Tracking (carregado por defer pra não bloquear LCP) -->
  <script src="/utm-forwarder.js" defer></script>
  <script src="/meta-tracking.js" defer></script>

  <!-- CSS inline (crítico) -->
  <style>...</style>
</head>
<body>
  <!-- ... seções ... -->
</body>
</html>
```

### 4.2 — Princípios de CSS mobile-first

**Variáveis CSS no root (design system):**
```css
:root {
  --page: #f6f8ec;
  --ink: #16332b;
  --brand: #a1c41e;
  --line: rgba(8, 44, 36, 0.12);
  --font-display: "...", sans-serif;
  --font-body: "Archivo", Arial, sans-serif;
  --container: 1160px;
  --shadow: 0 24px 70px rgba(8, 44, 36, 0.13);
}
```

**Regras inquebráveis:**
- ☐ Mobile-first: estilos base são mobile, `@media (min-width: ...)` adiciona desktop
- ☐ `box-sizing: border-box` em tudo
- ☐ Container fluido: `width: min(100% - 32px, var(--container))`
- ☐ Typography responsiva: `font-size: clamp(min, ideal, max)`
- ☐ Imagens: `max-width: 100%; height: auto; display: block`
- ☐ Tap targets: botões ≥ 48px de altura
- ☐ Sticky mobile CTA: `position: fixed; bottom: 0` + `env(safe-area-inset-bottom)` para iPhone notch
- ☐ Smooth scroll: `html { scroll-behavior: smooth }`

### 4.3 — Componentes obrigatórios (alta conversão)

```html
<!-- 1. TOPBAR com benefício duro -->
<div class="topbar">...</div>

<!-- 2. HEADER sticky -->
<header class="site-header"><nav>...</nav></header>

<!-- 3. HERO com grid 2 colunas -->
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">...</span>
      <h1>...</h1>
      <p class="hero-sub">...</p>
      <ul class="hero-list">...</ul>
      <div class="rating-row">★★★★★ 4,9 · 7.684 avaliações</div>
      <div class="price-card">...</div>
      <a class="btn brand lg" href="#oferta">CTA →</a>
      <div class="micro">🔒 🚚 💳</div>
    </div>
    <div class="hero-media">
      <img class="product" src="..." fetchpriority="high">
    </div>
  </div>
</section>

<!-- 4. POLARIZAÇÃO -->
<!-- 5. TRUST STRIP -->
<!-- 6. LEAD com 2 colunas (texto + imagem) -->
<!-- 7. MECANISMO em grid 3x2 -->
<!-- 8. INGREDIENTES (anchor + tabela) -->
<!-- 9. AUTORIDADE com stats -->
<!-- 10. SOCIAL PROOF grid 3x2 reviews -->
<!-- 11. COMPARAÇÃO 3 colunas -->
<!-- 12. OFERTA 3 cards (featured no centro) -->
<!-- 13. GARANTIA + ANTI-GARANTIA -->
<!-- 14. WHY NOW (dark block) -->
<!-- 15. 3 OPÇÕES close -->
<!-- 16. FINAL CTA dark -->
<!-- 17. P.S. card -->
<!-- 18. FAQ accordion -->
<!-- 19. FOOTER -->
<!-- 20. WHATSAPP FLOAT -->
<!-- 21. STICKY MOBILE CTA -->
```

### 4.4 — JavaScript mínimo (e suficiente)

Não use framework. Use vanilla JS para:

```javascript
// FAQ accordion
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.closest('.faq-item').classList.toggle('open');
  });
});

// Smooth scroll para âncoras
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', (e) => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({behavior: 'smooth', block: 'start'});
    }
  });
});
```

**Regras:**
- ☐ Zero dependência externa (sem jQuery, sem React, sem Vue)
- ☐ JS de no máximo 50 linhas
- ☐ Inline no fim do body (não no head)
- ☐ `defer` para tracking scripts

---

## FASE 5 · SEO + PERFORMANCE

**Objetivo:** página que ranqueia bem e carrega em ≤ 2.5s no LCP.

### 5.1 — SEO técnico (checklist)

- ☐ `<title>` único, 50-60 chars, com palavra-chave principal
- ☐ `<meta name="description">` 140-160 chars, com benefício + CTA implícito
- ☐ `<link rel="canonical">` apontando pra própria URL
- ☐ `<h1>` único na página, com Big Idea
- ☐ Hierarquia H2 → H3 → H4 limpa (sem pular níveis)
- ☐ Imagens com `alt` descritivo (não "image1.png")
- ☐ Links internos com texto âncora descritivo
- ☐ `<html lang="pt-BR">` correto
- ☐ Open Graph completo (og:title, og:description, og:image, og:type, og:url)
- ☐ Twitter cards (mesma estrutura do OG)
- ☐ Schema.org: pelo menos **Product + Organization + FAQPage**

**Exemplo de Schema Product:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Fit Moderno",
  "image": "...",
  "description": "...",
  "brand": {"@type": "Brand", "name": "SouFit"},
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "7684"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "BRL",
    "price": "219.90",
    "availability": "https://schema.org/InStock",
    "url": "..."
  }
}
```

### 5.2 — Performance: Core Web Vitals

**Metas Google:**
- LCP (Largest Contentful Paint) < 2.5s
- CLS (Cumulative Layout Shift) < 0.1
- INP (Interaction to Next Paint) < 200ms

**Como atingir:**

| Métrica | Técnica |
|---|---|
| **LCP** | `<link rel="preload">` da imagem hero · `fetchpriority="high"` · CDN com srcset · CSS crítico inline |
| **CLS** | Reservar dimensões (width/height) em `<img>` · evitar fontes que mudam tamanho (use `font-display: swap`) · não injetar conteúdo acima do fold via JS |
| **INP** | JS mínimo · sem listeners pesados no scroll · evitar bibliotecas grandes |

**Otimização de imagens:**
```html
<img src="image.webp"
     srcset="image-400.webp 400w,
             image-800.webp 800w,
             image-1200.webp 1200w"
     sizes="(max-width: 768px) 100vw, 50vw"
     width="800" height="1000"
     alt="..."
     loading="lazy"
     decoding="async">
```

**Para a imagem HERO:** adicione `fetchpriority="high"` e remova `loading="lazy"`.

### 5.3 — Auditoria (ferramentas)

Antes de fazer deploy, rode:

```bash
# Lighthouse local (Chrome DevTools)
# OU
npx lighthouse https://lp.exemplo.com/ --view

# PageSpeed Insights
open "https://pagespeed.web.dev/analysis?url=URL_AQUI"

# WebPageTest (mais detalhado)
open "https://www.webpagetest.org/"
```

**Metas mínimas:**
- Lighthouse Performance ≥ 90 (mobile)
- Lighthouse SEO ≥ 95
- Lighthouse Best Practices ≥ 90
- Lighthouse Accessibility ≥ 90

---

## FASE 6 · DEPLOY AUTOMATIZADO + VALIDAÇÃO

**Objetivo:** página no ar com pipeline reprodutível e validação de que está realmente publicada.

### 6.1 — Stack de deploy recomendada

| Opção | Quando usar |
|---|---|
| **Cloudflare Pages** | LP simples, CDN global grátis, SSL automático |
| **Vercel / Netlify** | Mesmo perfil, ótimo DX |
| **cPanel (HostGator/Hostinger)** | Quando o cliente já tem domínio + hospedagem tradicional |
| **GitHub Pages** | Apenas hobby ou docs (não use para LP com tracking) |
| **Plataforma de e-commerce** | Apenas se a edição vai no painel admin (Shopify, MDT, Tray) |

### 6.2 — Pipeline com GitHub Actions (cPanel)

**Estrutura mínima:**
```
projeto/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── .cpanel.yml             (fallback de deploy manual)
├── shared/                 (assets compartilhados)
│   ├── utm-forwarder.js
│   ├── meta-tracking.js
│   ├── root.htaccess
│   └── robots.txt
└── nome-da-lp/
    ├── index.html
    └── assets/
```

**`.github/workflows/deploy.yml` (essencial):**
```yaml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }

      - name: Pull on cPanel (Git Version Control)
        env:
          TOKEN: ${{ secrets.CPANEL_API_TOKEN }}
        run: |
          curl -fsS -H "Authorization: cpanel USER:$TOKEN" \
            "https://HOST:2083/execute/VersionControl/update?repository_root=PATH&branch=main"

      - name: Trigger cPanel Deploy
        env:
          TOKEN: ${{ secrets.CPANEL_API_TOKEN }}
        run: |
          curl -fsS -H "Authorization: cpanel USER:$TOKEN" \
            "https://HOST:2083/execute/VersionControlDeployment/create?repository_root=PATH"
```

### 6.3 — Checklist pré-deploy

- ☐ Página testada em mobile e desktop
- ☐ Todos os CTAs apontam para URL correta de checkout
- ☐ Imagens carregando (sem 404)
- ☐ FAQ accordion funcionando
- ☐ Sticky mobile CTA aparecendo em < 820px
- ☐ Schema.org validado em https://validator.schema.org/
- ☐ Open Graph testado em https://www.opengraph.xyz/
- ☐ Lighthouse rodado (todas as metas atingidas)
- ☐ Compliance verificado (sem alegações proibidas)
- ☐ Scripts de tracking incluídos (`<script src="/utm-forwarder.js" defer>`)

### 6.4 — Validação pós-deploy

```bash
# 1. Status HTTP
COMMIT=$(git rev-parse --short HEAD)
curl -sI "https://URL/?v=$COMMIT" | head -5
# Esperado: HTTP/2 200

# 2. Conteúdo crítico está no ar?
curl -s "https://URL/?v=$COMMIT" | grep -oE "BIG_IDEA_PARTE|PRECO_NOVO"
# Esperado: ambos retornam

# 3. Tracking scripts carregam?
curl -sI "https://URL/utm-forwarder.js" | head -3
curl -sI "https://URL/meta-tracking.js" | head -3
# Esperado: ambos HTTP 200

# 4. Schema.org válido (cole no validator)
open "https://validator.schema.org/#url=URL"
```

---

## FASE 7 · TRACKING + UTMs + INTEGRAÇÕES

**Objetivo:** garantir que cada clique → checkout → venda seja rastreado, atribuído e otimizado.

### 7.1 — Stack de tracking mínima

| Camada | Ferramenta | Onde colocar |
|---|---|---|
| Browser-side | **Meta Pixel** (Facebook) | `<script>` no head |
| Browser-side | **Google Tag (GA4)** | `<script>` no head |
| Server-side | **Meta Conversions API** | PHP/Node no servidor |
| Atribuição | **UTM Forwarder** custom | JS que pega UTMs da URL e passa pra todos os links |
| Session | **Hotjar / Microsoft Clarity** | Heatmap + session recording |

### 7.2 — UTM Forwarder (pattern que usamos no SouFit)

Arquivo `utm-forwarder.js` na raiz do domínio:
```javascript
(function () {
  var KEYS = ["utm_source","utm_medium","utm_campaign","utm_term",
              "utm_content","utm_id","fbclid","gclid","gbraid","wbraid","msclkid","ttclid"];
  var STORAGE = "tracking_params";

  // Pegar UTMs da URL atual ou do localStorage
  var current = new URLSearchParams(window.location.search);
  var stored = JSON.parse(localStorage.getItem(STORAGE) || "{}");
  KEYS.forEach(function(k) {
    var v = current.get(k);
    if (v) stored[k] = v;
  });
  localStorage.setItem(STORAGE, JSON.stringify(stored));

  // Decorar todos os links externos com os UTMs
  document.querySelectorAll('a[href]').forEach(function(a) {
    try {
      var u = new URL(a.href);
      KEYS.forEach(function(k) {
        if (stored[k] && !u.searchParams.has(k)) u.searchParams.set(k, stored[k]);
      });
      a.href = u.toString();
    } catch(e) {}
  });
})();
```

**Por que isso importa:** o cliente clica no ad com UTM `utm_source=meta&utm_campaign=fitmoderno_v2`, navega na LP, clica no CTA que vai pra `soufit.com/produtos/430/fit-moderno` — **com os UTMs já anexados na URL final** → atribuição preserva.

### 7.3 — Setup de Meta Pixel (exemplo)

```html
<!-- No <head> -->
<script>
!function(f,b,e,v,n,t,s){
  if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)
}(window, document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'PIXEL_ID');
fbq('track', 'PageView');
</script>
```

**Eventos customizados a disparar:**
- `Lead` — submit de formulário
- `InitiateCheckout` — clique no CTA principal (LP → checkout)
- `ViewContent` — entrada na LP
- `AddToCart` — se houver
- `Purchase` — só no servidor de checkout

### 7.4 — Server-side tracking (CAPI)

**Por que:** browser-side perde ~30% dos eventos devido a ad blockers e iOS Privacy. Server-side (Conversions API) cobre o gap.

**Implementação básica (PHP):**
```php
// shared/meta-capi.php
$accessToken = getenv('META_CAPI_TOKEN');
$pixelId = getenv('META_PIXEL_ID');
$eventData = [
  'event_name' => 'Lead',
  'event_time' => time(),
  'user_data' => [...hashed...],
  'custom_data' => [...]
];
// POST para graph.facebook.com/PIXEL_ID/events
```

> ⚠️ **Nunca exponha o `CAPI_TOKEN`** em HTML/JS — sempre server-side.

---

## FASE 8 · VARIAÇÕES, A/B TEST E ITERAÇÃO

**Objetivo:** validar empiricamente qual angular vende mais.

### 8.1 — Estratégia de variações

**Crie no mínimo 2 variações pareadas** que diferem em **1 dimensão crítica**:

| Dimensão | Variação A | Variação B |
|---|---|---|
| **Headline** | Reframe científico | Promessa direta |
| **Tom** | Premium calmo | Direct response visceral |
| **Oferta** | Sem desconto | Com desconto promo |
| **Lead** | História de problema | Revelação científica |
| **Hero image** | Produto isolado | Lifestyle / antes-depois |

> **Case Fit Moderno:** criamos 3 LPs (`fitmoderno-loja`, `fitmoderno-soufit`, `fitmoderno-soufit-2`) — mesma oferta, mesmo checkout, **3 ângulos persuasivos diferentes** para A/B test contínuo.

### 8.2 — Como rodar A/B test sem ferramenta especializada

**Método 1: Split por campanha de ads**
```
Campanha A → ad creative A → LP /v1/
Campanha B → ad creative B → LP /v2/
```
Compara CPA, ROAS, taxa de conversão por campanha. Simples, eficaz.

**Método 2: Redirecionamento server-side**
```php
// .htaccess ou similar
RewriteCond %{TIME_SEC} ^[02468]$
RewriteRule ^lp$ /v1/index.html [L]
RewriteRule ^lp$ /v2/index.html [L]
```

**Método 3: Ferramentas (quando houver budget)**
- VWO
- Convert.com
- Google Optimize (descontinuado, alternativas: Optimizely, AB Tasty)

### 8.3 — Período mínimo para significância

**Regra:** rodar até atingir **pelo menos 200 conversões por variação** OU **14 dias corridos** (o que vier primeiro).

Calcule significância estatística:
- Use https://abtestguide.com/calc/ ou similar
- Confiança mínima: 95%
- Se não bateu confiança em 14 dias, a diferença não é real — mantém a variação com melhor número de visitantes.

### 8.4 — Análise pós-teste

Para cada variação, analise:

| Métrica | Como medir |
|---|---|
| **CTR para `#oferta`** | Google Analytics ou heatmap |
| **Scroll depth** | Hotjar / Clarity |
| **Time on page** | GA4 |
| **CPA** | Plataforma de ads |
| **LTV** | CRM/checkout pós-venda |
| **Drop-off por seção** | Heatmap |

### 8.5 — Iteração baseada em heatmap

Após 14 dias, **abra o heatmap** (Clarity é grátis):

1. **Onde as pessoas paravam de scrollar?** → essa seção tá fraca
2. **Onde estavam clicando que não era link?** → adicionar CTA nesse ponto
3. **Quanto tempo gastam no FAQ?** → se muito, adicionar pergunta no hero
4. **Mobile vs desktop:** comportamento muito diferente? → talvez precisar de variação mobile separada

---

## APÊNDICE A · STACK DE FERRAMENTAS COMPLETO

### Pesquisa & Audit
- **WebFetch / curl** — extrair HTML, URLs, preços
- **Wappalyzer** — descobrir tecnologia do site concorrente
- **Lighthouse** — auditar performance/SEO
- **Wayback Machine** — versões antigas
- **SimilarWeb** — tráfego do concorrente

### Design System
- **Coolors.co** — paletas
- **Google Fonts** + **Adobe Fonts (Typekit)** — tipografia
- **TinyPNG / Squoosh** — compressão de imagem
- **Cloudinary / Imgix** — CDN com srcset automático

### Copy
- **Compilado Master Copywriting** (skill interna)
- **ChatGPT/Claude** para brainstorm (nunca pra escrever a versão final)
- **Hemingway Editor** — verificar densidade/clareza
- **Headline Analyzer (CoSchedule)** — score de headline

### Construção
- **VS Code** + extensões (Prettier, Live Server)
- **Tailwind CSS** (alternativa ao CSS custom) — quando for muito complexo
- **Astro / Eleventy** — quando virar multi-página

### Deploy
- **GitHub Actions** + **cPanel API** (case SouFit)
- **Cloudflare Pages** (alternativa moderna)
- **Vercel / Netlify**

### Tracking
- **Meta Pixel + CAPI**
- **Google Tag (GA4)**
- **Microsoft Clarity** (heatmap grátis)
- **Hotjar** (mais features, pago)

### Validação
- **PageSpeed Insights**
- **Schema.org Validator**
- **OpenGraph Debugger** (Meta Sharing Debugger)
- **AB Test Calculator**

---

## APÊNDICE B · RUBRICA DE QUALIDADE — "O QUE É ALTO NÍVEL"

Use esta tabela para autodiagnosticar qualquer LP em 5 minutos:

| Critério | ❌ Amadora (0-3) | ⚠️ Mediana (4-7) | ✅ Alto Nível (8-10) |
|---|---|---|---|
| **Headline** | Nome do produto | Promessa genérica | Big Idea com reframe |
| **Lead** | Pula direto pra feature | História sem emoção | Lead emocional que justifica fracasso passado |
| **Prova social** | "X estrelas" sem reviews | Reviews genéricas | Reviews que tocam na dor central + autoridade institucional |
| **Mecanismo** | Não tem | Lista de features | Mecanismo nomeado com sinergia explicada e estudo citado |
| **Oferta** | 1 botão "comprar" | 3 kits sem âncora clara | Value ladder com kit featured + recomendação contextualizada |
| **Garantia** | "30 dias" no rodapé | Selo visível | Garantia + anti-garantia + risco reverso |
| **FAQ** | 3-5 perguntas genéricas | 8-10 perguntas | 14-16 perguntas que matam objeções por antecipação |
| **CTA** | "Comprar" | "Comprar agora" | CTA específico ("Quero apoiar minha bioquímica hoje") |
| **Mobile UX** | Layout desktop comprimido | Adaptado | Mobile-first com sticky CTA + tap targets ≥48px |
| **Performance** | LCP > 4s | LCP 2.5-4s | **LCP < 2.5s · CLS < 0.1 · INP < 200ms** |
| **SEO técnico** | Sem schema | Schema básico | Product + FAQ + Organization + OG completo |
| **Compliance** | Alegações arriscadas | Algumas alegações soltas | Compliance + disclaimer + linguagem permitida |
| **Polarização** | Tenta agradar todos | Implícita | Caixa explícita "Não é pra você se..." |
| **Tracking** | Só pixel inline | Pixel + GA | Pixel + CAPI + UTM forwarder + heatmap |
| **A/B test** | Não tem | 1 variação | 2-3 variações com tese hipotética clara |

**Score:**
- 100-130 pontos: **Alto nível** — pronto para produção e tráfego pago
- 60-99 pontos: **Mediana** — usável mas vai performar ~50% do potencial
- < 60 pontos: **Amadora** — refazer antes de gastar mídia paga

---

## APÊNDICE C · SKILLS / DOCUMENTOS DE BASE

Para que esse processo funcione, o operador precisa ter **arquivos de referência** preparados antes:

### C.1 — Skill de Copywriting
**Arquivo:** `Copy Master/COMPILADO-MASTER-COPYWRITING.md`
**Conteúdo:** destila Masterson + Makepeace + Evaldo + Kern + Schwartz em ~500 linhas executáveis.
**Status:** ✅ existe

### C.2 — Dossiê do Produto
**Padrão:** `Produtos/[Nome]/[Nome].md`
**Conteúdo:**
- Ficha técnica
- Mecanismo de cada componente
- Estudos científicos citáveis
- Sinergias
- Compliance regulatória
- Persona e objeções

> **Importante:** sem dossiê do produto, sua copy fica genérica. **Invista nessa documentação antes de qualquer LP.**

### C.3 — Design System da Marca
**Padrão:** `Design System/design-system-[marca].md`
**Conteúdo:**
- Paleta de cores (hex)
- Tipografia (fontes + pesos)
- Logo (versões SVG/PNG)
- Padrão de componentes (botões, cards, formulários)
- Tom de voz

### C.4 — Snippets de Tracking
**Padrão:** `shared/`
- `utm-forwarder.js`
- `meta-tracking.js`
- `meta-capi.php`
- `ac-submit.php` (ActiveCampaign ou similar)
- `.htaccess` raiz

### C.5 — Template de LP (boilerplate)
**Padrão:** `Templates/lp-boilerplate/index.html`
Um HTML completo com CSS, estrutura, schema — pronto para "salvar como" e adaptar.

---

## APÊNDICE D · ERROS COMUNS A EVITAR

Coletei dos piores casos que vi/cometi:

1. **Escrever copy antes de pesquisar** → copy genérica, sem ângulo único
2. **Headline com nome do produto** → "Fit Moderno" em vez de "A causa da sua vontade de doce é falta de serotonina"
3. **Múltiplos CTAs no hero** → confusão e queda na conversão
4. **Reviews fabricadas óbvias** → derruba credibilidade
5. **Tabela nutricional com erro** → quem percebe, sai
6. **Alegações Anvisa proibidas** → reprovação em ads + risco jurídico
7. **Garantia escondida no rodapé** → cliente não vê = não compra
8. **Mobile com tap targets pequenos** → 80% do tráfego é mobile, 0% converte
9. **Imagens sem srcset** → LCP 6s+ no mobile, ads ficam caros
10. **Sentry / heatmap em produção com 100% sample** → quebra performance
11. **Hero image sem fetchpriority="high"** → LCP péssimo
12. **Esqueceu UTM forwarder** → atribuição perdida = não otimiza ads
13. **Mudou copy sem mudar URL** → cache do CDN serve versão antiga
14. **Deploy sem validar curl + browser** → "tá no ar?" "tá" e nem tá
15. **A/B test sem hipótese clara** → 3 variações de chute, nenhum aprendizado

---

## APÊNDICE E · CASE COMPLETO — FIT MODERNO (referência da aula)

Esse processo foi aplicado nas 3 variações que criamos da página de produto Fit Moderno. Use como exemplo concreto na aula.

### E.1 — Briefing
- Produto: Fit Moderno (suplemento alimentar SouFit)
- URL atual: `soufit.com/produtos/430/fit-moderno` (Next.js SSR não-editável)
- Objetivo: LP standalone como destino de ads + retargeting
- KPI: CPA via Meta Ads
- Nível público: 3-4 / Sofisticação: 4-5

### E.2 — Pesquisa
- Design system extraído: cores `--brand: #a1c41e`, fonte `obviously-narrow + Archivo`
- Imagens do CDN MDT (`static.mdt.global/products/...`)
- Dossiê de 556 linhas (13 ingredientes + 50+ estudos)
- Compliance Anvisa: lista de termos proibidos identificada
- Auditoria da página atual: 12 problemas críticos identificados

### E.3 — Estratégia (Variação 3)
- **One Belief:** "Equilibrar serotonina + glicose + saciedade é a chave para emagrecer sem sofrer e só é alcançável através do Complexo Fit 13™"
- **Big Idea:** "A causa da sua vontade de doce não é falta de disciplina. É falta de serotonina."
- **Lead:** Revelação científica + solução de problema
- **Inimigos:** Indústria de dieta + narrativa "força de vontade" + Big Pharma GLP-1

### E.4 — Copy
- 14 seções aplicando 5 livros bíblia
- 5 ingredientes-âncora destacados
- Estudos citados: Anton 2008, Briskey 2022, Parnell 2009, Cavaliere 1997
- Polarização Kern logo no início
- Anti-garantia + garantia tradicional
- 3 opções no close (Kern)
- P.S. revende

### E.5 — Tech
- HTML mobile-first, ~1.700 linhas
- CSS inline crítico (~700 linhas)
- JS vanilla (15 linhas)
- Schema.org: Product + FAQPage
- Sticky CTA mobile + WhatsApp float
- UTM forwarder ativo

### E.6 — Deploy
- GitHub Actions → cPanel HostGator
- 18 segundos do push ao live
- Validação via curl: HTTP 200 + 10 strings de copy confirmadas

### E.7 — 3 Variações no ar para A/B test
- `lp.soufit.com/fitmoderno-loja/` (promocional −24% OFF)
- `lp.soufit.com/fitmoderno-soufit/` (evergreen premium calmo)
- `lp.soufit.com/fitmoderno-soufit-2/` (evergreen direct-response visceral)

---

## 🎓 SUGESTÃO DE ROTEIRO DE AULA

### Aula 1 (2h) — Fases 0 e 1
- Briefing + escopo
- Pesquisa: como extrair design system + assets
- Auditoria de página existente
- **Exercício:** auditar uma LP escolhida pela turma

### Aula 2 (2h) — Fases 2 e 3
- Estratégia: One Belief + Big Idea + Schwartz
- Como aplicar a skill de copywriting
- **Exercício:** escrever headline + lead para o produto da aula

### Aula 3 (3h) — Fase 4
- HTML semântico
- CSS mobile-first
- Componentes obrigatórios
- **Exercício prático:** construir hero + polarização + oferta

### Aula 4 (2h) — Fases 5 e 6
- SEO + Schema.org
- Performance + Core Web Vitals
- Pipeline de deploy
- **Exercício:** deploy + validação

### Aula 5 (2h) — Fases 7 e 8
- Tracking (Pixel + GA + CAPI + UTMs)
- A/B test sem ferramenta
- Análise de heatmap
- **Exercício:** definir hipótese A/B + montar plano de iteração

### Aula 6 (3h) — Estudo de caso + workshop
- Walk-through completo do Fit Moderno
- Cada aluno aplica nas próprias LPs
- Feedback ao vivo

**Total: ~14 horas de aula** (pode comprimir em fim de semana intenso ou estender em 6 semanas)

---

> *"Uma landing page de alto nível não é arte. É engenharia de persuasão + engenharia de software + engenharia de tráfego. Cada decisão tem motivo. Cada elemento tem prova. Cada palavra tem propósito."*

**Fim do processo.**
