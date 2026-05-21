# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Landing page + API de captação de leads da Ferzion. Dois projetos no mesmo repositório:
- `backend/` — API Django (Django 6, Django REST Framework). App principal: `leads/`.
- `frontend/` — site estático (HTML/CSS/JS puro). Tudo num único `index.html`, sem build step.

## Idioma

Escreva comentários de código, mensagens de commit e conteúdo do site em **português (pt-BR)**.

## Backend (Django)

Comandos rodam de dentro de `backend/` com a virtualenv ativada:

```
cd backend && source .venv/bin/activate
python manage.py runserver        # dev server em :8000
python manage.py migrate
python manage.py test
```

- `.env` é obrigatório (veja `backend/.env.example`). `EMAIL_HOST_PASSWORD` precisa ser uma **Gmail App Password**, não a senha da conta — o envio de e-mail de confirmação de lead falha sem isso.
- `CORS_ALLOW_ALL_ORIGINS=True` é só para desenvolvimento; restrinja em produção.

## Frontend

- Site estático, **sem build step**. Para rodar localmente: `cd frontend && python -m http.server 8001`.
- Todo o design system (cores `--ink-*`/`--bone-*`/`--mint-*`, tipografia, breakpoints em 1024/768/480px) é definido inline no `<style>` de `index.html`. Edite os tokens lá; não crie arquivos CSS separados sem combinar antes.
- O formulário de contato deve enviar POST para o endpoint Django `/api/leads/` (o JavaScript do `index.html` ainda precisa ser ligado a essa URL).

## Git

Crie um branch por mudança e abra um PR contra `main`. Não commite direto na `main`.