# GAC Door Handles Website

## 📁 File Structure

```
gac-website/
├── index.html              ← Homepage
├── pull-handles.html       ← Pull Handles page
├── plate-handles.html      ← Plate Handles page
├── rose-handles.html       ← Rose Handles page
├── knobs.html              ← Knobs page
├── knockers.html           ← Knockers page
├── window-handles.html     ← Window Handles & Accessories page
├── contact.html            ← Contact page
├── css/
│   └── style.css           ← All styles
├── js/
│   ├── main.js             ← Nav, lightbox, animations
│   └── products.js         ← ⭐ ADD YOUR PRODUCTS HERE
├── images/
│   ├── logo.png            ← Your logo
│   ├── favicon.png         ← Browser tab icon
│   ├── hero-bg.jpg         ← Homepage hero background
│   ├── about.jpg           ← About section image
│   ├── categories/         ← One image per category (shown on homepage)
│   │   ├── pull-handles.jpg
│   │   ├── plate-handles.jpg
│   │   ├── rose-handles.jpg
│   │   ├── knobs.jpg
│   │   ├── knockers.jpg
│   │   └── window-handles.jpg
│   └── products/           ← ⭐ YOUR PRODUCT IMAGES GO HERE
│       ├── pull-handles/
│       ├── plate-handles/
│       ├── rose-handles/
│       ├── knobs/
│       ├── knockers/
│       └── window-handles/
├── admin/                  ← Decap CMS (optional visual editor)
│   ├── index.html
│   └── config.yml
└── netlify.toml            ← Netlify settings
```

---

## ➕ HOW TO ADD PRODUCT IMAGES

### Method 1 — Edit the JS file directly (simple, fast)

1. Open `js/products.js` in any text editor (Notepad, VS Code, etc.)
2. Find the category you want (e.g. `"pull-handles"`)
3. Add a new line inside its array:

```js
{ name: "Pull Handle PH-10", image: "images/products/pull-handles/ph-10.jpg" },
```

4. Copy your image file to `images/products/pull-handles/ph-10.jpg`
5. Done! The product will appear on the page automatically.

### Method 2 — Use the visual CMS (no code needed)

After deploying to Netlify:
1. Enable **Netlify Identity** in your Netlify dashboard
2. Enable **Git Gateway** in Identity → Services
3. Go to `yoursite.com/admin`
4. Log in and use the visual interface to add/edit products

---

## 🚀 HOW TO DEPLOY FOR FREE (Netlify)

1. Go to [netlify.com](https://netlify.com) and create a free account
2. Click **"Add new site" → "Deploy manually"**
3. Drag the entire `gac-website` folder onto the page
4. Your site is live in ~30 seconds!
5. To connect your custom domain: Site settings → Domain management → Add custom domain

### To update the site later:
- Make changes to your files
- Go back to Netlify → Deploys → Drag & drop the folder again

---

## 🌐 Estimated Annual Cost

| Item | Cost |
|------|------|
| Netlify hosting | **Free** |
| Custom domain (e.g. Namecheap/OVH) | ~$10–15/year |
| **Total** | **~$10–15/year** (vs $100 on Durable) |

