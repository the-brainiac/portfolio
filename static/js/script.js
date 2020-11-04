

let theme = localStorage.getItem("theme");

if (theme == null) {
  setTheme("light");
} else {
  setTheme(theme);
}

// function to toggle between light and dark theme
function toggleTheme() {
  if (localStorage.getItem("theme") === "blue") {
    setTheme("light");
  } else {
    setTheme("blue");
  }
}
function setTheme(mode) {
  if (mode == "light") {
    document.getElementById("theme-style").href = static + "/default.css";
  }

  if (mode == "blue") {
    document.getElementById("theme-style").href = static + "/blue.css";
  }

  localStorage.setItem("theme", mode);
}

// Immediately invoked function to set the theme on initial load
(function () {
  if (localStorage.getItem("theme") === "blue") {
    setTheme("blue");
    document.getElementById("slider").checked = true;
  } else {
    setTheme("light");
    document.getElementById("slider").checked = false;
  }
})();
