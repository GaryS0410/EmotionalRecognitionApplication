let canvas = document.getElementById('webcamCanvas');
let video = document.getElementById('video');

let context = canvas.getContext('2d');

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        video.srcObject = stream;
        video.play();
    }).catch((err) => {
        console.log('Could not access webcam/no webcam to access.')
        alert("No functional webcam detected. Please make sure to plug in a suitable webcam and allow your browser access to it.")
    })
}

// Upload function to send images to backend
function upload(file) {
    var formdata = new FormData();
    formdata.append('snap', file);

    fetch('/get_therapy_image', {
        method: 'POST',
        body: formdata
    })
    .then(response => response.blob())
    .catch(error => {
        console.error(error);
    })
}

// Take photo function which draws the image on the canvas.
function takePhoto() {
    context.drawImage(video, 0, 0, 640, 480);
    canvas.toBlob(upload, 'image/jpeg', 0.95);
}

// Clearing images request
function clearTherapyImages() {
    fetch('/clear_therapy_images')
        .then(response => response.text())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
}

// Event listeners and button related functionality
document.getElementById('start').addEventListener('click', () => {
    toggleStartButton(true);
    // disableSessionLengthButton(true);
    enableStopButton();
    takePhoto();
    intervalID = setInterval(takePhoto, 3000);
})

document.getElementById('stop').addEventListener('click', () => {
    clearInterval(intervalID);
    alterStartButton(true);
    disableStopButton();
})

// Clearing images trigger 
window.addEventListener('DOMContentLoaded', (event) => {
    clearTherapyImages();
    disableStopButton();
})

// Disables both stop/start
function disableButtons() {
    document.getElementById('start').disabled = true;
    document.getElementById('stop').disabled = true;
}

// Can disable/enable start
function toggleStartButton(isDisabled) {
    document.getElementById('start').disabled = isDisabled;
}

// Disables stop
function disableStopButton() {
    var stopButton = document.getElementById('stop');

    stopButton.classList.add("disabled");
}

// Enables stop
function enableStopButton() {
    var stopButton = document.getElementById('stop');

    stopButton.classList.remove("disabled");
}

// function disableSessionLengthButton(isDisabled) {
//     document.getElementById('sessionLength').disabled = isDisabled;
// }