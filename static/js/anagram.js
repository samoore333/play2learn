window.addEventListener('load', function anagram() {
    let anagram;
    wordLength = document.getElementById('wordLength');

    fetch('/static/json/anagrams.json')
        .then((response) => response.json())
        .then((data) => console.log(data))
    ;

    const anagram5 = {anagram5: "anagram5"};
    const anagram6 = {anagram6: "anagram6"};
    const anagram7 = {anagram7: "anagram7"};
    const anagram8 = {anagram8: "anagram8"};

    let rand5 = anagram5[(Math.floor(Math.random()*(anagram5.length)))];
    let rand6 = anagram6[(Math.floor(Math.random()*(anagram6.length)))];
    let rand7 = anagram7[(Math.floor(Math.random()*(anagram7.length)))];
    let rand8 = anagram8[(Math.floor(Math.random()*(anagram8.length)))];

    if (wordLength == '5') {
        anagram = rand5
    } else if (wordLength == '6') {
        anagram = rand6
    } else if (wordLength == '7') {
        anagram = rand7
    } else {
        anagram = rand8
    }

    let word = anagram[(Math.floor(Math.random()*(anagram.length)))];
    let count = anagram.length - 1;

    word = document.getElementById('word');
    count = document.getElementById('left');
    answer = document.getElementById('answer');
    list = document.getElementById('list');
    list = []

window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {
    
    let correctAnswer = anagram;
    document.getElementById('answer').innerHTML=answer;
    
    if (correctAnswer.indexOf(answer) !== -1 && question !== answer) {
        playerScore+=1;
        document.getElementById('playerScore').innerHTML=playerScore;
        document.getElementById('answer').focus();
        this.list.push(answer);
        count+=1;
    }
    else if (correctAnswer.indexOf(answer) === -1 || question === answer) {
        alert('You already got that word or this is not a valid anagram.')
    }

    let playerScore = + this.document.getElementById('playerScore').innerHTML;

    if (count == 0) {
        alert('You got all the anagrams for this word!')
    }

    let word = this.anagram[Math.floor(Math.random()*this.anagram.length)];
    let count = this.anagram.length - 1;

    document.getElementById('word').innerHTML=word;
    document.getElementById('left').innerHTML=count;
    document.getElementById('answer').focus();
    document.getElementById('list').innerHTML=list;
    list = []
    }
});
});