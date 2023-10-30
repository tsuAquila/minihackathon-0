document.addEventListener("DOMContentLoaded", function() {
    const questions = [
        {
            question: "Would you rather have the ability to fly or be invisible?",
            option1: "Fly",
            option2: "Invisible"
        },
        {
            question: "Would you rather want to find true love or win lottery next month?",
            option1: "True Love",
            option2: "Win Lottery"
        },
        {
            question: "Would you rather have everyone you know be able to read your thoughts or for everyone you know to have access to your Internet history?",
            option1: "Read Thoughts",
            option2: "Internet Access"
        },
        {
            question: "Would you rather lose your sight or your memories?",
            option1: "Lose Sight",
            option2: "Lose memories"
        },
        {
            question: "Would you rather give up air conditioning and heating for the rest of your life or give up the Internet for the rest of your life?",
            option1: "Give up ac",
            option2: "give up internet"
        },
        {
            question: "Would you rather never be able to go out during the day or never be able to go out at night?",
            option1: "During Day",
            option2: "During Night"
        },
        {
            question: "would you rather be royalty 100 years ago or average person 100 years from now",
            option1: "Royalty",
            option2: "Average person"
        },
    ];
    let currentQuestionIndex = 0;
    let countdown = 10;
    let countdownInterval;

    const questionElement = document.getElementById("question");
    const option1Button = document.getElementById("option1");
    const option2Button = document.getElementById("option2");
    const timerElement = document.getElementById("timer");

    option1Button.addEventListener("click", selectOption1);
    option2Button.addEventListener("click", selectOption2);

    function displayQuestion() {
        clearInterval(countdownInterval); // Reset countdown timer
        countdown = 10; // Reset countdown to 10 seconds
        countdownInterval = setInterval(updateCountdown, 1000); // Start countdown timer

        if (currentQuestionIndex < questions.length) {
            const currentQuestion = questions[currentQuestionIndex];
            questionElement.textContent = currentQuestion.question;
            option1Button.textContent = currentQuestion.option1;
            option2Button.textContent = currentQuestion.option2;
        } else {
            questionElement.textContent = "No more questions available.";
            option1Button.style.display = "none";
            option2Button.style.display = "none";
        }
    }

    function updateCountdown() {
        if (countdown > 0) {
            countdown--;
            timerElement.textContent = countdown;
        } else {
            // Time's up, do something (e.g., show the next question)
            clearInterval(countdownInterval);
            nextQuestion();
        }
    }

    function nextQuestion() {
        currentQuestionIndex++;
        displayQuestion(); // Load the next question
    }

    function selectOption1() {
        // Handle the selection of Option 1 (e.g., update the UI, keep score)
        // For demonstration, we'll just alert the choice:
        alert("You chose Option 1: " + questions[currentQuestionIndex].option1);
        nextQuestion();
    }

    function selectOption2() {
        // Handle the selection of Option 2 (e.g., update the UI, keep score)
        // For demonstration, we'll just alert the choice:
        alert("You chose Option 2: " + questions[currentQuestionIndex].option2);
        nextQuestion();
    }

    // Start the game by displaying the first question
    displayQuestion();
});


