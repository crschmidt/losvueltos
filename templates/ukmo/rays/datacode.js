
    
    // Creating a tool to read in WKT formatted geospatial data
    var wkt_f = new OpenLayers.Format.WKT();
    
    // Loop through all the counties and make a vector layer for each
    {% for object in object_list %}
    var polygon_{{ object.county.id }} = wkt_f.read('{{ object.county.simple_polygon_900913 }}');
    polygon_{{ object.county.id }}.data = { 
        'unemployment_rate': {{ object.unemployment_rate }},
        'unemployment': "{{ object.unemployment|intcomma }}",
        'name': "{{ object.county.name }}"
        };
    {% endfor %}
    
    // Create a vector layer that will display all the data
    var county_vector = new OpenLayers.Layer.Vector("Counties");
    county_vector.styleMap = styleMap;
    // Then add all the polygons to the vector layer
    county_vector.addFeatures([{% for object in object_list %}polygon_{{ object.county.id }}{% if not forloop.last %}, {% endif %}{% endfor %}]);
    
    // Hook some functions to the events that trigger when somebody mouses
    // over the counties on the map
    var selectControl = new OpenLayers.Control.SelectFeature(county_vector, {
        hover: true,
        onSelect: select_feature,
        onUnselect: unselect_feature
    });
                
    // Add the counties to the map
    map.addLayer(county_vector);
    // Turn on the control
    map.addControl(selectControl);
    selectControl.activate();

