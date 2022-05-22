// This will draw a 2-pixel-wide red polyline showing the path of
// Between the given points
async function jsonget() {
  var sourceCity = document.getElementById("source_city").value;
  var sourceCountry = document.getElementById('src_country').value;
  var destCity = document.getElementById('dest_city').value;
  var destCountry = document.getElementById('dest_country').value;
  console.log(sourceCity, sourceCountry, destCity, destCountry);

  var url = new URL("https://api.publicapis.org/entries");
  var params = {
      st: sourceCity,
      sc: sourceCountry,
      dt: destCity,
      dc: destCountry
  }
  // console.log(params);
  // for (k in params) 
  // { url.searchParams.append(k, params[k]);}


  const response = await fetch(url);

  const data = await response.json();

  if (data === undefined) {
      alert("api not fetched ")
  }
  else {
      // console.log("hereee,data");
      sessionStorage.setItem("user", JSON.stringify(data))
  }
}

async function submitForm() {

  console.log("fetching data");

  if (sessionStorage.user != undefined) {
      sessionStorage.user = '';
  }
  await jsonget();
  console.log(sessionStorage, sessionStorage.user);
  location.href = "result.html"

}


function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 2,
      center: { lat:34.0479, lng: 78.9629},
      mapTypeId: "terrain",
    });
    const PlanCoordinates = [
        {lat: -19.76666667, lng: 34.83333333},
        { lat: 23.0, lng: 70.18333333},
      { lat:26.9124, lng:75.7873},
      { lat:22.5726, lng:88.3639},
    ];
    const Path = new google.maps.Polyline({
      path: PlanCoordinates,
      geodesic: true,
      strokeColor: "#000000",
      strokeOpacity: 1.0,
      strokeWeight: 2,
    });
     const beachMarker = new google.maps.Marker({
      position: PlanCoordinates[1],
      map,
      title: "Hello World!",
    });
    const beachMarker2 = new google.maps.Marker({
      position: PlanCoordinates[2],
      map,
      title: "Hello World!",
    });
    const beachMarker3 = new google.maps.Marker({
      position:  PlanCoordinates[3],
      map,
      title: "Hello World!",
    });
     const beachMarker1 = new google.maps.Marker({
      position: PlanCoordinates[0],
      map,
      title: "Hello World!",
    });
    
    
    Path.setMap(map);
   }
    
   window.initMap = initMap;
   