// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    window.initializeMap = () => {
        const map = new Microsoft.Maps.Map(document.getElementById('map'), {
            credentials: 'Bing_Maps_Key',  
            center: new Microsoft.Maps.Location(-1.280555, 36.808945), // Nairobi location
            zoom: 10
        });

        const optimizeButton = document.getElementById('optimizeButton');
        optimizeButton.addEventListener('click', () => {
            fetch('/optimize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ locations: locations }) // Replace with my locations data
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert('Route optimized!');
                    // Add logic to update the map with the optimized route
                    const routeCoordinates = data.map(location => new Microsoft.Maps.Location(location.lat, location.lng));
                    const routeLine = new Microsoft.Maps.Polyline(routeCoordinates, { strokeColor: 'blue', strokeThickness: 3 });
                    map.entities.clear();
                    map.entities.push(routeLine);
                    map.setView({ bounds: Microsoft.Maps.LocationRect.fromLocations(routeCoordinates) });
                }
            })
            .catch(error => console.error('Error:', error));
        });

        document.getElementById('map').addEventListener('click', () => {
            document.getElementById('overlay').style.display = 'flex';
        });

        // Close overlay when the close button is clicked
        document.getElementById('closeOverlayButton').addEventListener('click', () => {
            document.getElementById('overlay').style.display = 'none';
        });

        // Handle form submissions
        ['locationSearchForm', 'nearbyPlacesForm', 'routeFinderForm', 'loginForm', 'createLocationForm', 'updateLocationForm'].forEach(formId => {
            document.getElementById(formId).addEventListener('submit', (event) => {
                event.preventDefault();

                const formData = new FormData(event.target);
                const data = Object.fromEntries(formData);

                let endpoint = '/my-endpoint'; // Replace with your actual endpoint
                let method = 'POST';

                if (formId === 'updateLocationForm') {
                    endpoint += `/${data.locationId}`;
                    method = 'PUT';
                }

                fetch(endpoint, {
                    method: method,
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    // Handle the response data
                    alert(`Form ${formId} submitted successfully.`);
                })
                .catch(error => console.error('Error:', error));
            });
        });
    };
});