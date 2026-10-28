# Portfolio — Md. Nizam Uddin Tuhin

A fast, dependency-free personal portfolio site built from my CV, ready to publish at
**https://nizambhl2001.github.io**

## What's inside

```
portfolio/
├── index.html                    # the whole site (single page, 6 sections)
├── 404.html                      # custom not-found page
├── robots.txt · sitemap.xml      # SEO
├── .nojekyll                     # tells GitHub Pages to serve files as-is
├── assets/
│   ├── css/styles.css            # design system, dark/light themes, responsive, print styles
│   ├── js/main.js                # theme toggle, nav, scroll effects, typing, contact form
│   └── Md-Nizam-Uddin-Tuhin-CV.pdf   # downloadable CV (generated)
├── make_cv.py                    # regenerate the CV PDF after editing content
└── deploy.sh                     # one-command publish to GitHub Pages
```

Highlights:

- **No frameworks, no CDNs, no build step** — plain HTML/CSS/JS, loads instantly anywhere.
- **Dark + light theme** with a toggle (remembers your choice).
- **Fully responsive** down to small phones, with an accessible mobile menu and skip link.
- **SEO ready**: meta description, Open Graph/Twitter cards, canonical URL, JSON-LD `Person` schema, sitemap.
- **Print-friendly** — `Ctrl/Cmd + P` gives a stripped-down, resume-style print view.
  For the polished one, use the **Download CV** button (generated from `make_cv.py`).
- **Downloadable CV** button wired to the generated PDF.

## Preview locally

```bash
cd portfolio
python3 -m http.server 8000
# open http://localhost:8000
```

## Publish to GitHub Pages

The site lives in the repo **`nizambhl2001/nizambhl2001.github.io`** (currently empty).
A user-site repo must be named exactly `<username>.github.io`, which this one is, so the site
serves from the root domain `https://nizambhl2001.github.io/`.

### Option A — the script (fastest)

```bash
cd portfolio
./deploy.sh
```

It asks for a GitHub **Personal Access Token** (Settings → Developer settings → Personal access
tokens → *classic*, tick `repo`) and pushes everything. Then, once only:

1. Go to `https://github.com/nizambhl2001/nizambhl2001.github.io/settings/pages`
2. **Source:** *Deploy from a branch* → **Branch:** `main` → **Folder:** `/ (root)` → **Save**
3. Wait ~1 minute → **https://nizambhl2001.github.io** goes live.

### Option B — manual

```bash
cd portfolio
git init
git remote add origin https://github.com/nizambhl2001/nizambhl2001.github.io.git
git add -A
git commit -m "Professional portfolio website"
git push -u origin main
```

Or simply drag-and-drop the files into the repo on github.com → **Add file → Upload files**.

## Making updates

- **Content:** edit the text directly in `index.html` (sections are commented: About, Skills,
  Experience, Projects, Education, Contact).
- **Colours:** change `--brand`, `--brand-2`, `--brand-3` at the top of `assets/css/styles.css`.
- **CV PDF:** edit `make_cv.py`, then `pip install reportlab && python3 make_cv.py`.

## Notes

- The contact form opens the visitor's email client with the message pre-filled (no backend needed).
  If you later want in-page sending, connect a service like Formspree and post the form there.
- Project links point at the `nizamuddintuhin` GitHub account, exactly as written in the CV —
  update them if those repos moved.
