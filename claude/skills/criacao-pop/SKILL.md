---
name: criacao-pop
description: |
  Cria Procedimentos Operacionais Padrão (POPs) seguindo a metodologia Vicente Falconi, no formato padronizado Soufit/Soulve, com saída em arquivo .docx pronto para circular e ser assinado. Use esta skill SEMPRE que o usuário pedir para "criar um POP", "padronizar um processo", "documentar como fazer X", "transformar essa aula/treinamento em POP", "estruturar o procedimento de Y", "POP para [qualquer área]", "padronizar a tarefa de", "fazer o procedimento operacional", ou enviar transcrição de aula/treinamento/reunião/conversa e pedir para virar processo documentado. Também use quando o usuário enviar material bruto (vídeo, transcrição, notas, áudio, conversa) sobre como executar uma tarefa específica e pedir estruturação. A skill aplica os 8 blocos padronizados (Cabeçalho, Objetivo, Material, Passos Críticos, Manuseio, Resultados, Ações Corretivas, Aprovação), valida qualidade Falconi automaticamente e gera o arquivo .docx final.
---

# Criação de POP — Soufit / Soulve

Skill de padronização de processos baseada em **Vicente Falconi** (*Gerenciamento da Rotina do Trabalho do Dia-a-Dia*) com saída em **.docx** no formato padronizado da Soufit/Soulve, pronto para uso pelo time.

---

## Princípio fundamental

Um POP é **o melhor jeito conhecido HOJE** de executar uma tarefa crítica. Não é manual exaustivo. Não é teoria. É **prescrição executável** para que qualquer pessoa minimamente treinada produza o mesmo resultado.

**Critérios para uma tarefa virar POP:**
- É **crítica** (se feita errado, gera perda, retrabalho ou risco)
- É **repetível** (acontece com frequência razoável)
- Tem **resultado observável** (dá pra medir se foi bem feita)
- Pode ser **executada por mais de uma pessoa**

Se a tarefa falha em algum desses critérios, **questione com o usuário se realmente precisa de POP** antes de criar.

---

## Workflow obrigatório

### Etapa 1 — Calibrar lendo 1 exemplo

**Antes de qualquer pergunta ao usuário**, leia **1 exemplo completo** da pasta `references/exemplos-completos/` para calibrar formato, granularidade e tom:

- `POP-CRM-001.json` — fonte limpa (treinamento bem transcrito)
- `POP-TRAF-001.json` — fonte truncada (sinalizada no rodapé)
- `POP-COPY-001.json` — fonte truncada (outro exemplo de sinalização conservadora)

Prefira o exemplo da área mais próxima ao processo que está sendo padronizado.

### Etapa 2 — Coletar inputs

Pergunte (ou extraia do material enviado):

1. **Empresa** — **DEFAULT: Soufit**. Só usar outro valor se o usuário pedir explicitamente "Soulve" ou outro cliente nomeado. **NUNCA usar "Modernitty", "Modernity" ou "Fit Moderno"** como nome de empresa — esses são nomes de repositório/produto/marca interna, **não** o nome da pessoa jurídica. Se o material vier de uma pasta `/Modernitty/...` ou similar, isso é apenas path do repositório de código; a empresa continua sendo **Soufit** (ou Soulve, se o usuário indicar).
2. **Área** (CRM, Tráfego, Copy, Operacional, etc.) → define os 3 primeiros caracteres do código
3. **Nome da tarefa** (verbo no infinitivo: "Estruturar fluxos de e-mail")
4. **Responsável** (cargo, não pessoa: "Gestor de tráfego")
5. **Número da revisão** (primeira / 2ª / 3ª)
6. **Fonte do conteúdo** (transcrição, treinamento, observação direta, prática consolidada)

Para o **código do POP**, consulte `references/exemplos.md` e proponha o próximo número da área. Se a área for nova, comece com 001.

### Etapa 3 — Extrair os 8 blocos

Carregue `references/falconi-principios.md` para critérios de qualidade. Para cada bloco:

| Bloco | Regra |
|---|---|
| **Objetivo** | 1 frase começando com verbo no infinitivo ("Garantir...", "Padronizar..."). Responde: o que esse POP garante quando bem executado? |
| **Material necessário** | 3 a 8 itens com item / quantidade / observação. Tudo que a pessoa precisa ter em mãos antes de começar. |
| **Passos críticos** | **15 a 25 ações observáveis** (15 mínimo, 25 ideal, 30 limite). Verbo no infinitivo + objeto + critério. Inclui decisões condicionais, valores específicos, sequências temporais. |
| **Manuseio do material** | 4 a 8 itens sobre onde salvar, como nomear, versionar, restrições. |
| **Resultados esperados** | 5 a 10 outputs **verificáveis** (alguém consegue olhar e dizer se aconteceu). |
| **Ações corretivas** | 5 a 10 itens, **todos iniciando com "Se..."**. Cobre os principais modos de falha. |

### Etapa 4 — Gerar o JSON estruturado

Monte um arquivo JSON seguindo o schema em `references/pop_schema.json`. Use os exemplos `.json` em `references/exemplos-completos/` como referência exata de estrutura.

**Salve em** `/home/claude/pop_data.json` (ou caminho equivalente do ambiente).

### Etapa 5 — Rodar o gerador

```bash
python scripts/generate_pop.py \
  --data /home/claude/pop_data.json \
  --output /mnt/user-data/outputs/POP-XXX-NNN.docx
```

### Etapa 5.5 — Commit no git ANTES do ClickUp (regra inviolável)

**Toda alteração de POP ou ativo Soufit precisa entrar no repositório `skills-processos` ANTES de ser publicada no ClickUp.** Ordem obrigatória:

1. **Gerar/atualizar o arquivo `.md` do POP** no repo `/Users/mateusrucci/Desktop/repos/skills-processos/processos/soufit/processos-internos/<area>/POP-XXX-NNN.md`. Mesmo formato Falconi 8 blocos descrito acima.
2. **Atualizar também o `.docx`** (output do gerador) em `/Modernitty/pops-falconi/` se for um POP que circula assinado.
3. **`git add` + `git commit`** no repo `skills-processos` com mensagem do tipo `Adiciona POP-XXX-NNN <area> <tema curto>` ou `Atualiza POP-XXX-NNN — <motivo>`.
4. **`git push origin main`** para o repo remoto `mateusrucci/skills-processos`.
5. **Somente depois disso**: criar/atualizar a page correspondente no ClickUp (folder "Processos Internos" > doc da area > page com nome do POP).

Se a publicação no ClickUp falhar, o git já tem a fonte preservada. Se o git falhar, **NÃO subir no ClickUp** — corrigir o git primeiro.

Mesma regra vale para ativos de marketing (produtos, design system, calendários): `ativos-marketing/` no git primeiro, ClickUp depois.

O script:
- **Valida automaticamente** todos os critérios Falconi (número mínimo/máximo de itens por bloco, "Se" nas ações corretivas, campos obrigatórios)
- **Falha com erro claro** se algo estiver fora do padrão
- **Gera o .docx** com formatação fiel aos POPs originais (tabela 3 colunas, células mescladas, cabeçalhos cinzas)

### Etapa 6 — Entregar

Se a validação passou:
1. Use `present_files` para entregar o `.docx` ao usuário
2. Sumarize: código do POP, nº de passos, nº de ações corretivas, fonte usada
3. Pergunte se quer ajustar algo antes de versionar

Se a validação falhou:
1. Mostre os erros ao usuário
2. **Não invente conteúdo para satisfazer a validação** — pergunte ao usuário para preencher as lacunas
3. Regere após ajustes

---

## Regras invioláveis

1. **Nunca invente conteúdo operacional.** Se a fonte (transcrição/material) está truncada ou genérica, marque no rodapé "Fontes" que o material foi truncado e que o POP deve ser revisado pelo responsável (como nos exemplos POP-TRAF-001 e POP-COPY-001).

2. **Nunca pule blocos.** Os 8 blocos são obrigatórios — a validação trava.

3. **Nunca abstraia demais nos passos críticos.** Se o passo não diz "o que fazer" de forma observável, está errado.

4. **Ações corretivas SEMPRE começam com "Se..."** — a validação rejeita o contrário.

5. **Se o usuário enviar transcrição truncada/de baixa qualidade**, sinalize no rodapé "Fontes" e seja conservador (não invente passos que não estão na fonte).

6. **Não responda com o POP em chat.** O entregável é o `.docx`. No chat, só o sumário.

7. **Nomenclatura do arquivo:** `POP-[ÁREA]-[NNN]-[nome-tarefa-em-kebab].docx`
   Exemplo: `POP-CRM-001-estruturar-fluxos-de-email.docx`

---

## Anti-padrões a evitar

| Anti-padrão | Por quê |
|---|---|
| POP narrativo em vez de prescrição numerada | Vira manual, não procedimento |
| POP sem responsável claro | Ninguém executa, ninguém revisa |
| POP com 40+ passos | Quebrar em 2 ou 3 POPs |
| Passos vagos: "fazer bem feito", "garantir qualidade" | Inexecutável |
| POP sem ações corretivas | Todo processo falha; preveja os modos |
| Misturar teoria e ação no mesmo passo | Confunde o executor |
| Promessas no objetivo que o conteúdo não entrega | Quebra o contrato com quem usa |

---

## Códigos de área (3 letras)

| Área | Código |
|---|---|
| CRM / E-mail | CRM |
| Tráfego Pago | TRAF |
| Copywriting | COPY |
| Criativo / Design | CRT |
| Influenciadores | INF |
| Afiliados | AFL |
| Marketplace | MKT |
| Operacional | OPS |
| Financeiro | FIN |
| Desenvolvimento | DEV |
| Web Design | WEB |
| Social Media | SOC |
| Atendimento | ATD |
| RH / Pessoas | RH |
| Comercial | COM |

---

## Referências

- `scripts/generate_pop.py` — gerador `.docx` com validação Falconi embutida
- `references/pop_schema.json` — schema JSON do input
- `references/template-pop.md` — template em Markdown (uso humano, leitura rápida)
- `references/falconi-principios.md` — fundamentos teóricos
- `references/exemplos.md` — índice dos POPs já criados + próximos números
- `references/guia-para-o-time.md` — guia de uso para membros do time
- `references/exemplos-completos/POP-CRM-001.json` — exemplo completo (fonte limpa)
- `references/exemplos-completos/POP-TRAF-001.json` — exemplo completo (fonte truncada)
- `references/exemplos-completos/POP-COPY-001.json` — exemplo completo (fonte truncada)
