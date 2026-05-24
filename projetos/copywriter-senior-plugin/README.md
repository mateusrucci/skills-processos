# copywriter-senior · Plugin Claude Code

Skill master de copywriting de altíssimo nível, destilada de 5 livros-bíblia do copy de resposta direta:

- **Great Leads** — Michael Masterson & John Forde
- **Quick-Start Copywriting System Vol 1 e 2** — Clayton Makepeace
- **A Carta de Vendas de 16 Palavras** — Evaldo Albuquerque
- **Ultimate Offer Formula** — Frank Kern
- **Breakthrough Advertising** — Eugene Schwartz (consciência + sofisticação)

## O que essa skill faz por você

Quando ativada, o Claude opera como um copywriter sênior treinado nesses 5 frameworks. Aplica:

- **One Belief** (Evaldo) — define a tese central da promoção em 16 palavras
- **Big Idea** (Ogilvy/Masterson) — uma frase memorável que sustenta a campanha
- **6 tipos de Lead** (Masterson) — escolha do lead ideal por nível de consciência
- **Escala de Schwartz** — 5 níveis de consciência × 5 níveis de sofisticação
- **10 perguntas sequenciais** (Evaldo) — copy que responde a tudo que o prospect pensa
- **9 etapas do close** (Carlton/Kern) — fechamento estruturado
- **15 princípios inquebráveis** — regras que aparecem nos 5 livros
- **24 lead starters + 10 templates de bullets** (Makepeace)
- **Compliance regulatório** (Anvisa, EFSA, plataformas de ads)

## Instalação

### Opção 1 — Marketplace (quando publicado)

```bash
# No Claude Code
/plugin install copywriter-senior
```

### Opção 2 — Instalação manual (clone do repo)

```bash
git clone https://github.com/SEU-USUARIO/copywriter-senior-plugin.git ~/copywriter-senior-plugin
# Depois copie ou symlinka:
ln -s ~/copywriter-senior-plugin/skills/copywriter-senior ~/.claude/skills/copywriter-senior
```

### Opção 3 — Instalação direta da skill

```bash
mkdir -p ~/.claude/skills
cp -R skills/copywriter-senior ~/.claude/skills/
```

Depois **reinicie o Claude Code** para que a skill seja carregada.

## Como usar

Após instalado, a skill é invocada **automaticamente** quando você pedir copy. Por exemplo:

- *"Escreve a copy completa de uma VSL para [produto]"*
- *"Cria a Big Idea e a One Belief para essa campanha"*
- *"Qual o tipo de lead ideal para esse público?"*
- *"Revisa essa copy e me diz onde tá fraco"*
- *"Monta a oferta irresistível usando o framework do Kern"*

Você também pode chamar explicitamente:

```
/copywriter-senior escreve uma carta de vendas para [produto]
```

## O que tem dentro

```
skills/copywriter-senior/
├── SKILL.md                                   # Instruções principais
└── references/
    ├── 01-master-compilation.md               # Visão geral consolidada
    ├── 02-great-leads-masterson.md            # 6 tipos de lead
    ├── 03-16-palavras-evaldo.md               # One Belief + 10 perguntas
    ├── 04-ultimate-offer-kern.md              # Close formula 9 etapas
    ├── 05-quick-start-makepeace.md            # Research, oferta, prova, momentum
    ├── 06-frameworks-essenciais.md            # Schwartz, Ogilvy, ABT, Cialdini
    └── 07-templates-prontos.md                # Templates de headline, bullet, garantia
```

## Quando NÃO usar essa skill

Esta é uma skill de **conhecimento profundo dos frameworks**. Para casos específicos, existem skills derivadas mais aplicadas:

- Copy de produtos do Mateus Rucci → `rucci-copy`
- Landing pages B2B → `b2b-landing-copy`
- Landing pages de pós-graduação → `posgrad-landing-copy`
- Posts de blog (não vendas) → `blog-writer`

## Filosofia

> "Pessoas amam comprar. Mas odeiam ser vendidas." — Frank Kern
>
> Essa skill segue o princípio de copy persuasivo ético: vender oferta excelente com narrativa que respeita a inteligência do prospect. Não usa urgência falsa, não fabrica escassez, não promete o que não entrega.

## Licença

MIT — use, modifique, redistribua. Apenas mantenha o crédito ao autor original e aos autores dos livros-bíblia.

## Autor

**Mateus Rucci** — SouFit / Grupo MDT
[mateusrucci.com.br](https://mateusrucci.com.br) · [@mateusrucci](https://instagram.com/mateusrucci)

## Contribuir

Pull requests bem-vindos. Especialmente:

- Templates regionais (BR vs PT vs ES)
- Cases adicionais por nicho
- Refinamento de prompts da skill principal

## Changelog

### 1.0.0 — 2026-05-24
- Lançamento inicial
- Skill master + 7 references
- Compatível com Claude Code 1.x e Codex CLI
