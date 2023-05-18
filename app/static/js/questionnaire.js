function nextQuestion() {
    var currentQuestion = $(".question:visible");
    var nextQuestion = currentQuestion.next(".question");
    var currentAnswer = currentQuestion.find("input:checked").val();

    if(currentAnswer) {
        if (nextQuestion.length) {
            currentQuestion.hide();
            currentQuestion.find("input").prop("disabled", true);
            nextQuestion.show();
            nextQuestion.find("input").prop("disabled", false);
        } else {
            $(".question input").prop("disabled", false);
            document.getElementById("questionnaire-form").submit();
        }
    } else {
        alert("Answer before continuing")
    }
}

function previousQuestion() {
    var currentQuestion = $(".question:visible");
    var lastQuestion = currentQuestion.prev(".question");

    if(lastQuestion.length) {
        currentQuestion.hide();
        currentQuestion.find("input").prop("disabled", true);
        lastQuestion.show();
        lastQuestion.find("input").prop("disabled", false);
    }
}

function clearQuestionnaireImages() {
    fetch('/clear_questionnaire_images')
        .then(response => response.text())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    clearQuestionnaireImages();
})