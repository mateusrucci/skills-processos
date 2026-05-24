---
name: rucci-carousel
description: Cria carrosseis para o Mateus Rucci com base no Banco de Carrosseis e nos modelos visuais atuais de card. Use quando ele pedir carrossel, carousel, slides, cards para Instagram ou LinkedIn, ou quando quiser transformar uma tese, case, tutorial, opinião forte ou insight em formato de carrossel. Consulte SEMPRE a skill rucci-copy em /Users/mateusrucci/.codex/skills/rucci-copy/SKILL.md antes de escrever a copy. O fluxo desta skill e obrigatorio: primeiro entender as referencias e entregar apenas a copy para aprovacao; so depois da aprovacao entregar a direcao visual com a copy e executar.
---

# rucci-carousel

Skill dedicada a criar carrosseis no estilo do Mateus Rucci a partir de duas camadas:

1. repertorio narrativo do acervo em `/Users/mateusrucci/Desktop/Banco de Carrosseis`
2. sistema visual atual dos cards enviado nos arquivos HTML

Esta skill existe para impedir um erro especifico: pular para design antes da copy estar aprovada.

## Leitura obrigatoria antes de qualquer resposta

### 1. Consulte SEMPRE a skill rucci-copy

Abra `/Users/mateusrucci/.codex/skills/rucci-copy/SKILL.md`.

Dependendo do pedido, leia tambem os arquivos necessarios dentro de `/Users/mateusrucci/.codex/skills/rucci-copy/references/`:

- `formato-organico.md`
- `hooks-library.md`
- `frameworks.md`
- `icp-mentoria.md` ou `icp-implementacao.md` quando o carrossel vender um produto do Mateus

### 2. Leia as referencias desta skill

- `references/acervo-playbook.md`
- `references/modelos-cards-atuais.md`

### 3. Se o usuario mandou arquivos de modelo, inspecione-os

Se houver HTML, imagens, screenshots ou cards anexados, leia esses arquivos antes de propor a direcao visual.

## Como pensar o trabalho

O acervo ensina **como a narrativa funciona**.

Os modelos HTML atuais ensinam **como o layout-base deve se comportar**.

Entao:

- o acervo define hook, progressao, densidade e CTA
- os modelos atuais definem paleta, estrutura, assinatura e acabamento

## Workflow obrigatorio

### Passo 1 - Identificar o tipo de carrossel

Classifique o pedido em uma destas familias:

- **opiniao forte**: tese dura, confronto, regra de lideranca
- **tutorial/utilitario**: passo a passo, ferramentas, checklist, playbook
- **case/engenharia reversa**: resultado, mecanismo, prova, fluxo
- **reframe emocional**: timing, perspectiva, validacao com densidade
- **single-slide manifesto**: frase de alto atrito que pode viver sozinha

Se o pedido estiver vendendo Mentoria ou Implementacao, trate como copy de produto e aplique a `rucci-copy` integralmente.

Se o pedido for conteudo de autoridade, IA, gestao ou opiniao, ainda assim use a `rucci-copy` como disciplina de copy:

- especificidade
- anti-generico
- hook forte
- 1 dor ou conflito central
- 1 CTA claro

### Passo 2 - Entender o objetivo do post

Defina internamente:

- objetivo principal: alcance, salvamento, comentario, DM, autoridade ou demanda
- conflito central
- big idea
- CTA de baixo atrito

Se faltar algo indispensavel, faca no maximo uma pergunta por vez.

### Passo 3 - Escrever somente a copy

Na primeira entrega, envie **apenas a copy para aprovacao**.

Nao entregue direcao visual, paleta, layout, escolha de modelo ou execucao nesta etapa.

Formato padrao:

```markdown
## Direcao de copy
- **Tipo de carrossel:** [opiniao / tutorial / case / reframe / manifesto]
- **Objetivo:** [alcance / comentario / DM / autoridade / etc.]
- **Big Idea:** [frase]
- **Conflito central:** [frase]
- **CTA:** [frase]

---

## Copy slide a slide
1. [hook]
2. [slide 2]
3. [slide 3]
...

---

## Notas
- [o que esta ancorando a copy]
- [o que pode virar variacao A/B]
```

### Passo 4 - Parar e esperar aprovacao

Depois de entregar a copy, pare.

So avance quando o usuario aprovar explicitamente a copy ou pedir ajustes.

### Passo 5 - So depois da aprovacao, entregar a direcao visual

Quando a copy for aprovada, entregue a direcao visual com a copy.

A direcao visual deve incluir:

- modelo-base escolhido (`v1` a `v6`) e por que
- familia visual (dark, white, navy, premium, tutorial, opiniao)
- regra tipografica
- logica de destaque
- uso ou nao de print, icone, diagrama, selo, barra, CTA-box
- mapeamento slide a slide

### Passo 6 - So executar se o usuario pedir

Apos copy aprovada e direcao visual definida, execute apenas se o usuario pedir para produzir os cards, HTMLs, layouts ou artes.

## Regras inviolaveis

1. **SEMPRE** consultar `rucci-copy` antes de escrever.
2. **NUNCA** pular direto para direcao visual na primeira resposta.
3. **NUNCA** misturar varias ideias no mesmo slide.
4. **SEMPRE** abrir com atrito, surpresa, confronto, beneficio claro ou resultado especifico.
5. **NUNCA** usar copy mole, abstrata ou coach generico.
6. **SEMPRE** usar 1 CTA de baixo atrito no fechamento.
7. **SEMPRE** exigir prova, exemplo, print, numero ou mecanismo quando a promessa for grande.
8. **NUNCA** inventar numero, case, print, ferramenta ou timeline.
9. **SEMPRE** escolher o visual em funcao da promessa, nao por gosto aleatorio.
10. **SEMPRE** preservar o minimalismo dos modelos atuais; nao encher de ornamento.

## Heuristicas de escrita para os slides

- 1 slide = 1 ideia
- pouco texto por slide
- 1 a 3 palavras com maior peso visual
- progressao linear
- sem explicacao redundante
- se a peca for tutorial, a utilidade precisa aparecer cedo
- se a peca for opiniao, a tese precisa ser instantaneamente entendida
- se a peca for case, a prova deve aparecer antes do meio

## Escolha rapida do tipo de abertura

Use uma das aberturas dominantes do acervo:

- mudanca de mercado
- resultado especifico fora da curva
- promessa utilitaria quantificada
- tese opinativa polarizadora
- reframe emocional com contraste

## Escolha rapida de CTA

Prefira CTAs de baixo atrito:

- comentar uma palavra-chave
- pedir guia, mapa ou tutorial
- seguir para acompanhar
- enviar para alguem especifico

Evite CTA de compra direta em carrossel de topo de funil, a menos que o pedido exija isso.
