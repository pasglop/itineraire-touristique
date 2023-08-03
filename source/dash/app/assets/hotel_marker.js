window.mapMarkerItinary = Object.assign({}, window.mapMarkerItinary, {
    hotel: {
        pointToLayer: function(feature, latlng){
            const hotelicon = L.icon({
              iconUrl: '/assets/icons/hotel.png',
              iconSize: [64, 64]
            });
            return L.marker(latlng, {icon: hotelicon});
        }
    },
    other: {
        pointToLayer: function(feature, latlng){
            const markicon = L.icon({
              iconUrl: '/assets/icons/' + feature.properties.type + '.png',
              shadowUrl: '/assets/icons/marker-shadow.png',
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
              shadowSize: [41, 41]
            });
            return L.marker(latlng, {icon: markicon});
        }
    }
});