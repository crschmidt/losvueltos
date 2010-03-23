var map;

/* 
    Configuration of the thematic map's stratification 
    i.e. Which numbers go with which colors.
*/
var setRGB = function ( green ){
    green = parseInt(green);
    green += ""
    rgb = 'rgb(220,' + green + ',0)'
    return rgb;
}
var context = {
    getColor: function(feature) {
        var rate = feature.data.unemployment_rate;
        var max_green = 255;
        var min_green = 1;
        var ceiling = 35;
        if (rate > ceiling) { setRGB( max_green )}
        var green = max_green - ((max_green - min_green) * (rate / ceiling))
        return setRGB(green);
    }
};

/* Firing up the map */
function load_map() {

    // The boundaries of California
    var max_extent = new OpenLayers.Bounds(-20037508.34, -20037508.34, 20037508.34, 20037508.34);

    var options = {
        projection: new OpenLayers.Projection("EPSG:4326"),
        displayProjection: new OpenLayers.Projection("EPSG:4326"),
        units: "m",
        numZoomLevels: 18,
        maxResolution: 156543.0339,
        maxExtent: max_extent,
        controls: [],
    };
    
    // Assigning it to an element in the HTML
    map = new OpenLayers.Map('bigmap', options);
    
    nav = new OpenLayers.Control.Navigation({'zoomWheelEnabled': true});
    map.addControl(nav);
    /* Configuration of the map's cosmetic style '*/
    var style = new OpenLayers.Style({
        strokeColor : '#DDDDDD', 
        strokeWidth: 1,
        strokeOpacity: 0.4,
        fillColor : "${getColor}", 
        fillOpacity : 0.90, 
        pointRadius : 3,
        strokeLinecap: "round"
    }, { context: context });

    var styleMap = new OpenLayers.StyleMap({
        'default': style, 
        'select': new OpenLayers.Style({
            fillColor : "#ff9400",
            fillOpacity : 0.98,
            strokeWidth : 3,
            strokeOpacity: 0.90
            }, { context: context })
    });

    // create Google Mercator layers
    var gmap = new OpenLayers.Layer.Google(
        "Google Maps",
        {'sphericalMercator': true, type: G_PHYSICAL_MAP}
    );
    map.addLayers([gmap]);
    
    var rays = new OpenLayers.Layer.Markers("Rays");
    map.addLayer(rays);
    // Loop through all the counties and make a vector layer for each
    {% for object in object_list %}
    var polygon_{{ object.id }} = new OpenLayers.Geometry.Point({{ object.geopoint.x }}, {{ object.geopoint.y }});
    polygon_{{ object.id }}.data = { 
        'error': {{ object.error }}
        };
    {% endfor %}

    var size = new OpenLayers.Size(10,17);
    var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
    var icon = new OpenLayers.Icon('http://mmxz.zophar.net/rpg/mana/magic/thunder_bolt.gif', size, offset);
    
    {% for object in object_list %}
    rays.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat({{ object.lon }}, {{ object.lat }}),icon));
    {% endfor %}
    rays.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(1, 12),icon.clone()));

    // Set the center of the map and zoom there
    var lon = 1500000; // SPAIN: var lon = -350000; 
    var lat = 6000000; // SPAIN: var lat = 5000000;
    var zoom = 2;
    map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);

};
