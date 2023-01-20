const COUNTER_KEY = 'my-counter';

function countDown(i, callback) {
//callback = callback || function(){};
timer = setInterval(function() {
    seconds = parseInt(i % 60, 10);
    seconds = seconds < 10 ? "0" + seconds : seconds;

    if ((i--) > 0) {
    document.getElementById("playerTime").innerHTML = seconds;
    window.sessionStorage.setItem(COUNTER_KEY, i);
    } else {
    window.sessionStorage.removeItem(COUNTER_KEY);
    clearInterval(timer);
    callback();
    window.location.href ="/mathgame/mathgame/<slug>/[name='detail']"
    }
}, 1000);
}

window.onload = function() {
let countDownTime = window.sessionStorage.getItem(COUNTER_KEY) || 30;
countDown(countDownTime, function() {
    $('#myModal').modal('show');
});
};

let score = + document.getElementById('score').innerHTML;

        if (value == answer) {
            score+=1;
            document.getElementById('score').innerHTML = score;
        } else {
            alert('You are incorrect, the answer was ' + answer);
        }

        $.post('/mathgame/mathgame/<slug>/play',   // url
        { score: 'score'}, // data to be submit
        function(data, status, jqXHR) {// success callback
                    $('p').append('status: ' + status + ', data: ' + data);
            })