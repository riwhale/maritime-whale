# NOTES:
# https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer
# https://plotly.com/python/mapbox-layers/

# NOAA leads:
# https://tileservice.charts.noaa.gov/tiles/tileservice.xml
# https://tileservice.charts.noaa.gov/tileset.html#50000_1-mapbox
# https://geo.weather.gc.ca/geomet/ (<-- in mapbox-layers example; see link)

from import_vessel_data import *

import plotly.express as px
import pandas as pd

def generate_plots(map_data):
    charleston = map_data[0]
    savannah =  map_data[1]
    agg =  map_data[2]
    zooms = [10, 10, 8.5]

    figs = {"charleston":None, "savannah":None, "agg":None}
    for i, view in enumerate(figs.keys()):
        figs[view] = px.scatter_mapbox(map_data[i], lat="Latitude", lon="Longitude",
                                       hover_name="Name", hover_data=["MMSI",
                                       "Date/Time UTC", "Max speed kn",
                                       "Mean speed kn", "LOA m", "LOA ft"],
                                       color_discrete_sequence=["white"],
                                       zoom=zooms[i], height=600)
        figs[view].update_traces(opacity=0.25,
                                 selector=dict(type='scattermapbox'))
        figs[view].update_layout(
            mapbox_style="open-street-map",
            mapbox_layers=[
                {
                    "below": "traces",
                    "sourcetype": "raster",
                    "sourceattribution": "Esri",
                    "source": [
                        "https://services.arcgisonline.com/arcgis/rest/" +
                        "services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
              ],
              showlegend=False)
        figs[view].update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return figs["agg"], figs["charleston"], figs["savannah"]
