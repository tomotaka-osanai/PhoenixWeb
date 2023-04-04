function toggleMenu() {
  const menu = document.getElementById("menu");
  menu.classList.toggle("show");
}
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector("nav ul");
const links = document.querySelectorAll("nav ul li");

hamburger.addEventListener("click", () => {
  // ハンバーガーメニューを開閉する
  navLinks.classList.toggle("open");
  // メニュー項目をフェードイン・アウトする
  links.forEach((link) => {
    link.classList.toggle("fade");
  });
  // ハンバーガーアイコンをアニメーションする
  hamburger.classList.toggle("toggle");
});
