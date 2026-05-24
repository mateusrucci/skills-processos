---
name: code-deploy-skill
description: Padroniza respostas de deploy e manutenção para VPS com comandos compactos, sempre especificando onde rodar cada bloco e preferindo SCP/RSYNC/SSH com senha embutida via scripts expect.
---

# Password Deploy

Use esta habilidade quando o usuário pedir deploy, manutenção, sincronização de arquivos, rebuild de containers, correção em VPS, ou qualquer operação parecida em projetos como Chatwoot, Typebot, Cal.com, Formbricks, N8N e serviços Docker atrás de proxy reverso.

## Objetivo

Responder no formato mais operacional possível:
- sempre separar claramente `No seu computador` e `Na VPS`
- preferir **o menor número possível de envios**
- preferir comandos com **senha já embutida**
- quando não der para embutir a senha, mostrar a senha **logo abaixo do comando**
- adaptar os comandos ao que já existe na VPS, em vez de assumir uma stack nova
- quando um passo for condicional para o próximo, mandar só esse passo e esperar o retorno
- pedir sempre o output/logs do comando executado quando a continuação depender dele
- por padrão, preparar e revisar arquivos localmente antes de enviar para a VPS

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

## Regra de sequência

Se o próximo comando depender do resultado do anterior:
- mandar **apenas um passo**
- pedir explicitamente para o usuário colar o retorno completo
- não adiantar os próximos passos

Exemplos de casos condicionais:
- descoberta de rede Docker
- descoberta de path real do compose
- inspeção de logs
- confirmação de erro de build
- leitura de `.env` ou segredos existentes

Se os passos **não** forem condicionais:
- mandar o máximo possível em um único bloco
- só quebrar em vários blocos quando isso melhorar auditoria, segurança ou chance de sucesso

## Preferência de ferramentas

Quando houver vários arquivos ou pastas para enviar, priorize:

1. `./scripts/rsync_with_password.expect`
2. `./scripts/scp_with_password.expect`
3. `./scripts/ssh_with_password.expect`
4. `ssh`, `scp` e `rsync` nativos quando os scripts `expect` não existirem no diretório atual

Use `rsync` para economizar envios separados. Junte múltiplos caminhos no mesmo comando sempre que for seguro.

## Fallback obrigatório

Se o usuário estiver em um diretório sem `./scripts/*_with_password.expect`, não insistir nesses comandos.

Nesse caso:
- usar `ssh root@HOST`
- mostrar a senha logo abaixo
- preferir blocos curtos para colar já dentro da VPS
- evitar comandos gigantes de uma linha quando houver senha com aspas, heredoc ou muitas expansões

## Descoberta obrigatória antes do deploy

Antes de montar comandos finais de deploy em uma VPS já usada, levantar o ambiente primeiro.

Checklist mínimo:
- sistema operacional e recursos
- versão do Docker e Compose
- containers ativos
- portas publicadas
- redes Docker existentes
- arquivos `docker-compose*.yml` em `/opt`
- arquivos `.env*` relevantes em `/opt`
- existência de proxy reverso já ativo
- hostname e DNS do domínio alvo

Se o usuário ainda não enviou isso, primeiro responder com comandos de diagnóstico e um checklist do que ele precisa colar de volta.

Ao pedir qualquer diagnóstico:
- sempre pedir o retorno completo
- sempre pedir logs/saída do comando executado
- só prosseguir depois de receber esse retorno

## Regra especial para esta VPS do usuário

Com base no ambiente já observado desta VPS:
- existe um Traefik já publicado nas portas `80` e `443` no container `n8n-traefik-1`
- não existe uma rede Docker chamada `traefik` por padrão
- já existem stacks em `/opt` como `chatwoot`, `calcom`, `formbricks`, `n8n` e outras
- o domínio pode já resolver para a VPS antes do deploy

Portanto:
- não assumir Caddy por padrão
- preferir integrar novos serviços ao proxy já existente quando fizer sentido
- antes de usar `traefik.docker.network`, confirmar o nome real da rede externa
- se a rede externa não existir, orientar a descobrir onde está o compose do Traefik antes de prosseguir
- evitar publicar novas portas `80` e `443`
- evitar instalar pacotes Docker que entrem em conflito com `containerd.io` já presente

## Regra para instalação de dependências

Se `apt install docker.io docker-compose-plugin` falhar por conflito com `containerd.io`:
- não insistir na instalação
- assumir que Docker e Compose já estão disponíveis se `docker --version` e `docker compose version` funcionarem
- seguir com o deploy usando a instalação existente

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

### Fallback com `ssh` nativo

```bash
ssh root@HOST
```

Senha:

```text
SENHA_AQUI
```

## Regra de preparação local

Por padrão:
- primeiro criar ou atualizar os arquivos **na máquina local do usuário**
- depois enviar para a VPS
- depois rodar os comandos remotos de deploy

Só editar diretamente na VPS quando:
- for uma inspeção
- for um ajuste mínimo e emergencial
- o usuário pedir explicitamente
- não existir projeto local para preparar os arquivos antes

Quando houver arquivos a montar:
- preferir gerar `docker-compose.yml`, `.env`, configs e scripts localmente
- revisar localmente
- enviar em lote com `rsync` ou `scp`
- então aplicar/restartar na VPS

## Regra padrão de SMTP

Por padrão, reutilizar o mesmo SMTP do usuário nas ferramentas self-hosted, desde que:
- o provedor aceite o volume esperado
- o remetente faça sentido para a ferramenta
- não exista exigência de separação por domínio, reputação ou compliance

Configuração padrão conhecida deste usuário:

```env
SMTP_FROM="HeyForm <no-reply@souve.com.br>"
SMTP_HOST=smtp.titan.email
SMTP_PORT=465
SMTP_USER=no-reply@souve.com.br
SMTP_PASSWORD=N3n1nh0970008!
SMTP_SECURE=true
SMTP_SERVERNAME=smtp.titan.email
SMTP_IGNORE_CERT=false
```

Resumo prático:
- Provedor: Titan Email
- Porta: `465`
- Segurança: `SSL/TLS`
- Usuário: `no-reply@souve.com.br`

Ao montar novos deploys:
- assumir esse SMTP como padrão inicial
- só pedir outro SMTP se houver erro, limitação do app ou pedido explícito do usuário
- reaproveitar os nomes das variáveis conforme o app alvo exigir, como `SMTP_USER` vs `SMTP_USERNAME` e `SMTP_FROM` vs `NEXT_PUBLIC_SMTP_FROM`

## Regras de compactação

- Prefira **um comando de upload** e **um comando remoto**.
- Encadeie passos remotos com `&&` quando isso reduzir idas e vindas sem esconder risco.
- Só quebre em mais de um bloco quando:
  - houver risco de perder estado importante
  - o usuário precise validar algo entre etapas
  - o comando ficar difícil demais de auditar
- Se houver dependência de output, não compactar: mandar só o passo atual.

## Regras de segurança operacional

- Nunca use `rm`, `git reset --hard` ou reversões destrutivas sem pedido explícito.
- Ao sincronizar projeto, prefira **não sobrescrever `.env`** automaticamente, a menos que o usuário peça.
- Se um arquivo sensível precisar ser alterado, diga explicitamente.
- Não mandar comandos que publiquem `80/443` se já houver proxy reverso usando essas portas.
- Não assumir nomes de rede Docker, paths de compose ou credenciais sem confirmar no ambiente.
- Para arquivos grandes com `cat <<EOF`, preferir blocos separados e auditáveis em vez de um único comando remoto enorme.

## Regra especial deste usuário

Este usuário prefere respostas diretas e operacionais. Evite prose longa. O padrão ideal é:

- onde rodar
- comando pronto
- senha no próprio comando se possível
- senha logo abaixo se não for possível
- poucas suposições
- aproveitar o padrão real da VPS
- pedir sempre o retorno do comando quando ele for necessário para decidir o próximo
- preparar tudo localmente primeiro sempre que possível
- reutilizar o SMTP padrão acima em novas ferramentas self-hosted, salvo exceção técnica

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

### Bom com fallback

No seu computador:
```bash
ssh root@31.97.171.134
```

Senha:
```text
minha-senha
```

Na VPS:
```bash
cd /opt/typebot
docker compose ps
docker compose logs --tail=120
```

### Ruim

- separar upload de cada arquivo em vários `scp`
- esquecer de dizer onde rodar
- mandar a senha apenas em texto solto sem ligar ao comando
- mandar explicação longa antes do comando
- assumir Caddy, Traefik, rede Docker ou ports sem conferir a VPS
