window.addEventListener('keydown', () => {
    if (document.getElementById('playerScore')) {
      const playerScore = document.getElementById('playerScore');
      playerScore.addEventListener('onchange', () => { register(1); })
    }
})

function register(score) {
    const csrfInput =  document.querySelector("input[name='csrfmiddlewaretoken']");
    const csrfToken = csrfInput.value;
    const score = Number(document.getElementById('playerScore').innerHTML);
    const data = {
        'score': score,
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
        const score = data.score;
        document.getElementById('playerScore').innerHTML = score;
        });
}