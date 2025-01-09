// Datos ficticios de productos
const mockProducts = [
    {
        name: 'Pizza Margarita',
        description: 'Pizza clásica con tomate, queso mozzarella y albahaca.',
        price: '8.99€'
    },
    {
        name: 'Hamburguesa Gourmet',
        description: 'Hamburguesa con carne de res, queso cheddar, bacon y salsa especial.',
        price: '12.50€'
    },
    {
        name: 'Ensalada César',
        description: 'Ensalada fresca con lechuga romana, pollo a la parrilla, croutons y aderezo César.',
        price: '7.99€'
    },
    {
        name: 'Pasta Carbonara',
        description: 'Pasta con salsa cremosa de huevo, queso parmesano, panceta y pimienta negra.',
        price: '10.50€'
    }
];

// Datos ficticios de camareros
const mockWaiters = [
    { id: 1, firstName: 'Carlos', lastName: 'Pérez', phone: '123-456-789', email: 'carlos@restaurante.com' },
    { id: 2, firstName: 'Ana', lastName: 'Gómez', phone: '987-654-321', email: 'ana@restaurante.com' },
    { id: 3, firstName: 'Luis', lastName: 'Martínez', phone: '456-789-123', email: 'luis@restaurante.com' },
    { id: 4, firstName: 'María', lastName: 'Sánchez', phone: '321-654-987', email: 'maria@restaurante.com' }
];

// Función para cargar los productos
function loadProducts() {
    // Obtener la tabla de productos
    const tbody = document.querySelector('#productsTable tbody');
    tbody.innerHTML = ''; // Limpiar antes de cargar nuevos datos

    // Recorrer los productos y agregar filas a la tabla
    mockProducts.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.name}</td>
            <td>${product.description}</td>
            <td>${product.price}</td>
        `;
        tbody.appendChild(row);
    });
}

// Función para cargar los camareros
function loadWaiters() {
    // Obtener la tabla de camareros
    const tbody = document.querySelector('#waitersTable tbody');
    tbody.innerHTML = ''; // Limpiar antes de cargar nuevos datos

    // Recorrer los camareros y agregar filas a la tabla
    mockWaiters.forEach(waiter => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${waiter.id}</td>
            <td>${waiter.firstName}</td>
            <td>${waiter.lastName}</td>
            <td>${waiter.phone}</td>
            <td>${waiter.email}</td>
        `;
        tbody.appendChild(row);
    });
}

// Función de logout
function logout() {
    // Simulando la respuesta de un logout
    const data = { success: true };

    if (data.success) {
        window.location.href = 'login.html';  // Redirigir al login
    }
}
