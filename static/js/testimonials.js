
document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.testimonials-container');
    const cards = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    let currentIndex = 0;
    const cardWidth = cards[0].offsetWidth + 30; // including gap

    // Initialize first card as active
    cards[currentIndex].classList.add('active');
    dots[currentIndex].classList.add('active');

    // Next button functionality
    nextBtn.addEventListener('click', function() {
        if (currentIndex < cards.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateTestimonials();
    });

    // Previous button functionality
    prevBtn.addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = cards.length - 1;
        }
        updateTestimonials();
    });

    // Dot navigation functionality
    dots.forEach((dot, index) => {
        dot.addEventListener('click', function() {
            currentIndex = index;
            updateTestimonials();
        });
    });

    // Auto-rotate testimonials
    let autoRotate = setInterval(() => {
        if (currentIndex < cards.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateTestimonials();
    }, 5000);

    // Pause auto-rotation on hover
    container.addEventListener('mouseenter', () => {
        clearInterval(autoRotate);
    });

    container.addEventListener('mouseleave', () => {
        autoRotate = setInterval(() => {
            if (currentIndex < cards.length - 1) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            updateTestimonials();
        }, 5000);
    });

    // Update testimonials display
    function updateTestimonials() {
        // Update container scroll position
        container.scrollTo({
            left: currentIndex * cardWidth,
            behavior: 'smooth'
        });

        // Update active card
        cards.forEach(card => card.classList.remove('active'));
        cards[currentIndex].classList.add('active');

        // Update dots
        dots.forEach(dot => dot.classList.remove('active'));
        dots[currentIndex].classList.add('active');
    }

    // Handle window resize
    window.addEventListener('resize', function() {
        cardWidth = cards[0].offsetWidth + 30;
        container.scrollTo({
            left: currentIndex * cardWidth,
            behavior: 'auto'
        });
    });
});




