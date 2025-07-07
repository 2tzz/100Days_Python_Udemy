
const resumeBtns = document.querySelectorAll('.resume-btn');

resumeBtns.forEach((btn , idx) => {
    btn.addEventListener('click' , () => {
        const resumeDetails = document.querySelectorAll('.resume-detail');

        resumeBtns.forEach(btn => {
            btn.classList.remove('active');
        });
        btn.classList.add('active');

        resumeDetails.forEach(detail => {
            detail.classList.remove('active');
        });
        resumeDetails[idx].classList.add('active');

    });
}) ;




const arrowRight = document.querySelector('.portfolio-box .navigation .arrow-right');
const arrowLeft = document.querySelector('.portfolio-box .navigation .arrow-left');
const imgSlide = document.querySelector('.portfolio-carousel .img-slide');
const slides = document.querySelectorAll('.portfolio-carousel .img-item');
const portfolioDetails = document.querySelectorAll('.portfolio-detail');
let index = 0;

const updatePortfolio = () => {
    // Update image slide position
    imgSlide.style.transform = `translateX(calc(${index * -100}% - ${index * 2}rem))`;
    
    // Update portfolio details
    portfolioDetails.forEach((detail, i) => {
        detail.classList.toggle('active', i === index);
    });
};

arrowRight.addEventListener('click', () => {
    if (index < slides.length - 1) {
        index++;
    } else {
        index = 0;
    }
    updatePortfolio();
});

arrowLeft.addEventListener('click', () => {
    if (index > 0) {
        index--;
    } else {
        index = slides.length - 1;
    }
    updatePortfolio();
});

// Initialize
updatePortfolio();





document.querySelector('.btn[download]').addEventListener('click', function() {
    gtag('event', 'CV_download', {
        'event_category': 'Engagement',
        'event_label': 'CV Download'
    });
});



// MENU TOGGLE
const menuIcon = document.querySelector('#menu-icon');
const navbar = document.querySelector('nav');

menuIcon?.addEventListener('click', () => {
    navbar.classList.toggle('active');
});

// HIGHLIGHT NAV LINKS BASED ON URL PATH
const navLinks = document.querySelectorAll('nav a');
const currentPath = window.location.pathname;

navLinks.forEach(link => {
    if (link.href.includes(currentPath)) {
        link.classList.add('active');
    }
});



document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');

        // Check if link is same-origin
        if (href.startsWith('/')) {
            e.preventDefault();
            document.body.classList.remove('fade-in');
            document.body.style.opacity = '0';
            setTimeout(() => {
                window.location.href = href;
            }, 300); // match this to your transition duration
        }
    });
});

// Add fade-in class on page load
window.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("fade-in");
});

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll('nav a');

    // Normalize paths by removing trailing slashes
    const normalize = path => path.replace(/\/+$/, '') || '/';
    const currentPath = normalize(window.location.pathname);

    navLinks.forEach(link => {
        const linkPath = normalize(new URL(link.href).pathname);
        if (linkPath === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
