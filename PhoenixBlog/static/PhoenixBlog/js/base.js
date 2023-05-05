$(function () {
  initHunburger();
  initSwiper();
  setEvent();
});

function toggleMenu() {
  const menu = document.getElementById("menu");
  menu.classList.toggle("show");
}

function initHunburger() {
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
}

function initSwiper() {
  var swiper = new Swiper(".swiper-container", {
    slidesPerView: "auto",
    spaceBetween: 15,
    breakpoints: {
      768: {
        slidesPerView: 3,
        spaceBetween: 20,
      },
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
}

function setEvent() {
  $("span.genre-toggle")
    .unbind("click")
    .bind("click", function () {
      if ($(this).hasClass("active")) {
        $(this).removeClass("active");
      } else {
        $(this).addClass("active");
      }
    });
}
