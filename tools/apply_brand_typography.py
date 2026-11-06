import os
import re
import shutil
import zipfile

BASE_DIR = r"e:\00-NEXXUS\Site - Copia\NEXXUS-REDESIGN"
PREVIEW_DIR = os.path.join(BASE_DIR, "preview-cliente")

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
    # 1. Google Fonts link tag replacement
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
    
    # 4. Replace CSS typography rules
    # Case A: Institutional page comments + h1,h2 + h3,h4 block
    pattern_a = r'(?:/\*.*?\*/\s*)?h1,\s*h2,\s*\.main-title,\s*\.title-bold\s*\{[^}]*\}\s*h3,\s*h4,\s*h5,\s*h6,\s*\.card-title\s*\{[^}]*\}'
    if re.search(pattern_a, content, flags=re.DOTALL):
        content = re.sub(pattern_a, CSS_TYPOGRAPHY_STANDARD, content, flags=re.DOTALL)
    else:
        # Case B: blog articles and simple h1, h2 and h3, h4
        pattern_b = r'h1,\s*h2[^{]*\{[^}]*\}\s*h3,\s*h4[^{]*\{[^}]*\}'
        if re.search(pattern_b, content, flags=re.DOTALL):
            content = re.sub(pattern_b, CSS_TYPOGRAPHY_STANDARD, content, flags=re.DOTALL)
        else:
            # Case C: if separate h1, h2, .main-title, .title-bold
            pattern_c = r'h1,\s*h2,\s*\.main-title,\s*\.title-bold\s*\{[^}]*\}'
            if re.search(pattern_c, content, flags=re.DOTALL):
                content = re.sub(pattern_c, CSS_TYPOGRAPHY_STANDARD, content, flags=re.DOTALL)
            
    return content

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
    'artigo.html',
    'artigo-nexxus.html',
    'links.html',
    'por-que-terceirizar-operacao-comercial.html',
    'quantas-reunioes-sdr-por-mes.html',
    'quanto-custa-terceirizar-time-de-vendas.html',
    'quem-fecha-a-venda-prospeccao-terceirizada.html',
    'tendencias-mercado-comercial-b2b.html',
    'terceirizar-ou-estruturar-comercial-interno.html'
]

def main():
    print("=== Aplicando Tipografia Padronizada do Index em Todas as Páginas ===")
    
    # 1. Process Root Files
    print("\n[1/3] Processando arquivos na raiz...")
    for fname in target_files:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                original = f.read()
            updated = transform_html(original)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"  [OK] Atualizado: {fname}")
        else:
            print(f"  [X] Nao encontrado: {fname}")

    # 2. Process preview-cliente Files
    print("\n[2/3] Processando arquivos em preview-cliente/...")
    for fname in target_files:
        fpath = os.path.join(PREVIEW_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                original = f.read()
            updated = transform_html(original)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"  [OK] Atualizado preview: {fname}")

    # 3. Rebuild preview-cliente.zip
    print("\n[3/3] Reconstruindo preview-cliente.zip...")
    zip_path = os.path.join(BASE_DIR, "preview-cliente.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PREVIEW_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, PREVIEW_DIR)
                zipf.write(file_path, arcname)

    print(f"  [OK] Pacote preview-cliente.zip atualizado ({os.path.getsize(zip_path):,} bytes)")

if __name__ == '__main__':
    main()
