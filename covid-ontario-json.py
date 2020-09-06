# https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/4f39b02b-47fe-4e66-95b6-e6da879c6910/download/conposcovidloc.geojson

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = "data/conposcovidloc.geojson"
with open(filename) as f:
    all_covid_data = json.load(f)

all_covid_dicts = all_covid_data["features"]
print(len(all_covid_dicts))

ages, lons, lats = [], [], []
for eq_dict in all_covid_dicts:
    age = eq_dict["properties"]["Age_Group"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]

    ages.append(age)
    lons.append(lon)
    lats.append(lat)

# print(ages[:10])
# print(lons[:5])
# print(lats[:5])

# Map the COVID-19 cases.
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats
}]

my_layout = Layout(title="Ontario COVID-19 Cases")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="ontario_covid19.html")