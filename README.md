# Skills e Processos

Repositorio central com todas as skills, regras, automacoes e processos operacionais usados nos meus ambientes Claude Code, Codex e nos projetos do Desktop.

## Estrutura

```
.
├── claude/
│   └── skills/               # 22 skills do ~/.claude/skills (versao mais recente)
├── codex/
│   ├── skills/               # Skills exclusivas do ~/.codex/skills
│   ├── rules/                # ~/.codex/rules
│   └── automations/          # ~/.codex/automations
├── projetos/                 # Skills isoladas em projetos especificos
│   ├── agente-gestor/        # Doc-guia do projeto Gestor Mestre (GESTOR_MESTRE.md)
│   ├── Cal-Agendador/
│   ├── Extrator-Kindle-Antigravity/
│   ├── Foto-Gloria-Chatwoot/
│   ├── Modernitty/
│   └── copywriter-senior-plugin/
└── processos/
    ├── avulsos/              # SKILL deploys avulsos, github-yeet
    ├── processo-de-aula/     # POPs detalhados de processos
    └── soufit/               # Espelho do ClickUp: processos internos + ativos de marketing
        ├── processos-internos/   # POPs Falconi (Trafego, CRM, Copy)
        └── ativos-marketing/     # Produtos (20), Design System, Calendarios
```

Skills duplicadas entre `~/.claude/skills` e `~/.codex/skills` foram deduplicadas — sempre que houve divergencia, foi mantida a versao do `.claude/` (mais completa).

O repo e atualizado manualmente de tempos em tempos com `rsync` (ver secao "Como atualizar" no final).

---

## claude/skills/ — Skills principais (22)

### Blog (pipeline completo)

| Skill | Descricao |
|-------|-----------|
| [`blog-orchestrator`](claude/skills/blog-orchestrator/) | Orquestra o fluxo completo de producao do blog, coordenando research → brief → writer → review → publish com checkpoints humanos. |
| [`blog-research`](claude/skills/blog-research/) | Pesquisa temas combinando sinais de viralidade (HN, Reddit) com analise de SEO (intencao de busca, concorrencia, E-E-A-T). |
| [`blog-brief`](claude/skills/blog-brief/) | Gera briefs estruturados com titulo SEO, slug, meta description, hierarquia H2/H3, angulo editorial, keywords, word count e CTA. |
| [`blog-writer`](claude/skills/blog-writer/) | Escreve posts completos em HTML semantico (com JSON-LD) a partir de um brief aprovado. |
| [`blog-review`](claude/skills/blog-review/) | Revisa posts cobrindo SEO on-page, qualidade editorial e voz; entrega score 0-100 e decisao APROVADO/REPROVADO. |
| [`blog-publish`](claude/skills/blog-publish/) | Publica posts aprovados no repositorio do site, atualiza indice e prepara o deploy. |

### Copywriting

| Skill | Descricao |
|-------|-----------|
| [`copywriter-senior`](claude/skills/copywriter-senior/) | Skill master consolidando 5 livros-biblia de copy direto (Masterson, Makepeace, Evaldo, Frank Kern). Base teorica/tecnica de VSL, lead, headline, oferta, garantia, etc. |
| [`rucci-copy`](claude/skills/rucci-copy/) | Copy de alto nivel para os produtos do Mateus Rucci (Mentoria e Implementacao) — aplica frameworks sobre ICPs reais. |
| [`rucci-carousel`](claude/skills/rucci-carousel/) | Carrosseis para Instagram/LinkedIn com base no Banco de Carrosseis e nos modelos visuais atuais. |

### Sales / ICP

| Skill | Descricao |
|-------|-----------|
| [`icp-generator`](claude/skills/icp-generator/) | Cria ICPs completos combinando JTBD, MEDDIC, April Dunford, Winning by Design e Heavybit. Entrega dores, gatilhos, linguagem, stakeholders e anti-ICP. |

### Design / Propostas

| Skill | Descricao |
|-------|-----------|
| [`canvas-design`](claude/skills/canvas-design/) | Composicoes visuais estaticas em `.png`/`.pdf` com design philosophy: posters, capas, art prints, campanhas, brand one-pagers. |
| [`proposal-vibe-design`](claude/skills/proposal-vibe-design/) | Propostas comerciais premium (PDF/PPTX) com direcao de arte editorial, sistemas claros/escuros, grids sofisticados, depth e glass. |

### Deploy / Infra

| Skill | Descricao |
|-------|-----------|
| [`code-deploy-skill`](claude/skills/code-deploy-skill/) | Padroniza respostas de deploy/manutencao em VPS (SCP/RSYNC/SSH) com comandos compactos e especificando onde rodar cada bloco. |
| [`hostgator-cpanel-deploy`](claude/skills/hostgator-cpanel-deploy/) | Deploy de sites estaticos e multiplas landings na HostGator/cPanel via GitHub Actions e cPanel API. |

### APIs / Integracoes

| Skill | Descricao |
|-------|-----------|
| [`redtrack-api`](claude/skills/redtrack-api/) | Master skill para automacoes Google Apps Script com a RedTrack API (landings, offers, campaigns, domains, streams, conversions). |
| [`clickup-task-creator`](claude/skills/clickup-task-creator/) | Cria, divide, atualiza e analisa tasks/subtasks no ClickUp via integracao conectada. |
| [`clickup-task-manager`](claude/skills/clickup-task-manager/) | Cria, estrutura e gerencia tasks no ClickUp do Mateus Rucci com padroes reais (workspaces, listas e user IDs ja mapeados, sem acentos). |
| [`knowledge-to-notion`](claude/skills/knowledge-to-notion/) | Transforma conteudo bruto em pagina completa no Notion, preenchendo propriedades do database e gerando Markdown final. |

### Gestao / Contexto / Processos

| Skill | Descricao |
|-------|-----------|
| [`gestor-mestre`](claude/skills/gestor-mestre/) | Consigliere de gestao baseado em 6 livros classicos (Falconi, Drucker, Bossidy/Charan, Gerber, Gawande). 4 modos: CONSULTA, DIRECIONAMENTO, PROATIVO, SINTESE. Cita sempre a fonte. |
| [`contexto-soufit`](claude/skills/contexto-soufit/) | Contexto canonico da SouFit / Grupo MDT — 20 produtos, design system, voz, deploy, ANVISA, mapa de arquivos. Carrega memoria, nao escreve copy. |
| [`okr-manager`](claude/skills/okr-manager/) | Cria, estrutura e faz check-in de OKRs seguindo Felipe Castro + John Doerr. Aplica os 4 Superpoderes (Foco, Alinhamento, Acompanhamento, Desafio) e CFRs. |
| [`criacao-pop`](claude/skills/criacao-pop/) | Cria POPs Falconi padronizados (8 blocos: Cabecalho, Objetivo, Material, Passos Criticos, Manuseio, Resultados, Acoes Corretivas, Aprovacao) com saida em .docx. |

---

## codex/skills/ — Skills exclusivas do Codex (1)

| Skill | Descricao |
|-------|-----------|
| [`falconi-pop-docx`](codex/skills/falconi-pop-docx/) | Cria Processos Operacionais Padrao (POPs) em DOCX no modelo Falconi a partir de aulas, transcricoes, anexos, links ou materiais do Gmail/Drive. |

## codex/rules/

- [`default.rules`](codex/rules/default.rules) — regras padrao globais do Codex.

## codex/automations/

- [`pesquisa-de-noticias-importantes-do-ultimo-dia`](codex/automations/pesquisa-de-noticias-importantes-do-ultimo-dia/) — automacao diaria de pesquisa de noticias.

---

## projetos/ — Skills isoladas em projetos especificos

### Cal-Agendador (Cal.com integration app)

| Skill | Descricao |
|-------|-----------|
| [`calcom-api`](projetos/Cal-Agendador/calcom-api/) | Interage com Cal.com API v2 (bookings, event types, availability, calendars). |
| [`web-design-guidelines`](projetos/Cal-Agendador/web-design-guidelines/) | Review de UI contra Web Interface Guidelines (acessibilidade, UX, best practices). |
| [`vercel-react-best-practices`](projetos/Cal-Agendador/vercel-react-best-practices/) | Guidelines de performance de React/Next.js da Vercel Engineering. |

### Modernitty (Facebook Ads tooling)

| Skill | Descricao |
|-------|-----------|
| [`meta-ads-audience-ops`](projetos/Modernitty/meta-ads-audience-ops/) | Cria, audita e padroniza publicos no Meta/Facebook Ads via Marketing API (Website Custom Audiences, lookalikes, remarketing). |
| [`hostgator-cpanel-deploy`](projetos/Modernitty/hostgator-cpanel-deploy/) | Variante do hostgator-cpanel-deploy ajustada para o fluxo do projeto (deploy direto na main, sem PR intermediario). |

### Foto-Gloria-Chatwoot (Chatwoot VPS)

| Skill | Descricao |
|-------|-----------|
| [`code-deploy-skill`](projetos/Foto-Gloria-Chatwoot/code-deploy-skill/) | Variante do code-deploy-skill com regras especificas de Chatwoot/Typebot/N8N atras de proxy reverso e sequencia condicional de comandos. |

### Extrator-Kindle-Antigravity

| Skill | Descricao |
|-------|-----------|
| [`kindle_processor`](projetos/Extrator-Kindle-Antigravity/kindle_processor/) | Agente de OCR que converte capturas de tela da biblioteca Kindle em Markdown limpo e desduplicado para o Notion. |

### copywriter-senior-plugin

Plugin completo (`.claude-plugin/`) empacotando a skill `copywriter-senior` para distribuicao. Inclui `LICENSE`, `README.md` proprio e a skill com referencias.

---

## processos/

### processos/avulsos/

- [`github-yeet-SKILL.md`](processos/avulsos/github-yeet-SKILL.md) — skill de fluxo rapido GitHub.
- [`skill-deploy.md`](processos/avulsos/skill-deploy.md) — processo de deploy de skills.
- [`skill.md`](processos/avulsos/skill.md) — referencia geral de skill.

### processos/processo-de-aula/

- [`PROCESSO-LP-ALTA-PERFORMANCE.md`](processos/processo-de-aula/PROCESSO-LP-ALTA-PERFORMANCE.md) — POP detalhado de processo de landing pages de alta performance.

---

## Como atualizar

Quando algo for atualizado nos diretorios de origem, basta sincronizar:

```bash
# Skills do Claude Code
rsync -a --exclude='.DS_Store' ~/.claude/skills/ claude/skills/

# Skills exclusivas do Codex (verificar antes diff -rq)
rsync -a --exclude='.DS_Store' ~/.codex/skills/falconi-pop-docx/ codex/skills/falconi-pop-docx/

# Rules e automations
cp ~/.codex/rules/default.rules codex/rules/
rsync -a ~/.codex/automations/ codex/automations/

# Limpar e commitar
find . -name ".DS_Store" -delete
git add -A
git commit -m "sync: atualiza skills/rules/automations"
git push
```

Antes de commitar: confira que nao ha credenciais, tokens, `.env` ou chaves privadas em nenhum arquivo.
