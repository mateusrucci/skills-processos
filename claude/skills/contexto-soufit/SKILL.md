---
name: contexto-soufit
description: Contexto canônico da empresa SouFit / Grupo MDT (suplementos do Mateus Rucci). Carrega 20 produtos, design system, voz, blog, deploy lp.soufit.com, Shopify, POPs Falconi, cross-sell, ANVISA e mapa de arquivos do repo Modernitty. Use SEMPRE que mencionar "SouFit", "Soufit", "Fit Moderno", "Modernity", "Modernitty", "Grupo MDT", "minha empresa/marca/produtos", "nosso portfólio", "loja", "lp.soufit", "blog Soufit", "Shopify", produtos da casa (Whey, Creatina 3 em 1, Magnésio 5 em 1, Multi Homem/Mulher/Sênior, Ômega 3, Vitali Pro+, Imune AZ, NAC, CoQ10, Cúrcuma+K2, Melatonina+L-Trip, Colágeno, Ácido Hialurônico, Puro Bronze, Chocotox, Oh!chá, Colágeno+AH+Vit C), ou quando envolver gestão, decisão, status, brand, ICP, persona, claim ANVISA, kit, POP ou processo da casa. NÃO escreve copy (use copywriter-senior) nem produz LP — só CARREGA contexto.
---

# contexto-soufit — Contexto mestre da SouFit / Grupo MDT

Skill de **contexto** (não de produção). Carrega tudo o que o Claude precisa saber sobre a empresa do Mateus para ajudar na gestão, decisão, alinhamento e operação. Funciona como uma "memória ativa de empresa": sempre que o assunto for SouFit / MDT / Modernitty, esta skill ancora a conversa.

---

## 🧭 Como usar esta skill

1. **Leia este SKILL.md inteiro** — contém o one-pager da empresa.
2. **Identifique o tipo de pergunta** do Mateus (ver tabela "Quando carregar qual reference" abaixo).
3. **Carregue o reference específico** com `Read` antes de responder, se a pergunta exigir profundidade.
4. **Nunca invente** dados de produto, dose, claim ANVISA ou preço — sempre confirme no arquivo-fonte (mapa em `references/10-mapa-arquivos-fonte.md`).
5. **Use português brasileiro** — voz de marca acolhedora, científica, sem promessas mágicas (ver `references/04-design-system-voz.md`).

---

## 🏢 One-pager da empresa

### O que é

**SouFit** é a marca-mãe de suplementos nutricionais do **Grupo MDT**, dirigida pelo **Mateus Rucci**. Opera com marcas correlatas: **Fit Moderno** (linha de emagrecimento, marca histórica), **Modernity** e a própria SouFit como guarda-chuva.

### Posicionamento

> *"Cuidar de si pode ser leve, científico e completamente seu."* (Reposicionamento 2026)

**Segmentos:** Emagrecimento · Beleza & Longevidade · Performance Esportiva · Saúde & Bem-estar.

**Arquétipos:** Cuidador (empático, acolhedor) + Sábio (educacional, transparente).

**Promessa central:** "Emagrecimento de verdade, com tecnologia eficiente e comunicação transparente" — estendido para longevidade e performance no reposicionamento 2026.

### Portfólio (20 produtos · 7 categorias)

| Categoria | Produtos | Persona dominante |
|---|---|---|
| **Beleza / Estética** | Fit Moderno · Puro Bronze · Ácido Hialurônico · Colágeno Hidrolisado · Colágeno+AH+Vit C · Chocotox · Oh!chá | Mulher 28-50 |
| **Hormonal / Vitalidade** | Vitali Pro+ · Melatonina+L-Triptofano | Homem 30-55 / Mulher 30-50 |
| **Imunidade / Antioxidação** | Imune AZ · NAC · Coenzima Q10 · Cúrcuma+K2 | Adulto 30-60 |
| **Cardio / Metabólico** | Ômega 3 | Adulto 30-60 com cuidado preventivo |
| **Multivitamínicos** | Multi Homem · Multi Mulher · Multi Sênior 50+ | Segmentado por idade/gênero |
| **Mineral âncora** | Magnésio 5 em 1 | Adulto 25-60 (estresse, treino) |
| **Performance** | Whey Protein 80% · Creatina 3 em 1 | Praticante musculação 18-45 |

Dossiês completos (500-700 linhas cada) em `/Modernitty/Produtos/<Nome>/<Nome>.md`. Veja `references/02-portfolio-produtos.md` para o resumo navegável.

### Operação

- **Repositório central:** `/Users/mateusrucci/Desktop/meus-scripts-apps-script/Modernitty/`
- **Domínio LP:** `lp.soufit.com` (HostGator cPanel · deploy via GitHub Actions)
- **Loja Shopify:** `soufit-4448.myshopify.com` (público: `oficial.soufit.com`) — tema Horizon em `/Modernitty/shopify-theme/`
- **Blog:** `soufit.com/blog/` — 6 categorias editoriais
- **Dashboard:** `painel.soufit.com.br` (FastAPI + React + Postgres em VPS própria; repo separado)
- **Repo GitHub:** `mateusrucci/soufit`
- **Tracking:** Meta Pixel `1172482898007013` + CAPI · UTM forwarder centralizado · Eventos via `window.SoufitTracker.track(...)`

### Identidade visual

- **Verde Soufit** `#ACC435` (CTA, destaque)
- **Azul Soufit** `#4E93D1` (secundária, educacional)
- **Preto/grafite** `#302F2D` (oficial)
- **Off-white** `#F3F1F1` (fundos)
- **Tipografia:** Obviously Narrow (títulos) + Sora (corpo)
- **Logo:** apenas verde, azul, preto ou branco. NUNCA em cor de produto, nem sobre fundo verde/azul.

### Voz de marca (resumo)

✅ Empática · Educacional · Motivacional realista · Acolhedora · Girly com substância
❌ Promessas mágicas · Jargão técnico · Motivação agressiva · Tom de superioridade · Estética isolada (foco em saúde integral)

### Skills do Claude usadas pela operação

| Skill | Para quê |
|---|---|
| `/contexto-soufit` (esta) | Contexto/conhecimento da empresa |
| `/copywriter-senior` | Frameworks profundos de copy (5 livros bíblia) |
| `/blog-research`, `/blog-brief`, `/blog-writer`, `/blog-review`, `/blog-publish`, `/blog-orchestrator` | Pipeline de blog |
| `/canvas-design`, `/brandbook-creator` | Peças visuais |
| `/hostgator-cpanel-deploy` | Deploy técnico de LP |
| `/redtrack-api` | Automações de tracker |
| `/clickup-task-creator` | Gestão de tarefas |

---

## 📚 Quando carregar qual reference

| O Mateus está perguntando sobre... | Carregue |
|---|---|
| Quem é a empresa, missão, posicionamento, voz, reposicionamento 2026 | `references/01-empresa-marca.md` |
| Catálogo de produtos, dose, claim ANVISA, persona-alvo, dossiê técnico | `references/02-portfolio-produtos.md` |
| Combinações, kits, upsell, bundles, "o que vender junto", overlap a evitar | `references/03-cross-sell-kits.md` |
| Cores, tipografia, logo, voz de marca, regras de aplicação | `references/04-design-system-voz.md` |
| Blog (categorias, tom, arquitetura, calendário editorial) | `references/05-editorial-blog.md` |
| Deploy, UTM, Meta Pixel, CAPI, lp.soufit.com, GitHub Actions | `references/06-operacao-tecnica.md` |
| POPs Falconi, processos documentados (copy, CRM, tráfego) | `references/07-pops-falconi.md` |
| Stack tecnológico, Shopify, dashboard, integrações | `references/08-canais-stack.md` |
| ANVISA, claims, palavras-tabu, compliance, auditoria de copy | `references/09-regulatorio-anvisa.md` |
| Onde está cada arquivo-fonte do repositório Modernitty | `references/10-mapa-arquivos-fonte.md` |

> **Regra prática:** se a resposta exige número, claim, dose, citação textual ou caminho de arquivo, **carregue o reference correspondente** antes de responder. Se for conversa estratégica/geral, este SKILL.md já basta.

---

## 🎯 Workflow para gestão (uso típico)

### Cenário 1 — Mateus pede status / planejamento
1. Identifique vertical (LP / Blog / Ads / Email / Shopify / Dashboard / POPs).
2. Carregue `references/10-mapa-arquivos-fonte.md` para localizar materiais.
3. Se for "o que está em andamento", leia o repositório (não confie na skill — a skill tem o **canônico**, não o **atual**).

### Cenário 2 — Mateus pede decisão sobre produto / oferta
1. Carregue `references/02-portfolio-produtos.md` (resumo) e o dossiê específico do produto em `/Modernitty/Produtos/<Nome>/<Nome>.md`.
2. Se for cross-sell / kit, carregue `references/03-cross-sell-kits.md`.
3. **Sempre** valide claim e dose com o arquivo-fonte antes de afirmar.

### Cenário 3 — Mateus pede alinhamento de marca / brand
1. Carregue `references/04-design-system-voz.md`.
2. Se for blog, complemente com `references/05-editorial-blog.md`.

### Cenário 4 — Mateus pede deploy / técnico
1. Carregue `references/06-operacao-tecnica.md` e `references/08-canais-stack.md`.
2. Confirme com `/Modernitty/lp.soufit.com/DEPLOY.md` para detalhes operacionais.

### Cenário 5 — Mateus pede revisão regulatória / auditoria de copy
1. Carregue `references/09-regulatorio-anvisa.md`.
2. Compare com `/Modernitty/Produtos/AUDITORIA-CONSISTENCIA.md`.

---

## 🚫 O que esta skill NÃO faz

- ❌ Escrever copy de venda (use `/copywriter-senior` ou `/vsl-copywriter`)
- ❌ Produzir LP do zero (use o processo em `/Modernitty/Processo de Aula/PROCESSO-LP-ALTA-PERFORMANCE.md`)
- ❌ Pesquisar pauta de blog (use `/blog-research`)
- ❌ Decidir tarefa do dia (use `/weekly-planner` ou ClickUp)
- ❌ Substituir auditoria humana de claim ANVISA (apenas sinaliza)

Esta skill **ancora**. Outras skills **executam**.

---

## 🆕 Como manter esta skill viva

Quando o Mateus mencionar uma mudança que afete o contexto canônico (lançamento de produto, mudança de posicionamento, novo domínio, novo POP, refresh de design system, novo claim ANVISA aprovado), **proponha atualizar o reference correspondente**. Não atualize sem aprovar — a skill é fonte da verdade, não rascunho.

**Versão da skill:** v1 · 2026-05-30 · Baseada em snapshot do repositório Modernitty em 2026-05.
