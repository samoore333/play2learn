window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {

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

        const csrfInput =  document.querySelector("input[name='csrfmiddlewaretoken']");
        const csrfToken = csrfInput.value;
        const data = {'score': score}

        if (value == answer) {
            score.register(1);
            const score = Number(document.getElementById('score').innerHTML);
        } else {
            alert('You are incorrect, the answer was ' + answer);
        }     

        fetch(ajaxURL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data),
        })
    }  
})
