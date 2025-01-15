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

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    window.location.href = "index.html";
});
