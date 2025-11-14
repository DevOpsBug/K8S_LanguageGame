async function includeHTML(selector, file) {
  const element = document.querySelector(selector);
  if (element) {
    const res = await fetch(file);
    const html = await res.text();
    element.innerHTML = html;
  }
}

async function loadUserInfo() {
    try {
        const response = await fetch('/api/public/userinfo', { credentials: 'include' });
        const data = await response.json();

        if (data.authenticated) {
            document.getElementById("user-status").textContent = "User: " + data.email;
            document.getElementById("login-btn").style.display = "none";
            document.getElementById("logout-btn").style.display = "inline-block";
            document.getElementById("private-area").style.display = "inline-block";
        } else {
            document.getElementById("user-status").textContent = "User: Guest";
            document.getElementById("login-btn").style.display = "inline-block";
            document.getElementById("logout-btn").style.display = "none";
            document.getElementById("private-area").style.display = "none";
        }

    } catch (err) {
        document.getElementById("user-status").textContent = "User: Guest";
        console.error("Error loading user info", err);
    }
}
        
// Call this on each page to load layout parts
window.addEventListener("DOMContentLoaded", async () => {
  await includeHTML("#header", "/partials/header.html");
  await includeHTML("#footer", "/partials/footer.html");
  loadUserInfo();
});
