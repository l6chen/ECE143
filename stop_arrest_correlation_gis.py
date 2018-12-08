# Author: Raul Pegan

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas

pd.options.display.max_rows = 10

divisions_df = geopandas.read_file("zip://./datasets/pd_divisions_datasd.zip")
beats_df = geopandas.read_file("zip://./datasets/pd_beats_datasd.zip")
stops_df = pd.read_csv('./datasets/vehicle_stops_2016_datasd_original.csv')

def create_arrest_data(): 
    '''
    Clean up the dataframe data and return a geopandas formatted df ready to be plotted.
    Utilizes the global dfs
    Returns the geopandas df for the arrest data
 
    :returns: geopandas df
    '''
    # Cleanup data
    stops = clean_stops(stops_df)
    
    # Build counts   
    # Amount of stops per service area
    stop_count = stops.groupby('service_area').count()

    # Amount of arrests per service area
    arrested_final_count = stops.loc[stops['arrested'] == 'Y'].groupby('service_area').count()

    # Probability of arrest per service area
    probability_of_arrest = (arrested_final_count/stop_count).fillna(0)
  
    # Build beats    
    beats = build_beats(beats_df)
    
    # Build divsums
    divsums_arrest = get_divsums(beats, probability_of_arrest, divisions_df)

    return divsums_arrest

def create_stop_data():
    '''
    Clean up the dataframe data and return a geopandas formatted df ready to be plotted.
    Utilizes the global dfs
    Returns the geopandas df for the stop data
 
    :returns: geopandas df
    '''
    # Cleanup data
    stops = clean_stops(stops_df)
    
    # Build counts
    # Amount of stops per service area
    stop_count = stops.groupby('service_area').count()
  
    # Build beats
    beats = build_beats(beats_df)
    
    # Build divsums
    divsums_stop = get_divsums(beats, stop_count, divisions_df)

    return divsums_stop


def clean_stops(in_stops_df):
    '''
    Clean up the stops dataframe data.
    Utilizes the global dfs

    :param in_stops_df: the stops df
    :type in_stops_df: pandas df
    :returns: pandas df
    '''
    stops_raw = in_stops_df[['arrested','service_area']].dropna()
    arrest_values = ['Y', 'N']
    stops_raw = stops_raw.loc[stops_raw['arrested'].isin(arrest_values)]
    stops_raw = stops_raw.loc[stops_raw['service_area'] != 'Unknown']

    return stops_raw


def build_beats(in_beats):
    '''
    Build up the beats dataframe data.
    Utilizes the global dfs

    :param in_beats: the beats df
    :type in_beats: pandas df
    :returns: pandas df
    '''
    # Build the beats dataframe to merge and get the divisions
    beats = in_beats[['div', 'serv']]
    # Only care about one appearance of each serv
    beats = beats.groupby('serv').first()
    beats = beats[['div']]

    # Clean the indeces and the datatypes
    beats = beats.reset_index()
    beats['serv'] = beats['serv'].astype(int)
    
    return beats

def get_divsums(beats, count, divisions):
    '''
    Return the geopandas dataframe combining the geometric specification from beats and the count per location
    specified in count
    
    :param beats: the location df, by police beats
    :type beats: pandas df
    :param count: pandas df containing all the records we wish to correlate to the beats
    :type count: pandas df
    :param divisions: filename for source text
    :type divisions: geopandas df
    :returns: geopandas df
    '''
    # Clean up the count data
    clean_count = count.reset_index()
    clean_count['service_area'] = clean_count['service_area'].astype(int)
   
    # Join beats and df
    count_by_area = beats.join(clean_count.set_index('service_area'), on='serv').dropna()
    count_by_area[['arrested']] = count_by_area[['arrested']].fillna(0)
    
    # Join divisions and df
    count_by_area = count_by_area.groupby('div').sum()['arrested']
    return divisions.join(count_by_area, on='div_num')
    
def plot_map(in_geodf):
    '''
    Plot geopandas dataframe containing the relevant count information provided from in_geopdf
    
    :param in_geopdf: the geopandas df containing our map and count data
    :type in_geopdf: geopandas df
    '''
    ax = in_geodf.plot(column='arrested', figsize=(30, 12), cmap='OrRd', legend=True)
    in_geodf.apply(lambda x: ax.annotate(s=x.div_name.capitalize(), xy=x.geometry.centroid.coords[0], ha='center'),axis=1)
    ax.set_axis_off()
    

if (__name__ == "__main__"):
    divsums_stop = create_stop_data()
    plot_map(divsums_stop)
    divsums_arrest = create_arrest_data()
    plot_map(divsums_arrest)
    