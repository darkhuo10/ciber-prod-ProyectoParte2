document.addEventListener("DOMContentLoaded", function() {
    loadWaiters();
});

let currentWaiterId = null; // Track the current waiter for editing

function loadWaiters() {
    // Sample data for waiters
    const waiters = [
        { id: 1, nombre: "Juan", apellido: "Perez", telefono: "123456789", email: "juan.perez@example.com", password: "secret123" },
        { id: 2, nombre: "Ana", apellido: "Gomez", telefono: "987654321", email: "ana.gomez@example.com", password: "password456" },
        // Add more waiters as needed
    ];

    addWaitersToTable(waiters);
}

function addWaitersToTable(waiters) {
    const tableBody = document.getElementById("waitersTable").getElementsByTagName("tbody")[0];
    waiters.forEach(function(waiter) {
        const row = tableBody.insertRow();
        row.insertCell(0).textContent = waiter.id;
        row.insertCell(1).textContent = waiter.nombre;
        row.insertCell(2).textContent = waiter.apellido;
        row.insertCell(3).textContent = waiter.telefono;
        row.insertCell(4).textContent = waiter.email;
        const actionsCell = row.insertCell(5);
        const editButton = document.createElement("button");
        editButton.textContent = "Editar";
        editButton.onclick = function() {
            currentWaiterId = waiter.id;
            enableEditing(row, waiter);
        };
        actionsCell.appendChild(editButton);
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Eliminar";
        deleteButton.onclick = function() {
            tableBody.deleteRow(row.rowIndex - 1);
        };
        actionsCell.appendChild(deleteButton);
    });
}

function enableEditing(row, waiter) {
    row.cells[1].innerHTML = `<input type='text' value='${waiter.nombre}' />`;
    row.cells[2].innerHTML = `<input type='text' value='${waiter.apellido}' />`;
    row.cells[3].innerHTML = `<input type='text' value='${waiter.telefono}' />`;
    row.cells[4].innerHTML = `<input type='text' value='${waiter.email}' />`;

    const passwordCell = document.createElement("td");
    passwordCell.innerHTML = `Contraseña: <input type='password' value='${waiter.password}' />`;
    row.appendChild(passwordCell); // Add the password cell to the row

    const actionsCell = row.cells[5];
    actionsCell.innerHTML = "";

    const saveButton = document.createElement("button");
    saveButton.textContent = "Guardar";
    saveButton.onclick = function() {
        saveChanges(row, waiter, passwordCell);
    };
    actionsCell.appendChild(saveButton);

    const cancelButton = document.createElement("button");
    cancelButton.textContent = "Cancelar";
    cancelButton.onclick = function() {
        cancelEditing(row, waiter);
    };
    actionsCell.appendChild(cancelButton);
}

function saveChanges(row, waiter, passwordCell) {
    waiter.nombre = row.cells[1].getElementsByTagName('input')[0].value;
    waiter.apellido = row.cells[2].getElementsByTagName('input')[0].value;
    waiter.telefono = row.cells[3].getElementsByTagName('input')[0].value;
    waiter.email = row.cells[4].getElementsByTagName('input')[0].value;
    waiter.password = passwordCell.getElementsByTagName('input')[0].value;

    row.cells[1].textContent = waiter.nombre;
    row.cells[2].textContent = waiter.apellido;
    row.cells[3].textContent = waiter.telefono;
    row.cells[4].textContent = waiter.email;
    passwordCell.remove(); // Remove the password cell

    row.cells[5].innerHTML = `<button onclick='enableEditing(this.parentElement.parentElement, ${JSON.stringify(waiter)})'>Editar</button>
                              <button onclick='this.parentElement.parentElement.parentElement.deleteRow(this.parentElement.parentElement.rowIndex - 1)'>Eliminar</button>`;
    currentWaiterId = null;
}

function cancelEditing(row, waiter) {
    row.cells[1].textContent = waiter.nombre;
    row.cells[2].textContent = waiter.apellido;
    row.cells[3].textContent = waiter.telefono;
    row.cells[4].textContent = waiter.email;

    row.cells[5].innerHTML = `<button onclick='enableEditing(this.parentElement.parentElement, ${JSON.stringify(waiter)})'>Editar</button>
                              <button onclick='this.parentElement.parentElement.parentElement.deleteRow(this.parentElement.parentElement.rowIndex - 1)'>Eliminar</button>`;
    const passwordCell = row.lastChild; // Assuming the password cell is the last child
    if (passwordCell.innerHTML.includes("Contraseña:")) {
        passwordCell.remove(); // Remove the password cell if present
    }
    currentWaiterId = null;
}

function uploadWaiters(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const newWaiters = JSON.parse(e.target.result);
        addWaitersToTable(newWaiters);
    };
    reader.readAsText(file);
}
