/**
 * Wanderlust - Travel Blog Website
 * Main JavaScript File
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Navbar Active State
    setActiveNavLink();
    
    // Initialize Scroll Animation
    initScrollAnimation();
    
    // Initialize Newsletter Form
    initNewsletterForm();
});

/**
 * Set active state for navigation links based on current page
 */
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

/**
 * Initialize scroll animation for elements
 */
function initScrollAnimation() {
    const cards = document.querySelectorAll('.destination-card, .team-card');
    
    // Simple scroll animation without external libraries
    window.addEventListener('scroll', function() {
        cards.forEach(card => {
            const cardTop = card.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (cardTop < windowHeight - 100) {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }
        });
    });
    
    // Initial check for elements in view
    setTimeout(() => {
        window.dispatchEvent(new Event('scroll'));
    }, 100);
}

/**
 * Initialize newsletter form submission
 */
function initNewsletterForm() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            
            if (emailInput && emailInput.value) {
                // Simulate form submission
                const submitBtn = this.querySelector('button[type="submit"]');
                const originalText = submitBtn.innerHTML;
                
                submitBtn.disabled = true;
                submitBtn.innerHTML = 'Subscribing...';
                
                setTimeout(() => {
                    submitBtn.innerHTML = 'Subscribed!';
                    emailInput.value = '';
                    
                    // Reset button after 2 seconds
                    setTimeout(() => {
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = originalText;
                    }, 2000);
                }, 1000);
            }
        });
    });
} 