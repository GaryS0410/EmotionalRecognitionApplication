function createPieChart(context, emotionsData) {
    var labels = [];
    var data = [];

    for (var emotion in data) {
        labels.push(emotion);
        data.push(emotionsData[emotion])
    }

    // maybe rename the "chart" variable to something more appropriate when it is in use
    var chart = new Chart(context, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
            }]
        },
        options: {
            responsive: true,
            legeng: {
                labels: {
                    // Add whatever the designated font color here
                    fontColor: '#'
                }
            }
        },
    });
}