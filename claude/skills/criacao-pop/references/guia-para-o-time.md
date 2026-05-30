# Guia de uso para o time — Skill criacao-pop

Este guia é para **membros do time da Soufit/Soulve** que vão usar a skill `criacao-pop` para padronizar processos. Não é para o Mateus apenas — é para qualquer pessoa do squad.

---

## Quando usar

**Use a skill quando:**
- ✅ Você terminou um treinamento, aula ou reunião que ensina **como executar uma tarefa específica** e quer transformar em processo padronizado
- ✅ Você descobriu uma forma melhor de executar uma rotina e quer registrar o método
- ✅ Você está fazendo onboarding de alguém novo no squad e percebe que falta um POP para uma tarefa crítica
- ✅ Você identificou um erro recorrente que poderia ser evitado com um padrão claro

**Não use a skill para:**
- ❌ Decisões estratégicas (isso é diretriz ou política, não POP)
- ❌ Frameworks conceituais (isso é playbook)
- ❌ Tarefas que cada pessoa faz de um jeito e tudo bem (não vale o esforço)
- ❌ Verificações simples (isso é checklist, não POP)

---

## Como abrir a conversa com Claude

**Padrão recomendado:**

```
Quero criar um POP para [nome da tarefa].

Material de origem: [transcrição / reunião / observação direta / etc.]
Empresa: [Soufit / Soulve]
Área: [CRM / Tráfego / Copy / etc.]
Responsável: [cargo]

[Cole aqui o material bruto, se houver]
```

Se o material bruto for um arquivo (vídeo, áudio, PDF, transcrição), faça upload junto com o pedido.

---

## O que esperar do Claude

A Claude vai:

1. **Ler 1 POP de exemplo** para calibrar o tom e formato
2. **Confirmar os campos do cabeçalho** (empresa, área, código POP, responsável, data, revisão)
3. **Extrair os 8 blocos** do material que você enviou
4. **Validar a qualidade** automaticamente (Falconi)
5. **Gerar o .docx final** pronto para circular
6. **Resumir no chat** o que foi gerado (sem despejar o POP inteiro)

**Se faltar informação**, ela vai te perguntar antes de gerar. **Não vai inventar.**

---

## Sua responsabilidade depois

A skill **te dá um rascunho de alta qualidade**, mas ele não é oficial até passar pelo ciclo PDCA da Falconi:

1. **P (Plan)** — você revisa o POP gerado. Tem algo que você faz e não está ali? Adicione. Tem algo ali que você não faz desse jeito? Ajuste.
2. **D (Do)** — execute conforme o POP por algumas semanas
3. **C (Check)** — verifique se os "Resultados esperados" estão saindo
4. **A (Act)** — se não, peça revisão (`POP-XXX-NNN revisão 2`)

**Não use o POP no dia 1 sem revisar.** A Claude faz 80% do trabalho; os outros 20% são seus.

---

## Como salvar e versionar

**Local oficial:** [a definir pelo Mateus — provavelmente Notion ou ClickUp Docs]

**Nomenclatura do arquivo:** `POP-[ÁREA]-[NNN]-[nome-tarefa-em-kebab].docx`
- ✅ `POP-CRM-002-criar-email-de-abandono-de-carrinho.docx`
- ❌ `POP novo CRM.docx`

**Versionamento:**
- Toda mudança gera **nova revisão** (não sobrescrever a anterior)
- Atualizar o número em "Nº da revisão" no cabeçalho
- Preencher "Revisado em: DD/MM/AAAA"
- Manter histórico das versões anteriores

---

## Quem aprova

Por padrão, o POP tem 3 linhas de assinatura:

1. **Executor [área]** — quem executa a tarefa no dia-a-dia
2. **Supervisor** — quem coordena a execução
3. **Chefia** — quem é responsável pelo resultado da área

Em squads pequenos, 2 das 3 pessoas podem ser a mesma. Em squads grandes, são 3 pessoas diferentes. **Nenhum POP é oficial sem as 3 assinaturas.**

---

## Quando questionar e escalar

**Questione com o Mateus / chefia se:**
- Você acha que a tarefa não cabe em um POP (talvez seja framework, decisão ou checklist)
- O processo depende muito de julgamento e padronizar pode atrapalhar
- Você não consegue definir resultados verificáveis claros
- O Claude validou e gerou, mas você sente que falta algo essencial

**Escalonar é parte do processo.** POP ruim é pior que POP nenhum.

---

## Dúvidas frequentes

**P: Posso editar o .docx depois?**
R: Pode, mas o ideal é regerar via skill para manter o padrão. Edição manual quebra a consistência visual entre POPs.

**P: E se o material que tenho está incompleto?**
R: A Claude vai sinalizar isso no campo "Fontes" do POP (como fez com o POP-TRAF-001 e POP-COPY-001). O POP entra como "rascunho a revisar" até alguém com conhecimento prático fechar as lacunas.

**P: Posso fazer POP de uma tarefa que só eu faço?**
R: Só vale se você espera que outras pessoas façam no futuro. Senão, é só você organizando seu próprio trabalho — use uma nota pessoal.

**P: Quantos POPs por área devem existir?**
R: O suficiente pra cobrir as **tarefas críticas** da área. Não é meta. Não é volume. É cobertura das atividades que se feitas errado machucam o time.

**P: Quando devo revisar um POP existente?**
R: A cada 6 meses no mínimo, ou sempre que: o processo mudou, surgiu uma nova falha recorrente, ou uma ferramenta nova entrou no fluxo.
