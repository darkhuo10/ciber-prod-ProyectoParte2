document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('loadProducts').addEventListener('click', loadProducts);
    document.getElementById('productUploadButton').addEventListener('click', () => document.getElementById('productUpload').click());
    document.getElementById('productUpload').addEventListener('change', uploadProducts);
    document.getElementById('editProductForm').addEventListener('submit', saveProductChanges);
    document.getElementById('addProductForm').addEventListener('submit', addProduct);
});

async function loadProducts() {
    const tbody = document.querySelector('#productsTable tbody');
    tbody.innerHTML = '';

    try {
        const response = await fetch('/api/products');
        const productos = await response.json();

        productos.forEach(producto => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${producto.nombre}</td>
                <td>${producto.descripcion}</td>
                <td>${producto.precio}</td>
                <td>
                    <button onclick="editProduct(${producto.id})">Editar</button>
                    <button onclick="deleteProduct(${producto.id})">Eliminar</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error('Error al cargar los productos:', error);
    }
}

async function uploadProducts(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = async function(e) {
        const data = JSON.parse(e.target.result);

        try {
            const response = await fetch('/api/upload/products', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const result = await response.json();
            console.log('Productos subidos a la API:', result);
            loadProducts();
        } catch (error) {
            console.error('Error al subir los productos:', error);
        }
    };
    reader.readAsText(file);
}

async function editProduct(productId) {
    try {
        const response = await fetch(`/api/products/${productId}`);
        const producto = await response.json();

        if (producto) {
            document.getElementById('editProductId').value = producto.id;
            document.getElementById('editProductName').value = producto.nombre;
            document.getElementById('editProductDescription').value = producto.descripcion;
            document.getElementById('editProductPrice').value = producto.precio;
            document.getElementById('editProductModal').style.display = 'block';
        }
    } catch (error) {
        console.error('Error al obtener el producto:', error);
    }
}

async function saveProductChanges(event) {
    event.preventDefault();

    const productId = parseInt(document.getElementById('editProductId').value);
    const productName = document.getElementById('editProductName').value;
    const productDescription = document.getElementById('editProductDescription').value;
    const productPrice = parseFloat(document.getElementById('editProductPrice').value);

    try {
        const response = await fetch(`/api/products/${productId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nombre: productName,
                descripcion: productDescription,
                precio: productPrice
            })
        });
        const result = await response.json();
        console.log('Producto actualizado:', result);
        closeModal();
        loadProducts();
    } catch (error) {
        console.error('Error al guardar los cambios del producto:', error);
    }
}

function closeModal() {
    document.getElementById('editProductModal').style.display = 'none';
}

async function addProduct(event) {
    event.preventDefault();

    const productName = document.getElementById('addProductName').value;
    const productDescription = document.getElementById('addProductDescription').value;
    const productPrice = parseFloat(document.getElementById('addProductPrice').value);

    try {
        const response = await fetch('/api/products', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nombre: productName,
                descripcion: productDescription,
                precio: productPrice
            })
        });
        const result = await response.json();
        console.log('Producto añadido:', result);
        closeAddModal();
        loadProducts();
    } catch (error) {
        console.error('Error al añadir el producto:', error);
    }
}

function closeAddModal() {
    document.getElementById('addProductModal').style.display = 'none';
}

async function deleteProduct(productId) {
    try {
        const response = await fetch(`/api/products/${productId}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        console.log('Producto eliminado:', result);
        loadProducts();
    } catch (error) {
        console.error('Error al eliminar el producto:', error);
    }
}
