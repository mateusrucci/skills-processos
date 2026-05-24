---
name: code-deploy-skill
description: Padroniza respostas de deploy e manutenção para VPS com comandos compactos, sempre especificando onde rodar cada bloco e preferindo SCP/RSYNC/SSH com senha embutida via scripts expect.
---

# Chatwoot Password Deploy

Use esta habilidade quando o usuário pedir deploy, manutenção, sincronização de arquivos, rebuild de containers, correção em VPS, ou qualquer operação parecida em projetos como Chatwoot.

## Objetivo

Responder no formato mais operacional possível:
- sempre separar claramente `No seu computador` e `Na VPS`
- preferir **o menor número possível de envios**
- preferir comandos com **senha já embutida**
- quando não der para embutir a senha, mostrar a senha **logo abaixo do comando**

## Formato obrigatório da resposta

Sempre responder em blocos curtos neste formato:

No seu computador:

```bash
comando-aqui
```

Senha:

```text
senha-aqui
```

Na VPS:

```bash
comando-aqui
```

Se a senha já estiver embutida no comando via script `expect`, não repetir a senha abaixo.

## Preferência de ferramentas

Quando houver vários arquivos ou pastas para enviar, priorize:

1. `./scripts/rsync_with_password.expect`
2. `./scripts/scp_with_password.expect`
3. `./scripts/ssh_with_password.expect`

Use `rsync` para economizar envios separados. Junte múltiplos caminhos no mesmo comando sempre que for seguro.

## Scripts padrão

### Upload com `rsync`

```bash
./scripts/rsync_with_password.expect 'SENHA' -av app/ ops/ root@HOST:/opt/chatwoot/
```

### Upload com `scp`

```bash
./scripts/scp_with_password.expect 'SENHA' arquivo1 arquivo2 root@HOST:/destino/
```

### Execução remota com `ssh`

```bash
./scripts/ssh_with_password.expect root@HOST 'SENHA' "cd /opt/chatwoot && ./ops/scripts/chatwoot-compose.sh build rails sidekiq && ./ops/scripts/chatwoot-compose.sh up -d rails sidekiq"
```

## Regras de compactação

- Prefira **um comando de upload** e **um comando remoto**.
- Encadeie passos remotos com `&&` quando isso reduzir idas e vindas sem esconder risco.
- Só quebre em mais de um bloco quando:
  - houver risco de perder estado importante
  - o usuário precise validar algo entre etapas
  - o comando ficar difícil demais de auditar

## Regras de segurança operacional

- Nunca use `rm`, `git reset --hard` ou reversões destrutivas sem pedido explícito.
- Ao sincronizar projeto, prefira **não sobrescrever `.env`** automaticamente, a menos que o usuário peça.
- Se um arquivo sensível precisar ser alterado, diga explicitamente.

## Regra especial deste usuário

Este usuário prefere respostas diretas e operacionais. Evite prose longa. O padrão ideal é:

- onde rodar
- comando pronto
- senha no próprio comando se possível
- senha logo abaixo se não for possível

## Exemplos de resposta

### Bom

No seu computador:
```bash
./scripts/rsync_with_password.expect 'minha-senha' -av app/ ops/ root@31.97.171.134:/opt/chatwoot/
```

Na VPS:
```bash
cd /opt/chatwoot && ./ops/scripts/chatwoot-compose.sh build rails sidekiq && ./ops/scripts/chatwoot-compose.sh up -d rails sidekiq
```

### Ruim

- separar upload de cada arquivo em vários `scp`
- esquecer de dizer onde rodar
- mandar a senha apenas em texto solto sem ligar ao comando
- mandar explicação longa antes do comando
