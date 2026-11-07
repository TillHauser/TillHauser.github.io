
/* =========================================
   1. Mobile navigation
========================================= */

const menuToggle = document.querySelector("#menu-toggle");
const mainNavigation = document.querySelector("#main-navigation");

menuToggle.addEventListener("click", () => {

    const isOpen = mainNavigation.classList.toggle("open");

    menuToggle.setAttribute("aria-expanded", isOpen);

    menuToggle.setAttribute(
        "aria-label",
        isOpen ? "Close navigation menu" : "Open navigation menu"
    );

});


/* Close menu when a navigation link is clicked */

const navigationLinks = document.querySelectorAll(".nav-link");

navigationLinks.forEach((link) => {

    link.addEventListener("click", () => {

        mainNavigation.classList.remove("open");

        menuToggle.setAttribute("aria-expanded", "false");

        menuToggle.setAttribute(
            "aria-label",
            "Open navigation menu"
        );

    });

});


/* =========================================
   2. Automatic copyright year
========================================= */

const currentYear = document.querySelector("#current-year");

currentYear.textContent = new Date().getFullYear();

