document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const productItems = document.querySelectorAll(".product");

    searchInput.addEventListener("input", function() {
        const searchTerm = searchInput.value.trim().toLowerCase();

        if (searchTerm === "") {
            productItems.forEach(function(item) {
                item.style.display = "block";
            });
        } else {
            productItems.forEach(function(item) {
                const productName = item.querySelector(".product-name").innerText.toLowerCase();
                if (productName.includes(searchTerm)) {
                    item.style.display = "block";
                } else {
                    item.style.display = "none";
                }
            });
        }
    });

    productItems.forEach(function(item) {
        item.addEventListener("click", function() {
            const detailUrl = item.dataset.detailUrl;
            if (detailUrl) {
                window.location.href = detailUrl;
            }
        });
    });
});
