window.addEventListener('load', function anagram() {
    const anagram5 = [
        [
          "abets",
          "baste",
          "betas",
          "beast",
          "beats"
        ],
        [
          "acres",
          "cares",
          "races",
          "scare"
        ],
        [
          "alert",
          "alter",
          "later"
        ],
        [
          "angel",
          "angle",
          "glean"
        ],
        [
          "baker",
          "brake",
          "break"
        ],
        [
          "bared",
          "beard",
          "bread",
          "debar"
        ],
        [
          "dater",
          "rated",
          "trade",
          "tread"
        ],
        [
          "below",
          "bowel",
          "elbow"
        ],
        [
          "caret",
          "cater",
          "crate",
          "trace",
          "react"
        ]
    ]
    const anagram6 = [
        [
          "arrest",
          "rarest",
          "raster",
          "raters",
          "starer"
        ],
        [
          "carets",
          "caters",
          "caster",
          "crates",
          "reacts",
          "recast",
          "traces"
        ],
        [
          "canter",
          "nectar",
          "recant",
          "trance"
        ],
        [
          "danger",
          "gander",
          "garden",
          "ranged"
        ],
        [
          "daters",
          "trades",
          "treads",
          "stared"
        ]
    ]
    const anagram7 = [
        [
          "allergy",
          "gallery",
          "largely",
          "regally"
        ],
        [
          "aspired",
          "despair",
          "diapers",
          "praised"
        ],
        [
          "claimed",
          "decimal",
          "declaim",
          "medical"
        ],
        [
          "dearths",
          "hardest",
          "hatreds",
          "threads",
          "trashed"
        ],
        [
          "detains",
          "instead",
          "sainted",
          "stained"
        ]
    ]
    const anagram8 = [
        [
          "parroted",
          "predator",
          "prorated",
          "teardrop"
        ],
        [
          "repaints",
          "painters",
          "pantries",
          "pertains"
        ],
        [
          "restrain",
          "retrains",
          "strainer",
          "terrains",
          "trainers"
        ],
        [
          "construe",
          "counters",
          "recounts",
          "trounces"
        ]
    ]

    let rand5 = anagram5[(Math.floor(Math.random()*(anagram5.length)))];
    let rand6 = anagram6[(Math.floor(Math.random()*(anagram6.length)))];
    let rand7 = anagram7[(Math.floor(Math.random()*(anagram7.length)))];
    let rand8 = anagram8[(Math.floor(Math.random()*(anagram8.length)))];

    wordLength = Number(document.getElementById('word_length').innerHTML);

    let word = + this.document.getElementById('word').innerHTML;
    let count = + this.document.getElementById('left').innerHTML;

    let anagram;
    
    if (wordLength == 5) {
        anagram = rand5
    } else if (wordLength == 6) {
        anagram = rand6
    } else if (wordLength == 7) {
        anagram = rand7
    } else {
        anagram = rand8
    }

    word = anagram[(Math.floor(Math.random()*(anagram.length)))];
    count = anagram.length - 1;
    const correct = anagram

    document.getElementById('word').innerHTML=word;
    document.getElementById('left').innerHTML=count;
    document.getElementById('answer').focus();

window.addEventListener("keydown", function(e) {
    if (e.key === 'Enter' || e.keycode === 13) {
    
    let answer = document.getElementById('answer').innerHTML;
    let playerScore = + this.document.getElementById('playerScore').innerHTML;
    list = document.getElementById('list');
    list = []
    
    if (correct.indexOf(answer) !== -1 && answer !== word) {
        playerScore+=1;
        document.getElementById('playerScore').innerHTML=playerScore;
        document.querySelector('input[type=text]').value = "";               
        this.list.push(answer);
        count+=1;
    }
    else if (correct.indexOf(answer) === -1 || answer === word) {
        alert('You already got that word or this is not a valid anagram.')
        document.querySelector('input[type=text]').value = "";               
    }

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