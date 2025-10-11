import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h3>Volcano information:</h3>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="OpenStreetMap")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=300, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(
        iframe), icon=folium.Icon(color="green")))


map.add_child(fg)
map.save("Map_html_popup_simple.html")
