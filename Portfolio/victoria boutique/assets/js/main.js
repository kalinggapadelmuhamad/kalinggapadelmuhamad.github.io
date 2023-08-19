$(document).ready(function () {
  $(".icon-menu").click(function () {
    $(".icon-menu").toggleClass("bxs-grid-alt");
    $(".menu").toggleClass("actives");
  });
});

var swiper = new Swiper(".home-slider", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 0,
    stretch: 0,
    depth: 100,
    modifier: 2,
    slideShadows: true,
  },
  loop: true,
  autoplay: {
    delay: 1500,
    disableOnIntereaction: false,
  },
});
