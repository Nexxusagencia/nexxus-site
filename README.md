# Nexxus — Plataforma Institucional & Engenharia Comercial B2B

Este repositório contém o código-fonte completo do novo site institucional da **Nexxus Agência Comercial**, construído com arquitetura em Python / Flask, estilização moderna Tailwind CSS em Glassmorphism, animações vetoriais e shader interativo WebGL.

---

## 🚀 Tecnologias Utilizadas

- **Backend / Servidor**: Python 3.10+ & Flask Framework.
- **Frontend / Styling**: HTML5, Vanilla CSS, Tailwind CSS CDN (com tokens customizados Nexxus Obsidian Glass).
- **Iconografia**: Iconify Icons (Solar & Line-MD Icons).
- **Motores Visuais**: WebGL Starfield Shader Canvas (`#webgl-stars`), Cursor Neonisado Interativo, Scroll Reveal Observer, Simulador de ROI B2B em Pop-up Modal e Accordion FAQ.
- **Tipografia**: Plus Jakarta Sans (Headlines 800, Cards/Subtítulos 700, Subheadlines 500, Body) e JetBrains Mono (Métricas e Código).

---

## 📂 Páginas Principais & Rotas

1. **Home (`/`)**: Abertura institucional, vídeo de fundo, seções O Problema, Soluções, Diferenciais, Metodologia, Calculadora de ROI e FAQ.
2. **Sobre a Nexxus (`/sobre`)**: 8 seções institucionais contando a história, o posicionamento B2B, a visão e os valores da agência.
3. **Serviços (`/servicos`)**: 12 seções detalhando Terceirização Comercial (BPO), Estruturação Interna, Mentoria Comercial e Soluções com Inteligência Artificial.
4. **Blog & Artigos (`/blog`, `/blog/<slug>`)**: Hub de conteúdo e inteligência comercial B2B com filtros por categoria, artigos pré-renderizados Jamstack, barra de leitura e artigos relacionados.
5. **Contato (`/contato`)**: Página de atendimento consultivo com formulário completo (`id="formulario"`), localização no Edifício Capital Corporate Office em SP e modo de demonstração ativado (`FORM_CONTACT_MODE = 'demo'`).
6. **Central de Links (`/links`)**: Hub com links rápidos para WhatsApp, Instagram, LinkedIn e páginas da agência.

---

## 🛠️ Como Executar o Projeto Localmente

### 1. Criar e Ativar o Ambiente Virtual (`.venv`):
```bash
# No Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# No Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar as Dependências:
```bash
pip install -r requirements.txt
```

### 3. Iniciar o Servidor Flask:
```bash
python app.py
```

### 4. Acessar no Navegador:
Abra o navegador em `http://localhost:5000` (ou `http://127.0.0.1:5000`).

---

## 🔒 Modo de Demonstração do Formulário de Contato (`FORM_CONTACT_MODE`)

O formulário da página Contato foi configurado em **Modo Demonstração** (`window.FORM_CONTACT_MODE = 'demo'`).

- **Comportamento em Modo Demo**: Valida o preenchimento, simula o tempo de carregamento e exibe a mensagem de demonstração (*"Formulário preenchido com sucesso. O envio real será ativado após a publicação do site."*), preservando os campos preenchidos na tela sem disparar webhooks ou abrir o WhatsApp automaticamente.
- **Ativação em Produção Futura**: Para integrar com Kommo CRM, Make, n8n ou SMTP de e-mail, altere a variável para `window.FORM_CONTACT_MODE = 'production'` e defina a rota `/api/contact` no `app.py`.

---

## 📄 Documentação Adicional na Pasta `/docs`

- [`docs/PROJECT_STRUCTURE.md`](docs/PROJECT_STRUCTURE.md): Explicação detalhada de cada diretório e arquivo.
- [`docs/ROUTES.md`](docs/ROUTES.md): Matriz de rotas Flask, arquivos correspondentes, links de cabeçalho e rodapé.
- [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md): Instruções de publicação e variáveis de ambiente.
