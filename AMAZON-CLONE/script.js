//Select slider and hide other images

const imgs = document.querySelectorAll('.header-slider ul img');
const prev_btn = document.querySelector('.control_prev');
const next_btn = document.querySelector('.control_next');

let n = 0;

function changesSlide(){ //Selects all images and hides them. When n=0 it will select 1st image and so on
    for (let i = 0; i < imgs.length; i++){
        imgs[i].style.display = 'none';
    }
    imgs[n].style.display = 'block'; //n = 0 then adds 1st image
}


changesSlide();


prev_btn.addEventListener('click', (e) => {
    if(n>0){
        n--;
    }else{
        n = imgs.length - 1;
    }
    changesSlide();
})

next_btn.addEventListener('click', (e) => {  //If image less than 1 then increase the value by 1
    if(n < imgs.length - 1){
        n++;
    }else{
        n = 0;
    }
    changesSlide();
})



















