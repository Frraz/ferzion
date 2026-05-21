---
name: dev
description: Sobe os dois servidores de desenvolvimento da Ferzion ao mesmo tempo — backend Django em :8000 e frontend estático em :8001. Use quando o usuário pedir para "rodar o projeto", "subir os servidores" ou testar localmente.
---

Suba os dois servidores de desenvolvimento em background:

1. **Backend (Django, porta 8000)** — rode em background:
   ```
   cd backend && source .venv/bin/activate && python manage.py runserver
   ```
   Antes, confira se `backend/.env` existe; se não, avise o usuário para criá-lo a partir de `backend/.env.example`.

2. **Frontend (estático, porta 8001)** — rode em background a partir de `frontend/`:
   ```
   python -m http.server 8001
   ```

Depois de iniciar os dois, informe ao usuário:
- Frontend: http://localhost:8001
- Backend/API: http://localhost:8000

Se alguma porta já estiver em uso, avise em vez de tentar matar o processo existente.