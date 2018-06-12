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