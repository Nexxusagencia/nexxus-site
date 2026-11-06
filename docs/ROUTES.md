# Matriz de Rotas & Links de Navegação

Este documento descreve as rotas ativas no backend Flask (`app.py`), seus arquivos correspondentes e as conexões de cabeçalho e rodapé.

---

## 🗺️ Tabela de Rotas Flask

| Rota HTTP | Arquivo Servido | Descrição |
| :--- | :--- | :--- |
| `/` | `index-nexxus.html` | Página Inicial (Home) |
| `/index-nexxus.html` | `index-nexxus.html` | Rota direta estática da Home |
| `/sobre` | `sobre-nexxus.html` | Página Institucional "Sobre a Nexxus" |
| `/sobre.html` | `sobre-nexxus.html` | Alias estático da página Sobre |
| `/sobre-nexxus.html` | `sobre-nexxus.html` | Rota direta da página Sobre |
| `/servicos` | `servicos-nexxus.html` | Página de Soluções e Serviços |
| `/servicos.html` | `servicos-nexxus.html` | Alias estático da página Serviços |
| `/servicos-nexxus.html` | `servicos-nexxus.html` | Rota direta da página Serviços |
| `/contato` | `contato-nexxus.html` | Página de Atendimento & Formulário |
| `/contato.html` | `contato-nexxus.html` | Alias estático da página Contato |
| `/contato-nexxus.html` | `contato-nexxus.html` | Rota direta da página Contato |
| `/blog` | `blog-nexxus.html` | Hub Principal do Blog e Artigos |
| `/blog.html` | `blog-nexxus.html` | Alias estático do Blog |
| `/blog/<slug>` | `<slug>.html` / `artigo.html` | Rota amigável direta para artigos individuais |
| `/artigo` | `artigo.html` | Template dinâmico para leitura de artigos |
| `/links` | `links.html` | Central de Links Institucionais |
| `/api/calculate-roi` | *Backend Endpoint* | API POST para cálculo do Simulador de ROI |

---

## 🔗 Links de Navegação nos Cabeçalhos e Rodapés

- **Home**: Aponta para `index-nexxus.html` (`/`).
- **Sobre**: Aponta para `sobre-nexxus.html` (`/sobre`).
- **Serviços**: Aponta para `servicos-nexxus.html` (`/servicos`).
- **Blog**: Aponta para `blog-nexxus.html` (`/blog`).
- **Contato**: Aponta para `contato-nexxus.html` (`/contato`).
- **Links**: Aponta para `links.html` (`/links`).
- **CTAs Comerciais de Diagnóstico**: Apontam para `contato-nexxus.html#formulario` (`/contato#formulario`).
