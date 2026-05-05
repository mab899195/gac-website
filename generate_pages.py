categories = [
    {
        "key": "pull-handles",
        "title": "Pull Handles",
        "description": "Discover our stylish and durable pull handles, perfect for adding a touch of elegance to any door.",
        "data_key": "pull-handles",
        "prev": None,
        "next": "plate-handles"
    },
    {
        "key": "plate-handles",
        "title": "Plate Handles",
        "description": "Elevate your design with our premium plate handles, seamlessly blending functionality and sophistication.",
        "data_key": "plate-handles",
        "prev": "pull-handles",
        "next": "rose-handles"
    },
    {
        "key": "rose-handles",
        "title": "Rose Handles",
        "description": "Refine your doors with our durable and charming rose handles for timeless elegance and smooth functionality.",
        "data_key": "rose-handles",
        "prev": "plate-handles",
        "next": "knobs"
    },
    {
        "key": "knobs",
        "title": "Knobs",
        "description": "Upgrade your doors with our stylish and functional knobs, crafted for smooth operation and lasting elegance.",
        "data_key": "knobs",
        "prev": "rose-handles",
        "next": "knockers"
    },
    {
        "key": "knockers",
        "title": "Knockers",
        "description": "Welcome guests with our durable knockers, marrying classic design for a lasting impression.",
        "data_key": "knockers",
        "prev": "knobs",
        "next": "window-handles"
    },
    {
        "key": "window-handles",
        "title": "Window Handles & Accessories",
        "description": "Enhance your windows with our ergonomic handles, meticulously crafted for smooth operation and lasting durability.",
        "data_key": "window-handles",
        "prev": "knockers",
        "next": None
    }
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — GAC Door Handles</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="icon" href="../images/favicon.ico" type="image/x-icon">
</head>
<body>

<!-- HEADER -->
<header>
  <a href="../index.html" class="logo">
    <img src="../images/logo.png" alt="GAC Door Handles" onerror="this.style.display='none'">
    <span class="logo-text">GAC Door Handles</span>
  </a>
  <nav>
    <a href="pull-handles.html"{active_pull}>Pull Handles</a>
    <a href="plate-handles.html"{active_plate}>Plate Handles</a>
    <a href="rose-handles.html"{active_rose}>Rose Handles</a>
    <a href="knobs.html"{active_knobs}>Knobs</a>
    <a href="knockers.html"{active_knockers}>Knockers</a>
    <a href="window-handles.html"{active_window}>Window Handles</a>
    <a href="contact.html" class="nav-contact">Contact Us</a>
  </nav>
  <div class="hamburger">
    <span></span><span></span><span></span>
  </div>
</header>

<!-- CATEGORY HERO -->
<div class="category-hero">
  <div class="breadcrumb">
    <a href="../index.html">Home</a>
    <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 18l6-6-6-6"/></svg>
    <span>{title}</span>
  </div>
  <p class="category-hero-eyebrow">GAC Door Handles</p>
  <h1 class="category-hero-title"><em>{title}</em></h1>
  <p class="category-hero-desc">{description}</p>
</div>

<!-- PRODUCTS GRID -->
<section class="products-section">
  <div id="products-grid" class="products-grid"></div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-grid">
    <div>
      <div class="footer-logo">GAC Door Handles</div>
      <p class="footer-tagline">Custom-made, elegant brass door handles and accessories. Masterfully crafted for timeless interiors.</p>
      <div class="contact-socials" style="margin-top:24px">
        <a href="https://facebook.com/profile.php?id=100063660506355" class="social-link" target="_blank" rel="noopener" aria-label="Facebook">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
        </a>
        <a href="https://instagram.com/gac.doorhandles/?hl=fr" class="social-link" target="_blank" rel="noopener" aria-label="Instagram">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>
        </a>
        <a href="https://linkedin.com/company/gac-door-handles-manufacturing/" class="social-link" target="_blank" rel="noopener" aria-label="LinkedIn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
        </a>
      </div>
    </div>
    <div>
      <div class="footer-col-title">Collections</div>
      <ul class="footer-links">
        <li><a href="pull-handles.html">Pull Handles</a></li>
        <li><a href="plate-handles.html">Plate Handles</a></li>
        <li><a href="rose-handles.html">Rose Handles</a></li>
        <li><a href="knobs.html">Knobs</a></li>
        <li><a href="knockers.html">Knockers</a></li>
        <li><a href="window-handles.html">Window Handles</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Contact</div>
      <ul class="footer-links">
        <li><a href="mailto:gachandles@gmail.com">gachandles@gmail.com</a></li>
        <li><a href="tel:+963212672702">+963 21 267 2702</a></li>
        <li><a href="https://wa.me/963944334550">WhatsApp</a></li>
        <li><a href="contact.html">Get In Touch</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span class="footer-copy">&copy; 2025 GAC Door Handles. All rights reserved.</span>
    <span class="footer-copy">Aleppo, Syria</span>
  </div>
</footer>

<!-- LIGHTBOX -->
<div id="lightbox" class="lightbox">
  <div class="lightbox-inner">
    <button class="lightbox-close" onclick="closeLightbox()">&#x2715;</button>
    <img class="lightbox-img" src="" alt="">
    <div class="lightbox-title"></div>
    <div class="lightbox-ref"></div>
    <div class="lightbox-nav">
      <button onclick="lightboxPrev()">&#x2190;</button>
      <button onclick="lightboxNext()">&#x2192;</button>
    </div>
  </div>
</div>

<script src="../js/main.js"></script>
<script>
  fetch('../products.json')
    .then(r => r.json())
    .then(data => {{
      const products = data['{data_key}'] || [];
      // Prefix image paths
      const prefixed = products.map(p => ({{
        ...p,
        image: p.image ? '../' + p.image : ''
      }}));
      buildProductGrid(prefixed, 'products-grid');
    }});
</script>
</body>
</html>
'''

active_map = {
    "pull-handles": "active_pull",
    "plate-handles": "active_plate",
    "rose-handles": "active_rose",
    "knobs": "active_knobs",
    "knockers": "active_knockers",
    "window-handles": "active_window"
}

for cat in categories:
    actives = {v: '' for v in active_map.values()}
    current_active_key = active_map[cat["key"]]
    actives[current_active_key] = ' class="active"'

    html = TEMPLATE.format(
        title=cat["title"],
        description=cat["description"],
        data_key=cat["data_key"],
        active_pull=actives["active_pull"],
        active_plate=actives["active_plate"],
        active_rose=actives["active_rose"],
        active_knobs=actives["active_knobs"],
        active_knockers=actives["active_knockers"],
        active_window=actives["active_window"],
    )

    filename = f'/home/claude/gac-website/pages/{cat["key"]}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created: {filename}')

print('All product pages created.')
