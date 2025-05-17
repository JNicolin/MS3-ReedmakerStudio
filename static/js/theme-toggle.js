document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("themeToggle");
    const body = document.body;
  
    function setTheme(dark) {
      if (dark) {
        body.classList.add("dark-mode");
        localStorage.setItem("theme", "dark");
        if (themeToggle) themeToggle.textContent = "☀️";
      } else {
        body.classList.remove("dark-mode");
        localStorage.setItem("theme", "light");
        if (themeToggle) themeToggle.textContent = "🌙";
      }
    }
  
    const savedTheme = localStorage.getItem("theme");
    setTheme(savedTheme === "dark");
  
    if (themeToggle) {
      themeToggle.addEventListener("click", () => {
        setTheme(!body.classList.contains("dark-mode"));
      });
    }
  });