---
name: clickup-task-manager
description: Skill completa para criar, estruturar e gerenciar tarefas no ClickUp do Mateus Rucci de forma rapida, eficaz e padronizada. Use SEMPRE que o usuario pedir "criar tarefa", "adicionar no ClickUp", "criar subtarefa", "criar checklist", "criar projeto no ClickUp" ou qualquer variacao. Aplica os padroes reais ja usados nas listas Gestao (estrategica) e Lancamento (operacional) e elimina decisoes desnecessarias para economizar tokens.
---

# ClickUp Task Manager — Mateus Rucci

Skill para criar tarefas no ClickUp com clareza, velocidade e baixo consumo de tokens, seguindo os padroes reais ja estabelecidos no workspace.

---

## REGRA DE OURO: SEM ACENTOS

**SEMPRE** escrever nomes de tarefas, descricoes e subtarefas **SEM ACENTOS** e **sem cedilha**. Isso evita problemas de encoding no ClickUp e em integracoes.

| Errado | Certo |
|--------|-------|
| Estratégia | Estrategia |
| Lançamento | Lancamento |
| Configuração | Configuracao |
| Análise | Analise |
| Conteúdo | Conteudo |

Excecao: apenas se o usuario escrever explicitamente com acento E pedir para manter assim.

---

## WORKSPACES E LISTAS CONHECIDAS

### Workspace Pessoal (Mateus Rucci)
**Default para tudo que nao for Soufit/cliente**

| Espaco | Lista | List ID |
|--------|-------|---------|
| Geral | Tarefas | `901326645169` |
| Akro Edu | Akro Edu | `901326511456` |
| SOUVE | Fase 00 - Diagnostico | `901302726312` |
| SOUVE | Fase 01 - Contratacao | `901302726512` |
| SOUVE | Fase 02 - Consultoria | `901302726826` |

### Workspace Soufit (Marketing MDT)

| Espaco | Pasta | Lista | List ID |
|--------|-------|-------|---------|
| Marketing MDT | Performance | Gestao | `901327242484` |
| Marketing MDT | Performance | Lancamento | `901327308565` |
| Marketing MDT | Performance | Triagem | `901327285790` |
| Marketing MDT | Performance | Projetos / Lancamentos | `901327285779` |
| Marketing MDT | Performance | CRM | `901321447946` |
| Marketing MDT | Performance | Midia Paga | `901321447954` |
| Marketing MDT | Performance | Devs | `901327292318` |
| Marketing MDT | Performance | E-Commerce | `901327308575` |
| Marketing MDT | Comunicacao/Branding | Calendario Conteudo | `901321447743` |
| Marketing MDT | Comunicacao/Branding | Criacao | `901321452148` |
| Marketing MDT | Comunicacao/Branding | Midias Sociais | `901325292072` |

### Quando PERGUNTAR a lista
Perguntar apenas quando:
1. A tarefa pode pertencer claramente a mais de um workspace (ambiguidade real)
2. O usuario menciona um cliente/projeto que ainda nao esta mapeado
3. A tarefa e claramente operacional de Soufit mas nao especifica se vai em Gestao, Lancamento, Midia Paga, etc.

**NUNCA perguntar** para tarefas pessoais, lembretes, compras, viagens, ou qualquer coisa que claramente cabe na lista padrao Geral > Tarefas.

---

## USUARIOS CONHECIDOS (User IDs)

### Workspace Pessoal
| Nome | ID |
|------|-----|
| Mateus Rucci | `3061062` |
| Ingrid | `81918186` |
| Lucas Maihach | `3059405` |

### Workspace Soufit
| Nome | ID |
|------|-----|
| Mateus Rucci | `118060211` |
| Daniel de Oliveira Medeiros | `118068229` |
| Hernanndes Alves | `118071732` |
| Ana Flavia | `118071745` |
| Nicolas Louzada | `236454661` |
| Andre Araujo | `230413938` |

Para outros nomes, usar `clickup_resolve_assignees` antes de criar.

---

## PADROES DE NOMENCLATURA

A skill aplica DOIS padroes distintos baseados no tipo de tarefa. Identificar o padrao certo antes de criar.

### Padrao 1 — ESTRATEGICO (lista Gestao e similares)
Para tarefas de planejamento, decisao, projetos macro.

**Formato:** `[AREA/CONTEXTO] - [O QUE FAZER] - [ENTREGA/RESULTADO ESPERADO]`

Exemplos reais do workspace:
- `Estrategia Mensal - Construcao da Estrategia Geral para apresentar para o time - Plano de tarefas + Funil pre estruturado`
- `Trafego Pago - Criar checklist de campanhas a serem subidas para o Hernandes - Criar documento com campanhas e contextualizacao`
- `Trackeamento Meta - Implementar conversoes Server-Side da Meta no E-commerce - Ter todos os dados sendo enviados para o servidor`
- `Anuncios - Planejar e estruturar volume de producao de anuncios - Plano pratico para copy, designer e video`

**Quando usar:** tarefas para listas Gestao, Triagem, Projetos/Lancamentos, ou quando a tarefa tem multiplas dimensoes (contexto + acao + entrega).

### Padrao 2 — OPERACIONAL (lista Lancamento, Tarefas pessoais)
Para tarefas executivas, checklists, acoes pontuais.

**Formato:** `Verbo no infinitivo + objetivo curto e direto`

Exemplos reais:
- `Definir marcos de aprovacao`
- `Criar copies de criativos estaticos`
- `Subir os Anuncios`
- `Mapear transformacao narrativa`
- `Preparar suporte de vendas`
- `Configurar gateway de pagamento`

**Quando usar:** lista Lancamento, subtarefas em geral, tarefas pessoais, compras, lembretes.

### Padrao 3 — SUBTAREFAS NUMERADAS
Para checklists grandes ou projetos com fases sequenciais.

**Formato:**
- Tarefa-pai numerada por fase: `0.1 Nome`, `0.2 Nome`, `1.1 Nome`...
- Subtarefas: verbo + objetivo direto

Exemplos:
- `0.1 Calendario e linha do tempo` -> subtarefa: `Definir marcos de aprovacao`
- `4.1 Roteiro do evento` -> subtarefa: `Escrever script completo`

### Padrao 4 — POR CATEGORIA (checklist)
Para checklists com muitos itens divididos por categoria.

**Formato:** `[Categoria] Acao especifica`

Exemplo:
- `[Config] Atualizar URL do perfil`
- `[Visual] Criar banner com proposta de valor`
- `[Conteudo] Publicar post de reposicionamento`

---

## ARQUITETURA DA TAREFA (antes de criar, pensar nisso)

Antes de chamar a tool, decidir:

### 1. E uma tarefa simples ou tem subtarefas?
- **Simples (1 acao isolada):** criar diretamente
- **Tem subtarefas:** estruturar a tarefa-pai + lista de subtarefas

### 2. Qual padrao de nomenclatura aplicar?
- Estrategica (Gestao) -> Padrao 1
- Operacional (Lancamento, pessoal) -> Padrao 2
- Checklist longo -> Padrao 3 ou 4

### 3. Qual lista?
- Pessoal/lembrete/compra -> Geral > Tarefas (`901326645169`)
- Estrategica Soufit -> Gestao (`901327242484`)
- Operacional Soufit lancamento -> Lancamento (`901327308565`)
- Cliente especifico -> Lista do cliente
- Ambiguidade real -> PERGUNTAR

### 4. Qual prioridade?
- **urgent** -> bloqueador, vence hoje/amanha, impacto financeiro direto
- **high** -> importante, vence essa semana, dependencia para outras tarefas
- **normal** -> padrao para a maioria
- **low** -> pessoal simples, compras, lembretes sem urgencia

### 5. Tem responsavel?
- Se o usuario mencionou alguem -> resolver ID e adicionar em `assignees`
- Se nao mencionou -> nao atribuir (deixar vazio)

### 6. Tem data?
- Se mencionou prazo -> adicionar `due_date` no formato YYYY-MM-DD
- Se nao mencionou -> nao adicionar

### 7. Precisa de descricao?
- **NAO precisa** para: tarefas simples, compras, lembretes, acoes obvias
- **SIM precisa** para: tarefas tecnicas com contexto, links importantes, checklists internos, projetos com escopo

---

## FLUXO DE CRIACAO

### Tarefa simples (sem subtarefas)
```
1. Identificar padrao de nomenclatura
2. Definir lista (default: 901326645169)
3. Definir prioridade
4. Chamar clickup_create_task uma unica vez
```

### Tarefa com subtarefas
```
1. Criar tarefa-pai primeiro -> capturar task_id
2. Para cada subtarefa: clickup_create_task com parent=[task_id]
3. Mesma list_id da pai
```

### Tarefa estruturada por fases (Padrao 3)
```
1. Criar tarefa-pai geral
2. Criar tarefas-pai de fase: "0.1 X", "0.2 Y" como filhas
3. Subtarefas de cada fase como netas
```

---

## OTIMIZACAO DE TOKENS

### O que ECONOMIZA tokens
- Nao buscar hierarquia do workspace antes de criar (usar IDs conhecidos direto)
- Nao adicionar descricao em tarefas simples
- Nao fazer retry automatico em caso de erro - reportar e perguntar
- Nao chamar `resolve_assignees` se ID ja esta mapeado nesta skill
- Criar tarefa direta quando lista e obvia, sem perguntar
- Resposta curta apos criacao: titulo + link, sem repetir tudo

### O que GASTA tokens (evitar)
- Descricoes muito longas em tarefas obvias
- Confirmar 2x antes de criar tarefa simples
- Buscar lista quando ja temos o ID
- Listar resumos enormes apos criar 1 tarefa
- Repetir o pedido do usuario antes de executar

### Formato ideal de resposta
**Tarefa simples:**
```
Criada: [Nome da tarefa](url)
```

**Tarefa com subtarefas:**
```
Criada: [Nome](url) com N subtarefas
[tabela com numero + nome se ajudar a clareza]
```

**Tarefa com observacao importante:**
Pode incluir 1 nota curta apenas se houver algo critico que o usuario precisa saber (ex: recorrencia precisa ser configurada manualmente, lista nao existia, etc.)

---

## STATUS POR LISTA (referencia)

### Lista Gestao (Soufit)
aberto -> planejamento -> executando -> revisao -> double check -> feito

### Lista Lancamento (Soufit)
pendente -> em progresso -> em aprovacao -> agendado -> feito

### Lista Tarefas (Pessoal)
to do -> in progress -> complete

Normalmente nao especificar status na criacao - ClickUp usa o default da lista.

---

## TAGS USADAS (Lista Lancamento)

Quando criar tarefas-pai de fases em um lancamento, usar tags numeradas:
- `0 planejamento`
- `1 captao convite`
- `2 captacao geral`
- `3 antecipao`
- `4 evento principal`
- `5 abertura de vagas`
- `6 psvenda e fechamento de carrinho`

---

## EXEMPLOS PRATICOS

### Exemplo 1 — Tarefa pessoal simples
> "Crie tarefa pra comprar presente da Cris"

**Acao:**
```
clickup_create_task(
  list_id="901326645169",
  name="Comprar presente da Cris",
  priority="low"
)
```

**Resposta:**
> Criada: [Comprar presente da Cris](url)

---

### Exemplo 2 — Tarefa estrategica Soufit
> "Cria tarefa de estruturar a nova rotina de daily na Gestao"

**Acao (Padrao 1 + lista Gestao):**
```
clickup_create_task(
  list_id="901327242484",
  name="Processos e Rotinas - Estruturar nova rotina de Daily - Definir pauta, formato e documento guia para a equipe",
  priority="high",
  assignees=["118060211"]
)
```

---

### Exemplo 3 — Tarefa com subtarefas
> "Cria tarefa de lancar produto X com subtarefas: briefing, copy, design, dev"

**Acao:**
```
1. Tarefa-pai:
clickup_create_task(
  list_id="901326645169",
  name="Lancar produto X",
  priority="high"
) -> capturar task_id

2. Subtarefas:
clickup_create_task(list_id, name="1. Briefing", parent=task_id)
clickup_create_task(list_id, name="2. Copy", parent=task_id)
clickup_create_task(list_id, name="3. Design", parent=task_id)
clickup_create_task(list_id, name="4. Dev", parent=task_id)
```

---

### Exemplo 4 — Tarefa com responsavel
> "Cria tarefa para a Ingrid revisar o site"

**Acao:**
```
clickup_create_task(
  list_id="901326645169",
  name="Revisar o site",
  priority="normal",
  assignees=["81918186"]
)
```

---

### Exemplo 5 — Ambiguidade real
> "Cria tarefa pra estruturar o funil de afiliados"

**Acao:** PERGUNTAR
> Em qual lista? Geral, Gestao Soufit, ou Afiliados Soufit?

---

### Exemplo 6 — Checklist grande por categoria
> "Cria todas essas 15 tarefas pra otimizar o LinkedIn"

**Acao:**
1. Criar tarefa-pai: `Otimizacao do LinkedIn`
2. Criar subtarefas com prefixo de categoria: `[Config] X`, `[Visual] Y`, `[Conteudo] Z`

---

## ERROS COMUNS A EVITAR

1. **Adicionar acentos** -> sempre remover
2. **Perguntar a lista pra tarefa obvia** -> usar default
3. **Buscar hierarquia antes de criar** -> usar IDs ja mapeados
4. **Descricoes longas em tarefas simples** -> deixar so o nome
5. **Listar tabela enorme apos criar 1 tarefa** -> resposta curta
6. **Repetir o pedido do usuario** -> ja entendeu, executa
7. **Tentar configurar recorrencia via API** -> avisar que precisa fazer manualmente
8. **Misturar padroes** -> escolher 1 padrao e aplicar consistente nas subtarefas

---

## CHECKLIST MENTAL ANTES DE CADA CRIACAO

- [ ] Removi todos os acentos do nome?
- [ ] Identifiquei o padrao certo (estrategico/operacional/checklist)?
- [ ] Tenho o list_id certo (e nao preciso buscar)?
- [ ] A prioridade faz sentido pro contexto?
- [ ] Se tem responsavel, ja tenho o ID?
- [ ] Descricao e necessaria ou e overkill?
- [ ] Resposta vai ser curta e clara?
