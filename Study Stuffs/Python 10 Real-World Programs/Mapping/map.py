import folium as fol
from folium.map import Icon, Marker, Popup
import pandas as pd

df = pd.read_csv('Volcanoes.txt')

lon = list(df['LON'])
lat = list(df['LAT'])
elev = list(df['ELEV'])

map = fol.Map(location=[38.58, -99.09], zoom_start=6, tiles='OpenStreetMap')


def color_set(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


fgv = fol.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(fol.CircleMarker(location=[lt, ln], radius=6, popup=str(
        el)+' m', fill_color=color_set(el), color='grey', fill_opacity=0.7))

fgp = fol.FeatureGroup(name='Populations')

fgp.add_child(fol.GeoJson(data=open('world.json', mode='r', encoding='utf-8-sig').read(), style_function=lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 4000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fol.LayerControl())

map.save('USA Volcanoes.html')
