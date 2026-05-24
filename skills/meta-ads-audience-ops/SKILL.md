---
name: meta-ads-audience-ops
description: Cria, audita e padroniza públicos no Meta/Facebook Ads via Marketing API, especialmente Website Custom Audiences por pixel, públicos de remarketing, listas customizadas e bases para lookalikes. Use quando o usuário pedir criação de públicos, remarketing, exclusões, lookalikes, auditoria de públicos ou operação de audiências do Facebook Ads por API.
---

# Meta Ads Audience Ops

## Guardrails

- Nunca grave access tokens em arquivos. Use `META_ACCESS_TOKEN` no ambiente.
- Antes de criar públicos, valide acesso com `python3 meta_audience_ops.py validate`.
- Antes de criar públicos novos, liste públicos existentes com `python3 meta_audience_ops.py list-audiences` para evitar duplicação.
- Criação de públicos altera a conta de anúncios; confirme nomes, regras e janelas de retenção antes de executar.
- Se a Meta retornar `Custom Audience Terms not yet accepted`, oriente o usuário a aceitar os termos de Custom Audiences no Business Manager.
- Se a API retornar erro de campo obsoleto, ajuste os fields para a versão ativa da Marketing API.

## Default Context

- Conta padrão: `act_977201716903353`
- Pixel padrão: `1172482898007013`
- API padrão no script: `v25.0`
- Script operacional no projeto: `meta_audience_ops.py`

## Workflow

1. Validar token, conta e pixel.
2. Listar públicos existentes e observar duplicatas, públicos pequenos, públicos desatualizados e lookalikes com falha.
3. Definir matriz de públicos:
   - site/all visitors por `PageView` ou URL;
   - eventos de fundo de funil como `Lead`, `AddToCart`, `InitiateCheckout`, `Purchase`;
   - Instagram visitas e engajamento com janelas 30D, 60D, 90D, 120D, 150D, 180D e 365D;
   - Instagram seguidores como público único, sem matriz de dias;
   - Página/Facebook engajamento com `page_engaged` e janelas 30D, 60D, 90D, 120D, 150D, 180D e 365D;
   - Vídeo conforme UI do Gerenciador de Anúncios: copiar um público referência e criar `subtype=ENGAGEMENT` com regra em lista usando `event_name` como `video_view_25_percent`, `object_id` do vídeo e `context_id` da página;
   - janelas 1D, 3D, 7D, 14D, 30D, 60D, 90D, 120D, 150D, 180D e 365D conforme volume;
   - exclusões de compradores/leads quando a operação pedir.
4. Criar públicos com nomes consistentes.
5. Listar novamente para capturar IDs e status.

## Naming

Use nomes legíveis para operação:

```text
[SITE] [EVENTO_OU_REGRA] [MARCA/PRODUTO] [JANELA]
```

Exemplos:

```text
[SITE] PAGE VIEW IGUMMY 30D
[SITE] ADD TO CART IGUMMY 30D
[SITE] PURCHASE IGUMMY 180D
```

## Commands

Validar:

```bash
python3 meta_audience_ops.py validate
```

Listar públicos:

```bash
python3 meta_audience_ops.py list-audiences --limit 100
```

Criar público de visitantes do site:

```bash
python3 meta_audience_ops.py create-website \
  --name "[SITE] PAGE VIEW IGUMMY 30D" \
  --retention-days 30
```

Criar público por evento:

```bash
python3 meta_audience_ops.py create-website \
  --name "[SITE] LEAD IGUMMY 180D" \
  --retention-days 180 \
  --event "Lead"
```

Criar público por URL:

```bash
python3 meta_audience_ops.py create-website \
  --name "[SITE] CHECKOUT IGUMMY 30D" \
  --retention-days 30 \
  --url-contains "checkout"
```

## Instagram Events

Fonte SOUFIT usada nos públicos existentes: `3972113599547814`.

- `IG-SEGUIDORES`: criar apenas um público, sem dias. Evento: `INSTAGRAM_PROFILE_FOLLOW`.
- `IG-VISITAS-{DAYS}D`: criar em matriz de dias. Evento: `ig_business_profile_visit`.
- `IG-ENGAJAMENTO-{DAYS}D`: criar em matriz de dias. Evento: `ig_business_profile_all`.

Comando para seguidores:

```bash
python3 meta_audience_ops.py create-instagram-followers --name "IG-SEGUIDORES"
```

Comando para visitas e engajamento:

```bash
python3 meta_audience_ops.py create-instagram-batch \
  --events ig_business_profile_visit ig_business_profile_all \
  --name-prefixes VISITAS ENGAJAMENTO \
  --retention-days 30 60 90 120 150 180 365
```

## Page/Facebook Events

Fonte de página SOUFIT: `677623735431645`.

- `FB-ENGAJAMENTO-{DAYS}D`: evento `page_engaged`.
- `FB-VISITAS-{DAYS}D`: evento `page_visited`.

Comando para todos que interagiram com a Página:

```bash
python3 meta_audience_ops.py create-page-batch \
  --events page_engaged \
  --name-prefixes ENGAJAMENTO \
  --retention-days 30 60 90 120 150 180 365
```

## Video Events

- Na UI da Meta, o público de vídeo salvo na conta apareceu como `subtype=ENGAGEMENT`, `data_source.sub_type=ENGAGEMENT_EVENTS`.
- O formato correto observado no público referência é uma lista no `rule`, por exemplo:

```json
[
  {
    "event_name": "video_view_25_percent",
    "object_id": "17867801079522600",
    "context_id": "677623735431645"
  }
]
```

- Não usar `subtype=VIDEO` + `video_group_ids` para esta operação, porque a UI não exibiu corretamente os públicos criados assim.
- Quando o usuário pedir para usar referência, copiar a regra de um público existente, por nome ou ID, e variar apenas `retention_days` e nome.
- O padrão operacional atual é `VIDEOVIEW-SOUFIT-25-{DAYS}D`, salvo instrução diferente.

Comandos:

```bash
python3 meta_audience_ops.py create-video-batch \
  --reference-audience-name VIDEOVIEW-SOUFIT-25-365D \
  --name-prefix VIDEOVIEW-SOUFIT-25 \
  --retention-days 30 90 365
```
