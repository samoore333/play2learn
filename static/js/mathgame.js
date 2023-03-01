window.addEventListener('load', function () {
    let number1;
    let number2;

    operator = document.getElementById('operator').innerHTML;
    max = Number(document.getElementById('max').innerHTML);

    if (operator == '+') {
        number1 = Math.floor((Math.random() * max) + 1);
        number2 = Math.floor((Math.random() * max) + 1);
    } else if (operator == '-') {
        number1 = Math.floor((Math.random() * max) + 1);
        number2 = Math.floor((Math.random() * max) + 1);
        if (number2 > number1) {
                number2 = number1
                number1 = number2
        }
    } else if (operator == '*') {
        number1 = Math.floor((Math.random() * max) + 1);
        number2 = Math.floor((Math.random() * max) + 1);
    } else {
        number2 = Math.floor((Math.random() * max) + 1);
        numberx = Math.floor((Math.random() * max) + 1);
        number1 = number2 * numberx
    }

    document.getElementById('number1').innerHTML=number1;
    document.getElementById('number2').innerHTML=number2;
    document.getElementById('tbInput').focus();

window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {
    

    if (operator == '+') {
        answer = number1 + number2;
    } else if (operator == '-') {
        answer = number1 - number2;
    } else if (operator == '*') {
        answer = number1 * number2;
    } else {
        answer = number1 / number2;
    }

    const checkAnswer = document.getElementById('tbInput');
    const value = checkAnswer.value;
    let playerScore = + this.document.getElementById('playerScore').innerHTML;
    

    if (value == answer) {
          playerScore++;
          document.getElementById('playerScore').innerHTML=playerScore;
          const data = {'score': playerScore};

          fetch("", {
          method: "POST",
          headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken}, 
          body: JSON.stringify(data),
          })
          .then(response => response.json())
          } else {
                    alert('You are incorrect, the answer was ' + answer);
    }

    document.querySelector('input[type=text]').value = "";               
    document.getElementById('number1').innerHTML = "";
    document.getElementById('number2').innerHTML = ""; 
    if (operator == '+') {
        number1 = Math.floor((Math.random() * max) + 1);
        number2 = Math.floor((Math.random() * max) + 1);
    } else if (operator == '-') {
        number1 = Math.floor((Math.random() * max) + 1);
        number2 = Math.floor((Math.random() * max) + 1);
        if (number2 > number1) {
                number2 = number1
                number1 = number2
        }
    } else if (operator == '*') {
        number1 = Math.floor((Math.random() * max) + 1);
        number2 = Math.floor((Math.random() * max) + 1);
    } else {
        number2 = Math.floor((Math.random() * max) + 1);
        numberx = Math.floor((Math.random() * max) + 1);
        number1 = number2 * numberx
    }
    document.getElementById('number1').innerHTML = number1; 
    document.getElementById('number2').innerHTML = number2;
    document.getElementById('tbInput').focus();

    }
});
});