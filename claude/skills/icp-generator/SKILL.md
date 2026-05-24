---
name: icp-generator
description: Cria ICPs (Ideal Customer Profiles) completos e de alta precisão combinando os melhores frameworks do mundo (Jobs-to-be-Done, MEDDIC, April Dunford, Winning by Design, Heavybit). Use esta skill SEMPRE que o usuário pedir para criar, definir, montar, mapear ou refinar um ICP, perfil de cliente ideal, cliente dos sonhos, avatar, persona B2B, ou qualquer variação de "quem é meu cliente ideal". Também use quando o usuário perguntar "pra quem eu vendo", "como definir meu cliente ideal", "quero prospectar melhor", "quero qualificar leads", ou quando o usuário quiser melhorar seu posicionamento de mercado e precisar saber com clareza quem atender. Esta skill entrega o ICP mais completo e preciso possível — não apenas uma lista de atributos, mas um perfil vivo com dores, gatilhos, linguagem, stakeholders, sinais de identificação, métricas e anti-ICP.
---

# ICP Generator — Perfil de Cliente Ideal de Alta Precisão

## Objetivo
Construir um ICP que vai além de atributos firmográficos e captura: quem é, o que sente, por que compra agora, quem decide, como identificar, e quem nunca atender.

## Frameworks combinados
Esta skill integra o melhor de:
- **Predictable Revenue** (Aaron Ross) — firmográficos e métricas
- **Jobs-to-be-Done** (Tony Ulwick / Clayton Christensen) — dor funcional, emocional e social
- **Positioning** (April Dunford) — fit vs. propensão, why change/why now/why you
- **Winning by Design** — 3 Whos (user, buyer, influencer) + 3 Whys
- **Heavybit ICP Template** — Anti-ICP e scoring de priorização
- **MEDDIC** — métricas, economic buyer, critérios de decisão

---

## Processo de criação do ICP

### ETAPA 1 — Coleta de contexto

Antes de gerar o ICP, colete as seguintes informações. Se o usuário não forneceu, **pergunte exatamente estas perguntas** (uma rodada só, não em mensagens separadas):

1. **O que você vende?** (produto/serviço, modelo: consultoria, SaaS, agência, infoproduto, etc.)
2. **Qual é o resultado que você entrega ao cliente?** (não o que você faz, mas o que muda na vida/empresa dele)
3. **Qual é o ticket médio / modelo de precificação?** (mensal, projeto, recorrência)
4. **Quais são seus 3 melhores clientes hoje?** (o que eles têm em comum?)
5. **Quais clientes você NUNCA mais quer atender?** (o que há de errado com eles?)
6. **Você tem restrições de mercado?** (geo, setor, tamanho mínimo de empresa, idioma)

Se o usuário já forneceu contexto suficiente na conversa, pule direto para a Etapa 2.

---

### ETAPA 2 — Geração do ICP

Com as respostas, gere o ICP completo seguindo a estrutura abaixo. Entregue sempre em formato de **tabela Markdown** com as colunas: Dimensão | Critério | Definição | Peso (1-5).

Após a tabela, inclua:
- **Resumo do ICP em 3 linhas** (quem é, qual dor resolve, por que compra agora)
- **Frase de qualificação rápida** (pergunta de 1 linha para identificar na hora se é ICP ou não)
- **Anti-ICP** em lista separada (5 deal-breakers que desqualificam imediatamente)

---

## Estrutura completa do ICP

### BLOCO 1 — QUEM (Firmográfico)
| Critério | O que mapear |
|---|---|
| Setor/Indústria | Segmento principal + sub-segmentos aceitos |
| Faturamento anual | Faixa de receita (R$ ou USD) |
| Nº de funcionários | Tamanho do time |
| Estágio da empresa | Startup / Scale-up / Consolidada / Enterprise |
| Modelo de negócio | B2B / B2C / Marketplace / SaaS / Serviço |
| Localização | Geo específica ou nacional/global |
| Maturidade digital | Nível de adoção de ferramentas e processos |

### BLOCO 2 — POR QUE COMPRA (Jobs-to-be-Done)
| Critério | O que mapear |
|---|---|
| Job funcional | Problema prático que tentam resolver (tarefa real) |
| Job emocional | Como a dor afeta pessoalmente (frustração, medo, vergonha, ansiedade) |
| Job social | Como resolver isso melhora status/reputação no mercado ou na empresa |
| Resultado desejado | O "after state" — como fica a vida/empresa depois da solução |
| Tentativas anteriores | O que já tentaram e por que falhou (dor da solução atual) |

### BLOCO 3 — QUANDO COMPRA (Propensão e Gatilhos)
| Critério | O que mapear |
|---|---|
| Why change | O que os faz sair do status quo agora |
| Why now | Evento/gatilho que cria urgência no momento |
| Why you | Por que escolher sua solução e não a concorrência ou o nada |
| Gatilhos observáveis | Sinais externos que indicam que o gatilho aconteceu |
| Orçamento | Budget aprovado, em discussão ou a ser criado |

**Exemplos de gatilhos de compra:**
- Crescimento acelerado criando gargalo operacional
- Troca de liderança (novo CEO, CMO, VP)
- Rodada de investimento captada
- Perda de cliente ou queda de receita
- Prazo regulatório / compliance
- Lançamento de produto/serviço novo
- Expansão para novo mercado

### BLOCO 4 — QUEM DECIDE (Stakeholders)
| Critério | O que mapear |
|---|---|
| User | Quem usa a solução no dia a dia (precisa amar o produto) |
| Economic Buyer | Quem aprova o budget e assina o contrato |
| Champion | Quem defende a compra internamente |
| Blocker | Quem pode vetar (CFO, TI, jurídico, etc.) |
| Influencer | Quem opina sem decidir |
| Cargo do decisor | Título/posição exata de quem bate o martelo |
| Tamanho do comitê | Quantas pessoas envolvidas na decisão |

### BLOCO 5 — COMO IDENTIFICAR (Sinais de Fit)
| Critério | O que mapear |
|---|---|
| Dados firmográficos | Tamanho, setor, faturamento (LinkedIn, Apollo, Receita Federal) |
| Tech stack | Ferramentas que já usam (sinal de maturidade e fit) |
| Comportamento digital | Job posts, conteúdo publicado, eventos que participam |
| Sinais de crescimento | Contratações, rodadas, expansão, prêmios |
| Sinais de dor | Reclamações públicas, reviews, mudanças de time |
| Canais de sourcing | LinkedIn Sales Nav, Apollo, eventos, comunidades, bases |

### BLOCO 6 — MÉTRICAS DO DEAL
| Critério | O que mapear |
|---|---|
| Ticket médio (MRR/ARR/projeto) | Valor do contrato |
| Ciclo de venda esperado | Do primeiro contato até assinatura |
| LTV esperado | Lifetime value médio |
| CAC aceitável | Custo máximo de aquisição viável |
| Payback period | Tempo para recuperar o CAC |
| Taxa de churn esperada | Para clientes desse perfil |

### BLOCO 7 — ANTI-ICP (Deal Breakers)
Liste os critérios que **desqualificam imediatamente**, sem exceção:
- Setor/vertical proibida
- Tamanho abaixo do mínimo
- Ticket inviável
- Estágio incompatível
- Comportamento/cultura incompatível
- Restrições técnicas ou legais

---

## Entregáveis obrigatórios

Ao final, sempre entregue:

1. **Tabela ICP completa** (todos os 7 blocos preenchidos)
2. **Resumo executivo do ICP** (3-5 linhas: quem é, dor principal, gatilho, por que te escolhe)
3. **Pergunta de qualificação rápida** (1 pergunta que em 30 segundos revela se é ICP ou não)
4. **Lista Anti-ICP** (5+ deal-breakers)
5. **Score de priorização** (se o usuário tiver múltiplos segmentos): ranqueie de 1 a 5 qual atender primeiro com base em: fit, propensão, deal size e velocidade de ciclo

---

## Regras de qualidade

- **Nunca gere ICP genérico.** Cada critério deve ser específico o suficiente para ser usado como filtro real numa lista de prospecção.
- **Foco em propensão, não só em fit.** Um cliente pode ter fit perfeito e zero propensão (sem gatilho, sem orçamento). O ICP ideal tem os dois.
- **Jobs-to-be-Done antes de firmográficos.** A dor real é mais preditiva de compra do que setor ou tamanho.
- **Anti-ICP é obrigatório.** Um ICP sem anti-ICP está incompleto. Saber quem não atender é tão estratégico quanto saber quem atender.
- **Se o usuário não sabe responder algum critério**, marque como "A validar" e sugira como coletar esse dado (entrevista com cliente, análise de base, etc.).

---

## Referências adicionais
Para casos mais complexos (múltiplos ICPs, mercado internacional, ICP B2C), leia:
- `references/icp-avancado.md` — ICPs múltiplos, scoring, internacionalização
- `references/icp-b2c.md` — Adaptação do framework para B2C e D2C
