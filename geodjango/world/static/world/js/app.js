const initialLnglat = [42.7875, 141.6813];
const initialZoom = 10;

let map = L.map('map');
map.setView(initialLnglat, initialZoom);

const pale = L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png', {
    attribution:
        "<a href='http://portal.cyberjapan.jp/help/termsofuse.html' target='_blank'>国土地理院</a>",
}).addTo(map);
const maptiler = L.tileLayer(
    'https://api.maptiler.com/maps/jp-mierune-streets/{z}/{x}/{y}.png?key=[Maptiler API key]',
    {
        attribution:
            '<a href="https://maptiler.jp/" target="_blank">© MIERUNE</a> <a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>',
    }
);

L.control
    .layers({
        '地理院地図 淡色': pale,
        'MapTiler MIERUNE Street': maptiler,
    })
    .addTo(map);

const apiUrl = '/api/world/';
const origin = 'http://localhost:8000';
const airportStyle = {
    weight: 6,
    color: '#ff4500',
    fillColor: '#00FF00',
    fillOpacity: 0.3,
};

let calcSelect = document.getElementById('calc');
let airportSelect = document.getElementById('airport');
let currentAirport;
let currentPolygon;
addAirport();

function updateMap() {
    if (currentAirport) map.removeLayer(currentAirport);
    if (currentPolygon) map.removeLayer(currentPolygon);

    const url = airportSelect.value
        ? `${apiUrl}centroid_lnglat?airport=${airportSelect.value}`
        : `${apiUrl}centroid_lnglat`;

    fetch(url)
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            const lnglat = data.lnglat;
            map.setView([lnglat[1], lnglat[0]], initialZoom);
        });
}

function addAirport() {
    const url = airportSelect.value
        ? `${apiUrl}airport?name=${airportSelect.value}`
        : `${apiUrl}airport`;

    fetch(url)
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            currentAirport = L.geoJson(data, {
                style: airportStyle,
                onEachFeature: function (feature, layer) {
                    layer.bindPopup(feature.properties.c28_005);
                },
            }).addTo(map);
        });
}

function addPolygon(calc) {
    const url = airportSelect.value
        ? `${apiUrl}${calc}?airport=${airportSelect.value}`
        : `${apiUrl}${calc}`;
    const endpoint = document.getElementById('endpoint');
    endpoint.style.display = 'inline';
    endpoint.setAttribute('href', `${origin}${url}`);

    fetch(url)
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            currentPolygon = L.geoJson(data, {
                onEachFeature: function (feature, layer) {
                    if (feature.properties.n03_004) {
                        layer.bindPopup(feature.properties.n03_004);
                    } else if (feature.properties.n03_003) {
                        layer.bindPopup(feature.properties.n03_003);
                    }
                },
            }).addTo(map);
        });
}

function addPopup(calc) {
    const url = airportSelect.value
        ? `${apiUrl}${calc}?airport=${airportSelect.value}`
        : `${apiUrl}${calc}`;
    const endpoint = document.getElementById('endpoint');
    endpoint.style.display = 'inline';
    endpoint.setAttribute('href', `${origin}${url}`);

    fetch(url)
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            alert(data.value);
        });
}

function buttonClick() {
    updateMap();
    addAirport();

    if (calcSelect.value == 'intersects') {
        addPolygon('intersects');
    } else if (calcSelect.value == 'crosses') {
        addPolygon('crosses');
    } else if (calcSelect.value == 'contains') {
        addPolygon('contains');
    } else if (calcSelect.value == 'within') {
        addPolygon('within');
    } else if (calcSelect.value == 'overlaps') {
        addPolygon('overlaps');
    } else if (calcSelect.value == 'disjoint') {
        addPolygon('disjoint');
    } else if (calcSelect.value == 'touches') {
        addPolygon('touches');
    } else if (calcSelect.value == 'left') {
        addPolygon('left');
    } else if (calcSelect.value == 'right') {
        addPolygon('right');
    } else if (calcSelect.value == 'overlaps_above') {
        addPolygon('overlaps_above');
    } else if (calcSelect.value == 'overlaps_below') {
        addPolygon('overlaps_below');
    } else if (calcSelect.value == 'distance_gt') {
        addPolygon('distance_gt');
    } else if (calcSelect.value == 'distance_gte') {
        addPolygon('distance_gte');
    } else if (calcSelect.value == 'distance_lt') {
        addPolygon('distance_lt');
    } else if (calcSelect.value == 'distance_lte') {
        addPolygon('distance_lte');
    } else if (calcSelect.value == 'dwithin') {
        addPolygon('dwithin');
    } else if (calcSelect.value == 'union') {
        addPolygon('union');
    } else if (calcSelect.value == 'asgeojson') {
        addPolygon('asgeojson');
    } else if (calcSelect.value == 'centroid') {
        addPolygon('centroid');
    } else if (calcSelect.value == 'boundingcircle') {
        addPolygon('boundingcircle');
    } else if (calcSelect.value == 'envelope') {
        addPolygon('envelope');
    } else if (calcSelect.value == 'distance') {
        addPopup('distance');
    }
}
