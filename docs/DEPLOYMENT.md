# Guia de Publicação e Deploy

Este documento orienta o processo de hospedagem e publicação do projeto da Nexxus.

---

## 🛠️ Requisitos de Hospedagem

- **Python**: 3.10 ou superior.
- **Servidor Web**: Gunicorn / uWSGI com Nginx (ou serviços PaaS como Render, Vercel, Railway ou Heroku).

---

## ⚙️ Variáveis de Ambiente (`.env`)

Crie o arquivo `.env` no servidor de produção com base no `.env.example`:

```env
FLASK_ENV=production
PORT=5000
FORM_CONTACT_MODE=demo
```

---

## 🚀 Comando de Inicialização para Produção (Gunicorn)

```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```
