let canvas = document.getElementById('webcamCanvas');
let context = canvas.getContext('2d');
let video = document.querySelector('#video');

let intervalID;

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        video.srcObject = stream;
        video.play();
    }).catch((err) => {
        console.log('not working');
    });
}

document.getElementById('start-questionnaire').addEventListener('click', function () {
    intervalID = setInterval(takePhoto, 10000);
})

function upload_image(captured_image) {
    var formdata = new FormData();
    formdata.append('snap', captured_image);

    fetch('/get_questionnaire_image', {
        method: 'POST',
        body: formdata,
    })
        .then(response => response.blob())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        })
}

function takePhoto() {
    context.drawImage(video, 0, 0, 640, 480);
    canvas.toBlob(upload_image, 'image/jpeg', 1);
}

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