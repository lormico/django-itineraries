// Initialize and add the map
let map;
let infowindow;

function initMap() {
    // Roba per i livelli vv
    const LayerOverlay = function () {
        this.overlays = [];
    }
    LayerOverlay.prototype = new google.maps.OverlayView();
    LayerOverlay.prototype.addOverlay = function (overlay) {
        this.overlays.push(overlay);
    };
    LayerOverlay.prototype.updateOverlays = function () {
        for (let i = 0; i < this.overlays.length; i++) {
            this.overlays[i].setMap(this.getMap());
        }
    };
    LayerOverlay.prototype.draw = function () {
    };
    LayerOverlay.prototype.onAdd = LayerOverlay.prototype.updateOverlays;
    LayerOverlay.prototype.onRemove = LayerOverlay.prototype.updateOverlays;
    // ^^ roba per i livelli

    const seenDays = new Set();
    const dayLists = new Map();

    const centerPosition = {lat: 35.344, lng: 131.031};

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: centerPosition,
        disableDefaultUI: true,
    });

    const staysData = new google.maps.Data({map: map});
    fetch("http://localhost:8000/data/stays")
        .then(response => response.json())
        .then(data => {
            data.features.forEach(feature => {
                const addedFeature = staysData.addGeoJson(feature);
                const day = feature.extraProperties.start.slice(0, 10);
                seenDays.add(day)
                if (!dayLists.has(day)) {
                    dayLists[day] = [];
                }
                dayLists[day].push(addedFeature);
            })
        });
    /*const staysLayer = new LayerOverlay();
    staysLayer.addOverlay(createMarker({lat: 35, lng: 131}));
    staysLayer.addOverlay(createMarker({lat: 22, lng: 131}));
    staysLayer.addOverlay(createMarker({lat: 42, lng: 150}));
    staysLayer.setMap(map);*/

    initZoomControl(map);
    initMapTypeControl(map);
    initToggleControl(map, staysData);

    infowindow = new google.maps.InfoWindow();

    staysData.addListener('click', function (event) {
        const feat = event.feature;
        let html = "<b>" + feat.getProperty('name') + "</b><br>" + feat.getProperty('price') + " " + feat.getProperty('price_currency');
        infowindow.setContent(html);
        infowindow.setPosition(event.latLng);
        infowindow.setOptions({pixelOffset: new google.maps.Size(0, -34)});
        infowindow.open(map);
    });

}

function initZoomControl(map) {
    document.querySelector(".zoom-control-in").onclick = function () {
        map.setZoom(map.getZoom() + 1);
    };

    document.querySelector(".zoom-control-out").onclick = function () {
        map.setZoom(map.getZoom() - 1);
    };

    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(
        document.querySelector(".zoom-control"),
    );
}

function initMapTypeControl(map) {
    const mapTypeControlDiv = document.querySelector(".maptype-control");

    document.querySelector(".maptype-control-map").onclick = function () {
        mapTypeControlDiv.classList.add("maptype-control-is-map");
        mapTypeControlDiv.classList.remove("maptype-control-is-satellite");
        map.setMapTypeId("roadmap");
    };

    document.querySelector(".maptype-control-satellite").onclick = function () {
        mapTypeControlDiv.classList.remove("maptype-control-is-map");
        mapTypeControlDiv.classList.add("maptype-control-is-satellite");
        map.setMapTypeId("hybrid");
    };

    map.controls[google.maps.ControlPosition.LEFT_TOP].push(mapTypeControlDiv);
}

function initToggleControl(map, layer) {
    const toggleControlDiv = document.querySelector(".fullscreen-control");

    toggleControlDiv.onclick = function () {
        if (hasMap(layer)) {
            layer.setMap(null);
        } else {
            layer.setMap(map);
        }
    };

    map.controls[google.maps.ControlPosition.RIGHT_TOP].push(toggleControlDiv);
}

function initLayerSelector(map) {
    
}

function hasMap(stuff) {
    return !(stuff.getMap() == null);
}

window.initMap = initMap;
