
var url = "./js/final_w_lat_lon.json"

var myMap = L.map("map", {
    center: [
      36.7783, -119.4179
    ],
    zoom: 6,
  });

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

// Perform a GET request to the query URL
d3.json(url, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data);
});


function createFeatures(sourceData) {




for (var i = 0; i < sourceData.length; i++) {

/*   // Conditionals for magnitude
  var color = "";
  if (sourceData[i].properties.mag > 5) {
    color = "red";
  }
  else if (sourceData[i].properties.mag > 4) {
    color = "orange";
  }
  else if (sourceData[i].properties.mag > 3) {
    color = "yellow";
  }
  else {
    color = "green";
  }
 */
var coords = [sourceData[i].Lat,sourceData[i].Lon]

var selectData = sourceData[i]["2016RENT"]

  // Add circles to map
L.circle(coords,{
    radius: selectData*5,
    fillColor: "blue",
    color: "black",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
}).addTo(myMap).bindPopup("<h3>" + sourceData[i].NAME);



}};
