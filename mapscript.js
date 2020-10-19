var map;

    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 7,
            center: new google.maps.LatLng(51.751110, 19.450170),
            mapTypeId: 'terrain'
        });

        // Create a <script> tag and set the USGS URL as the source.
        var script = document.createElement('script');
        // This example uses a local copy of the GeoJSON stored at
        // http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp
        script.src = 'mydata.js';
        document.getElementsByTagName('head')[0].appendChild(script);
    }




    // Loop through the results array and place a marker for each
    // set of coordinates.
    window.eqfeed_callback = function (results) {
        for (var i = 0; i < results.properties.length; i++) {

            var lat = results.properties[i].lat;
            var long = results.properties[i].long;
            var url = results.properties[i].url;
            var category = results.properties[i].category;
            var estimated_sum = results.properties[i].estimated_sum;
            var auction_date = results.properties[i].auction_date;
            var tooltip = "category: " +results.properties[i].category + " estimated_sum: " +estimated_sum + " auction_date: " + auction_date;
            var latLng = new google.maps.LatLng(lat, long);
            var marker = new google.maps.Marker({
                position: latLng,
                url: url,
                title: tooltip,
                map: map

            });

            if (category == 'grunty') {
                marker.setIcon('icons/shovel.png');
                }

            if (category == 'domy') {
                marker.setIcon('icons/house.png');
                }

            if (category == 'nieruchomo\u015bci' || category =='mieszkania') {
               marker.setIcon('icons/flats.png');
               }

            if (category == 'gara\u017ce, miejsca postojowe') {
               marker.setIcon('icons/garaz.png');
               }

            if (category == 'lokale u\u017cytkowe') {
               marker.setIcon('icons/local.png');
               }

              if (category == 'magazyny i hale') {
               marker.setIcon('icons/magazyn.png');
               }

            google.maps.event.addListener(marker, 'click', function () {

                window.open(this.url, '_blank');
            });
        }
    }