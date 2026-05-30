# Skill: criacao-pop

Cria Procedimentos Operacionais Padrão (POPs) seguindo metodologia Vicente Falconi, no formato padronizado Soufit/Soulve, com saída em `.docx` validada automaticamente.

---

## Instalação

### Opção 1: Claude Code (recomendado para uso por todo o time)

```bash
# Copie a pasta inteira para a pasta de skills do seu repo
cp -r criacao-pop ~/soufit-os/.claude/skills/

# ou globalmente
cp -r criacao-pop ~/.claude/skills/
```

### Opção 2: Skill upload no Claude.ai (Pro/Team/Enterprise)

1. Vá em **Settings → Skills**
2. Upload da pasta `criacao-pop`
3. Skill fica disponível em qualquer conversa

---

## Dependências

O script usa apenas uma biblioteca Python:

```bash
pip install python-docx
```

Tudo o mais é stdlib.

---

## Como usar

### Pelo Claude (automático)

Em qualquer conversa, peça naturalmente:

> "Quero criar um POP para [tarefa]. Material: [transcrição/aula/etc]"

A Claude vai:
1. Carregar a skill `criacao-pop` automaticamente
2. Ler um exemplo para calibrar
3. Coletar os dados
4. Validar qualidade Falconi
5. Gerar o `.docx`

### Direto via script (para automação)

Se você já tem o JSON pronto:

```bash
python scripts/generate_pop.py \
  --data caminho/para/dados.json \
  --output POP-XXX-NNN.docx
```

Schema do JSON: `references/pop_schema.json`
Exemplos: `references/exemplos-completos/*.json`

---

## Estrutura

```
criacao-pop/
├── README.md                              ← este arquivo
├── SKILL.md                               ← instruções para Claude
├── scripts/
│   └── generate_pop.py                    ← gerador .docx com validação Falconi
└── references/
    ├── pop_schema.json                    ← schema do input JSON
    ├── template-pop.md                    ← template em Markdown (leitura humana)
    ├── falconi-principios.md              ← fundamentos teóricos
    ├── exemplos.md                        ← índice + próximos números por área
    ├── guia-para-o-time.md                ← guia de uso para membros do squad
    └── exemplos-completos/
        ├── POP-CRM-001.json               ← exemplo (fonte limpa)
        ├── POP-TRAF-001.json              ← exemplo (fonte truncada)
        └── POP-COPY-001.json              ← exemplo (fonte truncada)
```

---

## Validações automáticas (Falconi rigoroso)

O script trava o `.docx` se:

- Faltar qualquer um dos 8 campos obrigatórios
- Código do POP fora do formato `POP-AREA-NNN`
- Menos de 3 itens em material necessário
- Menos de 15 ou mais de 30 passos críticos
- Menos de 4 ou mais de 8 itens em manuseio
- Menos de 5 ou mais de 10 resultados / ações corretivas
- Qualquer ação corretiva não começando com "Se "

---

## Manutenção

Quando criar um POP novo:

1. Adicione a linha em `references/exemplos.md` (tabela de POPs ativos)
2. Atualize o "próximo número" da área correspondente
3. Salve o JSON do POP novo em `references/exemplos-completos/` (vira referência futura)
4. Faça commit no Git para versionar

---

## Suporte

Dúvidas sobre a metodologia: leia `references/falconi-principios.md`
Dúvidas sobre uso pelo time: leia `references/guia-para-o-time.md`
Bugs no script: abrir issue no repo
