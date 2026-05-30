# 07 — POPs Falconi (Processos Operacionais Padrão)

> Procedimentos Operacionais Padrão da casa, baseados na metodologia Vicente Falconi (excelência operacional).
> Localização: `/Modernitty/pops-falconi/`

---

## 📋 POPs documentados (3 ativos)

### POP-COPY-001 — Criar copy para materiais ricos e ebooks
- **Arquivo:** `POP-COPY-001 - Criar copy para materiais ricos e ebooks.docx`
- **Domínio:** Copywriting / produção de conteúdo
- **Cobertura:** Como estruturar copy para materiais ricos (ebooks, guias, lead magnets)
- **Inputs típicos:** brief de produto, persona, ICP, oferta
- **Outputs típicos:** copy em camadas (hook, lead, body, CTA) seguindo frameworks SouFit

### POP-CRM-001 — Estruturar fluxos de email e jornada do cliente
- **Arquivo:** `POP-CRM-001 - Estruturar fluxos de email e jornada do cliente.docx`
- **Domínio:** E-mail marketing / CRM
- **Cobertura:** Como montar sequências (boas-vindas, nutrição, recuperação de carrinho, pós-venda)
- **Stack:** ActiveCampaign + Hotmart (implícito)

### POP-TRAF-001 — Fazer espionagem de tráfego e montar swipe file
- **Arquivo:** `POP-TRAF-001 - Fazer espionagem de trafego e montar swipe file.docx`
- **Domínio:** Tráfego / pesquisa competitiva
- **Cobertura:** Como auditar anúncios concorrentes, salvar referências e construir biblioteca de inspiração

---

## 🏗️ Estrutura padrão (Falconi)

Todo POP da casa segue o formato em **8 blocos**:

1. **Cabeçalho** (POP-ID, versão, data, dono, aprovação)
2. **Objetivo** (uma frase clara)
3. **Material** (ferramentas, acessos, templates necessários)
4. **Passos Críticos** (step-by-step numerado)
5. **Manuseio** (como executar com qualidade)
6. **Resultados Esperados** (critérios de pronto)
7. **Ações Corretivas** (o que fazer se algo der errado)
8. **Aprovação** (assinatura, vigência)

---

## 🛠️ Skill que cria POPs

Use `/criacao-pop` ou `anthropic-skills:criacao-pop` para:
- Transformar transcrição de aula/treinamento em POP estruturado
- Padronizar um processo já existente
- Documentar tarefa repetitiva

A skill aplica automaticamente os 8 blocos, valida qualidade Falconi e gera o `.docx` final pronto para circular e ser assinado.

---

## 📌 Convenções de nomeação

`POP-<AREA>-<NUMERO> - <Descrição da ação>.docx`

| Sigla | Área |
|---|---|
| **COPY** | Copywriting |
| **CRM** | E-mail marketing / Jornada |
| **TRAF** | Tráfego pago |
| **OPS** | Operações gerais |
| **PROD** | Produto / suplemento |
| **REG** | Regulatório (ANVISA) |
| **TEC** | Técnico (deploy, dev) |
| **CONT** | Conteúdo (blog, social) |
| **ATEND** | Atendimento ao cliente |
| **LOG** | Logística |

> Convenção sugerida; expandir conforme necessidade.

---

## 🎯 Quando propor um novo POP

Crie um POP novo quando:
- ✅ A tarefa é executada **mais de 3 vezes/mês**
- ✅ Tem **mais de 1 pessoa** que precisa executar
- ✅ Erros já aconteceram por falta de padrão
- ✅ Onboarding de novo membro do time precisa cobrir aquela tarefa

NÃO crie POP quando:
- ❌ Tarefa one-off
- ❌ Apenas o Mateus executa e ele já tem domínio
- ❌ Decisão depende muito do contexto (não dá pra padronizar)

---

## 📂 Outras referências de processo

Além dos POPs Falconi, a casa tem documentação de processo em:

| Arquivo | Cobertura |
|---|---|
| `/Modernitty/Processo de Aula/PROCESSO-LP-ALTA-PERFORMANCE.md` | Metodologia completa em 8 fases para LP (Fase 0 a Fase 8) |
| `/Modernitty/lp.soufit.com/PROCESSO.md` | Checklist seco de execução de LP |
| `/Modernitty/lp.soufit.com/BRIEFING-LP.md` | Guia passo a passo de briefing (Schwartz, lead codes, exemplos SouFit) |
| `/Modernitty/lp.soufit.com/CONTRIBUTING.md` | Como fazer mudanças no repo |
| `/Modernitty/lp.soufit.com/DEPLOY.md` | Deploy técnico detalhado |
| `/Modernitty/lp.soufit.com/00-base/` | Biblioteca / fonte da verdade (produtos, design, copy master) |

---

## 🚨 POPs que ainda faltam (gap análise)

Sugestões baseadas no que existe no repo mas ainda não tem POP formal:

- [ ] **POP-CONT-001** — Criar post de blog do zero (research → brief → write → review → publish)
- [ ] **POP-TEC-001** — Subir nova LP em `lp.soufit.com` (briefing → copy → build → deploy → QA)
- [ ] **POP-PROD-001** — Estruturar dossiê técnico de produto novo (14 seções padrão)
- [ ] **POP-REG-001** — Auditar copy para conformidade ANVISA (claims, palavras-tabu)
- [ ] **POP-CONT-002** — Produzir carrossel para redes sociais (copy + design)
- [ ] **POP-ATEND-001** — Tratar dúvidas de cliente sobre produto (FAQ + escalonamento)

Se o Mateus pedir para padronizar qualquer um desses, use `/criacao-pop`.
