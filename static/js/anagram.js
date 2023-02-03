window.addEventListener('load', function math() {
  
   

    fetch('/static/json/anagrams.json')
        .then((response) => response.json())
        .then(data => {
            const anagrams = data.anagrams
            let array = function(arr) {
                if ( typeof(arr) == "object") {
                    for (var i = 0; i < arr.length; i++) {
                        array(arr[i]);
                    }
                }
                else document.write(arr);
            }
            
            array(anagrams);
        })
    ;
    
    anagram5 = anagrams['5']

    let anagram5 = this.anagram5[Math.floor(Math.random()*this.anagram5.length)];
    anagram6 = this.anagram6[Math.floor(Math.random()*this.anagram6.length)];
    anagram7 = this.anagram7[Math.floor(Math.random()*this.anagram7.length)];
    anagram8 = this.anagram8[Math.floor(Math.random()*this.anagram8.length)];

    let anagram;
    const wordLength = (document.getElementById('wordlength'));

    if (wordLength == 5) {
        anagram = anagram5
    } else if (wordLength == 6) {
        anagram = rand6
    } else if (wordLength == 7) {
        anagram = rand7
    } else {
        anagram = rand8
    }

    let word = anagram[Math.floor(Math.random()*anagram.length)];
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