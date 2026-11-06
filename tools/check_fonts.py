import glob, os, re

for pattern in ["*.html", "preview-cliente/*.html"]:
    files = glob.glob(pattern)
    print(f"\n--- {pattern} ---")
    for fpath in sorted(files):
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            content = f.read()
        fonts_match = re.search(r'fonts\.googleapis\.com/css2\?([^"]+)', content)
        fonts = fonts_match.group(1) if fonts_match else "NO GOOGLE FONTS"
        h1_match = re.search(r'h1[^{]*\{([^}]+)\}', content)
        h1_css = h1_match.group(1).replace("\n", " ").strip() if h1_match else "NO H1 RULE"
        print(f"{fpath:48} | {fonts[:40]} | {h1_css[:45]}")
