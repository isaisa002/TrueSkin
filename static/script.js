document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const productsContainer = document.getElementById('productsContainer');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const modal = document.getElementById('productModal');
    const closeBtn = document.querySelector('.close-btn');
    
    let currentFilter = 'all';
    let currentSearch = '';

    // Filter button click handlers
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            currentFilter = button.dataset.filter;
            updateProducts();
        });
    });

    // Search input handler
    searchInput.addEventListener('input', debounce(() => {
        currentSearch = searchInput.value;
        updateProducts();
    }, 300));

    // Close modal when clicking the close button
    closeBtn.onclick = function() {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }

    // Close modal when clicking outside
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            document.body.style.overflow = "auto";
        }
    }

    // Close modal with Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = "none";
            document.body.style.overflow = "auto";
        }
    });

    function updateProducts() {
        const queryParams = new URLSearchParams({
            filter: currentFilter,
            search: currentSearch
        });

        fetch(`/api/products?${queryParams}`)
            .then(response => response.json())
            .then(products => {
                productsContainer.innerHTML = products.map(product => `
                    <div class="product-card" onclick="openProductModal(${JSON.stringify(product).replace(/"/g, '&quot;')})">
                        <div class="product-image">
                            <img src="${product.image}" alt="${product.name}">
                        </div>
                        <div class="product-info">
                            <span class="brand">${product.brand}</span>
                            <h2 class="name">${product.name}</h2>
                            <p class="price">$${product.price.toFixed(2)}</p>
                            <p class="description">${product.description}</p>
                            <div class="tags">
                                ${product.categories.map(category => 
                                    `<span class="tag">${category.replace('_', ' ')}</span>`
                                ).join('')}
                            </div>
                        </div>
                    </div>
                `).join('');
            });
    }


//-------------- cart -----------
function showToast() {
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    
    // Hide toast after 2 seconds
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2000);
}

// Update your add to cart function
document.querySelector('.btn-add-cart').addEventListener('click', function(e) {
    e.stopPropagation();
    const product = {
        id: parseInt(document.querySelector('#modalName').dataset.productId),
        name: document.querySelector('#modalName').textContent,
        brand: document.querySelector('#modalBrand').textContent,
        price: parseFloat(document.querySelector('#modalPrice').textContent.replace('$', '')),
        image: document.querySelector('#modalImage').src
    };
    addToCart(product, false);
    showToast();
});

// Update your addToCart function to include the toast
function addToCart(product, redirect = false) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));
    
    // Update cart count
    const countElement = document.getElementById('cartCount');
    countElement.textContent = cart.length;
    
    // Animate cart icon if not redirecting
    if (!redirect) {
        const cartIcon = document.querySelector('.cart-icon');
        cartIcon.classList.add('pop');
        setTimeout(() => cartIcon.classList.remove('pop'), 300);
        
        // Show toast notification
        showToast();
    }

    // Close modal
    document.getElementById('productModal').style.display = 'none';
    document.body.style.overflow = 'auto';

    // Redirect to cart if requested
    if (redirect) {
        window.location.href = '/cart';
    }
}

document.querySelector('.btn-buy-now').addEventListener('click', function(e) {
    e.stopPropagation();
    const product = {
        id: parseInt(document.querySelector('#modalName').dataset.productId),
        name: document.querySelector('#modalName').textContent,
        brand: document.querySelector('#modalBrand').textContent,
        price: parseFloat(document.querySelector('#modalPrice').textContent.replace('$', '')),
        image: document.querySelector('#modalImage').src
    };
    addToCart(product, true);  // true flag triggers redirect to cart
});

// Add this to your DOMContentLoaded event handler
document.addEventListener('DOMContentLoaded', function() {
    // ... your existing code ...
    
    // Initialize cart count
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const countElement = document.getElementById('cartCount');
    countElement.textContent = cart.length;
});

//-------------------------


    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func.apply(this, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Initial load
    updateProducts();
});

// Product modal handler
function openProductModal(product) {
    const modal = document.getElementById('productModal');
    
    // Update modal content
    document.getElementById('modalImage').src = product.image;
    document.getElementById('modalImage').alt = product.name;
    document.getElementById('modalBrand').textContent = product.brand;
    document.getElementById('modalName').textContent = product.name;
    document.getElementById('modalPrice').textContent = `$${product.price.toFixed(2)}`;
    document.getElementById('modalDescription').textContent = product.description;
    
    // Update tags
    document.getElementById('modalTags').innerHTML = product.categories
        .map(category => `<span class="tag">${category.replace('_', ' ')}</span>`)
        .join('');
    
    // Update benefits
    document.getElementById('modalBenefits').innerHTML = product.benefits
        ? product.benefits.map(benefit => `<li>${benefit}</li>`).join('')
        : '<li>Product benefits not available</li>';
    
    // Show modal
    modal.style.display = "block";
    document.body.style.overflow = "hidden"; // Prevent background scrolling
}


// Update the checkout function in cart.js
function checkout() {
    if (cart.length === 0) {
        return;
    }
    window.location.href = '/checkout';  // Or wherever your checkout page is
}

// Update the button click handlers in script.js
document.querySelector('.btn-buy-now').addEventListener('click', function(e) {
    e.stopPropagation();
    const product = {
        id: parseInt(document.querySelector('#modalName').dataset.productId),
        name: document.querySelector('#modalName').textContent,
        brand: document.querySelector('#modalBrand').textContent,
        price: parseFloat(document.querySelector('#modalPrice').textContent.replace('$', '')),
        image: document.querySelector('#modalImage').src
    };
    
    // Just add to cart and redirect without any alert
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));
    
    // Update cart count
    const countElement = document.getElementById('cartCount');
    if (countElement) {
        countElement.textContent = cart.length;
    }
    
    // Close modal
    document.getElementById('productModal').style.display = 'none';
    document.body.style.overflow = 'auto';
    
    // Redirect immediately
    window.location.href = '/cart';
});