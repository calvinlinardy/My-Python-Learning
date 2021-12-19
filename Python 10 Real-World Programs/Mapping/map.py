import folium as fol
from folium.map import Icon, Marker, Popup
import pandas as pd

df = pd.read_csv('Volcanoes.txt')

lon = list(df['LON'])
lat = list(df['LAT'])

map = fol.Map(location=[38.58, -99.09], zoom_start=6, tiles='Stamen Terrain')

fg = fol.FeatureGroup(name='Map')
for ln, lt in zip(lon, lat):
    fg.add_child(fol.Marker(
        location=[ln, lt], popup='Hi I am Here!', icon=fol.Icon(color='green')))
map.add_child(fg)

map.save('Jakarta.html')
