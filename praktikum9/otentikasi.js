function loginUser() {
    // Username dan password yang ditentukan
    const validUsername = "wann";
    const validPassword = "nf";

    // Ambil input dari form
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Pengecekan login
    if (username === validUsername && password === validPassword) {
        alert("Login berhasil!");
        // Arahkan ke halaman baru
        window.location.href = "sukses.html";
        return false; // mencegah reload form
    } else {
        alert("Login gagal! Username atau password salah.");
        return false; // tetap di halaman login
    }
}