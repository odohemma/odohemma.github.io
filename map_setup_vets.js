google.maps.event.addDomListener(window, 'load', initialize);
var markers = [];

var map; // The map object

var myCentreLat = 55.0;
var myCentreLng = -3.5;

var initialZoom = 5;

function infoCallback(infowindow, marker) {
  return function() {
    infowindow.open(map, marker);
  };
}

function addMarker(myPos, myTitle, myInfo) {
  //The marker variable which represents the vet locations is defined here
  var marker = new google.maps.Marker({
    position: myPos,
    map: map,
    title: myTitle,
    icon: 'veterinary.png'
  });


  //The variable for the marker's information window is defined here
  var infowindow = new google.maps.InfoWindow({
    content: myInfo,
    pixelOffset: new google.maps.Size(0, 15)
  });

  google.maps.event.addListener(marker, 'click', infoCallback(infowindow, marker));
}

function initialize() {
  //The map centre (which is the UK) is defined here
  var latlng = new google.maps.LatLng(myCentreLat, myCentreLng);
  var myOptions = {
    zoom: initialZoom,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

  //A loop to create 'Veterinary Clinic' title, 'Ref:', 'Postcode:' 
  //and 'LA:' tags in the information window is defined here.
  for (id in vet_markers) {
    var info = "<div class=infowindow><b>Veterinary Clinic</b><br>Ref: " + vet_markers[id].ref + "<br>Postcode: " +
      vet_markers[id].correctedp + "<br>LA: " + vet_markers[id].wd + "<br></div>";

    // Convert co-ords
    var osPt = new OSRef(vet_markers[id].easting, vet_markers[id].northing);
    var llPt = osPt.toLatLng(osPt);
    llPt.OSGB36ToWGS84();

    //This adds the defined markers and the information window to the map
    addMarker(new google.maps.LatLng(llPt.lat, llPt.lng), vet_markers[id].ref, info);
  }

  //This sets the maximum zoom level of the map
  google.maps.event.addListener(map, 'maptypeid_changed', function(event) {
    {
      map.setOptions({
        maxZoom: 17
      });
    }
  });



  // Create the search box and link it to the UI element.
  var input = /** @type {HTMLInputElement} */ (
    document.getElementById('pac-input'));
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  var searchBox = new google.maps.places.SearchBox(
    /** @type {HTMLInputElement} */
    (input));

  // Listen for the event fired when the user selects an item from the
  // pick list. Retrieve the matching places for that item.
  google.maps.event.addListener(searchBox, 'places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    for (var i = 0, marker; marker = markers[i]; i++) {
      marker.setMap(null);
    }

    // For each place, get the icon, place name, and location.
    markers = [];
    var bounds = new google.maps.LatLngBounds();
    for (var i = 0, place; place = places[i]; i++) {
      var image = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      markers.push(marker);

      bounds.extend(place.geometry.location);
    }

    map.fitBounds(bounds);
  });

  // Bias the SearchBox results towards places that are within the bounds of the
  // current map's viewport.
  google.maps.event.addListener(map, 'bounds_changed', function() {
    var bounds = map.getBounds();
    searchBox.setBounds(bounds);
  });


  // Add a marker clusterer to manage the markers.
  var markerCluster = new MarkerClusterer(map, markers, {
    imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
  });
}