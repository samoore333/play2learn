window.addEventListener('load', function math() {
    let number1;
    let number2;

    number1 = Math.floor((Math.random() * 10) + 1);
    number2 = Math.floor((Math.random() * 5) + 1);
    document.getElementById('number1').innerHTML=number1;
    document.getElementById('number2').innerHTML=number2;
    document.getElementById('tbInput').focus();
    const multiplicationEnd = document.getElementById('multiplicationEnd');
    const multiplicationGame = document.getElementById('multiplicationGame');


window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {

    
    let answer = number1 * number2;
    const checkAnswer = document.getElementById('tbInput');
    const value = checkAnswer.value;
    let playerScore = + this.document.getElementById('playerScore').innerHTML;
    let finalScore = + this.document.getElementById('playerScore').innerHTML;
    

    if (value == answer) {
          playerScore+=1;
          finalScore+=1;
          document.getElementById("playerScore").innerHTML=playerScore;
          document.getElementById("finalScore").innerHTML=finalScore;
       
    } else {
          alert('You are incorrect, the answer was ' + answer);
    }

    document.querySelector('input[type=text]').value = "";               
    document.getElementById('number1').innerHTML = "";
    document.getElementById('number2').innerHTML = ""; 
    number1 = Math.floor((Math.random() * 10) + 1);
    number2 = Math.floor((Math.random() * 5) + 1);
    document.getElementById('number1').innerHTML = number1; 
    document.getElementById('number2').innerHTML = number2;
    document.getElementById('tbInput').focus();

    answer = number1 * number2
    }
});
});
