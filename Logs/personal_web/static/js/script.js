// const navLinks = document.querySelectorAll('header nav a');
// const sections = document.querySelectorAll('section');
// const logoLink = document.querySelector('.logo');



// const removeActiveLinks = () => {

//     const header = document.querySelector('header')
//     const barsBox = document.querySelector('.bars-box')

//     header.classList.remove('active');
//     setTimeout(() => {
//         header.classList.add('active');
//     }, 1100);

//     navLinks.forEach(link => {
//         link.classList.remove('active');
//     });

//     barsBox.classList.remove('active');
//     setTimeout(() => {
//         barsBox.classList.add('active');
//     }, 1100);
// };

// const removeActiveSections = () => {
//     sections.forEach(section => {
//         section.classList.remove('active');
//     });
// };



// navLinks.forEach((link, idx) => {
//     link.addEventListener('click', (e) => {
//         e.preventDefault();
        
//         if (!link.classList.contains('active')) {
//             // Start transition out
//             removeActiveLinks();
//             removeActiveSections();
            
//             // Add active class to clicked link
//             link.classList.add('active');
            
//             // Delay section activation to match navbar animation
//             setTimeout(() => {
//                 sections[idx].classList.add('active');
//                 sections[idx].scrollIntoView({
//                     behavior: 'smooth',
//                     block: 'start'
//                 });
//             }, 2000); // Matches navbar animation duration
//         }
//     });
// });


// logoLink.addEventListener('click', (e) => {
//     e.preventDefault();
    
//     if (!navLinks[0].classList.contains('active')) {
//         removeActiveLinks();
//         removeActiveSections();
        
//         navLinks[0].classList.add('active');
        
//         setTimeout(() => {
//             sections[0].classList.add('active');
//             sections[0].scrollIntoView({
//                 behavior: 'smooth',
//                 block: 'start'
//             });
//         }, 2000); // Matches navbar animation duration
//     }
// });

// window.addEventListener('DOMContentLoaded', () => {
//     navLinks[0].classList.add('active');
//     sections[0].classList.add('active');
// });


// //resume


// const resumeBtns = document.querySelectorAll('.resume-btn');

// resumeBtns.forEach((btn , idx) => {
//     btn.addEventListener('click' , () => {
//         const resumeDetails = document.querySelectorAll('.resume-detail');

//         resumeBtns.forEach(btn => {
//             btn.classList.remove('active');
//         });
//         btn.classList.add('active');

//         resumeDetails.forEach(detail => {
//             detail.classList.remove('active');
//         });
//         resumeDetails[idx].classList.add('active');

//     });
// }) ;




// const arrowRight = document.querySelector('.portfolio-box .navigation .arrow-right');
// const arrowLeft = document.querySelector('.portfolio-box .navigation .arrow-left');
// const imgSlide = document.querySelector('.portfolio-carousel .img-slide');
// const slides = document.querySelectorAll('.portfolio-carousel .img-item');
// const portfolioDetails = document.querySelectorAll('.portfolio-detail');
// let index = 0;

// const updatePortfolio = () => {
//     // Update image slide position
//     imgSlide.style.transform = `translateX(calc(${index * -100}% - ${index * 2}rem))`;
    
//     // Update portfolio details
//     portfolioDetails.forEach((detail, i) => {
//         detail.classList.toggle('active', i === index);
//     });
// };

// arrowRight.addEventListener('click', () => {
//     if (index < slides.length - 1) {
//         index++;
//     } else {
//         index = 0;
//     }
//     updatePortfolio();
// });

// arrowLeft.addEventListener('click', () => {
//     if (index > 0) {
//         index--;
//     } else {
//         index = slides.length - 1;
//     }
//     updatePortfolio();
// });

// // Initialize
// updatePortfolio();




// // Add to your script.js
// document.querySelector('.btn[download]').addEventListener('click', function() {
//     gtag('event', 'CV_download', {
//         'event_category': 'Engagement',
//         'event_label': 'CV Download'
//     });
// });


// // Initialize EmailJS with your User ID
// (function() {
//     emailjs.init('R4PggCaUW0dBRPQWo', {
//     host: 'smtp.gmail.com',
//     port: 465,
//     secure: true
//     });
// });

// document.getElementById('contactForm').addEventListener('submit', function(event) {
//     event.preventDefault();
    
//     // Validate reCAPTCHA first
//     if (grecaptcha.getResponse().length === 0) {
//         alert('Please complete the reCAPTCHA');
//         return;
//     }

//     emailjs.sendForm('service_9peacgb', 'template_0jelvoo', this)
//         .then(() => {
//             alert('Message sent successfully!');
//             this.reset();
//             grecaptcha.reset();
//         }, (error) => {
//             console.error('EmailJS Error:', error);
//             alert(`Failed to send message: ${error.text}`);
//         });
// });



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

// RESUME TABS TOGGLE
const resumeBtns = document.querySelectorAll('.resume-btn');
const resumeDetails = document.querySelectorAll('.resume-detail');

resumeBtns?.forEach((btn, i) => {
    btn.addEventListener('click', () => {
        // Remove active classes
        resumeBtns.forEach(b => b.classList.remove('active'));
        resumeDetails.forEach(detail => detail.classList.remove('active'));

        // Activate current
        btn.classList.add('active');
        resumeDetails[i].classList.add('active');
    });
});

// PORTFOLIO CAROUSEL (if exists)
const carousels = document.querySelectorAll('.portfolio-carousel');

carousels?.forEach(carousel => {
    const slides = carousel.querySelector('.img-slide');
    const leftBtn = carousel.closest('.portfolio-box')?.querySelector('.arrow-left');
    const rightBtn = carousel.closest('.portfolio-box')?.querySelector('.arrow-right');

    let index = 0;
    const slideCount = slides?.children.length || 0;

    const updateCarousel = () => {
        slides.style.transform = `translateX(-${index * 100}%)`;
    };

    rightBtn?.addEventListener('click', () => {
        if (index < slideCount - 1) {
            index++;
            updateCarousel();
        }
    });

    leftBtn?.addEventListener('click', () => {
        if (index > 0) {
            index--;
            updateCarousel();
        }
    });
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
