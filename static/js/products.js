// products.js

document.addEventListener("DOMContentLoaded", async function() {
    const response = await fetch("/products/");
    const products = await response.json();

    const catalogContainer = document.getElementById("catalog");
    products.forEach(product => {
        const rowDiv = document.createElement("div");
        rowDiv.classList.add("row");

        const productDiv = document.createElement("div");
        productDiv.classList.add("product");

        const img = document.createElement("img");
        img.src = product.product_photo_blob;
        img.alt = product.product_name;
        img.width = 150;
        img.height = 150;
        productDiv.appendChild(img);

        const productInfoDiv = document.createElement("div");
        productInfoDiv.classList.add("product-info");

        const priceP = document.createElement("p");
        priceP.classList.add("price");
        priceP.textContent = `Цена: $${product.product_price}`;
        productInfoDiv.appendChild(priceP);

        const productNameP = document.createElement("p");
        productNameP.classList.add("product-name");
        productNameP.textContent = product.product_name;
        productInfoDiv.appendChild(productNameP);

        const addButton = document.createElement("button");
        addButton.classList.add("add");
        addButton.textContent = "Добавить";
        productInfoDiv.appendChild(addButton);

        productDiv.appendChild(productInfoDiv);
        rowDiv.appendChild(productDiv);
        catalogContainer.appendChild(rowDiv);
    });
});
