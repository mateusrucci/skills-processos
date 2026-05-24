---
name: redtrack-api
description: >
  Master skill for building Google Apps Script automations that interact with the RedTrack API
  (https://api.redtrack.io). Use this skill whenever the user mentions RedTrack, tracker API,
  landings, offers, campaigns, domains, traffic sources, streams, conversions, or any tracking
  platform CRUD operations via Google Sheets. Also trigger when the user wants to create, update,
  delete, or list any RedTrack entity (landings, offers, campaigns, domains, sources, streams,
  networks, scripts), extract RedTrack data to spreadsheets, build bulk operations from Sheets,
  or integrate RedTrack with other tools via its REST API. This skill covers the full RedTrack API
  surface: Dictionaries, Campaigns, Landings, Offers, Domains, Sources, Streams, Networks, Scripts,
  Reports, Logs (conversions/clicks), Settings, and Publishers/WhiteLabel. Even if the user just
  says "RedTrack" or "tracker API" without specifics, use this skill.
---

# RedTrack API — Google Apps Script Integration Skill

## Overview

This skill enables Claude to generate production-ready Google Apps Script code that interacts with
the RedTrack REST API. It covers every endpoint documented at `https://api.redtrack.io/docs/index.html`.

The typical output is a `.gs` file (Google Apps Script) that:
1. Reads input data from a Google Sheets tab
2. Makes authenticated API calls to RedTrack
3. Writes results (status, IDs, errors) back to the sheet
4. Provides a custom menu in Google Sheets for easy execution

## Architecture Pattern

Every script MUST follow this proven architecture:

```
┌─────────────────────────────────────────────────┐
│  CONFIG block (API_KEY, API_URL, SHEET_NAME)    │
├─────────────────────────────────────────────────┤
│  onOpen() → custom menu with emoji labels       │
├─────────────────────────────────────────────────┤
│  Action functions (user-facing)                 │
│  ├── testarConexao()  — test connectivity       │
│  ├── processSelecionadas() — selected rows      │
│  ├── processTodasPendentes() — all pending      │
│  └── limparStatus() — clear status columns      │
├─────────────────────────────────────────────────┤
│  processarLinhas(sheet, startRow, numRows)       │
│  — main loop: reads sheet, validates, calls API │
├─────────────────────────────────────────────────┤
│  API function (single entity operation)         │
│  — builds payload, makes HTTP request, returns  │
│    { sucesso: true/false, ... }                 │
├─────────────────────────────────────────────────┤
│  Helper functions (sheet creation, formatting)  │
└─────────────────────────────────────────────────┘
```

## Authentication

RedTrack uses a simple API key passed as a query string parameter on every request:
```
?api_key=YOUR_API_KEY
```
Never send the API key in headers. Always append it to the URL.

## CONFIG Block

Always start with a `CONFIG` object:

```javascript
var CONFIG = {
  API_KEY:    'USER_API_KEY_HERE',
  SHEET_NAME: 'TabName'
};
```

Base URLs per entity:
- Landings: `https://api.redtrack.io/landings`
- Offers: `https://api.redtrack.io/offers`
- Campaigns: `https://api.redtrack.io/campaigns`
- Domains: `https://api.redtrack.io/domains`
- Sources: `https://api.redtrack.io/sources`
- Streams: `https://api.redtrack.io/streams`
- Networks: `https://api.redtrack.io/networks`
- Scripts: `https://api.redtrack.io/scripts`
- Report: `https://api.redtrack.io/report`
- Conversions: `https://api.redtrack.io/conversions`
- Clicks: `https://api.redtrack.io/tracks`
- Settings: `https://api.redtrack.io/me/settings`

## HTTP Methods per Operation

| Operation | Method | URL Pattern | Success Code |
|-----------|--------|-------------|--------------|
| List | GET | `/entity?api_key=...` | 200 |
| Get by ID | GET | `/entity/{id}?api_key=...` | 200 |
| Create | POST | `/entity?api_key=...` | 201 (or 200) |
| Update | PUT | `/entity/{id}?api_key=...` | 200 |
| Delete | DELETE | `/entity/{id}?api_key=...` | 200 |

Some endpoints deviate (e.g., `PATCH /campaigns/status` for bulk status update).

## Sheet Layout Convention

**For CREATE operations:**
```
A: Status | B: Resultado/Erro | C onwards: Entity fields (Title, Type, URL, DomainId, etc.)
```

**For UPDATE operations:**
```
A: Status | B: Resultado/Erro | C: Entity ID | D onwards: Entity fields
```

**For EXTRACT/LIST operations:**
- Row 1: Headers (auto-generated from API response keys)
- Row 2+: Data
- Headers are bold, colored (#4a86e8 background, white text), frozen

---

## Core Code Patterns

### 1. Custom Menu (onOpen)

```javascript
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('🌐 RedTrack [Entity]')
    .addItem('🧪 Testar Conexão', 'testarConexao')
    .addSeparator()
    .addItem('▶️ [Action] Selecionadas', 'actionSelecionadas')
    .addItem('▶️ [Action] Todas Pendentes', 'actionTodasPendentes')
    .addSeparator()
    .addItem('🗑️ Limpar Status e Erros', 'limparStatus')
    .addToUi();
}
```

### 2. Connection Test

```javascript
function testarConexao() {
  try {
    var url = CONFIG.API_URL + '?api_key=' + CONFIG.API_KEY + '&limit=5';
    var options = {
      method: 'get',
      headers: { 'Accept': 'application/json' },
      muteHttpExceptions: true
    };
    var response = UrlFetchApp.fetch(url, options);
    var statusCode = response.getResponseCode();
    var responseBody = response.getContentText();

    if (statusCode === 200) {
      var data = JSON.parse(responseBody);
      var items = Array.isArray(data) ? data : (data.items || []);
      SpreadsheetApp.getUi().alert('✅ Teste OK',
        'Conexão OK! Itens encontrados: ' + items.length,
        SpreadsheetApp.getUi().ButtonSet.OK);
    } else {
      SpreadsheetApp.getUi().alert('❌ Erro ' + statusCode, responseBody,
        SpreadsheetApp.getUi().ButtonSet.OK);
    }
  } catch (error) {
    SpreadsheetApp.getUi().alert('❌ Erro', error.message,
      SpreadsheetApp.getUi().ButtonSet.OK);
  }
}
```

### 3. Row Processing Loop

This is the heart of every bulk operation script:

```javascript
function processarLinhas(sheet, startRow, numRows) {
  var totalCols = /* number of columns to read */;
  var data = sheet.getRange(startRow, 1, numRows, totalCols).getValues();
  var sucessos = 0, erros = 0, pulados = 0;

  for (var i = 0; i < data.length; i++) {
    var rowIndex = startRow + i;
    var row = data[i];
    var status = row[0];

    // Skip already processed
    if (status === 'Sucesso') { pulados++; continue; }

    // Validate required fields
    if (!row[REQUIRED_COL_INDEX]) {
      sheet.getRange(rowIndex, 1).setValue('Erro');
      sheet.getRange(rowIndex, 2).setValue('Campo obrigatório faltando');
      erros++; continue;
    }

    // Mark as processing
    sheet.getRange(rowIndex, 1).setValue('Processando...');
    SpreadsheetApp.flush();

    // Call API
    var resultado = apiFunction(/* params from row */);

    if (resultado.sucesso) {
      sheet.getRange(rowIndex, 1).setValue('Sucesso');
      sheet.getRange(rowIndex, 2).setValue('ID: ' + (resultado.id || 'ok'));
      sucessos++;
    } else {
      sheet.getRange(rowIndex, 1).setValue('Erro');
      sheet.getRange(rowIndex, 2).setValue(resultado.erro.substring(0, 500));
      erros++;
    }

    SpreadsheetApp.flush();
    Utilities.sleep(300); // Rate limiting
  }

  SpreadsheetApp.getUi().alert('✅ Processamento Concluído',
    '✅ Sucessos: ' + sucessos + '\n❌ Erros: ' + erros + '\n⏭️ Pulados: ' + pulados,
    SpreadsheetApp.getUi().ButtonSet.OK);
}
```

### 4. API Request Function (CREATE — POST)

```javascript
function criarEntity(/* params */) {
  try {
    var payload = { /* build from params */ };

    var url = CONFIG.API_URL + '?api_key=' + CONFIG.API_KEY;
    var options = {
      method: 'post',
      contentType: 'application/json',
      headers: { 'Accept': 'application/json' },
      payload: JSON.stringify(payload),
      muteHttpExceptions: true
    };

    var response = UrlFetchApp.fetch(url, options);
    var responseCode = response.getResponseCode();
    var responseBody = response.getContentText();

    if (responseCode === 201 || responseCode === 200) {
      var data = JSON.parse(responseBody);
      return { sucesso: true, id: data.id || null, dados: data };
    } else {
      var msg = 'HTTP ' + responseCode;
      try { msg += ': ' + JSON.stringify(JSON.parse(responseBody)); } catch(e) { msg += ': ' + responseBody; }
      return { sucesso: false, erro: msg };
    }
  } catch (error) {
    return { sucesso: false, erro: 'Exceção: ' + error.message };
  }
}
```

### 5. API Request Function (UPDATE — PUT)

Key difference: method is `'put'` and URL includes the entity ID in the path.

```javascript
function atualizarEntity(entityId, /* params */) {
  try {
    var payload = { id: entityId.toString(), /* other fields */ };

    var url = CONFIG.API_URL + '/' + entityId + '?api_key=' + CONFIG.API_KEY;
    var options = {
      method: 'put',
      contentType: 'application/json',
      headers: { 'Accept': 'application/json' },
      payload: JSON.stringify(payload),
      muteHttpExceptions: true
    };

    var response = UrlFetchApp.fetch(url, options);
    var responseCode = response.getResponseCode();
    var responseBody = response.getContentText();

    if (responseCode === 200) {
      return { sucesso: true, dados: JSON.parse(responseBody) };
    } else {
      var msg = 'HTTP ' + responseCode;
      try { msg += ': ' + JSON.stringify(JSON.parse(responseBody)); } catch(e) { msg += ': ' + responseBody; }
      return { sucesso: false, erro: msg };
    }
  } catch (error) {
    return { sucesso: false, erro: 'Exceção: ' + error.message };
  }
}
```

### 6. Data Extraction Pattern (LIST all to sheet)

For scripts that pull data FROM RedTrack INTO a sheet:

```javascript
function extrairEntities() {
  var sheet = obterOuCriarAba();
  sheet.clearContents();

  try {
    var url = CONFIG.API_URL + '?api_key=' + CONFIG.API_KEY + '&limit=500';
    var response = UrlFetchApp.fetch(url, {
      method: 'get',
      headers: { 'Accept': 'application/json' },
      muteHttpExceptions: true
    });

    if (response.getResponseCode() !== 200) {
      SpreadsheetApp.getUi().alert('❌ Erro', response.getContentText(),
        SpreadsheetApp.getUi().ButtonSet.OK);
      return;
    }

    var items = JSON.parse(response.getContentText());
    // Some endpoints return array directly, others return { items: [], total: N }
    if (!Array.isArray(items)) items = items.items || [];

    if (items.length === 0) {
      SpreadsheetApp.getUi().alert('ℹ️', 'Nenhum item encontrado.',
        SpreadsheetApp.getUi().ButtonSet.OK);
      return;
    }

    // Collect all unique keys for dynamic headers
    var keys = [];
    for (var i = 0; i < items.length; i++) {
      var itemKeys = Object.keys(items[i]);
      for (var j = 0; j < itemKeys.length; j++) {
        if (keys.indexOf(itemKeys[j]) === -1) keys.push(itemKeys[j]);
      }
    }

    // Write header
    var header = sheet.getRange(1, 1, 1, keys.length);
    header.setValues([keys]);
    header.setFontWeight('bold');
    header.setBackground('#4a86e8');
    header.setFontColor('#ffffff');

    // Write data rows — stringify objects/arrays
    var rows = [];
    for (var i = 0; i < items.length; i++) {
      var row = [];
      for (var j = 0; j < keys.length; j++) {
        var val = items[i][keys[j]];
        if (val === null || val === undefined) row.push('');
        else if (typeof val === 'object') row.push(JSON.stringify(val));
        else row.push(val);
      }
      rows.push(row);
    }

    sheet.getRange(2, 1, rows.length, keys.length).setValues(rows);
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, keys.length);

    SpreadsheetApp.getUi().alert('✅ Concluído',
      items.length + ' itens extraídos para "' + CONFIG.SHEET_NAME + '"',
      SpreadsheetApp.getUi().ButtonSet.OK);

  } catch (e) {
    SpreadsheetApp.getUi().alert('❌ Erro', e.message,
      SpreadsheetApp.getUi().ButtonSet.OK);
  }
}

function obterOuCriarAba() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(CONFIG.SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(CONFIG.SHEET_NAME);
  return sheet;
}
```

---

## Data Type Handling

When reading from Google Sheets and building API payloads:

- **Strings**: Always `.toString()` — Sheets may return numbers for IDs
- **Booleans**: Check for `true`, `'TRUE'`, `'true'`, and `1`
- **Arrays (tags, etc.)**: Read as comma-separated string, split and trim:
  ```javascript
  var tagsArray = [];
  if (tags && tags.toString().trim() !== '') {
    var split = tags.toString().split(',');
    for (var i = 0; i < split.length; i++) {
      var t = split[i].trim();
      if (t !== '') tagsArray.push(t);
    }
  }
  ```
- **Optional fields**: Only include in payload if non-empty:
  ```javascript
  if (value && value.toString().trim() !== '') {
    payload.field = value.toString();
  }
  ```
- **Nested objects**: Use `JSON.stringify()` when writing to sheets, `JSON.parse()` when reading back

## Error Handling

Always use `muteHttpExceptions: true` in fetch options. Parse error responses:

```javascript
if (responseCode !== 200) {
  var msg = 'HTTP ' + responseCode;
  try {
    var errorData = JSON.parse(responseBody);
    msg += ': ' + (errorData.error || JSON.stringify(errorData));
  } catch(e) {
    msg += ': ' + responseBody;
  }
  return { sucesso: false, erro: msg };
}
```

## Rate Limiting

- Add `Utilities.sleep(300)` between API calls in loops (300ms minimum)
- Report API has a hard 20 RPM limit — use `Utilities.sleep(3000)` for report calls
- For large batch operations (100+ items), consider adding a progress counter

## Unified Menu Pattern

When the user has multiple RedTrack scripts in one spreadsheet, use a unified menu:

```javascript
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('🌐 RedTrack')
    .addSubMenu(ui.createMenu('📄 Landings')
      .addItem('Criar Landings', 'criarLandings')
      .addItem('Atualizar Landings', 'atualizarLandings'))
    .addSubMenu(ui.createMenu('🎯 Offers')
      .addItem('Extrair Offers', 'extrairOffers')
      .addItem('Criar Offers', 'criarOffers'))
    .addSubMenu(ui.createMenu('📊 Campanhas')
      .addItem('Extrair Campanhas', 'extrairCampanhas'))
    .addSeparator()
    .addItem('🧪 Testar Conexão', 'testarConexao')
    .addToUi();
}
```

## Pagination

Some endpoints support pagination with `page` and `per` parameters:

```javascript
function extrairTodos() {
  var page = 1;
  var perPage = 100;
  var allItems = [];

  while (true) {
    var url = CONFIG.API_URL + '?api_key=' + CONFIG.API_KEY
      + '&page=' + page + '&per=' + perPage;
    var response = UrlFetchApp.fetch(url, {
      method: 'get',
      headers: { 'Accept': 'application/json' },
      muteHttpExceptions: true
    });

    var data = JSON.parse(response.getContentText());
    var items = Array.isArray(data) ? data : (data.items || []);

    if (items.length === 0) break;
    allItems = allItems.concat(items);

    if (items.length < perPage) break; // last page
    page++;
    Utilities.sleep(300);
  }

  return allItems;
}
```

## Language

The user communicates in Portuguese (BR). All UI strings (menu labels, alert messages,
status values, error messages) should be in Portuguese. Code comments can be in Portuguese
or English. Variable names should be descriptive and can be in either language.

---

# API Endpoint Reference

Base URL: `https://api.redtrack.io`
Auth: `?api_key=YOUR_KEY` on every request (query parameter, never header)

## Landings

### GET /landings — List landings
Query params: `api_key*`, `title`, `type` (landing|prelanding), `ids` (comma-sep), `tags` (comma-sep), `page`, `per`, `time_interval`, `date_from`, `date_to`, `total_stat` (bool)

Response 200 (default = array):
```json
[{
  "id": "string",
  "title": "string",
  "type": "string",
  "url": "string",
  "domain_id": "string",
  "listicle": true,
  "tags": ["string"],
  "serial_number": 0,
  "stat": {},
  "created_at": "string",
  "updated_at": "string",
  "user_id": "string",
  "workspace_ids": ["string"]
}]
```
With `total_stat=true`: `{ "total": 0, "items": [...] }`

### POST /landings — Create landing
Query: `api_key*`
Body (JSON):
```json
{
  "title": "string",       // required
  "domain_id": "string",   // required
  "type": "string",        // "landing" or "prelanding"
  "url": "string",
  "listicle": false,
  "tags": ["string"]
}
```
Response 201: landing object

### GET /landings/{id} — Get by ID
Response 200: landing object

### PUT /landings/{id} — Update landing
Body: same as create, plus `"id": "string"`
Response 200: updated landing object

### DELETE /landings/{id} — Delete landing
Response 200

---

## Offers

### GET /offers — List offers
Query: `api_key*`, `title`, `ids`, `networks`, `countries`, `status`, `tags`, `page`, `per`, `time_interval`, `date_from`, `date_to`, `total_stat`, `pixel_id`, `pixel_date_from`, `pixel_date_to`

Response 200 (default = array):
```json
[{
  "id": "string",
  "title": "string",
  "url": "string",
  "status": 0,
  "category": "string",
  "subcategory": "string",
  "country_codes": ["string"],
  "payment": { "amount": 0 },
  "cap": 0,
  "cap_alert": true,
  "clcap": 0,
  "clcap_alert": true,
  "click_cap": 0,
  "click_cap_period": "string",
  "click_cap_type": "string",
  "default_conversion_status": "string",
  "network_title": "string",
  "notes": "string",
  "postback_url": "string",
  "program_id": "string",
  "script_id": "string",
  "tags": ["string"],
  "pixels": [{
    "id": "string",
    "title": "string",
    "integration_alias": "string",
    "facebook": {
      "pixel_id": "string",
      "conversions_apikey": "string",
      "action_source_fb": "string",
      "event_source_url_fb": "string",
      "is_types_split": true,
      "settings": {
        "default_payout_type": 0,
        "default_payout_value": 0,
        "event_name": "string",
        "matching": [{
          "conversion_type": "string",
          "facebook_type": 0,
          "payout_type": 0,
          "payout_value": 0
        }]
      }
    },
    "tiktok": {
      "pixel_id": "string",
      "pixel_token": "string",
      "matching": [{ "conversions_type": "string", "tiktok_type": 0 }]
    },
    "snapchat": {
      "pixel_id": "string",
      "pixel_token": "string",
      "matching": [{ "conversions_type": "string", "snapchat_type": 0 }]
    }
  }],
  "pixels_relations": [{ "id": "string", "created_at": "string" }],
  "fingerprint_settings": {
    "first_click_weight": 0,
    "last_click_weight": 0,
    "assisted_click_weight": 0
  },
  "expires_at": "string",
  "stat": {},
  "created_at": "string",
  "updated_at": "string"
}]
```
With `total_stat=true`: `{ "general_total": 0, "total": 0, "items": [...] }`

### POST /offers — Create offer
Body: offer object. Required: `title`, `url`
Response 201

### GET /offers/{id}
### PUT /offers/{id}
### PATCH /offers/status — Bulk status update
### GET /offers/export — Export to S3

---

## Campaigns

### GET /campaigns — List campaigns
Query: `api_key*`, `title`, `ids`, `sources`, `status`, `tags`, `page`, `per`, `time_interval`, `date_from`, `date_to`, `timezone`, `total_stat`

Response 200 (default = array of campaign objects)

Campaign object key fields:
```json
{
  "id": "string",
  "title": "string",
  "domain_id": "string",
  "source_id": "string",
  "source_title": "string",
  "type": "string",
  "status": 0,
  "cost_model": "string",
  "cpc": 0,
  "redirect_type": 0,
  "tags": ["string"],
  "notes": ["string"],
  "streams": [{
    "id": "string",
    "weight": 0,
    "stream": {
      "id": "string",
      "title": "string",
      "template": true,
      "filters": { /* complex filter object */ },
      "landings": [{ "id": "string", "name": "string", "weight": 0 }],
      "offers": [{ "id": "string", "name": "string", "weight": 0 }],
      "prelandings": [{ "id": "string", "name": "string", "weight": 0 }]
    },
    "optimization": {
      "is_enabled": true,
      "metric": "string",
      "threshold": 0,
      "clicks_limit": 0,
      "limit": 0,
      "count": 0,
      "multiplicator": 0,
      "winner_share_limit": 0,
      "subs": ["string"],
      "conversion_types": ["string"]
    }
  }],
  "postbacks": [{ "url": "string", "statuses": ["string"], "goals": ["string"], "request_method": 0 }],
  "integration_postback": { /* same structure as postback */ },
  "pixels": [{ /* postback structure */ }],
  "integrations": { "cost_update": true, "fraudscore": true },
  "notifications": { "enabled": true, "clicks": 0, "conversions": 0, "roi": 0, "condition": "string" },
  "trackback_url": "string",
  "impression_url": "string",
  "created_at": "string",
  "updated_at": "string"
}
```

### POST /campaigns — Create campaign
Body: campaign object. Minimum: `title`, `domain_id`, at least one stream with offers.
Response 201

### GET /campaigns/{id}
### PUT /campaigns/{id} — Update campaign
### PATCH /campaigns/status — Bulk status update
### GET /campaigns/v2 — List (v2 format)

---

## Domains

### GET /domains — List domains
Query: `api_key*`, `type`, `page`, `per`

Response 200:
```json
{
  "items": [{
    "id": "string",
    "url": "string",
    "type": "string",
    "fallback_url": "string",
    "use_auto_generated_ssl": true,
    "ssl": { "active": true, "crt": "string", "key": "string", "expires": "string", "error": "string" },
    "acme": { "active": true, "crt": "string", "key": "string", "expires": "string", "error": "string" },
    "registry_expiry_date": "string",
    "created_at": "string",
    "user_id": "string",
    "workspace_ids": ["string"]
  }],
  "total": 0
}
```
**Important**: Domains returns `{ items, total }`, NOT a raw array.

### POST /domains — Create domain
Body: domain object. Required: `url`
Response 200

### PUT /domains/{id} — Update
### DELETE /domains/{id} — Delete
### POST /domains/regenerated_free_ssl/{id} — Regenerate SSL

---

## Sources (Traffic Sources)

### GET /sources — List sources
Query: `api_key*`, `title`, `ids`, `page`, `per`, `time_interval`, `date_from`, `date_to`, `total_stat`, `pixel_id`, `pixel_date_from`, `pixel_date_to`

Source object key fields:
```json
{
  "id": "string",
  "title": "string",
  "type": "string",
  "alias": "string",
  "status": "string",
  "preset_id": "string",
  "enable_direct_traffic": true,
  "enable_impressions": true,
  "currency": "string",
  "cost_level": "string",
  "subs": [{ "alias": "string", "value": "string", "role": "string", "hint": "string" }],
  "integrations": {
    "source_name": "string",
    "fraudscore": true,
    "params": { "key": "value" }
  },
  "integration_types": {
    "cost_update": true,
    "pause_campaign": true,
    "pause_creative": true,
    "pause_adgroup": true,
    "facebook_one_click": { "enabled": true, "ad_accounts": ["string"] }
  },
  "pixels": [{ /* pixel object */ }],
  "ref_id": "string",
  "external_id": "string"
}
```

### POST /sources — Create
### PUT /sources — Update (note: PUT on collection, not /{id})
### GET /sources/{id}
### DELETE /sources/{id}
### POST /sources/clone — Clone source

---

## Streams

### GET /streams — List
Query: `api_key*`, `title`, `page`, `per`

Response 200: `{ "items": [...], "total": 0 }`

Stream object:
```json
{
  "id": "string",
  "title": "string",
  "template": true,
  "filters": { /* filter object for every dimension */ },
  "landings": [{ "id": "string", "name": "string", "weight": 0, "filters": {} }],
  "offers": [{ "id": "string", "name": "string", "weight": 0, "filters": {} }],
  "prelandings": [{ "id": "string", "name": "string", "weight": 0, "filters": {} }],
  "expires_at": "string",
  "user_id": "string"
}
```

### POST /streams — Create
### PUT /streams/{id} — Update
### DELETE /streams/{id}
### GET /streams/{id}/optimization
### DELETE /streams/{id}/optimization — Reset
### GET /streams/{id}/optimization/paths

---

## Networks (Affiliate Networks)

### GET /networks — List
### POST /networks — Create
### GET /networks/{id}
### PUT /networks/{id}
### DELETE /networks/{id}

Network object key fields:
```json
{
  "id": "string",
  "title": "string",
  "alias": "string",
  "status": "string",
  "offer_url": "string",
  "postback_url": "string",
  "postback_mode": "string",
  "clickid": "string",
  "currency": "string",
  "subs": [{ "alias": "string", "value": "string" }],
  "offer_count": 0
}
```

---

## Scripts (Tracking Scripts)

### GET /scripts — List
### POST /scripts — Create
### GET /scripts/{id}
### PUT /scripts/{id}
### DELETE /scripts/{id}

Script object:
```json
{
  "id": "string",
  "name": "string",
  "campaign_id": "string",
  "domain_id": "string",
  "script_type": 0,
  "attribution_type": 0,
  "attribution_window": 0,
  "cookie_domain": "string",
  "script_code": "string",
  "is_auto_generated": true
}
```

---

## Reports

### GET /report — Traffic report
**Rate limit: 20 RPM**

Required params: `api_key*`, `group*`, `date_from*` (YYYY-MM-DD), `date_to*` (YYYY-MM-DD)

Optional filters: `campaign_id`, `source_id`, `offer_id`, `landing_id`, `network_id`,
`sub1`-`sub20`, `rt_source`, `rt_medium`, `rt_campaign`, `rt_adgroup`, `rt_ad`,
`rt_placement`, `rt_keyword`, `timezone`, `time_interval`, `tracks_view`,
`page`, `per` (max 1000), `total` (bool), `sortby`, `direction`,
`table_settings_name`

Response 200: array of stat objects (dynamic keys based on grouping)

### POST /tracks/cost — Update costs

---

## Conversions Log

### GET /conversions — Conversions log
### POST /conversions — Upload conversions
Body: `{ "campaign_id": "string", "clickid": "string", "payout": 0, "type": "string", "created_at": "string" }`
### GET /conversions/export — Export conversions

---

## Clicks Log

### GET /tracks — Clicks log

---

## Settings

### GET /me/settings — Get user settings
### PUT /me/settings — Update settings

---

## Dictionaries

All GET, all take `api_key` only:
- `/browsers`, `/browser_fullnames`
- `/categories`
- `/cities`
- `/connection_types`
- `/countries`
- `/currencies`
- `/devices`, `/device_brands`, `/device_fullnames`
- `/isp`
- `/languages`
- `/os`, `/os_fullnames`
- `/proxy_types`
- `/regions`
- `/timezones`

---

## Publishers / WhiteLabel

### POST /pub/auth — Publisher auth
### GET /pub/campaigns — Publisher campaigns
### GET /pub/me — Publisher info
### PUT /pub/profile — Update publisher
### POST /pub/publishers — Signup
### POST /pub/reset_password
### GET /pub/settings — Whitelabel settings
### GET /pub/payments — List payments
### POST /pub/payments — Request payment
### PUT /pub/payments/{id} — Update payment
### POST /pub/postbacks — Publisher conversions
### GET /pub/reports/traffic — Publisher stats
### GET /pub/referrals — Referral program participants
### GET /publishers/export — Export publishers
### GET /publishers/referral — Referral participants
### PUT /publishers/{id} — Update publisher

---

## Filters Object Structure

Used in Streams, Campaign Streams, and Landing/Offer/Prelanding filters:

```json
{
  "country": { "active": true, "exclude": false, "kind": 0, "comparison_type": "string", "values": ["US", "CA"] },
  "device_type": { "active": true, "exclude": false, "kind": 0, "values": ["mobile", "desktop"] },
  "os": { "active": true, "values": ["iOS", "Android"] },
  "browser": { "active": true, "values": ["Chrome"] },
  "browser_version": {},
  "city": {},
  "connection_type": {},
  "device_brand": {},
  "device_model": {},
  "domain_referrer": {},
  "fraud": {},
  "ip": {},
  "isp": {},
  "languages": {},
  "os_version": {},
  "proxy_type": {},
  "referrer": {},
  "region": {},
  "subs": {
    "active": true,
    "exclude": false,
    "kind": 0,
    "items": { "sub1": "value", "sub2": "value" }
  },
  "unique_visitor": { "active": true, "exclude": false, "kind": 0 }
}
```

Each filter dimension follows the ValuesFilter pattern with `active`, `exclude`, `kind`, `comparison_type`, and `values[]` — except `subs` which uses `items` (SubItems object) and `unique_visitor` which has no values array.
