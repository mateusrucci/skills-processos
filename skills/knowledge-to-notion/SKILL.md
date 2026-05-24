---
name: knowledge-to-notion
description: Transforma conteúdo bruto em uma página completa no Notion, preenchendo todas as propriedades do database existente e gerando uma estrutura Markdown final para a página.
---

# Knowledge -> Notion (Preenchimento Completo)

## Quando usar

Use esta habilidade sempre que o usuário pedir para transformar texto bruto (Kindle, OCR, transcrições, notas) em uma entrada completa em um database do Notion com **todos os campos existentes preenchidos**.

## Objetivo

Gerar:
1. Propriedades do Notion **100% preenchidas** com base no schema real do database.
2. Conteúdo da página em Markdown, com seções claras e acionáveis.

## Passo a passo

1. **Ler o schema real do database**
   - Use o conector do Notion para inspecionar o database informado pelo usuário.
   - Liste as propriedades com tipos (title, select, multi_select, rich_text, number, date, status, etc.).
   - Não invente propriedades que não existam.

2. **Mapear o conteúdo bruto**
   - Extraia os temas principais.
   - Identifique conceitos, princípios e aplicações práticas.
   - Capture trechos exatos quando necessário, mas priorize clareza.

3. **Preencher todas as propriedades**
   - Cada propriedade existente deve ter valor.
   - Se uma propriedade for select/status, escolha a opção mais apropriada do conjunto existente.
   - Se uma propriedade exigir padrão específico (ex.: data), use um valor coerente e explícito.
   - Nunca deixe vazio.

4. **Montar o conteúdo da página**
   - Estrutura mínima recomendada:
     - Definição
     - Princípios
     - Frameworks
     - Erros / Armadilhas
     - Aplicação prática
     - Insights-chave

5. **Entregar o output final**
   - Primeiro um bloco JSON com as propriedades.
   - Depois o Markdown da página.
   - Não explique o processo.

## Regras críticas

- Use somente o schema real do database.
- Não invente campos.
- Preencha tudo.
- Seja direto e operacional.
- Se faltar informação, inferir de modo conservador e útil.

## Saída esperada

1. JSON de propriedades (pronto para API/MCP)
2. Markdown estruturado
