# Ferzion

Landing page institucional + API de captação de leads da **Ferzion** — software sob
medida para operações com propósito (agronegócio, logística e gestão operacional).

O repositório reúne dois projetos independentes:

| Projeto | Pasta | Stack |
|---|---|---|
| **Backend** — API de leads | [`backend/`](backend/) | Django 6 · Django REST Framework · Python 3.14 |
| **Frontend** — site estático | [`frontend/`](frontend/) | HTML · CSS · JavaScript (vanilla, sem build step) |

---

## 📁 Estrutura

```
Ferzion/
├── backend/                  # API Django
│   ├── config/               # settings, urls, wsgi/asgi
│   ├── leads/                # app de captação de leads (models, views, serializers, services)
│   ├── templates/emails/     # template de e-mail de confirmação
│   ├── manage.py
│   ├── requirements.txt      # dependências Python
│   └── .env.example          # modelo de variáveis de ambiente
├── frontend/                 # site estático
│   ├── assets/               # logo, favicons, og-image
│   ├── index.html            # página única (HTML/CSS/JS inline)
│   ├── robots.txt
│   ├── sitemap.xml
│   └── site.webmanifest
├── .claude/                  # configuração do Claude Code (skills, settings, contexto)
├── CLAUDE.md                 # instruções para o Claude Code
└── README.md
```

---

## 🔧 Backend (Django)

Todos os comandos rodam **de dentro de `backend/`** com a virtualenv ativada.

### Primeira configuração

```bash
cd backend
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # preencha as variáveis (veja abaixo)
python manage.py migrate
python manage.py createsuperuser     # opcional — acesso ao /admin
```

### Rodar e testar

```bash
source .venv/bin/activate
python manage.py runserver           # API em http://localhost:8000
python manage.py test                # suíte de testes
```

### Endpoint principal

`POST /api/leads/` — recebe o formulário de contato do site.
Campos: `nome`, `email`, `whatsapp`, `segmento`, `desafio`.
Ao criar um lead, a API registra IP/User-Agent e dispara um e-mail de confirmação.

---

## 🎨 Frontend (site estático)

Não há build step. O site é uma única página (`index.html`) com CSS e JavaScript
inline — todo o design system (cores `--ink-*` / `--bone-*` / `--mint-*`, tipografia,
breakpoints em 1024/768/480px) é definido no `<style>` do próprio arquivo.

```bash
cd frontend
python -m http.server 8001           # site em http://localhost:8001
```

O formulário de contato deve enviar `POST` para o endpoint `/api/leads/` do backend.

---

## 🔑 Variáveis de ambiente

O backend exige um arquivo `backend/.env` (use `backend/.env.example` como modelo):

| Variável | Descrição |
|---|---|
| `DJANGO_SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | `True` em dev, `False` em produção |
| `EMAIL_HOST` · `EMAIL_PORT` · `EMAIL_USE_TLS` | SMTP de envio (Gmail) |
| `EMAIL_HOST_USER` | Conta de e-mail remetente |
| `EMAIL_HOST_PASSWORD` | **Gmail App Password** — não a senha da conta |
| `DEFAULT_FROM_EMAIL` | Remetente exibido nos e-mails |

> ⚠️ `EMAIL_HOST_PASSWORD` precisa ser uma **Gmail App Password**. Sem isso, o e-mail
> de confirmação de lead falha. O `.env` nunca é versionado (está no `.gitignore`).

---

## 🚀 Deploy

- **Backend:** servir com `gunicorn config.wsgi:application`. Em plataformas como
  Render/Railway/Heroku, configure o **root directory como `backend/`** — assim o
  build encontra `requirements.txt` e o start command fica `gunicorn config.wsgi`.
  Em produção: `DEBUG=False`, banco PostgreSQL (o `psycopg` já está nas dependências)
  e restrinja o CORS (`CORS_ALLOW_ALL_ORIGINS=True` é apenas para desenvolvimento).
- **Frontend:** publicar os arquivos estáticos de `frontend/` em qualquer CDN ou
  servidor web (Nginx, Netlify, Cloudflare Pages, etc.).

---

## 🌿 Fluxo de trabalho (Git)

Crie um branch por mudança e abra um Pull Request contra `main`. Não commite
direto na `main`. Mensagens de commit, comentários e conteúdo em **português (pt-BR)**.

---

## 🧱 Stack

| Camada | Tecnologias |
|---|---|
| Backend | Python 3.14 · Django 6 · Django REST Framework · Gunicorn |
| Banco | SQLite (dev) · PostgreSQL (produção) |
| Frontend | HTML5 · CSS3 · JavaScript ES6+ (vanilla) |
| Tipografia | Instrument Serif · Manrope · JetBrains Mono |
| Analytics | Google Analytics 4 |

---

*Ferzion · Software sob medida para operações com propósito · ferzion.com.br*
