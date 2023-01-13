function check() {  
    const operator = document.getElementById("operator");

    if (operator == '+') {
        answer = number1 + number2;
    } else if (operator == '-') {
        answer = number1 - number2;
    } else if (operator == 'x') {
        answer = number1 * number2;
    } else {
        answer = number1 / number2;
    }

    const checkAnswer = document.getElementById("tbInput");
    const value = checkAnswer.value;

    if (value == answer) {
          playerScore+=1;
          document.getElementById("playerScore").innerHTML=playerScore;
       
    } else {
          alert('You are incorrect, the answer was ' + answer);
    }
};

