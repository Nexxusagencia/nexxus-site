# Estrutura Detalhada do Projeto Nexxus

Esta documentação descreve a organização técnica dos arquivos do projeto.

```
NEXXUS-REDESIGN/
├── app.py                      # Servidor backend Flask e mapeamento de rotas
├── requirements.txt            # Dependências Python (Flask)
├── README.md                   # Manual principal do projeto
├── .gitignore                  # Arquivos ignorados pelo Git (.venv, caches, etc.)
├── .env.example                # Modelo de variáveis de ambiente para produção
│
├── index-nexxus.html           # Template canônico da Home (servido em / e /index-nexxus.html)
├── index.html                  # Alias sincronizado da Home
├── sobre-nexxus.html           # Template canônico da página Sobre (servido em /sobre)
├── sobre.html                  # Alias sincronizado da página Sobre
├── servicos-nexxus.html        # Template canônico da página Serviços (servido em /servicos)
├── servicos.html               # Alias sincronizado da página Serviços
├── contato-nexxus.html         # Template canônico da página Contato (servido em /contato)
├── contato.html                # Alias sincronizado da página Contato
│
├── public/                     # Diretório de mídias organizadas do projeto
│   └── images/
│       ├── sobre/              # Fotografias corporativas exclusivas da página Sobre
│       ├── servicos/           # Fotografias corporativas exclusivas da página Serviços
│       └── contato/            # Fotografias corporativas da página Contato
│
├── docs/                       # Documentação técnica para manutenção e IAs
│   ├── PROJECT_STRUCTURE.md    # Inventário da estrutura (este arquivo)
│   ├── ROUTES.md               # Mapeamento de rotas e navegação
│   └── DEPLOYMENT.md           # Guia de publicação e hospedagem
│
└── _archive/                   # Arquivos temporários e quarentena de desenvolvimento
    ├── temporary-development-files/ # Scripts utilitários Python de desenvolvimento
    └── pending-deletion/       # Quarentena de arquivos para revisão futura
```
