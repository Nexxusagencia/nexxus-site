import os
import re
import shutil
import zipfile

BASE_DIR = r"e:\00-NEXXUS\Site - Copia\NEXXUS-REDESIGN"
PREVIEW_DIR = os.path.join(BASE_DIR, "preview-cliente")

STANDARDIZED_FOOTER = """    <!-- ============================================================
         RODAPÉ INSTITUCIONAL PADRONIZADO (NEXXUS)
         ============================================================ -->
    <footer class="mt-20 border-t border-white/10 bg-slate-950 py-16 text-slate-400 text-sm relative z-10 selection:bg-nexxus-blue-500/30 selection:text-white">
      <div class="max-w-7xl mx-auto px-6">
        
        <!-- Grid Superior: 4 Colunas Estruturadas -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-12 pb-12 border-b border-white/10">
          
          <!-- Coluna 1: Marca, Missão & Redes Sociais (lg:col-span-4) -->
          <div class="lg:col-span-4 space-y-4 text-left">
            <a href="index.html" class="inline-flex items-center gap-2.5 group">
              <img src="nexxusagencia.com.br/assets/logo-nexxus-white-original-blue.png" alt="Nexxus Agência Comercial" class="h-8 w-auto select-none transition-transform group-hover:scale-105">
            </a>

            <p class="text-xs text-slate-400 font-light leading-relaxed max-w-sm">
              A Nexxus estrutura e opera o setor comercial da sua empresa com método proprietário, inteligência de dados e equipe dedicada (SDR, Hunter e Closer). Operação no ar em 20 dias.
            </p>

            <!-- Status Operacional -->
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>Operação Comercial B2B Ativa</span>
            </div>

            <!-- Canais Sociais -->
            <div class="flex items-center gap-3 pt-2">
              <a href="https://www.instagram.com/nexxus.inc/" target="_blank" rel="noopener noreferrer" class="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 hover:border-nexxus-mint-400 hover:bg-slate-800/80 flex items-center justify-center text-white text-lg transition-all hover:-translate-y-0.5 shadow-sm group" title="Instagram @nexxus.inc" aria-label="Instagram">
                <iconify-icon icon="line-md:instagram" class="group-hover:text-nexxus-mint-400 transition-colors"></iconify-icon>
              </a>
              <a href="https://linkedin.com/company/nexxus-ag%C3%AAncia/" target="_blank" rel="noopener noreferrer" class="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 hover:border-nexxus-blue-400 hover:bg-slate-800/80 flex items-center justify-center text-white text-lg transition-all hover:-translate-y-0.5 shadow-sm group" title="LinkedIn Nexxus" aria-label="LinkedIn">
                <iconify-icon icon="line-md:linkedin" class="group-hover:text-nexxus-blue-400 transition-colors"></iconify-icon>
              </a>
              <a href="https://wa.me/5511999999999?text=Ol%C3%A1%2C+gostaria+de+um+diagn%C3%B3stico+comercial+com+a+Nexxus" target="_blank" rel="noopener noreferrer" class="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 hover:border-emerald-400 hover:bg-slate-800/80 flex items-center justify-center text-white text-lg transition-all hover:-translate-y-0.5 shadow-sm group" title="WhatsApp Comercial" aria-label="WhatsApp">
                <svg class="w-5 h-5 text-white group-hover:text-emerald-400 transition-colors fill-current" viewBox="0 0 24 24">
                  <path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.23 8.23 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.2 8.2 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24M8.53 7.33c-.16 0-.43.06-.66.31c-.22.25-.87.86-.87 2.07c0 1.22.89 2.39 1 2.56c.14.17 1.76 2.67 4.25 3.73c.59.27 1.05.42 1.41.53c.59.19 1.13.16 1.56.1c.48-.07 1.46-.6 1.67-1.18s.21-1.07.15-1.18c-.07-.1-.23-.16-.48-.27c-.25-.14-1.47-.74-1.69-.82c-.23-.08-.37-.12-.56.12c-.16.25-.64.81-.78.97c-.15.17-.29.19-.53.07c-.26-.13-1.06-.39-2-1.23c-.74-.66-1.23-1.47-1.38-1.72c-.12-.24-.01-.39.11-.5c.11-.11.27-.29.37-.44c.13-.14.17-.25.25-.41c.08-.17.04-.31-.02-.43c-.06-.11-.56-1.35-.77-1.84c-.2-.48-.4-.42-.56-.43c-.14 0-.3-.01-.47-.01"/>
                </svg>
              </a>
              <a href="links.html" class="w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 hover:border-nexxus-blue-400 hover:bg-slate-800/80 flex items-center justify-center text-white text-lg transition-all hover:-translate-y-0.5 shadow-sm group" title="Central de Links" aria-label="Central de Links">
                <iconify-icon icon="solar:link-circle-bold" class="group-hover:text-nexxus-blue-400 transition-colors"></iconify-icon>
              </a>
            </div>
          </div>

          <!-- Coluna 2: Soluções Comerciais (lg:col-span-3) -->
          <div class="lg:col-span-3 space-y-4 text-left">
            <h4 class="text-white font-normal text-xs uppercase font-heading tracking-wider flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-nexxus-blue-500"></span>
              <span>Soluções</span>
            </h4>
            <ul class="space-y-2.5 text-xs font-light">
              <li><a href="servicos.html#terceirizacao" class="hover:text-white transition-colors flex items-center gap-1.5 group"><iconify-icon icon="solar:arrow-right-linear" class="text-slate-600 group-hover:text-nexxus-blue-400 group-hover:translate-x-0.5 transition-all"></iconify-icon><span>Terceirização Comercial (BPO)</span></a></li>
              <li><a href="servicos.html#estruturacao" class="hover:text-white transition-colors flex items-center gap-1.5 group"><iconify-icon icon="solar:arrow-right-linear" class="text-slate-600 group-hover:text-nexxus-blue-400 group-hover:translate-x-0.5 transition-all"></iconify-icon><span>Estruturação de Vendas B2B</span></a></li>
              <li><a href="servicos.html#mentoria" class="hover:text-white transition-colors flex items-center gap-1.5 group"><iconify-icon icon="solar:arrow-right-linear" class="text-slate-600 group-hover:text-nexxus-blue-400 group-hover:translate-x-0.5 transition-all"></iconify-icon><span>Mentoria & Treinamento SDR/Closer</span></a></li>
              <li><a href="servicos.html#tecnologia" class="hover:text-white transition-colors flex items-center gap-1.5 group"><iconify-icon icon="solar:arrow-right-linear" class="text-slate-600 group-hover:text-nexxus-blue-400 group-hover:translate-x-0.5 transition-all"></iconify-icon><span>Implementação CRM Kommo</span></a></li>
              <li><a href="index.html#metodo" class="hover:text-white transition-colors flex items-center gap-1.5 group"><iconify-icon icon="solar:arrow-right-linear" class="text-slate-600 group-hover:text-nexxus-blue-400 group-hover:translate-x-0.5 transition-all"></iconify-icon><span>Metodologia em 6 Etapas</span></a></li>
              <li><a href="javascript:void(0)" onclick="if(window.openRoiModal){window.openRoiModal()}else{location.href='index.html#roi-calculator'}" class="text-nexxus-mint-400 hover:text-white transition-colors flex items-center gap-1.5 group"><iconify-icon icon="solar:calculator-bold-duotone" class="text-nexxus-mint-400"></iconify-icon><span class="font-medium">Simulador de ROI B2B</span></a></li>
            </ul>
          </div>

          <!-- Coluna 3: Institucional & Conteúdo (lg:col-span-2) -->
          <div class="lg:col-span-2 space-y-4 text-left">
            <h4 class="text-white font-normal text-xs uppercase font-heading tracking-wider flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-nexxus-mint-400"></span>
              <span>Institucional</span>
            </h4>
            <ul class="space-y-2.5 text-xs font-light">
              <li><a href="index.html" class="hover:text-white transition-colors">Início</a></li>
              <li><a href="sobre.html" class="hover:text-white transition-colors">Sobre a Nexxus</a></li>
              <li><a href="servicos.html" class="hover:text-white transition-colors">Serviços</a></li>
              <li><a href="blog.html" class="hover:text-white transition-colors">Blog & Artigos</a></li>
              <li><a href="index.html#diferenciais" class="hover:text-white transition-colors">Diferenciais</a></li>
              <li><a href="index.html#faq" class="hover:text-white transition-colors">FAQ</a></li>
              <li><a href="links.html" class="hover:text-white transition-colors">Central de Links</a></li>
              <li><a href="contato.html" class="hover:text-white transition-colors">Contato & Diagnóstico</a></li>
            </ul>
          </div>

          <!-- Coluna 4: Contato, Sede & Atendimento (lg:col-span-3) -->
          <div class="lg:col-span-3 space-y-4 text-left">
            <h4 class="text-white font-normal text-xs uppercase font-heading tracking-wider flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-nexxus-blue-400"></span>
              <span>Contato & Sede</span>
            </h4>
            <div class="space-y-3.5 text-xs">
              <div class="flex items-start gap-2.5">
                <iconify-icon icon="solar:letter-bold" class="text-nexxus-blue-400 text-base shrink-0 mt-0.5"></iconify-icon>
                <div class="font-light">
                  <div class="text-[10px] text-slate-500 uppercase font-mono">E-mail Corporativo</div>
                  <a href="mailto:admin@nexxusagencia.com.br" class="text-slate-300 hover:text-white transition-colors">admin@nexxusagencia.com.br</a>
                </div>
              </div>

              <div class="flex items-start gap-2.5">
                <iconify-icon icon="solar:map-point-bold" class="text-nexxus-mint-400 text-base shrink-0 mt-0.5"></iconify-icon>
                <div class="font-light text-slate-300 leading-relaxed">
                  <div class="text-[10px] text-slate-500 uppercase font-mono">Sede Operacional</div>
                  <div class="text-white font-medium">Edifício Capital Corporate Office</div>
                  <div class="text-slate-400">Ao lado do Shopping Morumbi</div>
                  <div class="text-slate-400">São Paulo / SP — Brasil</div>
                </div>
              </div>

              <div class="pt-2">
                <a href="contato.html" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-nexxus-blue-500/10 hover:bg-nexxus-blue-500/20 border border-nexxus-blue-500/30 text-nexxus-blue-400 hover:text-white text-xs font-semibold transition-all">
                  <iconify-icon icon="solar:chat-round-dots-bold"></iconify-icon>
                  <span>Solicitar Diagnóstico Comercial</span>
                </a>
              </div>
            </div>
          </div>

        </div>

        <!-- Sub-Footer: Copyright com Ano Automático & Informações Legais -->
        <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-500">
          <div class="flex flex-col sm:flex-row items-center gap-2 sm:gap-4 text-center sm:text-left">
            <div>
              &copy; <span class="current-year">2026</span> Nexxus Agência Comercial. Todos os direitos reservados.
            </div>
            <span class="hidden sm:inline text-slate-700">•</span>
            <div class="text-slate-400 font-mono text-[11px]">
              Operação Comercial & Estruturação B2B
            </div>
          </div>

          <div class="flex items-center gap-4 text-[11px] font-mono text-slate-400">
            <span>São Paulo / SP</span>
            <span class="text-slate-700">•</span>
            <span class="text-slate-400">Alta Performance B2B</span>
          </div>
        </div>

      </div>

      <script>
        (function() {
          var y = new Date().getFullYear();
          var els = document.querySelectorAll('.current-year');
          for (var i = 0; i < els.length; i++) { els[i].textContent = y; }
        })();
      </script>
    </footer>"""

def update_footer_in_html(content):
    # Fix any invalid line-md:whatsapp across the page (Iconify line-md has no whatsapp icon)
    content = content.replace('line-md:whatsapp', 'mdi:whatsapp')

    # Check if page is links.html
    if 'Central de Links' in content and '<!-- Footer Copyright -->' in content:
        # Update copyright with auto year
        links_footer_pattern = r'<!-- Footer Copyright -->\s*<div class="[^"]*">\s*©[^<]*</div>'
        links_footer_new = '''<!-- Footer Copyright -->
    <div class="text-[11px] text-slate-400 font-mono pt-4">
      &copy; <span class="current-year">2026</span> Nexxus Agência Comercial · São Paulo / SP
    </div>
    <script>
      (function() {
        var y = new Date().getFullYear();
        var els = document.querySelectorAll('.current-year');
        for (var i = 0; i < els.length; i++) { els[i].textContent = y; }
      })();
    </script>'''
        return re.sub(links_footer_pattern, links_footer_new, content)
    
    # For standard pages with <footer ...>...</footer>
    footer_pattern = r'(?:<!--[^\n]*FOOTER[^\n]*-->\s*)?<footer[^>]*>.*?</footer>'
    if re.search(footer_pattern, content, flags=re.DOTALL):
        return re.sub(footer_pattern, STANDARDIZED_FOOTER, content, flags=re.DOTALL)
    
    return content

files = [
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
    print("=== Padronizando Rodapé em Todas as Páginas com Ano Automático ===")
    
    # 1. Root files
    print("\n[1/3] Atualizando rodapés na raiz...")
    for fname in files:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            updated = update_footer_in_html(content)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"  [OK] Rodape atualizado: {fname}")
        else:
            print(f"  [X] Nao encontrado: {fname}")
            
    # 2. Preview files
    print("\n[2/3] Atualizando rodapés em preview-cliente/...")
    for fname in files:
        fpath = os.path.join(PREVIEW_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            updated = update_footer_in_html(content)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"  [OK] Rodape atualizado em preview: {fname}")
            
    # 3. Rebuild preview-cliente.zip
    print("\n[3/3] Reconstruindo preview-cliente.zip...")
    zip_path = os.path.join(BASE_DIR, "preview-cliente.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files_in_dir in os.walk(PREVIEW_DIR):
            for file in files_in_dir:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, PREVIEW_DIR)
                zipf.write(file_path, arcname)

    print(f"  [OK] Pacote preview-cliente.zip reconstruido ({os.path.getsize(zip_path):,} bytes)")

if __name__ == '__main__':
    main()
