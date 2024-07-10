document.getElementById('menu-icon').addEventListener('click', function() {
    document.getElementById('side-menu').style.width = '250px';
});

document.querySelector('.close-btn').addEventListener('click', function() {
    document.getElementById('side-menu').style.width = '0';
});

document.getElementById('side-menu').addEventListener('mouseleave', function() {
    document.getElementById('side-menu').style.width = '0';
});
