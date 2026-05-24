# Regras de Redação — blog-writer

Regras de escrita para posts de blog otimizados para humanos, Google Search,
AI Overviews e busca com IA (Claude, ChatGPT). Baseado nas diretrizes do Google
Search Central (E-E-A-T, conteúdo people-first) e nas boas práticas de SEO para IA.

---

## 1. Princípio Central: People-First

O Google avalia se o conteúdo foi criado para satisfazer o usuário ou para manipular
algoritmos. A pergunta que deve guiar cada parágrafo:

> **"Esse parágrafo resolve uma dúvida real do ICP ou só existe para encher página?"**

Se a resposta for "encher página" — delete.

Teste de qualidade do Google:
- O leitor sai do post sentindo que aprendeu algo útil?
- Ele precisaria pesquisar novamente para complementar o que leu?
- O post tem informação que vai além do óbvio para quem já conhece o tema superficialmente?

---

## 2. Tom de Voz

**Sempre leia o perfil do cliente antes de escrever.**
O tom está em `references/clients/{slug}.md`.

### Princípios gerais (para qualquer blog)

- Escreva para um adulto inteligente que não tem tempo a perder
- Direto ao ponto — sem rodeios, sem "Neste artigo iremos explorar..."
- Especificidade > generalidade: "R$ 8.000/mês de verba" > "verbas altas"
- Ativo > passivo: "O gestor cometeu um erro" > "Um erro foi cometido"
- Concreto > abstrato: "3 de cada 5 campanhas falham na fase de testes" > "muitas campanhas falham"

### Proibido em qualquer blog

| Expressão | Substitua por |
|---|---|
| "No mundo atual..." | Vai direto ao ponto |
| "É de extrema importância..." | "É fundamental..." ou reestruture |
| "Como todos sabemos..." | Delete — se todos sabem, não precisa dizer |
| "Neste artigo, vamos explorar..." | Intro direta ao problema |
| "Mindset", "jornada", "propósito" como tema | Termos concretos do nicho |
| "Clique aqui" | Texto âncora descritivo |
| "E muito mais!" | Liste ou delete |
| Adjetivos vagos: "incrível", "revolucionário" | Dado concreto que prove |

---

## 3. Estrutura de Parágrafos

### Regra dos 4×4
- Máximo **4 linhas** por parágrafo (no editor, não no browser)
- Máximo **4 palavras técnicas** por parágrafo sem explicação
- Máximo **4 itens** em uma lista sem quebrar em seções

### Primeiro parágrafo de cada H2: o snapshot
O Google e as IAs usam o primeiro parágrafo após cada heading para gerar snippets.
Esse parágrafo deve:
1. Responder a pergunta do heading diretamente
2. Funcionar sozinho, sem contexto do resto do post
3. Ser 2–4 frases, máximo 80 palavras

**Exemplo ruim:**
> H2: Como estruturar um time de tráfego pago
> Primeiro parágrafo: "Antes de falar sobre estruturação, é importante entender
> o contexto em que as empresas brasileiras operam e os desafios únicos que enfrentam..."

**Exemplo bom:**
> H2: Como estruturar um time de tráfego pago
> Primeiro parágrafo: "Um time de tráfego funcional precisa de três papéis mínimos:
> estrategista, operador e analista de dados. Em empresas com verba abaixo de R$ 30k/mês,
> um único gestor sênior pode acumular os três — acima disso, a divisão se torna necessária."

---

## 4. Introdução

A introdução tem um único objetivo: confirmar para o leitor que ele está no lugar certo
e que vale continuar lendo.

### Estrutura em 3 partes (máx 150 palavras total)

**Parte 1 — Problema/Situação** (1–2 frases)
Descreve a dor ou o contexto do ICP. Específico, não genérico.

**Parte 2 — Por que é difícil / O erro comum** (1–2 frases)
O que a maioria faz de errado ou por que o problema persiste.

**Parte 3 — Promessa do post** (1–2 frases)
O que o leitor vai ter ao final. Não "vamos ver", mas "você vai saber".

**Exemplo:**
> Verba de R$ 15k/mês no Meta e resultado piorando mês a mês. É o cenário de 60%
> dos empresários que chegam até nós para diagnóstico. O problema raramente é o
> gestor — quase sempre é a estrutura de campanha.
>
> Neste post, você vai ver exatamente como auditamos campanhas em 47 projetos e
> o padrão de erro que aparece em 80% dos casos.

---

## 5. Densidade de Keyword

### Regra geral
- **Keyword principal:** aparece naturalmente, sem forçar. Referência: 1–2% do texto total
- Não existe "densidade ideal" oficial no Google — o que existe é uso natural vs stuffing
- Se soar estranho em voz alta, está forçado — reescreva

### Distribuição no post
| Onde | Regra |
|---|---|
| `<title>` e H1 | Obrigatório — o mais à esquerda possível |
| Primeiro parágrafo | Obrigatório — nos primeiros 100 words |
| H2s | Pelo menos 2 dos H2s devem conter keyword ou variação |
| Meta description | Obrigatório |
| Alt text de imagem principal | Recomendado |
| Conclusão | Recomendado — uma vez, natural |

### Keywords secundárias
Distribuídas nos H2/H3 e corpo. Uma por seção, naturalizada.
Se não couber sem forçar — não coloca.

---

## 6. E-E-A-T na Redação

### Experiência — mostrar vivência real
- Usar dados proprietários: "em 47 projetos que analisamos..."
- Casos reais (anonimizados): "um cliente do setor de saúde com verba de R$ 12k/mês..."
- Erros que o autor já cometeu ou viu acontecer: "a armadilha que cometemos em 2021..."

### Especialidade — demonstrar profundidade
- Explicar o "por quê" por trás do "o quê"
- Trazer nuances que contradizem o senso comum
- Referenciar conceitos técnicos corretamente (com link para fonte quando necessário)

### Autoridade — construir referência
- Linkar para conteúdos internos relacionados (links internos)
- Citar fontes externas de qualidade quando trouxer dado externo
- Bio do autor no final do post (indicar com `[BIO DO AUTOR]` — o template vai preencher)

### Confiança — ser preciso e transparente
- Nunca inventar estatísticas — se não tem fonte, não usa
- Indicar quando é opinião vs dado: "na minha experiência..." vs "segundo o relatório X..."
- Sem promessas exageradas que o post não cumpre
- Datas dos dados citados — dado de 2019 sobre mercado de IA já não serve

---

## 7. Links

### Links internos
- Inserir onde existe conteúdo relacionado no blog (ou que vai existir)
- Formato no HTML: `<a href="/blog/{slug}">{texto âncora descritivo}</a>`
- Formato quando o post ainda não existe: `[LINK INTERNO: {tema do post relacionado}]`
- Mínimo 2 links internos por post — ajuda crawler e distribui autoridade

### Links externos
- Apenas para fontes de qualidade: estudos, relatórios oficiais, dados de mercado
- Sempre com `rel="noopener" target="_blank"`
- Nunca inventar URL — se não tem a fonte exata, indique `[FONTE: {descrição}]` para pesquisar depois
- Não linkar para concorrentes diretos

---

## 8. Imagens

O blog-writer não gera imagens — indica onde devem ir e o que devem mostrar.

### Formato de indicação
```
[IMAGEM: {descrição objetiva do que a imagem deve mostrar}]
[ALT: {texto alt otimizado — descritivo, sem keyword stuffing}]
[POSIÇÃO: após o parágrafo X da seção Y]
```

### Regras de alt text (Google Search Central)
- Descrever o que a imagem mostra, não "palavra-chave aqui"
- Máximo 125 caracteres
- Não começar com "Imagem de..." ou "Foto de..."
- Se for gráfico/tabela: descrever o dado principal que ele mostra

### Formatos recomendados para publicação
- WebP para fotografias e ilustrações (melhor compressão, suportado pelo Google)
- SVG para ícones e gráficos simples
- PNG para screenshots onde clareza é crítica
- Indicar o formato preferido no placeholder

---

## 9. Listas e Tabelas

### Quando usar listas
- Quando os itens são genuinamente paralelos e enumeráveis
- Quando o leitor vai querer escanear (checklist, passos, critérios)
- Máximo 7 itens numa lista sem sub-seções

### Quando NÃO usar listas
- Para quebrar um parágrafo que poderia ser prosa fluida
- Para parecer "mais organizado" sem necessidade real
- Quando os itens têm tamanhos muito diferentes (>3x de variação)

### Tabelas
- Usar quando há comparação real entre 2+ opções em 2+ critérios
- Sempre com `<thead>` e `<tbody>` semânticos
- Caption descritivo: `<caption>{O que a tabela mostra}</caption>`
- Não usar tabela para layout — apenas para dados tabulares

---

## 10. Conclusão e CTA

### Estrutura da conclusão (máx 120 palavras)

**Parte 1 — Síntese** (2–3 frases)
Resume o argumento central, não todos os pontos. O leitor já leu o post.

**Parte 2 — Próximo passo** (1–2 frases)
O que o leitor deve fazer com o que aprendeu. Concreto.

**Parte 3 — CTA** (1 frase + botão/link)
Alinhado com o CTA padrão do perfil do cliente.

### Regras do CTA
- Um único CTA por post — dois CTAs competem entre si e reduzem conversão
- Texto do CTA: verbo + benefício ("Fazer diagnóstico gratuito", não "Clique aqui")
- Posição: sempre na conclusão, nunca no meio do post
- Formato HTML: `<a href="{URL}" class="cta-button">{Texto do CTA}</a>`
