window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {
        
        let number1 = document.getElementById('number1').innerHTML;
        let number2 = document.getElementById('number2').innerHTML;      
        let operator = document.getElementById('operator').innerHTML;
        const checkAnswer = document.getElementById('tbInput');
        const value = checkAnswer.value;

        if (operator == '+') {
            answer = number1 + number2;
        } else if (operator == '-') {
            answer = number1 - number2;
        } else if (operator == 'x') {
            answer = number1 * number2;
        } else {
            answer = number1 / number2;
        }
        
        if (value == answer) {
            playerScore+=1;
            document.getElementById("playerScore").innerHTML=playerScore;
         
        } else {
                alert('You are incorrect, the answer was ' + answer);
        }

    }})