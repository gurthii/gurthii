// Modal helpers
const modal = document.getElementById('modal');
const statusEl = document.getElementById('saveStatus');

function toggleModal(show) {
    if (!modal) return;
    modal.style.display = show ? 'block' : 'none';
    if (show && statusEl) {
        statusEl.textContent = '';
        statusEl.style.display = 'none';
    }
}

function showModal() { toggleModal(true); }
function hideModal() { toggleModal(false); }

function saveData(event) {
    event.preventDefault();
    const form = event.target;
    const fd = new FormData(form);
    console.log('Target Price:', fd.get('targetPrice'));
    console.log('User Email:', fd.get('userEmail'));
    if (statusEl) { statusEl.textContent = 'Price tracking saved successfully!'; statusEl.style.display = 'block'; }
    form.reset();
}

// Dismiss on outside click / Escape
document.addEventListener('click', function(e) {
    if (!modal || modal.style.display !== 'block') return;
    if (!modal.contains(e.target) && !e.target.closest('.button-container')) hideModal();
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && modal && modal.style.display === 'block') hideModal();
});