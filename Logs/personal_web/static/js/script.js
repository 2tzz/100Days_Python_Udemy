// Resume tab switching
const resumeBtns = document.querySelectorAll('.resume-btn');

resumeBtns.forEach((btn, idx) => {
    btn.addEventListener('click', () => {
        const resumeDetails = document.querySelectorAll('.resume-detail');

        resumeBtns.forEach(btn => btn.classList.remove('active'));
        btn.classList.add('active');

        resumeDetails.forEach(detail => detail.classList.remove('active'));
        resumeDetails[idx].classList.add('active');
    });
});

// Portfolio carousel
const arrowRight = document.querySelector('.portfolio-box .navigation .arrow-right');
const arrowLeft = document.querySelector('.portfolio-box .navigation .arrow-left');
const imgSlide = document.querySelector('.portfolio-carousel .img-slide');
const slides = document.querySelectorAll('.portfolio-carousel .img-item');
const portfolioDetails = document.querySelectorAll('.portfolio-detail');
let index = 0;

const updatePortfolio = () => {
    imgSlide.style.transform = `translateX(calc(${index * -100}% - ${index * 2}rem))`;

    portfolioDetails.forEach((detail, i) => {
        detail.classList.toggle('active', i === index);
    });
};

arrowRight?.addEventListener('click', () => {
    index = (index + 1) % slides.length;
    updatePortfolio();
});

arrowLeft?.addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    updatePortfolio();
});

updatePortfolio(); // Initialize on load

// CV download tracking
document.querySelector('.btn[download]')?.addEventListener('click', function () {
    gtag('event', 'CV_download', {
        'event_category': 'Engagement',
        'event_label': 'CV Download'
    });
});

// Initialize EmailJS
(function () {
    emailjs.init('R4PggCaUW0dBRPQWo', {
        host: 'smtp.gmail.com',
        port: 465,
        secure: true
    });
})();

// Contact form submission
document.getElementById('contactForm')?.addEventListener('submit', function (event) {
    event.preventDefault();

    if (grecaptcha.getResponse().length === 0) {
        alert('Please complete the reCAPTCHA');
        return;
    }

    emailjs.sendForm('service_9peacgb', 'template_0jelvoo', this)
        .then(() => {
            alert('Message sent successfully!');
            this.reset();
            grecaptcha.reset();
        }, (error) => {
            console.error('EmailJS Error:', error);
            alert(`Failed to send message: ${error.text}`);
        });
});
