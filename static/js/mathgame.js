window.addEventListener('load', function math() {
    let num1;
    let num2;

    if (document.getElementById(mathgame.operation = 'addition')) {
        num1 = Math.floor((Math.random() * 10) + 1);
        num2 = Math.floor((Math.random() * 10) + 1);
        document.getElementById("num1").innerHTML=num1;
        document.getElementById("num2").innerHTML=num2;
        document.getElementById('tbInput').focus();
    } else if (document.getElementById(mathgame.operation = 'subtraction')) {
        num1 = Math.floor((Math.random() * 10) + 5);
        num2 = Math.floor((Math.random() * 5) + 1);
        document.getElementById("num1").innerHTML=num1;
        document.getElementById("num2").innerHTML=num2;
        document.getElementById('tbInput').focus();
    } else if (document.getElementById(mathgame.operation = 'multiplication')) {
        num1 = Math.floor((Math.random() * 10) + 1);
        num2 = Math.floor((Math.random() * 5) + 1);
        document.getElementById("num1").innerHTML=num1;
        document.getElementById("num2").innerHTML=num2;
        document.getElementById('tbInput').focus();
    } else {
        num1 = Math.floor((Math.random() * 10) + 5) * 2;
        num2 = Math.floor((Math.random() * 5) + 1) * 2;
        document.getElementById("num1").innerHTML=num1;
        document.getElementById("num2").innerHTML=num2;
        document.getElementById('tbInput').focus();
    }
})

window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {

        if (document.getElementById(mathgame.operation = 'addition')){
            let answer = num1 + num2;
        } else if (document.getElementById(mathgame.operation = 'subtraction')){
            let answer = num1 - num2;
        } else if (document.getElementById(mathgame.operation = 'multiplication')){
            let answer = num1 * num2;
        } else {
            let answer = num1 / num2;
        }
        const checkAnswer = document.getElementById('tbInput');
        const value = checkAnswer.value;
        let playerScore = + this.document.getElementById(mathgame.score).innerHTML;

        if (value == answer) {
            playerScore+=1;
            document.getElementById("playerScore").innerHTML=playerScore;
        
        } else {
            alert('You are incorrect, the answer was ' + answer);
        }
    }
})
