---
name: blog-orchestrator
description: Orquestra o fluxo completo de producao do blog, coordenando blog-research, blog-brief, blog-writer, blog-review e blog-publish. Use SEMPRE que o usuario pedir "criar um post completo", "automatizar o blog", "rodar o fluxo do blog", "produzir artigo do zero", "pipeline de blog", "calendario editorial ate publicacao", ou quando quiser transformar uma pauta em post publicado. Mantem checkpoints humanos antes de brief final, escrita, publicacao e deploy.
---

# blog-orchestrator

Skill de orquestracao do sistema de blog. Ela nao substitui as skills especializadas;
ela define a ordem correta, os checkpoints e os caminhos de arquivos para evitar
conteudo generico, publicacao errada ou deploy prematuro.

## Arquitetura

Fluxo padrao:

```text
blog-research -> blog-brief -> aprovacao humana -> blog-writer -> blog-review -> aprovacao humana -> blog-publish -> commit/deploy sob pedido explicito
```

Skills envolvidas:

- `blog-research`: descobre pautas com sinais de demanda, SEO e E-E-A-T.
- `blog-brief`: cria o brief estruturado e aguarda aprovacao.
- `blog-writer`: escreve HTML completo apenas com brief aprovado.
- `blog-review`: aprova/reprova com score minimo 90.
- `blog-publish`: publica no repositorio real apenas se o review estiver aprovado.

## Caminhos oficiais

Repositorio Git real:

```text
/Users/mateusrucci/Desktop/meus-scripts-apps-script/Site Mateus
```

Artefatos locais de trabalho fora do repo:

```text
~/blog-research/{blog}/{timestamp}/raw.json
~/blog-brief/{blog}/{post}/brief.md
~/blog-writer/{blog}/{post}/index.html
```

Publicacao final dentro do repo:

```text
/Users/mateusrucci/Desktop/meus-scripts-apps-script/Site Mateus/blog/{slug}/index.html
```

URL publica final:

```text
https://mateusrucci.com.br/blog/{slug}/
```

Regra: a URL publica nunca termina com `index.html`. O `index.html` existe apenas
como arquivo fisico para o servidor.

## Modos de uso

### Modo 1 - Pesquisa ate pauta

Use quando o usuario pedir temas, calendario editorial, keywords ou "o que escrever".

1. Acione `blog-research`.
2. Use perfil do blog `rucci`.
3. Priorize pautas com dado/caso/experiencia real.
4. Entregue lista priorizada.
5. Pare e aguarde o usuario escolher a pauta.

Nao gere brief sem pauta escolhida.

### Modo 2 - Pauta ate brief

Use quando o usuario ja escolheu uma pauta.

1. Acione `blog-brief`.
2. Inclua keyword, intencao, angulo, anchor de credibilidade, estrutura H2/H3, CTA e schemas.
3. Mostre o brief ao usuario.
4. Pare e aguarde aprovacao explicita.

Nao salve nem escreva o post antes de aprovacao.

### Modo 3 - Brief aprovado ate HTML

Use quando o usuario disser "aprovado", "pode escrever" ou indicar um brief aprovado.

1. Confirme que existe brief aprovado em `~/blog-brief/{blog}/{post}/brief.md` ou no chat.
2. Acione `blog-writer`.
3. Salve o HTML em `~/blog-writer/{blog}/{post}/index.html`.
4. Nao publique no repo ainda.
5. Passe para `blog-review`.

### Modo 4 - Review ate publicacao local

Use quando houver HTML pronto.

1. Acione `blog-review`.
2. Se score < 90 ou houver problema critico, pare e devolva para correcao.
3. Se score >= 90 e status aprovado, peça autorizacao para publicar localmente no repo, a menos que o usuario ja tenha pedido publicacao.
4. Acione `blog-publish`.
5. Publique no repo Git em `blog/{slug}/index.html`.
6. Atualize `blog/index.html`.
7. Garanta que `.cpanel.yml` inclua `blog/`.

### Modo 5 - Commit/deploy

So execute se o usuario pedir explicitamente commit, push ou deploy.

1. Rode `git diff --stat`.
2. Mostre escopo.
3. Nao inclua arquivos nao relacionados.
4. Faça commit com mensagem clara se solicitado.
5. Push/deploy somente se solicitado.

## Regras de decisao

- Se o usuario pedir "fazer tudo", ainda mantenha checkpoints de aprovacao de brief e review.
- Se o usuario trouxer um tema direto, pule `blog-research` se a pauta tiver keyword, publico, angulo e anchor de credibilidade.
- Se faltar anchor de credibilidade, pare e peça dado, caso ou experiencia real.
- Se faltar fonte para afirmacao factual forte, use pesquisa web ou marque como lacuna.
- Se o post for do Mateus Rucci, use o perfil em `clients/mateus-rucci/perfil.md` quando estiver no repo, alem das referencias internas das skills.
- Use o banco `clients/mateus-rucci/conteudos-transcritos.md` como mapa rapido de temas proprietarios quando estiver disponivel.

## Checkpoints obrigatorios

1. Aprovacao de pauta: antes do brief, quando vier de pesquisa.
2. Aprovacao de brief: antes de escrever.
3. Review >= 90: antes de publicar no repo.
4. Confirmacao de publicacao: antes de copiar para `blog/{slug}/index.html`, salvo se o usuario ja pediu "publique".
5. Pedido explicito de Git: antes de commit, push ou deploy.

## Qualidade minima

O post final deve ter:

- Conteudo central em HTML estatico.
- Canonical sem `index.html`.
- Links internos sem `index.html`.
- JSON-LD Article e BreadcrumbList.
- H1 unico.
- Meta description dentro do limite aprovado.
- CTA unico para diagnostico/auditoria.
- Pelo menos uma anchor real de credibilidade.
- Nenhum dado inventado.

## Saida recomendada por etapa

Ao trocar de etapa, informe:

```text
Etapa concluida: {research|brief|writer|review|publish}
Artefato: {caminho ou resumo}
Status: {aguardando aprovacao|aprovado|bloqueado|publicado localmente}
Proximo passo: {acao objetiva}
```

## Regras inviolaveis

1. Nao pular aprovacao de brief.
2. Nao escrever sem brief aprovado.
3. Nao publicar sem review aprovado.
4. Nao usar URL publica com `index.html`.
5. Nao fazer commit, push ou deploy remoto sem pedido explicito.
6. Nao publicar conteudo importante dependente de JavaScript.
7. Nao inventar dados, fontes, cases ou resultados.
