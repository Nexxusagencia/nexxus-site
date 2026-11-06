import os
import re
import shutil
import zipfile

BASE_DIR = r"e:\00-NEXXUS\Site - Copia\NEXXUS-REDESIGN"
PREVIEW_DIR = os.path.join(BASE_DIR, "preview-cliente")

GOOGLE_FONTS_NEW = """  <!-- Google Fonts: Plus Jakarta Sans (Modern Geometric Sans) & JetBrains Mono (Code/Metrics) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">"""

def update_html_content(content):
    # 1. Replace Google Fonts link block containing Anton or Oswald
    content = re.sub(
        r'<!--\s*Google Fonts:[^>]*-->\s*<link rel="preconnect"[^>]*>\s*<link rel="preconnect"[^>]*>\s*<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">',
        GOOGLE_FONTS_NEW,
        content
    )
    content = re.sub(
        r'<link rel="preconnect"[^>]*>\s*<link rel="preconnect"[^>]*>\s*<link href="https://fonts\.googleapis\.com/css2\?[^"]*(?:Anton|Oswald)[^"]*" rel="stylesheet">',
        GOOGLE_FONTS_NEW,
        content
    )
    content = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*(?:Anton|Oswald)[^"]*" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">',
        content
    )

    # 2. Replace Tailwind fontFamily config
    # heading: ['Anton', 'Oswald', 'sans-serif'] or heading: ['Oswald', 'sans-serif']
    content = re.sub(
        r"heading:\s*\[['\"](?:Anton['\"],\s*['\"]Oswald|Oswald)['\"],\s*['\"]sans-serif['\"]\]",
        "heading: ['Plus Jakarta Sans', 'Inter', 'sans-serif']",
        content
    )
    # sans: ['Nexa', 'Plus Jakarta Sans', ...]
    content = re.sub(
        r"sans:\s*\[['\"]Nexa['\"],\s*['\"]Plus Jakarta Sans['\"],\s*['\"]Inter['\"],\s*['\"]sans-serif['\"]\]",
        "sans: ['Plus Jakarta Sans', 'Inter', 'sans-serif']",
        content
    )
    content = re.sub(
        r"sans:\s*\[['\"]Nexa['\"],\s*['\"]Plus Jakarta Sans['\"],\s*['\"]sans-serif['\"]\]",
        "sans: ['Plus Jakarta Sans', 'Inter', 'sans-serif']",
        content
    )

    # 3. Replace CSS rules for h1, h2
    # Anton/Oswald for h1, h2 in main pages:
    content = re.sub(
        r"/\*\s*Brandbook 2026 Typography[^/]*\*/\s*h1,\s*h2,\s*\.main-title,\s*\.title-bold\s*\{[^}]*font-family:\s*['\"](?:Anton|Oswald)[^}]*\}",
        """/* Tipografia Moderna Geometica (Plus Jakarta Sans) - Alta Legibilidade e Estetica SaaS Premium */
    h1, h2, .main-title, .title-bold {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
      font-weight: 800 !important;
      letter-spacing: -0.025em;
      line-height: 1.15 !important;
    }""",
        content
    )
    content = re.sub(
        r"h1,\s*h2,\s*\.main-title,\s*\.title-bold\s*\{[^}]*font-family:\s*['\"](?:Anton|Oswald)[^}]*\}",
        """h1, h2, .main-title, .title-bold {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
      font-weight: 800 !important;
      letter-spacing: -0.025em;
      line-height: 1.15 !important;
    }""",
        content
    )

    # For blog posts with simple h1, h2 and h3, h4:
    content = re.sub(
        r"h1,\s*h2\s*\{[^}]*font-family:\s*['\"](?:Anton|Oswald)[^}]*\}",
        "h1, h2 { font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important; font-weight: 800 !important; text-transform: uppercase; letter-spacing: -0.025em; line-height: 1.2 !important; }",
        content
    )
    content = re.sub(
        r"h3,\s*h4\s*\{[^}]*font-family:\s*['\"](?:Anton|Oswald)[^}]*\}",
        "h3, h4 { font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important; font-weight: 700 !important; text-transform: uppercase; letter-spacing: -0.015em; line-height: 1.28 !important; }",
        content
    )

    # For preview-cliente/index.html Oswald styles:
    content = re.sub(
        r"/\*\s*Typography Rules: Títulos em Oswald[^/]*\*/\s*h1\s*\{[^}]*\}\s*h2\s*\{[^}]*\}\s*h3\s*\{[^}]*\}\s*h4,\s*h5,\s*h6\s*\{[^}]*\}",
        """/* Tipografia Moderna Geometrica (Plus Jakarta Sans) */
    h1, h2, .main-title, .title-bold {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
      font-weight: 800 !important;
      letter-spacing: -0.025em;
      line-height: 1.15 !important;
    }
    h3, h4, h5, h6, .card-title {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
      font-weight: 700 !important;
      letter-spacing: -0.015em;
      line-height: 1.28 !important;
    }""",
        content
    )

    # h3, h4, h5, h6 in main pages
    content = re.sub(
        r"h3,\s*h4,\s*h5,\s*h6,\s*\.card-title\s*\{[^}]*font-family:\s*['\"](?:Nexa['\"],\s*['\"]Plus Jakarta Sans|Plus Jakarta Sans)[^}]*\}",
        """h3, h4, h5, h6, .card-title {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
      font-weight: 700 !important;
      letter-spacing: -0.015em;
      line-height: 1.28 !important;
    }""",
        content
    )

    # body font family
    content = re.sub(
        r"font-family:\s*['\"]Nexa['\"],\s*['\"]Plus Jakarta Sans['\"],\s*['\"]Inter['\"],\s*sans-serif",
        "font-family: 'Plus Jakarta Sans', 'Inter', sans-serif",
        content
    )
    content = re.sub(
        r"font-family:\s*['\"]Nexa['\"],\s*['\"]Plus Jakarta Sans['\"],\s*sans-serif",
        "font-family: 'Plus Jakarta Sans', 'Inter', sans-serif",
        content
    )

    return content

# Get list of HTML files in root
target_files = [
    'index.html',
    'index-nexxus.html',
    'sobre.html',
    'sobre-nexxus.html',
    'servicos.html',
    'servicos-nexxus.html',
    'contato.html',
    'contato-nexxus.html',
    'blog.html',
    'blog-nexxus.html',
    'links.html',
    'artigo.html',
    'artigo-nexxus.html',
    'quanto-custa-terceirizar-time-de-vendas.html',
    'terceirizar-ou-estruturar-comercial-interno.html',
    'tendencias-mercado-comercial-b2b.html',
    'quem-fecha-a-venda-prospeccao-terceirizada.html',
    'quantas-reunioes-sdr-por-mes.html',
    'por-que-terceirizar-operacao-comercial.html'
]

print("Processing files in root...")
for fname in target_files:
    fpath = os.path.join(BASE_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = update_html_content(original)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated: {fname}")

print("\nProcessing files in preview-cliente...")
for fname in target_files:
    fpath = os.path.join(PREVIEW_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = update_html_content(original)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated preview: {fname}")

print("\nRebuilding preview-cliente.zip...")
zip_path = os.path.join(BASE_DIR, "preview-cliente.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(PREVIEW_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, PREVIEW_DIR)
            zipf.write(file_path, arcname)

print("preview-cliente.zip rebuilt successfully!")
