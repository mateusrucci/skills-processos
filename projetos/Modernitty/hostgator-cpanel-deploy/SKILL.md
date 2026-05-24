---
name: hostgator-cpanel-deploy
description: Padroniza deploy de sites estaticos e multiplas landings na HostGator/cPanel via GitHub Actions e cPanel API. Use quando o usuario pedir configurar, corrigir, refazer, validar ou automatizar deploy em HostGator/cPanel, especialmente com repositorio GitHub, dominio como lp.soufit.com, estrutura shared e sites por pagina, UTM central, Meta Pixel/CAPI central, .cpanel.yml, Git Version Control do cPanel, Fileman/save_file_content, CPANEL_API_TOKEN ou publicação sem clicar manualmente no cPanel.
---

# HostGator cPanel Deploy

## Objetivo

Configurar deploy recorrente de landings estaticas no HostGator/cPanel sem exigir clique manual depois do push.

Padrao esperado:
- GitHub e a fonte de verdade.
- GitHub Actions chama a API do cPanel em cada push na `main`.
- O repositorio no cPanel fica em um diretorio controlado, como `/home3/USUARIO/lp.soufit.com`.
- Os arquivos publicos finais ficam direto no dominio/subdominio, como `/home3/USUARIO/lp.soufit.com/fitmoderno/`.
- Scripts centrais ficam na raiz publica do dominio, como `/home3/USUARIO/lp.soufit.com/utm-forwarder.js`.

## Estrutura padrao

Use esta estrutura para projetos com varios sites/landings:

```txt
.
├── .cpanel.yml
├── .github/workflows/deploy.yml
├── shared/
│   ├── utm-forwarder.js
│   ├── meta-tracking.js
│   └── meta-capi.php
└── sites/
    └── fitmoderno/
        ├── index.html
        ├── cdn-cgi/
        ├── fonts.googleapis.com/
        ├── fonts.gstatic.com/
        ├── use.typekit.net/
        ├── wp-content/
        └── wp-includes/
```

Regras:
- `shared/` guarda scripts que valem para todos os sites.
- `sites/<pagina>/` guarda a landing inteira que deve ser publicada em `/<pagina>/`.
- Nao criar subpasta extra com o nome do repositorio dentro do destino publico.
- Se o usuario pedir "mandar a pasta junto", publicar em `/<pagina>/`; se pedir "direto dentro dela", publicar o conteudo no diretorio informado.

## GitHub Actions

Crie ou atualize `.github/workflows/deploy.yml`.

Modelo base:

```yaml
name: Deploy -> HostGator

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    name: cPanel Git Pull
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Pull latest code on cPanel
        env:
          CPANEL_API_TOKEN: ${{ secrets.CPANEL_API_TOKEN }}
        run: |
          curl --show-error --fail-with-body \
            -H "Authorization: cpanel CPANEL_USER:$CPANEL_API_TOKEN" \
            "https://CPANEL_HOST:2083/execute/VersionControl/update?repository_root=/home3/CPANEL_USER/DOMINIO&branch=main"

      - name: Trigger cPanel Git Deploy via API
        env:
          CPANEL_API_TOKEN: ${{ secrets.CPANEL_API_TOKEN }}
        run: |
          curl --show-error --fail-with-body \
            -H "Authorization: cpanel CPANEL_USER:$CPANEL_API_TOKEN" \
            "https://CPANEL_HOST:2083/execute/VersionControlDeployment/create?repository_root=/home3/CPANEL_USER/DOMINIO"

      - name: Publish public files directly
        env:
          CPANEL_API_TOKEN: ${{ secrets.CPANEL_API_TOKEN }}
        run: |
          publish_file() {
            local dir="$1"
            local file="$2"
            local source="$3"

            curl --show-error --fail-with-body \
              -H "Authorization: cpanel CPANEL_USER:$CPANEL_API_TOKEN" \
              --data-urlencode "dir=$dir" \
              --data-urlencode "file=$file" \
              --data-urlencode "content@$source" \
              "https://CPANEL_HOST:2083/execute/Fileman/save_file_content" >/dev/null
          }

          publish_file "/home3/CPANEL_USER/DOMINIO" "utm-forwarder.js" "shared/utm-forwarder.js"
          publish_file "/home3/CPANEL_USER/DOMINIO" "meta-tracking.js" "shared/meta-tracking.js"
          publish_file "/home3/CPANEL_USER/DOMINIO" "meta-capi.php" "shared/meta-capi.php"
          publish_file "/home3/CPANEL_USER/DOMINIO/fitmoderno" "index.html" "sites/fitmoderno/index.html"
```

Substituir:
- `CPANEL_USER`: usuario cPanel, exemplo `mate9316`.
- `CPANEL_HOST`: host cPanel, exemplo `br956.hostgator.com.br`.
- `DOMINIO`: diretorio raiz do dominio, exemplo `lp.soufit.com`.
- `fitmoderno`: slug da landing.

Use `Fileman/save_file_content` quando o Git Pull funciona, mas o `.cpanel.yml` nao copia os arquivos finais para a raiz publica esperada.

## .cpanel.yml

Mantenha `.cpanel.yml` como fallback para deploy manual pelo cPanel.

Modelo:

```yaml
---
deployment:
  tasks:
    - echo "Deploying validated package"
    - export BASEPATH=$HOME/lp.soufit.com/
    - export DEPLOYPATH=$HOME/lp.soufit.com/fitmoderno/
    - /bin/mkdir -p $BASEPATH
    - /bin/mkdir -p $DEPLOYPATH
    - /bin/rm -f $BASEPATH/index.html
    - /bin/cp shared/utm-forwarder.js $BASEPATH/utm-forwarder.js
    - /bin/cp shared/meta-tracking.js $BASEPATH/meta-tracking.js
    - /bin/cp shared/meta-capi.php $BASEPATH/meta-capi.php
    - /bin/cp -R sites/fitmoderno/index.html sites/fitmoderno/cdn-cgi sites/fitmoderno/fonts.googleapis.com sites/fitmoderno/fonts.gstatic.com sites/fitmoderno/use.typekit.net sites/fitmoderno/wp-content sites/fitmoderno/wp-includes $DEPLOYPATH
```

Nunca depender só do `.cpanel.yml` se o objetivo for deploy automatico confiavel. O workflow deve validar e publicar o essencial.

## Scripts centrais obrigatorios

Toda pagina HTML publicada no dominio deve incluir no `<head>`:

```html
<script src="/utm-forwarder.js" defer></script>
<script src="/meta-tracking.js" defer></script>
```

Se houver Meta Pixel, incluir fallback logo apos abrir `<body>`:

```html
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=PIXEL_ID&amp;ev=PageView&amp;noscript=1" alt="" /></noscript>
```

Padrao Soufit atual:
- `meta-tracking.js` dispara `PageView` no carregamento.
- Links `https://soufit.com/comprar?...` disparam `AddToCart`.
- O mesmo `eventID` deve ser usado no Pixel normal e na CAPI.
- `meta-capi.php` deve responder `GET` com `status: ok`.

## Validacao antes do push

Execute validacoes locais sempre que possivel:

```bash
node --check shared/utm-forwarder.js
node --check shared/meta-tracking.js
```

Se PHP existir localmente:

```bash
php -l shared/meta-capi.php
```

Validar referencias principais:

```bash
rg -n "utm-forwarder|meta-tracking|meta-capi|soufit.com/comprar|AddToCart" .cpanel.yml .github sites shared
```

Simular pacote quando houver reorganizacao de pastas:

```bash
node -e "const fs=require('fs'),path=require('path'),os=require('os'); const root=fs.mkdtempSync(path.join(os.tmpdir(),'deploy-')); const base=path.join(root,'lp.soufit.com'); const site=path.join(base,'fitmoderno'); fs.mkdirSync(site,{recursive:true}); for (const f of ['utm-forwarder.js','meta-tracking.js','meta-capi.php']) fs.copyFileSync(path.join('shared',f),path.join(base,f)); fs.cpSync('sites/fitmoderno',site,{recursive:true}); console.log(base)"
```

## Publicacao e verificacao

### Regra principal: deploy imediato apos qualquer alteracao

**Sempre commitar e pushar direto na `main` — sem PR intermediario.**
O push na `main` dispara o GitHub Action automaticamente.

```bash
git add <arquivos-alterados>
git commit -m "descricao curta"
git push origin main
```

Nunca usar branches ou PRs para mudancas de conteudo/deploy neste projeto.
O repositorio local deve estar sempre no branch `main`:

```bash
git checkout main
git pull origin main
# ... faz alteracoes ...
git add <arquivos>
git commit -m "descricao"
git push origin main   # deploy dispara aqui
```

### Estrutura de pastas (sem camada sites/)

O repositorio e o proprio `lp.soufit.com/` no servidor.
Landings ficam direto na raiz do repo, nao dentro de `sites/`:

```
repo/ (= lp.soufit.com/ no servidor)
├── shared/                   ← scripts centrais
├── fitmoderno/               ← landing 1
├── protocolo-magra-em-casa/  ← landing 2
├── .cpanel.yml
└── .github/workflows/deploy.yml
```

Para adicionar nova landing: criar `<slug>/` na raiz e uma linha `publish_file` no `deploy.yml`.

### Verificar apos o push

```bash
gh run list --limit 3          # confirma que o Action disparou
curl -I "https://lp.soufit.com/protocolo-magra-em-casa/?v=$(git rev-parse --short HEAD)"
curl -I "https://lp.soufit.com/fitmoderno/?v=$(git rev-parse --short HEAD)"
curl -I "https://lp.soufit.com/utm-forwarder.js?v=$(git rev-parse --short HEAD)"
```

Se Cloudflare retornar 404 cacheado, repetir com `?v=COMMIT` ou outro cache-buster.

## Diagnostico de erros comuns

`fatal: could not read Username for 'https://github.com'`:
- Repositorio privado via HTTPS sem credencial.
- Preferir deploy via GitHub Actions chamando cPanel API ou configurar SSH/deploy key corretamente.

`git@github.com: Permission denied (publickey)`:
- Deploy key nao foi adicionada no repositorio correto ou chave publica errada.
- Conferir fingerprint e usar Deploy keys do GitHub.

Action sucesso, mas arquivo publico 404:
- O cPanel fez Git Pull no diretorio do repositorio, mas nao copiou para a raiz publica.
- Adicionar etapa `Publish public files directly` com `Fileman/save_file_content`.

Pagina aparece em `/sites/<pagina>/` mas nao em `/<pagina>/`:
- Estrutura antiga com camada `sites/` — migrar para raiz do repo.
- A pasta da landing deve ficar em `<pagina>/` na raiz, nao em `sites/<pagina>/`.
- Atualizar paths no `deploy.yml` de `sites/<pagina>/index.html` para `<pagina>/index.html`.

## Regras de seguranca

- Nunca expor tokens no resumo final.
- Guardar `CPANEL_API_TOKEN` em GitHub Secrets.
- Para Meta CAPI, preferir variavel/secret fora do repo quando o ambiente permitir. Se o projeto privado exigir token no PHP para funcionar no HostGator, nao repetir o valor no final.
- Antes de remover arquivos publicos, confirmar o path absoluto para evitar apagar diretorio errado.
- Nao usar `git reset --hard` ou delecoes destrutivas sem pedido explicito.
