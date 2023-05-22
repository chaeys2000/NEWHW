const btn = document.querySelector(".menu-button");
const navbar = document.querySelector(".navbar");

function toggleMenu() {
  btn.classList.toggle("active");
  navbar.classList.toggle("active");
}

btn.addEventListener("click", toggleMenu);
