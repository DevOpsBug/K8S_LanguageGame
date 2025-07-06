async function includeHTML(selector, file) {
  const element = document.querySelector(selector);
  if (element) {
    const res = await fetch(file);
    const html = await res.text();
    element.innerHTML = html;
  }
}

// Call this on each page to load layout parts
window.addEventListener("DOMContentLoaded", () => {
  includeHTML("#header", "/partials/header.html");
  includeHTML("#footer", "/partials/footer.html");

  /*
  const path = window.location.pathname;

  // load dynamic page content
  if (path === "/" || path === "/index.html") {
    includeHTML("#content", "/pages/home.html");
  } else if (path === "/about.html") {
    includeHTML("#content", "/pages/about.html");
  } else {
    includeHTML("#content", "/pages/404.html");
  }
    */
});
