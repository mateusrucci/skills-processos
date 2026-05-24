---
name: rucci-copy
description: Escreve copy de alto nível para os produtos do Mateus Rucci (SOULVE MARKETING) — Mentoria de Tráfego e Implementação de Time Interno. Use esta skill SEMPRE que o Mateus pedir copy, texto, anúncio, ad, VSL, landing page, e-mail, post orgânico, reel, headline, hook, lead, CTA ou qualquer peça persuasiva para OS PRÓPRIOS PRODUTOS DELE (Mentoria, Implementação, Soulve, Rucci). Também use quando ele disser "escreve uma copy", "faz um anúncio pra minha mentoria", "copy pro meu produto", "landing da minha implementação", "pra minha persona" ou qualquer variação que envolva vender OS serviços dele, não os de clientes. Esta skill aplica os frameworks de Michael Masterson (5 tipos de lead), Eugene Schwartz (nível de consciência e sofisticação), Bíblia dos Hooks e Processo Twenty Five sobre os ICPs reais já documentados de Mentoria e Implementação. NÃO use para copy de clientes do Mateus (use vsl-copywriter ou b2b-landing-copy para isso).
---

# rucci-copy — Copy para os produtos do Mateus Rucci

Skill dedicada a escrever copy para os DOIS produtos do Mateus:

- **Mentoria Individual de Tráfego** — empresário sócio-fundador, R$ 500k–5M/ano, verba de R$ 8k–22k/mês
- **Implementação de Time Interno** — CEO/board, R$ 3M–50M/ano, verba de R$ 50k–200k/mês

**Importante:** são duas personas radicalmente diferentes. A linguagem, a dor central, os gatilhos e a prova são distintos. NUNCA escreva copy "neutra" que sirva pros dois — isso falha com ambos.

---

## Workflow (siga nesta ordem)

### Passo 1 — Identificar o produto

Olhe o pedido do Mateus. Se ele já disser qual produto (mentoria, implementação), vá direto pro Passo 2. Se não estiver claro, pergunte apenas UMA pergunta:

> "É pra Mentoria (empresário R$ 500k–5M) ou Implementação (CEO R$ 3M–50M)?"

**Não pergunte mais de uma coisa de cada vez.** Depois que ele responder, só pergunte algo novo se for *realmente* indispensável (ver lista abaixo).

### Passo 2 — Identificar o formato

Identifique pelo pedido qual formato ele quer:

| Pedido contém | Formato | Reference file |
|---|---|---|
| "anúncio", "ad", "criativo", "Meta", "Google", "LinkedIn" | **ad** | `references/formato-ad.md` |
| "VSL", "vídeo de vendas", "script de vídeo" | **vsl** | `references/formato-vsl.md` |
| "landing", "LP", "página de vendas", "página de captura" | **landing** | `references/formato-landing.md` |
| "e-mail", "email", "sequência", "newsletter" | **email** | `references/formato-email.md` |
| "post", "reel", "carrossel", "orgânico", "Instagram", "LinkedIn orgânico" | **organico** | `references/formato-organico.md` |

Se o formato não estiver claro, pergunte.

### Passo 3 — Ler as referências obrigatórias

Antes de escrever QUALQUER coisa, leia (use a tool `view`):

1. O arquivo do ICP correspondente: `references/icp-mentoria.md` OU `references/icp-implementacao.md`
2. O arquivo do formato: `references/formato-{ad|vsl|landing|email|organico}.md`
3. O arquivo de frameworks: `references/frameworks.md` (Masterson + Schwartz + Big Idea)

Se for peça curta (ad, post, headline), leia também `references/hooks-library.md`.

### Passo 4 — Decidir o posicionamento

Antes de escrever, defina internamente (e coloque num bloco "Direção criativa" no topo do entregável):

1. **Nível de consciência** (Schwartz): Inconsciente / Consciente do problema / Consciente da solução / Consciente do produto / Mais consciente
2. **Nível de sofisticação** (Schwartz): 1 (primeiro no mercado) / 2 (amplifica claim) / 3 (mecanismo) / 4 (mecanismo melhor) / 5 (identificação/história)
3. **Tipo de lead** (Masterson): Oferta / Promessa / Problema–Solução / Big Idea / História
4. **Big Idea**: uma frase que resuma a angulação (ver `frameworks.md`)
5. **Gatilho principal** (1 dos 25+ do ICP): ex. "Informação privilegiada", "Inimigo comum", "Autoconhecimento"

### Passo 5 — Escrever

Siga a estrutura do arquivo de formato. Use **exclusivamente** a linguagem, os números, as objeções e as provas do ICP correspondente. Se faltar algo específico (ex. data de abertura, valor exato, URL), pergunte — **não invente números**.

### Passo 6 — Entregar

Formato de entrega padrão:

```markdown
## Direção criativa
- **Produto:** [Mentoria / Implementação]
- **Nível de consciência:** [X]
- **Sofisticação:** [X]
- **Lead:** [tipo]
- **Big Idea:** [frase]
- **Gatilho principal:** [gatilho]

---

## [Peça]

[copy completa, pronta pra colar]

---

## Notas
- [decisões que tomei e por quê, em 2-3 bullets curtos]
- [o que posso variar se ele quiser A/B]
```

---

## Regras invioláveis

1. **NUNCA** misturar linguagem de Mentoria com Implementação. Veja a tabela abaixo.
2. **NUNCA** inventar número, case, nome de cliente ou data. Se faltar, pergunta.
3. **NUNCA** usar copy genérica tipo "transforme seu negócio", "alavanque seus resultados". O Mateus detesta isso e não é o registro dele.
4. **SEMPRE** ancorar em pelo menos 1 dor + 1 objeção + 1 prova do ICP correspondente.
5. **SEMPRE** usar especificidade cirúrgica: números, prazos, nomes de plataforma, verba real.
6. **NUNCA** abrir com pergunta retórica batida ("você já se sentiu...", "imagine se..."). Ver `hooks-library.md` para hooks validados.
7. **SEMPRE** terminar a peça com CTA único e claro — nunca 2 CTAs concorrentes.

### Diferencial de linguagem Mentoria vs. Implementação

| Dimensão | Mentoria | Implementação |
|---|---|---|
| Persona | Empresário/dono | CEO/board |
| Verbo-chave | "entender", "liderar", "assumir controle" | "estruturar", "internalizar", "ativo" |
| Vocabulário | "tráfego", "agência", "gestor", "verba" | "CAC", "LTV", "ROI", "board", "valuation" |
| Dor | "não sei o que está funcionando" | "não consigo defender o ROI pro board" |
| Prova | "400 projetos", "R$ 200M gerenciados" | "400 implementações", "cases por setor e porte" |
| Escassez | "6 vagas/mês" | "4 projetos/trimestre" |
| Formato de sessão | "60min semanal + WhatsApp" | "fases de 90 dias + recrutamento + processo" |
| CTA típico | "Agende seu diagnóstico" | "Agende uma conversa estratégica" |
| Emoção de fundo | Frustração + vontade de autonomia | Pressão societária + necessidade de previsibilidade |

---

## Quando pedir mais informação

**Pergunte apenas se for imprescindível.** Em ordem de prioridade:

1. Qual produto (se não estiver claro no pedido)
2. Qual formato (se não estiver claro)
3. Qual o objetivo específico da peça (captação de lead? agendamento? conversão direta?)
4. Existe algum case/número recente específico que ele queira usar?
5. Existe oferta/bônus/escassez específica (data, valor, vagas)?

**Nunca faça uma bateria de perguntas.** Máximo 2 perguntas de uma vez, e só quando ausência delas impediria a peça.

---

## Índice de arquivos de referência

- `references/icp-mentoria.md` — Persona completa, dores, desejos, objeções, linguagem da Mentoria
- `references/icp-implementacao.md` — Persona completa, dores, desejos, objeções, linguagem da Implementação
- `references/frameworks.md` — 5 leads de Masterson, consciência/sofisticação de Schwartz, Big Idea
- `references/formato-ad.md` — Ads para Meta / Google / YouTube / LinkedIn
- `references/formato-vsl.md` — Estrutura de VSL (hook, mecanismo, prova, oferta, garantia, fechamento)
- `references/formato-landing.md` — Landing page (hero → CTA)
- `references/formato-email.md` — Sequências de e-mail
- `references/formato-organico.md` — Posts, reels, carrosséis
- `references/hooks-library.md` — Hooks adaptados da Bíblia dos Hooks + Processo Twenty Five
- `references/briefing-template.md` — Perguntas de briefing quando faltar info
