// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Code to run after the DOM is loaded

    // Your JavaScript logic here
    // For example, interacting with the Google Maps API, handling form submissions, etc.

    // Sample code to demonstrate a button click event
    const optimizeButton = document.getElementById('optimizeButton');
    optimizeButton.addEventListener('click', function() {
        // Placeholder code for optimization (replace with actual logic)
        alert('Optimizing route...');
        // You can make an AJAX request to the server to trigger route optimization
        // Example using fetch API:
        // fetch('/optimize', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ locations: /* your data here */ })
        // })
        // .then(response => response.json())
        // .then(data => {
        //     // Handle the optimized route data
        // });
    });
});
