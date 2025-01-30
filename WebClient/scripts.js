// Usuarios de prueba
const users = [
    {
        username: 'usuario1',
        password: 'password1'
    },
    {
        username: 'usuario2',
        password: 'password2'
    }
];

// Variable para activar/desactivar el modo de prueba
const testMode = true; // Cambiar a false cuando la API esté disponible

// Abrir el modal de cierre de sesión
function openLogoutModal() {
    document.getElementById('logoutModal').style.display = 'block';
}

// Cerrar el modal de cierre de sesión
function closeLogoutModal() {
    document.getElementById('logoutModal').style.display = 'none';
}

// Cerrar sesión y redirigir al login
async function logout() {
    if (testMode) {
        // Modo de prueba: simular el cierre de sesión sin API
        window.location.href = 'login.html'; // Redirigir al login
    } else {
        try {
            const response = await fetch('/api/logout', {
                method: 'GET', // Petición GET para cerrar sesión
            });

            const result = await response.json();

            if (result.status === 'OK') {
                window.location.href = 'login.html'; // Redirigir al login si el cierre de sesión fue exitoso
            } else {
                alert("Error al cerrar sesión.");
            }
        } catch (error) {
            console.error('Error al intentar cerrar sesión:', error);
            alert("Hubo un error al intentar cerrar sesión.");
        }
    }
}

// Cerrar el modal de cierre de sesión si se hace clic fuera de él
window.onclick = function(event) {
    if (event.target == document.getElementById('logoutModal')) {
        closeLogoutModal();
    }
};

// Iniciar sesión y redirigir solo si es exitoso
document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Obtener las credenciales del usuario
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    if (testMode) {
        // Comprobar las credenciales contra los usuarios de prueba en modo de prueba
        const user = users.find(user => user.username === username && user.password === password);

        if (user) {
            // Si la autenticación fue exitosa, redirigir al usuario
            window.location.href = "index.html"; // Redirigir a la página principal
        } else {
            // Si hubo un error de autenticación, mostrar el mensaje de error
            alert("Error al iniciar sesión. Por favor, comprueba tus credenciales.");
        }
    } else {
        try {
            // Enviar las credenciales al servidor para autenticación
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            const result = await response.json();

            if (response.ok) {
                // Si la autenticación fue exitosa, redirigir al usuario
                window.location.href = "index.html"; // Redirigir a la página principal
            } else {
                // Si hubo un error de autenticación, mostrar el mensaje del servidor
                alert(result.mensaje || "Error al iniciar sesión.");
            }
        } catch (error) {
            // Manejar cualquier error que ocurra durante la solicitud
            console.error('Error al intentar iniciar sesión:', error);
            alert("Hubo un error al intentar iniciar sesión.");
        }
    }
});

// Redirigir a la página principal
function goToMainPage() {
    window.location.href = "index.html";
}
