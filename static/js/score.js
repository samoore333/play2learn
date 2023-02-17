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
}