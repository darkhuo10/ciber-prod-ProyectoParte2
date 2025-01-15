document.addEventListener('DOMContentLoaded', () => {
    const loadProductsButton = document.getElementById('loadProducts');
    const productsTableBody = document.getElementById('productsTable').getElementsByTagName('tbody')[0];

    let products = [
        { id: 1, name: "Pizza Margarita", description: "Queso, tomate, y albahaca", price: 8.50, allergens: "Gluten, Lactosa", ingredients: "Harina, Queso, Tomate, Albahaca" },
        { id: 2, name: "Hamburguesa", description: "Carne de vacuno, queso, lechuga y tomate", price: 9.00, allergens: "Gluten, Lactosa", ingredients: "Pan, Carne de vacuno, Queso, Lechuga, Tomate" },
        { id: 3, name: "Ensalada César", description: "Pollo, lechuga, crutones y aderezo César", price: 7.00, allergens: "Gluten, Huevo", ingredients: "Pollo, Lechuga, Crutones, Aderezo César" }
    ];
    let currentProductIndex = null;

    loadProductsButton.addEventListener('click', loadProducts);

    function loadProducts() {
        renderProducts();
    }

    function renderProducts() {
        productsTableBody.innerHTML = '';
        products.forEach((product, index) => {
            const row = productsTableBody.insertRow();
            row.innerHTML = `
                <td>${product.name}</td>
                <td>${product.description}</td>
                <td class="nowrap">${product.price.toFixed(2)} €</td>
                <td class="nowrap">
                    <button class="view" data-index="${index}">Ver/Editar</button>
                    <button class="delete" data-index="${index}">Eliminar</button>
                </td>
            `;
        });

        document.querySelectorAll('.view').forEach(button => {
            button.addEventListener('click', function () {
                openProductModal(this.getAttribute('data-index'));
            });
        });

        document.querySelectorAll('.delete').forEach(button => {
            button.addEventListener('click', function () {
                deleteProduct(this.getAttribute('data-index'));
            });
        });
    }

    function openProductModal(index) {
        const product = products[index];
        currentProductIndex = index;
        document.getElementById('productId').value = index;
        document.getElementById('productName').value = product.name;
        document.getElementById('productDescription').value = product.description;
        document.getElementById('productPrice').value = product.price;
        document.getElementById('productAllergens').value = product.allergens;
        document.getElementById('productIngredients').value = product.ingredients;

        toggleEditMode(false);

        const modal = document.getElementById('productModal');
        modal.style.display = 'block';

        document.getElementById('productForm').onsubmit = function(event) {
            event.preventDefault();
            product.name = document.getElementById('productName').value;
            product.description = document.getElementById('productDescription').value;
            product.price = parseFloat(document.getElementById('productPrice').value);
            product.allergens = document.getElementById('productAllergens').value;
            product.ingredients = document.getElementById('productIngredients').value;
            toggleEditMode(false);
            renderProducts();
        };

        document.getElementById('editButton').addEventListener('click', () => {
            toggleEditMode(true);
        });
    }

    function toggleEditMode(editable) {
        document.getElementById('productName').disabled = !editable;
        document.getElementById('productDescription').disabled = !editable;
        document.getElementById('productPrice').disabled = !editable;
        document.getElementById('productAllergens').disabled = !editable;
        document.getElementById('productIngredients').disabled = !editable;
        document.getElementById('editButton').style.display = editable ? 'none' : 'inline-block';
        document.getElementById('saveButton').style.display = editable ? 'inline-block' : 'none';
        document.getElementById('cancelButton').style.display = editable ? 'inline-block' : 'none';
        document.getElementById('modalTitle').textContent = editable ? 'Editar Producto' : 'Información del Producto';
    }

    window.closeModal = function() {
        document.getElementById('productModal').style.display = 'none';
        currentProductIndex = null;
    };

    function deleteProduct(index) {
        products.splice(index, 1);
        renderProducts();
        if (index === currentProductIndex) {
            closeModal();
        }
    }
});
