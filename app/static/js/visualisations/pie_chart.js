var emotion_colours = {
    "angry": "red",
    "disgust": "green",
    "fear": "black",
    "happy": "yellow",
    "sad": "blue",
    "surprise": "orange",
    "neutral": "gray"
}

function createPieChart(ctx, emotionsData) {
    var labels = [];
    var data = [];

    for (var emotion in emotionsData) {
        labels.push(emotion);
        data.push(emotionsData[emotion])
    }

    var label_colours = labels.map(label => emotion_colours[label]);

    // maybe rename the "chart" variable to something more appropriate when it is in use
    var chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: label_colours
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: 'white'
                    },
                }
            },
            responsive: true,
            maintainAspectRatio: true,
            legend: {
                labels: {
                    color: '#c7c6cd'
                },
            },
        },
    });
}