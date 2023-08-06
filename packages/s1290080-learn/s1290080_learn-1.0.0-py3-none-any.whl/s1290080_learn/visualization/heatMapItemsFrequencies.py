import plotly.express as px
import pandas as pd
import re

class heatMapItemsFrequencies:
    def __init__(self, itemsFrequenciesDictionary):
        self.itemsFrequenciesDictionary  = itemsFrequenciesDictionary
    
    def plotHeatMap(self):
        latitudes = []
        longitudes = []
        vals = []
        for v in list(self.itemsFrequenciesDictionary.items()):
            try:
                lg, lt = re.findall('\d+\.\d+', v[0])
                latitudes.append(float(lt))
                longitudes.append(float(lg))
                vals.append(v[1])
            except:
                continue
        df = pd.DataFrame()
        df["latitude"] = latitudes
        df["longitude"] = longitudes
        df["val"] = vals
        fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='val', radius=10, zoom=4)
        fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()
