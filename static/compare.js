let products = [];

fetch('/api/products')
    .then(response => response.json())
    .then(data => {
        products = data;
    })
    .catch(error => console.error('Error fetching products:', error));

function displaySearchResults(searchInput, resultsContainer, productContainer, otherProductContainer) {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredProducts = products.filter(product => 
        product.name.toLowerCase().includes(searchTerm) || 
        product.brand.toLowerCase().includes(searchTerm)
    );

    resultsContainer.innerHTML = '';
    filteredProducts.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <h3>${product.brand}</h3>
            <p>${product.name}</p>
            <p>$${product.price}</p>
        `;
        productCard.onclick = () => {
            displayProduct(product, productContainer, otherProductContainer);
            resultsContainer.innerHTML = '';
            searchInput.value = '';
        };
        resultsContainer.appendChild(productCard);
    });
}

function displayProduct(product, container, otherContainer) {
    const otherProduct = otherContainer.dataset.product ? JSON.parse(otherContainer.dataset.product) : null;
    
    container.innerHTML = `
        <img src="${product.image}" alt="${product.name}" class="product-image">
        <h2>${product.brand}</h2>
        <h3>${product.name}</h3>
        <div class="product-detail ${otherProduct && product.price !== otherProduct.price ? 'highlight-difference' : ''}">
            <strong>Price:</strong> $${product.price}
        </div>
        <div class="product-detail">
            <strong>Description:</strong> ${product.description}
        </div>
        <div class="product-detail ${otherProduct && JSON.stringify(product.categories) !== JSON.stringify(otherProduct.categories) ? 'highlight-difference' : ''}">
            <strong>Categories:</strong> ${product.categories.join(', ')}
        </div>
        <div class="product-detail">
            <strong>Benefits:</strong>
            <ul>
                ${product.benefits.map(benefit => `<li>${benefit}</li>`).join('')}
            </ul>
        </div>
        <div class="product-detail ${otherProduct && product.transparency !== otherProduct.transparency ? 'highlight-difference' : ''}">
            <strong>Transparency Rating:</strong> ${product.transparency}/5
        </div>
    `;
    container.dataset.product = JSON.stringify(product);
}

document.addEventListener('DOMContentLoaded', () => {
    const dropdown1 = document.getElementById('dropdown1');
    const dropdown2 = document.getElementById('dropdown2');
    const search1 = document.getElementById('search1');
    const search2 = document.getElementById('search2');

    dropdown1.addEventListener('click', () => {
        displaySearchResults(
            search1,
            document.getElementById('results1'),
            document.getElementById('product1'),
            document.getElementById('product2')
        );
    });

    dropdown2.addEventListener('click', () => {
        displaySearchResults(
            search2,
            document.getElementById('results2'),
            document.getElementById('product2'),
            document.getElementById('product1')
        );
    });

    search1.addEventListener('input', (e) => {
        displaySearchResults(
            e.target,
            document.getElementById('results1'),
            document.getElementById('product1'),
            document.getElementById('product2')
        );
    });

    search2.addEventListener('input', (e) => {
        displaySearchResults(
            e.target,
            document.getElementById('results2'),
            document.getElementById('product2'),
            document.getElementById('product1')
        );
    });
});