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
            score+=1;
            document.getElementById('playerScore').innerHTML=score;
            let xhr = new XMLHttpRequest();
            xhr.open("POST", "https://reqbin.com/echo/post/json");
            xhr.setRequestHeader("Accept", "application/json");
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                console.log(xhr.status);
                console.log(xhr.responseText);
            }};

            let data = `{
            "score": score,
            }`;

            xhr.send(data);
            
        } else {
            alert('You are incorrect, the answer was ' + answer);
        }
    }
})
