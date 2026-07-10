/**
 * HeartSeg AI 2026 — Main JavaScript
 * Handles: Loader, Navbar, Mobile Menu, Smooth Scroll, 
 * Counters, Intersection Observer, Back to Top, Parallax
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // =========================================
    // Loader
    // =========================================
    const loader = document.getElementById('loader');
    
    if (loader) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                loader.classList.add('hidden');
            }, 600);
        });
    }
    
    // =========================================
    // Navbar Scroll Effect
    // =========================================
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;
    
    if (navbar) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;
            
            if (currentScroll > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
            
            lastScroll = currentScroll;
        });
    }
    
    // =========================================
    // Mobile Menu Toggle
    // =========================================
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
        
        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
        
        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.classList.remove('menu-open');
            }
        });
    }
    
    // =========================================
    // Active Nav Link on Scroll
    // =========================================
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.nav-links a[href^="#"]');
    
    if (sections.length && navItems.length) {
        const observerOptions = {
            root: null,
            rootMargin: '-80px 0px -60% 0px',
            threshold: 0
        };
        
        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navItems.forEach(item => {
                        item.classList.remove('active');
                        if (item.getAttribute('href') === `#${id}`) {
                            item.classList.add('active');
                        }
                    });
                }
            });
        }, observerOptions);
        
        sections.forEach(section => sectionObserver.observe(section));
    }
    
    // =========================================
    // Animated Counters
    // =========================================
    const counters = document.querySelectorAll('.counter');
    
    if (counters.length) {
        const animateCounter = (counter) => {
            const target = parseFloat(counter.dataset.target);
            const duration = 2000;
            const start = performance.now();
            const isDecimal = target % 1 !== 0;
            
            const update = (now) => {
                const elapsed = now - start;
                const progress = Math.min(elapsed / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
                const current = eased * target;
                
                counter.textContent = isDecimal ? current.toFixed(1) : Math.floor(current);
                
                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                    counter.textContent = target;
                }
            };
            
            requestAnimationFrame(update);
        };
        
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(counter => counterObserver.observe(counter));
    }
    
    // =========================================
    // Performance Chart Animation
    // =========================================
    const progressRings = document.querySelectorAll('.ring-progress');
    
    if (progressRings.length) {
        const chartObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const ring = entry.target;
                    const percent = ring.style.getPropertyValue('--percent');
                    // The CSS handles the transition, we just need to trigger it
                    ring.style.strokeDashoffset = `calc(283 - (283 * ${percent}) / 100)`;
                    chartObserver.unobserve(ring);
                }
            });
        }, { threshold: 0.5 });
        
        progressRings.forEach(ring => chartObserver.observe(ring));
    }
    
    // =========================================
    // Back to Top Button
    // =========================================
    const backToTop = document.getElementById('backToTop');
    
    if (backToTop) {
        const toggleVisibility = () => {
            if (window.pageYOffset > 500) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        };
        
        window.addEventListener('scroll', toggleVisibility, { passive: true });
        
        backToTop.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // =========================================
    // Smooth Scroll for Anchor Links
    // =========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const offset = 80;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // =========================================
    // Parallax Effect for Neural Orbs
    // =========================================
    const orbs = document.querySelectorAll('.neural-orb');
    
    if (orbs.length && !window.matchMedia('(pointer: coarse)').matches) {
        let ticking = false;
        
        window.addEventListener('mousemove', (e) => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const x = e.clientX / window.innerWidth;
                    const y = e.clientY / window.innerHeight;
                    
                    orbs.forEach((orb, index) => {
                        const speed = (index + 1) * 15;
                        const xOffset = (x - 0.5) * speed;
                        const yOffset = (y - 0.5) * speed;
                        orb.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
                    });
                    
                    ticking = false;
                });
                
                ticking = true;
            }
        });
    }
    
    // =========================================
    // Reveal on Scroll (AOS replacement)
    // =========================================
    const revealElements = document.querySelectorAll('[data-reveal]');
    
    if (revealElements.length) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        revealElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            revealObserver.observe(el);
        });
        
        // Add revealed styles
        const style = document.createElement('style');
        style.textContent = `
            [data-reveal].revealed {
                opacity: 1 !important;
                transform: translateY(0) !important;
            }
        `;
        document.head.appendChild(style);
    }
    
    // =========================================
    // Card Tilt Effect (Desktop only)
    // =========================================
    const tiltCards = document.querySelectorAll('[data-tilt]');
    
    if (tiltCards.length && !window.matchMedia('(pointer: coarse)').matches) {
        tiltCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
            });
        });
    }
    
    // =========================================
    // Form Validation Helpers
    // =========================================
    const forms = document.querySelectorAll('form[data-validate]');
    
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    field.addEventListener('input', () => {
                        field.classList.remove('error');
                    }, { once: true });
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
    
    // =========================================
    // Console Welcome
    // =========================================
    console.log(
        '%c HeartSeg AI ',
        'background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; font-size: 20px; font-weight: bold; padding: 8px 16px; border-radius: 8px;'
    );
    console.log(
        '%c2026 Edition — AI-Powered Cardiac MRI Segmentation',
        'color: #94a3b8; font-size: 12px;'
    );
    console.log(
        '%cGitHub: https://github.com/Darkwebnew/Miniproject',
        'color: #818cf8; font-size: 12px;'
    );
});

// =========================================
// Utility: Debounce function
// =========================================
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// =========================================
// Utility: Throttle function
// =========================================
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}