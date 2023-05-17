let canvas = document.querySelector('#webcamCanvas');
let context = canvas.getContext('2d');
let video = document.querySelector('#video');

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        video.srcObject = stream;
        video.play();
    }).catch((err) => {
        console.log('not working');
    });
}

function upload(file) {
    var formdata = new FormData();
    formdata.append('snap', file);

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
    canvas.toBlob(upload, 'image/jpeg', 0.95);
}