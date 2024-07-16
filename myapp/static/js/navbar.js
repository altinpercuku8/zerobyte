const openMn = document.getElementById('openMenu');
const clsMn = document.getElementById('closeMenu');
const menu = document.querySelector('.links');

document.body.style.overflow = "initial";




openMn.addEventListener('click', function(){
    menu.style.width = "100%";
    document.body.style.overflow = "hidden"
});

clsMn.addEventListener('click', function(){
    menu.style.width = 0;
    document.body.style.overflow = "visible"
});
