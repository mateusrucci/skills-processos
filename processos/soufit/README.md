# Soufit / Grupo MDT — Processos e Ativos

Espelho versionado do que esta publicado no ClickUp (espaco **Marketing MDT**). Atualizado manualmente de tempos em tempos.

## Estrutura

```
soufit/
├── processos-internos/        # Espelho da pasta "Processos Internos" no ClickUp
│   ├── trafego/POP-TRAF-001.md
│   ├── crm/POP-CRM-001.md
│   └── copy/POP-COPY-001.md
└── ativos-marketing/          # Espelho da pasta "Ativos do Marketing" no ClickUp
    ├── produtos/              # 20 dossies cientificos (1 por SKU)
    ├── design-system.md
    └── calendarios/
        ├── marketing-anual.md
        └── marketing-afiliados.md
```

## Mapeamento Git → ClickUp

| Aqui no git | No ClickUp (Marketing MDT) |
|---|---|
| `processos-internos/<area>/POP-XXX-NNN.md` | Pasta "Processos Internos" > Doc `<Area>` > Page `POP-XXX-NNN` |
| `ativos-marketing/produtos/<Nome>.md` | Pasta "Ativos do Marketing" > Doc "Produtos" > Page `<Nome>` |
| `ativos-marketing/design-system.md` | Pasta "Ativos do Marketing" > Doc "Design System" > Page "Design System Soufit v2" |
| `ativos-marketing/calendarios/marketing-anual.md` | Pasta "Ativos do Marketing" > Doc "Calendario Marketing Anual" |
| `ativos-marketing/calendarios/marketing-afiliados.md` | Pasta "Ativos do Marketing" > Doc "Calendario Marketing Afiliados" |

## Padroes

- **POPs:** seguem metodologia Falconi (8 blocos: Cabecalho, Objetivo, Material, Passos Criticos, Manuseio, Resultados, Acoes Corretivas, Aprovadores, Fontes). Empresa = `Soufit` sempre. Sem acentos em campo de empresa, codigo, area.
- **Produtos:** dossies completos com base cientifica, claims ANVISA literais, referencias com DOI, modo de uso, seguranca, persona, objecoes.
- **Calendarios:** seguir os templates dos placeholders quando forem construidos.

## Atualizacoes recentes

- 2026-05-30 — Estrutura inicial criada com 3 POPs, 20 produtos, Design System, 2 placeholders de calendario.
