const PRODUCTS = {
  "pull-handles": [
    { name: "109", image: "images/products/pull-handles/109.jpg" },
    { name: "114 Black", image: "images/products/pull-handles/114_Black.jpg" },
    { name: "9", image: "images/products/pull-handles/9.jpg" }
  ],
  "plate-handles": [
    { name: "115", image: "images/products/plate-handles/115.jpg" },
    { name: "125", image: "images/products/plate-handles/125.jpg" },
    { name: "165", image: "images/products/plate-handles/165.jpg" }
  ],
  "rose-handles": [
    { name: "117", image: "images/products/rose-handles/117.jpg" },
    { name: "167", image: "images/products/rose-handles/167.jpg" },
    { name: "177", image: "images/products/rose-handles/177.jpg" }
  ],
  "knobs": [
    { name: "28", image: "images/products/knobs/28.jpg" },
    { name: "30", image: "images/products/knobs/30.jpg" },
    { name: "33", image: "images/products/knobs/33.jpg" }
  ],
  "knockers": [
    { name: "144", image: "images/products/knockers/144.jpg" },
    { name: "148", image: "images/products/knockers/148.jpg" },
    { name: "55", image: "images/products/knockers/55.jpg" }
  ],
  "window-handles": [
    { name: "00", image: "images/products/window-handles/00.jpg" },
    { name: "144 A", image: "images/products/window-handles/144-A.jpg" },
    { name: "144 B", image: "images/products/window-handles/144-B.jpg" },
    { name: "177", image: "images/products/window-handles/177.jpg" },
    { name: "247", image: "images/products/window-handles/247.jpg" },
    { name: "387", image: "images/products/window-handles/387.jpg" },
    { name: "54", image: "images/products/window-handles/54.jpg" }
  ]
};

function renderProducts() {
  const grid = document.getElementById('products-grid');
  if (!grid || !CATEGORY) return;

  const items = PRODUCTS[CATEGORY] || [];
  if (items.length === 0) {
    grid.innerHTML = '<p style="text-align:center;color:var(--text-light);padding:4rem 0;">No products found in this category yet.</p>';
    return;
  }

  grid.innerHTML = items.map((p, i) => `
    <div class="product-card" data-img-src="${p.image}" data-name="${p.name}" data-index="${i}">
      <img src="${p.image}" alt="${p.name}" loading="lazy"
        onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
      <div class="img-placeholder" style="display:none">
        <span class="icon">&#10022;</span>
        <span>${p.name}</span>
      </div>
      <div class="product-card-overlay"></div>
      <div class="product-card-info">
        <p class="product-card-name">${p.name}</p>
        <p class="product-card-tag">Brass Hardware</p>
      </div>
      <div class="product-card-zoom">&#8853;</div>
    </div>
  `).join('');
}

renderProducts();
