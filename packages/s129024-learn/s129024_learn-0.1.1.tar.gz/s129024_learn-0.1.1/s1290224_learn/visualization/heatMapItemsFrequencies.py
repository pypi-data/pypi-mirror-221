# import necessary libraries
import pandas as pd
import plotly.express as px
import re

class heatMapItemsFrequencies:
    """
    A class to ccept the itemsFrequenciesDictionary
    and plot them on a map (plotly express open-street map)
    
    Attributes
    ----------
    itemsFrequenciesDictionary : str
        A dictionary contains the points and the frequency of each.
    
    Methods
    -------
    show()
        Prints the HeatMap. 
        The color of each pixel represents its frequency in the database. 
    """
    def __init__(self, itemsFrequenciesDictionary):
        """
        Parameters
        ----------
        itemsFrequenciesDictionary : str
            A dictionary contains the points and the frequency of each.
        """
        self.itemsFrequenciesDictionary = itemsFrequenciesDictionary
    
    def show(self):
        """
        Prints the HeatMap. 
        The color of each pixel represents its frequency in the database. 
        """
        
        # lists to store latitudes, longitudes, and counts
        latitudes = []
        longitudes = []
        counts = []
        
        # iterate over the dictionaly
        for key, value in self.itemsFrequenciesDictionary.items():
            # extract longtitude and latitude
            lst = re.findall("\d+\.\d*", key)
            # extract the count for the sensor
            count = value
            if lst != [] and count != []:
                # store the extracted longtitude
                longitudes.append(lst[0])
                # store the extracted latitude
                latitudes.append(lst[1])
                # store the extracted count
                counts.append(value)
            else:
                longitudes.append(None)
                latitudes.append(None)
                counts.append(None)
        
        # store the obtained informations to a dataframe
        location_count_info = pd.DataFrame({"latitude":
                                            latitudes,
                                           "longitude":
                                           longitudes,
                                           "count": counts})
        fig = px.scatter_mapbox(
            # setting of data falame, latitude, and longtitude
            data_frame = location_count_info,
            lat = "latitude",
            lon = "longitude",
            # things to be displayed when hovering over
            hover_name = "count",
            hover_data = ["count"],
            # settings for markers
            opacity = 0.4,
            color = "count",
            color_continuous_scale="Reds",
            # setting for drawing
            center={'lat':34.686567, 'lon':135.52000},
            zoom=4,
            height=600,
            width=800)
        fig.update_layout(mapbox_style='open-street-map')
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.update_layout(title_text="spatial locations of the sensors")
        fig.show()