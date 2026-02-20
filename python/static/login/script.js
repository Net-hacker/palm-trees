let mode = false;

class Sha256Hash {
    static async encode(input) {
        const encoder = new TextEncoder();
        const data = encoder.encode(input);
        const hashBuffer = await crypto.subtle.digest('SHA-256', data);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }
}

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

function signUpInstead() {
  const sign = document.getElementById("signUp");
  const login = document.getElementById("login");

  sign.hidden = false;
  sign.style.display = "flex"
  login.style.display = "none";
  login.hidden = true;
}

function loginInstead() {
  const sign = document.getElementById("signUp");
  const login = document.getElementById("login");

  sign.hidden = true;
  sign.style.display = "none"
  login.style.display = "flex";
  login.hidden = hidden;
}

function login() {
  const username = document.getElementById("user");
  const password = document.getElementById("pass");

  if (username.value == "" || password.value == "") {
    document.getElementById("messageL").innerText = "you need to enter something!";
  } else if (username.value == "palm") {
    document.getElementById("messageL").innerText = "use something else!";
  } else {
    fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user_name: username.value,
        user_password: password.value
      })
    })
    .then(response => {
      if (response.ok) {
        window.location.href = "/";
      } else if (response.status === 300) {
        document.getElementById("messageL").innerText = "wrong password";
      } else {
        document.getElementById("messageL").innerText = "user not found! maybe sign up";
      }
    })
    .catch((e) => console.error(e));
  }
}

function signUp() {
  const username = document.getElementById("username")
  const password = document.getElementById("password")
  const passwordV = document.getElementById("passwordV")

  if (username.value == "" || password.value == "") {
    document.getElementById("messageS").innerText = "you need to enter something!";
  } else if (username.value == "palm") {
    document.getElementById("messageS").innerText = "use something else!";
  } else if (password.value != passwordV.value) {
    document.getElementById("messageS").innerText = "not the same password!";
  } else {
    fetch("/api/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user_name: username.value,
        user_password: password.value
      })
    })
    .then(response => {
      if (response.ok) {
        window.location.href = "/";
      } else {
        document.getElementById("messageS").innerText = "couldn't sign up";
      }
    })
    .catch((e) => console.error(e));
  }
}
