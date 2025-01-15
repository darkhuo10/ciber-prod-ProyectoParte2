document.addEventListener("DOMContentLoaded", function() {
    // Cargar los usuarios
    if (window.location.pathname === "/index.html") {
        fetchUsers();
    }

    // Manejo del formulario de registro
    if (document.getElementById("registerForm")) {
        document.getElementById("registerForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            fetch("/api/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = "index.html";
                } else {
                    alert("Error al registrar el usuario.");
                }
            });
        });
    }

    // Manejo del formulario de actualización
    if (document.getElementById("updateForm")) {
        const userId = new URLSearchParams(window.location.search).get("id");
        fetch(`/api/users/${userId}`)
            .then(response => response.json())
            .then(user => {
                document.getElementById("userId").value = user.id;
                document.getElementById("username").value = user.username;
                document.getElementById("password").value = user.password;
            });

        document.getElementById("updateForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const userId = document.getElementById("userId").value;
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            fetch(`/api/users/${userId}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = "index.html";
                } else {
                    alert("Error al actualizar el usuario.");
                }
            });
        });
    }
});

function fetchUsers() {
    fetch("/api/users")
        .then(response => response.json())
        .then(users => {
            const tbody = document.querySelector("#userTable tbody");
            tbody.innerHTML = "";

            users.forEach(user => {
                const tr = document.createElement("tr");

                tr.innerHTML = `
                    <td>${user.id}</td>
                    <td>${user.username}</td>
                    <td>
                        <a href="update.html?id=${user.id}"><button>Editar</button></a>
                        <button onclick="deleteUser(${user.id})">Eliminar</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        });
}

function deleteUser(id) {
    fetch(`/api/users/${id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            fetchUsers(); // Recargar la lista de usuarios
        } else {
            alert("Error al eliminar el usuario.");
        }
    });
}
