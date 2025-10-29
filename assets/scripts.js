// Grab nodes
const triggers = document.querySelectorAll('.screenshot-trigger');
const popup = document.getElementById('popup');
const popupImg = popup.querySelector('img');
const closeBtn = document.getElementById('closeBtn');

// Helper to open
function openPopup(imgSrc) {
  if (!imgSrc) return;
  popupImg.src = imgSrc;
  popup.style.display = 'block';
  popup.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  // ensure scroll starts at top of overlay
  popup.scrollTop = 0;
}

// Helper to close & cleanup
function closePopup() {
  popup.style.display = 'none';
  popup.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  // clear src to stop image loading/keep memory clean
  popupImg.src = '';
}

// Wire triggers
triggers.forEach(el => {
  el.addEventListener('click', (e) => {
    const src = el.getAttribute('src'); // keeps your current pattern
    openPopup(src);
  });
});

// Close when clicking on the overlay background only (not when clicking the image or close button)
// So check that the click target is the popup element itself
popup.addEventListener('click', (e) => {
  if (e.target === popup) closePopup();
});

// Close button — stop propagation so overlay handler won't also run
closeBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  closePopup();
});

// Optional: close on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && popup.style.display === 'block') {
    closePopup();
  }
});
