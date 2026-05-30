# 06 — Operação Técnica (Deploy, Tracking, LP)

> Como a operação técnica do `lp.soufit.com` funciona, regras obrigatórias de UTM e Meta Pixel, fluxo de deploy.
> Fontes canônicas:
> - `/Modernitty/README-deploy.md`
> - `/Modernitty/lp.soufit.com/DEPLOY.md`
> - `/Modernitty/lp.soufit.com/PROCESSO.md`
> - `/Modernitty/lp.soufit.com/.cpanel.yml`

---

## 🚀 Stack de deploy

| Camada | Tecnologia |
|---|---|
| **Repositório** | GitHub `mateusrucci/soufit` |
| **CI/CD** | GitHub Actions (`.github/workflows/deploy.yml`) |
| **Hospedagem** | HostGator cPanel (`br956.hostgator.com.br:2083`) |
| **Trigger** | `git push origin main` (deploy automático) |
| **Tempo** | ~25 segundos até produção |
| **Fallback** | `.cpanel.yml` (deploy manual pelo cPanel se Actions falhar) |

### Destino base no servidor

```
$HOME/lp.soufit.com/                  ← raiz do domínio
$HOME/lp.soufit.com/fitmoderno/       ← exemplo de subpasta
```

### Estrutura do repositório (verticais)

```
lp.soufit.com/                        ← repo root
├── 00-base/                          ← biblioteca (produtos, design system, copy master)
├── lp/, quiz/, upsell/, ebook/,      ← LPs publicadas (ficam NA RAIZ por restrição do .cpanel.yml)
│   desconto/, evento/, afiliado/,
│   politica-de-privacidade/,
│   termos-de-servico/,
│   exclusao-de-dados/
├── ecom/                             ← PDPs estáticos otimizados
├── loja/                             ← e-commerce dinâmico (integração Shopify)
├── lanc/                             ← lançamento (em andamento)
├── shared/                           ← scripts publicados na raiz do domínio
│   ├── utm-forwarder.js
│   ├── meta-tracking.js
│   ├── meta-capi.php
│   ├── ac-form.js
│   ├── ac-submit.php
│   └── robots.txt + root.htaccess
├── docs/tracking/                    ← documentação de tracking
├── 02-blog/, 03-ads/, 04-emails/     ← verticais internas (NÃO publicadas)
├── 99-referencias-externas/          ← POPs e frameworks externos
├── _tools/                           ← Apps Script, scripts internos
├── .cpanel.yml                       ← tarefas de deploy
└── .github/workflows/deploy.yml      ← CI/CD
```

> ⚠️ **Pastas com prefixo numérico (00-, 02-, etc) e `_tools/` NÃO vão pro site público.** Apenas as pastas da raiz sem prefixo são publicadas.

---

## 🚨 Regra obrigatória de UTM

**Toda página HTML publicada em `lp.soufit.com` DEVE incluir no `<head>`:**

```html
<script src="/utm-forwarder.js" defer></script>
```

O script preserva e propaga automaticamente entre páginas:

```
utm_source, utm_medium, utm_campaign, utm_term, utm_content, utm_id,
fbclid, gclid, gbraid, wbraid, msclkid, ttclid
```

**Checklist antes do deploy:**
1. ✅ `<script src="/utm-forwarder.js" defer></script>` presente no `<head>`
2. ✅ `shared/utm-forwarder.js` existe no repositório
3. ✅ `.cpanel.yml` copia o script para `$HOME/lp.soufit.com/`
4. ✅ Links de checkout recebem UTMs automaticamente (script adiciona)

---

## 🎯 Regra obrigatória de Meta Pixel + CAPI

**Meta Pixel ID:** `1172482898007013`

**Toda página deve incluir no `<head>`:**

```html
<script src="/utm-forwarder.js" defer></script>
<script src="/meta-tracking.js" defer></script>
```

**E o noscript fallback logo após `<body>`:**

```html
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=1172482898007013&ev=PageView&noscript=1" alt="" />
</noscript>
```

### Eventos automáticos

| Evento | Disparado quando |
|---|---|
| `PageView` | Ao carregar qualquer página |
| `AddToCart` | Ao clicar em link `https://soufit.com/comprar?...` |

### Eventos manuais

```html
<script>
window.SoufitTracker.track('Lead',
  { content_name: 'Nome do formulário' },
  { email: 'cliente@email.com' }
);
</script>
```

### Checklist antes do deploy

1. ✅ Página inclui `/meta-tracking.js`
2. ✅ Página inclui noscript fallback com pixel ID `1172482898007013`
3. ✅ `.cpanel.yml` copia `shared/meta-tracking.js` e `shared/meta-capi.php` para `$HOME/lp.soufit.com/`
4. ✅ Endpoint `/meta-capi.php` responde `status: ok` em GET

---

## 🔐 Secrets do GitHub (configurados em Settings > Secrets and variables > Actions)

```
HOSTGATOR_FTP_SERVER
HOSTGATOR_FTP_USERNAME
HOSTGATOR_FTP_PASSWORD
CPANEL_API_TOKEN   ← se usar cPanel API ao invés de FTP
```

---

## 📋 Fluxo de criação de uma LP nova

1. **Briefing** — `lp.soufit.com/BRIEFING-LP.md` (caminho A: só copy, B: só design, C: completo)
2. **Pesquisa & extração de assets** — produto, público, concorrência
3. **Estratégia de copy** — One Belief → Big Idea (frameworks em `/Copy Master/COMPILADO-MASTER-COPYWRITING.md`)
4. **Criação de copy** — camadas + checklist Evaldo/Kern
5. **Construção técnica** — HTML semântico mobile-first
6. **SEO + performance** — Schema.org + Core Web Vitals
7. **Deploy automatizado** — `git push origin main`
8. **Tracking + UTMs + integrações** — confirmar UTM, Pixel, CAPI
9. **Variações + A/B test** — iteração baseada em dados

**Tempo típico:**
- Simples: 4-8h
- Complexa: 16-24h
- Alta conversão com A/B: 40+h

**Processo completo:** `/Modernitty/Processo de Aula/PROCESSO-LP-ALTA-PERFORMANCE.md`

---

## 🚨 Por que landings ficam na raiz (decisão 2026-05)

O `.cpanel.yml` tem ~150 paths absolutos (`shared/X.htaccess`, `lp/Y/index.html`, etc) que copiam arquivos da raiz do repo para a raiz pública. Mover as pastas para `01-landing-pages/` exigiria:

- Reescrever todos os paths do `.cpanel.yml`
- Reconfigurar `REPOSITORY_ROOT` no cPanel
- Operação cirúrgica, sem ambiente de staging, com risco de derrubar produção

**Ganho** (simetria visual com `02-blog/`, `03-ads/`) **não compensa o risco**. Decisão: landings permanecem na raiz. Conceitualmente formam a "vertical Landings" (`01-`), apenas sem o prefixo numérico.

---

## 📂 Páginas publicadas em `lp.soufit.com` (raiz)

```
/                           ← home (se houver)
/lp/                        ← LPs de copy (advertorial, captura)
/quiz/                      ← engajamento + recomendação de produto
/upsell/                    ← oferta pós-compra
/desconto/                  ← landing de cupom
/evento/                    ← lançamento, live, masterclass
/ebook/                     ← download + nutrição
/afiliado/                  ← captação de creators
/ecom/                      ← PDPs estáticos otimizados (primeira: /ecom/fitmoderno)
/loja/                      ← e-commerce dinâmico
/lanc/                      ← lançamento ativo
/sobre-nos/
/contato/
/politica-de-privacidade/
/politica-de-cookies/
/politica-de-envio/
/termos-de-servico/
/trocas-e-devolucoes/
/exclusao-de-dados/
```

---

## 🛠️ Skills relacionadas

- `/hostgator-cpanel-deploy` — deploy técnico padronizado
- `/run`, `/verify`, `/code-review` — QA antes de deploy
