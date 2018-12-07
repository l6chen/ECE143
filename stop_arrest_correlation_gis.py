import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas

pd.options.display.max_rows = 10

## TODO: Docstrings

# To do : encapsulate functions to do:
# gather arrest and stop data
# combine that data with location

def create_data():
    divisions = geopandas.read_file("zip://./datasets/pd_divisions_datasd.zip")
    beats = geopandas.read_file("zip://./datasets/pd_beats_datasd.zip")

    df = pd.read_csv('./datasets/vehicle_stops_2016_datasd_original.csv')

    #Clean the values
    stops_raw = df[['arrested','service_area']].dropna()
    arrest_values = ['Y', 'N']
    stops_raw2 = stops_raw.loc[stops_raw['arrested'].isin(arrest_values)]
    stops_raw3 = stops_raw2.loc[stops_raw2['service_area'] != 'Unknown']

    # Amount of stops per service area
    stop_count = stops_raw3.groupby('service_area').count()

    # Amount of arrests per service area
    arrested_final_count = stops_raw3.loc[stops_raw3['arrested'] == 'Y'].groupby('service_area').count()

    # Amount of stops without arrests per service area
    not_arrested_final_count = stops_raw3.loc[stops_raw3['arrested'] == 'N'].groupby('service_area').count()

    # Probability of arrest per service area
    probability_of_arrest = (arrested_final_count/stop_count).fillna(0)

    # Build the beats datafram to merge and get the divisions
    beats2 = beats[['div', 'serv']]
    # Only care about one appearance of each serv
    grouped = beats2.groupby('serv').first()
    beats3 = grouped[['div']]

    # Clean the indeces and the datatypes
    stop_count = stop_count.reset_index()
    probability_of_arrest = probability_of_arrest.reset_index()
    beats3 = beats3.reset_index()
    stop_count['service_area'] = stop_count['service_area'].astype(int)
    probability_of_arrest['service_area'] = probability_of_arrest['service_area'].astype(int)
    beats3['serv'] = beats3['serv'].astype(int)

    # Join beats and df
    stopped_by_area = beats3.join(stop_count.set_index('service_area'), on='serv').dropna()
    stopped_by_area[['arrested']] = stopped_by_area[['arrested']].fillna(0).astype(int)

    # Join divisions and df
    stopped_by_area = stopped_by_area.groupby('div').sum()['arrested']
    divsums_stop = divisions.join(stopped_by_area, on='div_num')

    # Repeat the same process as above, but with probability of arrest
    arrested_prob_by_area = beats3.join(probability_of_arrest.set_index('service_area'), on='serv').dropna()
    arrested_prob_by_area[['arrested']] = arrested_prob_by_area[['arrested']].fillna(0)

    arrested_prob_by_area = arrested_prob_by_area.groupby('div').sum()['arrested']
    divsums_arrest = divisions.join(arrested_prob_by_area, on='div_num')

    return divsums_stop, divsums_arrest

def plot_stop_map():
    divsums_stop, divsums_arrest = create_data()
    ax = divsums_stop.plot(column='arrested', figsize=(30, 12), cmap='OrRd', legend=True)
    divsums_stop.apply(lambda x: ax.annotate(s=x.div_name.capitalize(), xy=x.geometry.centroid.coords[0], ha='center'),axis=1)
    ax.set_axis_off()
    

def plot_arrest_map():
    divsums_stop, divsums_arrest = create_data()
    ax = divsums_arrest.plot(column='arrested', figsize=(30, 12), cmap='OrRd', legend=True)
    divsums_stop.apply(lambda x: ax.annotate(s=x.div_name.capitalize(), xy=x.geometry.centroid.coords[0], ha='center'),axis=1)
    ax.set_axis_off()

if (__name__ == "__main__"):
    plot_stop_map()
    plot_arrest_map()
