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

        // Display the full JSON body of the response, pretty-printed
        const pretty = JSON.stringify(data, null, 2);
        document.getElementById("user-status").textContent = pretty;



    } catch (err) {
        console.error("Error loading user info", err);
    }
}
        
// Call this on each page to load layout parts
window.addEventListener("DOMContentLoaded", async () => {
  await includeHTML("#header", "/partials/header.html");
  await includeHTML("#footer", "/partials/footer.html");
  loadUserInfo();
});
