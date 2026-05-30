# Design System - Soufit

Sistema de identidade visual da marca **Soufit** (Grupo MDT), atualizado com base no Brandbook Soufit v2 (MAR/2026).

Soufit é a marca-mãe; produtos como **Fit Moderno**, **Beauty Bronze**, **Beauty Verisol**, **Soneka Booster**, **Immune Life**, entre outros, operam sob essa identidade. A landing original do Fit Moderno (referenciada em `wp-content/uploads/elementor/css/post-197.css` e `post-11.css`) segue compatível como uma das aplicações desse sistema.

## Posicionamento

- **Segmento**: emagrecimento, beleza, bem-estar e longevidade.
- **Arquétipos**: Cuidador (acolhedor, empático) + Sábio (educacional, transparente).
- **Tom de voz**: empático, acolhedor, educativo e inspirador. Sem promessas mágicas, sem "milagres em X dias".
- **Promessa**: "Emagrecimento de verdade, com tecnologia eficiente e comunicação transparente."

## Tokens de cor

```css
:root {
  /* Primárias da marca — uso em logo, CTAs, títulos e destaques */
  --sf-green: #ACC435;     /* Verde Soufit (HEX ACC435) */
  --sf-blue:  #4E93D1;     /* Azul Soufit (HEX 4E93D1) */

  /* Secundárias — fundos, textos, contraste */
  --sf-offwhite: #F3F1F1;  /* Off-white principal */
  --sf-dark:     #302F2D;  /* Preto/cinza-grafite oficial */

  /* Subtons (gerados de cor primária até offwhite) */
  --sf-green-soft: #d6e58c;
  --sf-green-mute: #ebf2c6;
  --sf-blue-soft:  #a7c6e8;
  --sf-blue-mute:  #d4e3f3;

  /* Gradiente único permitido (apenas entre primárias) */
  --sf-gradient-primary: linear-gradient(180deg, #4E93D1 0%, #ACC435 100%);

  /* Apoio funcional */
  --sf-text-muted: #6b6b6b;
  --sf-border-soft: rgba(48, 47, 45, 0.12);
  --sf-shadow-card: 0 15px 80px rgba(0, 0, 0, 0.10);

  /* Aliases legados (compat com a landing original do Fit Moderno) */
  --fm-brand: var(--sf-green);
  --fm-black: var(--sf-dark);
  --fm-white: #ffffff;
  --fm-gray-bg: var(--sf-offwhite);
}
```

### Regras de uso das cores

- **Logo Soufit**: apenas em verde, azul, preto (`--sf-dark`) ou branco. **Nunca** em outras cores ou sobre fundos verde/azul (perde reconhecimento).
- **Gradiente**: restrito às duas primárias da marca. Proibido em logo.
- **CTAs**: verde sobre fundo claro/escuro, ou azul sobre fundo claro. O preto/grafite também é CTA válido para rótulos.
- **Cores de produto** (ver seção "Paletas de produto"): aplicação **exclusiva** em rótulos e embalagens. Não usar logo nessas cores.

## Paletas de produto

Cores destinadas a rótulos e embalagens — combinam com primárias/secundárias. **Logotipo proibido nessas cores.**

### Linha Saúde

| Produto             | Principal  | Secundária |
|---------------------|------------|------------|
| Vitali Pro          | `#251517`  | `#561920`  |
| MultiVita Homem     | `#2B2D56`  | `#285098`  |
| MultiVita Mulher    | `#CD5588`  | `#DFA3B5`  |
| MultiVita Sênior    | `#606A72`  | `#A2B1BD`  |
| Puro Bronze         | `#CD652E`  | `#DC913D`  |
| Ác. Hialurônico     | `#58428D`  | `#705B9E`  |
| Colágeno Verisol    | `#C63380`  | `#CE609A`  |
| Coenzima Q10        | `#568C40`  | `#8DB863`  |
| Cúrcuma             | `#D3A121`  | `#EBBD30`  |
| Imune AZ            | `#4691CF`  | `#76B8E9`  |
| Magnésio 5em1       | `#3A9C76`  | `#7BB58E`  |
| NAC                 | `#C73D48`  | `#D68280`  |
| Ômega 3             | `#DF9A29`  | `#F1CB3D`  |

### Linha Performance

- Creme base (para todos): `#FDF8DD`

| Produto       | Principal  | Secundária |
|---------------|------------|------------|
| Whey (verde)  | `#53602D`  | `#B0C333`  |
| Whey (chocol.)| `#693F2E`  | `#C7A182`  |
| Whey (morang.)| `#BA3E4F`  | `#DD9997`  |
| Whey (baunil.)| `#BFA125`  | `#EAD478`  |
| BCAA          | `#4E88A2`  | `#69B7DA`  |
| Colágeno      | `#21512F`  | `#7AAE45`  |
| Colágeno (lar)| `#C75C1F`  | `#E09F2F`  |
| Colágeno (uva)| `#351520`  | `#921E38`  |
| Creatina      | `#BA3E4F`  | `#E0A8B8`  |
| L-glutamina   | `#186369`  | `#229EA8`  |
| Pré-treino    | `#D98932`  | `#E6B034`  |
| Pré-treino (r)| `#9E1B46`  | `#CC577A`  |

> Regra de expansão: novos produtos devem seguir a régua harmônica, tendo como valor base o verde da paleta primária Soufit.

## Tipografia

```css
:root {
  --sf-font-display: "Obviously Narrow", "obviously-narrow", sans-serif;
  --sf-font-body:    "Sora", "Archivo", sans-serif;

  /* Aliases legados */
  --fm-font-display: var(--sf-font-display);
  --fm-font-body:    var(--sf-font-body);
}
```

- **Títulos**: `Obviously Narrow Black` (peso máximo, condensado).
- **Subtítulos / nome de produto em rótulo**: `Obviously Narrow Light`.
- **Estilização criativa de títulos**: `Obviously Narrow Super` (preenchido + contorno, OK para campanhas e datas sazonais).
- **Parágrafos, botões, textos descritivos**: família `Sora` (Light para corpo, Bold para botões e destaques).

### Escala de referência

```css
.sf-hero-title {
  font-family: var(--sf-font-display);
  font-weight: 900;          /* Obviously Narrow Black */
  font-size: 85px;
  line-height: 75px;
}

.sf-section-title {
  font-family: var(--sf-font-display);
  font-weight: 900;
  font-size: 42px;
  line-height: 42px;
}

.sf-eyebrow {
  font-family: var(--sf-font-display);
  font-weight: 300;          /* Obviously Narrow Light */
  font-size: 18px;
  letter-spacing: 2px;
}

.sf-body {
  font-family: var(--sf-font-body);
  font-weight: 300;          /* Sora Light */
  font-size: 18px;
  line-height: 1.55;
}

.sf-button-text,
.sf-small-strong {
  font-family: var(--sf-font-body);
  font-weight: 700;          /* Sora Bold */
  font-size: 18px;
}
```

### Regras tipográficas

- Preferir **caixa baixa** iniciando frases com maiúscula. Caixa baixa estilizada (tudo minúsculo) também é permitida.
- Evitar sombras, 3D e distorções (exceto em campanhas/sazonais específicas).
- Sempre garantir leitura e contraste entre os elementos.

### Mobile

```css
@media (max-width: 767px) {
  .sf-hero-title { font-size: 36px; line-height: 1.05; }
  .sf-section-title { font-size: 32px; }
}
```

## Elementos visuais

A marca trabalha com **formas orgânicas e arredondadas** (lembrando o corpo humano e a naturalidade) combinadas com **círculos, elipses e estrelas de 4 pontas**.

- **Cápsulas/pills**: contêineres de tag (`@soufitmoderno`, `2025`, etc.).
- **Elipses verticais** (a "M" estilizada do brand pattern): pano de fundo das capas e cards de seção.
- **Estrelas de 4 pontas (`✦`)**: pontuação visual moderna; usar em pares cercando títulos curtos.
- **Ícones**: linha fina, sem preenchimento, dentro de círculo. Sem cor de fill, só stroke.

## Layout

```css
:root {
  --sf-container-desktop: 1140px;
  --sf-container-tablet: 1024px;
  --sf-container-mobile: 767px;
  --sf-section-gap: 88px;
  --sf-widget-gap: 20px;
  --sf-radius-card: 20px;
  --sf-radius-image: 10px;
  --sf-radius-pill: 9999px;
}

.sf-section { width: 100%; padding-block: var(--sf-section-gap); }
.sf-section--green { background: var(--sf-green); color: var(--sf-dark); }
.sf-section--blue  { background: var(--sf-blue);  color: #fff; }
.sf-section--dark  { background: var(--sf-dark);  color: var(--sf-offwhite); }
.sf-section--light { background: var(--sf-offwhite); color: var(--sf-dark); }
```

## Botões

CTA principal mantém o formato pill com ícone circular à direita. A cor primária do botão pode ser **verde** (geral) ou **azul** (educacional/Sábio).

```css
.sf-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  background: var(--sf-green);
  color: var(--sf-dark);
  font-family: var(--sf-font-body);
  font-weight: 700;          /* Sora Bold */
  font-size: 18px;
  border: 0;
  border-radius: var(--sf-radius-pill);
  padding: 22px 110px 22px 28px;
  text-decoration: none;
  z-index: 1;
}

.sf-button--blue    { background: var(--sf-blue); color: #fff; }
.sf-button--outline {
  background: transparent;
  color: var(--sf-dark);
  border: 1.5px solid currentColor;
  padding-right: 28px;
}

.sf-button-icon {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1px solid currentColor;
  background: transparent;
}
```

## Cards e rótulos

### Cards de conteúdo

```css
.sf-card {
  background: #fff;
  color: var(--sf-dark);
  border-radius: var(--sf-radius-card);
  box-shadow: var(--sf-shadow-card);
  padding: 28px;
}

.sf-card--dark { background: var(--sf-dark); color: var(--sf-offwhite); }
.sf-card--green { background: var(--sf-green); color: var(--sf-dark); }
.sf-card--blue  { background: var(--sf-blue);  color: #fff; }

.sf-pill {
  display: inline-flex;
  align-items: center;
  border-radius: var(--sf-radius-pill);
  border: 1.5px solid currentColor;
  padding: 8px 18px;
  font-family: var(--sf-font-body);
  font-weight: 700;
  font-size: 14px;
}
```

### Rótulos padrão (linha)

Anatomia para produtos que pertencem a uma linha (Saúde / Performance):

1. **Assinatura**: logotipo Soufit em pílula escura no topo.
2. **Nome do produto**: `Obviously Narrow Light` (sub-categoria, ex.: "beauty") + `Obviously Narrow Super` (nome forte, ex.: "bronze") empilhados.
3. **Descrição**: `Sora Bold` — "Suplemento alimentar em cápsulas".
4. **Tag de ativo**: pílula com `Sora Bold` (ex.: "BETACAROTENO + L-TIROSINA").
5. **Destaques**: lista com check + `Obviously Narrow Light`.
6. **Cores**: cor de produto + paleta principal Soufit.

### Rótulos independentes

Produtos com identidade própria (ex.: ChocoTox) podem usar logotipo, fontes e paletas exclusivas, **desde que mantenham**:

- A assinatura Soufit em pílula no topo.
- A família `Sora` em todos os textos descritivos.

## Ícones e elementos auxiliares

- Construção apenas com linhas (`stroke-width` constante), sem preenchimento.
- Dentro de círculos com mesma `stroke`.
- Tamanhos comuns: 24px (inline), 52px (lista de benefícios), 80–130px (decorativo).
- Estrela de 4 pontas (`✦`) é o "selo" decorativo da marca — sempre como acento, nunca como protagonista.

## Voz de marca

### Como falamos

- **Empáticos**: "Nós te entendemos." / "Sabemos que a rotina é corrida."
- **Educacionais e transparentes**: explicar a ciência por trás dos produtos de forma simples.
- **Motivacionais, mas realistas**: incentivar consistência, não perfeição.
- **Acolhedores**: criar senso de comunidade.

### Como NÃO falamos

- ✗ "Perca 10kg em uma semana!" / "Fórmula mágica."
- ✗ Linguagem técnica em excesso ou jargão científico.
- ✗ "Não desista!" / "Seja forte!" (motivação agressiva).
- ✗ Tom de superioridade ou "solução única".
- ✗ Foco em estética isolada — Soufit fala de saúde integral.

## Regras de aplicação

- **Logo**: nunca distorcer, contornar, sombrear, rotacionar ou aplicar gradiente. Manter `2x` de margem de proteção.
- **Cor de logo**: somente verde, azul, preto (`#302F2D`) ou branco — nunca cores de produto.
- **Gradiente**: somente entre as duas primárias e em fundos/elementos, nunca em logo nem em texto corrido.
- **Tipografia**: `Obviously` para títulos e destaques; `Sora` para qualquer texto funcional.
- **CTAs**: pill arredondado, ícone circular à direita, texto em `Sora Bold`.
- **Cards**: raio `20px`; imagens internas `10px`; sem bordas pesadas.
- **Mobile**: laterais de `20px`, colunas empilhadas, títulos próximos de `32–36px`.
- **Foto**: pessoas reais, luz natural, sorrisos genuínos. Evitar estética "antes/depois agressiva" — preferir "rotina possível".

## Compat / Migração da landing Fit Moderno

A landing antiga usa tokens `--fm-*` e CTA preto/verde-lima (#A1C41E). Para alinhar ao novo padrão:

1. Substituir `#A1C41E` por `var(--sf-green)` (`#ACC435`) gradualmente — diferença ~2% de matiz, não quebra layout.
2. Trocar `Archivo` por `Sora` na próxima revisão do CSS.
3. Em novas seções, introduzir o azul `#4E93D1` como cor secundária de ênfase (sub-cabeçalhos, ícones de seção educacional).
4. Manter logo Soufit, mas garantir que apareça em verde sobre fundo claro/escuro — nunca sobre verde ou azul.
