# 10 — Mapa de Arquivos-Fonte

> Localização canônica de cada documento no repositório Modernitty.
> Use este mapa para responder "onde está o arquivo X?" e para confirmar dados antes de afirmar.

---

## 📍 Raiz do repositório

```
/Users/mateusrucci/Desktop/meus-scripts-apps-script/Modernitty/
```

---

## 📚 Arquivos-mestre (consulte ANTES de criar conteúdo)

| Arquivo | Caminho relativo | Conteúdo | Tamanho |
|---|---|---|---|
| **Índice de Produtos** | `Produtos/INDICE.md` | Navegação dos 20 produtos | 237 linhas |
| **Cross-sell** | `Produtos/CROSS-SELL.md` | 10 kits + sinergias + overlaps | 331 linhas |
| **Auditoria regulatória** | `Produtos/AUDITORIA-CONSISTENCIA.md` | Nota 72/100 + 3 falhas sistêmicas | — |
| **Compilado Copy Master** | `Copy Master/COMPILADO-MASTER-COPYWRITING.md` | 5 livros bíblia destilados | 489 linhas |
| **Design System** | `Design System/design-system-fitmoderno.md` | Brandbook v2 completo | 335 linhas |
| **Blog Scope** | `Blog/blog-scope.md` | Tese editorial + arquitetura | 28kB |
| **Processo de LP** | `Processo de Aula/PROCESSO-LP-ALTA-PERFORMANCE.md` | 8 fases de produção de LP | 43kB |
| **README Deploy** | `README-deploy.md` | Regras HostGator + UTM + Pixel | 146 linhas |

---

## 💊 Dossiês de Produto (20 SKUs)

**Localização padrão:** `Produtos/<Nome>/<Nome>.md`

```
Produtos/
├── Fit Moderno/Fit Moderno.md                       (556 linhas)
├── Puro Bronze/Puro Bronze.md                       (651 linhas)
├── Ácido Hialurônico/Ácido Hialurônico.md           (677 linhas)
├── Colágeno Hidrolisado/Colágeno Hidrolisado.md     (599 linhas)
├── Chocotox/Chocotox.md                             (473 linhas)
├── Oh!chá/Oh!chá.md                                 (481 linhas)
├── Colágeno + AH + Vitamina C/...md                 (540 linhas)
├── Vitali Pro+/Vitali Pro+.md                       (570 linhas)
├── Melatonina + L-Triptofano/...md                  (465 linhas)
├── Imune AZ/Imune AZ.md                             (563 linhas)
├── NAC/NAC.md                                       (497 linhas)
├── Coenzima Q10/Coenzima Q10.md                     (506 linhas)
├── Cúrcuma + Vitamina K2/...md                      (513 linhas)
├── Ômega 3/Ômega 3.md                               (497 linhas)
├── Multivitamínico Homem/Multivitamínico Homem.md   (528 linhas)
├── Multivitamínico Mulher/Multivitamínico Mulher.md (667 linhas)
├── Multivitamínico Sênior/Multivitamínico Sênior.md (657 linhas)
├── Magnésio 5 em 1/Magnésio 5 em 1.md               (538 linhas)
├── Whey Protein 80%/Whey Protein 80%.md             (576 linhas)
└── Creatina 3 em 1/Creatina 3 em 1.md               (499 linhas)
```

**Cada dossiê tem 14 seções padronizadas** (ver `02-portfolio-produtos.md`).

---

## 🏗️ Repositório de LP (`lp.soufit.com/`)

```
lp.soufit.com/
├── README.md                        ← CENTRAL DE OPERAÇÕES (comece aqui)
├── PROCESSO.md                      ← checklist seco
├── BRIEFING-LP.md                   ← guia de briefing (caminhos A/B/C)
├── DEPLOY.md                        ← deploy técnico
├── CONTRIBUTING.md                  ← como contribuir
├── AGENTS.md                        ← skills usadas
├── .cpanel.yml                      ← tarefas de deploy
├── .github/workflows/deploy.yml     ← CI/CD
├── lp-taxonomy.json                 ← taxonomia das LPs
├── 00-base/                         ← biblioteca interna
│   └── (espelha Produtos/, Copy Master/, Design System/, Processo de Aula/)
├── 02-blog/                         ← vertical blog
├── 03-ads/                          ← vertical ads
├── 04-emails/                       ← vertical emails
├── 05-relatorios/                   ← (depreciado — dashboard tem repo próprio)
├── 99-referencias-externas/         ← POPs + frameworks externos
├── _tools/                          ← Apps Script, scripts internos
├── apps-script/                     ← Google Apps Script
├── docs/tracking/                   ← documentação de tracking
├── estrategia/                      ← documentos estratégicos
├── shared/                          ← scripts publicados na raiz do domínio
│   ├── utm-forwarder.js
│   ├── meta-tracking.js
│   ├── meta-capi.php
│   ├── ac-form.js
│   ├── ac-submit.php
│   └── ...
├── lp/                              ← LPs de copy publicadas
├── quiz/, upsell/, ebook/, desconto/, evento/, afiliado/, lanc/, ecom/, loja/
├── politica-de-privacidade/, termos-de-servico/, exclusao-de-dados/, ...
└── splittrack-lead-bridge.js
```

---

## 🛒 Shopify

```
shopify-theme/                       ← tema Horizon
├── assets/ (117)
├── blocks/ (95)
├── config/ (settings)
├── layout/
├── legal-pages/ (12)
├── locales/ (53 idiomas)
├── sections/ (45)
├── snippets/ (105)
└── templates/ (16)

shopify-theme.backup-20260528-235027/ ← backup automático

shopify-admin/                       ← ferramentas admin
shopify-dev-check/                   ← validações dev
shopify-live-check/                  ← validações produção
```

**Screenshots de preview:**
```
shopify-preview-cart-mobile-final.png    (348 KB)
shopify-preview-cart-mobile.png          (345 KB)
shopify-preview-home-desktop.png         (1.1 MB)
shopify-preview-home-mobile.png          (2.5 MB)
shopify-preview-product-mobile-final.png (481 KB)
shopify-preview-product-mobile.png       (493 KB)
```

---

## 📋 POPs (Procedimentos Operacionais Padrão)

```
pops-falconi/
├── POP-COPY-001 - Criar copy para materiais ricos e ebooks.docx
├── POP-CRM-001 - Estruturar fluxos de email e jornada do cliente.docx
└── POP-TRAF-001 - Fazer espionagem de trafego e montar swipe file.docx
```

---

## 📊 Outras pastas

| Pasta | Conteúdo |
|---|---|
| `Relatorios/soufit/` | Pasta vazia local — dashboard real está em VPS própria |
| `facebook ads Modernity/` | Criativos históricos Modernity |
| `emails/` | Sequências de e-mail (estrutura legada) |
| `lp/`, `quiz/`, `upsell/`, `desconto/`, `evento/`, `ebook/`, `afiliado/` | Estruturas legadas (na raiz de Modernitty, não no lp.soufit.com) |
| `lp-taxonomy-sync/` | Sincronização de taxonomia |
| `Lançamento Produto Kit 22-06/` | Vazia em 2026-05-29 (planejamento futuro?) |

---

## 🎯 Outros artefatos

| Arquivo | Caminho | Função |
|---|---|---|
| Feed XML para Meta/Google | `soufit-feed.xml` | Catálogo publicado em `lp.soufit.com/feed.xml` |
| Skill local (legado) | `skill.md` | Skill antiga (referência) |
| Skill deploy (legado) | `skill-deploy.md` | Skill antiga (referência) |
| Evals | `evals.json` | Configuração de evals |
| README global | `README-deploy.md` | Deploy HostGator (raiz) |

---

## 🔎 Como encontrar algo rapidamente

### "Onde está o dossiê do produto X?"
→ `/Modernitty/Produtos/<Nome do Produto>/<Nome do Produto>.md`

### "Onde está a regra Y do design?"
→ `/Modernitty/Design System/design-system-fitmoderno.md`

### "Como é o claim ANVISA do Z?"
→ Dossiê do produto, Seção 12 ("Reposicionamento crítico") OU `references/09-regulatorio-anvisa.md` desta skill

### "Como é deploy de LP?"
→ `/Modernitty/lp.soufit.com/DEPLOY.md` OU `references/06-operacao-tecnica.md` desta skill

### "Qual o tom para escrever para a persona X?"
→ Dossiê do produto, Seção 9 ("Posicionamento estratégico") + `references/04-design-system-voz.md` desta skill

### "Qual o cross-sell do produto X?"
→ `/Modernitty/Produtos/CROSS-SELL.md` OU `references/03-cross-sell-kits.md` desta skill

### "Quem é o público da marca?"
→ `references/01-empresa-marca.md` (resumo) + `/Modernitty/Design System/design-system-fitmoderno.md`

---

## 🆕 Auto memory associada

A memória persistente do Claude tem registros relevantes para SouFit em:

```
/Users/mateusrucci/.claude/projects/-Users-mateusrucci-Desktop-meus-scripts-apps-script-Modernitty/memory/
├── MEMORY.md (índice)
├── project_soufit_feed.md
├── project_landing_pages_processo.md
├── project_soufit_repo_central.md
├── project_soufit_ecom_pdp.md
└── project_shopify_soufit.md
```

Consulte essas memórias para informações que mudam ao longo do tempo (status de iniciativas, decisões tomadas, mudanças de estrutura).
