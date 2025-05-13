document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.getElementById('navbarNav');
    navbar.addEventListener('show.bs.collapse', function () {
        navbar.classList.add('collapsed');
    });
    navbar.addEventListener('hide.bs.collapse', function () {
        navbar.classList.remove('collapsed');
    });
});