var pink = document.getElementById('pink');
var blue = document.getElementById('blue');

var counter = 0;

function jump(){
    pink.classList.add('animate');

    setTimeout(function(){
        pink.classList.remove('animate')
    }, 300);
}

var check = setInterval(function(){
    let pinkTop = parseInt(window.getComputedStyle(pink).getPropertyValue('top'));
    let blueLeft = parseInt(window.getComputedStyle(blue).getPropertyValue('left'));

    if(blueLeft < 20 && blueLeft > -20 && pinkTop >= 150){
        blue.style.animation = 'none';

        alert('Game Over. Score: ' + counter / 100);
        counter = 0;

        blue.style.animation = 'blue 2s infinite linear';
    }else{
        counter++;

        document.getElementById('scoreSpan').innerHTML = counter / 100;
    }
}, 10);