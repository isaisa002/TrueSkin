document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const productsContainer = document.getElementById("productsContainer");
  const filterButtons = document.querySelectorAll(".filter-btn");
  const modal = document.getElementById("productModal");
  const closeBtn = document.querySelector(".close-btn");

  let currentFilter = "all";
  let currentSearch = "";

  // Filter button click handlers
  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      filterButtons.forEach((btn) => btn.classList.remove("active"));
      button.classList.add("active");
      currentFilter = button.dataset.filter;
      updateProducts();
    });
  });

  // Search input handler
  searchInput.addEventListener(
    "input",
    debounce(() => {
      currentSearch = searchInput.value;
      updateProducts();
    }, 300)
  );

  // Close modal when clicking the close button
  closeBtn.onclick = function () {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  };

  // Close modal when clicking outside
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  };

  // Close modal with Escape key
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && modal.style.display === "block") {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  });

  function updateProducts() {
    const queryParams = new URLSearchParams({
      filter: currentFilter,
      search: currentSearch,
    });

    fetch(`/api/products?${queryParams}`)
      .then((response) => response.json())
      .then((products) => {
        productsContainer.innerHTML = products
          .map(
            (product) => `
                    <div class="product-card" onclick="openProductModal(${JSON.stringify(
                      product
                    ).replace(/"/g, "&quot;")})">
                        <div class="product-image">
                            <img src="${product.image}" alt="${product.name}">
                        </div>
                        <div class="product-info">
                            <span class="brand">${product.brand}</span>
                            <h2 class="name">${product.name}</h2>
                            <p class="price">$${product.price.toFixed(2)}</p>
                            <p class="description">${product.description}</p>
                            <div class="tags">
                                ${product.categories
                                  .map(
                                    (category) =>
                                      `<span class="tag">${category.replace(
                                        "_",
                                        " "
                                      )}</span>`
                                  )
                                  .join("")}
                            </div>
                        </div>
                    </div>
                `
          )
          .join("");
      });
  }

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
  const modal = document.getElementById("productModal");

  // Update modal content
  document.getElementById("modalImage").src = product.image;
  document.getElementById("modalImage").alt = product.name;
  document.getElementById("modalBrand").textContent = product.brand;
  document.getElementById("modalName").textContent = product.name;
  document.getElementById("modalPrice").textContent = `$${product.price.toFixed(
    2
  )}`;
  document.getElementById("modalDescription").textContent = product.description;

  // Update tags
  document.getElementById("modalTags").innerHTML = product.categories
    .map((category) => `<span class="tag">${category.replace("_", " ")}</span>`)
    .join("");

  // Update benefits
  document.getElementById("modalBenefits").innerHTML = product.benefits
    ? product.benefits.map((benefit) => `<li>${benefit}</li>`).join("")
    : "<li>Product benefits not available</li>";

  // Show modal
  modal.style.display = "block";
  document.body.style.overflow = "hidden"; // Prevent background scrolling
}

// Update the checkout function in cart.js
function checkout() {
  if (cart.length === 0) {
    return;
  }
  window.location.href = "/checkout"; // Or wherever your checkout page is
}

// Open and display the reviews on porduct modal

// Get element of product
function openProductModal(product) {
  //save the current product so can add the added rating
  window.current_product = product;

  document.getElementById("modalImage").src = product.image;
  document.getElementById("modalBrand").textContent = product.brand;
  document.getElementById("modalName").textContent = product.name;
  document.getElementById("modalPrice").textContent = `$${product.price.toFixed(
    2
  )}`;
  document.getElementById("modalDescription").textContent = product.description;

  //tags
  const tags_container = document.getElementById("modalTags");
  tags_container.innerHTML = ""; // Clear existing tags
  product.categories.forEach((tag) => {
    const tag_element = document.createElement("span");
    tag_element.className = "tag";
    tag_element.textContent = tag.replace("_", " ");
    tags_container.appendChild(tag_element);
  });

  //benifits
  const benefits_container = document.getElementById("modalBenefits");
  benefits_container.innerHTML = ""; // Clear existing benefits
  product.benefits.forEach((benefit) => {
    const benefitItem = document.createElement("li");
    benefitItem.textContent = benefit;
    benefits_container.appendChild(benefitItem);
  });

  // average of ratings
  const average_container = document.getElementById("modalAverageRating");
  if (product.reviews && product.reviews.length > 0) {
    const totalRating = product.reviews.reduce(
      (sum, review) => sum + review.rating,
      0
    );
    const averageRating = totalRating / product.reviews.length;
    average_container.innerHTML = `
        ${"⭐".repeat(Math.floor(averageRating))} 
        (${averageRating.toFixed(1)} / 5)
      `;
  } else {
    average_container.innerHTML = "No reviews available for this product yet.";
  }

  const modal = document.getElementById("productModal");
  modal.style.display = "block";

  // view more button
  const viewMoreButton = document.getElementById("viewMoreReviews");
  viewMoreButton.onclick = () => openReviewsPopup(product);
}

// open the review pop up
function openReviewsPopup(product) {
  const reviewsList = document.getElementById("allReviewsList");
  reviewsList.innerHTML = ""; // Clear existing reviews

  if (product.reviews && product.reviews.length > 0) {
    product.reviews.forEach((review) => {
      const reviewItem = document.createElement("li");
      reviewItem.innerHTML = `
          <strong>${review.name}</strong> - ${"⭐".repeat(review.rating)}
          <p>${review.comment}</p>
        `;
      reviewsList.appendChild(reviewItem);
    });
  } else {
    reviewsList.innerHTML = "<li>No reviews available for this product.</li>";
  }
  const reviewsModal = document.getElementById("reviewsModal");
  reviewsModal.style.display = "block";
}
document.getElementById("closeReviewsModal").onclick = function () {
  document.getElementById("reviewsModal").style.display = "none";
};
document.querySelector(".close-btn").onclick = function () {
  document.getElementById("productModal").style.display = "none";
};

// Add a review
document.getElementById("addReviewButton").addEventListener("click", () => {
  document.getElementById("addReviewModal").style.display = "block";
});
document.getElementById("closeAddReviewModal").addEventListener("click", () => {
  document.getElementById("addReviewModal").style.display = "none";
});

// Form for review
document.getElementById("addReviewForm").addEventListener("submit", (event) => {
  //prevent refresh
  event.preventDefault();
  const name = document.getElementById("reviewerName").value;
  const rating = parseInt(document.getElementById("reviewRating").value);
  const comment = document.getElementById("reviewComment").value;

  //if no input need to write all the fields
  if (!name || !rating || !comment) {
    alert("Please fill all the necessary fields");
    return;
  }

  //add the review to the current product
  const currentProduct = window.current_product;
  if (currentProduct) {
    currentProduct.reviews.push({ name, rating, comment });
    openProductModal(currentProduct);
    document.getElementById("addReviewModal").style.display = "none";
    //clear field when added
    document.getElementById("addReviewForm").reset();
  } else {
    alert("An error occurred. Please try again...");
  }
});
