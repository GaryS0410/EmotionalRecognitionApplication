let canvas = document.getElementById('webcamCanvas');
let video = document.getElementById('video');

let context = canvas.getContext('2d');

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

// Everything button related 
document.getElementById('start')

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

// Clearing images trigger 
window.addEventListener('DOMContentLoaded', (event) => {
    clearTherapyImages();
})