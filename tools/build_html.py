"""Build a standalone HTML viewer for a Markdown file with Mermaid diagrams.

Usage: python3 build_html.py <input.md> <output.html> "<page title>"
Each diagram gets PNG/JPG/SVG export buttons. Needs network access to jsdelivr
(marked + mermaid) when the page is opened.
"""
import html
import sys

md_path, out_path = sys.argv[1], sys.argv[2]
md = open(md_path, encoding='utf-8').read()

TEMPLATE = r'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
  :root {
    --bg: #f6f7f9; --surface: #ffffff; --text: #1f2328; --muted: #57606a;
    --border: #d8dee4; --accent: #714b67; --accent-soft: #f3edf2; --code: #f0f2f4;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--text);
    font: 15px/1.6 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
  header { background: var(--accent); color: #fff; padding: 20px 16px; }
  header .wrap { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between; }
  header h1 { margin: 0; font-size: 20px; }
  .wrap { max-width: 1100px; margin: 0 auto; }
  main { padding: 16px; }
  #content { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 8px 24px 24px; }
  #content > h1:first-child { display: none; }
  h2 { border-bottom: 2px solid var(--accent-soft); padding-bottom: 6px; margin-top: 36px; color: var(--accent); }
  table { border-collapse: collapse; width: 100%; display: block; overflow-x: auto; margin: 12px 0; }
  th, td { border: 1px solid var(--border); padding: 6px 10px; text-align: left; vertical-align: top; }
  th { background: var(--code); }
  code { background: var(--code); padding: 1px 5px; border-radius: 4px; font-size: 13px; }
  hr { border: 0; border-top: 1px solid var(--border); margin: 28px 0; }
  .diagram { border: 1px solid var(--border); border-radius: 8px; margin: 14px 0 20px; background: #fff; }
  .diagram .bar { display: flex; flex-wrap: wrap; gap: 6px; justify-content: flex-end;
    padding: 6px 8px; border-bottom: 1px solid var(--border); background: var(--code); border-radius: 8px 8px 0 0; }
  .diagram .canvas { padding: 16px; overflow-x: auto; text-align: center; }
  .diagram .canvas svg { max-width: 100%; height: auto; }
  button { font: inherit; font-size: 13px; cursor: pointer; border: 1px solid var(--border);
    background: #fff; color: var(--text); border-radius: 6px; padding: 4px 10px; }
  button:hover { border-color: var(--accent); color: var(--accent); }
  header button { background: rgba(255,255,255,.15); color: #fff; border-color: rgba(255,255,255,.4); }
  header button:hover { background: rgba(255,255,255,.25); color: #fff; border-color: #fff; }
  .err { color: #b42318; white-space: pre-wrap; text-align: left; font-size: 13px; }
  @media print { header, .bar { display: none; } body { background: #fff; } #content { border: 0; } }
</style>
</head>
<body>
<header>
  <div class="wrap">
    <h1>__H1__</h1>
    <div>
      <button id="all-png">Export semua PNG</button>
      <button id="all-jpg">Export semua JPG</button>
    </div>
  </div>
</header>
<main class="wrap"><div id="content">Memuat…</div></main>

<script type="text/markdown" id="md-source">__MD__</script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"></script>
<script>
(async function () {
  const FONT = '-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif';
  const src = document.getElementById('md-source').textContent;
  const content = document.getElementById('content');
  content.innerHTML = marked.parse(src);

  mermaid.initialize({
    startOnLoad: false,
    theme: 'base',
    securityLevel: 'loose',
    htmlLabels: false,
    flowchart: { htmlLabels: false, curve: 'basis' },
    themeVariables: {
      fontFamily: FONT,
      primaryColor: '#f3edf2', primaryBorderColor: '#714b67', primaryTextColor: '#1f2328',
      lineColor: '#57606a', secondaryColor: '#e6f4f1', tertiaryColor: '#fafbfc',
    },
  });

  // Give each diagram a name from the nearest preceding heading.
  const blocks = [...content.querySelectorAll('pre > code.language-mermaid')];
  let n = 0;
  for (const code of blocks) {
    n += 1;
    const pre = code.parentElement;
    let h = pre.previousElementSibling;
    while (h && !/^H[1-3]$/.test(h.tagName)) h = h.previousElementSibling;
    const title = h ? h.textContent : 'diagram';
    const name = `${String(n).padStart(2, '0')}_${title.replace(/^[0-9.\s]+/, '').replace(/[^\w]+/g, '_').replace(/^_|_$/g, '').toLowerCase()}`;

    const box = document.createElement('div');
    box.className = 'diagram';
    box.dataset.name = name;
    box.innerHTML = `<div class="bar">
        <button data-fmt="png">PNG</button><button data-fmt="jpg">JPG</button><button data-fmt="svg">SVG</button>
      </div><div class="canvas"></div>`;
    pre.replaceWith(box);
    try {
      const { svg } = await mermaid.render(`mmd-${n}`, code.textContent);
      box.querySelector('.canvas').innerHTML = svg;
    } catch (e) {
      box.querySelector('.canvas').innerHTML = `<div class="err">Gagal render diagram: ${e.message}</div>`;
    }
  }

  function svgString(svg) {
    const clone = svg.cloneNode(true);
    const vb = svg.viewBox.baseVal;
    const w = vb && vb.width ? vb.width : svg.getBoundingClientRect().width;
    const h = vb && vb.height ? vb.height : svg.getBoundingClientRect().height;
    clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    clone.setAttribute('width', w);
    clone.setAttribute('height', h);
    clone.style.maxWidth = 'none';
    return { text: new XMLSerializer().serializeToString(clone), w, h };
  }

  function download(href, filename) {
    const a = document.createElement('a');
    a.href = href; a.download = filename;
    document.body.appendChild(a); a.click(); a.remove();
  }

  async function exportBox(box, fmt) {
    const svg = box.querySelector('.canvas svg');
    if (!svg) return;
    const { text, w, h } = svgString(svg);
    const name = box.dataset.name;
    if (fmt === 'svg') {
      download(URL.createObjectURL(new Blob([text], { type: 'image/svg+xml' })), `${name}.svg`);
      return;
    }
    const scale = 2, pad = 24;
    const img = new Image();
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(text);
    await img.decode();
    const canvas = document.createElement('canvas');
    canvas.width = (w + pad * 2) * scale;
    canvas.height = (h + pad * 2) * scale;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, pad * scale, pad * scale, w * scale, h * scale);
    const mime = fmt === 'jpg' ? 'image/jpeg' : 'image/png';
    try {
      download(canvas.toDataURL(mime, 0.95), `${name}.${fmt}`);
    } catch (e) {
      alert('Browser menolak ekspor gambar (' + e.message + '). Silakan gunakan tombol SVG.');
    }
  }

  content.addEventListener('click', (ev) => {
    const btn = ev.target.closest('.bar button');
    if (btn) exportBox(btn.closest('.diagram'), btn.dataset.fmt);
  });
  async function exportAll(fmt) {
    for (const box of content.querySelectorAll('.diagram')) {
      await exportBox(box, fmt);
      await new Promise(r => setTimeout(r, 300));
    }
  }
  document.getElementById('all-png').onclick = () => exportAll('png');
  document.getElementById('all-jpg').onclick = () => exportAll('jpg');
})();
</script>
</body>
</html>
'''

assert '</script' not in md.lower()
h1 = next(l[2:].strip() for l in md.splitlines() if l.startswith('# '))
title = sys.argv[3] if len(sys.argv) > 3 else h1
out = TEMPLATE.replace('__TITLE__', html.escape(title)).replace('__H1__', html.escape(h1)).replace('__MD__', md)
open(out_path, 'w', encoding='utf-8').write(out)
print('written', out_path)
