/**
 * HeartSeg AI - Main JavaScript
 * Handles: Loader, Navbar, Mobile Menu, Smooth Scroll, Counters, AOS, Back to Top
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // =========================================
    // Loader
    // =========================================
    const loader = document.getElementById('loader');
    
    window.addEventListener('load', function() {
        setTimeout(() => {
            loader.classList.add('hidden');
        }, 800);
    });
    
    // =========================================
    // Navbar Scroll Effect
    // =========================================
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
    
    // =========================================
    // Mobile Menu Toggle
    // =========================================
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
        
        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });
    }
    
    // =========================================
    // Active Nav Link on Scroll
    // =========================================
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.nav-links a');
    
    window.addEventListener('scroll', function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;
            
            if (pageYOffset >= sectionTop && pageYOffset < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href') === '#' + current) {
                item.classList.add('active');
            }
        });
    });
    
    // =========================================
    // Animated Counters
    // =========================================
    const counters = document.querySelectorAll('.counter');
    const speed = 200;
    
    const animateCounter = (counter) => {
        const target = parseFloat(counter.getAttribute('data-target'));
        const isDecimal = target % 1 !== 0;
        const count = parseFloat(counter.innerText);
        const increment = target / speed;
        
        if (count < target) {
            const next = count + increment;
            counter.innerText = isDecimal ? next.toFixed(1) : Math.ceil(next);
            setTimeout(() => animateCounter(counter), 15);
        } else {
            counter.innerText = target;
        }
    };
    
    // Trigger counters when in view
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                animateCounter(counter);
                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => counterObserver.observe(counter));
    
    // =========================================
    // Back to Top Button
    // =========================================
    const backToTop = document.getElementById('backToTop');
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 500) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });
    
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // =========================================
    // Initialize AOS (Animate On Scroll)
    // =========================================
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 100,
            easing: 'ease-out-cubic'
        });
    }
    
    // =========================================
    // Smooth Scroll for Anchor Links
    // =========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
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
    // Performance Chart Animation on Scroll
    // =========================================
    const perfCharts = document.querySelectorAll('.perf-chart .progress');
    
    const chartObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const circle = entry.target;
                const percent = circle.style.getPropertyValue('--percent');
                circle.style.strokeDashoffset = `calc(283 - (283 * ${percent}) / 100)`;
                chartObserver.unobserve(circle);
            }
        });
    }, { threshold: 0.5 });
    
    perfCharts.forEach(chart => chartObserver.observe(chart));
    
    // =========================================
    // Parallax Effect for Hero Orbs
    // =========================================
    const orbs = document.querySelectorAll('.gradient-orb');
    
    window.addEventListener('mousemove', function(e) {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        orbs.forEach((orb, index) => {
            const speed = (index + 1) * 20;
            const xOffset = (x - 0.5) * speed;
            const yOffset = (y - 0.5) * speed;
            
            orb.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
        });
    });
    
    // =========================================
    // Console Welcome Message
    // =========================================
    console.log('%c HeartSeg AI ', 'background: linear-gradient(135deg, #0ea5e9, #8b5cf6); color: white; font-size: 20px; font-weight: bold; padding: 8px 16px; border-radius: 8px;');
    console.log('%cDeveloped by Sriram V at Saveetha Engineering College', 'color: #94a3b8; font-size: 12px;');
    console.log('%cGitHub: https://github.com/Darkwebnew/Miniproject', 'color: #0ea5e9; font-size: 12px;');
});