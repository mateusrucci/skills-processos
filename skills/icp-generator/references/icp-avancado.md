# ICP Avançado — Múltiplos Segmentos, Scoring e Internacionalização

## Quando usar este arquivo
Leia este arquivo quando:
- O usuário tem múltiplos segmentos e precisa priorizar
- O usuário quer expandir para mercado internacional (especialmente US)
- O usuário precisa de um sistema de scoring para qualificar leads em escala

---

## ICPs Múltiplos — Como priorizar

Quando o negócio atende mais de um perfil de cliente, monte uma **Matriz de Priorização de ICP**:

| Segmento | Fit (1-5) | Propensão (1-5) | Deal Size (1-5) | Velocidade (1-5) | Score Total |
|---|---|---|---|---|---|
| Segmento A | | | | | |
| Segmento B | | | | | |
| Segmento C | | | | | |

**Definições:**
- **Fit**: O quanto o cliente se beneficia da solução (problema real, solução adequada)
- **Propensão**: O quanto está pronto para comprar agora (gatilho ativo, budget, urgência)
- **Deal Size**: Valor do contrato relativo ao esforço de venda
- **Velocidade**: Rapidez do ciclo de decisão

**Regra:** Foque no segmento com maior score total. Nunca tente atender todos simultaneamente com a mesma mensagem.

---

## ICP para Mercado Internacional (US Market)

Adaptações obrigatórias ao mapear ICP para o mercado americano:

### Firmográfico
- Substituir faixas de faturamento em R$ por USD (referência: empresa com $1M-$10M ARR = scale-up típico)
- Usar SIC codes ou NAICS codes para classificação de setor
- Considerar diferenças regionais: West Coast (tech), East Coast (finance/consulting), Midwest (manufacturing)

### Comportamento de compra
- Ciclos de decisão mais rápidos em startups americanas vs. brasileiras
- Champions têm mais autonomia para aprovar orçamentos menores (<$5k/mês sem aprovação de CFO)
- Avaliações via G2, Capterra, Trustpilot têm peso maior na decisão
- Trials e POCs (Proof of Concept) são esperados antes da compra

### Sinais de identificação (US)
- Crunchbase (funding rounds, investidores)
- LinkedIn Sales Navigator (job titles, company size, hiring signals)
- G2 (reviews, comparações com concorrentes)
- BuiltWith / Similartech (tech stack)
- Inc. 5000 / Deloitte Fast 500 (empresas de crescimento rápido)

### Canais de sourcing (US)
- LinkedIn Sales Navigator (principal)
- Apollo.io
- ZoomInfo
- Clay (enriquecimento)
- Eventos: SaaStr, HubSpot INBOUND, Dreamforce, Product Hunt

---

## Sistema de Lead Scoring baseado no ICP

Monte um sistema de pontos para qualificar leads automaticamente:

### Critérios e pontuação sugerida

**Firmográfico (máx 30 pontos)**
- Setor correto: +10
- Faturamento dentro da faixa: +10
- Tamanho de time correto: +5
- Localização adequada: +5

**Propensão (máx 40 pontos)**
- Gatilho de compra ativo identificado: +20
- Budget confirmado ou provável: +10
- Decisor mapeado: +10

**Comportamento (máx 30 pontos)**
- Visitou site/landing page: +5
- Solicitou diagnóstico/demo: +15
- Respondeu outbound: +10

**Anti-ICP (penalização)**
- Qualquer deal-breaker identificado: -100 (desqualificação imediata)

**Classificação:**
- 70-100 pontos: ICP quente — prioridade máxima
- 40-69 pontos: ICP morno — nutrir e qualificar mais
- 0-39 pontos: Fora do ICP — não investir tempo

---

## Validação do ICP

O ICP nunca está 100% pronto. Valide continuamente:

1. **Win/Loss Analysis**: De cada 10 deals, quantos ICPs fecharam? Quantos não-ICPs fecharam?
2. **Churn por segmento**: Clientes ICP churnam menos? Se não, o ICP está errado.
3. **Ciclo de venda por segmento**: ICP real fecha mais rápido. Se não, revisar propensão.
4. **NPS por segmento**: ICP real é mais satisfeito. Se não, revisar fit.

Revisão recomendada: a cada 90 dias ou após fechar 20+ novos clientes.
