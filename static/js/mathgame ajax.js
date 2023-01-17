window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {

        let number1 = document.getElementById('number1').innerHTML;
        let number2 = document.getElementById('number2').innerHTML;      
        let operator = document.getElementById("operator");
        const checkAnswer = document.getElementById('tbInput');
        const value = checkAnswer.value;
        const csrfInput =  document.querySelector("input[name='csrfmiddlewaretoken']");
        const csrfToken = csrfInput.value;

        if (operator == '+') {
            answer = number1 + number2;
        } else if (operator == '-') {
            answer = number1 - number2;
        } else if (operator == 'x') {
            answer = number1 * number2;
        } else {
            answer = number1 / number2;
        }
        
        const data = {
            'correct': correct,
            'incorrect': incorrect
        }
        
        if (value == answer) {
            correct+=1;
        } else {
            incorrect+=1;
        }

        fetch(ajaxURL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                const numCorrect = count(correct)
                let score = `${numCorrect}`;
                document.getElementById('playerScore').innerHTML = data.correct;
            });
    }  
})
