#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
#read data from datasets
ALL=pd.read_csv('./datasets/vehicle_stops_2016_datasd.csv')      
data=pd.DataFrame({'stop_id':ALL['stop_id'],'subject_race':ALL['subject_race'],'timestamp':ALL['timestamp'],'arrested':ALL['arrested']});
race=list(data['subject_race'])
race=list(set(race))                        #get all the races
arrest=data[(data['arrested']=='Y')]
race_arrestdata=list(arrest['subject_race'])
race_num=[]                                 #this is the arrested population of each race
for i in race:
    race_num.append(race_arrestdata.count(i))
racenum_arrest=dict(zip(race,race_num))
arrest_pie=racenum_arrest.copy()
del arrest_pie[race[0]]
del arrest_pie['X']

i=0;
for k in arrest_pie.copy():
    if arrest_pie[k]<50:
        i=i+arrest_pie[k];
        del arrest_pie[k];
arrest_pie['other']=i                     # here we get the data we need to creat a pie chart of race distribution
labels=['HISPANIC','WHITE','BLACK','OTHER']
sizes=list(arrest_pie.values())


# In[5]:


import numpy as np
race=list(data['subject_race'])
race=list(set(race))
arrest_bar=racenum_arrest.copy()
del arrest_bar[race[0]]
del arrest_bar['X']
race_ele=race
race_ele.remove(race_ele[0])
race_ele.remove('X')
#derive the population who were not arrested
race=list(data['subject_race'])
race_pop=[]
for i in race_ele:
    race_pop.append(race.count(i))
race_pop_uarre=[race_pop[i]-list(arrest_bar.values())[i] for i in range(0,len(race_pop))]
race_list=list(arrest_bar.keys());
name_list=['CHINESE','ASIAN INDIAN','BLACK','KOREAN','PACIFIC ISLANDER','VIETNAMESE','SAMOAN','INDIAN','OTHER ASIAN','OTHER','CAMBODIAN','GUAMANIAN','HISPANIC','WHITE','LAOTIAN','JAPANESE','FILIPINO','HAWAIIAN']


#calculate the percentage of arrested in each race
race_perc_uarre=[(race_pop[i]-list(arrest_bar.values())[i])*100/race_pop[i] for i in range(0,len(race_pop))]
race_perc_arre=[list(arrest_bar.values())[i]*100/race_pop[i] for i in range(0,len(race_pop))]



idx = np.arange(len(name_list))


# In[ ]:




