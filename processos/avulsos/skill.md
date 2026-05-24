---
name: soufit-deploy
description: >
  Gerencia o repositório GitHub mateusrucci/soufit e o deploy no cPanel HostGator para o domínio lp.soufit.com.
  Use esta skill SEMPRE que o usuário mencionar: criar landing page nova, adicionar página ao soufit, fazer deploy,
  subir para o cPanel, verificar status do deploy, commit no repositório soufit, nova LP no lp.soufit.com,
  "quero criar uma página para X no soufit", "como adiciono uma LP", "sobe para o ar", "publica a página".
  Também use quando o usuário editar arquivos dentro de /Users/mateusrucci/Desktop/meus-scripts-apps-script/Modernitty/lp.soufit.com/
  e quiser publicar as mudanças.
---

# Skill: soufit-deploy

Você gerencia o repositório e o pipeline de deploy do domínio lp.soufit.com.

## Contexto do projeto

| Item | Valor |
|------|-------|
| Repo local | `/Users/mateusrucci/Desktop/meus-scripts-apps-script/Modernitty/lp.soufit.com/` |
| GitHub | `mateusrucci/soufit` (branch `main`) |
| Domínio | `lp.soufit.com` |
| Hosting | HostGator cPanel — `br956.hostgator.com.br:2083`, usuário `mate9316` |
| Caminho no servidor | `/home3/mate9316/lp.soufit.com/` |
| Deploy trigger | Push para `main` → GitHub Actions → cPanel VersionControl + Fileman API |

## Estrutura do repositório

```
lp.soufit.com/  (raiz do repo)
├── fitmoderno/                  → lp.soufit.com/fitmoderno
├── protocolo-magra-em-casa/     → lp.soufit.com/protocolo-magra-em-casa
├── protocolo-magra-em-casa-obg/ → lp.soufit.com/protocolo-magra-em-casa-obg
├── shared/                      → scripts publicados na raiz do domínio
│   ├── ac-form.js
│   ├── ac-submit.php
│   ├── meta-capi.php
│   ├── meta-tracking.js
│   ├── utm-forwarder.js
│   ├── robots.txt
│   └── root.htaccess
├── .cpanel.yml                  → tarefas de cópia executadas pelo cPanel
└── .github/workflows/deploy.yml → pipeline de CI/CD
```

**Regra fundamental:** cada nova página vira uma pasta na raiz do repo. A URL final é `lp.soufit.com/<nome-da-pasta>`.

---

## Fluxo de deploy

1. `git push origin main` dispara o workflow `Deploy -> HostGator`
2. O workflow valida os assets, aciona o Git Pull do cPanel e publica os arquivos via Fileman API
3. O `.cpanel.yml` copia os arquivos `shared/` para a raiz do domínio e os uploads de mídia para os subdiretórios corretos
4. O deploy leva ~25 segundos e você pode verificar o resultado com `gh run list --repo mateusrucci/soufit --limit 1`

---

## Operações disponíveis

### 1. Criar nova landing page

Quando o usuário quiser uma nova página em `lp.soufit.com/<slug>`:

**Passo 1 — Criar a estrutura:**
```
lp.soufit.com/
└── <slug>/
    └── index.html   ← conteúdo da página
```

Se a página tiver imagens ou mídia, coloque em `<slug>/assets/` ou `<slug>/wp-content/uploads/`.

**Passo 2 — Adicionar ao `deploy.yml`:**
Adicione uma linha `publish_file` ao step "Publish shared + entry HTML files":
```yaml
publish_file "/home3/mate9316/lp.soufit.com/<slug>" "index.html" "<slug>/index.html"
```

**Passo 3 — Validação no `deploy.yml` (opcional):**
Se a página tiver assets críticos, adicione ao step de validação:
```bash
test -f <slug>/index.html
```

**Passo 4 — Commit e push:**
```bash
git add <slug>/ .github/workflows/deploy.yml
git commit -m "feat: add landing page <slug>"
git push origin main
```

**Passo 5 — Confirmar deploy:**
```bash
gh run list --repo mateusrucci/soufit --limit 1
```
Aguarde status `completed / success`.

---

### 2. Publicar mudanças em página existente

Quando o usuário editar uma página e quiser publicar:

```bash
cd /Users/mateusrucci/Desktop/meus-scripts-apps-script/Modernitty/lp.soufit.com
git add <arquivos-modificados>
git commit -m "<descrição da mudança>"
git push origin main
```

Depois confirme:
```bash
gh run list --repo mateusrucci/soufit --limit 1
```

---

### 3. Verificar status do deploy

```bash
gh run list --repo mateusrucci/soufit --limit 5
```

Para ver detalhes de um run específico:
```bash
gh run view <run-id> --repo mateusrucci/soufit --log
```

Se o deploy falhar, verifique:
- Se `protocolo-magra-em-casa/index.html` existe (validação obrigatória no workflow)
- Se `protocolo-magra-em-casa/wp-content/uploads/` existe
- Se os caminhos no `deploy.yml` e `.cpanel.yml` estão corretos (sem prefixo `lp.soufit.com/`)

---

### 4. Atualizar scripts compartilhados (`shared/`)

Os arquivos em `shared/` são publicados na raiz do domínio (`lp.soufit.com/`). Para atualizar:

```bash
# edite shared/<arquivo>
git add shared/
git commit -m "fix: atualiza <arquivo> em shared"
git push origin main
```

---

### 5. Forçar re-deploy sem mudanças de código

Use o workflow_dispatch do GitHub Actions:
```bash
gh workflow run deploy.yml --repo mateusrucci/soufit --ref main
```

---

## Arquivos críticos para editar com cuidado

| Arquivo | O que faz |
|---------|-----------|
| `.cpanel.yml` | Copia arquivos no servidor após o git pull. Caminhos são relativos à raiz do repo. |
| `.github/workflows/deploy.yml` | Valida assets, aciona o cPanel e publica via Fileman API. Caminhos também relativos à raiz. |
| `shared/root.htaccess` | Configuração do servidor para o domínio raiz. |
| `shared/meta-capi.php` | Integração com Facebook Conversions API. |
| `shared/ac-submit.php` | Handler de formulários para ActiveCampaign. |

**Atenção:** nunca adicione prefixo `lp.soufit.com/` nos caminhos do `.cpanel.yml` ou `deploy.yml` — as páginas agora ficam diretamente na raiz do repo.

---

## Convenções de nomenclatura

- Slugs de página: `kebab-case` (ex: `nova-oferta`, `webinar-gratuito`)
- Commits: use prefixo semântico — `feat:` para nova página, `fix:` para correção, `refactor:` para reorganização
- Páginas de obrigado/confirmação: use sufixo `-obg` (ex: `nova-oferta-obg`)