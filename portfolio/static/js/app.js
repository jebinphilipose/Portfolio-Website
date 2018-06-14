/* Preloader Script begin */
var preloader = document.getElementById('preloader');

window.addEventListener('load', function () {
    setTimeout(function () {
        document.getElementById("preloader").style.opacity = 0;
        document.getElementById("wrapper").style.opacity = 1;
    }, 2000);
    setTimeout(function () {
        document.getElementById("preloader").remove();
    }, 3000);
});
/* Preloader Script end */

/* Script for typing effect begin */
$(window).on('load', function () {
    setTimeout(function () {
        var typed = new Typed('#type', {
            strings: [
                "Hi, I'm Jebin Philipose <span>&semi;)</span>",
                "I am a computer science engineering student",
                "I am a self-made Full Stack Web Developer",
                "I love <i class='fas fa-code'></i>",
                "Start scrolling to learn more about me",
            ],
            typeSpeed: 50,
            backSpeed: 30,
            loop: true,
            loopCount: Infinity
        });
    }, 2000);
});
/* Script for typing effect begin */

/* Smooth scroll to a section begin */
$(document).ready(function () {
    $("header a").click(function (event) {
        event.preventDefault();
        var target = $(this.getAttribute('href'));
        if (target.length) {
            $('html, body').stop().animate({
                scrollTop: target.offset().top
            }, 1000);
        }

    });
});
/* Smooth scroll to a section end */