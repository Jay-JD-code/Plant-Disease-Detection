// Main JavaScript for Plant Disease Detection App - Modern Enhanced Version

document.addEventListener('DOMContentLoaded', function() {
    // Initialize modern UI enhancements
    initializeModernFeatures();
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // File upload validation
    const fileInput = document.getElementById('file');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                // Check file size (16MB max)
                const maxSize = 16 * 1024 * 1024; // 16MB
                if (file.size > maxSize) {
                    alert('File size must be less than 16MB');
                    fileInput.value = '';
                    return;
                }

                // Check file type
                const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp'];
                if (!allowedTypes.includes(file.type)) {
                    alert('Please select a valid image file (JPEG, PNG, GIF, BMP)');
                    fileInput.value = '';
                    return;
                }

                // Show file size
                const fileSize = (file.size / 1024 / 1024).toFixed(2);
                console.log(`Selected file: ${file.name} (${fileSize} MB)`);
            }
        });
    }

    // Drag and drop functionality
    const uploadForm = document.getElementById('uploadForm');
    if (uploadForm) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadForm.addEventListener(eventName, preventDefaults, false);
        });

        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        ['dragenter', 'dragover'].forEach(eventName => {
            uploadForm.addEventListener(eventName, highlight, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            uploadForm.addEventListener(eventName, unhighlight, false);
        });

        function highlight(e) {
            uploadForm.classList.add('drag-over');
        }

        function unhighlight(e) {
            uploadForm.classList.remove('drag-over');
        }

        uploadForm.addEventListener('drop', handleDrop, false);

        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;

            if (files.length > 0) {
                fileInput.files = files;
                fileInput.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }
    }

    // Progress bar animation
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        const width = bar.style.width || bar.getAttribute('aria-valuenow') + '%';
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = width;
        }, 500);
    });

    // Smooth fade-in for cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all cards for animation
    document.querySelectorAll('.card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(card);
    });

    // Copy to clipboard functionality
    window.copyToClipboard = function(text) {
        navigator.clipboard.writeText(text).then(function() {
            // Show success message
            const toast = document.createElement('div');
            toast.className = 'toast position-fixed top-0 end-0 m-3';
            toast.innerHTML = `
                <div class="toast-header">
                    <i class="fas fa-copy text-success me-2"></i>
                    <strong class="me-auto">Copied</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
                </div>
                <div class="toast-body">
                    Text copied to clipboard!
                </div>
            `;
            document.body.appendChild(toast);
            const bsToast = new bootstrap.Toast(toast);
            bsToast.show();
            
            // Remove toast after it's hidden
            toast.addEventListener('hidden.bs.toast', function() {
                toast.remove();
            });
        });
    };

    // Enhanced search functionality with debounce
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function(e) {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const searchTerm = e.target.value.toLowerCase().trim();
                const classItems = document.querySelectorAll('.class-item');
                let visibleCount = 0;

                classItems.forEach(item => {
                    const className = item.querySelector('.card-title').textContent.toLowerCase();
                    const badges = item.querySelectorAll('.badge');
                    let badgeText = '';
                    badges.forEach(badge => badgeText += badge.textContent.toLowerCase() + ' ');

                    if (className.includes(searchTerm) || badgeText.includes(searchTerm)) {
                        item.style.display = 'block';
                        visibleCount++;
                    } else {
                        item.style.display = 'none';
                    }
                });

                // Show/hide no results message
                let noResultsMsg = document.getElementById('noResultsMessage');
                if (visibleCount === 0 && searchTerm !== '') {
                    if (!noResultsMsg) {
                        noResultsMsg = document.createElement('div');
                        noResultsMsg.id = 'noResultsMessage';
                        noResultsMsg.className = 'col-12 text-center py-5';
                        noResultsMsg.innerHTML = `
                            <div class="text-muted">
                                <i class="fas fa-search fa-3x mb-3"></i>
                                <h4>No results found</h4>
                                <p>Try adjusting your search terms</p>
                            </div>
                        `;
                        document.querySelector('.row:has(.class-item)').appendChild(noResultsMsg);
                    }
                    noResultsMsg.style.display = 'block';
                } else if (noResultsMsg) {
                    noResultsMsg.style.display = 'none';
                }
            }, 300);
        });
    }

    // Add loading state to forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="spinner-border spinner-border-sm me-2"></i>Processing...';
                submitBtn.disabled = true;

                // Re-enable button after a delay (fallback)
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 30000); // 30 seconds
            }
        });
    });

    // Add click-to-zoom functionality for images
    const images = document.querySelectorAll('.img-fluid');
    images.forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            // Create modal for image zoom
            const modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.innerHTML = `
                <div class="modal-dialog modal-lg modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Image Preview</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body text-center">
                            <img src="${img.src}" class="img-fluid" alt="Zoomed image">
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
            const bsModal = new bootstrap.Modal(modal);
            bsModal.show();

            // Remove modal when hidden
            modal.addEventListener('hidden.bs.modal', function() {
                modal.remove();
            });
        });
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 5000);
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl+U to focus upload input
        if (e.ctrlKey && e.key === 'u') {
            e.preventDefault();
            const fileInput = document.getElementById('file');
            if (fileInput) {
                fileInput.click();
            }
        }
        
        // Escape to clear search
        if (e.key === 'Escape' && searchInput) {
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
        }
    });
});

// Utility functions
window.utils = {
    // Format file size
    formatFileSize: function(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    },

    // Validate image file
    isValidImage: function(file) {
        const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp'];
        return validTypes.includes(file.type);
    },

    // Show toast notification
    showToast: function(message, type = 'info') {
        const toastContainer = document.getElementById('toastContainer') || (() => {
            const container = document.createElement('div');
            container.id = 'toastContainer';
            container.className = 'toast-container position-fixed top-0 end-0 p-3';
            document.body.appendChild(container);
            return container;
        })();

        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.innerHTML = `
            <div class="toast-header">
                <i class="fas fa-info-circle text-${type} me-2"></i>
                <strong class="me-auto">Notification</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        `;
        
        toastContainer.appendChild(toast);
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();

        toast.addEventListener('hidden.bs.toast', function() {
            toast.remove();
        });
    }
};

// Modern UI enhancement functions
function initializeModernFeatures() {
    // Add smooth scrolling behavior
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // Initialize responsive image handling
    initializeResponsiveImages();
    
    // Add modern touch interactions
    initializeTouchInteractions();
    
    // Initialize performance optimizations
    initializePerformanceOptimizations();
    
    // Add accessibility enhancements
    initializeAccessibility();
}

function initializeResponsiveImages() {
    // Lazy load images with intersection observer
    const lazyImages = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });
    
    lazyImages.forEach(img => imageObserver.observe(img));
    
    // Add responsive image error handling
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.className = 'image-placeholder d-flex align-items-center justify-content-center bg-light';
            placeholder.style.height = '200px';
            placeholder.innerHTML = '<i class="fas fa-image text-muted fa-2x"></i>';
            this.parentNode.replaceChild(placeholder, this);
        });
    });
}

function initializeTouchInteractions() {
    // Add touch-friendly interactions for mobile devices
    if ('ontouchstart' in window) {
        document.body.classList.add('touch-device');
        
        // Improve button touch targets
        document.querySelectorAll('.btn').forEach(btn => {
            btn.style.minHeight = '44px';
            btn.style.minWidth = '44px';
        });
        
        // Add touch feedback to cards
        document.querySelectorAll('.card').forEach(card => {
            card.addEventListener('touchstart', function() {
                this.style.transform = 'scale(0.98)';
            });
            
            card.addEventListener('touchend', function() {
                this.style.transform = '';
            });
        });
    }
}

function initializePerformanceOptimizations() {
    // Debounce resize events
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            // Trigger custom resize event for components that need it
            window.dispatchEvent(new CustomEvent('optimizedResize'));
        }, 100);
    });
    
    // Optimize scroll events
    let scrollTimeout;
    let isScrolling = false;
    
    window.addEventListener('scroll', function() {
        if (!isScrolling) {
            window.requestAnimationFrame(function() {
                // Handle scroll-based animations
                updateScrollBasedAnimations();
                isScrolling = false;
            });
            isScrolling = true;
        }
    });
    
    // Preload critical resources
    const criticalImages = document.querySelectorAll('[data-preload]');
    criticalImages.forEach(img => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = img.src || img.dataset.src;
        document.head.appendChild(link);
    });
}

function updateScrollBasedAnimations() {
    const scrolled = window.pageYOffset;
    const rate = scrolled * -0.5;
    
    // Parallax effect for hero section
    const hero = document.querySelector('.hero-section');
    if (hero) {
        hero.style.transform = `translateY(${rate}px)`;
    }
    
    // Update navbar on scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (scrolled > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
}

function initializeAccessibility() {
    // Add keyboard navigation support
    document.addEventListener('keydown', function(e) {
        // Tab navigation improvements
        if (e.key === 'Tab') {
            document.body.classList.add('keyboard-navigation');
        }
    });
    
    document.addEventListener('mousedown', function() {
        document.body.classList.remove('keyboard-navigation');
    });
    
    // Add ARIA labels to dynamic content
    const dynamicElements = document.querySelectorAll('[data-dynamic]');
    dynamicElements.forEach(element => {
        if (!element.getAttribute('aria-label')) {
            element.setAttribute('aria-label', element.textContent || 'Interactive element');
        }
    });
    
    // Add focus indicators
    const focusableElements = document.querySelectorAll('button, input, select, textarea, a[href]');
    focusableElements.forEach(element => {
        element.addEventListener('focus', function() {
            this.style.outline = '2px solid var(--accent-green)';
            this.style.outlineOffset = '2px';
        });
        
        element.addEventListener('blur', function() {
            this.style.outline = '';
            this.style.outlineOffset = '';
        });
    });
}

// Mobile-first responsive utilities
window.responsive = {
    // Check if device is mobile
    isMobile: function() {
        return window.innerWidth <= 768;
    },
    
    // Check if device is tablet
    isTablet: function() {
        return window.innerWidth > 768 && window.innerWidth <= 1024;
    },
    
    // Check if device is desktop
    isDesktop: function() {
        return window.innerWidth > 1024;
    },
    
    // Adaptive behavior based on screen size
    adaptiveContent: function() {
        const isMobile = this.isMobile();
        
        // Adjust card layouts
        document.querySelectorAll('.card').forEach(card => {
            if (isMobile) {
                card.classList.add('mobile-optimized');
            } else {
                card.classList.remove('mobile-optimized');
            }
        });
        
        // Adjust button sizes
        document.querySelectorAll('.btn').forEach(btn => {
            if (isMobile && !btn.classList.contains('btn-sm')) {
                btn.classList.add('btn-mobile');
            } else {
                btn.classList.remove('btn-mobile');
            }
        });
    }
};

// Initialize responsive behavior on load and resize
window.addEventListener('load', window.responsive.adaptiveContent.bind(window.responsive));
window.addEventListener('optimizedResize', window.responsive.adaptiveContent.bind(window.responsive));
