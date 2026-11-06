import os
import re
import difflib

BASE_DIR = r"e:\00-NEXXUS\Site - Copia\NEXXUS-REDESIGN"

GOOGLE_FONTS_STANDARD = """  <!-- Google Fonts: Anton (Títulos Principais), Oswald (Subtítulos dos Cards), Plus Jakarta Sans (UI, Textos & Métricas) & JetBrains Mono (Code/Metrics) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">"""

TAILWIND_FONT_FAMILY_STANDARD = """fontFamily: {
            heading: ['Oswald', 'sans-serif'],
            anton: ['Anton', 'sans-serif'],
            oswald: ['Oswald', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },"""

CSS_TYPOGRAPHY_STANDARD = """    /* Títulos Principais de Alto Impacto (H1, H2, .main-title, .title-bold): Anton */
    h1, h2, .main-title, .title-bold {
      font-family: 'Anton', sans-serif !important;
      font-weight: 400 !important;
      letter-spacing: 0.035em;
      text-transform: uppercase;
      line-height: 1.15 !important;
    }

    /* Subtítulos dos Cards (H3, H4, H5, H6, .card-title): Oswald Condensed Regular */
    h3, h4, h5, h6, .card-title {
      font-family: 'Oswald', sans-serif !important;
      font-weight: 400 !important;
      letter-spacing: 0.025em;
      text-transform: uppercase;
      line-height: 1.25 !important;
    }

    /* Métricas numéricas em Plus Jakarta Sans para máxima legibilidade */
    .counter-val {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
    }"""

def transform_html(content):
    # 1. Google Fonts replacement
    content = re.sub(
        r'(?:<!--\s*Google Fonts:[^>]*-->\s*)?(?:<link rel="preconnect"[^>]*>\s*){0,3}<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">',
        GOOGLE_FONTS_STANDARD,
        content
    )
    
    # 2. Tailwind Config fontFamily
    content = re.sub(
        r'fontFamily:\s*\{[^}]+\},',
        TAILWIND_FONT_FAMILY_STANDARD,
        content
    )
    
    # 3. Clean legacy Nexa @font-face
    content = re.sub(
        r'\s*@font-face\s*\{\s*font-family:\s*[\'"]Nexa[\'"][^}]*\}',
        '',
        content
    )
    
    # 4. Replace CSS typography block
    # Case A: Institutional page comments + h1,h2 + h3,h4 block
    pattern_a = r'(?:/\*\s*Brandbook 2026 Typography:[^/]*\*/\s*)?h1,\s*h2,\s*\.main-title,\s*\.title-bold\s*\{[^}]*\}\s*h3,\s*h4,\s*h5,\s*h6,\s*\.card-title\s*\{[^}]*\}'
    if re.search(pattern_a, content):
        content = re.sub(pattern_a, CSS_TYPOGRAPHY_STANDARD, content)
    else:
        # Case B: blog articles and simple h1, h2 and h3, h4
        pattern_b = r'h1,\s*h2\s*\{[^}]*\}\s*h3,\s*h4\s*\{[^}]*\}'
        if re.search(pattern_b, content):
            content = re.sub(pattern_b, CSS_TYPOGRAPHY_STANDARD, content)
        else:
            # Case C: if separate h1, h2, .main-title, .title-bold
            pattern_c = r'h1,\s*h2,\s*\.main-title,\s*\.title-bold\s*\{[^}]*\}'
            if re.search(pattern_c, content):
                content = re.sub(pattern_c, CSS_TYPOGRAPHY_STANDARD, content)
            
    return content

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
    'terceirizar-ou-estruturar-comercial-interno.html',
    'index.html', 'index-nexxus.html'
]

print("Dry-run test of transform_html:")
for f in files:
    fpath = os.path.join(BASE_DIR, f)
    with open(fpath, encoding='utf-8') as fh:
        original = fh.read()
    transformed = transform_html(original)
    has_anton_gf = "family=Anton" in transformed
    has_anton_tw = "anton: ['Anton', 'sans-serif']" in transformed
    has_anton_css = "font-family: 'Anton', sans-serif !important;" in transformed
    has_oswald_css = "font-family: 'Oswald', sans-serif !important;" in transformed
    diff_lines = len(list(difflib.unified_diff(original.splitlines(), transformed.splitlines())))
    print(f"{f:45} | Anton GF: {has_anton_gf} | TW: {has_anton_tw} | CSS Anton: {has_anton_css} | CSS Oswald: {has_oswald_css} | Diff lines: {diff_lines}")
