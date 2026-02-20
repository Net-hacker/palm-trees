let mode = false;

window.addEventListener('load', () => {
  const m = sessionStorage.getItem('mode');
  if (m === 'light') {
    document.body.classList.toggle("light-mode");
    mode = true;
  }
});

function changeMode() {
  if (mode === false) {
    document.body.classList.toggle("light-mode");
    sessionStorage.setItem('mode', 'light');
    mode = true;
  } else {
    document.body.classList.toggle("light-mode");
    sessionStorage.setItem('mode', 'dark');
    mode = false;
  }
}

function showMenu() {
  const menu = document.getElementById("menu");
  if (menu.hasAttribute('hidden')) {
    menu.hidden = false;
    menu.style.display = "flex";
  } else {
    menu.style.display = "none";
    menu.hidden = true;
  }
}

function logout() {
  window.location.href = "/logout";
}
