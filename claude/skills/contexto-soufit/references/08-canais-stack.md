# 08 — Canais & Stack Tecnológico

> Plataformas, integrações e infraestrutura da operação SouFit.

---

## 🌐 Canais de presença

| Canal | URL | Tipo |
|---|---|---|
| **Site institucional / Loja oficial** | `soufit.com` | Principal |
| **Loja Shopify (admin)** | `soufit-4448.myshopify.com` | Interno |
| **Loja Shopify (público)** | `oficial.soufit.com` | E-commerce |
| **Landings** | `lp.soufit.com` | HostGator |
| **Blog** | `soufit.com/blog/` | Editorial |
| **Dashboard interno** | `painel.soufit.com.br` | Operacional |
| **Instagram** | `@soufitmoderno` | Social |
| **Feed de catálogo** | `lp.soufit.com/feed.xml` | Meta/Google Ads |

---

## 🛒 Stack — Loja & E-commerce

### Shopify (loja principal)
- **Admin:** `soufit-4448.myshopify.com`
- **Público:** `oficial.soufit.com`
- **Tema:** Horizon (baixado em `/Modernitty/shopify-theme/`)
- **Estrutura local do tema:**
  ```
  shopify-theme/
  ├── assets/         (117 itens)
  ├── blocks/         (95 itens)
  ├── config/         (settings_schema.json, settings_data.json)
  ├── layout/         (theme.liquid + outros)
  ├── legal-pages/    (12 páginas legais)
  ├── locales/        (53 idiomas)
  ├── sections/       (45 sections)
  ├── snippets/       (105 snippets)
  └── templates/      (16 templates)
  ```
- **Backup:** `/Modernitty/shopify-theme.backup-20260528-235027/`
- **Skill admin:** ferramentas internas em `/Modernitty/shopify-admin/`

### PDPs estáticos otimizados
- **Pasta:** `/Modernitty/lp.soufit.com/ecom/`
- **Distinção:** `/ecom/` (estático otimizado) ≠ `/loja/` (dinâmico Shopify) ≠ `/lp/` (LPs de copy)
- **Primeiro deploy:** `lp.soufit.com/ecom/fitmoderno`

---

## 📊 Stack — Dashboard interno

**URL:** `painel.soufit.com.br`
**Repo:** Próprio (não no Modernitty)
**Acesso:** HTTPS com Certbot

| Camada | Tecnologia |
|---|---|
| **Backend** | FastAPI + SQLAlchemy + APScheduler |
| **Frontend** | React + Vite + TailwindCSS + Recharts |
| **Banco** | PostgreSQL |
| **Cache** | Redis |
| **Infra** | Docker Compose + Nginx |
| **Hospedagem** | VPS própria (Ubuntu/Debian) |
| **Atualização** | A cada 5 minutos (automática) |

### Integrações do dashboard

- **Meta Ads** (gasto, impressões, CTR, CPC, conversões, ROAS)
- **Instagram Graph** (seguidores, visitas, alcance)
- **Google Sheets OU ActiveCampaign** (leads por dia/origem)

---

## 🎯 Stack — Tracking

| Item | Valor |
|---|---|
| **Meta Pixel ID** | `1172482898007013` |
| **Meta CAPI** | `/meta-capi.php` (endpoint na raiz do `lp.soufit.com`) |
| **Eventos** | `window.SoufitTracker.track(...)` |
| **UTM** | `/utm-forwarder.js` (preserva entre páginas) |
| **GTM** | Camada auxiliar (ver `docs/tracking/`) |
| **Tracker (afiliados)** | RedTrack (integração via API) |

**Documentação:** `/Modernitty/lp.soufit.com/docs/tracking/README.md`

---

## 📧 Stack — E-mail & CRM

- **Plataforma:** ActiveCampaign (implícito) ou Hotmart
- **Endpoint de captura:** `shared/ac-submit.php` + `shared/ac-form.js`
- **Fluxos:** Definidos em POP-CRM-001
- **Pastas no repo:**
  - `/Modernitty/emails/` — sequências e templates
  - `/Modernitty/lp.soufit.com/04-emails/` — aquisição, e-books de captura

---

## 📊 Stack — Anúncios

- **Plataforma principal:** Meta Ads (Facebook + Instagram)
- **Plataformas secundárias:** TikTok Ads, Google Ads
- **Tracking:** Meta Pixel + CAPI (com eventID unificado)
- **Repositório de criativos:**
  - `/Modernitty/facebook ads Modernity/` — histórico Modernity
  - `/Modernitty/lp.soufit.com/03-ads/` — vertical atual
- **Skill de espionagem:** POP-TRAF-001

---

## 🔧 Stack — Automação & Scripts

| Pasta | Conteúdo |
|---|---|
| `/Modernitty/lp.soufit.com/_tools/` | Apps Script, scripts internos |
| `/Modernitty/lp.soufit.com/apps-script/` | Google Apps Script |
| `/Modernitty/lp-taxonomy-sync/` | Sincronização da taxonomia de LPs |
| `/Modernitty/shopify-dev-check/` | Validações Shopify (dev) |
| `/Modernitty/shopify-live-check/` | Validações Shopify (produção) |

### Skill para automações

- `/redtrack-api` — Google Apps Script + RedTrack
- `/clickup-task-creator` — Tarefas no ClickUp (listas Gestão e Lançamento)

---

## 📦 Stack — Hospedagem

| Domínio | Hospedagem | Plano |
|---|---|---|
| `lp.soufit.com` | HostGator cPanel (`br956.hostgator.com.br`) | Shared |
| `oficial.soufit.com` | Shopify | — |
| `painel.soufit.com.br` | VPS própria | — |
| `soufit.com` | (verificar — provavelmente Hostgator também) | — |

---

## 🔑 Acessos críticos (não armazenar nesta skill)

Os acessos sensíveis ficam **fora** do repositório (e desta skill):

- HostGator cPanel
- Shopify Partner / Admin
- Meta Business
- GitHub `mateusrucci/soufit`
- ActiveCampaign
- RedTrack
- VPS (SSH key)
- ClickUp Workspace

Para qualquer ação que exija acesso, **peça ao Mateus** e nunca tente derivar/adivinhar senhas ou tokens.

---

## 📂 Estrutura geral do repositório `Modernitty/`

```
Modernitty/                          ← repo central de operações Grupo MDT
├── Produtos/                         ← 20 dossiês técnicos de produto
├── Copy Master/                      ← COMPILADO-MASTER-COPYWRITING.md (5 livros bíblia)
├── Design System/                    ← design-system-fitmoderno.md
├── Blog/                             ← blog-scope.md (28kB)
├── Processo de Aula/                 ← PROCESSO-LP-ALTA-PERFORMANCE.md
├── Lançamento Produto Kit 22-06/    ← vazia em 2026-05-29
├── pops-falconi/                     ← 3 POPs ativos (.docx)
├── lp.soufit.com/                    ← repositório git do lp.soufit.com
├── shopify-theme/                    ← tema Horizon baixado
├── shopify-admin/                    ← ferramentas admin
├── Relatorios/soufit/                ← dashboard (repo próprio em VPS)
├── facebook ads Modernity/           ← criativos históricos
├── emails/                           ← sequências de email
├── lp/, quiz/, upsell/, desconto/   ← landings (estruturas legadas)
├── afiliado/, evento/, ebook/
├── lp-taxonomy-sync/                 ← sync de taxonomia
├── README-deploy.md                  ← regras de deploy
└── soufit-feed.xml                   ← feed Meta/Google
```
