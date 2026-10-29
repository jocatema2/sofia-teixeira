#!/usr/bin/env python3
"""Gera o index.html do site a partir de src/template.html.

Uso, a partir da raiz do repositório:

    python3 src/build.py

O template tem três marcas — __MARK__, __MARKFULL__ e __PORTRAIT__ — que são
substituídas pelas imagens em base64, para o site ficar num único ficheiro sem
dependências. Os blocos entre /* preview-only:start */ e /* preview-only:end */
só servem a pré-visualização no claude.ai e são retirados aqui.

A chave do formulário (ACCESS_KEY) é preservada entre gerações: se já estiver
no index.html, é reposta automaticamente no ficheiro novo.
"""
import base64, pathlib, re

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
BASE = 'https://www.sofiateixeira.com/'

html = (SRC / 'template.html').read_text(encoding='utf-8')

# ---- imagens embutidas ---------------------------------------------------
def data_uri(nome, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode((SRC / nome).read_bytes()).decode()

html = html.replace('__PORTRAIT__', data_uri('portrait.jpg', 'image/jpeg'))
html = html.replace('__MARKFULL__', data_uri('markfull.png', 'image/png'))
html = html.replace('__MARK__', data_uri('mark.png', 'image/png'))
for marca in ('__PORTRAIT__', '__MARK__', '__MARKFULL__'):
    assert marca not in html, marca

# ---- retirar o que só existe na pré-visualização -------------------------
html, n = re.subn(r'[ \t]*/\* preview-only:start \*/.*?/\* preview-only:end \*/\n',
                  '', html, flags=re.S)
assert n == 2, f'blocos preview-only: {n}'

def cortar(padrao, etiqueta):
    global html
    novo, n = re.subn(padrao, '', html, flags=re.S)
    assert n == 1, f'{etiqueta}: {n} correspondências'
    html = novo

cortar(r'\n  /\* -+ private pedidos panel -+ \*/.*?\n  \.pedidos-empty\{[^}]*\}', 'css do painel')
cortar(r'\n      <div class="pedidos-panel".*?\n      </div>\n', 'markup do painel')
assert 'claude.use' not in html and 'pedidos-panel' not in html

# ---- manter a chave do formulário que já esteja publicada ----------------
destino = ROOT / 'index.html'
if destino.exists():
    anterior = re.search(r"var ACCESS_KEY = '([^']*)'", destino.read_text(encoding='utf-8'))
    if anterior and anterior.group(1):
        html = html.replace("var ACCESS_KEY = ''", f"var ACCESS_KEY = '{anterior.group(1)}'", 1)
        print('chave do formulário preservada')

# ---- cabeçalho do documento ---------------------------------------------
fim_titulo = html.index('\n') + 1
titulo = html[:fim_titulo].strip()
corpo = html[fim_titulo:]

cabeca = f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{titulo}
<meta name="description" content="Ana Sofia Teixeira — consultora estratégica em processos de mudança, decisão e reorganização pessoal ou organizacional.">
<meta name="author" content="Ana Sofia Teixeira">
<link rel="canonical" href="{BASE}">
<meta property="og:url" content="{BASE}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<meta property="og:site_name" content="Ana Sofia Teixeira">
<meta property="og:title" content="Ana Sofia Teixeira">
<meta property="og:description" content="Consultora estratégica em processos de mudança, decisão e reorganização pessoal ou organizacional.">
<meta property="og:image" content="{BASE}og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FAF6ED">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<style>*,*::before,*::after{{box-sizing:border-box}}body{{margin:0}}</style>
</head>
<body>
"""

destino.write_text(cabeca + corpo.rstrip() + "\n</body>\n</html>\n", encoding='utf-8')
print(f'index.html gerado: {destino.stat().st_size // 1024} KB')
