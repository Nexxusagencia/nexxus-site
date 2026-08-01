import os
import time
from flask import Flask, send_file, send_from_directory, jsonify, request, Response

app = Flask(__name__, static_folder=".")
START_TIME = time.time()

# Nexxus Design System Tokens
DESIGN_TOKENS = {
    "system": {
        "name": "Nexxus Design System",
        "version": "2.5.0",
        "author": "Nexxus Performance Marketing Agency",
        "year": 2026
    },
    "colors": {
        "bg": "#020611",
        "card": "#080E20",
        "glass": "rgba(9, 16, 36, 0.75)",
        "border": "rgba(1, 117, 239, 0.15)",
        "blue": {
            "default": "#0175ef",
            "glow": "rgba(1, 117, 239, 0.35)",
            "light": "#60a5fa",
            "dark": "#1e40af"
        },
        "mint": {
            "default": "#25c9b5",
            "glow": "rgba(37, 201, 181, 0.35)",
            "light": "#5eead4",
            "dark": "#0d9488"
        }
    },
    "typography": {
        "fontHeading": "'Oswald', sans-serif",
        "fontBody": "'Nexa', 'Plus Jakarta Sans', sans-serif",
        "fontMono": "'JetBrains Mono', monospace",
        "lineHeightHeading": "1.28"
    },
    "shadows": {
        "glowBlue": "0 0 25px rgba(1, 117, 239, 0.35)",
        "glowMint": "0 0 25px rgba(37, 201, 181, 0.35)",
        "glassInset": "inset 0 1px 1px rgba(255, 255, 255, 0.1), 0 20px 40px -10px rgba(0,0,0,0.8)"
    }
}

@app.route("/")
@app.route("/index-nexxus.html")
def index():
    nexxus_path = os.path.join(os.path.dirname(__file__), "index-nexxus.html")
    return send_file(nexxus_path)

@app.route("/sobre")
@app.route("/sobre.html")
@app.route("/sobre-nexxus.html")
def sobre():
    sobre_path = os.path.join(os.path.dirname(__file__), "sobre-nexxus.html")
    return send_file(sobre_path)

@app.route("/servicos")
@app.route("/servicos.html")
@app.route("/servicos-nexxus.html")
def servicos():
    servicos_path = os.path.join(os.path.dirname(__file__), "servicos-nexxus.html")
    return send_file(servicos_path)

@app.route("/contato")
@app.route("/contato.html")
@app.route("/contato-nexxus.html")
def contato():
    contato_path = os.path.join(os.path.dirname(__file__), "contato-nexxus.html")
    return send_file(contato_path)

@app.route("/design-system")
@app.route("/design-system.html")
def design_system():
    ds_path = os.path.join(os.path.dirname(__file__), "design-system-standalone.html")
    return send_file(ds_path)

@app.route("/download/design-system")
def download_design_system():
    ds_path = os.path.join(os.path.dirname(__file__), "design-system-standalone.html")
    return send_file(ds_path, as_attachment=True, download_name="nexxus-design-system.html")

@app.route("/download/design-system-zip")
def download_design_system_zip():
    zip_path = os.path.join(os.path.dirname(__file__), "design-system-package.zip")
    return send_file(zip_path, as_attachment=True, download_name="nexxus-design-system-package.zip")

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "system": DESIGN_TOKENS["system"],
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "environment": "production" if os.environ.get("FLASK_ENV") == "production" else "development"
    })

@app.route("/api/tokens", methods=["GET"])
def get_tokens():
    return jsonify(DESIGN_TOKENS)

@app.route("/api/calculate-roi", methods=["POST"])
def calculate_roi():
    data = request.get_json() or {}
    try:
        spend = float(data.get("spend", 5000))
        ticket = float(data.get("ticket", 1500))
    except (ValueError, TypeError):
        spend, ticket = 5000.0, 1500.0

    avg_cpl = 80.21
    conversion_rate = 0.075
    
    leads = round(spend / avg_cpl)
    sales = round(leads * conversion_rate)
    revenue = sales * ticket
    roas = round(revenue / spend, 2) if spend > 0 else 0
    cpa = round(spend / (sales if sales > 0 else 1), 2)
    profit = revenue - spend

    recommendation = "Excelente viabilidade para tráfego pago!" if roas >= 3.0 else "Recomendado otimizar taxa de conversão da landing page."

    return jsonify({
        "spend": spend,
        "ticket": ticket,
        "leads": leads,
        "sales": sales,
        "revenue": revenue,
        "profit": profit,
        "roas": roas,
        "cpa": cpa,
        "recommendation": recommendation
    })

@app.route("/api/export-css", methods=["GET"])
def export_css():
    css_content = f"""/* === NEXXUS DESIGN SYSTEM AUTOMATIC CSS EXPORT v{DESIGN_TOKENS['system']['version']} === */
:root {{
  --nexxus-bg: {DESIGN_TOKENS['colors']['bg']};
  --nexxus-card: {DESIGN_TOKENS['colors']['card']};
  --nexxus-blue: {DESIGN_TOKENS['colors']['blue']['default']};
  --nexxus-blue-glow: {DESIGN_TOKENS['colors']['blue']['glow']};
  --nexxus-mint: {DESIGN_TOKENS['colors']['mint']['default']};
  --nexxus-mint-glow: {DESIGN_TOKENS['colors']['mint']['glow']};
  --font-heading: {DESIGN_TOKENS['typography']['fontHeading']};
  --font-body: {DESIGN_TOKENS['typography']['fontBody']};
  --font-mono: {DESIGN_TOKENS['typography']['fontMono']};
}}

.glass-card {{
  background: {DESIGN_TOKENS['colors']['glass']};
  backdrop-filter: blur(20px);
  border: 1px solid {DESIGN_TOKENS['colors']['border']};
  box-shadow: {DESIGN_TOKENS['shadows']['glassInset']};
}}

.btn-nexxus-primary {{
  background: {DESIGN_TOKENS['colors']['blue']['default']};
  color: #FFFFFF;
  font-weight: 700;
  border-radius: 9999px;
  box-shadow: {DESIGN_TOKENS['shadows']['glowBlue']};
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}}
"""
    return Response(css_content, mimetype="text/css", headers={"Content-Disposition": "attachment; filename=nexxus-design-system.css"})

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    print("Servidor do Design System Nexxus rodando em http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

