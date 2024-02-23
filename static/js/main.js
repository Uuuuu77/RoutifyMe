// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    window.initializeMap = () => {
        const map = new Microsoft.Maps.Map(document.getElementById('map'), {
            credentials: 'YOUR_BING_MAPS_API_KEY', // Replace with your actual Bing Maps API key
            center: new Microsoft.Maps.Location(37.7749, -122.4194), // Example: San Francisco
            zoom: 10
        });

        const optimizeButton = document.getElementById('optimizeButton');
        optimizeButton.addEventListener('click', () => {
            alert('Optimizing route...');
            // Add your route optimization logic here
        });

        document.getElementById('map').addEventListener('click', () => {
            document.getElementById('overlay').style.display = 'flex';
        });
    };
});
