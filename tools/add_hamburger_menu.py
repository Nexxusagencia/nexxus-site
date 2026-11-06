"""
add_hamburger_menu.py
Adiciona menu hambúrguer mobile a todos os HTMLs do projeto NEXXUS.

Estratégia:
- Detecta o bloco <nav class="glass-card ..."> de cada página
- Injeta o botão hambúrguer antes do fechamento do </nav>
- Injeta o drawer mobile após o </header>
- Injeta o script de toggle se ainda não existir
"""
import os
import re

BASE_DIR = r"e:\00-NEXXUS\Site - Copia\NEXXUS-REDESIGN"

PAGES = [
    "index.html",
    "sobre.html",
    "servicos.html",
    "contato.html",
    "blog.html",
    "artigo.html",
    "links.html",
    "por-que-terceirizar-operacao-comercial.html",
    "quantas-reunioes-sdr-por-mes.html",
    "quanto-custa-terceirizar-time-de-vendas.html",
    "quem-fecha-a-venda-prospeccao-terceirizada.html",
    "tendencias-mercado-comercial-b2b.html",
    "terceirizar-ou-estruturar-comercial-interno.html",
]

# ------------------------------------------------------------------
# Botão hambúrguer — inserido DENTRO do <nav>, antes do </nav>
# Visível apenas em < lg (mobile/tablet)
# ------------------------------------------------------------------
HAMBURGER_BTN = """
        <!-- Botão Hambúrguer (Mobile) -->
        <button
          id="mobile-menu-btn"
          class="lg:hidden flex items-center justify-center w-10 h-10 rounded-xl bg-slate-900 border border-slate-800 hover:border-nexxus-blue-500 text-white transition-all ml-auto shrink-0"
          aria-label="Abrir menu"
          aria-expanded="false"
          aria-controls="mobile-menu-drawer"
          onclick="toggleMobileMenu()"
        >
          <span id="hamburger-icon">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
          </span>
          <span id="close-icon" class="hidden">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </span>
        </button>"""

# ------------------------------------------------------------------
# Drawer mobile — inserido APÓS </header>
# ------------------------------------------------------------------
MOBILE_DRAWER = """
    <!-- ============================================================
         MENU MOBILE DRAWER (hambúrguer)
         ============================================================ -->
    <div
      id="mobile-menu-drawer"
      class="fixed inset-x-0 top-0 z-40 lg:hidden translate-y-[-110%] transition-transform duration-300 ease-in-out"
      aria-hidden="true"
    >
      <!-- Overlay backdrop -->
      <div
        id="mobile-menu-backdrop"
        class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm opacity-0 transition-opacity duration-300"
        onclick="toggleMobileMenu()"
      ></div>

      <!-- Painel do menu -->
      <div class="relative z-10 bg-slate-950 border-b border-slate-800/60 shadow-2xl px-5 pt-24 pb-8 flex flex-col gap-2">

        <!-- Links de Navegação -->
        <nav class="flex flex-col gap-1">
          <a href="index.html"   class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/60 font-medium text-sm transition-all">
            <iconify-icon icon="solar:home-2-bold" class="text-nexxus-blue-400 text-lg shrink-0"></iconify-icon> Início
          </a>
          <a href="sobre.html"   class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/60 font-medium text-sm transition-all">
            <iconify-icon icon="solar:users-group-rounded-bold" class="text-nexxus-blue-400 text-lg shrink-0"></iconify-icon> Sobre a Nexxus
          </a>
          <a href="servicos.html" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/60 font-medium text-sm transition-all">
            <iconify-icon icon="solar:chart-bold" class="text-nexxus-blue-400 text-lg shrink-0"></iconify-icon> Serviços
          </a>
          <a href="blog.html"    class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/60 font-medium text-sm transition-all">
            <iconify-icon icon="solar:document-text-bold" class="text-nexxus-blue-400 text-lg shrink-0"></iconify-icon> Blog & Artigos
          </a>
          <a href="links.html"   class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/60 font-medium text-sm transition-all">
            <iconify-icon icon="solar:link-circle-bold" class="text-nexxus-blue-400 text-lg shrink-0"></iconify-icon> Central de Links
          </a>
          <a href="contato.html" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/60 font-medium text-sm transition-all">
            <iconify-icon icon="solar:chat-round-dots-bold" class="text-nexxus-blue-400 text-lg shrink-0"></iconify-icon> Contato
          </a>
        </nav>

        <!-- Divisor -->
        <div class="border-t border-slate-800 my-2"></div>

        <!-- CTA WhatsApp -->
        <a
          href="https://wa.me/5511999999999?text=Ol%C3%A1%2C+gostaria+de+um+diagn%C3%B3stico+comercial"
          target="_blank" rel="noopener noreferrer"
          class="flex items-center justify-center gap-2 px-5 py-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 hover:bg-emerald-500/20 font-bold text-sm transition-all"
        >
          <iconify-icon icon="mdi:whatsapp" class="text-xl"></iconify-icon>
          Falar no WhatsApp
        </a>

        <a
          href="contato.html"
          class="flex items-center justify-center gap-2 px-5 py-3.5 rounded-xl bg-nexxus-blue-500/10 border border-nexxus-blue-500/30 text-nexxus-blue-400 hover:bg-nexxus-blue-500/20 font-bold text-sm transition-all"
        >
          <iconify-icon icon="solar:target-bold"></iconify-icon>
          Solicitar Diagnóstico Comercial
        </a>

        <!-- Status operacional -->
        <div class="flex items-center justify-center gap-2 pt-2 text-[11px] font-mono text-slate-500">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Operação Comercial B2B Ativa • São Paulo
        </div>
      </div>
    </div>"""

# ------------------------------------------------------------------
# Script de toggle — injetado antes de </body>
# ------------------------------------------------------------------
TOGGLE_SCRIPT = """
    <script>
      /* ---- Mobile Menu Toggle (Hambúrguer) ---- */
      function toggleMobileMenu() {
        var drawer   = document.getElementById('mobile-menu-drawer');
        var backdrop = document.getElementById('mobile-menu-backdrop');
        var btn      = document.getElementById('mobile-menu-btn');
        var hamIcon  = document.getElementById('hamburger-icon');
        var closeIcon= document.getElementById('close-icon');
        var isOpen   = drawer.getAttribute('aria-hidden') === 'false';

        if (isOpen) {
          // Fechar
          drawer.classList.add('translate-y-[-110%]');
          drawer.classList.remove('translate-y-0');
          backdrop.classList.remove('opacity-100');
          backdrop.classList.add('opacity-0');
          drawer.setAttribute('aria-hidden', 'true');
          btn.setAttribute('aria-expanded', 'false');
          hamIcon.classList.remove('hidden');
          closeIcon.classList.add('hidden');
          document.body.style.overflow = '';
        } else {
          // Abrir
          drawer.classList.remove('translate-y-[-110%]');
          drawer.classList.add('translate-y-0');
          backdrop.classList.remove('opacity-0');
          backdrop.classList.add('opacity-100');
          drawer.setAttribute('aria-hidden', 'false');
          btn.setAttribute('aria-expanded', 'true');
          hamIcon.classList.add('hidden');
          closeIcon.classList.remove('hidden');
          document.body.style.overflow = 'hidden';
        }
      }

      // Fechar ao redimensionar para desktop
      window.addEventListener('resize', function() {
        if (window.innerWidth >= 1024) {
          var drawer = document.getElementById('mobile-menu-drawer');
          if (drawer && drawer.getAttribute('aria-hidden') === 'false') {
            toggleMobileMenu();
          }
        }
      });
    </script>"""


def inject_hamburger(content, filename):
    """Injeta hambúrguer no nav, drawer após header, e script antes de </body>."""
    changed = False

    # 1. Já foi aplicado? Skip.
    if 'mobile-menu-btn' in content:
        print(f"  [SKIP] Já tem hambúrguer: {filename}")
        return content

    # 2. Injeta botão hambúrguer antes do </nav> do header principal
    #    (o primeiro </nav> dentro do <header class="sticky...)
    # Encontra o primeiro </nav> após a tag glass-card
    nav_close_pattern = r'(glass-card[\s\S]*?)(</nav>\s*</header>)'
    match = re.search(nav_close_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + HAMBURGER_BTN + "\n      " + content[match.start(2):]
        changed = True
    else:
        print(f"  [WARN] Padrão nav não encontrado em: {filename}")
        return content

    # 3. Injeta drawer após </header>
    content = re.sub(r'(</header>)', r'\1' + MOBILE_DRAWER, content, count=1)

    # 4. Injeta script antes de </body>
    if 'toggleMobileMenu' not in content:
        content = content.replace('</body>', TOGGLE_SCRIPT + '\n  </body>', 1)

    if changed:
        print(f"  [OK] Hambúrguer adicionado: {filename}")

    return content


def main():
    print("=== Adicionando Menu Hambúrguer Mobile ===\n")
    for fname in PAGES:
        fpath = os.path.join(BASE_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  [X] Não encontrado: {fname}")
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        updated = inject_hamburger(content, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)

    print("\n[DONE] Menu hambúrguer aplicado em todas as páginas!")


if __name__ == '__main__':
    main()
