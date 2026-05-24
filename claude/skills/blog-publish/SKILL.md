---
name: blog-publish
description: Publica posts de blog aprovados no repositorio do site, atualiza o indice do blog, valida SEO tecnico basico e prepara o deploy. Use SEMPRE que o usuario pedir "publicar post", "subir artigo", "colocar no blog", "fazer deploy do post", "atualizar o indice do blog", "publicar no site", ou quando um post vier aprovado pela skill blog-review. Nunca publica post reprovado ou sem HTML revisado.
---

# blog-publish

Skill de publicacao de posts aprovados no blog do site Mateus Rucci.

Ela recebe um HTML aprovado pela `blog-review`, copia/adapta o arquivo para o projeto real,
atualiza a listagem do blog e valida se o post esta tecnicamente publicavel.

## Premissas

- Repositorio principal: `/Users/mateusrucci/Desktop/meus-scripts-apps-script/Site Mateus`
- Pasta publica do blog: `blog/`
- Arquivo fisico do post: `blog/{slug}/index.html`
- URL publica final do post: `https://mateusrucci.com.br/blog/{slug}/`
- Indice do blog: `blog/index.html`
- CSS compartilhado do blog: `blog/assets/blog.css`
- Deploy cPanel: `.cpanel.yml`

## Pre-requisitos bloqueantes

Antes de publicar, verifique:

1. Existe um HTML do post vindo de `blog-writer`.
2. Existe review da `blog-review`.
3. O review esta `APROVADO` com score >= 90.
4. Nao existe problema critico pendente.
5. O slug final esta aprovado.

Se qualquer item faltar, pare e diga exatamente o que falta.

Nunca publique post reprovado. Nunca contorne o review.

## Workflow

### Passo 1 - Identificar fonte e destino

Aceite uma destas fontes:

- Caminho do HTML aprovado, normalmente `~/blog-writer/{blog}/{post}/index.html`
- HTML colado no chat
- Arquivo local indicado pelo usuario

Confirme o repositorio Git antes de publicar:

```bash
git rev-parse --show-toplevel
```

O retorno deve ser:

```text
/Users/mateusrucci/Desktop/meus-scripts-apps-script/Site Mateus
```

Se o retorno for diferente, pare. Nao publique em outro repositorio.

Defina o destino:

```text
/Users/mateusrucci/Desktop/meus-scripts-apps-script/Site Mateus/blog/{slug}/index.html
```

Defina a URL publica:

```text
https://mateusrucci.com.br/blog/{slug}/
```

Regra: a URL publica, canonical, breadcrumbs, links internos, Open Graph e sitemap
NUNCA devem terminar em `index.html`. `index.html` e apenas o arquivo fisico usado
pelo hosting estatico.

Regra de fluxo: o HTML aprovado pode existir primeiro como artefato local em
`~/blog-writer/{blog}/{post}/index.html`. A publicacao so acontece quando esse HTML
e copiado para dentro do repositorio Git em `blog/{slug}/index.html`.

Se `blog/{slug}/` ja existir, compare antes de sobrescrever. Se houver diferenca
substantiva e o usuario nao pediu substituicao, pergunte antes.

### Passo 2 - Validar o HTML antes de mover

Cheque no HTML:

- `<!DOCTYPE html>`
- `<html lang="pt-BR">`
- `<title>` presente
- `<meta name="description">` presente
- `<meta name="robots" content="index, follow...">` ou ausencia de `noindex`
- `<link rel="canonical" href="https://mateusrucci.com.br/blog/{slug}/">`
- nenhuma URL publica contendo `/index.html`
- exatamente um `<h1>`
- `<article>` presente
- JSON-LD `Article` presente
- JSON-LD `BreadcrumbList` presente
- conteudo principal em HTML estatico, nao dependente de JS
- links internos com URLs validas
- links externos com `rel="noopener"` quando `target="_blank"`

Se o HTML tiver `noindex`, canonical errado, URL publica com `/index.html`, H1
duplicado, JSON-LD Article ausente, ou slug/canonical divergente, pare e devolva
para correcao.

### Passo 3 - Publicar arquivo no projeto

Crie a pasta `blog/{slug}/` se necessario.

Salve o HTML como:

```text
blog/{slug}/index.html
```

Depois de salvar, confirme que o arquivo existe dentro do repositorio Git:

```bash
git status --short -- blog/{slug}/index.html blog/index.html .cpanel.yml
```

Se o arquivo nao aparecer como novo/modificado quando esperado, investigue antes de
responder que publicou.

Preserve o padrao visual existente do blog sempre que possivel:

- reuse `blog/assets/blog.css`
- mantenha navegacao semelhante a posts existentes
- mantenha CTA para `/diagnostico-personalizado/`
- mantenha URLs absolutas canonicas em `https://mateusrucci.com.br/blog/{slug}/`
- nunca use `https://mateusrucci.com.br/blog/{slug}/index.html` em links, canonical,
  Open Graph, JSON-LD ou sitemap

### Passo 4 - Atualizar o indice do blog

Atualize `blog/index.html` para incluir o novo post nas secoes existentes.

Regras:

- O post novo deve aparecer como card/list item clicavel.
- O link do card deve apontar para `/blog/{slug}/`, nunca para `/blog/{slug}/index.html`.
- Use o mesmo padrao HTML visual dos posts ja existentes.
- Titulo, resumo, data, categoria e tempo de leitura devem bater com o HTML do post.
- Nao remova posts antigos.
- Nao quebre links existentes.

Se a estrutura do indice estiver muito manual ou ambigua, faca a menor alteracao segura.

### Passo 5 - Validar deploy cPanel

Abra `.cpanel.yml` e confirme que a pasta `blog/` e copiada para o deploy.

Se nao existir uma linha equivalente a:

```yaml
- /bin/cp -rf blog/ $DEPLOYPATH
```

adicione-a no bloco `deployment.tasks`, mantendo o estilo do arquivo.

### Passo 6 - Checar arquivos auxiliares

Se existirem, atualize:

- `sitemap.xml`: adicionar URL do post
- `robots.txt`: garantir que nao bloqueia `/blog/`, `Googlebot` e `OAI-SearchBot`
- RSS/feed: adicionar item do post

Se nao existirem, nao crie automaticamente, a menos que o usuario peca.

### Passo 7 - Verificacao final

Execute checagens locais possiveis:

- `git rev-parse --show-toplevel`
- `git diff --stat`
- `git status --short -- blog/{slug}/index.html blog/index.html .cpanel.yml`
- busca por `noindex` no post
- busca por canonical incorreto
- busca por `/index.html` em URLs publicas do post e do indice
- validacao simples de quantidade de H1
- verificacao de links internos obvios no HTML

Se houver ambiente/servidor local disponivel, recomende abrir no navegador para QA visual.

## Saida obrigatoria

Ao concluir, responda com:

```text
Post publicado localmente.

Arquivo fisico: blog/{slug}/index.html
URL publica: https://mateusrucci.com.br/blog/{slug}/
Indice atualizado: sim/nao
Deploy cPanel atualizado: sim/nao
Validacoes: {resumo curto}

Proximo passo: revisar visualmente e fazer commit/deploy.
```

Se algo bloquear:

```text
Publicacao bloqueada.
Motivo: {motivo especifico}
Arquivo afetado: {caminho, se houver}
Acao necessaria: {proximo passo}
```

## Regras inviolaveis

1. Nao publicar post sem review aprovado.
2. Nao publicar HTML com `noindex` acidental.
3. Nao publicar canonical que nao bate com o slug final.
4. Nao publicar URL publica, canonical, JSON-LD, Open Graph, sitemap ou link interno com `index.html`.
5. Nao remover posts existentes do indice.
6. Nao inventar data, autor, fonte ou URL externa.
7. Nao alterar arquivos fora do escopo do blog/deploy sem permissao.
8. Nao fazer commit, push ou deploy remoto sem pedido explicito do usuario.

## Criterios de SEO e IA aplicados

- Conteudo central em HTML estatico.
- Headings claros e hierarquicos.
- URL publica, limpa e permanente.
- JSON-LD coerente com o conteudo visivel.
- Breadcrumb navegacional e estruturado.
- Snippet elegivel, sem `noindex`/`nosnippet` acidental.
- Crawl liberado quando houver `robots.txt`, incluindo Googlebot e OAI-SearchBot.
- Links internos para descoberta de paginas profundas.
