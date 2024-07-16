const openMn = document.getElementById('openMenu');
const clsMn = document.getElementById('closeMenu');
const menu = document.querySelector('.links');

openMn.addEventListener('click', function(){
    document.body.style.overflow = "hidden";
    menu.style.width = "100%";
});

clsMn.addEventListener('click', function(){
    menu.style.width = 0;
    if (menu.style.width == 0){
        document.body.style.overflow = "initial";
    }
});
