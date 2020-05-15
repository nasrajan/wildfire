/**
 * Initialize the Google Map and add our custom layer overlay.
 * @param {string} mapid
 * @param {string} token
 */

var map;
const initialize = (mapid, token) => {
  // Create an ImageOverlay using the MapID and token we got from App Engine.
  const tileSource = new ee.layers.EarthEngineTileSource({mapid, token});
  const layer = new ee.layers.ImageOverlay(tileSource);

  //const myLatLng = new google.maps.LatLng(-34.397, 150.644);
  const myLatLng = new google.maps.LatLng(32.84, -117.20);
  const mapOptions = {
    center: myLatLng,
    zoom: 8  ,
    maxZoom: 10,
    streetViewControl: false,
  };

  // Create the base Google Map.
  //const map = new google.maps.Map(document.getElementById('pred'), mapOptions);
  map = new google.maps.Map(document.getElementById('pred'), mapOptions);

  // Add the EE layer to the map.
  map.overlayMapTypes.push(layer);
 // grid = new Graticule(map, true);
  return map;

};

function getLatLong() {
  return new google.maps.LatLng(32.84, -117.20);
}