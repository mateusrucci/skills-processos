# 04 — Design System & Voz de Marca

> Identidade visual e verbal da SouFit (Brandbook v2 · MAR/2026).
> Fonte canônica: `/Modernitty/Design System/design-system-fitmoderno.md`

---

## 🎨 Paleta de cores

### Primárias da marca (uso em logo, CTAs, títulos)

| Token | Hex | Uso |
|---|---|---|
| `--sf-green` | `#ACC435` | Verde SouFit — destaque, CTA principal |
| `--sf-blue` | `#4E93D1` | Azul SouFit — secundária, educacional (Sábio) |
| `--sf-dark` | `#302F2D` | Preto/grafite oficial |
| `--sf-offwhite` | `#F3F1F1` | Off-white principal (fundos) |

### Subtons

```css
--sf-green-soft: #d6e58c;
--sf-green-mute: #ebf2c6;
--sf-blue-soft:  #a7c6e8;
--sf-blue-mute:  #d4e3f3;
```

### Gradiente único permitido

```css
--sf-gradient-primary: linear-gradient(180deg, #4E93D1 0%, #ACC435 100%);
```

⚠️ **Proibido em logo.** Só em fundos/elementos, e SEMPRE entre as duas primárias.

### Apoio funcional

```css
--sf-text-muted: #6b6b6b;
--sf-border-soft: rgba(48, 47, 45, 0.12);
--sf-shadow-card: 0 15px 80px rgba(0, 0, 0, 0.10);
```

---

## 🏷️ Paletas de produto (rótulos e embalagens)

⚠️ **Logo PROIBIDO nessas cores.** Aplicação exclusiva em rótulos.

### Linha Saúde

| Produto | Principal | Secundária |
|---|---|---|
| Vitali Pro | `#251517` | `#561920` |
| MultiVita Homem | `#2B2D56` | `#285098` |
| MultiVita Mulher | `#CD5588` | `#DFA3B5` |
| MultiVita Sênior | `#606A72` | `#A2B1BD` |
| Puro Bronze | `#CD652E` | `#DC913D` |
| Ác. Hialurônico | `#58428D` | `#705B9E` |
| Colágeno Verisol | `#C63380` | `#CE609A` |
| Coenzima Q10 | `#568C40` | `#8DB863` |
| Cúrcuma | `#D3A121` | `#EBBD30` |
| Imune AZ | `#4691CF` | `#76B8E9` |
| Magnésio 5em1 | `#3A9C76` | `#7BB58E` |
| NAC | `#C73D48` | `#D68280` |
| Ômega 3 | `#DF9A29` | `#F1CB3D` |

### Linha Performance *(creme base `#FDF8DD`)*

| Produto | Principal | Secundária |
|---|---|---|
| Whey (verde) | `#53602D` | `#B0C333` |
| Whey (chocolate) | `#693F2E` | `#C7A182` |
| Whey (morango) | `#BA3E4F` | `#DD9997` |
| Whey (baunilha) | `#BFA125` | `#EAD478` |
| BCAA | `#4E88A2` | `#69B7DA` |
| Colágeno (verde) | `#21512F` | `#7AAE45` |
| Colágeno (laranja) | `#C75C1F` | `#E09F2F` |
| Colágeno (uva) | `#351520` | `#921E38` |
| Creatina | `#BA3E4F` | `#E0A8B8` |
| L-glutamina | `#186369` | `#229EA8` |
| Pré-treino | `#D98932` | `#E6B034` |
| Pré-treino (rosa) | `#9E1B46` | `#CC577A` |

> **Régua de expansão:** novos produtos seguem régua harmônica, com base no verde primário SouFit.

---

## ✍️ Tipografia

```css
--sf-font-display: "Obviously Narrow", "obviously-narrow", sans-serif;
--sf-font-body:    "Sora", "Archivo", sans-serif;
```

### Pesos por uso

| Elemento | Família | Peso | Tamanho desk | Tamanho mob |
|---|---|---|---|---|
| Hero title | Obviously Narrow Black | 900 | 85px | 36px |
| Section title | Obviously Narrow Black | 900 | 42px | 32px |
| Eyebrow | Obviously Narrow Light | 300 (tracking 2px) | 18px | — |
| Body | Sora Light | 300 | 18px (line 1.55) | — |
| Button / Strong | Sora Bold | 700 | 18px | — |

### Regras tipográficas

- ✅ Preferir **caixa baixa** iniciando frases com maiúscula
- ✅ Caixa baixa estilizada (tudo minúsculo) permitida
- ❌ Sem sombras, 3D, distorções (exceto campanhas sazonais)
- ✅ Sempre garantir contraste e legibilidade

---

## 🎯 Regras de aplicação do logo

✅ **Cores permitidas:** verde · azul · preto (`#302F2D`) · branco
❌ **NUNCA:**
- Em outras cores (incluindo cores de produto)
- Sobre fundo verde ou azul (perde reconhecimento)
- Com distorção, contorno, sombra, rotação ou gradiente
- Sem margem de proteção (mínimo `2x`)

---

## 🟢 CTAs

Pill arredondado com ícone circular à direita.

```css
.sf-button {
  background: var(--sf-green);       /* ou --sf-blue (educacional) */
  color: var(--sf-dark);              /* ou #fff sobre azul */
  border-radius: 9999px;
  padding: 22px 110px 22px 28px;
  font-family: var(--sf-font-body);
  font-weight: 700;                   /* Sora Bold */
  font-size: 18px;
}
```

**Variantes:**
- `.sf-button` — verde, padrão
- `.sf-button--blue` — azul, educacional/Sábio
- `.sf-button--outline` — transparente com borda

---

## 📦 Cards & Pills

```css
--sf-radius-card: 20px;
--sf-radius-image: 10px;
--sf-radius-pill: 9999px;
--sf-container-desktop: 1140px;
--sf-section-gap: 88px;
```

**Variantes de seção:**
- `.sf-section--green` (fundo verde, texto dark)
- `.sf-section--blue` (fundo azul, texto branco)
- `.sf-section--dark` (fundo preto, texto offwhite)
- `.sf-section--light` (fundo offwhite, texto dark)

---

## 🌸 Elementos visuais da marca

- **Formas orgânicas e arredondadas** (lembrando corpo humano e naturalidade)
- **Cápsulas/pills** como contêineres de tag (`@soufitmoderno`, `2025`)
- **Elipses verticais** — "M" estilizada do brand pattern (fundo de capas e cards)
- **Estrelas de 4 pontas (`✦`)** — pontuação visual moderna; usar em pares cercando títulos curtos
- **Ícones de linha fina, sem preenchimento**, dentro de círculo com mesma stroke

---

## 🗣️ Voz de marca

### Os 4 pilares

| Pilar | Como aparece |
|---|---|
| **Amiga que entende** | Abre com cotidiano real |
| **Especialista sem esnobismo** | Cita ciência, explica sempre |
| **Motivadora sem pressão** | CTA é convite ("que tal?"), nunca exigência |
| **Girly com substância** | Estética + profundidade |

### Como FALAMOS (✅)
- "Nós te entendemos." / "Sabemos que a rotina é corrida."
- Explicar ciência em linguagem simples
- Incentivar consistência, não perfeição
- Criar senso de comunidade

### Como NÃO FALAMOS (❌)
- ❌ "Perca 10kg em uma semana!" / "Fórmula mágica."
- ❌ Jargão científico em excesso
- ❌ "Não desista!" / "Seja forte!" (motivação agressiva)
- ❌ Tom de superioridade ou "solução única"
- ❌ Estética isolada — SouFit fala de saúde **integral**

### Sobre fotografia

- ✅ Pessoas reais, luz natural, sorrisos genuínos
- ❌ Antes/depois agressivo
- ✅ Estética "rotina possível", não transformação extrema

---

## 🏷️ Anatomia de rótulos

### Rótulos padrão (linha Saúde / Performance)

1. **Assinatura** — logotipo SouFit em pílula escura no topo
2. **Nome do produto** — Obviously Narrow Light (sub-categoria, ex.: "beauty") + Obviously Narrow Super (nome forte, ex.: "bronze") empilhados
3. **Descrição** — Sora Bold ("Suplemento alimentar em cápsulas")
4. **Tag de ativo** — pílula com Sora Bold (ex.: "BETACAROTENO + L-TIROSINA")
5. **Destaques** — lista com check + Obviously Narrow Light
6. **Cores** — cor de produto + paleta principal SouFit

### Rótulos independentes (ex.: ChocoTox)

Pode usar logotipo, fontes e paletas exclusivas, **desde que mantenha:**
- A assinatura SouFit em pílula no topo
- A família Sora em todos os textos descritivos

---

## 🔄 Aliases legados (compat com Fit Moderno antigo)

```css
--fm-brand: var(--sf-green);
--fm-black: var(--sf-dark);
--fm-white: #ffffff;
--fm-gray-bg: var(--sf-offwhite);
--fm-font-display: var(--sf-font-display);
--fm-font-body:    var(--sf-font-body);
```

**Migração da landing antiga Fit Moderno:**
1. Trocar `#A1C41E` por `var(--sf-green)` (`#ACC435`) — diferença ~2% de matiz
2. Trocar `Archivo` por `Sora`
3. Introduzir azul `#4E93D1` como secundária em sub-cabeçalhos educacionais
4. Logo SouFit em verde sobre fundo claro/escuro
