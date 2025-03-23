function convertSTOtoJSON(stoContent) {
    return new Promise((resolve, reject) => {
        fetch('http://localhost:5000/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ stoContent: stoContent })
        })
        .then(response => response.json())
        .then(data => resolve(data))
        .catch(error => reject(error));
    });
}

fetch('./version2/data.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        const muscleForces = data.muscle_forces;
        const time = muscleForces.time;
        const muscleGroups = data.muscle_groups;

        const lineGraphContainer = document.getElementById('line-graph-container');
        let chartCount = 0;
        let currentRow;

        for (const groupName in muscleGroups) {
            const muscles = muscleGroups[groupName];

            const datasets = muscles.map(muscle => {
                const color = getRandomColor();
                return {
                    label: muscle,
                    data: muscleForces[muscle],
                    backgroundColor: color + '80',
                    borderColor: color,
                    fill: true
                };
            });

            const canvas = document.createElement('canvas');

            if (chartCount % 3 === 0) {
                currentRow = document.createElement('div');
                currentRow.classList.add('chart-row');
                lineGraphContainer.appendChild(currentRow);
            }

            currentRow.appendChild(canvas);

            new Chart(canvas, {
                type: 'line',
                data: {
                    labels: time,
                    datasets: datasets
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    plugins: {
                        legend: {
                            display: true,
                        },
                        title: {
                            display: true,
                            text: groupName
                        }
                    }
                }
            });

            chartCount++;
        }
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function getRandomColorWithOpacity(opacity) {
    const color = getRandomColor();
    return color.replace('#', '#' + opacity.toString(16));
}