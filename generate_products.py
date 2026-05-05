"""
Generate products.js and products.json from images in images/products/<category>/.

Usage:
  python3 generate_products.py

Add images to any category folder, run this script, then preview the site.
Netlify runs it automatically on every deploy (see netlify.toml).

Supported image formats: jpg, jpeg, png, webp, gif, avif
Product name is derived from the filename: "my-product-01.jpg" → "My Product 01"
Products are sorted alphabetically by filename within each category.
"""

import json
import os

CATEGORIES = [
    ("pull-handles",    "Pull Handle"),
    ("plate-handles",   "Plate Handle"),
    ("rose-handles",    "Rose Handle"),
    ("knobs",           "Knob"),
    ("knockers",        "Knocker"),
    ("window-handles",  "Window Handle"),
]

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
IMAGES_DIR = "images/products"


def filename_to_name(filename):
    stem = os.path.splitext(filename)[0]
    return stem.replace("-", " ").replace("_", " ").title()


def scan_category(folder_key):
    folder = os.path.join(IMAGES_DIR, folder_key)
    if not os.path.isdir(folder):
        return []

    files = sorted(
        f for f in os.listdir(folder)
        if os.path.splitext(f)[1].lower() in IMAGE_EXTENSIONS
    )

    return [
        {
            "name": filename_to_name(f),
            "image": f"{IMAGES_DIR}/{folder_key}/{f}",
        }
        for f in files
    ]


def build_products_js(data):
    lines = ["const PRODUCTS = {"]
    for i, (key, _) in enumerate(CATEGORIES):
        items = data[key]
        comma = "," if i < len(CATEGORIES) - 1 else ""
        if not items:
            lines.append(f'  "{key}": []{comma}')
        else:
            lines.append(f'  "{key}": [')
            for j, p in enumerate(items):
                item_comma = "," if j < len(items) - 1 else ""
                lines.append(
                    f'    {{ name: {json.dumps(p["name"])}, image: {json.dumps(p["image"])} }}{item_comma}'
                )
            lines.append(f'  ]{comma}')
    lines.append("};")
    lines.append("")
    lines.append("""function renderProducts() {
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

renderProducts();""")
    return "\n".join(lines) + "\n"


def main():
    data = {}
    for key, _ in CATEGORIES:
        data[key] = scan_category(key)
        count = len(data[key])
        print(f"  {key}: {count} image{'s' if count != 1 else ''}")

    # Write products.js
    js_path = os.path.join("js", "products.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(build_products_js(data))
    print(f"\nWrote {js_path}")

    # Write products.json (for pages/ subdirectory pages)
    json_data = {}
    for key, _ in CATEGORIES:
        json_data[key] = [
            {"name": p["name"], "image": p["image"]}
            for p in data[key]
        ]
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    print("Wrote products.json")


if __name__ == "__main__":
    print("Scanning image folders...")
    main()
    print("\nDone. Preview with: python3 -m http.server 8080")
