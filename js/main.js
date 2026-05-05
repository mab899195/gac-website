const nav = document.querySelector('nav');
window.addEventListener('scroll', () => { nav.classList.toggle('scrolled', window.scrollY > 30); });

const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (toggle) {
  toggle.addEventListener('click', () => { navLinks.classList.toggle('open'); });
  document.querySelectorAll('.nav-links a').forEach(a => { a.addEventListener('click', () => navLinks.classList.remove('open')); });
}

const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(a => { if (a.getAttribute('href') === currentPage) a.classList.add('active'); });

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

let currentImages = [], currentIndex = 0;
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.getElementById('lightbox-caption');

function openLightbox(images, index) {
  currentImages = images; currentIndex = index; showLightboxImage();
  lightbox.classList.add('active'); document.body.style.overflow = 'hidden';
}
function closeLightbox() { lightbox.classList.remove('active'); document.body.style.overflow = ''; }
function showLightboxImage() {
  const item = currentImages[currentIndex];
  lightboxImg.src = item.src; lightboxImg.alt = item.name;
  if (lightboxCaption) lightboxCaption.textContent = item.name;
}
function lightboxNext() { currentIndex = (currentIndex + 1) % currentImages.length; showLightboxImage(); }
function lightboxPrev() { currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length; showLightboxImage(); }

if (lightbox) {
  document.getElementById('lightbox-close').addEventListener('click', closeLightbox);
  document.getElementById('lightbox-backdrop').addEventListener('click', closeLightbox);
  document.getElementById('lightbox-next').addEventListener('click', lightboxNext);
  document.getElementById('lightbox-prev').addEventListener('click', lightboxPrev);
  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') lightboxNext();
    if (e.key === 'ArrowLeft') lightboxPrev();
  });
}

function initProductCards() {
  const cards = document.querySelectorAll('.product-card');
  const images = Array.from(cards).map(card => ({
    src: card.dataset.imgSrc || card.querySelector('img')?.src || '',
    name: card.dataset.name || card.querySelector('.product-card-name')?.textContent || ''
  }));
  cards.forEach((card, i) => { card.addEventListener('click', () => openLightbox(images, i)); });
}
initProductCards();

document.querySelectorAll('.product-card').forEach((card, i) => {
  card.style.opacity = '0'; card.style.transform = 'translateY(24px)';
  card.style.transition = `opacity 0.5s ease ${i * 0.06}s, transform 0.5s ease ${i * 0.06}s`;
  setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 80 + i * 40);
});
