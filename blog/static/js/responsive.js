const navbarBtn = document.getElementById('navbar-open');
const navbarResponsive = document.getElementById('responsive-navbar');

navbarBtn.addEventListener('click', function (event) {
    if (navbarResponsive.style.display == 'block') {
        navbarResponsive.style.display = 'none';
    } else {
        navbarResponsive.style.display = 'block';
    }
})
