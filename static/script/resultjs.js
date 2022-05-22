function run() {
    if (sessionStorage.user != undefined) var obj = JSON.parse(sessionStorage.user);

    console.log(obj)
    var src_lat = document.getElementById('src_lat');
    // src_lat.innerHTML = obj.name;


    var Src_Lng = document.getElementById('Src_Lng');
    Src_Lng.innerHTML = "sourceLongitude";

    var Dest_Lat = document.getElementById('Dest_Lat');
    Dest_Lat.innerHTML = "DestLatitude";


    var Dest_Lng = document.getElementById('Dest_Lng');
    Dest_Lng.innerHTML = "DestLongitude";

    var Src_Port_Country = document.getElementById('Src_Port_Country');
    Src_Port_Country.innerHTML = "" + " in " + " ";

    var Dest_Port_Country = document.getElementById('Dest_Port_Country');
    Dest_Port_Country.innerHTML = "" + " in " + " ";
}


