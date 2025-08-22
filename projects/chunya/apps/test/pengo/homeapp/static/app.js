// Modal functionality
function showModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'flex';
}

function hideModal() {
    document.getElementById('modal').style.display = 'none';
    // Clear form and status
    document.querySelector('form').reset();
    document.getElementById('saveStatus').style.display = 'none';
}

function saveData(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const targetPrice = formData.get('targetPrice');
    const userEmail = formData.get('userEmail');
    
    // Show success message
    const saveStatus = document.getElementById('saveStatus');
    saveStatus.textContent = 'Price tracking saved successfully!';
    saveStatus.style.display = 'block';
    saveStatus.style.color = '#0B0B0B'
    saveStatus.style.fontWeight = '200'
    saveStatus.style.fontStyle = 'italic'
    
    // Hide modal after a short delay
    setTimeout(() => {
        hideModal();
    }, 2000);
    
    // Here you would typically send the data to your backend
    console.log('Target Price:', targetPrice);
    console.log('User Email:', userEmail);
}

// Close modal when clicking outside of it
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal');
    
    window.onclick = function(event) {
        if (event.target === modal) {
            hideModal();
        }
    }
});
