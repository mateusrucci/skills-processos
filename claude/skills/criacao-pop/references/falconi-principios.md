# Princípios Falconi por trás do POP

Vicente Falconi — *Gerenciamento da Rotina do Trabalho do Dia-a-Dia* (1994) e *TQC: Controle da Qualidade Total no Estilo Japonês* (1992).

---

## Por que padronizar

> "Não se pode melhorar o que não está padronizado."

Sem padrão, cada execução é uma nova invenção. Variação alta = resultado imprevisível = impossível identificar causa raiz quando algo dá errado. O POP **trava o método** para depois conseguir **melhorar o método**.

## O que é um POP (no rigor Falconi)

POP = **documento que descreve a forma correta de executar uma tarefa**, validada por quem executa e aprovada por quem é responsável pelo resultado.

**Características obrigatórias:**
1. **Simples** — qualquer pessoa minimamente treinada entende e executa
2. **Específico** — não deixa margem para interpretação
3. **Executável** — descreve ações, não conceitos
4. **Medível** — o output pode ser verificado
5. **Revisável** — tem data, versão e responsável

## Critérios para uma tarefa virar POP

Falconi divide tarefas em 3 grupos:

| Tipo | Exemplo | Vira POP? |
|---|---|---|
| **Tarefa crítica padronizável** | Calcular comissão de afiliado, lançar campanha no Meta | ✅ Sim |
| **Tarefa rotineira sem variação** | Salvar arquivo em pasta | ❌ Não vale o esforço |
| **Tarefa criativa não-replicável** | Decidir nova estratégia de marca | ❌ Não cabe POP, cabe framework |

**Antes de criar um POP, pergunte:**
- Essa tarefa é executada por mais de uma pessoa?
- Se feita errado, gera perda ou retrabalho relevante?
- Tem um "jeito melhor conhecido hoje" que vale ser fixado?

Se as três respostas forem sim → vira POP.

## Quem cria o POP

> "O POP deve ser escrito por quem executa, validado por quem supervisiona e aprovado por quem é responsável pelo resultado."

Por isso o template tem 3 assinaturas: **Executor / Supervisor / Chefia**.

Na prática, com IA: a Claude ajuda a estruturar, mas o **executor real precisa revisar** antes de virar oficial. POP imposto de cima vira papel morto.

## Ciclo PDCA aplicado ao POP

| Fase | Ação |
|---|---|
| **P (Plan)** | Escrever o POP — definir o padrão |
| **D (Do)** | Executar conforme o POP |
| **C (Check)** | Verificar se resultados esperados estão saindo |
| **A (Act)** | Se sim, manter; se não, revisar o POP (nova versão) |

Por isso o cabeçalho tem "Estabelecido em" + "Revisado em" + "Nº da revisão". POP sem ciclo de revisão é POP morto.

## Por que existem "Ações corretivas" no POP

Falconi: **todo processo falha**. A diferença entre operação amadora e profissional é se a falha foi **prevista e tem resposta pré-definida**, ou se vira incêndio.

As ações corretivas (sempre começando com "Se...") são a **biblioteca de respostas a falhas conhecidas**. Cada vez que uma falha nova aparece e é resolvida, vira nova ação corretiva na próxima revisão.

## Hierarquia de documentos (contexto)

| Nível | Documento | Pergunta que responde |
|---|---|---|
| Estratégico | Política / Diretriz | Por que fazemos? |
| Tático | Manual / Playbook | Como pensamos sobre isso? |
| **Operacional** | **POP** | **Como executamos passo a passo?** |
| Registro | Checklist / Formulário | O que foi feito? |

POP fica na camada operacional. Não confunda com playbook (que é mais conceitual) nem com checklist (que é só verificação).

## Aplicação Soufit/Soulve

- POPs vivem em pasta centralizada (futuramente: `clickup_docs` ou Notion database de POPs)
- Cada área tem prefixo próprio (POP-CRM, POP-TRAF, POP-COPY...)
- Revisão mínima: a cada 6 meses ou quando o processo mudar
- Toda mudança gera nova revisão (não sobrescrever, manter histórico)
- POP é referência **obrigatória** para onboarding de novos membros do squad
