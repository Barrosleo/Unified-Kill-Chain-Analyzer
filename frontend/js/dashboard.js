// Fetch the logs from the API endpoint exposed by the Flask backend
fetch('http://localhost:5000/api/logs')
  .then(response => response.json())
  .then(data => {
    // Count events per phase
    const phaseCounts = {};
    data.forEach(event => {
      phaseCounts[event.phase] = (phaseCounts[event.phase] || 0) + 1;
    });
    const labels = Object.keys(phaseCounts);
    const counts = Object.values(phaseCounts);

    const ctx = document.getElementById('killChainChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Number of Events',
          data: counts,
          backgroundColor: 'rgba(153, 102, 255, 0.6)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  .catch(error => console.error('Error fetching logs:', error));
