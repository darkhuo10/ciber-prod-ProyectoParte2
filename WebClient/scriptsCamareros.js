let waiters = [
    { id: 1, name: 'Juan', lastName: 'Pérez', phone: '123456789', email: 'juan@example.com', password: '1234' },
    { id: 2, name: 'Ana', lastName: 'Gómez', phone: '987654321', email: 'ana@example.com', password: 'abcd' }
];

function loadWaiters() {
    const tableBody = document.querySelector("#waitersTable tbody");
    tableBody.innerHTML = '';

    waiters.forEach(waiter => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${waiter.name}</td>
            <td>${waiter.lastName}</td>
            <td>
                <button class="edit-btn" onclick="openEditModal(${waiter.id})">Editar</button>
                <button class="delete-btn" onclick="deleteWaiter(${waiter.id})">Eliminar</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function openEditModal(id) {
    const waiter = waiters.find(waiter => waiter.id === id) || { id: null, name: '', lastName: '', phone: '', email: '', password: '' };

    document.getElementById('editName').value = waiter.name;
    document.getElementById('editLastName').value = waiter.lastName;
    document.getElementById('editPhone').value = waiter.phone;
    document.getElementById('editEmail').value = waiter.email;
    document.getElementById('editPassword').value = waiter.password;

    // Asegúrate de ocultar la contraseña y restablecer el texto del botón
    const passwordField = document.getElementById('editPassword');
    const button = document.getElementById('showPasswordButton');
    passwordField.type = 'password';
    button.textContent = 'Ver Contraseña';

    const modal = document.getElementById('editModal');
    modal.style.display = 'block';

    document.getElementById('editForm').onsubmit = function(event) {
        event.preventDefault();
        waiter.name = document.getElementById('editName').value;
        waiter.lastName = document.getElementById('editLastName').value;
        waiter.phone = document.getElementById('editPhone').value;
        waiter.email = document.getElementById('editEmail').value;
        waiter.password = document.getElementById('editPassword').value;

        if (waiter.id === null) {
            waiter.id = waiters.length ? waiters[waiters.length - 1].id + 1 : 1;
            waiters.push(waiter);
        }

        modal.style.display = 'none';
        loadWaiters();
    };
}

function closeModal() {
    const passwordField = document.getElementById('editPassword');
    passwordField.type = 'password';  // Ocultar la contraseña si se cierra el modal
    document.getElementById('editModal').style.display = 'none';
    document.getElementById('editForm').reset(); // Reiniciar el formulario para agregar nuevos camareros
}

function deleteWaiter(id) {
    waiters = waiters.filter(waiter => waiter.id !== id);
    loadWaiters();
}

function togglePasswordVisibility() {
    const passwordField = document.getElementById('editPassword');
    const button = document.getElementById('showPasswordButton');

    if (passwordField.type === "password") {
        passwordField.type = "text"; // Muestra la contraseña
        button.textContent = "Ocultar Contraseña"; // Cambia el texto del botón
    } else {
        passwordField.type = "password"; // Oculta la contraseña
        button.textContent = "Ver Contraseña"; // Restaura el texto original del botón
    }
}

function uploadWaiters(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        try {
            const waitersData = JSON.parse(e.target.result);

            if (Array.isArray(waitersData)) {
                waiters = waitersData;
                loadWaiters();
            } else {
                alert("El archivo debe contener un array de camareros.");
            }
        } catch (error) {
            alert("Hubo un error al procesar el archivo JSON.");
        }
    };

    reader.readAsText(file);
}

function openLogoutModal() {
    document.getElementById('logoutModal').style.display = 'block';
}

function closeLogoutModal() {
    document.getElementById('logoutModal').style.display = 'none';
}

function logout() {
    window.location.href = 'login.html'; 
}

window.onclick = function(event) {
    if (event.target == document.getElementById('logoutModal')) {
        closeLogoutModal();
    }
}

function goToMainPage() {
    window.location.href = "index.html"; // Redirige a la página principal
}
