document.addEventListener('DOMContentLoaded', () => {
    // Elements for Product Management
    const loadProductsButton = document.getElementById('loadProducts');
    const productsTableBody = document.getElementById('productsTable') ? document.getElementById('productsTable').getElementsByTagName('tbody')[0] : null;

    let products = [];
    let currentEditingIndex = null;
    let currentViewingIndex = null;

    if (loadProductsButton) {
        loadProductsButton.addEventListener('click', loadProducts);
    }

    function loadProducts() {
        products = [
            { id: 1, name: "Pizza Margarita", description: "Queso, tomate, y albahaca", price: 8.50, supplier: "Proveedor A", expiryDate: "2023-12-31" },
            { id: 2, name: "Hamburguesa", description: "Carne de vacuno, queso, lechuga y tomate", price: 9.00, supplier: "Proveedor B", expiryDate: "2024-01-15" },
            { id: 3, name: "Ensalada César", description: "Pollo, lechuga, crutones y aderezo César", price: 7.00, supplier: "Proveedor C", expiryDate: "2023-11-20" }
        ];
        renderProducts();
    }

    function renderProducts() {
        if (!productsTableBody) return;
        productsTableBody.innerHTML = '';
        products.forEach((product, index) => {
            const row = productsTableBody.insertRow();
            row.innerHTML = `
                <td>${product.name}</td>
                <td>${product.description}</td>
                <td class="nowrap">${product.price.toFixed(2)} €</td>
                <td class="nowrap">
                    <button class="view" data-index="${index}">Ver</button>
                    <button class="edit" data-index="${index}">Editar</button>
                    <button class="delete" data-index="${index}">Eliminar</button>
                </td>
            `;
        });

        // Attach event listeners to newly created buttons
        document.querySelectorAll('.view').forEach(button => {
            button.addEventListener('click', function () {
                viewProduct(this.getAttribute('data-index'));
            });
        });

        document.querySelectorAll('.edit').forEach(button => {
            button.addEventListener('click', function () {
                editProduct(this.getAttribute('data-index'));
            });
        });

        document.querySelectorAll('.delete').forEach(button => {
            button.addEventListener('click', function () {
                deleteProduct(this.getAttribute('data-index'));
            });
        });
    }

    function viewProduct(index) {
        const product = products[index];
        currentViewingIndex = index;
        document.getElementById('viewProductName').textContent = product.name;
        document.getElementById('viewProductDescription').textContent = product.description;
        document.getElementById('viewProductPrice').textContent = product.price.toFixed(2) + ' €';
        document.getElementById('viewProductSupplier').textContent = product.supplier;
        document.getElementById('viewProductExpiryDate').textContent = product.expiryDate;
        document.getElementById('viewProductModal').style.display = 'block';
    }

    window.closeModal = function() {
        document.getElementById('viewProductModal').style.display = 'none';
        currentViewingIndex = null;
    };

    function editProduct(index) {
        const product = products[index];
        currentEditingIndex = index;
        document.getElementById('editProductId').value = index;
        document.getElementById('editProductName').value = product.name;
        document.getElementById('editProductDescription').value = product.description;
        document.getElementById('editProductPrice').value = product.price;
        document.getElementById('editProductModal').style.display = 'block';
    }

    document.getElementById('editProductForm').addEventListener('submit', saveProductChanges);

    function saveProductChanges(event) {
        event.preventDefault();
        const index = document.getElementById('editProductId').value;
        products[index].name = document.getElementById('editProductName').value;
        products[index].description = document.getElementById('editProductDescription').value;
        products[index].price = parseFloat(document.getElementById('editProductPrice').value);
        renderProducts();
        closeEditModal();
    }

    function deleteProduct(index) {
        products.splice(index, 1);
        renderProducts();
        if (index === currentEditingIndex) {
            closeEditModal();
        }
        if (index === currentViewingIndex) {
            closeModal();
        }
    }

    window.closeEditModal = function() {
        document.getElementById('editProductModal').style.display = 'none';
        currentEditingIndex = null;
    };

    window.closeAddModal = function() {
        document.getElementById('addProductModal').style.display = 'none';
    };
});
