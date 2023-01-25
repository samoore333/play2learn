window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {

        let number1 = document.getElementById('number1').innerHTML;
        let number2 = document.getElementById('number2').innerHTML;
        let num1 = Number(number1);
        let num2 = Number(number2);
        let operator = document.getElementById('operator').innerHTML;
        let userAnswer = document.getElementById('tbInput');
        let value = userAnswer.value;
        const scores = document.getElementById('playerScore');
        
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
            scores = Number(document.getElementById('playerScore').innerHTML+=1);
            const csrfInput =  document.querySelector("input[name='csrfmiddlewaretoken']");
            const csrfToken = csrfInput.value;
            const data = {
                'scores': scores,
            }
            $(ajaxURL, {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(data),
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('playerScore').innerHTML = data.scores;
                });
            } else {
                alert('You are incorrect, the answer was ' + answer);
        }
    }
})

function register(scores) {
    const csrfInput =  document.querySelector("input[name='csrfmiddlewaretoken']");
    const csrfToken = csrfInput.value;
    const num_scores = Number(document.getElementById('playerScore').innerHTML);
    const data = {
        'scores': scores,
        'num_scores': num_scores
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
            document.getElementById('playerScore').innerHTML = data.num_scores;
        });
}
