import glob, os, re

files = [
    'sobre.html', 'sobre-nexxus.html',
    'servicos.html', 'servicos-nexxus.html',
    'contato.html', 'contato-nexxus.html',
    'blog.html', 'blog-nexxus.html',
    'artigo.html', 'artigo-nexxus.html',
    'links.html',
    'por-que-terceirizar-operacao-comercial.html',
    'quantas-reunioes-sdr-por-mes.html',
    'quanto-custa-terceirizar-time-de-vendas.html',
    'quem-fecha-a-venda-prospeccao-terceirizada.html',
    'tendencias-mercado-comercial-b2b.html',
    'terceirizar-ou-estruturar-comercial-interno.html'
]

for f in files:
    if os.path.exists(f):
        content = open(f, encoding='utf-8').read()
        gf = re.search(r'(?:<!--\s*Google Fonts:[^>]*-->\s*)?(?:<link rel="preconnect"[^>]*>\s*){0,3}<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">', content)
        tf = re.search(r'fontFamily:\s*\{[^}]+\},', content)
        h1 = re.search(r'h1,\s*h2[^{]*\{[^}]+\}', content)
        print(f"{f:45} | GF: {bool(gf)} | TF: {bool(tf)} | H1: {bool(h1)}")
    else:
        print(f"{f:45} | NOT FOUND")
