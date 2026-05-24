---
name: falconi-pop-docx
description: Cria Processos Operacionais Padrao (POPs) em DOCX no modelo Falconi a partir de aulas, transcricoes, anexos, links ou materiais encontrados no Gmail/Drive. Use quando o usuario pedir POP, procedimento operacional padrao, SOP, processo operacional, modelo Falconi, transformar aula em processo, documentar rotina, criar manual de execucao, ou gerar .docx operacional com passos criticos, materiais, resultados esperados, acoes corretivas e aprovacao.
---

# Falconi POP DOCX

## Objetivo

Transformar aulas, transcricoes e materiais de treinamento em um Processo Operacional Padrao em `.docx`, seguindo a logica visual e estrutural do modelo Falconi: cabecalho de controle, material necessario, passos criticos, manuseio do material, resultados esperados, acoes corretivas e aprovacao.

Quando o pedido envolver documento `.docx`, use tambem a skill `documents:documents` se ela estiver disponivel para gerar, renderizar e verificar visualmente o arquivo final.

## Fluxo

1. Coletar materiais
   - Procurar aulas, transcricoes, anexos e links nos conectores disponiveis.
   - Se houver Gmail disponivel, buscar por termos do usuario, assunto da aula, remetente, data, nome do treinamento e palavras como `transcricao`, `aula`, `gravacao`, `drive`, `meet`, `zoom`, `loom`.
   - Se Gmail nao estiver disponivel, usar Google Drive quando os materiais estiverem linkados/sincronizados, ou pedir ao usuario os arquivos/exportacoes necessarios.
   - Baixar ou ler apenas os materiais relevantes. Nao inventar conteudo ausente.

2. Extrair o procedimento
   - Identificar a tarefa operacional principal ensinada na aula.
   - Separar contexto explicativo de instrucao executavel.
   - Converter falas longas em comandos objetivos, verificaveis e em ordem.
   - Preservar numeros, limites, prazos, criterios de qualidade, nomes de ferramentas, campos, telas, links e excecoes.
   - Registrar lacunas como `A confirmar:` quando a aula nao fornecer dado suficiente.

3. Estruturar no modelo Falconi
   - Usar a referencia em `references/modelo-falconi-pop.md`.
   - Criar um POP por tarefa operacional. Se a aula cobrir varias rotinas independentes, sugerir dividir em multiplos POPs.
   - Manter linguagem de execucao: verbo no infinitivo ou imperativo, frases curtas, uma acao por passo.

4. Gerar o DOCX
   - Preferir o script `scripts/generate_pop_docx.py` quando houver um POP estruturado em JSON.
   - Para documentos mais elaborados, usar ferramentas da skill `documents:documents`, mantendo as secoes obrigatorias.
   - Salvar em caminho claro, com nome como `POP - Nome da tarefa.docx`.

5. Verificar qualidade
   - Renderizar ou abrir o DOCX quando possivel.
   - Conferir se tabelas cabem na pagina, numeracao esta correta e nao ha texto quebrado de forma ruim.
   - Revisar contra a transcricao para evitar alucinacao operacional.

## JSON para o script

Use este formato como entrada para `scripts/generate_pop_docx.py`:

```json
{
  "empresa": "Nome da empresa",
  "area": "Area ou departamento",
  "nome_tarefa": "Nome da tarefa",
  "responsavel": "Cargo responsavel",
  "codigo": "POP-001",
  "estabelecido_em": "24/05/2026",
  "revisado_em": "",
  "numero_revisao": "primeira",
  "objetivo": "Resultado que o procedimento deve garantir.",
  "materiais": [
    {"item": "Ferramenta ou material", "quantidade": "1", "observacao": "Quando necessario"}
  ],
  "passos_criticos": [
    "Executar a primeira acao critica.",
    "Conferir o criterio de qualidade."
  ],
  "manuseio_material": [
    "Guardar materiais e arquivos no local definido."
  ],
  "resultados_esperados": [
    "Resultado observavel e mensuravel."
  ],
  "acoes_corretivas": [
    "Se ocorrer erro, verificar causa provavel e acionar responsavel."
  ],
  "aprovadores": ["Executor", "Supervisor", "Chefia"],
  "fontes": [
    "Aula/transcricao usada como evidencia"
  ]
}
```

Rodar:

```bash
python3 /Users/mateusrucci/.codex/skills/falconi-pop-docx/scripts/generate_pop_docx.py entrada.json saida.docx
```

## Padroes de escrita

- Titulo da tarefa deve ser especifico: `Publicar campanha no Meta Ads`, nao `Campanhas`.
- Cada passo critico deve conter uma acao verificavel.
- Resultados esperados devem dizer como saber que deu certo.
- Acoes corretivas devem cobrir erros provaveis da execucao, nao conselhos genericos.
- Materiais incluem softwares, acessos, planilhas, templates, credenciais, URLs, arquivos e equipamentos.
- Se houver risco de compliance, dados financeiros, acesso de cliente ou impacto em producao, incluir checagens e aprovacao antes da execucao.
- Nao transformar principios conceituais em passo operacional sem evidencia na aula.
