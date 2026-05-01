# Ferzion — Landing Page · Handoff para Desenvolvedor

> Versão: **v3** · Data: maio 2025  
> Arquivo principal: `Ferzion Landing Page v3.html`

---

## 📁 Estrutura de Arquivos

```
handoff/
├── Ferzion Landing Page v3.html   ← Arquivo principal (autocontido)
├── assets/
│   └── logo-ferzion.jpeg          ← Logo da empresa (substituir por PNG transparente)
├── tweaks-panel.jsx               ← Componente React do painel de tweaks (dependência)
└── README.md                      ← Este arquivo
```

---

## 🚀 Como usar

O arquivo `Ferzion Landing Page v3.html` é **quase autocontido** — depende de:

1. **`assets/logo-ferzion.jpeg`** — logo da empresa (caminho relativo)
2. **`tweaks-panel.jsx`** — painel de tweaks (só necessário em desenvolvimento/design; pode ser removido na versão final de produção)
3. **Google Fonts** (CDN) — Playfair Display + DM Sans
4. **React 18 + Babel** (CDN) — apenas para o painel de Tweaks

> **Para deploy em produção:** remova o bloco de Tweaks (React, Babel, `#tweaks-root` e o `<script type="text/babel">`) para eliminar dependências desnecessárias e melhorar performance.

---

## 🎨 Design System

### Paleta de Cores

| Token | HEX | Uso |
|---|---|---|
| `--bg-deep` | `#071A12` | Fundo principal das seções dark |
| `--bg-mid` | `#0F2D23` | Cards, navbar, containers elevados |
| `--bg-light` | `#F2EBDD` | Seções de contraste (Problema, FAQ, Processo) |
| `--bg-subtle` | `#D9CFBE` | Bordas em seções light, hover states |
| `--text-primary` | `#F2EBDD` | Texto principal em fundos dark |
| `--text-dark` | `#1A1A1A` | Texto principal em fundos light |
| `--text-muted` | `#8A9E95` | Subtextos, labels, metadados |
| `--accent` | `#58E1A8` | CTA primário, highlights, bordas ativas |
| `--accent-teal` | `#4CA7A1` | Elementos secundários, ícones técnicos |
| `--border-dark` | `#1E3D2F` | Bordas em contexto dark |

### Tipografia

| Papel | Fonte | Pesos | Uso |
|---|---|---|---|
| Display | Playfair Display | 600, 700 (+ italic 600) | Títulos H1, H2, H3 |
| Corpo | DM Sans | 300, 400, 500 | Texto corrido, labels, UI |

**Escalas de tamanho:**
- H1: `clamp(40px, 5.5vw, 72px)`
- H2: `clamp(28px, 3.5vw, 48px)`
- H3: `22px`
- Corpo base: `17px` (ajustável via `font-size` no `:root`)
- Labels/tags: `11px`, `font-weight: 500`, `letter-spacing: 0.1em`, `text-transform: uppercase`

### Espaçamento

| Componente | Valor |
|---|---|
| Padding de seções | `120px 0` (desktop) / `80px 0` (mobile) |
| Container max-width | `1200px` |
| Padding lateral container | `48px` (desktop) / `20px` (mobile) |
| Gap de cards | `20px` |
| Padding interno de cards | `36–40px` |
| Altura da navbar | `72px` |

### Border Radius

| Elemento | Valor |
|---|---|
| Cards principais | `16px` |
| Botões | `8px` |
| Pills/tags | `999px` |
| Inputs do formulário | `8px` |

---

## 📐 Estrutura de Seções

| # | ID | Fundo | Descrição |
|---|---|---|---|
| 1 | `#navbar` | `#071A12` (blur on scroll) | Navbar fixa, blur ao scroll |
| 2 | `#hero` | `#071A12` | Hero 60/40 com dashboard mockup 3D |
| 3 | `#problema` | `#F2EBDD` | 5 pain cards em grid |
| 4 | `#solucao` | `#071A12` | 3 diferenciais + métricas |
| 5 | `#cases` | `#0F2D23` | Grid 2×2 de sistemas entregues |
| 6 | `#processo` | `#F2EBDD` | Timeline vertical de 4 etapas |
| 7 | `#tech` | `#071A12` | Benefícios + stack técnico |
| 8 | `#faq` | `#F2EBDD` | Accordion com 5 perguntas |
| 9 | `#sobre` | `#071A12` | Manifesto + 3 stat cards |
| 10 | `#cta-final` | `#0F2D23` | CTA split + formulário |
| 11 | `#footer` | `#071A12` | Grid 4 colunas + social |

---

## ⚙️ Funcionalidades JavaScript (Vanilla)

Todas implementadas em JS puro, sem frameworks. Localizadas no bloco `<script>` no final do `<body>`.

| Funcionalidade | Implementação |
|---|---|
| Navbar blur on scroll | `IntersectionObserver` / `window.scroll` |
| Mobile drawer | Toggle de classes + overlay |
| Scroll reveal | `IntersectionObserver` com `translateY + opacity` |
| FAQ accordion | `max-height` animado + rotação da seta |
| Máscara de telefone | Input listener com regex |
| Validação do formulário | Validação client-side com feedback visual |
| Cursor customizado | `mousemove` + `requestAnimationFrame` com lag |
| Contador animado | `IntersectionObserver` + easing cúbico |
| Scroll progress bar | `window.scroll` → `width %` |
| Active nav links | `IntersectionObserver` por seção |
| Smooth anchor scroll | `window.scrollTo` com offset da navbar |

---

## 📱 Breakpoints Responsivos

| Breakpoint | Comportamento |
|---|---|
| `> 1024px` | Layout completo desktop |
| `≤ 1024px` | Container comprime, footer mantém 4 cols com menor gap |
| `≤ 768px` | Stack vertical em todas as seções, hamburger menu, footer 2 cols |
| `≤ 480px` | Footer 1 coluna |

---

## 📬 Contatos configurados

| Canal | Valor |
|---|---|
| Email | ferzion.dev@gmail.com |
| WhatsApp | +55 94 9 9208-3253 (`wa.me/559492083253`) |
| LinkedIn | linkedin.com/company/ferzion |

> **Atenção:** O formulário de contato faz validação client-side mas **não tem backend**. É necessário integrar um serviço de envio de e-mails (ex: Formspree, EmailJS, ou endpoint próprio em Django/Python).

---

## 🔧 Recomendações para produção

### 1. Formulário de contato
Integrar o `<form id="contact-form">` com um backend. Sugestões:
- **Formspree** (`action="https://formspree.io/f/SEU_ID"`) — sem backend necessário
- **EmailJS** — envio direto do front-end
- **Endpoint Django** — já que o stack é Python/Django

Substituir o `form.addEventListener('submit', ...)` pelo envio real via `fetch()`.

### 2. Logo em PNG transparente
Substituir `assets/logo-ferzion.jpeg` por um PNG com fundo transparente. O CSS atual usa `filter: brightness(0) invert(1)` para deixar o logo branco — com PNG transparente o resultado será muito mais limpo.

### 3. Remover Tweaks em produção
O painel de Tweaks (React + Babel via CDN) adiciona ~300KB desnecessários em produção. Para remover:
1. Remover as 3 tags `<script>` de React, ReactDOM e Babel no `<head>`
2. Remover `<div id="tweaks-root"></div>`
3. Remover `<script type="text/babel" src="tweaks-panel.jsx"></script>`
4. Remover o `<script type="text/babel">` com o componente `TweaksApp`
5. Deletar `tweaks-panel.jsx`

### 4. Performance
- Adicionar `font-display: swap` já está implícito via Google Fonts URL
- Considerar hospedar as fontes localmente para eliminar dependência externa
- O dashboard mockup do hero é 100% CSS/HTML — zero imagens externas

### 5. SEO básico
Adicionar no `<head>`:
```html
<meta name="description" content="Ferzion — Software sob medida para operações reais. Sistemas personalizados para agronegócio, logística e gestão operacional.">
<meta property="og:title" content="Ferzion — Software sob medida para operações reais">
<meta property="og:description" content="Criamos sistemas personalizados que eliminam o caos operacional.">
<meta property="og:image" content="URL_DA_OG_IMAGE">
<link rel="canonical" href="https://dev.ferzion.com.br">
```

### 6. Analytics
Adicionar Google Analytics 4 ou Plausible antes do `</head>`.

---

## 🖼️ Assets necessários para produção

| Asset | Status | Ação necessária |
|---|---|---|
| Logo PNG transparente | ⚠️ Pendente | Substituir `assets/logo-ferzion.jpeg` |
| OG Image (1200×630px) | ⚠️ Pendente | Criar para compartilhamento em redes sociais |
| Favicon | ⚠️ Pendente | Adicionar `<link rel="icon">` no `<head>` |

---

## 🏗️ Stack técnico do site

| Tecnologia | Versão | Uso |
|---|---|---|
| HTML5 | — | Estrutura |
| CSS3 | — | Estilo (Grid, Flexbox, Custom Properties, Animations) |
| JavaScript | Vanilla ES6+ | Todas as interações |
| React | 18.3.1 | Apenas Tweaks Panel (remover em produção) |
| Babel Standalone | 7.29.0 | Transpile JSX do Tweaks Panel (remover em produção) |
| Google Fonts | — | Playfair Display + DM Sans |

---

## 📞 Dúvidas

Contato do designer responsável pelo protótipo via projeto Ferzion no Claude.

---

*Ferzion · Software sob medida para operações reais · ferzion.dev@gmail.com*
