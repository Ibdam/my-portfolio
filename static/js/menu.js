document.addEventListener("DOMContentLoaded", function () {
    var navLinks = document.querySelectorAll(".navbar-nav .nav-link");
    var navCollapse = document.querySelector(".navbar-collapse");

    navLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            if (navCollapse.classList.contains("show")) {
                navCollapse.classList.remove("show"); // Hide the menu
            }
        });
    });
});
