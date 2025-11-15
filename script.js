document.addEventListener('DOMContentLoaded', function() {
    const viewButton = document.getElementById('viewButton');
    const diagramSelect = document.getElementById('diagramSelect');
    
    if (viewButton && diagramSelect) {
        viewButton.addEventListener('click', function() {
            const selectedDiagram = diagramSelect.value;
            
            if (!selectedDiagram) {
                alert('Please select a diagram type first!');
                diagramSelect.focus();
                return;
            }
            
            window.location.href = `/diagram/${selectedDiagram}`;
        });
        
        diagramSelect.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                viewButton.click();
            }
        });
    }
    
    const cards = document.querySelectorAll('.notation-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
    
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.getAttribute('href').startsWith('/')) {
                e.preventDefault();
                const href = this.getAttribute('href');
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.3s ease';
                setTimeout(() => {
                    window.location.href = href;
                }, 300);
            }
        });
    });
});
