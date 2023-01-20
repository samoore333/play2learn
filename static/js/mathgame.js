window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {
        
        let number1 = document.getElementById('number1').innerHTML;
        let number2 = document.getElementById('number2').innerHTML;
        let num1 = Number(number1);
        let num2 = Number(number2);  
        let operator = document.getElementById('operator').innerHTML;
        const checkAnswer = document.getElementById('tbInput');
        const value = checkAnswer.value;
        let score = + this.document.getElementById('playerScore').innerHTML;

        if (operator == '+') {
            answer = num1 + num2;
        } else if (operator == '-') {
            answer = num1 - num2;
        } else if (operator == 'x') {
            answer = num1 * num2;
        } else {
            answer = num1 / num2;
        }

        if (value == answer) {
            document.getElementById('playerScore').innerHTML =+1;
            score.save()
        } else {
            alert('You are incorrect, the answer was ' + answer);
        }
    }
})
