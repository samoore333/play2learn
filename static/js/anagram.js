window.addEventListener('load', function math() {
    let anagram = this.anagram;
    
    fetch('/static/json/anagrams.json')
        .then((response) => response.json())
        .then((data) => console.log(data))
    ;

    const anagrams = JSON.parse()

    for (anagram in anagrams) {
        anagram5 = (anagrams['anagram5'])
        anagram6 = (anagrams['anagram6'])
        anagram7 = (anagrams['anagram7'])
        anagram8 = (anagrams['anagram8'])
    }

    let anagram5 = this.anagram5[Math.floor(Math.random()*this.anagram5.length)];
    let anagram6 = this.anagram6[Math.floor(Math.random()*this.anagram6.length)];
    let anagram7 = this.anagram7[Math.floor(Math.random()*this.anagram7.length)];
    let anagram8 = this.anagram8[Math.floor(Math.random()*this.anagram8.length)];

    const wordLength = Number(document.getElementById('wordlength').innerHTML);

    if (wordLength == 5) {
        anagram = anagram5
    } else if (wordLength == 6) {
        anagram = anagram6
    } else if (wordLength == 7) {
        anagram = anagram7
    } else {
        anagram = anagram8   
    }

    let word = this.anagram[Math.floor(Math.random()*this.anagram.length)];
    let count = this.anagram.length - 1;

    document.getElementById('word').innerHTML=word;
    document.getElementById('left').innerHTML=count;
    document.getElementById('answer').focus();
    document.getElementById('list').innerHTML=list;
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
        count+=-1;
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