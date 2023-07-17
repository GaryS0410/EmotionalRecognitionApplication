function createScoreGraph(ctx, labels, data, label_type) {
    var line_graph = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: label_type,
                data: data,
                backgroundColor: 'rgb(75, 192, 192)',
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.4
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: '#66CCCC'
                    },
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
}

function createEmotionalStateGraph(ctx, labels, data) {
    var line_graph = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: "Emotional State Scores",
                data: data,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: '#FF6384'
                    },
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 0.1
                    }
                }
            }
        }
    });
}