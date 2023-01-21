window.addEventListener("submit", function(e) {

        let number1 = document.getElementById('number1').innerHTML;
        let number2 = document.getElementById('number2').innerHTML;
        let num1 = Number(number1);
        let num2 = Number(number2);  
        let operator = document.getElementById('operator').innerHTML;
        const checkAnswer = document.getElementById('tbInput');
        const value = checkAnswer.value;

        if (operator == '+') {
            answer = num1 + num2;
        } else if (operator == '-') {
            answer = num1 - num2;
        } else if (operator == 'x') {
            answer = num1 * num2;
        } else {
            answer = num1 / num2;
        }

        let score = + document.getElementById('playerScore').innerHTML;

        if (value == answer) {
            score+=1;
            document.getElementById('playerScore').innerHTML = score;
            register(score)
        } else {
            alert('You are incorrect, the answer was ' + answer);
        }
})

function register(score) {
    const csrfInput =  document.querySelector("input[name='csrfmiddlewaretoken']");
    const csrfToken = csrfInput.value;
    const data = {'score': score}

    fetch(ajaxURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
}