// Datos de ejemplo para Usuarios, Camareros y Productos
const exampleUsers = [
    { id: 1, idwaiter: 1, username: 'jdoe', password: '123456' },
    { id: 2, idwaiter: 2, username: 'mrodriguez', password: 'abcdef' }
];

const exampleWaiters = [
    { id: 1, identification: '123456789', firstname: 'Juan', lastname1: 'Pérez', lastname2: 'López', phone: '612345678', email: 'juan@example.com' },
    { id: 2, identification: '987654321', firstname: 'Maria', lastname1: 'Rodríguez', lastname2: 'González', phone: '623456789', email: 'maria@example.com' }
];

const exampleProducts = [
    { id: 1, name: 'Café', description: 'Café negro', number: 100, price: 1.5 },
    { id: 2, name: 'Té', description: 'Té verde', number: 50, price: 2.0 },
    { id: 3, name: 'Pastel', description: 'Pastel de manzana', number: 20, price: 3.0 }
];

// Función para cargar los datos de ejemplo
function loadData() {
    // Actualizar las tablas con los datos de ejemplo
    updateTable('usersTable', exampleUsers, ['id', 'idwaiter', 'username', 'password']);
    updateTable('waitersTable', exampleWaiters, ['id', 'identification', 'firstname', 'lastname1', 'lastname2', 'phone', 'email']);
    updateTable('productsTable', exampleProducts, ['id', 'name', 'description', 'number', 'price']);
}

// Función para actualizar una tabla con los datos
function updateTable(tableId, data, columns) {
    const table = document.getElementById(tableId).getElementsByTagName('tbody')[0];
    table.innerHTML = ''; // Limpiar la tabla antes de llenarla

    data.forEach(item => {
        const row = table.insertRow();
        columns.forEach(column => {
            const cell = row.insertCell();
            cell.textContent = item[column] || 'N/A'; // Si no existe el valor, mostramos 'N/A'
        });
    });
}
