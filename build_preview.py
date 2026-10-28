"""Build a single-file, fully self-contained copy of the site (preview.html).

Useful for in-app previews / emailing the site as one file. The real deployment
still uses index.html + assets/ so the CSS and JS can be cached separately.
"""
import re
import pathlib
import base64

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
css = (root / "assets/css/styles.css").read_text(encoding="utf-8")
js = (root / "assets/js/main.js").read_text(encoding="utf-8")
pdf = (root / "assets/Md-Nizam-Uddin-Tuhin-CV.pdf").read_bytes()
pdf_b64 = base64.b64encode(pdf).decode()

html = html.replace(
    '<link rel="stylesheet" href="assets/css/styles.css" />',
    "<style>\n" + css + "\n</style>",
)
html = html.replace(
    '<script src="assets/js/main.js" defer></script>',
    "<script>\n" + js + "\n</script>",
)
html = html.replace(
    'href="assets/Md-Nizam-Uddin-Tuhin-CV.pdf" download',
    f'href="data:application/pdf;base64,{pdf_b64}" download="Md-Nizam-Uddin-Tuhin-CV.pdf"',
)
html = re.sub(r"\n\s*<!-- Open Graph / social -->.*?</script>\n", "\n", html, flags=re.S) if False else html

(root / "preview.html").write_text(html, encoding="utf-8")
print("preview.html written:", (root / "preview.html").stat().st_size, "bytes")
